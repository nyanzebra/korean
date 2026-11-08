exec(open(W + '/b2.py', encoding='utf-8').read())

def g(rel, word):
    res = [c for c in final[rel].cards if c.word == word]
    assert len(res) == 1, (rel, word, len(res))
    return res[0]

FILLED = 0
def fill(rel, word, exs, meaning=None, notes=None):
    global FILLED
    c = g(rel, word)
    assert not c.examples, (rel, word, 'not empty')
    setex(c, exs)
    FILLED += len(exs)
    if meaning is not None: setmean(c, meaning)
    if notes: addnotes(c, notes)
    return c

# ================= 감정.md =================
E = EMO
c = fill(E, '서럽다', [
    ('친구들이 내 생일을 잊어버려서 너무 서러웠어요', 'My friends forgot my birthday, so I felt really hurt and sad'),
    ('억울하게 혼이 나서 서러워서 눈물이 났어요', 'I was scolded unfairly and cried from feeling so wronged')],
    meaning=['feeling sad and wronged (e.g., when you are unfairly scolded or blamed, or when everyone forgets your birthday)'])
c = fill(E, '부담스럽다', [
    ('갑작스러운 부탁이라서 좀 부담스러워요', 'It is a sudden request, so it feels a bit burdensome'),
    ('너무 비싼 선물은 받기 부담스러워요', 'It is uncomfortable to receive a gift that is too expensive')])
c.meaning = ['burdensome', 'uncomfortable']
c.notes = ['- Often used for requests or favors', '- Related: 부담 (burden, pressure) in 사회_문화/사회와 문화.md']
c = g(E, '오바하다'); c.word = '오버하다'
setmean(c, ['to overreact', 'to go over the top'])
setex(c, [('그렇게까지 화낼 필요는 없잖아, 너무 오버하지 마', "You don't need to get that angry, don't overreact"),
          ('친구가 사소한 일에 오버해서 다들 웃었어요', 'My friend overreacted to a trivial matter and everyone laughed')])
FILLED += 2
c.notes = ['- 오바하다 is a common misspelling; the standard spelling is 오버하다 (from English "over")', '- Related: 호들갑을 떨다 (to make a fuss)']
fill(E, '겁먹다', [
    ('개가 짖자 아이가 겁먹고 울기 시작했어요', 'When the dog barked, the child got scared and started crying'),
    ('겁먹지 마세요, 별일 아니에요', "Don't be scared, it's nothing serious")])
fill(E, '두근거리다', [
    ('시험 결과를 확인하기 전에 가슴이 두근거렸어요', 'My heart was pounding before I checked my exam results'),
    ('좋아하는 사람을 만나면 심장이 두근거려요', 'My heart races when I meet the person I like')])
c = fill(E, '공감되다', [
    ('그 노래 가사에 정말 공감돼요', 'I really relate to the lyrics of that song'),
    ('주인공의 고민이 너무 공감돼서 눈물이 났어요', "The main character's worries were so relatable that I cried")],
    meaning=['to be something that people can identify with or relate to', 'to feel sympathy / to resonate'])
c.notes = ['- Related: 공감하다 (to sympathize, empathize)']
fill(E, '설레다', [
    ('내일이 소풍이라 너무 설레요', 'Tomorrow is the picnic, so I am so excited'),
    ('첫 데이트를 앞두고 가슴이 설렜어요', 'My heart fluttered before the first date')])
c = fill(E, '마음의 여유를 찾다', [
    ('바쁜 일상 속에서도 마음의 여유를 찾으려고 노력해요', 'I try to find peace of mind even in my busy daily life'),
    ('여행을 다녀온 뒤에 마음의 여유를 찾았어요', 'I found peace of mind after coming back from the trip')])
c.notes = ['- 마음의 여유가 있다 is about having a spacious/open heart and mind']
c = g(E, '마음을 통하다'); c.word = '마음이 통하다'
setmean(c, ['for hearts to connect', 'to understand each other', 'to be on the same wavelength'])
setex(c, [('우리는 처음 만났을 때부터 마음이 통했어요', 'We clicked from the moment we first met'),
          ('마음이 통하는 친구가 한 명만 있어도 힘이 돼요', 'Even having one friend who really understands you is a great support')])
