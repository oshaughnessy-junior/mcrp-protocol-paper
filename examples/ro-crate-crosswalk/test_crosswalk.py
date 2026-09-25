import copy
import tempfile
import unittest
from pathlib import Path
from crosswalk import BASE,CONTEXT,PROFILE,export_srr,import_crate,generic_projection,verify_payloads,fixture

class Crosswalk(unittest.TestCase):
    def setUp(self):self.srr,self.payloads=fixture();self.crate=export_srr(self.srr)
    def node(self,id):return next(n for n in self.crate['@graph'] if n['@id']==id)
    def test_exact_subset_roundtrip(self):self.assertEqual(import_crate(self.crate),self.srr)
    def test_ro_crate_root_shape_independent(self):
        # Checks derived directly from the official descriptor/root requirements.
        self.assertEqual(self.crate['@context'],CONTEXT)
        meta=self.node('ro-crate-metadata.json');root=self.node(meta['about']['@id'])
        self.assertEqual(meta['@type'],'CreativeWork');self.assertEqual(meta['conformsTo'],{'@id':BASE})
        self.assertEqual(root['@type'],'Dataset')
        for key in ('name','description','datePublished','license'):self.assertIn(key,root)
        for node in self.crate['@graph']:self.assertIn('@id',node);self.assertIn('@type',node)
    def test_graph_order_does_not_matter(self):
        self.crate['@graph'].reverse();self.assertEqual(import_crate(self.crate),self.srr)
    def test_critical_semantics_preserved(self):
        self.srr['claims'][0]['scope']='Narrowed scope';self.srr['decisions'][0]['outcome']='rejected'
        self.srr['decisions'][0]['valid_until']=0
        self.assertEqual(import_crate(export_srr(self.srr)),self.srr)
    def test_unknown_srr_fields_rejected(self):
        for obj in (self.srr,self.srr['claims'][0],self.srr['decisions'][0],self.srr['artifacts'][0],self.srr['edges'][0]):
            obj['unmapped-important-field']='must survive'
            with self.assertRaises(ValueError):export_srr(self.srr)
            del obj['unmapped-important-field']
    def test_unknown_crate_fields_rejected(self):
        for node in self.crate['@graph']:
            node['mcrp:unknown']='hidden-state'
            with self.assertRaises(ValueError):import_crate(self.crate)
            del node['mcrp:unknown']
    def test_stripped_scope_and_extension_context_rejected(self):
        del self.node('#claim-mean')['mcrp:scope']
        with self.assertRaises(ValueError):import_crate(self.crate)
        self.crate=export_srr(self.srr);self.crate['@context']=BASE+'/context'
        with self.assertRaises(ValueError):import_crate(self.crate)
    def test_duplicate_entity_and_unknown_entity_rejected(self):
        self.crate['@graph'].append(copy.deepcopy(self.crate['@graph'][0]))
        with self.assertRaises(ValueError):import_crate(self.crate)
        self.crate=export_srr(self.srr);self.crate['@graph'].append({'@id':'#alien','@type':'Thing'})
        with self.assertRaises(ValueError):import_crate(self.crate)
    def test_dangling_reference_rejected(self):
        self.node('#claim-mean')['mcrp:requires']=[{'@id':'#absent'}]
        with self.assertRaises(ValueError):import_crate(self.crate)
    def test_changed_descriptor_and_flattening_rejected(self):
        self.node('ro-crate-metadata.json')['about']={'@id':'#claim-mean'}
        with self.assertRaises(ValueError):import_crate(self.crate)
        self.crate=export_srr(self.srr);self.node('#claim-mean')['mcrp:requires']=[{'@id':'payload/input.txt','name':'nested entity'}]
        with self.assertRaises(ValueError):import_crate(self.crate)
    def test_extension_unaware_loss_is_explicit(self):
        projection,loss=generic_projection(self.crate)
        self.assertIn('#claim-mean/mcrp:scope',loss['discarded_paths'])
        self.assertIn('#decision-review/mcrp:outcome',loss['discarded_paths'])
        self.assertNotIn('conformsTo',next(n for n in projection['@graph'] if n['@id']=='./'))
        with self.assertRaises(ValueError):import_crate(projection)
    def test_payload_bytes_verified_and_tamper_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'payload').mkdir();(root/PROFILE).write_text('local profile description')
            for path,data in self.payloads.items():(root/path).write_bytes(data)
            self.assertTrue(verify_payloads(self.crate,root))
            (root/'payload/input.txt').write_text('4.0\n')
            with self.assertRaises(ValueError):verify_payloads(self.crate,root)
    def test_bad_path_digest_type_and_missing_profile(self):
        for field,value in (('id','../secret.txt'),('sha256','not-a-digest'),('bytes',True)):
            source=copy.deepcopy(self.srr);source['artifacts'][0][field]=value
            with self.assertRaises(ValueError):export_srr(source)
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'payload').mkdir()
            for path,data in self.payloads.items():(root/path).write_bytes(data)
            with self.assertRaises(ValueError):verify_payloads(self.crate,root)
    def test_inputs_not_mutated(self):
        old=copy.deepcopy(self.crate);generic_projection(self.crate);import_crate(self.crate)
        self.assertEqual(self.crate,old)

if __name__=='__main__':unittest.main()
