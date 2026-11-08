exec(open(W + '/b4.py', encoding='utf-8').read())

# ================= 개념_추상 =================
GNf = GN
fill(GN, '세상', [('세상에 완벽한 사람은 없어요', 'No one in the world is perfect'),
                  ('세상이 정말 많이 변했네요', 'The world has really changed a lot')])
fill(GN, '것', [('먹을 것 좀 있어요?', 'Do you have anything to eat?'),
                ('중요한 것은 포기하지 않는 거예요', 'The important thing is not to give up')])
c = fill(GN, '이름', [('이름이 뭐예요?', "What's your name?"),
                     ('그 가게는 맛집으로 이름이 났어요', 'That shop has made a name for itself as a great restaurant')],
         meaning=['name', 'title', 'reputation (이름이 나다 = to become well known)'])
c = g(GN, '요인')
c.examples[0] = ['성공의 핵심 요인', ['key factor of success']]
c.notes = ['- Related: 원인 (cause), 요소 (element)']
c = g(GN, '원인'); c.notes = ['- Related: 요인 (factor), 이유 (reason), 결과 (result)']
c = g(GN, '이유'); c.notes = ['- Related: 원인 (cause), 까닭 (reason, native Korean)']
c = g(GN, '결론')
setmean(c, ['conclusion', 'result (of a discussion or decision)'])
c = g(GN, '주의')
setex(c, [('운전할 때는 주의해야 해요', 'You need to be careful when driving'),
          ('주의를 기울이다', 'to pay attention')])
c.notes = ['- Related: 주의하다 (to be careful, to pay attention) in 감정_심리/생각_마음.md', '- 주의 사항 (precautions) is the usual compound; see 사항']
c = g(GN, '사항')
setex(c, [('주의 사항을 꼭 읽어 보세요', 'Please be sure to read the precautions'),
          ('필수 사항', 'required items')])
c = g(GN, '방법'); c.notes = ['- Related: 방식 (manner, way of doing), 수단 (means)']
c = g(GN, '방식'); c.notes = ['- Related: 방법 (method, how to do something)']
c = g(GN, '정보'); c.notes = ['- Related: 추가 정보 (additional information), 소식 (news), 지식 (knowledge)']
c = g(GN, '추가 정보'); c.notes = ['- Related: 정보 (information), 추가하다 (to add)']
c = g(GN, '상황')
c.notes = ['- Related: 사태 (situation, state of affairs), 형편 (circumstances, esp. financial), 처지 (one\'s position)']
c = g(GN, '조건'); c.notes = ['- Related: 여건 (conditions, circumstances), 상황 (situation)']
addex(c, [('좋은 조건으로 계약했어요', 'We signed the contract on good terms')])
c = g(GN, '법칙'); c.notes = ['- Related: 규칙 (rule), 원칙 (principle) in 개인_특성/규율.md']
c = g(GN, '기'); c.tags = ' #abstract'

# 관점.md
c = g(VIEW, '입장')
setmean(c, ['position', 'stance', 'standpoint', 'entrance, admission (入場)'])
addex(c, [('공연장 입장은 7시부터예요', 'Admission to the concert hall starts at 7')])
c.notes = ['- 입장 (立場): position, standpoint', '- 입장 (入場): entering, admission (입장료 = admission fee)', '- Related: 관점 (viewpoint), 처지 (one\'s situation)']
rep(g(VIEW, '별개'), 'a whole another thing', 'a whole other thing')
c = g(VIEW, '전망')
setmean(c, ['view (through a window)', 'prospect', 'future outlook', 'expectation'])
c.tags = ' #abstract #outlook'
c = g(VIEW, '관점'); c.notes = ['- Related: 입장 (position, stance), 시각 (view), 측면 (aspect), 의견 (opinion) in 소통_관계/의견.md']