FILLED += 2
c.notes = ['- Related: 마음이 맞다 (to get along, be compatible), 공감하다 (to empathize)']
c = fill(E, '얌체', [
    ('줄을 안 서고 새치기하는 얌체 같은 사람이 있어요', 'There is a selfish person who cuts in line instead of waiting'),
    ('얌체처럼 자기 것만 챙기지 마', "Don't just look out for yourself like a freeloader")],
    meaning=['selfish person', 'a person who shrewdly puts their own interests first without caring about others'])
fill(E, '궁금하다', [
    ('그 사람이 요즘 어떻게 지내는지 궁금해요', 'I am curious how that person is doing these days'),
    ('결과가 너무 궁금해서 잠이 안 와요', "I'm so curious about the result that I can't sleep")])
c = g(E, '감정')
rep(c, '뿌뜻하다', '뿌듯하다')
c = g(E, '즐겁다'); setmean(c, ['to be enjoyable', 'to be pleasant', 'to be fun'])
rep(c, 'merry christmas', 'Merry Christmas')
c.notes = ['- Related: 즐기다 (to enjoy), 신나다 (to be thrilled)']
c = g(E, '놀라다'); rep(c, '소식을 들고 놀랐어요', '소식을 듣고 놀랐어요')
c = g(E, '으쓱거리다'); setmean(c, ['to shrug one\'s shoulders', 'to swagger', 'to be conceited', 'to be vain'])
c = g(E, '천하다')
delex(c, '천하무적')
addex(c, [('신분이 천하다고 사람을 무시해서는 안 돼요', "You shouldn't look down on people because of a low social status")])
c = g(REG, '아쉽다')
rep(c, '퀴즈에 틀린 걸 너무 아쉬워마세요', '퀴즈를 틀린 걸 너무 아쉬워하지 마세요')
c = g(E, '동기')
rep(c, '문제 시(視)하고', '문제시하고')
c.notes = ['- https://hinative.com/questions/24883124', '- Related: 계기 (the trigger or occasion for starting something), 목적 (purpose)']
c = g(E, '계기')
rep(c, 'This will be good opportunity', 'This will be a good opportunity')
c.notes = ['- https://hinative.com/questions/24883124', '- Related: 동기 (motivation), 기회 (opportunity)']
c = g(E, '목적')
c.notes.append('- Related: 의도 (intention), 목표 (goal), 동기 (motive)')
c = g(E, '목표')
c.notes.append('- Related: 목적 (purpose), 의도 (intention)')
# 진심
c = g(E, '진심')
setmean(c, ['sincerity', 'true feelings', 'sincere', 'genuine', '(진심으로) sincerely, truly, from the heart'])
addex(c, [('진심으로 사과드립니다', 'I sincerely apologize')])
c.notes = ['- 진심 is a noun (true feelings); 진심으로 is the adverb "sincerely / truly"', '- Related: 성의 (sincere effort), 진지하다 (to be serious), 성실하다 (to be sincere/diligent)']
c = g(E, '성의')
c.notes = [n for n in c.notes]
# 행복
c = g(E, '행복')
setmean(c, ['happiness', 'joy'])
addnotes(c, ['- See the quote in 성공_성취/행복과_노력.md: "행복이란 타인을 행복하게 해주려는 노력의 부산물이다"', '- Related: 행복하다 (to be happy), 행복감 (sense of happiness), 기쁨 (joy)'])
# 두렵다, etc: flat -> done by parser. ensure English cleanup
c = g(E, '두려워하다')
# 사랑 etc fine
c = g(E, '의도')
c.notes = ['- Related: 목적 (purpose), 목표 (goal), 계획 (plan), 뜻 (intention/meaning)']
c.tags = ' #abstract'
c = g(E, '호감')
rep(c, '따라서, 호감을 갖는 또 다른 존재만이 제게 호감을 보일 수 있는 거죠.', '__DEL__', allow_missing=True)
delex(c, '__DEL__')
c.notes = ['- The "smash" in "smash or pass"', '- Related: 호감형 (a likable type / person who makes a good impression)']
c = g(E, '위로하다')
c.tags = ' #abstract'
c.notes = ['- Related: 위로 (comfort), 달래다 (to soothe), 격려하다 (to encourage)']
c = g(E, '발그레하다')
addex(c, [('추운 날씨에 볼이 발그레해졌어요', 'Her cheeks turned rosy in the cold weather')])
c.notes = ['- Related: 빨갛다 (to be red), 붉어지다 (to turn red)']
