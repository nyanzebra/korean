import os, re, copy

HANGUL = re.compile(r'[\uac00-\ud7a3]')
SR_RE = re.compile(r'<!--SR:!(\d{4}-\d{2}-\d{2}),(\d+),(\d+)-->')

class Card:
    def __init__(self, word, tags=''):
        self.word = word
        self.tags = tags          # e.g. ' #sogang #sogang-4A' (after #card)
        self.meaning = []
        self.examples = []        # list of [ko, [en,...]]
        self.notes = []
        self.tagline = []         # lines under ### Tags
        self.sr = None
        self.src = ''
    def interval(self):
        if not self.sr: return -1
        return int(SR_RE.match(self.sr).group(2))

class FileModel:
    def __init__(self):
        self.pre = []
        self.cards = []
        self.post = []

def norm_indent(line):
    m = re.match(r'^([ \t]*)(.*)$', line)
    ws, rest = m.group(1), m.group(2)
    if rest.startswith('* '): rest = '- ' + rest[2:]
    return (1 if ws else 0), rest

def parse_card_body(card, lines):
    sec = None
    raw = {'뜻': [], '예': [], 'Notes': [], 'Tags': []}
    for ln in lines:
        s = ln.strip()
        if s == '' : continue
        if s == '?begin': continue
        m = SR_RE.search(s)
        if m and s.startswith('<!--SR'):
            card.sr = s; continue
        m = re.match(r'^###\s+(.*)$', s)
        if m:
            name = m.group(1).strip()
            if name == 'Note': name = 'Notes'
            if name not in raw: raise Exception('unknown section %r in %s' % (name, card.word))
            sec = name; continue
        if sec is None:
            raise Exception('line before section in %s: %r' % (card.word, ln))
        raw[sec].append(ln.rstrip('\n'))
    # meaning
    for ln in raw['뜻']:
        lvl, rest = norm_indent(ln)
        rest = rest.strip()
        card.meaning.append(rest[2:].strip() if rest.startswith('- ') else rest)
    # examples
    items = []
    for ln in raw['예']:
        lvl, rest = norm_indent(ln)
        rest = rest.strip()
        if rest == '-' : continue
        if rest.startswith('- '): rest = rest[2:].strip()
        elif rest.startswith('-'): rest = rest[1:].strip()
        if lvl == 0 and '\t' in rest:
            ko, en = rest.split('\t', 1)
            items.append((0, ko.strip())); items.append((1, en.strip().lstrip('\t')))
        else:
            items.append((lvl, rest))
    # flat pairs
    if items and all(l == 0 for l, _ in items) and len(items) % 2 == 0:
        ok = all(HANGUL.search(items[i][1]) and not HANGUL.search(items[i+1][1]) for i in range(0, len(items), 2))
        if ok:
            items = [(0 if i % 2 == 0 else 1, t) for i, (_, t) in enumerate(items)]
    cur = None
    for l, t in items:
        if l == 0:
            cur = [t, []]; card.examples.append(cur)
        else:
            if cur is None:
                cur = [t, []]; card.examples.append(cur)
            else:
                cur[1].append(t)
    # notes
    for ln in raw['Notes']:
        lvl, rest = norm_indent(ln)
        rest = rest.strip()
        if rest.startswith('- '):
            card.notes.append(('  ' if lvl else '') + '- ' + rest[2:].strip())
        else:
            card.notes.append('- ' + rest)
    card.tagline = [l.strip() for l in raw['Tags'] if l.strip()]

def parse_file(path, txt=None):
    fm = FileModel()
    if txt is None: txt = open(path, encoding='utf-8').read()
    txt = txt.lstrip('\ufeff')
    lines = txt.split('\n')
    i = 0
    cur = None
    body = []
    while i < len(lines):
        ln = lines[i]
        if cur is None:
            m = re.match(r'^## (.*)#card(.*)$', ln)
            if m:
                cur = Card(m.group(1).strip(), m.group(2).rstrip())
                cur.src = path
                body = []
            else:
                if ln.strip() in ('', '---'):
                    pass
                elif fm.cards:
                    fm.post.append(ln)
                else:
                    fm.pre.append(ln)
        else:
            if ln.strip().startswith('?end'):
                parse_card_body(cur, body)
                fm.cards.append(cur); cur = None
            elif re.match(r'^## ', ln) and '#card' in ln:
                raise Exception('card without ?end in %s: %s' % (path, cur.word))
            else:
                body.append(ln)
        i += 1
    if cur is not None: raise Exception('unterminated card %s %s' % (path, cur.word))
    return fm

def emit_card(c):
    out = ['## %s #card%s' % (c.word, c.tags), '?begin', '### 뜻']
    for m in c.meaning: out.append('- ' + m)
    out.append('')
    out.append('### 예')
    for ko, ens in c.examples:
        out.append('- ' + ko)
        for e in ens: out.append('  - ' + e)
    if c.notes:
        out.append(''); out.append('### Notes')
        out.extend(c.notes)
    if c.tagline:
        out.append(''); out.append('### Tags')
        out.extend(c.tagline)
    if c.sr:
        out.append(''); out.append(c.sr)
    out.append('?end')
    return '\n'.join(out)

def emit_file(fm):
    parts = []
    if fm.pre:
        pre = '\n'.join(fm.pre).strip('\n')
        if pre: parts.append(pre)
    for c in fm.cards: parts.append(emit_card(c))
    if fm.post:
        parts.append('---\n\n' + '\n'.join(fm.post).strip('\n'))
    return '\n\n'.join(parts) + '\n'

def merge_cards(cards, word=None, tags=None):
    base = copy.deepcopy(cards[0])
    for c in cards[1:]:
        for m in c.meaning:
            if m not in base.meaning: base.meaning.append(m)
        keys = {k for k, _ in base.examples}
        for ko, en in c.examples:
            if ko not in keys:
                base.examples.append([ko, list(en)]); keys.add(ko)
        for n in c.notes:
            if n not in base.notes: base.notes.append(n)
        for t in c.tagline:
            if t not in base.tagline: base.tagline.append(t)
        # tags union
        have = base.tags.split()
        for t in c.tags.split():
            if t not in have: have.append(t)
        base.tags = (' ' + ' '.join(have)) if have else ''
        if c.interval() > base.interval(): base.sr = c.sr
    if word: base.word = word
    if tags is not None: base.tags = tags
    return base
