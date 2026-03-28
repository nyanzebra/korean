#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# Words that are clearly conjugations or not real vocab
REMOVE_WORDS = {
    # Conjugations in 자연.md
    "필요해", "필요해요", "조심해", "해줄", "좋아해요", "확인해", "감사해요", 
    "확실해", "기억해", "환영해", "연결해", "싫어해요", "중요해요", "어떡해요",
    "환영해요", "실례해요", "해줘야", "해줄래", "해보죠", "부족해",
    
    # Conjugations in 활동/동작.md
    "나가서", "어서요", "어째서", "혼자서", "하면서", "돼서", "들어갈", "무서워",
    "들어가서", "물러서", "지켜봐", "이서요", "가서요", "오셔서",
    
    # Conjugations in 시간.md
    "떠날", "일어날",
    
    # Conjugations in 몸/신체.md
    "제발", "제발요", "어차피", "알다시피", "건배", "발사",
    
    # Conjugations in 장소/장소.md
    "때문이야", "문제야", "제길", "이길", "말하길", "곳이야",
    
    # Conjugations in 사람.md
    "사람이야",
    
    # Conjugations in 직장/직장 생활.md
    "제일", "죽일", "종일", "하루종일", "헤일리", "일하러", "별일",
    
    # Conjugations in 말하기.md
    "말해줘", "오말리", "정말이야", "얘기할", "말이오", "말인데", "말해야",
    "말해요", "말해봐요", "자말",
    
    # Conjugations in 식사/음식.md
    "물어봐", "물어볼", "결국엔",
    
    # Conjugations in 상태/상태.md
    "전화해", "행복해", "걱정마", "걱정할", "화난",
    
    # Conjugations in 건강/의료.md
    "약속해", "약속해요", "치료할", "염병할",
    
    # Conjugations in 교통.md
    "차례야", "리차드", "조차",
    
    # Conjugations in 양 & 질.md
    "원치", "의원님", "요원님", "원할",
    
    # Conjugations in 추상적인 것/것.md
    "사실이야", "이유야", "사실이에요",
    
    # Conjugations in 형태와 형사.md
    "여기선", "선장님", "낯선", "모양이야", "선택할",
    
    # Other misplaced/wrong
    "중입니다", "맥주", # 맥주 should be in 식사
}

def remove_unwanted_entries():
    """Remove conjugations and misplaced words"""
    total_removed = 0
    
    for root, dirs, files in os.walk("단어"):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                original_content = content
                
                # Remove unwanted entries
                for word in REMOVE_WORDS:
                    pattern = rf"## {re.escape(word)} #card\s*\?begin\s*### 뜻\s*-\s*### 예\s*-\s*\?end\n*"
                    content = re.sub(pattern, "", content)
                
                # Check if anything was removed
                if content != original_content:
                    # Count removals
                    removed = len(re.findall(r"## \S+ #card", original_content)) - len(re.findall(r"## \S+ #card", content))
                    if removed > 0:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"  {filepath}: Removed {removed} entries")
                        total_removed += removed
    
    return total_removed

print("Removing remaining conjugations and misplaced words...")
removed = remove_unwanted_entries()
print(f"\nTotal removed: {removed} entries")
