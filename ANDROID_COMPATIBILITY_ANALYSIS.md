# Android Filename Compatibility Analysis Report

**Status:** Analysis Complete (No edits made)  
**Date:** October 1, 2026

---

## Overview

Android has strict filename restrictions on some file systems (particularly FAT32 and some implementations of ext4). Characters that cause issues include parentheses, ampersands, arrows, and dots in certain positions.

This report identifies all problematic files and suggests Android-compatible alternative names.

---

## Android Filename Restrictions

Android generally restricts these characters in filenames:
- `< > : " / \ | ? *` - Completely forbidden (FAT32 reserved)
- `( )` - Can cause issues on some devices/filesystems
- `&` - Can cause issues when syncing/accessing certain services
- `→` or other arrows - May cause encoding issues
- Leading/trailing spaces or dots - Problematic

**Status in this repo:**
- ✅ No `< > : " / \ | ? *` found
- ⚠️ **Parentheses `( )` - FOUND (96+ files)**
- ⚠️ **Ampersand `&` - FOUND (8+ files)**
- ⚠️ **Arrow `→` - FOUND (1 file)**
- ⚠️ **Middle dot `·` - FOUND (multiple files)**

---

## Critical Issues (Must Fix)

### 1. **Files with Parentheses `( )`** - 96+ files

