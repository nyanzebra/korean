import os, re, sys

D = '/home/robert/Documents/GitHub/korean/단어/Helping words'


def base(h):
    return re.split(r' #', h[3:], 1)[0].strip()


class Card:
    ORDER = ['뜻', '예', 'Notes', 'Tags']

    def __init__(self, heading, body):
        self.heading = heading.rstrip()
        self.sec = {}
        self.sr = None
        lines = []
        for raw in body:
            raw = raw.rstrip()
            if raw.strip() == '':
                continue
            st = raw.strip()
            if st.endswith('?end') and st != '?end':
                raw = raw[:raw.rfind('?end')].rstrip()
                lines.append(raw)
                lines.append('?end')
                continue
            lines.append(raw)
        cur = None
        for ln in lines:
            m = re.match(r'^(\s*)([-*])(\s+|$)(.*)$', ln)
            if m:
                lvl = 1 if m.group(1) else 0
                txt = m.group(4).strip()
                ln = ('\t' * lvl) + ('- ' + txt if txt else '-')
            if ln.strip() in ('?begin', '?end'):
                continue
            if ln.startswith('<!--SR'):
                self.sr = ln.strip()
                continue
            if ln.startswith('### '):
                cur = ln[4:].strip()
                self.sec[cur] = []
                continue
            if cur is None:
                raise Exception('line before section in %s: %r' % (heading, ln))
            self.sec[cur].append(ln)
        for k in ('뜻', 'Notes'):
            if k in self.sec:
                self.sec[k] = [x for x in self.sec[k] if x.strip() not in ('-',)]
        if '예' in self.sec:
            if all(x.strip() in ('-', '- todo', 'todo') for x in self.sec['예']):
                self.sec['예'] = []

    @property
    def base(self):
        return base(self.heading)

    def placeholder(self):
        return not self.sec.get('예')

    def set_mean(self, items):
        self.sec['뜻'] = ['- ' + x for x in items]

    def set_ex(self, pairs):
        out = []
        for ko, en in pairs:
            out.append('- ' + ko)
            out.append('\t- ' + en)
        self.sec['예'] = out

    def add_ex(self, pairs):
        cur = self.sec.get('예', [])
        for ko, en in pairs:
            cur.append('- ' + ko)
            cur.append('\t- ' + en)
        self.sec['예'] = cur

    def add_notes(self, items):
        cur = self.sec.get('Notes', [])
        for x in items:
            cur.append('- ' + x)
        self.sec['Notes'] = cur

    def set_notes(self, items):
        self.sec['Notes'] = ['- ' + x for x in items]

    def render(self):
        out = [self.heading, '?begin']
        keys = [k for k in self.ORDER if k in self.sec] + [k for k in self.sec if k not in self.ORDER]
        for k in keys:
            out.append('### ' + k)
            out.extend(self.sec[k])
        if self.sr:
            out.append(self.sr)
        out.append('?end')
        return '\n'.join(out)


def mk(heading, mean, ex, notes=None, sr=None, tags=None):
    c = Card(heading, ['?begin', '### 뜻', '### 예', '?end'])
    c.sec = {}
    c.set_mean(mean)
    c.set_ex(ex)
    if notes:
        c.set_notes(notes)
    if tags:
        c.sec['Tags'] = [tags]
    c.sr = sr
    return c


class F:
    def __init__(self, name):
        self.name = name
        path = os.path.join(D, name)
        txt = open(path, encoding='utf-8').read().split('\n')
        pre, cards = [], []
        cur_h, cur_b = None, []
        for ln in txt:
            if ln.startswith('## '):
                if cur_h is not None:
                    cards.append(Card(cur_h, cur_b))
                cur_h, cur_b = ln, []
            elif cur_h is None:
                if ln.strip():
                    pre.append(ln.rstrip())
            else:
                cur_b.append(ln)
        if cur_h is not None:
            cards.append(Card(cur_h, cur_b))
        self.pre = pre
        self.cards = cards

    def get(self, b):
        r = [c for c in self.cards if c.base == b]
        if len(r) != 1:
            raise Exception('get %s in %s -> %d' % (b, self.name, len(r)))
        return r[0]

    def pop(self, b):
        c = self.get(b)
        self.cards.remove(c)
        return c

    def replace(self, b, new):
        c = self.get(b)
        self.cards[self.cards.index(c)] = new

    def save(self):
        parts = []
        if self.pre:
            parts.append('\n'.join(self.pre))
        parts.extend(c.render() for c in self.cards)
        open(os.path.join(D, self.name), 'w', encoding='utf-8').write('\n\n'.join(parts) + '\n')


