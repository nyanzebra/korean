import re, os, sys

BASE = '/home/robert/Documents/GitHub/korean/단어/'
HANGUL = re.compile(r'[\uac00-\ud7a3\u3130-\u318f]')


class Card:
    def __init__(self):
        self.title = ''
        self.tags = []
        self.meanings = []
        self.examples = []  # list of [kor, eng_list]
        self.notes = []
        self.sr = None
        self.warn = []


def split_heading(h):
    h = h[3:].strip()
    toks = h.split(' ')
    i = len(toks)
    while i > 0 and toks[i - 1].startswith('#'):
        i -= 1
    title = ' '.join(toks[:i]).strip()
    tags = toks[i:]
    return title, tags


def clean_bullet(s):
    s = s.rstrip()
    m = re.match(r'^\s*[-*]\s?(.*)$', s)
    if m:
        return m.group(1).strip()
    return None


def indent_of(s):
    n = 0
    for ch in s:
        if ch == '\t':
            n += 4
        elif ch == ' ':
            n += 1
        else:
            break
    return n


def parse_examples(lines, warn):
    ex = []
    for ln in lines:
        if not ln.strip():
            continue
        ind = indent_of(ln)
        txt = clean_bullet(ln)
        if txt is None:
            warn.append('non-bullet in examples: ' + ln)
            continue
        if txt == '' or txt.lower() == 'todo':
            continue
        if ind >= 2:
            if ex:
                ex[-1][1].append(txt)
            else:
                ex.append([txt, []])
            continue
        if '\t' in txt:
            k, e = txt.split('\t', 1)
            ex.append([k.strip(), [e.strip()]])
            continue
        m = re.match(r'^(.*?[\uac00-\ud7a3][^\n]*?) - ([A-Za-z\(\"\'][^\uac00-\ud7a3]*)$', txt)
        if m and HANGUL.search(m.group(1)):
            ex.append([m.group(1).strip(), [m.group(2).strip()]])
            continue
        if not HANGUL.search(txt) and ex and not ex[-1][1]:
            ex[-1][1].append(txt)
            continue
        ex.append([txt, []])
    return ex


