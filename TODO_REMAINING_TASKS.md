# Remaining Reorganization Tasks

**Status:** AGENT.md complete and clarified  
**Next Steps:** Execute these 6 remaining fixes

---

## 1. ✅ Remove Untitled Files (READY TO DO)
**Status:** 10 files to delete
- `korean/Untitled.md`, `korean/Untitled 1.md` through `korean/Untitled 7.md`
- `korean/Untitled.base`, `korean/Untitled 1.base`

---

## 2. 심화_회화 Folder (116-133 files)
**Status:** Needs complete reorganization
**What's there:** 9 numbered files with vocabulary lists from YouTube videos
- Files: 116.md, 117.md, 118.md, 125.md, 126.md, 127.md, 128.md, 131.md, 133.md
**What to do:**
- Parse each file and extract vocabulary
- Convert each entry to standard `#card` format
- Append to appropriate semantic folders (활동, 추상적인 것, 상태, etc.)
- Delete the 심화_회화 folder after content is distributed

**Example from 116.md:**
- 벌어지다 → `활동/동작.md`
- 소재 → `학/` or `추상적인 것/`
- 전망 → `추상적인 것/관점.md`

---

## 3. 사자성어 Consolidation
**Status:** Content split between two locations
**Current:**
- `korean/사자성어/ㄱ.md`, `korean/사자성어/ㄴ.md` (in root)
- `korean/단어/표現_慣用句/사자성어.md` (in 단어/)

**What to do:**
1. Move all content from `korean/사자성어/` to `korean/단어/表現_慣用句/사자성어.md`
2. Organize by semantic meaning (behavior, relationships, success, misfortune, appearance)
3. Delete the root `korean/사자성어/` folder

---

## 4. 특질 & 특성 & 특징 & 특기 Folder Reorganization
**Status:** Awkwardly structured folder with generic files
**Current:**
- Folder: `korean/단어/特質 & 特性 & 特徴 & 特技/`
- Files: index.md, 기술.md, 두드러짐.md

**What to do:**
1. Create individual semantic files:
   - `korean/단어/추상적인 것/특질.md`
   - `korean/단어/추상적인 것/특성.md`
   - `korean/단어/추상적인 것/특징.md`
   - `korean/단어/추상적인 것/특기.md`
2. Each file should have multiple vocabulary cards with related terms in Notes
3. Delete the folder

---

## 5. Class Notes Conversion
**Status:** Multiple class_notes files need parsing and distribution
**Examples:**
- `korean/단어/사람/class_notes_건강상태.md` (contains: 간병인, 검색하다, etc.)
- Other class_notes files in various folders

**What to do:**
1. For each class_notes file:
   - Extract vocabulary entries
   - Convert to standard `#card` format
   - Append to appropriate semantic files
2. Delete the class_notes file after content is moved

---

## 6. Delete Outdated Documentation
**Status:** Many old report files accumulate
**Files to delete:**
- FOLDER_ANALYSIS_REPORT.md
- COMPLETION_REPORT.md
- IMPLEMENTATION_COMPLETE.md
- REORGANIZATION_SUMMARY.md
- REORGANIZATION_CONVERSATIONAL_KOREAN.md
- CLASS_NOTES_INDEX.md
- CLASS_NOTES_ORGANIZATION_REPORT.md
- REORGANIZATION_SUMMARY_CLASS_NOTES.txt
- VOCAB_IMPORT_SUMMARY.md
- 단어_ORGANIZATION_ANALYSIS.md
- FINAL_REORGANIZATION_COMPLETE.md
- QUICK_START_GUIDE.md

**Files to keep:**
- AGENT.md (new standards guide)
- korean/단어/Index.md (master vocabulary index)

---

## Priority Order (Recommended)

1. **Remove Untitled files** (easiest, quick win)
2. **Consolidate 사자성어** (straightforward move)
3. **Fix 특질 & 특성 folder** (semantic reorganization)
4. **Convert class_notes** (data migration with format conversion)
5. **Process 116-133** (most complex, but high-value content)
6. **Delete old reports** (cleanup)

---

## Validation Checklist

After all tasks complete:

- [ ] No `Untitled*` files exist
- [ ] No numbered files (116-133, etc.) exist
- [ ] No unconverted `class_notes*` files exist
- [ ] All `#card` entries have 뜻 and 예
- [ ] All folders have Index.md
- [ ] 사자성어 organized by semantic meaning
- [ ] 특질, 특성, 특징, 특기 are individual files in 추상적인 것/
- [ ] All vocabulary in proper semantic folders
- [ ] Old reports deleted
- [ ] AGENT.md and 단어/Index.md are current

---

**These tasks will complete the repository reorganization according to AGENT.md standards.**
