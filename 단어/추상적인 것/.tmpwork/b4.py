exec(open(W + '/b3.py', encoding='utf-8').read())

# ================= 생각_마음 =================
M = MIND
rep(g(M, '떠오르다'), '머리카락 떠오를', '머리카락이 떠오를')
rep(g(M, '마음을 단단히 먹다'), '공부 하려고', '공부하려고')
fill(M, '기도하다', [
    ('매일 아침 가족의 건강을 위해 기도해요', "I pray every morning for my family's health"),
    ('시험을 앞두고 합격하게 해 달라고 기도했어요', 'Before the exam, I prayed that I would pass')])
c = g(M, '주의하다'); setmean(c, ['to pay attention to', 'to be careful', 'to take care'])
c.notes = ['- Related: 주의 (caution, attention) in 개념_추상/개념.md']
c = g(M, '마음 맞다'); c.word = '마음이 맞다'
c = g(M, '마음이 놓다'); c.word = '마음이 놓이다'
setmean(c, ['to feel relieved', 'to be at ease'])
setex(c, [('네가 옆에 있으니까 마음이 놓여요', "I feel at ease because you're by my side"),
          ('아이가 무사히 도착했다는 연락을 받고 마음이 놓였어요', 'I felt relieved when I heard that the child had arrived safely'),
          ('일이 좀 잘된다고 마음을 놓아서는 안 된다', "Don't relax your attention because of a small success or two")])
c.notes = ['- 마음을 놓다 (the last example) means to let one\'s guard down / relax one\'s attention, while 마음이 놓이다 means to feel relieved']
c = g(M, '정신')
rep(c, 'collect one\'s mind, pay attention', 'to pull oneself together, to come to one\'s senses')
fill(M, '정신 건강', [
    ('정신 건강을 위해 매일 산책을 해요', 'I take a walk every day for my mental health'),
    ('요즘 정신 건강이 걱정돼서 상담을 받아 보려고요', "I'm worried about my mental health these days, so I'm thinking of getting counseling")])
c = fill(M, '스트레스가 쌓이다', [
    ('일이 너무 많아서 스트레스가 쌓였어요', 'I have so much work that my stress has piled up'),
    ('스트레스가 쌓이면 잠을 잘 못 자요', "When stress piles up, I can't sleep well")])
c.notes = ['- Related: 스트레스 받다 (to be stressed), 스트레스를 풀다 (to relieve stress)']
c = fill(M, '스트레스를 풀다', [
    ('저는 운동으로 스트레스를 풀어요', 'I relieve stress by exercising'),
    ('노래방에 가서 스트레스를 풀었어요', 'I went to karaoke and relieved my stress')])
c.notes = ['- Related: 스트레스가 쌓이다 (to have stress pile up), 스트레스 해소 방법 (how to relieve stress)']
c = fill(M, '스트레스 해소 방법', [
    ('가장 좋은 스트레스 해소 방법이 뭐예요?', 'What is the best way to relieve stress?'),
    ('제 스트레스 해소 방법은 산책이에요', 'My way of relieving stress is taking a walk')])
c.notes = ['- Related: 스트레스를 풀다 (to relieve stress), 해소하다 (to resolve, to relieve)']
c = g(M, '정신이 없다')
setmean(c, ["to be so busy or distracted that one can't think straight", 'to be absorbed (in something)', 'scatter-brained'])
delex(c, '먹이와 포도')
addex(c, [('요즘 일이 너무 많아서 정신이 없어요', "I'm so busy these days that I can't think straight"),
          ('그는 포도를 먹느라고 정신이 없었다', 'He was so absorbed in eating grapes that he forgot everything else')])
rep(g(M, '겪다'), 'suffer a guest', 'to host (put up with) guests')
c = g(M, '정중하다')
rep(c, '그니까', '그러니까')
c.examples[0][1] = ['So please try to be a bit more polite']
addex(c, [('그는 모두에게 정중하게 인사했어요', 'He greeted everyone politely')])
c.notes = ['- Related: 예의 바르다 (to be well-mannered), 공손하다 (to be respectful)']
c = fill(M, '존경', [
    ('저는 부모님을 깊이 존경해요', 'I deeply respect my parents'),
    ('그는 많은 사람들에게 존경을 받고 있어요', 'He is respected by many people')])