# 수와 양: month names
c = g(QTY, '삼'); rep(c, '삼 월', '삼월')
c = g(QTY, '사'); rep(c, '사 월', '사월')
c = g(QTY, '오'); rep(c, '오 월', '오월')
c = g(QTY, '육'); rep(c, '육 월', '유월')
c = g(QTY, '칠'); rep(c, '칠 월', '칠월')
c = g(QTY, '구'); rep(c, '구 월', '구월')
c = g(QTY, '양'); c.tags = ' #quantity #amount'
c.notes = ['- Related: 량 (suffix form of 양, as in 생산량), 수량 (quantity) in 사회_문화/사업과 경제.md, 많이 (a lot)']
c = g(QTY, '부분'); c.tags = ' #quantity #part'
c.notes = ['- Related: 일부 (a part, some), 일부분 (a portion), 부분적 (partial), 조각 (piece), 전체 (whole)']
c = g(QTY, '일부'); c.notes = ['- Related: 부분 (part, portion), 나머지 (the rest)']

# 쇼핑과 구매
c = g('개념_추상/쇼핑과 구매.md', '장 보다'); c.word = '장(을) 보다'
c = g('개념_추상/쇼핑과 구매.md', '입어보다'); c.word = '입어 보다'
rep(g('개념_추상/쇼핑과 구매.md', '계산'), 'Please calculate/check me out', "Please ring me up / I'd like to pay")

# 부사 file
final[ADV].pre = ['# 부사와 연결 표현 (Adverbs & Connecting Expressions)']

# ================= 사회_문화 =================
c = fill(SOC, '보이지 않는 규칙', [
    ('한국에는 어른에게 물건을 드릴 때 두 손으로 드리는 보이지 않는 규칙이 있어요', 'In Korea there is an unspoken rule of giving things to elders with both hands'),
    ('회사마다 보이지 않는 규칙이 있어서 처음에는 적응하기 어려워요', 'Every company has unspoken rules, so it is hard to adjust at first')],
    meaning=['unspoken rule', 'unwritten rule'])
c.notes = ['- Related: 불문율 (unwritten law), 규칙 (rule) in 개인_특성/규율.md']
c = g(SOC, '부담'); c.notes = ['- Related: 부담스럽다 (to be burdensome) in 감정_심리/감정.md']
c = g(SOC, '문화'); c.notes = ['- Related: 풍습 (custom), 전통 (tradition)']
c = g(SOC, '풍습'); c.notes = ['- Related: 문화 (culture), 습관 (habit) in 개념_추상/개념.md']
c = g(BIZ, '인정')
setmean(c, ['recognition', 'acknowledgment', '(人情) human feeling, compassion'])
c.notes = ['- 인정 (認定): recognition, acknowledgment (인정하다 = to admit, to acknowledge)', '- 인정 (人情): human feeling, compassion (인정이 없다 = to be cold-hearted)']
rep(g(BIZ, '자본'), 'Capital money', 'Capital stock; paid-in capital', allow_missing=True)
c = g(BIZ, '행사'); c.tags = ' #event #function #sogang #sogang-4A'
c = g(BIZ, '지적 재산'); c.tags = ' #business #legal'
c = g(BIZ, '자금'); c.tags = ' #business #funds'
c = g(BIZ, '수량'); c.notes = ['- Related: 양 (quantity) in 개념_추상/수와 양.md']
c = g(LANG, '주황'); rep(c, '주황 빛', '주황빛')

