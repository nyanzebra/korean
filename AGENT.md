# AGENT.md - Korean Vocabulary Repository Standards & Practices

**Last Updated:** October 1, 2026  
**Purpose:** Guidelines for organizing and maintaining the Korean vocabulary repository with consistent quality and structure.

---

## 📚 Repository Philosophy

This repository uses **semantic organization** (not grammatical) to organize Korean vocabulary by meaningful categories. All files use **Obsidian-compatible flashcard format** with spaced repetition support.

---

## 🎯 Core Principles

### 1. **Semantic Categorization**
- Organize by **what things are or what you want to express**, not by grammar
- Each folder represents a semantic concept (e.g., "활동" for activities, "감정" for emotions)
- Files within folders are more specific (e.g., "요리" for cooking under "활동")

### 2. **One Word = One Card**
- Each vocabulary entry is a single `#card` block
- Each card has: `뜻` (meaning), `예` (examples), optionally `Notes`
- Format is strictly maintained for flashcard compatibility

### 3. **Vocabulary Pattern (Standard Format)**

```markdown
## [Vocabulary Word] #card
?begin
### 뜻
- [Primary English translation]
- [Alternative translation if applicable]

### 예
- [Korean sentence] - [English translation]
- [Korean sentence] - [English translation]

### Notes
- [Additional context, usage patterns, or related terms]

<!--SR:!2027-01-15,100,250-->
?end
```

### 4. **Class Notes Pattern**
When you have class notes or lists of raw vocabulary:
- **DO NOT** simply copy the raw content into a folder
- **DO** parse and convert to standard card format with proper meanings and examples
- **DO** extract words and place them in semantically appropriate files
- If no appropriate file exists, create one

Example of what NOT to do:
```markdown
아버지 건강 상태가 나빠지다
간병인
검색하다
```

Example of what TO do:
```markdown
## 간병인 #card
?begin
### 뜻
- caregiver, medical assistant
### 예
- 아버지를 돌보기 위해 간병인을 고용했어요
  - We hired a caregiver to look after my father
?end

## 검색하다 #card
?begin
### 뜻
- to search, to look up
### 예
- 인터넷에서 검색했어요
  - I searched online
?end
```

### 5. **Advanced Vocabulary (심화_회화) Pattern**
Files numbered 116-133 (or similar) should NOT exist as standalone files. Instead:
- Parse each numbered file
- Extract vocabulary entries
- Convert to standard card format
- Place in semantically appropriate folders

For example, from 116.md:
- `벌어지다` (widen/happen) → `활동/동사.md` or `활동/동작.md`
- `소재` (material/subject matter) → `학/` (education) or `추상적인 것/`
- `전망` (view/prospect) → `추상적인 것/관점.md`
- etc.

Then **delete** the numbered file (all content moved to proper locations).

---

## 📁 Directory Structure Guidelines

### Main Semantic Categories (Single-level, not nested):
```
단어/
├── 추상적인 것/        # Abstract concepts (~50 files)
├── 활동/              # Activities, verbs
├── 상태/              # States, conditions
├── 세상/              # The world, nature
├── 생활/              # Daily life
├── 사람/              # People, relationships
├── 장소/              # Places, locations
├── 표現_慣用句/        # Expressions, idioms
├── 직장/              # Workplace
├── 학/                # Education, academics
├── 시간.md            # Time (reference file)
├── 기타_단어.md       # Miscellaneous
└── [17 other semantic categories]
```

### What NOT to Do:
- ❌ Keep numbered files (116.md, 117.md, etc.) - convert and delete
- ❌ Create files like `심화_회화/` that just copy content - move content to proper places
- ❌ Keep class note files as-is without converting to standard format
- ❌ Create single large comparison files (combine only when semantically related)
- ❌ Use cryptic folder names like `특질 & 특성 & 특징 & 특기` - split into individual words with Notes