c.notes = ['- Related: 존경심 (feeling of respect), 존경하다 (to respect)']
c = g(M, '존경심')
setmean(c, ['respect', 'feeling of respect (존경 + 심 "heart/mind")'])
c.notes = ['- Related: 존경 (respect), 존경하다 (to respect)']
rep(g(M, '중심'), '자기 중심 적인', '자기중심적인')
c = g(M, '집중력')
c.notes = ['- Related: 기억력 (memory), 효율성 (efficiency, in 성공_성취/효율_생산성.md), 집중하다 (to concentrate)']
c = g(M, '기억력')
c.notes = ['- Related: 집중력 (concentration), 기억하다 (to remember)']
addex(c, [('나이가 들수록 기억력이 떨어져요', 'Your memory gets worse as you get older')])

# ================= 느낌 =================
c = g('감정_심리/느낌.md', '왠지 실감 안나는데'); c.word = '왠지 실감이 안 나는데'
setex(c, [('내일 결혼한다는 게 왠지 실감이 안 나는데', "It somehow doesn't feel real that I'm getting married tomorrow"),
          ('합격 소식을 들었는데 아직도 실감이 안 나요', "I heard I passed, but it still doesn't feel real")])
FILLED += 2
c.notes = ['- 실감이 나다 = to feel real; 실감이 안 나다 = it does not feel real']

# ================= 실수_두려움 =================
c = g('감정_심리/실수_두려움.md', '주로')
delex(c, '일주일에 주로')
addex(c, [('저는 일주일에 주로 5일 일해요', 'I mainly work 5 days a week')])
final['감정_심리/실수_두려움.md'].post = ['### Note',
    'From: "살면서 저지를 수 있는 가장 큰 실수는 실수할까 봐 끊임없이 걱정하는 것이다"',
    '(The biggest mistake you can make in life is to constantly worry about making mistakes.)']

# ================= 후회 =================
final[REG].pre = ['# 후회 (Regret)']
c = g(REG, '후회')
delex(c, '후회하다')
rep(c, '평생 후회할 거 같아요', '평생 후회할 것 같아요')
c.notes = ['- Related: 후회하다 (to regret), 유감 (regret, pity), 아쉽다 (to feel something is a pity)']
c = g(REG, '유감')
setmean(c, ['regret', 'pity', 'remorse', '(formal) being sorry that something unfortunate happened'])
c.notes = ['- Related: 유감스럽다 (to be regrettable), 안타깝다 (to feel sorry), 아쉽다 (to be a pity)']
c = g(REG, '유감스럽다')
addex(c, [('유감스럽게도 초대에 응할 수 없습니다', 'Unfortunately, I cannot accept the invitation')])
c.notes = ['- More formal than 아쉽다 and 안타깝다']
c = g(REG, '안타깝다')
addex(c, [('아픈 친구를 도와주지 못해서 안타까워요', "I feel sorry that I couldn't help my sick friend"),
          ('안타깝게도 우리 팀이 경기에서 졌어요', 'Unfortunately, our team lost the game')])
c.notes = ['- 안타깝다: feeling sorry or frustrated about a situation (often for someone else)',
           '- 아쉽다: feeling that something fell short or ended too soon (a personal "what a pity")',
           '- 유감스럽다: formal "regrettable"']
c = g(REG, '아쉽다')
c.notes = ['- 아쉽다: feeling that something fell short or ended too soon (a personal "what a pity")',
           '- Related: 안타깝다 (to feel sorry or frustrated), 유감스럽다 (regrettable)']
c = g(REG, '할 수 있었는데')
addex(c, [('더 열심히 할 수 있었는데...', 'I could have tried harder...')])
c = g(REG, '해야 했는데')
addex(c, [('미리 예약을 해야 했는데 깜빡했어요', 'I should have made a reservation in advance, but I forgot')])
c = g(REG, '해야만 했는데')
setmean(c, ['should have had to do (emphatic)', 'absolutely had to do (but did not)'])
setex(c, [('해야만 했는데 못 했어요', 'I absolutely had to do it, but I could not'),
          ('그때 사과를 해야만 했는데', 'I really had to apologize back then...')])
