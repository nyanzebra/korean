import sys,os
sys.path.insert(0,'/tmp/work')
from lib import *
R='/home/robert/Documents/GitHub/korean/단어/추상적인 것'
for dp,dn,fn in os.walk(R):
    for f in sorted(fn):
        if f=='Index.md' or f=='완료_및_완성.md': continue
        p=os.path.join(dp,f)
        txt=open(p,encoding='utf-8').read()
        txt=txt.replace('## ### 그리워하다','## 그리워하다').replace('?endTry saying that like you mean it.','?end')
        try:
            fm=parse_file(p,txt)
            print(os.path.relpath(p,R),len(fm.cards),'pre',len(fm.pre),'post',len(fm.post))
        except Exception as e:
            print('ERR',p,e)
