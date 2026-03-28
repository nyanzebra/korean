#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# Words to skip - still too basic or conjugated
SKIP_WORDS = {
    "한번",
    "내게",
    "갖고",
    "여전히",
    "듣고",
    "두고",
    "이것",
    "알겠지",
    "요즘",
    "제게",
    "있니",
    "만난",
    "굉장히",
    "네게",
    "못한",
    "나갈",
    "만한",
    "짓이야",
    "잊지",
    "왔다",
    "같군요",
    "모든걸",
    "그렇습니다",
    "있겠어",
    "것보다",
    "찾았어요",
    "같다",
    "생긴",
    "반가워요",
    "내내",
    "이러지",
    "고맙네",
    "할까요",
    "않게",
    "않는다",
    "알았죠",
    "보낸",
    "하니까",
    "반드시",
    "아무리",
    "알아야",
    "그러다",
    "돌아올",
    "있는게",
    "좋습니다",
    "좋다",
    "찾아야",
    "못하게",
    "이래",
    "모르고",
    "없잖아요",
    "그동안",
    "거니",
    "빼고",
    "거긴",
    "그랬어요",
    "죽지",
    "몰랐어",
    "뭐라",
    "믿고",
    "좋네요",
    "모르겠다",
    "그렇고",
    "오직",
    "있었습니다",
    "그러게",
    "데려다",
    "보기",
    "돌아갈",
    "쓰지",
    "그러죠",
    "거니까",
    "가자고",
    "좋겠어요",
    "보고싶어",
    "되니까",
    "있었네",
    "하더라",
    "되겠지",
    "그리워",
    "어떻게든",
    "보니까",
    "못했어",
    "그래야지",
    "그리워",
    "그렇네",
    "그렇네요",
    "됐나",
    "잘됐어",
    "그랬구나",
    "알겠네",
    "없었지",
    "있겠지",
    "왔구나",
    "갔어요",
    "됐어요",
    "데릭",
    "루크",
    "제임스",
    "에밀리",
    "마리",
    "토니",
    "조이",
    "리즈",
    "벤",
    "잭슨",
    "그랬구나",
    "했겠지",
    "왔네",
    "갔다",
    "되겠어",
    "됐잖아",
    "아니었어요",
    "없겠지",
}

# Enhanced categorization with Korean meanings and examples
CATEGORIES = {
    "사람": {
        "keywords": [
            "아저씨",
            "자식",
            "녀석",
            "인간",
            "소녀",
            "소년",
            "아줌마",
            "청소년",
        ],
        "words": {
            "아저씨": (
                "middle-aged man, mister",
                "저 아저씨한테 물어봐요 - Ask that man over there",
            ),
            "자식": (
                "child, offspring",
                "부모는 자식을 사랑한다 - Parents love their children",
            ),
            "녀석": (
                "guy, fellow (casual)",
                "그 녀석은 정말 재미있어 - That guy is really funny",
            ),
            "인간": (
                "human being, person",
                "모든 인간은 평등하다 - All humans are equal",
            ),
        },
    },
    "상태": {
        "keywords": [
            "필요",
            "관심",
            "진정한",
            "예쁜",
            "착한",
            "어려운",
            "잘못된",
            "중요",
        ],
        "words": {
            "필요": ("need, necessity", "도움이 필요해요 - I need help"),
            "필요한": (
                "necessary, needed",
                "필요한 물건을 준비하세요 - Prepare the necessary items",
            ),
            "관심": ("interest, attention", "관심을 가지다 - to take interest in"),
            "진정한": ("true, genuine", "진정한 친구 - a true friend"),
            "예쁜": ("pretty, beautiful", "예쁜 꽃 - a pretty flower"),
            "착한": ("kind, good", "착한 아이 - a good child"),
            "어려운": ("difficult, hard", "어려운 문제 - a difficult problem"),
            "잘못된": ("wrong, mistaken", "잘못된 결정 - a wrong decision"),
            "위대한": ("great, magnificent", "위대한 업적 - a great achievement"),
        },
    },
    "활동": {
        "keywords": ["데이트", "산책", "운동", "경기", "모임"],
        "words": {
            "데이트": ("date, dating", "오늘 데이트 있어요 - I have a date today"),
        },
    },
    "시간": {
        "keywords": ["크리스마스", "한잔"],
        "words": {
            "크리스마스": (
                "Christmas",
                "크리스마스에 뭐 해요? - What do you do at Christmas?",
            ),
            "한잔": (
                "one drink, a drink",
                "커피 한잔 할래요? - Want to have a cup of coffee?",
            ),
        },
    },
    "추상적인 것": {
        "keywords": ["사건", "사고", "세상"],
        "words": {
            "사건": (
                "incident, event, case",
                "중요한 사건이 일어났다 - An important event occurred",
            ),
            "사고": (
                "accident, incident",
                "교통 사고가 났어요 - There was a traffic accident",
            ),
            "세상": ("world, society", "이 세상은 넓다 - This world is wide"),
        },
    },
    "직장": {
        "keywords": ["박사"],
        "words": {
            "박사": ("doctor, PhD", "김 박사님 - Dr. Kim"),
        },
    },
    "법": {
        "keywords": ["경찰"],
        "words": {
            "경찰": ("police", "경찰을 부르세요 - Call the police"),
        },
    },
    "특질 & 특성 & 특징 & 특기": {
        "keywords": ["바보", "열심히"],
        "words": {
            "바보": ("fool, idiot", "바보같이 행동하지 마 - Don't act like a fool"),
            "열심히": ("diligently, hard", "열심히 공부하다 - to study hard"),
        },
    },
}


