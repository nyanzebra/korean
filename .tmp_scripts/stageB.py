import sys, os
sys.path.insert(0, '/home/robert/Documents/GitHub/korean/.tmp_scripts')
from lib import *

P = Pool().load('식사/음식.md', '식사/것.md', '식사/맛.md', '장소/식당.md', '장소/가게.md')

# renames / typo titles
for r, c in P.all():
    if c.title == '양염':
        c.title = '양념'
    if c.title == '탄산 음료':
        c.title = '탄산음료'
    if c.title == '쇠고기':
        c.title = '소고기'
    if c.title == '' or c.title == '어묵':
        c.title = '어묵'

new = {}


def assign(rel, titles):
    new[rel] = [P.pull(t) for t in titles]


# stray lines after 깔다's ?end are leftovers of 쓰리다 (already moved) -> drop
assign('식사/음식.md', ['음식', '요리', '별미', '별미 중의 별미', '밥', '국', '찌개', '반찬', '죽', '라면', '국수',
                        '만두', '떡', '송편', '김치', '동치미', '누룽지', '꼬치', '어묵', '조림', '주먹밥', '삼각김밥',
                        '빵', '과자', '호박 파이', '회', '찍먹', '부먹',
                        '음료수', '커피', '술', '막걸리', '탄산음료', '녹차', '유자차', '생강차'])
assign('식사/재료.md', ['고기', '소고기', '돼지고기', '닭고기', '계', '칠면조', '생선', '참치', '새우', '오징어', '조개',
                        '채소', '배추', '무', '상추', '오이', '버섯', '당근', '감자', '고구마', '단호박', '마늘', '생강',
                        '과일', '사과', '배', '포도', '딸기', '바나나', '수박', '감', '귤', '오렌지', '복숭아',
                        '우유', '계란', '땅콩', '쌀', '찹쌀', '벼', '곡물', '밀가루', '메밀',
                        '설탕', '소금', '식초', '후추', '간장', '된장', '고추장', '참기름', '양념', '향신료', '박하',
                        '오미자', '동백', '인삼', '육수', '재료', '신선한'])
assign('식사/요리.md', ['볶다', '썰다', '다지다', '갈다', '까다', '튀기다', '끓이다', '찌다', '굽다', '익다', '덜 익다',
                        '졸이다', '데우다', '식히다', '무치다', '버무리다', '뿌리다', '담다', '떠 먹다', '긁어 먹다', '국자'])
assign('식사/맛.md', ['맛', '맛보다', '간', '향', '시다', '달다', '맵다', '짜다', '싱겁다', '담백하다', '느끼하다',
                      '고소하다', '새콤하다', '매콤하다', '걸쭉하다', '기름기 있다', '자극적인 음식', '알맞다'])
assign('식사/식습관.md', ['식사', '굶다', '과식', '폭식', '섭취', '식후', '후식', '입맛이 없다', '입맛을 살리다',
                          '야식', '건강식품', '채식주의자', '시키다', '배달하다', '장을 보다', '먹으러'])
# 뷔페 -> 장소/식당.md ; 전문점 -> 장소/가게.md
buffet = P.pull('뷔페')
spec = P.pull('전문점')
P.files['장소/식당.md'].append(buffet)
P.files['장소/가게.md'].append(spec)

left = []
for rel in ['식사/음식.md', '식사/것.md', '식사/맛.md']:
    left += P.files[rel]
    P.files[rel] = []
new['식사/기타.md'] = left

ALL = {}
for rel, cs in list(new.items()) + list(P.files.items()):
    for c in cs:
        ALL.setdefault(c.title, c)


def E(title, **kw):
    return setc(ALL[title], **kw)

# ---------- 음식
E('음식', meanings=['food', 'cuisine'],
  add_examples=ex('어떤 음식을 좋아해요?', 'What kind of food do you like?'))
E('요리', meanings=['cooking', 'cuisine', 'dish'])
E('꼬치', meanings=['skewer', 'food on a skewer'],
  examples=ex('닭꼬치', 'chicken skewers',
              '포장마차에서 꼬치를 먹었어요', 'I ate skewers at a street food stall',
              '꼬치에 고기와 채소를 끼웠어요', 'I put meat and vegetables on the skewers'))
E('어묵', meanings=['fish cake', 'boiled fish paste'],
  examples=ex('겨울에는 따뜻한 어묵 국물이 생각나요', 'In winter I crave warm fish cake broth',
              '어묵을 꼬치에 꽂아서 팔아요', 'They sell fish cake on skewers'))
