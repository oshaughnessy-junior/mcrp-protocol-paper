"""A deliberately closed SRR subset and RO-Crate 1.2 transport demonstration."""
import copy
import hashlib
import json
import re
from datetime import date
from pathlib import Path

BASE='https://w3id.org/ro/crate/1.2'
NS='https://example.org/mcrp/toy-crosswalk/0.1#'
CONTEXT=[BASE+'/context',{'mcrp':NS}]
PROFILE='profile.html'
LICENSE='https://creativecommons.org/licenses/by/4.0/'
RELATIONS={'derives','requires-evidence','requires-authority','requires-freshness','contextualizes','contradicts'}


def keys(obj,expected):
    if type(obj) is not dict or set(obj)!=set(expected.split()):
        raise ValueError('missing or unknown fields; unsupported data must not vanish')


def text(value):
    if not isinstance(value,str) or not value.strip():raise ValueError('nonempty string required')


def ref(value):return {'@id':value}


def validate_srr(srr):
    keys(srr,'release title description date license artifacts claims decisions edges')
    for k in ('release','title','description','date','license'):text(srr[k])
    date.fromisoformat(srr['date'])
    if srr['license']!=LICENSE:raise ValueError('fixture profile supports CC BY 4.0 only')
    for k in ('artifacts','claims','decisions','edges'):
        if type(srr[k]) is not list:raise ValueError('list required')
    if not srr['artifacts'] or not srr['claims']:raise ValueError('nonempty artifact and claim sets required')
    ids={'./','ro-crate-metadata.json',PROFILE,LICENSE}; artifacts=set(); claims=set()
    for a in srr['artifacts']:
        keys(a,'id name sha256 media_type bytes')
        if not isinstance(a['id'],str) or not re.fullmatch(r'payload/[A-Za-z0-9_-]+\.[A-Za-z0-9]+',a['id']):raise ValueError('unsupported artifact path')
        if not isinstance(a['sha256'],str) or not re.fullmatch('[0-9a-f]{64}',a['sha256']):raise ValueError('SHA256 required')
        if type(a['bytes']) is not int or a['bytes']<0:raise ValueError('nonnegative byte count required')
        text(a['name']);text(a['media_type'])
        if a['id'] in ids:raise ValueError('duplicate ID')
        ids.add(a['id']);artifacts.add(a['id'])
    for c in srr['claims']:
        keys(c,'id text scope requires')
        if not isinstance(c['id'],str) or not re.fullmatch('#claim-[A-Za-z0-9_-]+',c['id']):raise ValueError('unsupported claim ID')
        text(c['text']);text(c['scope'])
        if c['id'] in ids:raise ValueError('duplicate ID')
        ids.add(c['id']);claims.add(c['id'])
    for c in srr['claims']:
        if type(c['requires']) is not list or any(not isinstance(v,str) for v in c['requires']) or len(set(c['requires']))!=len(c['requires']) or not set(c['requires'])<=artifacts|claims:raise ValueError('unresolved or duplicate requirement')
    for d in srr['decisions']:
        keys(d,'id claim actor outcome policy valid_until')
        if not isinstance(d['id'],str) or not re.fullmatch('#decision-[A-Za-z0-9_-]+',d['id']):raise ValueError('unsupported decision ID')
        if d['id'] in ids or d['claim'] not in claims:raise ValueError('duplicate decision or unresolved claim')
        ids.add(d['id']);text(d['actor']);text(d['policy'])
        if d['outcome'] not in ('pending','approved','rejected'):raise ValueError('unsupported disposition')
        if type(d['valid_until']) is not int or d['valid_until']<0:raise ValueError('synthetic validity tick required')
    known=artifacts|claims|{d['id'] for d in srr['decisions']}
    seen=set()
    for e in srr['edges']:
        keys(e,'source target kind')
        if e['source'] not in known or e['target'] not in known or e['kind'] not in RELATIONS:raise ValueError('unsupported or unresolved edge')
        t=tuple(e[k] for k in ('source','target','kind'))
        if t in seen:raise ValueError('duplicate edge')
        seen.add(t)
    return srr