def parse_file(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = re.sub('[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
    text = text.replace('\u00a0', ' ')
    lines = text.split('\n')
    pre = []
    cards = []
    cur = None
    for ln in lines:
        if ln.startswith('## '):
            cur = Card()
            cur.title, cur.tags = split_heading(ln)
            cur.raw = {'뜻': [], '예': [], 'Notes': []}
            cur.state = 'head'
            cards.append(cur)
            continue
        if cur is None:
            pre.append(ln)
            continue
        s = ln.strip()
        if s == '?begin':
            cur.state = 'body'
            continue
        if s == '?end':
            cur.state = 'end'
            continue
        if s == '---':
            continue
        if s.startswith('<!--SR'):
            cur.sr = s
            continue
        m = re.match(r'^###\s*(.*)$', s)
        if m:
            name = m.group(1).strip()
            if name in ('뜻', '예', 'Notes'):
                cur.state = name
                continue
            cur.warn.append('unknown section ' + name)
            cur.state = 'unk'
            continue
        if cur.state in ('뜻', '예', 'Notes'):
            if s:
                cur.raw[cur.state].append(ln)
        elif s:
            cur.warn.append(cur.state + ': ' + ln)
    for c in cards:
        c.meanings = [clean_bullet(l) for l in c.raw['뜻'] if clean_bullet(l)]
        c.examples = parse_examples(c.raw['예'], c.warn)
        nn = []
        for l in c.raw['Notes']:
            t = clean_bullet(l)
            ind = indent_of(l)
            if t is None:
                nn.append(l.strip())
            else:
                nn.append(('  ' if ind >= 2 else '') + '- ' + t)
        c.notes = nn
    return '\n'.join(pre).strip('\n'), cards


def render(c):
    out = []
    out.append('## ' + ' '.join([c.title] + (c.tags if c.tags else ['#card'])))
    out.append('?begin')
    out.append('### 뜻')
    for m in c.meanings:
        out.append('- ' + m)
    out.append('### 예')
    for k, e in c.examples:
        out.append('- ' + k)
        for x in e:
            out.append('  - ' + x)
    if c.notes:
        out.append('### Notes')
        out.extend(c.notes)
    if c.sr:
        out.append(c.sr)
    out.append('?end')
    return '\n'.join(out)


def write_cards(path, pre, cards):
    parts = []
    if pre.strip():
        parts.append(pre.strip('\n'))
    for c in cards:
        parts.append(render(c))
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(parts) + '\n')


def report(name, cards):
    for c in cards:
        for w in c.warn:
            print('WARN', name, c.title, '|', w)
        if not c.meanings:
            print('NOMEAN', name, c.title)
        if not c.examples:
            print('NOEX', name, c.title)
        elif any(not e for k, e in c.examples):
            print('NOENG', name, c.title)


def sr_interval(sr):
    if not sr:
        return -1
    m = re.search(r'!\d{4}-\d\d-\d\d,(\d+),(\d+)', sr)
    return int(m.group(1)) if m else -1


def merge_into(a, b):
    for m in b.meanings:
        if m not in a.meanings:
            a.meanings.append(m)
    have = {k for k, e in a.examples}
    for k, e in b.examples:
        if k not in have:
            a.examples.append([k, list(e)])
            have.add(k)
    for n in b.notes:
        if n not in a.notes:
            a.notes.append(n)
    if sr_interval(b.sr) > sr_interval(a.sr):
        a.sr = b.sr
    for t in b.tags:
        if t not in a.tags:
            a.tags.append(t)
    return a


def find(cards, title):
    return [c for c in cards if c.title == title]


def get(cards, title):
    r = find(cards, title)
    if len(r) != 1:
        raise Exception('get %s -> %d' % (title, len(r)))
    return r[0]


def load(rel):
    return parse_file(BASE + rel)


def save(rel, pre, cards):
    write_cards(BASE + rel, pre, cards)


def ex(*pairs):
    """ex('kor','eng','kor','eng')"""
    return [[pairs[i], [pairs[i + 1]]] for i in range(0, len(pairs), 2)]


class Pool:
    def __init__(self):
        self.files = {}   # rel -> list of cards (ordered)

    def load(self, *rels):
        for r in rels:
            pre, cards = load(r)
            if pre.strip() and not pre.strip().startswith('#'):
                print('PRE-nonheading', r, pre[:80])
            self.files[r] = cards
        return self

    def take(self, rel, title, must=True):
        cs = [c for c in self.files[rel] if c.title == title]
        if not cs:
            if must:
                raise Exception('take: %s / %s not found' % (rel, title))
            return None
        c = cs[0]
        for x in cs[1:]:
            merge_into(c, x)
        self.files[rel] = [x for x in self.files[rel] if x.title != title]
        return c

    def peek(self, rel, title):
        cs = [c for c in self.files[rel] if c.title == title]
        return cs[0] if cs else None

    def all(self):
        for r, cs in self.files.items():
            for c in cs:
                yield r, c

    def findany(self, title):
        return [(r, c) for r, c in self.all() if c.title == title]

    def pull(self, title, exclude_rel=None):
        """take (and merge) every card with this title from whichever files"""
        found = [(r, c) for r, c in self.findany(title)]
        if not found:
            raise Exception('pull: %s not found' % title)
        first = found[0][1]
        for r, c in found[1:]:
            merge_into(first, c)
        for r, c in found:
            self.files[r] = [x for x in self.files[r] if x is not c]
        return first

    def pull_opt(self, title):
        if not self.findany(title):
            return None
        return self.pull(title)


def setc(c, title=None, meanings=None, examples=None, add_examples=None,
         notes=None, add_notes=None, add_meanings=None, tags=None, sr=None):
    if title is not None:
        c.title = title
    if meanings is not None:
        c.meanings = list(meanings)
    if add_meanings:
        for m in add_meanings:
            if m not in c.meanings:
                c.meanings.append(m)
    if examples is not None:
        c.examples = [list(x) for x in examples]
    if add_examples:
        have = {k for k, e in c.examples}
        for k, e in add_examples:
            if k not in have:
                c.examples.append([k, list(e)])
    if notes is not None:
        c.notes = ['- ' + n if not n.startswith(('- ', '  ')) else n for n in notes]
    if add_notes:
        for n in add_notes:
            n = '- ' + n if not n.startswith(('- ', '  ')) else n
            if n not in c.notes:
                c.notes.append(n)
    if tags is not None:
        c.tags = tags
    return c


def finalize(cards, name):
    """dedupe by title (merge), warn about empties"""
    out = []
    seen = {}
    for c in cards:
        if c.title in seen:
            merge_into(seen[c.title], c)
        else:
            seen[c.title] = c
            out.append(c)
    report(name, out)
    return out
