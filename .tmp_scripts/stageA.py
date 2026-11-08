import sys
sys.path.insert(0, '/home/robert/Documents/GitHub/korean/.tmp_scripts')
from lib import *

TYPOS = [('바래요', '바라요'), ('고장났어요', '고장 났어요'), ('욕조가 크요', '욕조가 커요'),
         ('야외 음아당', '야외 음악당')]


def fix_text(c):
    def f(s):
        for a, b in TYPOS:
            s = s.replace(a, b)
        return s
    c.title = f(c.title)
    c.meanings = [f(x) for x in c.meanings]
    c.examples = [[f(k), [f(x) for x in e]] for k, e in c.examples]
    c.notes = [f(x) for x in c.notes]


P = Pool().load('몸/신체부위.md', '몸/신체.md', '몸/해부.md', '몸/화장.md', '몸/것.md', '몸/치아.md',
                '건강/건강.md', '건강/신체 부위.md', '건강/의료.md', '건강/증상.md',
                '장소/병원.md', '식사/음식.md')

# ---- renames
for r, c in P.all():
    if c.title == '물리 치료':
        c.title = '물리치료'
    if c.title == '긴머리를 하다':
        c.title = '긴 머리를 하다'
    if c.title == '햇빛 알러지':
        c.title = '햇빛 알레르기'
    if c.title == '살 찌다':
        c.title = '살찌다'
    if c.title == '가스가  차다':
        c.title = '가스가 차다'
    if c.title == '가스가 차다':
        pass

# ---- cards that go to 장소/병원.md
hosp = P.files['장소/병원.md']
for t in ['병원', '응급실']:
    c = P.pull(t)
    P.files['장소/병원.md'].append(c)
# keep 병원 first
P.files['장소/병원.md'].sort(key=lambda c: 0 if c.title == '병원' else 1)

new = {}


def assign(rel, titles):
    out = []
    for t in titles:
        c = P.pull(t)
        out.append(c)
    new[rel] = out


# ----- 몸/신체부위.md : external body parts
assign('몸/신체부위.md', [
    '머리', '얼굴', '눈썹', '코', '입', '입술', '혀', '이', '귀', '목', '고개', '뺨', '수염',
    '어깨', '팔', '겨드랑이', '손', '손등', '손바닥', '손가락', '손톱', '손발', '맨손',
    '등', '가슴', '허리', '허벅지', '허벅지 뒤 근육', '무릎', '종아리', '다리', '발', '발가락', '발톱'])

assign('몸/해부.md', [
    '해부', '육체', '성별', '피부', '뼈', '관절', '근육', '근력', '삼두근', '내장', '속',
    '심장', '폐', '위', '장', '신장', '뇌', '피', '침', '침을 흘리다', '눈물', '헛기침',
    '호흡', '숨', '맥박', '체온', '혈압', '시력', '키', '체격', '덩치가 크다', '몸무게', '체중',
    '단백질', '탄수화물', '상처', '흉터', '굳은살', '멍'])

assign('몸/신체.md', ['온몸', '뒷모습', '포옹', '목소리', '목숨', '눈치', '피곤해', '배고파'])

assign('몸/화장.md', ['머리를 감다', '머리를 말리다', '머리가 길다', '긴 머리를 하다', '빗질', '문신'])

# leftovers in the 몸 files -> 기타
left = []
for rel in ['몸/신체부위.md', '몸/신체.md', '몸/해부.md', '몸/화장.md', '몸/것.md']:
    for c in P.files[rel]:
        left.append(c)
    P.files[rel] = []
new['몸/기타.md'] = left

# 건강/신체 부위 leftovers?
for c in P.files['건강/신체 부위.md']:
    print('LEFT 건강/신체 부위:', c.title)

# ---- other moves: 쓰리다 -> 증상.md
ssr = P.pull('쓰리다')
P.files['건강/증상.md'].append(ssr)

# ---- text edits
def C(title):
    return P.pull(title) if False else None


def find_card(title):
    for r, cs in list(P.files.items()):
        pass
    for rel, cs in new.items():
        for c in cs:
            if c.title == title:
                return c
    for rel, cs in P.files.items():
        for c in cs:
            if c.title == title:
                return c
    raise Exception('nf ' + title)


def E(title, **kw):
    return setc(find_card(title), **kw)

E('성별', meanings=['gender', 'sex (male/female)'],
  examples=ex('신청서에 이름, 나이, 성별을 쓰세요', 'Write your name, age and sex on the application form',
              '성별에 관계없이 누구나 지원할 수 있어요', 'Anyone can apply regardless of gender'))
E('삼두근', meanings=['triceps'],
  examples=ex('팔 뒤쪽 근육인 삼두근을 운동했어요', 'I worked out my triceps, the muscle at the back of the arm',
              '팔굽혀펴기는 삼두근에 좋아요', 'Push-ups are good for the triceps'),
  notes=['Related: 이두근 (biceps), 근육 (muscle)'])