# ================= 프로세스: 완료_및_완성 =================
CW = '프로세스_절차/완료_및_완성.md'
final[CW] = FileModel()
final[CW].pre = ['# 완료와 완성 (Completion & Perfection)']
final[CW].cards = [
    C('완료 (完了)', ['completion (of a task or process)', 'done, finished, processed'],
      [('결제가 완료되었습니다', 'The payment has been completed'),
       ('다운로드가 완료되면 알려 드릴게요', "I'll let you know when the download is complete"),
       ('신청이 완료됐어요', 'The application has been completed')],
      notes=['- Focuses on a task or process being finished; often used in formal, administrative, or technical contexts',
             '- Examples: 결제 완료 (payment complete), 다운로드 완료, 신청 완료',
             '- Related: 완성 (completion of a creation), 완료하다 (to complete)']),
    C('완성 (完成)', ['completion (of a creation)', 'finished, perfected, fully realized'],
      [('소설을 드디어 완성했어요', 'I finally finished the novel'),
       ('건물이 완성되려면 아직 멀었어요', 'The building is still far from finished'),
       ('드디어 완성됐어요!', "It's finally finished!")],
      notes=['- Focuses on something being fully made or built; used when a work, product, or creation reaches its final form',
             '- Examples: 소설 완성, 작품 완성',
             '- Related: 완료 (completion of a task or process)']),
    C('완벽 (完璧)', ['perfection', 'flawless, perfect'],
      [('완벽한 사람은 없어요', 'No one is perfect'),
       ('그는 완벽주의자예요', 'He is a perfectionist')],
      notes=['- Flawless, with no room for improvement', '- Related: 완벽하다 (to be perfect), 완벽주의자 (perfectionist), 완전 (complete, total)']),
    C('완전 (完全)', ['complete, total', 'completely, totally (casual adverb: "so ~", "totally ~")'],
      [('완전 맛있어요!', "It's so delicious!"),
       ('완전한 자유를 원해요', 'I want complete freedom')],
      notes=['- Often used as an adverb in casual speech', '- Related: 완전히 (completely), 완벽 (perfection)']),
    C('완치 (完治)', ['full recovery', 'complete cure'],
      [('병이 완치됐어요', 'My illness has fully healed'),
       ('완치까지 얼마나 걸려요?', 'How long until a full recovery?')],
      notes=['- Used specifically for recovering completely from an illness', '- Related: 치료 (treatment), 회복 (recovery)']),
]
final[CW].post = [
    '#### Quick comparison',
    '',
    '|Word|Core idea|Typical context|',
    '|---|---|---|',
    '|완료|task is done|admin, tech, processes|',
    '|완성|creation is done|art, writing, building|',
    '|완벽|no flaws|quality, personality|',
    '|완전|totally, fully|adverb, emphasis|',
    '|완치|fully healed|medical|',
    '',
    'The biggest one to keep straight: **완료** is for _doing_ something, **완성** is for _making_ something.',
]

# ================= global post-pass =================
SPLIT_TAGS = ('#vocabulary',)
for rel, fm in final.items():
    for c in fm.cards:
        # reversed examples (English first, Korean in translation line)
        for e in c.examples:
            if not HANGUL.search(e[0]) and e[1] and HANGUL.search(e[1][0]):
                e[0], e[1] = e[1][0], [e[0]]
        if '#vocabulary' in c.tags:
            nm = []
            for m in c.meaning:
                if '(' not in m and ', ' in m:
                    nm.extend(x.strip() for x in m.split(', ') if x.strip())
                else:
                    nm.append(m)
            c.meaning = nm
        c.meaning = [m.strip() for m in c.meaning if m.strip()]

for rel, fm in final.items():
    for c in fm.cards:
        seen = []
        for m in c.meaning:
            if m not in seen: seen.append(m)
        c.meaning = seen
def reorder(rel, words):
    cs = final[rel].cards
    first = []
    for w in words:
        first += [c for c in cs if c.word == w]
    final[rel].cards = first + [c for c in cs if c not in first]
reorder(REG, ['후회', '후회하다', '유감', '유감스럽다', '안타깝다', '아쉽다'])

rep(g(REG, '후회'), '후회 할거야', '후회할 거야')
rep(g(EMO, '그리워하다'), '될거야', '될 거야')
rep(g(APPLY, '해당'), '안되는', '안 되는')
c = g(OPIN, '내키다'); setmean(c, ['to feel inclined to', 'to feel like doing something'])
