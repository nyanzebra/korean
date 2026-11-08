exec(open(W + '/b5.py', encoding='utf-8').read())
import collections

# ---------- validation ----------
heads = collections.defaultdict(list)
for rel, fm in final.items():
    for c in fm.cards:
        heads[c.word].append(rel)
        if not c.meaning: print('EMPTY MEANING', rel, c.word)
        if not c.examples: print('EMPTY EXAMPLES', rel, c.word)
        for ko, en in c.examples:
            if not en and HANGUL.search(ko):
                print('NO EN', rel, c.word, ko)
            if not HANGUL.search(ko): print('NO KO', rel, c.word, ko)
for w, rs in heads.items():
    if len(rs) > 1: print('DUP', w, rs)
print('TOTAL CARDS', sum(len(fm.cards) for fm in final.values()), 'FILLED', FILLED, 'BEFORE', BEFORE_CARDS)

if os.path.exists(OUT): shutil.rmtree(OUT)
for rel, fm in final.items():
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(emit_file(fm))