names = ['Helping words.md', '관용구.md', '대명사.md', '말하기.md', '방향.md', '부분 표현.md', '부사.md',
         '수와 카운터.md', '시간 개념.md', '시간 표현.md', '위치 표현.md', '의성어.md', '의성어_및_표현.md',
         '의태어.md', '접속사.md', '표현.md', '표현_및_언어.md', '필수 동사.md', '필수 형용사.md']
fs = {n: F(n) for n in names}
HW, GY, DM, MH, BH, BP, BS, SC, SG, SP, WC, SS, SSP, ST, JS, PH, PHU, PD, PY = [fs[n] for n in names]

# ---------------------------------------------------------------- moves
# 의성어_및_표현 -> 의성어 / 관용구
c = SSP.pop('또각또가')
c.heading = '## 또각또각 #card'
SS.cards.append(c)
GY.cards.append(SSP.pop('안도의 한숨'))
GY.cards.append(SSP.pop('노을이 비치다'))
# 표현_및_언어 -> 말하기
for b in ['속담', '뜻풀이하다', '인용하다']:
    MH.cards.append(PHU.pop(b))
# 표현 -> Helping words
HW.cards.append(PH.pop('불문하다'))
# 부분 표현 -> 관용구
GY.cards.append(BP.pop('유난 떨다'))
# 시간 표현 -> 시간 개념
for c in list(SP.cards):
    SG.cards.append(c)
SP.cards = []
# 위치 표현 -> 방향
for c in list(WC.cards):
    BH.cards.append(c)
WC.cards = []
# 접속사 adverbs -> 부사
for c in list(JS.cards):
    if '#adverb' in c.heading:
        JS.cards.remove(c)
        BS.cards.append(c)

# ---------------------------------------------------------------- merges
# 꼬박꼬박 (의태어 keeps; SR from Helping words copy has interval 295)
old = HW.pop('꼬박꼬박')
ST.replace('꼬박꼬박', mk(
    '## 꼬박꼬박 #card',
    ['regularly, faithfully, without fail', 'dutifully, obediently (following what someone says)'],
    [('매달 꼬박꼬박 저축한다.', 'I save faithfully every month.'),
     ('어른의 말을 꼬박꼬박 잘 듣다', 'readily obey one\'s elders.'),
     ('대출금을 매월 꼬박꼬박 갚아 나가다', 'make the monthly payment on one\'s loan regularly[right on time].')],
    ['Often used negatively too: 꼬박꼬박 말대꾸하다 (to talk back every single time)',
     'Not to be confused with 꾸벅꾸벅 (nodding off / bowing repeatedly), as in 꾸벅꾸벅 졸다. The old Helping words copy had the typo "꼬박꼬박 졸다".'],
    sr=old.sr))

# 바짝 / 활짝 / 꽉  (부사 -> 의태어)
BS.pop('바짝'); BS.pop('활짝'); BS.pop('꽉')
ST.replace('바짝', mk(
    '## 바짝 #card #distance #close #tightly #degree',
    ['closely', 'tightly, very close', 'intently, hard', 'completely (dry)'],
    [('그는 내 옆에 바짝 다가앉았다.', 'He sat down right next to me.'),
     ('빨래가 햇볕에 바짝 말랐다.', 'The laundry dried completely in the sun.'),
     ('시험이 얼마 남지 않아서 바짝 공부해야 한다.', 'The exam is close, so I have to study hard.')],
    ['바짝바짝 is the repeated form (e.g. 입이 바짝바짝 마르다 — one\'s mouth keeps going dry) — see its own card',
     'Different word from 반짝 / 반짝반짝 (twinkling)']))