### What TO Do:
- ✅ Create focused semantic files within existing categories
- ✅ Merge related vocabulary into single semantic file
- ✅ Use Notes sections to add context and connect related terms
- ✅ Keep folder structure flat (not deeply nested)

---

## 📝 File Naming Conventions

### Semantic Category Files:
- Use **Korean names** (not romanized)
- Use **underscores** for spaces: `전쟁_관련.md`
- Use **descriptive names**: `동작.md`, `요리.md`, `스포츠.md`

### Reference Files (root of 단어/):
- `Index.md` - Master vocabulary index
- `Honorifics.md` - Honorific forms
- `시간.md` - Time-related vocabulary
- `기타_단어.md` - Miscellaneous terms

### Files to NEVER Create:
- ❌ `116.md`, `117.md`, etc. (numbered files - convert and delete)
- ❌ `심화_회화.md` or similar "track" files (distribute content)
- ❌ `Untitled.md`, `Untitled 1.md`, etc. (clean up immediately)

---

## 🔄 How to Process New Content

### When you have raw vocabulary or class notes:

**Step 1: Parse and Categorize**
- Extract each word/phrase
- Identify the semantic category it belongs to
- Check if it already exists in the repository

**Step 2: Convert to Standard Format**
```markdown
## [Word] #card
?begin
### 뜻
- [Translation]

### 예
- [Example] - [English]

### Notes
- [If multiple related terms, list them]
?end
```

**Step 3: Place in Appropriate File**
- If semantic file exists → append to it
- If semantic file doesn't exist → create it in the right semantic folder
- If multiple related words → group them in the same file

**Step 4: Update Index Files**
- Add to relevant `INDEX.md` in the semantic category
- Update `단어/Index.md` if new category created

**Step 5: Delete Original Source**
- Remove numbered files (116.md, etc.)
- Remove raw class note files after content is distributed
- Clean up temporary working files

---

## 🗂️ Handling Special Cases

### Case 1: Multiple Vocabulary with Same Theme
**File:** `특질 & 특성 & 특징 & 특기`

**Current Problem:** Creates a folder with 1-2 files that are just name placeholders

**Solution:**
- Create individual files for each word: `특질.md`, `특성.md`, `특징.md`, `특기.md`
- Each file can have multiple cards about that concept
- Add Notes section explaining differences:
  ```markdown
  ## 특질 #card
  ?begin
  ### 뜻
  - characteristic, trait, quality
  
  ### 예
  - 좋은 특질을 가지고 있어요
    - He has good qualities
  
  ### Notes
  - 특질: inherent nature, fundamental characteristic
  - 특성: unique trait, distinctive feature
  - 특징: notable feature, distinguishing mark
  - 특기: special skill, forte
  ?end
  ```

### Case 2: Idioms (속담, 격언, 사자성어)
- Keep as **separate files** (not merged)
- Each type is culturally and linguistically distinct
- Put all three in `표現_慣용구/` folder
- Maintain in their own dedicated files

### Case 3: Class Notes with Random Vocabulary
**File:** `class_notes_건강상태.md` containing:
```
아버지 건강 상태가 나빠지다
간병인
검색하다
```

**Current Problem:** Raw notes not converted to flashcard format

**Solution:**
1. Extract: `간병인`, `검색하다`, `건강상태`, `나빠지다`
2. Convert to card format
3. Place in appropriate files:
   - `간병인` → `사람/직업.md` (caregiver is a profession)
   - `검색하다` → `활동/컴퓨터.md` (common tech verb)
   - `건강상태` → `건강/상태.md` (health status)
   - `나빠지다` → `상태/악화.md` (getting worse)
4. Delete the class notes file after content is moved
5. Create proper entry for the concept if it doesn't exist

### Case 4: Consolidation (사자성어)
**Current:** Content in both:
- `korean/사자성어/ㄱ.md`, etc. (in root)
- `korean/단어/표現_慣用句/사자성어.md` (in 단어/)

