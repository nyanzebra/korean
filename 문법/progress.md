# Reorganization Progress & Rationale

## What was done
The flat `문법/` folder (~155 files, alphabetical-ish by filename) was reorganized into 14
subfolders by **grammatical function**, plus a rewritten `Index.md` and a new `study-plan.md`.
No original content was deleted except true duplicates (see "Merges" below) and one empty
placeholder file (`.md`, zero bytes).

### Folder scheme
- `00-기초 필수 문법 (TODO stubs)` — beginner grammar that didn't exist in the vault at all
  (은/는 vs 이/가, 아서/어서, (으)면, 고 있다, negation, etc.). Each is a skeleton card tagged
  `#todo` — fill in Usage/Form/Restrictions/Examples as you study them.
- `01-조사` — particles, bound nouns, comparison markers (N+X patterns).
- `02-연결어미 (이유·원인·목적)` — connective endings for cause/reason/purpose.
- `03-연결어미 (조건·가정·양보)` — conditionals and concession connectives.
- `04-연결어미 (대조·전환)` — contrast/background connectives (는데 family, 에도 불구하고, etc.).
- `05-종결어미 (추측·가능성)` — sentence-final endings, speculation, possibility.
- `06-인용·간접화법` — reported/indirect speech.
- `07-시제·상` — tense and aspect (더니/던/다가, 채로, 게 됐어요, etc.).
- `08-사동·피동` — causative and passive voice overviews.
- `09-보조동사·보조용언` — auxiliary-verb constructions (주다, 버리다, 척하다, 만하다...).
- `10-명사화` — nominalization.
- `11-높임법·문체` — honorifics and speech level (반말/plain form).
- `12-숫자·단위` — counters and date counting.
- `13-어휘 뉘앙스 (비-문법)` — these aren't grammar points at all, just vocabulary
  nuance/comparison notes (e.g. 떨어지다 vs 넘어지다, 신청 vs 등록 vs 접수). Kept here rather than
  moved to `단어/` since the user asked specifically about the `문법` folder; consider moving
  these to `단어/` in a future pass.

Every file move preserved 100% of original content — this was a pure `mv`, not a rewrite.

## Merges (content consolidated, no information lost)
A few files were genuine duplicates or near-duplicates of the same grammar point. These were
merged into one file (all examples/notes from both kept) and the redundant file deleted:

| Kept file | Merged from (deleted) | Why |
|---|---|---|
| `05-.../네요 & 군요(구나, 구먼).md` | `Surprise.md`, `구.md` | Both were the same 네요/군요/구나 "expressing surprise/realization" topic; `구.md` additionally covered 구먼/구만. |
| `01-.../로서 & 로써 & 로 인하여.md` | `로서.md` (contentless stub), `로 인하다.md` | Same 로 인하다 grammar point; unique examples from `로 인하다.md` appended. |
| `07-.../다(가) 보니(까)...md` | `아 보니까.md` | `아 보니까.md`'s example didn't exist in the comprehensive comparison file; appended it. |
| `09-.../척하다.md` | `착하다.md` | `착하다.md` was a mistitled duplicate of the 척하다 "pretend" pattern (title typo — 착하다 actually means "kind", unrelated) with a different example set; examples merged, note about 체하다 alternate spelling kept. |
| `07-.../채(로).md` | `는 채로, 며, 면서, 을때.md` | The second file was a comparison note about 채로 vs 며/면서/을 때; merged as an appendix to the 채로 card. |

## Deliberately NOT merged (kept separate, just colocated)
These looked similar by name but are either genuinely distinct grammar or the merge risk/benefit
wasn't worth it in this pass. All now sit in the same folder so they're easy to compare, and
Index.md/study-plan.md call out the ones worth double-checking:

- **텐데 cluster** (`텐데.md`, `을 텐데.md`, `을 텐데 걱정이다.md`, `텐데 vs 을까 봐.md`) — all in
  `05-종결어미`. These have overlapping usage explanations of varying quality/depth. A future pass
  could consolidate into a single authoritative `텐데.md` card with subsections, but each currently
  has slightly different example sentences worth preserving verbatim, so I left them split.
- **는데.md vs 는 데.md** — genuinely different grammar (는데 = connective; 는 데 = bound noun
  "the situation/place of ~"). Correctly kept separate, in different folders (04 vs 01).
- **만 하다.md vs 만하다.md** — genuinely different (만 하다 = "as big/much as N"; 만하다 = "worth
  doing"). Kept separate, in different folders (01 vs 09) since their grammatical role differs.
- **V하다 주다.md vs 어 주다.md** — distinct patterns (아다 주다 = do-and-bring vs 아 주다 = do-for),
  already cross-referenced in the file text. Kept separate, colocated in `09`.
- **에 따라 있다.md vs 에 따라서.md** — distinct (spatial arrangement vs "depending on/according
  to"). Kept separate, both in `01`.

## Known remaining rough edges / suggestions for a future pass
1. The 텐데 cluster (see above) could still be merged into one card with subsections.
2. `13-어휘 뉘앙스 (비-문법)` arguably belongs under `단어/` rather than `문법/` since these are
   vocabulary-nuance comparisons, not grammar points — left in place per original scope of this
   task (문법 folder only).
3. Stub files in `00-기초 필수 문법 (TODO stubs)/` are skeletons only — no Usage/Form/Examples
   filled in. They exist so the study plan has a complete beginner→advanced path; content should
   be added lesson-by-lesson.
4. Some `#card` headers had typos in the original vault (e.g. 채(로).md's header literally said
   "## 문법" instead of the grammar point) — fixed as encountered during merges, but did not do a
   full audit of every remaining file's header for similar typos.
5. If using Obsidian's spaced-repetition plugin (`<!--SR:...-->` comments seen in several files),
   double check merged files still parse correctly with your plugin — the SR metadata was kept
   as-is on whichever file "won" the merge.

## File count sanity check
- Before: ~155 files (flat) + 1 empty file + `Index.md`.
- After: 155 real grammar/vocab files distributed across 14 subfolders + `Index.md` +
  `study-plan.md` + `progress.md` (this file) + 22 new stub files in `00-...` = **~178 files total**,
  0 content lost, 6 files deleted as pure duplicates/empty.