final[REG].post = ['### Note',
    'From: "인생에서 가장 슬픈 3가지: 할 수 있었는데..., 해야 했는데..., 해야만 했는데..."',
    '(The three saddest things in life: "I could have done it...", "I should have done it...", "I absolutely had to do it...")']

# ================= 개인_특성 =================
T = TRAIT
fam = {
    '특질': 'inherent nature, fundamental quality (more formal/written)',
    '특성': 'unique trait or property of a person or thing',
    '특징': 'notable feature, distinguishing mark',
    '특기': 'special skill, forte',
    '성질': 'nature, temperament; physical or chemical property',
}
for w in fam:
    c = g(T, w)
    others = '; '.join('%s (%s)' % (k, v) for k, v in fam.items() if k != w)
    c.notes = ['- %s: %s' % (w, fam[w]), '- Compare: ' + others]
c = fill(T, '특질', [
    ('그 지역 사람들의 공통된 특질을 연구했어요', 'I studied the common characteristics of the people in that region'),
    ('이 식물은 독특한 특질을 가지고 있어요', 'This plant has a unique characteristic')],
    meaning=['trait', 'characteristic (formal, written)', 'inherent quality'])
c.notes = ['- 특질: ' + fam['특질'], '- Compare: ' + '; '.join('%s (%s)' % (k, v) for k, v in fam.items() if k != '특질')]
fill(T, '정직하다', [('그는 정직해서 모두에게 신뢰를 받아요', 'He is honest, so everyone trusts him'),
                     ('정직하게 말해 줘서 고마워요', 'Thank you for being honest with me')])
fill(T, '똘똘하다', [('그 아이는 어려도 아주 똘똘해요', 'That child is very sharp even though she is young'),
                     ('우리 막내가 똘똘해서 뭐든지 금방 배워요', 'Our youngest is so smart that she learns everything quickly')])
fill(T, '둔하다', [('저는 눈치가 둔해서 분위기를 잘 못 읽어요', "I'm slow on the uptake, so I can't read the mood well"),
                   ('그는 몸이 둔해서 운동을 잘 못해요', 'He is clumsy and not good at sports')])
fill(T, '대단하다', [('혼자서 그 일을 해내다니 정말 대단해요', "It's really amazing that you did that all by yourself"),
                     ('그 가수는 요즘 대단한 인기를 끌고 있어요', 'That singer is enormously popular these days')])
fill(T, '해맑다', [('아이가 해맑게 웃고 있어요', 'The child is smiling innocently'),
                   ('그의 해맑은 얼굴을 보면 기분이 좋아져요', 'I feel good when I see his bright, innocent face')])
c = g(T, '곱다'); rep(c, '허리다 곱다', '허리가 곱다')
rep(g(T, '자존심'), 'self-repect', 'self-respect')
c = g(T, '번덕스럽다'); c.word = '변덕스럽다'
for e in c.examples:
    e[0] = e[0].replace('번덕스', '변덕스')
c = g(T, '유용하다')
setex(c, [('이 앱은 여행할 때 아주 유용해요', 'This app is very useful when traveling'),
          ('유용한 정보를 알려 줘서 고마워요', 'Thank you for telling me useful information')])
c.notes = ['- Not to be confused with 유용 (流用, to divert or misappropriate funds): 회사 돈을 유용하다 = to misappropriate company funds']
fill(T, '약점/단점/나쁜점', [('제 가장 큰 약점은 걱정이 너무 많다는 거예요', 'My biggest weakness is that I worry too much'),
                          ('이 휴대폰의 단점은 배터리가 빨리 닳는 거예요', 'The downside of this phone is that its battery drains quickly')])
fill(T, '강점/장점/좋은점', [('제 강점은 끈기예요', 'My strength is perseverance'),
                          ('이 도시의 장점은 교통이 편리하다는 거예요', 'The advantage of this city is that transportation is convenient')])
fill('개인_특성/외모.md', '모습', [('그는 어릴 때와 모습이 많이 달라졌어요', 'He looks very different from when he was a child'),
                                  ('거울 속 내 모습이 낯설게 느껴졌어요', 'My reflection in the mirror felt unfamiliar')],
     meaning=['appearance', 'shape', 'form', 'figure'])

# ================= 윤리_신념 =================
fill(RESP, '제가 책임지겠습니다', [('이번 일은 제가 책임지겠습니다', 'I will take responsibility for this matter'),
                                    ('문제가 생기면 제가 끝까지 책임지겠습니다', 'If any problem arises, I will take responsibility to the end')])