def export_srr(srr):
    validate_srr(srr)
    graph=[{'@id':'ro-crate-metadata.json','@type':'CreativeWork','about':ref('./'),'conformsTo':ref(BASE)},
           {'@id':'./','@type':'Dataset','name':srr['title'],'description':srr['description'],
            'datePublished':srr['date'],'license':ref(srr['license']),'conformsTo':ref(PROFILE),
            'hasPart':[ref(a['id']) for a in srr['artifacts']]+[ref(PROFILE)],
            'mcrp:releaseIdentity':srr['release'],
            'mcrp:claims':[ref(c['id']) for c in srr['claims']],
            'mcrp:decisions':[ref(d['id']) for d in srr['decisions']],
            'mcrp:edges':[ref('#edge-'+str(i)) for i in range(len(srr['edges']))]},
           {'@id':LICENSE,'@type':'CreativeWork','name':'CC BY 4.0','description':'Attribution 4.0 International; synthetic fixture metadata and payload.'},
           {'@id':PROFILE,'@type':['File','CreativeWork','Profile'],'name':'Local MCRP crosswalk transport profile 0.1',
            'description':'Bounded example profile; not an endorsed or registered standard.','version':'0.1','encodingFormat':'text/html'}]
    for a in srr['artifacts']:
        graph.append({'@id':a['id'],'@type':'File','name':a['name'],'encodingFormat':a['media_type'],
                      'contentSize':str(a['bytes']),'mcrp:sha256':a['sha256']})
    for c in srr['claims']:
        graph.append({'@id':c['id'],'@type':['CreativeWork','mcrp:Claim'],'name':c['id'],
                      'text':c['text'],'mcrp:scope':c['scope'],'mcrp:requires':[ref(v) for v in c['requires']]})
    for d in srr['decisions']:
        graph.append({'@id':d['id'],'@type':['CreativeWork','mcrp:Decision'],'name':d['id'],
                      'about':ref(d['claim']),'mcrp:actor':d['actor'],'mcrp:outcome':d['outcome'],
                      'mcrp:policy':d['policy'],'mcrp:validUntil':d['valid_until']})
    for i,e in enumerate(srr['edges']):
        graph.append({'@id':'#edge-'+str(i),'@type':['CreativeWork','mcrp:Edge'],'name':'Declared '+e['kind']+' edge',
                      'mcrp:source':ref(e['source']),'mcrp:target':ref(e['target']),'mcrp:kind':e['kind']})
    return {'@context':copy.deepcopy(CONTEXT),'@graph':graph}


def import_crate(crate):
    """Strict profile-aware inverse, not a general JSON-LD or RO-Crate importer."""
    keys(crate,'@context @graph')
    if crate['@context']!=CONTEXT or type(crate['@graph']) is not list:raise ValueError('unsupported context or graph')
    try:
        nodes={}
        for node in crate['@graph']:
            if type(node) is not dict or node['@id'] in nodes:raise ValueError('duplicate/invalid entity')
            nodes[node['@id']]=node
        root=nodes['./']
        def targets(field):
            values=root[field]
            if type(values) is not list:raise ValueError('array required')
            for value in values:keys(value,'@id')
            return [nodes[v['@id']] for v in values]
        artifacts=targets('hasPart')
        claims=targets('mcrp:claims'); decisions=targets('mcrp:decisions'); edges=targets('mcrp:edges')
        srr={'release':root['mcrp:releaseIdentity'],'title':root['name'],'description':root['description'],
             'date':root['datePublished'],'license':root['license']['@id'],
             'artifacts':[{'id':a['@id'],'name':a['name'],'sha256':a['mcrp:sha256'],
                           'media_type':a['encodingFormat'],'bytes':int(a['contentSize'])} for a in artifacts if a['@id']!=PROFILE],
             'claims':[{'id':c['@id'],'text':c['text'],'scope':c['mcrp:scope'],
                        'requires':[v['@id'] for v in c['mcrp:requires']]} for c in claims],
             'decisions':[{'id':d['@id'],'claim':d['about']['@id'],'actor':d['mcrp:actor'],
                           'outcome':d['mcrp:outcome'],'policy':d['mcrp:policy'],'valid_until':d['mcrp:validUntil']} for d in decisions],
             'edges':[{'source':e['mcrp:source']['@id'],'target':e['mcrp:target']['@id'],'kind':e['mcrp:kind']} for e in edges]}
        # Closed subset: every entity/property must be accounted for, not dropped.
        expected={n['@id']:n for n in export_srr(srr)['@graph']}
        if expected!=nodes:raise ValueError('unknown, changed, or unsupported profile fields')
        return srr
    except (KeyError,TypeError,ValueError,OverflowError) as exc:
        raise ValueError('not a supported lossless profile instance: '+str(exc)) from exc


