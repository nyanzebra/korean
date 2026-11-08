import sys
W = '/home/robert/Documents/GitHub/korean/단어/추상적인 것/.tmpwork'
sys.path.insert(0, W)
exec(open(W + '/' + sys.argv[1], encoding='utf-8').read())