fill(DUTY, '할 의무가 있다', [('시민은 세금을 낼 의무가 있어요', 'Citizens have a duty to pay taxes'),
                              ('회사는 직원의 안전을 지킬 의무가 있어요', "A company has an obligation to protect its employees' safety")])
fill(DUTY, '의무감이 들다', [('도와줘야 한다는 의무감이 들었어요', 'I felt a sense of duty to help'),
                             ('부모님을 모셔야 한다는 의무감에 고향으로 돌아왔어요', 'Out of a sense of duty to look after my parents, I returned to my hometown')])
c = g(DUTY, '의무')
c.notes = ['- Related: 할 의무가 있다 (to have a duty to), 의무감이 들다 (to feel obligated), 권리 (right) in 사회_문화/사회와 문화.md, 책임 (responsibility)']
c = g(RESP, '책임감')
c.notes = ['- Related: 책임 (responsibility), 제가 책임지겠습니다 (I will take responsibility)']
c = g('윤리_신념/신념_신뢰.md', '정의'); setmean(c, ['justice', 'definition'])
c = g('윤리_신념/신념_신뢰.md', '실현하다'); setmean(c, ['to realize (a dream)', 'to materialize', 'to put into practice'])
final['윤리_신념/신념_신뢰.md'].post = ['### Note',
    'From: "잘 모르고 무식한 사람의 신념을 가지는 것만큼 무서운 것이 없다"',
    "(Nothing is as frightening as the convictions of ignorant people who don't know any better.)"]

# ================= 상태_변화 =================
final[STATE].pre = ['# 상태 (States & Conditions)']
c = fill(STATE, '보상', [('회사는 직원들에게 피해에 대한 보상을 해 주었어요', 'The company compensated its employees for the damage'),
                         ('열심히 노력한 것에 대한 보상을 받았어요', 'I received a reward for my hard work')],
         meaning=['compensation', 'reward', 'reimbursement'])
c.notes = ['- 보상 (補償): compensation for loss or damage', '- 보상 (報償): reward for effort']
fill(STATE, '지형', [('한국은 산이 많은 지형이에요', 'Korea has mountainous terrain'),
                     ('지형을 고려해서 도로를 설계했어요', 'We designed the road considering the terrain')],
     meaning=['terrain', 'topography'])
c = g(STATE, '소유')
setex(c, [e for e in [
    ['차량을 소유하다', ['to own a vehicle']],
]] + [[ko, en] for ko, en in c.examples if '풀소유' not in ko and '풀소유' not in ' '.join(en)][0:0] + [e for e in c.examples if not e[0].startswith('풀소유')]) if False else None
c.examples = [e for e in c.examples if not e[0].startswith('풀소유')]
c.examples.insert(0, ['차량을 소유하고 있어요', ['I own a vehicle']])
rep(c, '메출', '매출')
final[RISK].pre = ['# 위험 (Threat & Danger)']
fill(RISK, '위협', [('그 나라의 핵 개발은 이웃 나라들에게 큰 위협이 돼요', "That country's nuclear development is a major threat to its neighbors"),
                    ('그는 나를 해치겠다고 위협했어요', 'He threatened to harm me')])
c = g(RISK, '위기'); c.notes = ['- Related: 위협 (threat), 위험 (danger), 기회 (opportunity) in 성공_성취/기회.md']
rep(g('상태_변화/연속.md', '첩출하다'), 'series of misfortune', 'series of misfortunes')
rep(g('상태_변화/유지.md', '유지하다'), 'remains in', 'remain in')

# ================= 성공_성취 =================
c = fill(ACH, '업적', [('그는 과학 분야에서 큰 업적을 남겼어요', 'He left great achievements in the field of science'),
                      ('세종대왕의 업적을 기리는 기념관이 있어요', "There is a memorial hall honoring King Sejong's achievements")],
         meaning=['achievement', 'accomplishment', 'great work'])
c = fill(INFL, '미치다', [('날씨는 농작물에 큰 영향을 미쳐요', 'The weather has a big effect on crops'),
                         ('그는 게임에 미쳐서 밤새 했어요', 'He was crazy about the game and played all night'),
                         ('아직 목표에 미치지 못했어요', "I haven't reached my goal yet")],
         meaning=['to affect, to have an effect on (에 영향을 미치다)', 'to go crazy, to be obsessed with (에 미치다)', 'to reach, to come up to', 'to fall short of (미치지 못하다)'])