**Solution:**
1. Consolidate all 사자성어 into `korean/단어/表現_慣用句/사자성어.md`
2. Include all entries in proper flashcard format
3. Delete the root `korean/사자성어/` folder

---

## 🎓 Examples of Good Organization

### Good: Semantic Distribution
```
116.md (raw content) →
  - 벌어지다 → 활동/동작.md (movement/happening verb)
  - 소재 → 학/주제.md (subject matter in education)
  - 전망 → 추상적인 것/관점.md (prospect/perspective)
  - 포기하다 → 상태/결정.md (giving up = decision/state)
  - 형성되다 → 활동/동작.md (to form/create)
```

### Bad: Keeping Numbered Files
```
❌ korean/단어/심화_회화/116.md
❌ korean/단어/심화_회화/117.md
... (just moving content, not organizing)
```

### Good: Individual Word Files with Notes
```
✅ korean/단어/특질.md
   - Contains cards about "특질" with related terms in Notes
   
✅ korean/단어/특성.md
   - Contains cards about "특성" with related terms in Notes
   
[Not: 특질 & 특성 & 특징 & 특기/ folder]
```

---

## ✅ Pre-Commit Checklist

Before considering work done, verify:

- [ ] All numbered files (116-133, etc.) are converted and **deleted**
- [ ] All class note files are converted to standard card format
- [ ] All raw vocabulary lists are parsed and distributed
- [ ] New semantic files created only when necessary
- [ ] All new files follow standard `#card` format
- [ ] Duplicate content is consolidated
- [ ] `Untitled.md` files removed
- [ ] Empty folders deleted
- [ ] Index files updated
- [ ] Documentation current and accurate

---

## 🔧 Maintenance Commands

### Find raw/unconverted files:
```bash
# Look for numbered files
ls korean/단어/심화_회화/*.md | grep "^[0-9]"

# Look for Untitled files
find korean -name "Untitled*"

# Look for class notes not yet integrated
find korean -name "class_notes*" -type f
```

### Verify card format:
```bash
# Check for cards without proper format
grep -L "^## " korean/단어/**/*.md | head
```

---

## 📞 Common Questions

**Q: Should I merge all similar vocabulary into one file?**  
A: No. Create focused semantic files. Example: Don't merge "감정" (emotions) with "상태" (states). They're different.

**Q: What if vocabulary fits multiple categories?**  
A: Put it in the most specific category. Use `Notes` to cross-reference related files.

**Q: Should I keep numbered files for reference?**  
A: No. All content must be converted to standard format and distributed. Delete numbered files.

**Q: How do I handle class notes with mixed topics?**  
A: Parse and distribute to appropriate semantic folders. One entry per card. Delete the note file.

**Q: Can I create subfolders within semantic categories?**  
A: Minimize nesting. Keep structure flat. Use file naming and cross-references instead.

---

## 📊 Repository Health Checklist

Run periodically to ensure quality:

```markdown
- [ ] No files named "Untitled*"
- [ ] No numbered files (116-133, etc.)
- [ ] No raw "class_notes*" files without conversion
- [ ] All cards have `#card` marker
- [ ] All cards have `뜻` section
- [ ] All cards have `예` section (at minimum)
- [ ] No folders with single or duplicate files
- [ ] Index files point to actual content
- [ ] No empty folders
- [ ] Documentation reflects actual structure
```

---

## 🎯 Goals

The repository should:
- ✅ Be **semantically organized** for easy discovery
- ✅ Use **consistent formatting** for reliable spaced repetition
- ✅ **Avoid duplication** and redundancy
- ✅ Be **maintainable** by following clear patterns
- ✅ **Scale efficiently** as new content is added
- ✅ Have **minimal decision-making** when adding new vocabulary

---

**By following these guidelines, future agents and humans can efficiently add, organize, and maintain Korean vocabulary without degrading quality.**
