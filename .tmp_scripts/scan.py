import sys, glob, os
sys.path.insert(0, '/home/robert/Documents/GitHub/korean/.tmp_scripts')
from lib import *

files = sys.argv[1:]
for rel in files:
    pre, cards = load(rel)
    print('==', rel, len(cards), 'cards; pre=', repr(pre[:60]))
    report(rel, cards)