E('조림', meanings=['braised dish', 'food simmered in seasoned broth'],
  examples=ex('생선 조림', 'braised fish',
              '감자조림을 만들었어요', 'I made braised potatoes',
              '밥반찬으로는 장조림이 인기가 많아요', 'Soy-braised beef is popular as a side dish for rice'),
  notes=['Related: 졸이다 (to reduce/boil down)'])
E('죽', add_examples=ex('아플 때는 죽을 먹는 게 좋아요', "When you're sick, it's good to eat porridge"))
E('음료수', meanings=['beverage', 'drink', 'soft drink'],
  add_examples=ex('시원한 음료수 한 잔 주세요', 'A glass of cold drink, please'))
E('커피', meanings=['coffee'],
  examples=ex('아침마다 커피를 마셔요', 'I drink coffee every morning',
              '커피 한 잔 주세요', 'A cup of coffee, please'))
E('술', meanings=['alcohol', 'liquor'],
  examples=ex('저는 술을 잘 못 마셔요', "I can't drink alcohol very well",
              '술을 마시고 운전하면 안 돼요', "You must not drive after drinking alcohol"))
E('탄산음료', add_notes=['Standard spelling is written without a space: 탄산음료'])
E('녹차', add_examples=ex('식사 후에 녹차를 한 잔 마셨어요', 'I had a cup of green tea after the meal'))

# ---------- 재료
E('소고기', meanings=['beef'], add_notes=['쇠고기 is an equally standard variant of 소고기'])
E('계', meanings=['chicken (Sino-Korean 鷄, used in compounds)'],
  examples=ex('계란', 'egg (chicken egg)',
              '계육', 'chicken meat'),
  notes=['계 = 닭; 닭 is the native Korean word', 'Related: 계란 (egg), 닭고기 (chicken meat)'])
E('후추', meanings=['pepper', 'black pepper'])
E('간장', meanings=['soy sauce'],
  examples=ex('간장에 찍어 먹어요', 'I eat it dipped in soy sauce',
              '간장으로 간을 했어요', 'I seasoned it with soy sauce'),
  notes=['Related: 된장 (soybean paste), 고추장 (red pepper paste)'])
E('양념', meanings=['seasoning', 'marinade', 'sauce (seasoning mix)'],
  add_examples=ex('양념 갈비', 'marinated ribs'))
E('육수', meanings=['stock', 'broth (made from meat, anchovies, etc.)'])
E('곡물', add_notes=['Related: 쌀 (rice), 밀가루 (flour), 벼 (rice plant)'])

# ---------- 요리
E('볶다', add_examples=[])
for k, e in ALL['볶다'].examples:
    if k == '고추를 볶다':
        e[:] = ['to stir-fry peppers']
for k, e in ALL['다지다'].examples:
    if k == '고기를 다지다':
        e[:] = ['to mince meat']
E('버무리다', examples=ex('양념을 버무렸어요', 'I mixed in the seasoning',
                         '김치 속을 버무리다', 'to mix the kimchi filling'))
E('졸이다', examples=ex('국물을 졸였어요', 'I reduced the broth',
                       '생선을 간장에 졸였어요', 'I braised the fish in soy sauce'))
E('떠 먹다', meanings=['to scoop up and eat (with a spoon)', 'to have a spoonful'],
  examples=ex('국을 숟가락으로 떠 먹었어요', 'I ate the soup scooping it with a spoon',
              '아이스크림을 떠 먹다', 'to eat ice cream with a spoon'),
  notes=['Written 떠먹다 in standard spelling (one word)'])
E('긁어 먹다', meanings=['to scrape and eat', 'to squeeze money out of someone', 'to extort'])

# ---------- 맛
E('걸쭉하다', meanings=['to be thick (of a liquid)', 'to be viscous'],
  examples=ex('죽이 걸쭉해요', 'The porridge is thick',
              '국물이 걸쭉하게 끓었어요', 'The broth has boiled down thick'))
E('기름기 있다', meanings=['to be oily', 'to be greasy', 'to be fatty'],
  examples=ex('이 고기는 기름기가 너무 많아요', 'This meat is too fatty',
              '기름기 있는 음식은 별로 안 좋아해요', "I don't really like oily food"),
  notes=['Also: 기름기가 많다 (to be very oily)'])
