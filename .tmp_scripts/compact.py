import sys
sys.path.insert(0,'/home/robert/Documents/GitHub/korean/.tmp_scripts')
from lib import *
pre,cards=load(sys.argv[1])
if pre: print('PRE:',pre[:200].replace('\n',' / '))
for i,c in enumerate(cards):
    tg=' '.join(t for t in c.tags if t!='#card')
    ex='; '.join(k+' => '+' '.join(e) for k,e in c.examples)
    sr=c.sr[7:-3] if c.sr else ''
    nt=(' NOTES: '+' / '.join(c.notes)) if c.notes else ''
    print(f"{i}. {c.title} [{tg}] {{{'; '.join(c.meanings)}}} EX: {ex}{nt} {sr}")
