import sys, os, re, copy, shutil
sys.path.insert(0, W)
from lib import *

R = '/home/robert/Documents/GitHub/korean/단어/추상적인 것'
OUT = '/tmp/work/out'

# ---------- load ----------
RAW_PATCH = {
    '감정_심리/감정.md': [
        ('## ### 그리워하다', '## 그리워하다'),
    ],
    '개념_추상/것.md': [
        ('\n\n## 무가치 #card', '\n?end\n\n## 무가치 #card'),
    ],
}
F = {}
for dp, dn, fn in os.walk(R):
    dn[:] = [d for d in dn if not d.startswith('.')]
    for f in sorted(fn):
        if not f.endswith('.md'): continue
        if f == 'Index.md' or f == '완료_및_완성.md': continue
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, R)
        txt = open(p, encoding='utf-8').read().lstrip('\ufeff')
        txt = txt.replace('\u00a0', ' ').replace('\u200b', '').replace('\u2028','\n')
        txt = re.sub(r'\?end(?=\S)[^\n]*', '?end', txt)
        for a, b in RAW_PATCH.get(rel, []):
            assert a in txt, (rel, a)
            txt = txt.replace(a, b)
        if rel == '감정_심리/감정.md':
            pat = re.compile(r'\?end\n- 그는 기뻐서 얼굴이 발그레하다\n\t- His face is flushed with joy\.\n(<!--SR:[^\n]*-->)\n\?end')
            assert pat.search(txt)
            txt = pat.sub(lambda m: '?end\n\n## 발그레하다 #card\n?begin\n### 뜻\n- to be flushed\n- to be rosy\n### 예\n- 그는 기뻐서 얼굴이 발그레하다\n\t- His face is flushed with joy.\n' + m.group(1) + '\n?end', txt)
        F[rel] = parse_file(p, txt)
# BEFORE counts
BEFORE_CARDS = sum(len(fm.cards) for fm in F.values()) + 0
D = {}      # destination files: rel -> FileModel
def dst(rel):
    if rel not in D:
        D[rel] = FileModel()
    return D[rel]

def find(rel, word, remove=True):
    res = [c for c in F[rel].cards if c.word == word]
    if not res: raise KeyError((rel, word))
    if remove:
        F[rel].cards = [c for c in F[rel].cards if c.word != word]
    return res

def move(src, word, dest, one=True):
    cs = find(src, word)
    assert len(cs) == 1, (src, word, len(cs))
    dst(dest).cards.append(cs[0])
    return cs[0]

def addto(dest, card):
    dst(dest).cards.append(card)

def C(word, meaning, examples, tags='', notes=None, sr=None, tagline=None):
    c = Card(word, (' ' + tags) if tags and not tags.startswith(' ') else tags)
    c.meaning = list(meaning)
    c.examples = [[ko, [en] if en else []] for ko, en in examples]
    c.notes = list(notes or [])
    c.sr = sr
    c.tagline = list(tagline or [])
    return c

def get(rel, word):
    res = [c for c in D[rel].cards if c.word == word]
    assert len(res) == 1, (rel, word, len(res))
    return res[0]

def setex(c, exs):
    c.examples = [[ko, [en] if en else []] for ko, en in exs]

def addex(c, exs):
    for ko, en in exs:
        c.examples.append([ko, [en] if en else []])

def setmean(c, m): c.meaning = list(m)
def setnotes(c, n): c.notes = list(n)
def addnotes(c, n):
    for x in n:
        if x not in c.notes: c.notes.append(x)

def rep(c, old, new, allow_missing=False):
    hit = 0
    def r(s):
        nonlocal hit
        if old in s: hit += 1
        return s.replace(old, new)
    c.meaning = [r(x) for x in c.meaning]
    c.examples = [[r(ko), [r(e) for e in en]] for ko, en in c.examples]
    c.notes = [r(x) for x in c.notes]
    if hit == 0 and not allow_missing:
        raise Exception('rep not found: %s %r' % (c.word, old))

def delex(c, ko_sub):
    n = len(c.examples)
    c.examples = [e for e in c.examples if ko_sub not in e[0]]
    assert len(c.examples) < n, (c.word, ko_sub)

def swap_ex(c, idx):
    ko, en = c.examples[idx]
    assert len(en) == 1
    c.examples[idx] = [en[0], [ko]]
