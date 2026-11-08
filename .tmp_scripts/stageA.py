import sys, os
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


FILES = ['몸/신체부위.md', '몸/신체.md', '몸/해부.md', '몸/화장.md', '몸/것.md', '몸/치아.md',
         '건강/건강.md', '건강/신체 부위.md', '건강/의료.md', '건강/증상.md',
         '장소/병원.md', '식사/음식.md']
P = Pool().load(*FILES)

# ---- renames
REN = {'물리 치료': '물리치료', '긴머리를 하다': '긴 머리를 하다', '햇빛 알러지': '햇빛 알레르기',
       '살 찌다': '살찌다', '가스가  차다': '가스가 차다'}
for r, c in P.all():
    if c.title in REN:
        c.title = REN[c.title]

new = {}


def assign(rel, titles):
    new[rel] = [P.pull(t) for t in titles]


# 병원 / 응급실 -> 장소/병원.md
for t in ['병원', '응급실']:
    P.files['장소/병원.md'].append(P.pull(t))
P.files['장소/병원.md'].sort(key=lambda c: 0 if c.title == '병원' else 1)

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

# leftovers of the 몸 files -> 기타
left = []
for rel in ['몸/신체부위.md', '몸/신체.md', '몸/해부.md', '몸/화장.md', '몸/것.md']:
    left += P.files[rel]
    P.files[rel] = []
new['몸/기타.md'] = left
P.files['몸/치아.md'] = P.files['몸/치아.md']
for c in P.files['건강/신체 부위.md']:
    print('LEFT 건강/신체 부위:', c.title)
P.files['건강/신체 부위.md'] = []

# 쓰리다 -> 건강/증상.md
P.files['건강/증상.md'].append(P.pull('쓰리다'))

# 건강 files: remaining stay; expose to the finder
ALL = {}
for rel, cs in list(new.items()) + list(P.files.items()):
    for c in cs:
        ALL.setdefault(c.title, c)


def E(title, **kw):
    return setc(ALL[title], **kw)

# ---------- 몸 edits
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
  notes=["고개를 숙이다 = to bow/lower one's head; 고개를 젓다 = to shake one's head"])
E('눈썹', meanings=['eyebrow'],
  examples=ex('눈썹이 짙어요', 'My eyebrows are thick',
              '눈썹을 그렸어요', 'I drew on my eyebrows'))