def generic_projection(crate):
    """Show exactly what a deliberately extension-unaware consumer discards."""
    import_crate(crate)
    projected=copy.deepcopy(crate); projected['@context']=BASE+'/context'; losses=[]
    for node in projected['@graph']:
        for key in tuple(node):
            if key.startswith('mcrp:'):
                losses.append(node['@id']+'/'+key);del node[key]
        if type(node.get('@type')) is list:
            removed=[t for t in node['@type'] if t.startswith('mcrp:')]
            if removed:losses.append(node['@id']+'/@type:'+','.join(removed))
            node['@type']=[t for t in node['@type'] if not t.startswith('mcrp:')]
    root=next(n for n in projected['@graph'] if n['@id']=='./')
    del root['conformsTo'];losses.append('./conformsTo:local-profile-claim-withdrawn')
    return projected,{'discarded_paths':losses,'semantic_result':'No MCRP reliance, authority, scope, digest, or invalidation semantics preserved by this consumer.'}


def verify_payloads(crate,directory):
    srr=import_crate(crate)
    base=Path(directory).resolve()
    for a in srr['artifacts']:
        path=(base/a['id']).resolve()
        if base not in path.parents:raise ValueError('payload escapes crate directory')
        data=path.read_bytes()
        if len(data)!=a['bytes'] or hashlib.sha256(data).hexdigest()!=a['sha256']:raise ValueError('payload mismatch')
    if not (base/PROFILE).is_file():raise ValueError('local profile description missing')
    return True


def fixture():
    data=b'1.0\n2.0\n3.0\n'
    srr={'release':'srr:synthetic-crosswalk-v1','title':'Synthetic scoped-claim example',
         'description':'A transport fixture, not verified scientific evidence.','date':'2026-09-25','license':LICENSE,
         'artifacts':[{'id':'payload/input.txt','name':'Toy numbers','sha256':hashlib.sha256(data).hexdigest(),'media_type':'text/plain','bytes':len(data)}],
         'claims':[{'id':'#claim-mean','text':'The fixture mean is 2.0','scope':'These three synthetic values only','requires':['payload/input.txt']}],
         'decisions':[{'id':'#decision-review','claim':'#claim-mean','actor':'declared-reviewer','outcome':'pending','policy':'toy-policy-v1','valid_until':20}],
         'edges':[{'source':'payload/input.txt','target':'#claim-mean','kind':'requires-evidence'},
                  {'source':'#claim-mean','target':'#decision-review','kind':'requires-evidence'}]}
    return srr,{'payload/input.txt':data}

if __name__=='__main__':
    here=Path(__file__).parent; out=here/'example-crate';out.mkdir(exist_ok=True)
    srr,payloads=fixture();crate=export_srr(srr)
    for name,data in payloads.items():
        path=out/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
    (out/PROFILE).write_text((here/PROFILE).read_text())
    (out/'ro-crate-metadata.json').write_text(json.dumps(crate,indent=2)+'\n')
    (here/'srr-input.json').write_text(json.dumps(srr,indent=2)+'\n')
    projection,loss=generic_projection(crate)
    (here/'extension-unaware-projection.json').write_text(json.dumps(projection,indent=2)+'\n')
    (here/'loss-manifest.json').write_text(json.dumps(loss,indent=2)+'\n')
    result={'self_roundtrip_equal':import_crate(crate)==srr,'payload_hashes_match':verify_payloads(crate,out),
            'entity_count':len(crate['@graph']),'unaware_consumer_loss_paths':len(loss['discarded_paths']),
            'external_validator':'not run','independent_consumer':'not tested','standard_target':BASE}
    (here/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
