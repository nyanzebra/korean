# Cleanup Audit: Content Items Referenced But Missing

**Date:** October 1, 2026  
**Purpose:** Identify vocabulary gaps found during Master Index rebuild

---

## Items Referenced in Old Master Index (But No Longer Listed)

During the cleanup and rebuild of the Master Index, the following items were referenced but do not have corresponding vocabulary files in the repository:

### ❌ Missing Content (Referenced but no files found)

1. **결혼 (Marriage/Wedding)** - Location: Previously referenced in `생활` folder
   - **Current Status:** Content EXISTS but in multiple places:
     - `korean/단어/사람/가족과 관계.md` - Has `결혼` and `결혼하다` cards
     - `korean/단어/생활/가족.md` - Has `장가` (for men) and `시집` (for women)
     - `korean/단어/장소/집과 가구.md` - Has `예식장` (wedding hall)
     - `korean/단어/세상/정부_행정.md` - Has `결혼 증명서` (marriage certificate)
   - **Recommendation:** These files are correctly placed. The reference in the old Master Index was to a non-existent dedicated file.

2. **장례 (Funeral/Mourning)** - Location: Previously in root Master Index
   - **Current Status:** File exists at `korean/단어/생활/장례.md`
   - **Recommendation:** Correctly placed in 생활 (Daily Life)

3. **대화 (Conversation)** - Location: Previously in 활동 section
   - **Current Status:** No dedicated file found
   - **Recommendation:** Consider creating `korean/단어/활동/대화.md` or adding to `소통.md`

---

## Recommendations for Content Addition

Based on the gap analysis, here are vocabulary topics that could be beneficial to add:

### Priority 1: High-Frequency, Essential Vocabulary

- [ ] **대화 (Conversation/Dialogue)** - Conversational verbs and phrases
  - Suggested location: `korean/단어/활동/대화.md`
  - Content to include: Speaking patterns, question forms, response phrases

- [ ] **결혼식 (Wedding Ceremony)** - Wedding-specific vocabulary
  - Suggested location: `korean/단어/생활/결혼식.md` or expand existing files
  - Content to include: Ceremony terms, wedding roles, traditions

### Priority 2: Intermediate Vocabulary

- [ ] **여행 (Travel/Journey)** - More comprehensive travel vocabulary
  - Currently exists: `korean/단어/생활/여행지.md` (destinations only)
  - Could expand to: Travel activities, transportation, accommodation

- [ ] **오락 (Entertainment/Recreation)** - Beyond current `연예` folder
  - Consider: Movies, games, hobbies organization

### Priority 3: Specialized Vocabulary

- [ ] **약속 (Appointment/Promise)** - Schedule and commitment vocabulary
  - Suggested location: `korean/단어/생활/` or `활동/`

- [ ] **감염병 (Disease/Epidemic)** - Specialized medical vocabulary
  - Suggested location: `korean/단어/건강/질병.md` (expand if exists)

---

## How to Add Missing Content

When you decide to add any of these:

1. **Create the new file** in the appropriate semantic folder
2. **Use standard `#card` format** (see AGENT.md):
   ```markdown
   ## [Korean Word] #card
   ?begin
   ### 뜻
   - [English translation]
   
   ### 예
   - [Korean sentence]
     - [English translation]
   
   ### Notes
   - Related terms: ...
   
   ?end
   ```

3. **Update the folder's Index.md** with a new line:
   ```markdown
   - [[new-file.md|Description]]
   ```

4. **Update parent Master Index** (`korean/단어/Index.md`) if creating a new semantic category

5. **Follow AGENT.md** for complete guidelines

---

## Verification Checklist

- [x] All referenced items in old Master Index verified
- [x] Existing content for "결혼" found and confirmed
- [x] Missing content identified
- [x] Recommended locations proposed
- [x] Priority levels assigned

---

## Notes

- The old Master Index had references to items that either:
  1. Existed but in different locations than expected
  2. Didn't exist at all (could be added)
  3. Were consolidated into other files (no longer needed separately)

- All currently existing files are properly organized by semantic meaning per AGENT.md standards

- The new Master Index (`korean/단어/Index.md`) is accurate and reflects actual repository contents

---

**Next Steps:** Consider which missing items to add based on your learning priorities. Recommend starting with **대화 (Conversation)** as it complements the existing 소통 folder and is high-frequency.