def should_skip(word):
    """Check if word should be skipped"""
    if word in SKIP_WORDS:
        return True

    # Skip if too short
    if len(word) <= 1:
        return True

    # Skip obvious conjugations
    conjugation_patterns = [
        r".*지만$",
        r".*어서$",
        r".*아서$",
        r".*니까$",
        r".*는데$",
        r".*잖아$",
        r".*겠어$",
        r".*겠지$",
        r".*구나$",
        r".*네요$",
        r".*다고$",
        r".*라고$",
        r".*세요$",
        r".*ㅂ시다$",
        r".*어요$",
        r".*아요$",
        r".*습니다$",
    ]

    for pattern in conjugation_patterns:
        if re.match(pattern, word):
            return True

    return False


def categorize_word(word):
    """Categorize a word based on keywords"""
    for category, info in CATEGORIES.items():
        if word in info.get("words", {}):
            return category
        for keyword in info["keywords"]:
            if keyword in word:
                return category

    return None


def get_definition(word):
    """Get definition and example for a word"""
    for category, info in CATEGORIES.items():
        if word in info.get("words", {}):
            meaning, example = info["words"][word]
            return meaning, example

    # Default meanings for common words not in dictionary
    return None, None


def main():
    # Read unsorted words
    with open("unsorted_words.txt", "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]

    print(f"Processing {len(words)} words...")

    # Categorize words
    categorized = {}
    skipped = []

    for word in words:
        if should_skip(word):
            skipped.append(word)
            continue

        category = categorize_word(word)
        meaning, example = get_definition(word)

        if category and meaning:
            if category not in categorized:
                categorized[category] = []
            categorized[category].append((word, meaning, example))
        else:
            # Keep in unsorted for manual review
            if "unsorted" not in categorized:
                categorized["unsorted"] = []
            categorized["unsorted"].append((word, "", ""))

    print(f"\nSkipped {len(skipped)} words")
    print(f"Categorized into {len(categorized)} categories:")
    for cat, words_list in categorized.items():
        print(f"  {cat}: {len(words_list)} words")

    # Write to files
    for category, words_list in categorized.items():
        if category == "unsorted":
            continue

        output_file = f"categorized_{category}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            for word, meaning, example in words_list:
                f.write(f"## {word} #card\n")
                f.write("?begin\n")
                f.write("### 뜻\n")
                f.write(f"- {meaning}\n")
                f.write("### 예\n")
                f.write(f"- {example}\n")
                f.write("?end\n\n")

        print(f"Wrote {len(words_list)} words to {output_file}")

    # Write unsorted
    if "unsorted" in categorized:
        with open("still_unsorted.txt", "w", encoding="utf-8") as f:
            for word, _, _ in categorized["unsorted"]:
                f.write(f"{word}\n")
        print(
            f"\nWrote {len(categorized['unsorted'])} words to still_unsorted.txt for manual review"
        )


if __name__ == "__main__":
    main()