c.notes = ['- Related: 영향 (influence), 영향을 주다 (to influence)']
c = g(INFL, '영향'); c.notes = ['- Related: 미치다 (영향을 미치다 = to have an influence), 영향을 주다 / 받다 (to give / receive influence)']
rep(g('성공_성취/기회.md', '기회'), '"이번 기회에', '이번 기회에')
c = g('성공_성취/기회.md', '기회'); c.notes = ['- Related: 위기 (crisis) in 상태_변화/위험.md, 계기 (trigger, occasion) in 감정_심리/감정.md']
c = g(HAPPY, '~게 해주다'); c.word = '~게 해 주다'
setmean(c, ['to let / allow / enable someone to do something', 'to do something so that someone can feel or do something'])
setex(c, [('아이들이 꿈을 이룰 수 있게 해 주다', 'To enable children to achieve their dreams'),
          ('행복하게 해 주다', 'To make someone happy')])
c = g(HAPPY, '~게 하다'); setmean(c, ['to make / let / cause someone to do something'])
c = g(HAPPY, '노력'); c.notes = ['- Related: 노력하다 (to make an effort), 열심히 (hard)']
c = g(EFF, '비생산'); c.word = '비생산적'
c.notes = ['- Related: 생산적 (productive), 효율 (efficiency)']
c = g(EFF, '효율'); c.notes = ['- Related: 효율성 (efficiency), 효율적 (efficient)']
c = g(EFF, '효율성'); c.notes = ['- Related: 효율 (efficiency), 효율적 (efficient)', '- Related: 집중력 (concentration, focus) in 감정_심리/생각_마음.md']

# ================= 소통_관계 =================
c = g('소통_관계/대응.md', '대하다')
rep(c, '사람을 대하기 싫어하다', '사람 대하기를 싫어하다')
rep(c, "don't like to treat/receive people", 'to dislike dealing with people')
c = g('소통_관계/조언.md', '조언')
c.examples[0][1] = ['advice from an expert']
c.notes = ['- Related: 충고 (advice/warning, more direct), 제안 (proposal)']
c = g('소통_관계/조언.md', '충고'); c.notes = ['- Related: 조언 (advice, neutral tone), 제안 (proposal)']
fill(OPIN, '주관적', [('그건 네 주관적인 생각일 뿐이야', "That's just your subjective opinion"),
                      ('맛은 사람마다 다른 주관적인 평가예요', 'Taste is a subjective judgment that differs from person to person')])
fill(OPIN, '객관적', [('객관적으로 보면 그 계획은 너무 위험해요', 'Objectively speaking, that plan is too risky'),
                      ('객관적인 자료를 바탕으로 판단해야 해요', 'You have to judge based on objective data')])
rep(g(OPIN, '내키다'), '마음내키지 않는 대답', '마음 내키지 않는 대답')
c = fill(OPIN, '변호하다', [('변호사가 피고인을 변호했어요', 'The lawyer defended the defendant'),
                            ('친구의 잘못을 변호해 주고 싶지는 않아요', "I don't want to defend my friend's mistake")])
c.notes = ['- Related: 변호사 (lawyer), 옹호하다 (to advocate, to support)']
c = g(OPIN, '의견')
c.notes = ['- Related: 관점 (viewpoint), 생각 (thought), 주장 (claim), 내 의견으로는 (in my opinion)']
c = g(OPIN, '나의 관점'); c.notes = ['- Related: 관점 (viewpoint) in 개념_추상/관점.md']
c = g(OPIN, '내 관점으로는'); c.notes = ['- Related: 관점 (viewpoint) in 개념_추상/관점.md']
final[COMM].pre = ['# 의사소통 (Communication)']
c = g(COMM, '연결')
rep(c, '연결을 끊었어', '연결을 끊었어요')
c.examples = [e for e in c.examples if e[0] != '연결하다']
c.notes = ['- Related: 연결하다 (to connect), 링크 (link), 이음 (joining), 관계 (relationship)']
c = g(COMM, '오해'); c.notes = ['- Related: 오도하다 (to mislead), 착오 (error), 오류 (mistake), 이해 (understanding)']

