# 단어 Folder Structure Analysis

**Analysis Date:** 2026-10-01  
**Location:** `/home/robert/Documents/GitHub/korean/단어`

---

## 📊 OVERVIEW SUMMARY

| Metric | Count |
|--------|-------|
| **Total Files** | 242 |
| **Total Folders** | 28 |
| **Files in Root** | 26 |
| **Files in Subfolders** | 216 |
| **Empty Folders** | 3 |
| **Folders with 1-2 Files** | 10 |
| **Duplicate Topics** (root + folder) | 8 |

---

## 📁 ROOT FILES (26 files)

**Organizational/Index Files:**
- `Index.md` - Main index file
- `Honorifics.md` - Honorifics topic file

**Topic Files (should likely be in subfolders):**
- `교통.md` - **DUPLICATE** (also has 교통/ folder)
- `자연.md` - **DUPLICATE** (also has 자연/ folder)
- `연예.md` - **DUPLICATE** (also has 연예/ folder)
- `법.md` - **DUPLICATE** (also has 법/ folder)
- `사람.md` - **DUPLICATE** (also has 사람/ folder)
- `형태와 형사.md` - **DUPLICATE** (also has 형태와 형사/ folder)
- `전자 기술.md` - **DUPLICATE** (also has 전자 기술/ folder)
- `특질 & 특성 & 특징 & 특기.md` - **DUPLICATE** (also has 특질 & 특성 & 특징 & 특기/ folder)

**Miscellaneous Topic Files (no corresponding folders):**
- `움직이다.md`
- `말하기.md`
- `의성어.md`
- `의태어.md`
- `컴퓨터.md`
- `전자 기기.md`
- `나이.md`
- `발표.md`
- `방향.md`
- `시간.md`
- `전쟁.md`
- `정치.md`
- `양 & 질.md`
- `길.md`
- `책.md`
- `sort later.md` - **NEEDS ORGANIZATION**

---

## 📂 SUBFOLDER INVENTORY

### Large Folders (20+ files)

| Folder | Count | Key Files | Status |
|--------|-------|-----------|--------|
| **추상적인 것** | 40 | Abstract concepts, emotions, morality | ✅ Well-populated |
| **생활** | 27 | Daily life, hobbies, fashion, relationships | ✅ Well-populated |
| **장소** | 27 | Places, locations, buildings, rooms | ✅ Well-populated |
| **활동** | 25 | Actions, sports, activities, hobbies | ✅ Well-populated |

### Medium Folders (8-12 files)

| Folder | Count | Key Files | Status |
|--------|-------|-----------|--------|
| **상태** | 12 | Adjectives, states, descriptions | ✅ Good size |
| **세상** | 11 | Countries, world, animals, economy | ✅ Good size |
| **Helping words** | 15 | Grammar, particles, expressions | ✅ Good size |
| **직장** | 8 | Jobs, workplace, company | ✅ Adequate |
| **학** | 8 | School, education, science | ✅ Adequate |

### Small Folders (3-5 files)

| Folder | Count | Key Files | Status |
|--------|-------|-----------|--------|
| **한국 역사** | 3 | Korean war, colonialism, dynasty | ⚠️ Small |
| **건강** | 4 | Health, symptoms, medical | ⚠️ Small |
| **기계** | 4 | Machinery, sports equipment, rotation | ⚠️ Small |
| **사람** | 4 | Family, relationships, titles | ⚠️ Small + DUPLICATE |
| **자연** | 4 | Plants, weather, animals, liquids | ⚠️ Small + DUPLICATE |
| **몸** | 5 | Anatomy, teeth, cosmetics | ⚠️ Small |
| **한국** | 5 | Korean regions, history, culture | ⚠️ Small |
| **식사** | 3 | Food, taste | ⚠️ Very small |

### Minimal Folders (1-2 files)

