# Remaining Reorganization Tasks

**Status:** AGENT.md complete and clarified  
**Next Steps:** Execute remaining fixes by semantic principle

---

## Overview

These tasks focus on applying the semantic organization principles from AGENT.md. Rather than being prescriptive about specific files, follow these general patterns:

**General Pattern:**
1. Identify content that doesn't follow repository standards
2. Extract vocabulary and organize by semantic meaning
3. Convert to standard `#card` format
4. Place in appropriate semantic folder
5. Delete the original file

---

## Task 1: Remove Non-Conforming Files

**What to look for:**
- Files named `Untitled*`
- Files with raw vocabulary lists
- Files that are just placeholders or staging

**What to do:**
- Delete Untitled files immediately
- For other files: extract any content, organize it semantically, then delete

**Status:** 10 files identified (Untitled.md, Untitled 1-7.md, and .base versions)

---

## Task 2: Organize Non-Semantic Folders

**What to look for:**
- Folders that combine multiple semantic concepts (e.g., with "&" separators)
- Folders that contain only copies of content from elsewhere
- Folders without clear semantic meaning

**What to do:**
1. Identify the semantic concepts within the folder
2. Create individual files for each concept
3. Move vocabulary to appropriate semantic locations
4. Delete the non-semantic folder

---

## Task 3: Consolidate Duplicate Content

**What to look for:**
- Content appearing in multiple locations
- Folders in root that duplicate content in 단어/
- Alphabetically organized content that should be semantic

**What to do:**
1. Identify all copies
2. Merge into single semantic location
3. Reorganize by semantic meaning (not alphabetically)
4. Delete duplicate locations

---

## Task 4: Convert Raw/Unconverted Files

**What to look for:**
- Files with raw vocabulary lists (no `#card` format)
- Class notes files
- Files without proper 뜻 and 예 sections
- Files with mixed content that should be distributed

**What to do:**
1. Extract vocabulary entries
2. Determine semantic category for each word
3. Convert to standard `#card` format
4. Append to appropriate semantic file
5. Delete the raw file

---

## Task 5: Add Index.md to All Folders

**What to look for:**
- Any semantic folder without an Index.md

**What to do:**
- Create Index.md in each folder
- List all files in that folder
- Provide brief context about what the folder contains

---

## Task 6: Clean Up Documentation

**What to look for:**
- Old report files (COMPLETION_REPORT.md, etc.)
- Process logs
- Temporary work-in-progress documents

**What to do:**
- Keep only: AGENT.md (standards) and Index.md files (navigation)
- Delete outdated/temporary documentation
- Update Index.md files as needed

---

## Priority Order

1. Remove Untitled files (quick win)
2. Add Index.md to all folders (quick win)
3. Consolidate duplicate content (medium effort)
4. Organize non-semantic folders (medium effort)
5. Convert raw/unconverted files (higher effort)
6. Clean up documentation (quick cleanup)

---

## Validation Checklist

After completing these tasks:

- [ ] No `Untitled*` files exist
- [ ] No files with raw vocabulary lists (all converted to `#card` format)
- [ ] All folders have Index.md
- [ ] All vocabulary organized by semantic meaning
- [ ] No duplicate content across locations
- [ ] All cards have `#card` marker
- [ ] All cards have 뜻 section
- [ ] All cards have 예 section with Korean-English pairs
- [ ] Only essential documentation remains (AGENT.md, Index.md)

---

## General Principles to Follow

- **Semantic organization** is the primary principle
- **Hanja is optional** - use only when helpful for clarity, not by default
- **Hangul first** - folder and file names should be descriptive Korean
- **Standard format** - all vocabulary follows `#card` format with 뜻 and 예
- **No duplicates** - each piece of vocabulary appears in one semantic location
- **Data preservation** - never delete content, only reorganize and move it
- **Clean structure** - minimal nesting, flat organization

---

**Reference:** See AGENT.md for standards and guidelines.
