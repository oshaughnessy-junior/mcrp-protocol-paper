#!/usr/bin/env python3
"""Render manuscript with Pandoc and the optional Typst Python package.

Run with a Python environment containing typst, and pandoc on PATH.
This creates a .typ intermediate and PDF; it does not upload either file.
"""
import argparse
from pathlib import Path
import re
import subprocess
import typst

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--edition', default='September 2026 - revision responding to aiXiv review1587')
args = parser.parse_args()
output = args.output.resolve()
output.parent.mkdir(parents=True, exist_ok=True)
source = output.with_suffix('.typ')
subprocess.run([
    'pandoc', str(root/'paper/position-paper.md'), '-f', 'markdown', '-t', 'typst',
    '-s', '--citeproc', '--bibliography', str(root/'paper/refs.bib'),
    '-M', 'title=MCRP: A Prospective, Claim-Versioned Verification Lifecycle for Computational Research',
    '-M', 'author=Codex (AI) and junior (AI)', '-M', 'date='+args.edition,
    '-V', 'papersize=us-letter', '-V', 'fontsize=9.7pt', '-o', str(source)
], check=True)
s = source.read_text()
s = re.sub(r'\bsect\b', '∩', s) # Pandoc output compatibility with Typst 0.15.
s = s.replace('margin: (x: 1.25in, y: 1.25in)', 'margin: (x: 0.8in, y: 0.8in)')
s = s.replace('columns: (25%, 25%, 25%, 25%),', 'columns: (18%, 27%, 16%, 39%),', 1)
s = s.replace('columns: (25%, 25%, 25%, 25%),', 'columns: (14%, 28%, 29%, 29%),', 1)
s = re.sub(r'columns: \((?:\d+(?:\.\d+)?%, ){5}\d+(?:\.\d+)?%\),',
           'columns: (30%, 7%, 42%, 7%, 7%, 7%),', s)
s = s.replace('align: (auto,right,auto,auto,auto,auto,),',
              'align: (left,center,left,center,center,center,),')
s = s.replace('[First required level]', '[Level]')
s = s.replace('columns: (50%, 50%),', 'columns: (20%, 80%),')
s = re.sub(r'align: \((?:auto,)+\),', lambda m: m.group().replace('auto','left'), s)
s = s.replace('  set heading(numbering: sectionnumbering)',
              '  show table: it => { set par(justify: false); set text(size: 9pt); it }\n'
              '  set heading(numbering: sectionnumbering)')
source.write_text(s)
typst.compile(str(source), output=str(output), root=str(output.parent))
print(output)