| Folder | Count | Key Files | Status |
|--------|-------|-----------|--------|
| **교통** | 1 | 교통수단.md | ❌ DUPLICATE + Minimal |
| **색깔** | 1 | 색깔.md | ❌ Minimal |
| **연예** | 1 | 미디어.md | ❌ DUPLICATE + Minimal |
| **법** | 1 | 범죄.md | ❌ DUPLICATE + Minimal |
| **형태와 형사** | 1 | 더미.md | ❌ DUPLICATE + Minimal |
| **전자 기술** | 2 | 기술.md, 미디어와 통신.md | ⚠️ DUPLICATE + Small |
| **특질 & 특성 & 특징 & 특기** | 2 | 두드러짐.md, 기술.md | ⚠️ DUPLICATE + Small |

### **EMPTY FOLDERS** (3)

| Folder | Status | Action Needed |
|--------|--------|----------------|
| **계산자** | Empty | 🗑️ Should be deleted or content added |
| **형용사** | Empty | 🗑️ Should be deleted or content added |
| **동사** | Empty | 🗑️ Should be deleted or content added |

---

## 🚨 CRITICAL ISSUES IDENTIFIED

### 1. **DUPLICATE TOPICS** (8 items)
Files exist in BOTH root and as folders:
- `교통.md` + `/교통/` folder
- `자연.md` + `/자연/` folder
- `연예.md` + `/연예/` folder
- `법.md` + `/법/` folder
- `사람.md` + `/사람/` folder
- `형태와 형사.md` + `/형태와 형사/` folder
- `전자 기술.md` + `/전자 기술/` folder
- `특질 & 특성 & 특징 & 특기.md` + `/특질 & 특성 & 특징 & 특기/` folder

**Decision needed:** Are these index files or should they be consolidated?

### 2. **EMPTY FOLDERS** (3)
- `계산자/` - 0 files
- `형용사/` - 0 files (contains only subdirectory "색깔")
- `동사/` - 0 files (contains only subdirectory "동료")

### 3. **ORPHAN ROOT FILES** (16 files without folders)
These topic files have no corresponding folder:
- `움직이다.md`
- `말하기.md`
- `의성어.md` (also in Helping words/)
- `의태어.md`
- `컴퓨터.md` (also in 활동/)
- `전자 기기.md`
- `나이.md` (should be in 사람/ or 세상/)
- `발표.md` (should be in 활동/ or 직장/)
- `방향.md` (Helping words/ has "방향 동사.md")
- `시간.md` (also in 세상/ and Helping words/)
- `전쟁.md` (also in 활동/)
- `정치.md` (should be in 세상/)
- `양 & 질.md` (should be in 추상적인 것/)
- `길.md` (should be in 장소/)
- `책.md` (should be in 학/ or 생활/)
- `sort later.md` - **UNORGANIZED**

### 4. **EXTREMELY SMALL FOLDERS** (7 folders with ≤2 files)
These are candidates for merging:
- `교통/` (1 file)
- `색깔/` (1 file)
- `연예/` (1 file)
- `법/` (1 file)
- `형태와 형사/` (1 file, dummy content)
- `전자 기술/` (2 files)
- `특질 & 특성 & 특징 & 특기/` (2 files)

### 5. **POTENTIAL FOLDER MERGES** (candidates)
Based on content overlap and size:
- `기械/` + `기계/` - Different topics but small
- `건강/` + `몸/` - Related (health vs. body parts)
- `식사/` + `생활/` - Related but distinct
- `색깔/` + `상태/` or `형용사/` - Small, could move
- `연예/` + `생활/` or `세상/` - Small, could move
- `법/` + `세상/` - Related but distinct
- `교통/` + `장소/` or `세상/` - Could consolidate

### 6. **NAMING INCONSISTENCIES**
- Very long folder name: `특질 & 특성 & 특징 & 특기/` - Consider simplifying
- Mixed naming conventions: `형태와 형사/` vs others
- Folder "동사/" is empty but has a subdirectory "동료" (unrelated)
- Folder "형용사/" is empty but has subdirectory "색깔" (a specific type)

### 7. **SUBDIRECTORY ISSUES**
- `동사/동료/` - Seems misplaced
- `형용사/색깔/` - Should probably be `색깔/` at root level (which it is)
- `장소/학교/` - Should this be in `학/`?

