# Vocabulary Reorganization Report - October 1, 2026

## 📋 Summary

Successfully consolidated scattered marriage, family, and conversation vocabulary into better-organized semantic locations. This reorganization improves discoverability and reduces fragmentation across the repository.

---

## ✅ Part 1: Marriage & Wedding Consolidation

### New File Created
**Location:** `korean/단어/생활/결혼.md`

**Consolidated From:**
- ✓ `korean/단어/사람/가족과 관계.md` - Extracted: 결혼, 결혼하다, 이혼
- ✓ `korean/단어/생활/가족.md` - Extracted: 장가, 시집
- ✓ `korean/단어/장소/집과 가구.md` - Extracted: 예식장
- ✓ `korean/단어/세상/정부_행정.md` - Extracted: 결혼 증명서
- ✓ `korean/단어/표현_관용구/일상표현.md` - Extracted: 축하합니다

### Cards in 결혼.md
1. **결혼** - noun, marriage
2. **결혼하다** - verb, to get married
3. **장가** - noun, marriage (for men)
4. **시집** - noun, marriage (for women)
5. **이혼** - noun, divorce
6. **예식장** - noun, wedding hall
7. **신랑** - noun, groom
8. **신부** - noun, bride
9. **결혼 증명서** - noun, marriage certificate
10. **축하합니다** - expression, congratulations

**Semantic Benefit:** All marriage-related vocabulary now centralized in the "생활" (Daily Life) category, making it semantically appropriate and easy to discover.

---

## ✅ Part 2: Conversation & Dialogue File Creation

### New File Created
**Location:** `korean/단어/활동/대화.md`

**Cards Included:**
All cards are conversation-focused verbs and expressions from various sources:
1. **대화하다** - to converse/have a conversation
2. **질문하다** - to ask/question
3. **부탁하다** - to request/ask favor
4. **약속하다** - to promise/make plans
5. **인사하다** - to greet/say hello
6. **말을 걸다** - to speak to someone/start conversation
7. **대답하다** - to answer/respond/reply
8. **맞장구치다** - to respond appropriately/chime in
9. **반응하다** - to react/respond/answer
10. **오해하다** - to misunderstand/misinterpret
11. **마중** - meeting someone/greeting
12. **추천하다** - to recommend/suggest

**Semantic Benefit:** Creates a dedicated "Conversation" file separate from broader "소통 (Communication)" file. This allows users to quickly find dialogue-specific verbs without wading through general communication concepts.

**Relationship:** 
- `소통.md` = Broader communication verbs (설명하다, 표현하다, 이야기하다, etc.)
- `대화.md` = Focused dialogue and conversation interactions

---

## 📊 Index Updates

### 1. korean/단어/생활/Index.md
**Updated:** Added new entry for 결혼.md

| File | Description |
|------|-------------|
| [[결혼.md\|결혼]] | Marriage, wedding, and divorce vocabulary |

**Last Updated:** October 1, 2026 - Added 결혼.md consolidating marriage vocabulary from scattered locations

---

### 2. korean/단어/활동/Index.md
**Updated:** Added new entry for 대화.md

| File | Description |
|------|-------------|
| [[대화.md\|대화]] | Conversation and dialogue |

**Last Updated:** October 1, 2026 - Added 대화.md file consolidating conversation vocabulary

---

## 🔗 Cross-References & Notes

### Marriage File Notes
The 결혼 증명서 card includes this note:
```
Related: 출생 증명서 (birth certificate), 증명 (proof), 행정 (administration)
```

### Conversation File Notes
Multiple cards include related term cross-references:
- **말을 걸다** references: 대화하다, 말하다, 인사하다
- **대답하다** references: 반응하다, 응하다, 맞장구치다
- **맞장구치다** references: 반응하다, 대답하다, 응하다
- **반응하다** references: 맞장구치다, 대답하다, 응하다

---

## ⚠️ Original File Status (For Review)

**Note:** Original cards remain in their original locations. The following files should be reviewed for cleanup:

1. **korean/단어/사람/가족과 관계.md**
   - Still contains: 결혼, 결혼하다, 이혼 (plus many family & relationship cards)
   - Action: Consider keeping as-is since it also contains other relationship vocabulary