# ================= 시간_공간 =================
fill('시간_공간/수명.md', '수명', [('한국인의 평균 수명은 점점 늘어나고 있어요', 'The average lifespan of Koreans keeps increasing'),
                                   ('이 배터리는 수명이 짧아서 자주 바꿔야 해요', 'This battery has a short life, so I have to replace it often')])
c = g(TIME, '점심'); setmean(c, ['lunch', 'noon (midday)'])
c = g(TIME, '아무때나'); c.word = '아무 때나'
for e in c.examples: e[0] = e[0].replace('아무때나', '아무 때나')
c = g(TIME, '시각')
c.examples = [['출발 시각', ['Departure time']], ['현재 시각은 오후 세 시입니다', ['The current time is 3 PM']]]
c = g(TIME, '기간')
c.examples = [['긴 기간', ['Long period']], ['한 달 동안의 기간', ['A period of one month']]]
c = g(TIME, '한밤중')
c.examples = [['한밤중에 깼어요', ['I woke up in the middle of the night']], ['한밤중에 전화가 와서 깜짝 놀랐어요', ['I was startled by a phone call in the middle of the night']]]
c = fill(TIME, '년', [('2024년에 한국에 왔어요', 'I came to Korea in 2024'),
                     ('한국어를 공부한 지 3년이 됐어요', 'It has been three years since I started studying Korean')],
         meaning=['year', '(counter) years'])
c.notes = ['- Related: 해 (year, native Korean), 연도 (year, as a date), 올해 (this year)']
c = g(TIME, '어느새'); c.notes = c.notes
c = g(LOC, '중간'); c.tags = ' #location #middle'
c = g(LOC, '방향'); c.tags = ' #location #direction'
rep(c, '어떤 방향?', '어느 방향이에요?')
rep(c, 'What direction?', 'Which direction is it?')
c = g(LOC, '어디'); rep(c, '어디에요?', '어디예요?')
c = g(LOC, '아무데나'); c.word = '아무 데나'
for e in c.examples: e[0] = e[0].replace('아무데나', '아무 데나')
c = g(LOC, '각 곳'); c.word = '각지'
setmean(c, ['every place', 'various places (各地)'])
setex(c, [('전국 각지에서 사람들이 모였어요', 'People gathered from all over the country'),
          ('세계 각지의 음식을 맛볼 수 있어요', 'You can taste food from all around the world')])
c.notes = ['- Related: 곳곳 (here and there), 여기저기 (all over the place)']

# ================= 프로세스_절차 =================
fill(PROC, '평가하다', [('학생들의 발표를 점수로 평가했어요', "I evaluated the students' presentations with scores"),
                        ('이 제품의 품질을 객관적으로 평가하기는 어려워요', "It's hard to objectively assess this product's quality")])
fill(PROC, '방지하다', [('화재를 방지하기 위해 소화기를 설치했어요', 'We installed fire extinguishers to prevent fires'),
                        ('사고를 방지하려면 안전 수칙을 지켜야 해요', 'To prevent accidents, you have to follow the safety rules')])
fill(PROC, '매기다', [('심사위원들이 참가자들에게 점수를 매겼어요', 'The judges gave scores to the contestants'),
                      ('물건마다 가격을 매겨서 진열했어요', 'We put a price on each item and displayed them')])
c = g(PROC, '절차'); c.notes = ['- Related: 단계 (stage, step), 과정 (process), 순서 (order, sequence)']
c = g(PROC, '단계'); c.notes = ['- Related: 절차 (procedure), 과정 (process)']
c = g(PROC, '과정'); c.notes = ['- Related: 절차 (procedure), 단계 (stage, step), 결과 (result)']
c = g(APPLY, '해당'); c.notes = ['- Related: 해당하다 (to apply to, to correspond to), 적용 (application)']
c = g(APPLY, '해당하다'); c.notes = [n for n in c.notes] + ['- Related: 해당 (noun form: corresponding, relevant)']
c = g(ACT, '작용하다'); c.notes = ['- Related: 작용 (action, function), 영향 (influence)']
c = g(ACT, '작용'); c.notes = ['- Related: 작용하다 (to act, to work), 상호 작용 (interaction), 반응 (reaction)']