E('눈물', add_examples=ex('영화를 보다가 눈물이 났어요', 'I cried while watching the movie'))
E('머리를 감다', meanings=["to wash one's hair"],
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
E('씹히다', meanings=['to be chewed', 'to be bitten accidentally (e.g. tongue)', 'to chew (well)'],
  examples=ex('밥을 먹다가 혀가 씹혔어요', 'I accidentally bit my tongue while eating',
              '고기가 질겨서 잘 안 씹혀요', "The meat is tough, so it doesn't chew well"))
E('악물다', meanings=['to clench (one\'s teeth)', 'to grit one\'s teeth'],
  examples=ex('이를 악물고 참았어요', 'I gritted my teeth and endured it',
              '이를 악물고 끝까지 달렸어요', 'I ran to the end with gritted teeth'),
  notes=['이를 악물다 = to clench/grit one\'s teeth (also: to steel oneself)'])

# ---------- 건강 edits
E('중독되다', meanings=['to be addicted to', 'to be poisoned'],
  examples=ex('스마트폰에 중독된 것 같아요', 'I think I\'m addicted to my smartphone',
              '그는 도박에 중독됐어요', 'He became addicted to gambling'))
E('가스가 차다', meanings=['to be full of gas', 'to feel bloated'],
  add_examples=ex('배에 가스가 차서 불편해요', 'My stomach is full of gas and uncomfortable'))
E('눈이 충혈되다', meanings=['to have bloodshot eyes'],
  examples=ex('잠을 못 자서 눈이 충혈됐어요', 'My eyes are bloodshot because I couldn\'t sleep',
              '눈이 충혈돼서 안과에 갔어요', 'My eyes were bloodshot, so I went to the eye doctor'))
E('두통이 심하다', meanings=['to have a severe headache'],
  examples=ex('어제부터 두통이 심해요', 'I\'ve had a severe headache since yesterday',
              '두통이 심해서 약을 먹었어요', 'My headache was bad, so I took medicine'))
E('속이 답답하다', meanings=['to have indigestion', 'to feel bloated or heavy in the stomach',
                          'to feel stifled or frustrated (figurative)'],
  examples=ex('많이 먹었더니 속이 답답해요', 'I ate a lot and my stomach feels heavy',
              '체해서 속이 답답해요', 'I have indigestion, so my stomach feels stuffy'))
E('속이 쓰리다', meanings=['to have a burning stomach', 'to have gastric pain', 'to have an unsettled stomach'],
  examples=ex('빈속에 커피를 마셨더니 속이 쓰려요', 'My stomach burns after drinking coffee on an empty stomach',
              '매운 음식을 먹으면 속이 쓰려요', 'My stomach burns when I eat spicy food'),
  notes=['Related: 쓰리다 (to sting/burn), 속 (stomach/inside)'])
E('쓰리다', meanings=['to sting', 'to feel a burning pain (e.g. stomach, wound)'],
  examples=ex('속이 쓰려요', 'My stomach burns',
              '상처에 소독약을 바르니까 쓰려요', 'The disinfectant stings my wound'),
  notes=['Related: 속이 쓰리다 (to have a burning stomach)'])
E('콧물이 나다', meanings=['to have a runny nose'],
  examples=ex('감기에 걸려서 콧물이 나요', 'I caught a cold and my nose is running',
              '찬바람을 맞으면 콧물이 나요', 'My nose runs when I\'m exposed to cold wind'),
  notes=['Related: 콧물 (runny nose) in 의료'])
E('토하다', meanings=['to vomit', 'to throw up'],
  examples=ex('먹은 것을 다 토했어요', 'I threw up everything I ate',
              '차멀미 때문에 토할 것 같아요', 'I feel like throwing up because of carsickness'))
E('깁스를 하다', meanings=['to wear a cast', 'to get a cast'],
  examples=ex('다리가 부러져서 깁스를 했어요', 'I broke my leg and got a cast',
              '깁스를 한 팔로 글씨를 쓰기 힘들어요', 'It\'s hard to write with an arm in a cast'))
E('발목이 삐다', meanings=['to sprain one\'s ankle', 'to twist one\'s ankle'],
  examples=ex('축구를 하다가 발목이 삐었어요', 'I sprained my ankle while playing soccer',
              '계단에서 발목을 삐어서 병원에 갔어요', 'I sprained my ankle on the stairs, so I went to the hospital'),
  notes=['Also: 발목을 삐다 (same meaning)'])
E('얼굴에 뭐가 나다', meanings=['to break out in pimples', 'to break out (on the face)'],
  examples=ex('스트레스를 받으면 얼굴에 뭐가 나요', 'When I\'m stressed, I break out on my face',
              '어제부터 얼굴에 뭐가 났어요', 'Something has broken out on my face since yesterday'))
E('햇빛에 타다', meanings=['to get sunburnt', 'to get tanned'],
  examples=ex('바닷가에서 햇빛에 많이 탔어요', 'I got badly sunburnt at the beach',
              '햇빛에 타서 피부가 따가워요', 'I got sunburnt, so my skin stings'))
E('햇빛 알레르기', meanings=['sun allergy'],
  examples=ex('햇빛 알레르기가 있어서 선크림을 꼭 발라요', 'I have a sun allergy, so I always apply sunscreen',
              '봄이 되면 햇빛 알레르기가 심해져요', 'My sun allergy gets worse in spring'))
E('외상증후군', add_notes=['PTSD in standard Korean is usually 외상 후 스트레스 장애'])
E('소아과', meanings=['pediatrics', 'pediatric clinic'],
  examples=ex('아이가 열이 나서 소아과에 갔어요', 'My child had a fever, so I went to the pediatrician',
              '소아과는 오전에 사람이 많아요', 'Pediatric clinics are crowded in the morning'))
E('소아', meanings=['child (medical term)', 'pediatric'],
  examples=ex('소아 환자', 'pediatric patient',
              '소아 비만이 늘고 있어요', 'Childhood obesity is increasing'),
  notes=['소아 = 아이들 (children)', 'Related: 소아과 (pediatrics)'])
E('병신', meanings=['offensive slur for a disabled person or an idiot (vulgar; avoid using)'],
  examples=ex('병신처럼 행동하지 마', "Don't act like an idiot (vulgar)"),
  notes=['Considered very offensive and should be avoided. Use 장애인 (person with a disability) for the first sense.'])
E('복수', add_meanings=['ascites (fluid in the abdomen)'],
  add_examples=ex('간 질환 때문에 복수가 찼어요', 'Fluid built up in his abdomen because of liver disease'))
E('매스껍다', meanings=['to feel nauseous', 'to be queasy'],
  examples=ex('속이 매스꺼워요', 'I feel nauseous',
              '차를 오래 탔더니 속이 매스꺼워서 토할 것 같아요', 'After a long ride in the car I feel so queasy I want to throw up'))
E('살찌다', add_notes=['Also written 살이 찌다 (with particle)'])

# ---------- finalize + save
def save_rel(rel, cards):
    cards = [c for c in cards]
    for c in cards:
        fix_text(c)
    cards = finalize(cards, rel)
    save(rel, '', cards)


for rel in ['몸/신체부위.md', '몸/신체.md', '몸/해부.md', '몸/화장.md', '몸/기타.md']:
    save_rel(rel, new[rel])
save_rel('몸/치아.md', P.files['몸/치아.md'])
for rel in ['건강/건강.md', '건강/의료.md', '건강/증상.md', '장소/병원.md', '식사/음식.md']:
    save_rel(rel, P.files[rel])

for rel in ['건강/신체 부위.md', '몸/것.md']:
    p = BASE + rel
    if os.path.exists(p):
        os.remove(p)
        print('removed', rel)