2. **korean/단어/생활/가족.md**
   - Still contains: 장가, 시집 (plus other family cards)
   - Action: Consider keeping as-is since file title reflects immediate family

3. **korean/단어/장소/집과 가구.md**
   - Still contains: 예식장 (plus many house/furniture cards)
   - Action: Consider keeping as-is since it's primarily about housing

4. **korean/단어/세상/정부_행정.md**
   - Still contains: 결혼 증명서 (plus admin/government vocabulary)
   - Action: Consider keeping as-is since administrative documents are in proper category

5. **korean/단어/표현_관용구/일상표현.md**
   - Still contains: 축하합니다 (plus other daily expressions)
   - Action: Consider keeping as-is since expressions serve multiple contexts

---

## 🎯 Recommendation

**No deletion recommended** - Instead, the new consolidated files serve as:
- **Primary location** for finding all marriage vocabulary in one place
- **Cross-reference points** for users browsing original categories
- **Improved discovery** through semantic consolidation

If future cleanup is desired, add cross-reference comments in original files directing users to `결혼.md` for comprehensive marriage vocabulary.

---

## 📁 Directory Structure Improvements

### Before
```
Marriage vocabulary scattered across:
  └─ 사람/가족과 관계.md     (relationships)
  └─ 생활/가족.md           (family)
  └─ 장소/집과 가구.md      (house/furniture)
  └─ 세상/정부_행정.md      (government)
  └─ 표현_관용구/일상표현.md (daily expressions)
```

### After
```
Wedding semantically organized:
  └─ 생활/결혼.md          ← Single source of truth
     ├─ Concepts (결혼, 이혼, 장가, 시집)
     ├─ People (신랑, 신부)
     ├─ Places (예식장)
     ├─ Documents (결혼 증명서)
     └─ Expressions (축하합니다)

Conversation semantically focused:
  └─ 활동/대화.md          ← Conversation-specific verbs
     ├─ Dialogue (대화하다, 말을 걸다)
     ├─ Response (대답하다, 반응하다, 맞장구치다)
     ├─ Questioning (질문하다)
     ├─ Requesting (부탁하다)
     ├─ Promising (약속하다)
     ├─ Greeting (인사하다, 마중)
     └─ Misc (오해하다, 추천하다)
```

---

## 💾 Files Modified

✅ **Created:**
- `korean/단어/생활/결혼.md` (96 lines)
- `korean/단어/활동/대화.md` (144 lines)

✅ **Updated:**
- `korean/단어/생활/Index.md` - Added 결혼.md entry
- `korean/단어/활동/Index.md` - Added 대화.md entry

📋 **Referenced (Not Modified):**
- `korean/단어/사람/가족과 관계.md`
- `korean/단어/생활/가족.md`
- `korean/단어/장소/집과 가구.md`
- `korean/단어/세상/정부_행정.md`
- `korean/단어/표현_관용구/일상표현.md`
- `korean/단어/활동/소통.md`

---

## ✨ Benefits

1. **Improved Discoverability** - Marriage vocabulary consolidated in one semantic location
2. **Better Organization** - Conversation verbs now have dedicated file separate from broader communication
3. **Cross-Referenced** - Notes in cards point to related concepts in other files
4. **Semantic Clarity** - Clear separation between conversation (대화.md) and general communication (소통.md)
5. **Repository Standards** - Follows AGENT.md guidelines for semantic organization
6. **Backward Compatible** - Original files remain intact for legacy references

---

## 🔄 Future Considerations

1. **Family Vocabulary Review** - Consider whether `사람/가족과 관계.md` should remain focused on relationships vs. family
2. **Duplicate Management** - Monitor if original file locations get updated independently
3. **Cross-Reference Documentation** - Consider adding comments in original files directing to consolidated locations
4. **소통 vs 대화 Usage** - Ensure users understand the distinction between broader communication and focused dialogue

---

**Report Generated:** October 1, 2026  
**Repository Version:** Current  
**Status:** ✅ Complete & Ready for Use
