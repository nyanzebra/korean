import sys
sys.path.insert(0,'/home/robert/Documents/GitHub/korean/.tmp_scripts')
from lib import *
pre,cards=load(sys.argv[1])
for i,c in enumerate(cards):
    print(i, c.title, ' '.join(t for t in c.tags if t!='#card'), 'SR' if c.sr else '', '|', '; '.join(c.meanings)[:40])