ST.replace('활짝', mk(
    '## 활짝 #card',
    ['widely, broadly', 'fully open, wide open', 'in full bloom', 'brightly (smiling)'],
    [('활짝 웃다', 'to smile broadly'), ('활짝 열다', 'to open wide'),
     ('봄이 되자 꽃이 활짝 피었다.', 'When spring came, the flowers bloomed in full.'),
     ('아이가 활짝 웃으며 달려왔다.', 'The child came running with a bright smile.')]))
ST.replace('꽉', mk(
    '## 꽉 #card #tight #full',
    ['tightly', 'jam-packed, full'],
    [('꽉 잡다', 'to hold tight'), ('꽉 찼어요', "It's full"),
     ('가방에 짐이 꽉 찼다.', 'The bag is jam-packed.')],
    ['Related: 꼭 (tightly / without fail, in 부사.md), 꾹 / 꾹꾹 (pressing firmly)']))

# 꼭 (의태어 -> 부사)
ST.pop('꼭')
BS.replace('꼭', mk(
    '## 꼭 #card #adverb #certainly #must #sogang #sogang-4A',
    ['certainly, must, without fail', 'tightly (holding, pressing)', 'exactly, just (꼭 맞다, 꼭 닮다)'],
    [('꼭 오세요', 'Please come without fail'), ('꼭 필요해요', "It's absolutely necessary"),
     ('내일은 꼭 와야 해.', 'You must come tomorrow, without fail.'),
     ('아이의 손을 꼭 잡았다.', "I held the child's hand tightly.")],
    ['Related: 반드시 (surely, more formal), 꽉 (tightly / packed, in 의태어.md)']))

# 점점 (의태어 + 접속사 -> 부사)
old = ST.pop('점점')
BS.replace('점점', mk(
    '## 점점 #card #adverb #gradually #little-by-little #sogang #sogang-4A',
    ['gradually, little by little', 'more and more'],
    [('점점 좋아져요', "It's gradually getting better"),
     ('날씨가 점점 추워진다.', "It's getting colder and colder.")],
    ['See also 점점 더 많이 (more and more, quantity) in this file']))

# 깜빡 / 깜박
a = ST.pop('깜박')
ST.replace('깜빡', mk(
    '## 깜빡 #card',
    ['blinking', 'forgetting for a moment'],
    [('약속을 깜빡 잊었다.', 'I completely forgot about the appointment.'),
     ('그는 눈을 한 번 깜박였다.', 'He blinked once.'),
     ('열쇠를 가져오는 걸 깜박했다.', 'I forgot to bring the key.')],
    ['깜박 and 깜빡 are both standard variants (깜빡 is the stronger form); the repeated form 깜빡깜빡 (blinking / flickering) has its own card',
     'Verbs: 깜박이다 / 깜빡이다 (to blink, flicker)']))

# 말이에요 (말이예요 + 말예요)
MH.pop('말이예요'); MH.pop('말예요')
cur = MH.get('말이요')
MH.cards.insert(MH.cards.index(cur), mk(
    '## 말이에요 #card',
    ["I'm saying / what I mean is (polite)", "it's about... (stating what one is talking about)"],
    [('제 말이 그 말이에요.', "That's exactly what I'm saying."),
     ('그게 아니라 이 말이에요.', 'Not that — I mean this.'),
     ('중요한 말이에요.', "It's an important thing to say.")],
    ['Standard spelling is 말이에요 (말 ends in a consonant, so 이에요 — not 예요). 말이예요 and 말예요 are common misspellings/non-standard contractions of it',
     '말이요 (separate card) is a different form, used when echoing what someone said: 제 말이요!']))
cur.set_mean(['as for (what was just said) (polite echo)', 'exactly! (in 제 말이요)'])
cur.set_ex([('제 말이요!', "That's exactly what I'm saying!"),
            ('그 말이요? 저도 그렇게 생각해요.', 'That remark? I think so too.')])
cur.set_notes(['말이요 = 말 + 이요. It echoes someone\'s words politely; for "it is what I mean" use 말이에요 (separate card)',
               '말이예요 / 말예요 are non-standard — use 말이에요'])
