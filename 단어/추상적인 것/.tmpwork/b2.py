exec(open(W + '/b1.py', encoding='utf-8').read())

RT = '개념_추상.md'
GN = '개념_추상/개념.md'   # 개념
GT = '개념_추상/것.md'
LOC = '시간_공간/위치와 장소.md'
TIME = '시간_공간/시간.md'
BIZ = '사회_문화/사업과 경제.md'
SOC = '사회_문화/사회와 문화.md'
LANG = '사회_문화/언어와 예술.md'
QTY = '개념_추상/수와 양.md'
VIEW = '개념_추상/관점.md'
ADV = '개념_추상/부사_연결_표현.md'
EMO = '감정_심리/감정.md'
MIND = '감정_심리/생각_마음.md'
REG = '감정_심리/후회.md'
TRAIT = '개인_특성/특성_성격.md'
DISC = '개인_특성/규율.md'
OPIN = '소통_관계/의견.md'
COMM = '소통_관계/의사소통.md'
ADJ = '소통_관계/조정.md'
STATE = '상태_변화/상태.md'
RISK = '상태_변화/위험.md'
ACH = '성공_성취/성취.md'
INFL = '성공_성취/영향.md'
EFF = '성공_성취/효율_생산성.md'
HAPPY = '성공_성취/행복과_노력.md'
DUTY = '윤리_신념/의무.md'
RESP = '윤리_신념/책임.md'
PROC = '프로세스_절차/절차.md'
ACT = '프로세스_절차/작용.md'
APPLY = '프로세스_절차/적용.md'
OLD_REG = '감정_심리/후회_겸웅.md'
OLD_MIND = '감정_심리/생각___마음.md'
OLD_STATE = '상태_변화/개념과_상태.md'
F['감정_심리/생각_마음.md'] = F.pop(OLD_MIND)
F[REG] = F.pop(OLD_REG)
EMO_ = EMO

# ---------- root 개념_추상.md distribution ----------
for w in ['소재', '결론', '기', '추가 정보']: move(RT, w, GN)
move(RT, '지적 재산', BIZ)
for w in ['당시', '어느새', '조만간', '한때', '해마다', '시간이 흐르다', '예전에 비해서']: move(RT, w, TIME)
for w in ['어디선가', '곳곳', '생활하기 좋다', '지리적인 특징']: move(RT, w, LOC)
for w in ['거꾸로', '논리적으로', '더욱더', '딴에는', '어쩌면', '외에도', '이와 달리', '지나지 않다', '만만치 않다', '널리 퍼지다']: move(RT, w, ADV)
for w in ['살아가다', '청년층']: move(RT, w, SOC)
move(RT, '어우러지다', ADJ)
for w in ['제대로 된 번역', '템포가 빠르다']: move(RT, w, LANG)
move(RT, '효율성', EFF)
move(RT, '집중력', MIND)
move(RT, '해내다', ACH)
move(RT, '해당하다', APPLY)
move(RT, '체크하다', PROC)

# other root files
move('위치_공간.md', '근교', LOC)
move('특질_성격.md', '고집', TRAIT)
move('특질_성격.md', '고집불통', TRAIT)
move('특질_성격.md', '의도', EMO)
move('개인_특성.md', '부분', QTY)
move('개인_특성.md', '유능하다', TRAIT)
move('소통_관계.md', '오해', COMM)
move('관계.md', '연결', COMM)

# ---------- 개념.md / 것.md moves ----------
move(GN, '영향', INFL)
move(GN, '작용', ACT)
move(GN, '절차', PROC); move(GN, '단계', PROC)
for w in ['관점', '측면', '면']: move(GN, w, VIEW)
for w in ['특성', '특징', '성질']: move(GN, w, TRAIT)
for w in ['규칙', '원칙', '질서']: move(GN, w, DISC)
for w in ['문화', '풍습']: move(GN, w, SOC)
for w in ['서론', '제목']: move(GN, w, LANG)
move(GN, '년', TIME)
for w in ['반면에', '대부분']: move(GN, w, ADV)
move(GT, '위로하다', EMO)
move(GT, '변호하다', OPIN)
move(GT, '약점/단점/나쁜점', TRAIT); move(GT, '강점/장점/좋은점', TRAIT)
move(GT, '노력', HAPPY)

# ---------- other moves ----------
for w in ['내 의견으로는', '나의 관점', '내 관점으로는', '동의하다', '동의하지 않다']: move(EFF, w, OPIN)
move(SOC, '의무', DUTY); move(SOC, '책임감', RESP); move(SOC, '과정', PROC)
move('성공_성취/기회.md', '위기', RISK)
move(OLD_STATE, '호감', EMO)
for w in ['후회하다', '유감스럽다', '안타깝다', '아쉽다']: move(EMO, w, REG)

# ---------- merges ----------
def mergeinto(dest, sources, order=None):
    pos = None
    cards = []
    for rel, w in sources:
        idxs = [i for i, c in enumerate(F[rel].cards) if c.word == w]
        if rel == dest and pos is None and idxs: pos = idxs[0]
        cards += find(rel, w)
    order = order or list(range(len(cards)))
    m = merge_cards([cards[i] for i in order])
    F[dest].cards.insert(pos if pos is not None else len(F[dest].cards), m)

mergeinto(VIEW, [(RT, '전망'), (GN, '전망')])
mergeinto(LOC, [(RT, '방향'), (LOC, '방향')])
mergeinto(LOC, [(RT, '중간'), ('위치_공간.md', '중간'), (LOC, '중간')], [2, 1, 0])
mergeinto(QTY, [(RT, '양'), (LANG, '양')], [1, 0])
mergeinto(BIZ, [(RT, '자금'), (BIZ, '자금')], [1, 0])
mergeinto(EMO, [(HAPPY, '행복'), (EMO, '행복')], [1, 0])
mergeinto(OPIN, [(EFF, '의견'), (SOC, '의견')], [1, 0])
mergeinto(GN, [(GN, '조건'), (OLD_STATE, '조건')])
for w in ['의미', '이유', '상황']:
    mergeinto(GN, [(GN, w), (GT, w)])
cs_idx = [i for i, c in enumerate(F[GT].cards) if c.word == '계획']
mergeinto(GT, [(GT, '계획'), (GT, '계획')][:1]) if False else None
_c = find(GT, '계획')
F[GT].cards.insert(cs_idx[0], merge_cards([_c[1], _c[0]]))
mergeinto(EMO, [(EMO, '진심'), (EMO, '진심')][:1]) if False else None
_idx = [i for i, c in enumerate(F[EMO].cards) if c.word == '진심']
_c = find(EMO, '진심')
F[EMO].cards.insert(_idx[0], merge_cards([_c[0], _c[1]]))
mergeinto(REG, [(EMO, '후회'), (REG, '후회')], [0, 1])
mergeinto(REG, [(EMO, '유감'), (REG, '유감')], [0, 1])

# ---------- assemble files ----------
RENAME = {GT: GN, OLD_STATE: STATE}
DELETE = {RT, '관계.md', '위치_공간.md', '특질_성격.md', '개인_특성.md', '소통_관계.md'}
final = {}
order = []
def put(rel, fm_or_cards, pre=None, post=None):
    pass

for rel, fm in F.items():
    if rel in DELETE:
        assert not fm.cards, (rel, [c.word for c in fm.cards])
        continue
    new = RENAME.get(rel, rel)
    t = final.setdefault(new, FileModel())
    if not t.pre: t.pre = fm.pre
    t.post += fm.post
    t.cards += fm.cards
for rel, fm in D.items():
    t = final.setdefault(rel, FileModel())
    t.cards += fm.cards
