# AGENT.md - Korean Vocabulary Repository Standards

**Last Updated:** October 1, 2026  
**Purpose:** Guidelines for organizing and maintaining the Korean vocabulary repository with consistent quality and structure.

---

## 📚 Core Philosophy

This repository uses **semantic organization** to group Korean vocabulary by **meaningful categories**, not by grammar. All files use **Obsidian-compatible flashcard format** (`#card` markers) with spaced repetition support.

---

## 🎯 Essential Standards

### Vocabulary Card Format (REQUIRED for ALL vocab files)

Every vocabulary entry must follow this exact format:

```markdown
## [Korean Word/Phrase] #card
?begin
### 뜻
- [Primary English translation]
- [Alternative translation if applicable]

### 예
- [Korean sentence] - [English translation]
- [Korean sentence] - [English translation]

### Notes
[Optional: related terms, usage patterns, nuances]

<!--SR:!2027-01-15,100,250-->
?end
```

**Key Points:**
- Each entry is ONE `#card` block
- Korean and English on SEPARATE lines in `예` section
- Each file contains multiple cards
- `Notes` section is optional but recommended for clarification

### Example:

```markdown
## 간병인 #card
?begin
### 뜻
- caregiver
- medical assistant

### 예
- 아버지를 돌보기 위해 간병인을 고용했어요
  - We hired a caregiver to look after my father
- 간병인이 필요한 환자가 많아요
  - Many patients need caregivers

### Notes
- Related: 보호자 (guardian), 의료진 (medical staff)

?end
```

---

## 📁 Directory Structure

**Organization by Semantic Meaning:**
- Organize files by semantic meaning ("what things are or what you want to express")
- Use descriptive Korean folder names like `활동`, `감정`, `추상적인 것`, `표現 (慣用句)`
- Create files within folders for specific topics, e.g., `활동/요리.md`, `활동/동작.md`
- Use underscores for spaces in filenames: `신념_신뢰.md`
- Use hanja in parentheses for clarity: `표現 (慣用句).md`
- Keep structure flat (minimal nesting)
- **Create an Index.md in each folder** for easy navigation
- Place vocabulary files in semantically appropriate folders, not in root

---

## 🔄 How to Process Content

### When adding raw vocabulary or class notes:

1. **Parse and identify** semantic category for each word
2. **Convert to standard `#card` format** with 뜻, 예, and optional Notes
3. **Append to existing file** in the semantic folder, OR create new semantic file if needed
4. **Add to folder's Index.md** if new file created
5. **Delete original raw file** after content is distributed

### Example: Converting class notes

**RAW:**
```
아버지 건강 상태가 나빠지다
간병인
검색하다
```

**CONVERTED:**
- `간병인` → append to `사람/직업.md` as proper `#card`
- `검색하다` → append to `활동/컴퓨터.md` as proper `#card`
- `건강상태` → append to `건강/상태.md` as proper `#card`
- DELETE class_notes file

---

## 📝 Reference Files

### Root of `단어/`:
- `Index.md` - Master vocabulary index with all categories
- `Honorifics.md` - Honorific forms
- `시간.md` - Time-related vocabulary
- `기타_단어.md` - Miscellaneous terms that don't fit categories

### Each semantic folder should have:
- `Index.md` - Lists all files in that folder and provides context

---

## ✅ Quality Checklist

Before considering work complete:

- [ ] All numbered files converted and distributed (116-133, etc.)
- [ ] All class_notes files converted to standard card format
- [ ] All cards have `#card` marker
- [ ] All cards have `뜻` section  
- [ ] All cards have `예` section with Korean-English pairs
- [ ] All folders have `Index.md`
- [ ] Content organized by semantic meaning
- [ ] Hanja used in parentheses: `表現 (慣用句)` not `表現_慣用句`
- [ ] No empty folders
- [ ] No Untitled files

---

## 🎓 Examples

### Good: Semantic Distribution
```
116.md vocabulary list:
- 벌어지다 (widen/happen) → 활동/동작.md
- 소재 (material/subject matter) → 학/주제.md  
- 전망 (view/prospect) → 추상적인 것/관점.md
- 포기하다 (give up) → 상태/결정.md

[Delete 116.md after distribution]
```

### Good: Individual Semantic Files with Notes
```
✅ korean/단어/추상적인 것/특질.md
   Contains: Multiple 특질 cards with Notes explaining related terms
   
✅ korean/단어/추상적인 것/특성.md
   Contains: Multiple 특성 cards with Notes on nuances
```

### Good: Related Terms with Notes
```markdown
## 특질 #card
?begin
### 뜻
- characteristic trait
- inherent nature

### 예
- 좋은 특질을 가지고 있어요
  - He has good characteristics

### Notes
- 특질: inherent nature, fundamental characteristic
- 특성: unique trait, distinctive feature  
- 특징: notable feature, distinguishing mark
- 특기: special skill, forte

?end
```

---

## 🗂️ 사자성어 (四字熟語 - Chinese Idioms) Organization

Organize `사자성어.md` by **semantic meaning**, not alphabetically:

**Semantic Categories for Idioms:**
- Behavior/Character (행동과 성격): 작심삼일, 근묵자흑
- Relationships (인간관계): 관포지교, 수어지교
- Success/Achievement (성공과 성취): 금의환양, 금상첨화
- Misfortune/Hardship (불운과 고충): 고진감래, 과유불급
- Appearance/Quality (외모와 품질): 경국지색, 금지옥엽

Group similar idioms together within the file for easy discovery.

---

## 📞 Common Questions

**Q: Should I keep numbered files for reference?**  
A: Convert all content to standard format and distribute to semantic folders. Delete numbered files.

**Q: What if a word fits multiple categories?**  
A: Put it in the most specific semantic category. Use `Notes` to reference related concepts in other files.

**Q: Can I create subfolders within semantic categories?**  
A: Minimize nesting. Keep structure flat. Use file naming and cross-references in Notes instead.

**Q: Should I convert all class notes?**  
A: Yes. Parse class notes, convert each vocabulary item to proper `#card` format, distribute to appropriate folders, then delete the class_notes file.

---

## 🎯 Repository Goals

- Semantically organized for intuitive discovery
- Consistently formatted for spaced repetition reliability
- Duplicate-free and well-deduplicated
- Maintainable by following clear patterns
- Scalable for efficient content addition
- Well-indexed with Index.md in each folder

---

**These guidelines enable efficient, high-quality vocabulary organization that scales with the repository.**