---

## 📋 FILES BY FOLDER STATUS

### Files in Root That SHOULD Be Organized

**High Priority (Duplicates):**
```
8 files that have both root .md AND folder duplicates
→ Decide: keep root index file or move to folder?
```

**Medium Priority (Orphans):**
```
16 files without corresponding folders
→ Should be moved into existing appropriate folders
```

**Low Priority:**
```
2 organizational files (Index.md, Honorifics.md)
→ Keep in root
```

---

## 🎯 ORGANIZATION PLAN RECOMMENDATIONS

### Phase 1: Resolve Duplicates
- [ ] Decide for each of 8 duplicate items: keep root OR keep folder content?
- [ ] Option A: Keep root index files, remove or consolidate folder contents
- [ ] Option B: Keep folder structure, move root files into folders as index files

### Phase 2: Delete/Consolidate Empty Folders
- [ ] Delete `계산자/` (empty)
- [ ] Reorganize `형용사/` (empty main folder, has `색깔/` subfolder)
- [ ] Reorganize `동사/` (empty main folder, has `동료/` subfolder)

### Phase 3: Merge Small Folders
- [ ] `색깔/` → Consider merge to `상태/` or create as permanent small folder
- [ ] `연예/` → Could merge to `생활/` or `세상/`
- [ ] `법/` → Could expand or merge to `세상/`
- [ ] `교통/` → Could merge to `장소/` or `세상/`
- [ ] `전자 기술/` + `전자 기기/` → Consider merging

### Phase 4: Organize Orphan Root Files
Move these into appropriate folders:
- `움직이다.md` → `동사/` or `활동/`
- `말하기.md` → `Helping words/` or `활동/`
- `의성어.md` → `Helping words/`
- `의태어.md` → `Helping words/`
- `컴퓨터.md` → `활동/` (already has "컴퓨터.md")
- `전자 기기.md` → New folder or `전자 기술/`
- `나이.md` → `사람/`
- `발표.md` → `활동/` or `직장/`
- `방향.md` → `Helping words/`
- `시간.md` → `Helping words/` (consolidate with existing)
- `전쟁.md` → `활동/` (already has "전쟁.md")
- `정치.md` → `세상/`
- `양 & 질.md` → `추상적인 것/`
- `길.md` → `장소/`
- `책.md` → `학/` or `생활/`
- `sort later.md` → Review and organize

### Phase 5: Rename for Clarity
- `특질 & 특성 & 특징 & 특기/` → Consider shorter name: `특질/` or `특성/`

---

## 📈 DISTRIBUTION ANALYSIS

### Top 5 Largest Categories
1. **추상적인 것** - 40 files (Concepts, emotions, morality)
2. **생활** - 27 files (Lifestyle, daily activities)
3. **장소** - 27 files (Places and locations)
4. **활동** - 25 files (Actions and activities)
5. **상태** - 12 files (States and descriptions)

### Distribution by Size
- **Large (20+):** 4 folders
- **Medium (8-12):** 5 folders
- **Small (3-7):** 9 folders
- **Minimal (1-2):** 7 folders
- **Empty:** 3 folders

---

## 💡 KEY INSIGHTS

1. **Redundancy:** 8 items exist in both root and as folders (33% of root files)
2. **Orphans:** 16 root files (62% of non-index root files) lack corresponding folders
3. **Bloat:** 10 folders contain only 1-2 files (consider consolidation)
4. **Structure:** 4 folders contain 40% of all files (very unbalanced)
5. **Empty:** 3 folders exist but are completely empty
6. **Organization:** Clear categorization exists but needs cleanup and consolidation

---

## ✅ NEXT STEPS

1. **Review Root Files:** Identify which should be indexes vs. organizational files
2. **Create Consolidation Strategy:** Decide which small folders to merge
3. **Plan File Moves:** Map orphan files to their final homes
4. **Execute Cleanup:** Phase out empty and minimal folders
5. **Validate:** Ensure no broken links after reorganization

---

**Status:** 🟡 Analysis Complete - Awaiting Action Plan Decision