E('자극적인 음식', meanings=['stimulating food', 'strongly flavored food (very spicy, salty, etc.)'],
  examples=ex('자극적인 음식은 위에 안 좋아요', 'Strongly flavored food is bad for the stomach',
              '아이에게 너무 자극적인 음식을 주지 마세요', "Don't give children food that's too strongly flavored"))

# ---------- 식습관
E('식사', meanings=['meal', 'eating a meal'],
  add_notes=['식사하다 = to have a meal (polite word for 먹다)'])
E('굶다', meanings=['to starve', 'to skip a meal', 'to fast'],
  add_examples=ex('다이어트한다고 아침을 굶었어요', 'I skipped breakfast because I am on a diet'))
for k, e in ALL['굶다'].examples:
    pass
ALL['굶다'].examples = [[k.replace('라마단 기간이 되어되자', '라마단 기간이 되자'), e] for k, e in ALL['굶다'].examples]
E('섭취', meanings=['intake', 'consumption', 'to take in (food, nutrients)'],
  add_examples=ex('비타민을 충분히 섭취하세요', 'Make sure to take in enough vitamins'))
E('식후', meanings=['after a meal', 'after meals'],
  examples=ex('이 약은 식후 30분에 드세요', 'Take this medicine 30 minutes after meals',
              '식후에 커피를 한 잔 마시는 걸 좋아해요', 'I like having a cup of coffee after meals'),
  notes=['Opposite: 식전 (before a meal)'])
E('후식', meanings=['dessert'],
  examples=ex('식사 후에 후식으로 과일이 나왔어요', 'Fruit was served as dessert after the meal',
              '후식은 뭘로 하시겠어요?', 'What would you like for dessert?'))
E('건강식품', meanings=['health food', 'dietary supplement'],
  examples=ex('부모님께 건강식품을 사 드렸어요', 'I bought health food for my parents',
              '건강식품 가게에서 홍삼을 샀어요', 'I bought red ginseng at a health food store'))
E('야식', meanings=['late-night snack', 'late-night meal'])

# ---------- 기타
E('깔다', meanings=['to lay', 'to spread'],
  examples=ex('식탁보를 깔았어요', 'I spread the tablecloth',
              '바닥에 돗자리를 깔고 앉았어요', 'I spread a mat on the ground and sat down'))
E('마시오', meanings=['Drink (formal written imperative of 마시다)'],
  examples=ex('흔들어서 마시오', 'Shake before drinking',
              '식후 30분에 물과 함께 마시오', 'Drink with water 30 minutes after meals'),
  notes=['Used mostly on signs and instructions: -시오 / -(으)시오 is the formal written command ending'])
E('낱개', meanings=['single item', 'individual piece'])

# ---------- 식당 (장소)
E('돌아가면서 내다', meanings=['to take turns paying'],
  examples=ex('우리는 밥값을 돌아가면서 내요', 'We take turns paying for meals',
              '오늘은 제가 낼게요. 다음에는 돌아가면서 내요', "I'll pay today. Next time, let's take turns"),
  notes=['Related: 각자 내다 (each pays their own)'])
E('각자 내다', meanings=['to split the bill', 'to pay separately (go Dutch)'],
  examples=ex('오늘은 각자 낼까요?', 'Shall we each pay for ourselves today?',
              '친구들과 밥을 먹고 각자 냈어요', 'I ate with friends and we each paid our own share'),
  notes=['Related: 돌아가면서 내다 (take turns paying), 더치페이 (go Dutch)'])
E('전문점', examples=ex('막걸리 전문점', 'makgeolli specialty shop',
                      '커피 전문점', 'coffee specialty shop',
                      '이 동네에는 칼국수 전문점이 많아요', 'There are many noodle-soup specialty shops in this neighborhood'))

# ---------- save


def save_rel(rel, cards):
    for c in cards:
        fix_text(c)
    cards = finalize(cards, rel)
    save(rel, '', cards)


for rel in ['식사/음식.md', '식사/재료.md', '식사/요리.md', '식사/맛.md', '식사/식습관.md', '식사/기타.md']:
    save_rel(rel, new[rel])
for rel in ['장소/식당.md', '장소/가게.md']:
    save_rel(rel, P.files[rel])
p = BASE + '식사/것.md'
if os.path.exists(p):
    os.remove(p)
    print('removed 식사/것.md')