E('덩치가 크다', meanings=['to be big-boned', 'to have a large frame (body)', 'to be big in size'],
  examples=ex('그 선수는 덩치가 커서 눈에 띄어요', 'That player has a large frame, so he stands out',
              '동생은 저보다 덩치가 훨씬 커요', 'My younger brother is much bigger than me'),
  notes=['덩치 = body size/bulk; related: 체격 (physique)'])
E('내장', meanings=['internal organs', 'guts', 'intestines', 'bowels'],
  examples=ex('생선 내장을 빼고 요리하세요', 'Remove the guts of the fish before cooking',
              '교통사고로 내장이 손상됐어요', 'My internal organs were damaged in the car accident'),
  notes=['Related: 장 (intestine), 위 (stomach)'])
E('수염', meanings=['beard', 'mustache', 'whiskers'],
  examples=ex('수염을 기르다', 'to grow a beard',
              '아침마다 수염을 깎아요', 'I shave my beard every morning'),
  notes=['Related: 턱수염 (beard), 콧수염 (mustache)'])
E('뺨', meanings=['cheek', 'slap on the cheek'],
  examples=ex('부끄러워서 뺨이 빨개졌어요', 'My cheeks turned red from embarrassment',
              '아이의 뺨에 입을 맞췄어요', 'I kissed the child on the cheek',
              '뺨을 맞다', 'to get slapped on the cheek'),
  notes=['Related: 볼 (cheek, more colloquial), 얼굴 (face)'])
E('흉터', meanings=['scar'],
  examples=ex('얼굴에 흉터가 남았어요', 'A scar remained on my face',
              '수술 흉터가 점점 옅어지고 있어요', 'The surgery scar is gradually fading'),
  notes=['상처 (wound) vs 흉터 (the scar left after the wound heals)'])
E('굳은살', meanings=['callus', 'hardened skin'],
  examples=ex('기타를 치면 손가락에 굳은살이 생겨요', 'Calluses form on your fingers when you play guitar',
              '발에 굳은살이 박였어요', 'I have calluses on my feet'))
E('단백질', meanings=['protein'],
  examples=ex('단백질을 많이 먹으면 근육이 생겨요', 'If you eat a lot of protein, you build muscle',
              '계란에는 단백질이 풍부해요', 'Eggs are rich in protein'))
E('탄수화물', meanings=['carbohydrate', 'carbs'],
  examples=ex('다이어트 중이라서 탄수화물을 줄이고 있어요', "I'm on a diet, so I'm cutting back on carbs",
              '밥과 빵에는 탄수화물이 많아요', 'Rice and bread are high in carbohydrates'))
E('근육', meanings=['muscle', 'muscles'],
  add_examples=ex('운동을 해서 팔에 근육이 생겼어요', 'I exercised and built muscle in my arms'))
E('침을 흘리다', meanings=['to drool', 'to salivate'],
  examples=ex('아기가 자면서 침을 흘려요', 'The baby drools while sleeping',
              '맛있는 음식을 보고 침을 흘렸어요', 'I drooled at the sight of the delicious food'))
E('침', meanings=['saliva', 'spit'],
  examples=ex('침을 흘리다', 'to drool',
              '긴장해서 침을 삼켰어요', 'I swallowed nervously',
              '길에 침을 뱉지 마세요', "Don't spit on the street"))
E('고개', meanings=['neck and head (as in head movements)', 'nod', 'mountain pass'],
  examples=ex('고개를 끄덕이다', 'to nod',
              '부끄러워서 고개를 숙였어요', 'I bowed my head out of embarrassment',
              '고개를 들어서 하늘을 봤어요', 'I lifted my head and looked at the sky',
              '고개를 넘어가면 우리 마을이 보여요', 'If you go over the pass, you can see our village'),
  notes=['고개를 숙이다 = to bow/lower one\'s head; 고개를 젓다 = to shake one\'s head'])
E('눈썹', meanings=['eyebrow'],
  examples=ex('눈썹이 짙어요', 'My eyebrows are thick',
              '눈썹을 그렸어요', 'I drew on my eyebrows'))
E('눈물', add_examples=ex('영화를 보다가 눈물이 났어요', 'I cried while watching the movie'))
E('틀니' if False else '머리', meanings=['head', 'hair'] if False else ['head'])
E('머리를 감다', meanings=['to wash one\'s hair'],
  examples=ex('아침마다 머리를 감아요', 'I wash my hair every morning',
              '샴푸로 머리를 감았어요', 'I washed my hair with shampoo'))
E('머리를 말리다', meanings=["to dry one's hair"],
  examples=ex('머리를 감고 드라이어로 말려요', 'After washing my hair, I dry it with a hair dryer',
              '머리를 안 말리고 자면 감기에 걸려요', "If you go to sleep without drying your hair, you'll catch a cold"))
E('머리가 길다', meanings=['to have long hair'])
E('긴 머리를 하다', meanings=["to wear one's hair long"])
E('틀니', meanings=['dentures', 'false teeth'],
  examples=ex('할아버지는 틀니를 하고 계세요', 'My grandfather wears dentures',
              '밤에는 틀니를 빼서 깨끗이 닦아요', 'At night I take out the dentures and clean them'))