These files are in the **문법/** folder structure. Parentheses can cause issues on Android when accessing through certain apps.

**Sample problematic files:**
- `./문법/00-기초 필수 문법 (TODO stubs)/아 어 보다 (시도).md`
- `./문법/00-기초 필수 문법 (TODO stubs)/(으)로 (방향·도구·자격 기본).md`
- `./문법/00-기초 필수 문법 (TODO stubs)/아서 & 어서 (기본 이유·순서).md`
- `./문법/03-연결어미 (조건·가정·양보)/할 경우를 대비해서 (할지도 모르니까).md`
- `./문법/04-연결어미 (대조·전환)/다고 해서 다 -> 것은 아니에요.md`
- And **~90 more files** with various parenthetical notes

**Recommended fixes:**
Replace `( )` with `[ ]` or remove parenthetical notes entirely. Examples:

| Current Filename | Recommended Alternative |
|---|---|
| `아 어 보다 (시도).md` | `아 어 보다 시도.md` or `아 어 보다 [시도].md` |
| `(으)로 (방향·도구·자격 기본).md` | `으로 방향·도구·자격 기본.md` or `으로 [방향·도구·자격 기본].md` |
| `할 경우를 대비해서 (할지도 모르니까).md` | `할 경우를 대비해서 할지도 모르니까.md` |
| `다고 해서 다 -> 것은 아니에요.md` | `다고 해서 다 것은 아니에요.md` (remove arrow) |

---

### 2. **Files with Ampersand `&`** - 8 files

The ampersand character can cause syncing issues on Android devices, particularly with cloud services.

**Problematic files:**

1. `./문법/01-조사 (Particles)/Every X & Some X.md`
2. `./문법/01-조사 (Particles)/만으로는.md` (no & in filename, but see context)
3. `./문법/00-기초 필수 문법 (TODO stubs)/아야 어야 하다·되다 (의무).md`
4. `./문법/00-기초 필수 문법 (TODO stubs)/아서 & 어서 (기본 이유·순서).md`
5. `./문법/00-기초 필수 문법 (TODO stubs)/조차 & 마저 & 까지도.md`
6. `./문법/00-기초 필수 문법 (TODO stubs)/부터 & 까지.md`
7. `./문법/00-기초 필수 문법 (TODO stubs)/안 & 못 & 지 않다 (부정).md`
8. `./문법/01-조사 (Particles)/만 vs 뿐.md` (uses "vs" instead)
9. `./문법/11-높임법·문체/주셔서 & 계셔서.md`
10. `./문법/05-종결어미 (추측·가능성)/을까 하다 & 을까 보다.md`
11. `./문법/05-종결어미 (추측·가능성)/은가 보다 & 나 보다.md`
12. Plus others...

**Recommended fixes:**
Replace `&` with alternatives like `and`, `vs`, or just comma-space. Examples:

| Current Filename | Recommended Alternative |
|---|---|
| `Every X & Some X.md` | `Every X and Some X.md` or `Every X vs Some X.md` |
| `아서 & 어서 (기본 이유·순서).md` | `아서 어서 기본 이유 순서.md` |
| `조차 & 마저 & 까지도.md` | `조차 마저 까지도.md` or `조차_마저_까지도.md` |
| `부터 & 까지.md` | `부터_까지.md` or `부터 까지.md` |
| `안 & 못 & 지 않다 (부정).md` | `안_못_지 않다 부정.md` |

---

### 3. **File with Arrow `→`** - 1 file

The arrow character can cause encoding issues on Android:

**Problematic file:**
- `./문법/04-연결어미 (대조·전환)/다고 해서 다 -> 것은 아니에요.md`

**Note:** This uses the ASCII string `->` which should be okay, but if it's the Unicode arrow `→`, it could cause issues.

**Recommended fix:**

| Current Filename | Recommended Alternative |
|---|---|
| `다고 해서 다 -> 것은 아니에요.md` | `다고 해서 다 것은 아니에요.md` (remove arrow) |
| or | `다고 해서 다 to 것은 아니에요.md` |

---

## Secondary Issues (Should Consider)

### 4. **Files with Middle Dot `·`** - Multiple files

The middle dot (`·`) is used in Korean grammar files. While not strictly forbidden on Android, it can cause issues on some devices and with certain file managers.

**Examples:**
- `./문법/00-기초 필수 문법 (TODO stubs)/(으)로 (방향·도구·자격 기본).md`
- `./문법/00-기초 필수 문법 (TODO stubs)/아야 어야 하다·되다 (의무).md`
- `./문법/01-조사 (Particles)/Every X & Some X.md`
- And many more in grammar files

**Recommended fix:**
Replace `·` with:
- Comma-space: `, `
- Forward slash: ` / `
- Underscore: `_`
- Hyphen: ` - `

Examples:

| Current | Recommended |
|---|---|
| `방향·도구·자격 기본` | `방향, 도구, 자격 기본` or `방향_도구_자격 기본` |
| `하다·되다` | `하다_되다` or `하다, 되다` |

---

## Low Priority Issues

### 5. **Files with Spaces After Numbers** - Many files

Files like `3A-105 1.md` and `3A-142-144 fixed 1.md` have inconsistent naming but work on Android. However, they should be standardized.

**Examples:**
- `./숙제/3A/textbook/3A-105 1.md` → Should be `3A-105-v1.md` or `3A-105_v1.md`
- `./숙제/3A/textbook/3A-142-144 fixed 1.md` → Should be `3A-142-144_fixed_v1.md`
- `./숙제/3B/workbook/2과 - fixed.md` → Should be `2과_fixed.md` (hyphen surrounded by spaces)
- `./숙제/3B/workbook/4과 - Fixed.md` → Should be `4과_fixed.md` (inconsistent capitalization)

---

## Complete List of Problematic Files

### By Category:

**문법/ Folder (Primary Issues - 96+ files):**

The entire `문법/` folder has a systematic issue with parentheses in both:
1. Folder names: `(TODO stubs)`, `(Particles)`, `(이유·원인·목적)`, etc.
2. Filenames: Most files in these folders have notes in parentheses

**Specific examples with multiple issues:**
- `아야 어야 하다·되다 (의무).md` - Has both `·` and `()`
- `아서 & 어서 (기본 이유·순서).md` - Has `&`, `·`, and `()`
- `(으)로 (방향·도구·자격 기본).md` - Has `(`, `)`, and `·`
- `아 어 지다 (상태 변화).md` - Has space before Korean and `()`

---

## Recommendation Priority

### **Priority 1 (Must Fix for Android - 8 files):**
Files with `&` character:
- All 8 files listed above with ampersands

### **Priority 2 (Should Fix - 1 file):**
Files with `→` arrow character:
- `다고 해서 다 -> 것은 아니에요.md`

### **Priority 3 (Strongly Recommended - 96+ files):**
All files with `( )` in filenames:
- All files in `문법/00-기초 필수 문법 (TODO stubs)/` with notes in parentheses
- All files in `문법/[numbered sections]/` with parenthetical notes

### **Priority 4 (Optional - 20+ files):**
Files with `·` middle dot and inconsistent spacing:
- Various files that could benefit from standardization

### **Priority 5 (Nice to Have - 50+ files):**
Files with version numbers like `1`, `fixed`, `Fixed`:
- `3A-105 1.md` → `3A-105_v1.md`
- `22-26 Fixed.md` → `22-26_fixed.md`

---

## Migration Strategy

### **Recommended Approach:**

1. **Phase 1 (Critical)**: Remove `&` from 8 files
   - Quick wins with maximum compatibility benefit
   
2. **Phase 2 (Important)**: Remove `→` from 1 file

3. **Phase 3 (Recommended)**: 
   - Remove parentheses or convert to brackets `[ ]` in 96+ grammar files
   - Replace middle dots `·` with commas or underscores

4. **Phase 4 (Optional)**:
   - Standardize version numbering (space to underscore)
   - Standardize "fixed" capitalization

### **Safe Character Set for Android:**

For maximum compatibility across all Android devices and file systems, use only:
- Korean Hangul: `가-힣`
- English letters: `a-z A-Z`
- Numerals: `0-9`
- Safe punctuation: `-` (hyphen), `_` (underscore), `.` (dot for extension)
- Safe spacing: Single spaces (not multiple)

**Avoid:**
- `( ) & · → / : ; ' " , [ ] { }`
- Multiple consecutive spaces
- Leading/trailing spaces

---

## Summary Table

| Issue | Count | Files | Priority | Fix Method |
|---|---|---|---|---|
| Parentheses `()` | ~96 | Grammar (문법/) | 3 | Remove or convert to `[ ]` |
| Ampersand `&` | 8 | Mixed locations | 1 | Replace with `and` or `-` |
| Arrow `→` | 1 | Grammar file | 2 | Remove arrow |
| Middle Dot `·` | Multiple | Throughout | 3 | Replace with `,` or `_` |
| Version spacing | ~50 | Homework (숙제/) | 4 | Convert space to `_` |
| **TOTAL ISSUES** | **155+** | | | |

---

## No Changes Made

As requested, **no edits have been made to any files**. This report identifies issues only and provides recommendations for review and approval before implementation.

---

## Next Steps

To proceed with Android compatibility fixes:

1. **Review** this report and confirm which priorities to address
2. **Approve** the recommended naming conventions
3. **Execute** the file renames (using `move_path` tool)
4. **Validate** that all links still work in Obsidian
5. **Test** on Android device to confirm compatibility

---

**Report prepared:** October 1, 2026  
**Analysis scope:** All `.md` files in `/korean` directory  
**Files analyzed:** 387 total `.md` files  
**Problematic files identified:** 155+ files with issues
