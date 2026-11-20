# Task: Continue the repository documentation audit

## Metadata

- **ID:** 20261120-123000
- **Created:** 2026-11-20 12:30 UTC
- **Updated:** 2026-11-20 13:03 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** None
- **Archived:** No

## 1. Original Request

> Right now we still have the audit. But we don't have a task for it currently. Create a task for it, then move entire audit log (from version 5 onwards) from initialization policy to it.

## 2. Subsequent Instructions

No subsequent clarifications recorded.

## 3. Objective

Continue and complete the repository documentation audit. Keep its complete historical audit log in this task record instead of the initialization policy.

## 4. Requirements

- Preserve the complete audit history from Version 5 onward in this task record.
- Keep `skills/INITIALIZATION_POLICY.md` focused on current initialization policy and its own change history through Version 4.
- Preserve the future revision template, initialization review checklist, and maintenance rule in the initialization policy.
- Track unresolved audit work and update this task record as work progresses.
- Do not raise lint baselines to make findings disappear.
- Do not alter historical archive records unless the user authorizes those changes.
- Verify every repository write by fetching the committed path from branch `gpt`.

## 5. Decisions

- The audit is an active P1 task because its prior records explicitly leave work open.
- Versions 5–32 are moved verbatim into this task's Audit History section.
- Branch `gpt` remains the sole working branch. Do not modify `main` without explicit authorization.

## 6. Progress Log

### 2026-11-20 12:30 UTC

- **Action:** Inspected the task board, task template, initialization policy, and workspace task directory on branch `gpt`.
- **Result:** No active task tracks the repository documentation audit. The initialization policy contains audit history beginning at Version 5 and continuing through Version 32 in two separate ranges.
- **References:** `workspace/task_board.md`, `workspace/TASK_TEMPLATE.md`, `skills/INITIALIZATION_POLICY.md`.
- **Next:** Create this task, move Versions 5–32 into it, and update the task board.

### 2026-11-20 12:46 UTC

- **Action:** Paused the repository documentation audit to execute the user's explicitly approved P1 Condensed Mode workflow task.
- **Result:** This audit remains In Progress and is no longer the current execution task. Its remaining work and next actions are unchanged.
- **References:** `workspace/tasks/20261120-123400-condensed-mode-task-gates-and-reporting.md`, `workspace/task_board.md`.
- **Next:** Resume this audit after the Condensed Mode task reaches an outcome.

### 2026-11-20 12:49 UTC

- **Action:** Resumed the repository documentation audit after the approved Condensed Mode workflow task reached Done.
- **Result:** This audit is again the current execution task. Its recorded remaining work and next actions remain unchanged.
- **References:** `workspace/task_board.md`, `archive/tasks/20261120-123400-condensed-mode-task-gates-and-reporting.md`, `workspace/discussion.md`.
- **Next:** Continue from the existing audit Next Actions.

### 2026-11-20 12:57 UTC

- **Action:** Rebuilt the Markdown inventory at the Version 17/19 audit commit and at the current branch head. Compared the historical source-file exclusion rules.
- **Result:** Reconciled the 121-versus-119 discrepancy. The 121-file count did not exclude the two files under `skills/asd-ste100/examples/`. Version 19 excluded those two files and correctly reported 119. At the same historical commit, the repository contained 166 Markdown files. The current branch contains 176 Markdown files and 129 files under the same Version 19 source-file exclusions.
- **Current workflow scope:** The full-document lint workflow uses a different exclusion set. Its current tree contains 47 in-scope Markdown files. Do not compare this count directly with the 119/129 active-link source count.
- **Linter configuration:** Compared all 19 historical baseline entries with the current branch tree. Two entries referred to deleted `skills/novelist-initiation/` files. Removed those stale entries. All 17 remaining baseline paths exist in the current tree. No baseline value changed.
- **Changed path:** `skills/asd-ste100/scripts/ste-lint-repository.sh`.
- **Commit:** `94cedba3c786ff78ec57385f8a18d0b1f5475bfd`.
- **Read-back:** Fetched the updated wrapper from branch `gpt`. Confirmed that all 17 baseline paths exist in the current tree and that both stale paths are absent.
- **Validation limit:** Did not run the linter or its self-test. The connected repository tools do not provide a repository shell. No CI run was manually triggered or inspected.
- **Next:** Reduce current lint findings and obtain a fresh full-document lint result in an authorized repository execution environment.

### 2026-11-20 13:00 UTC

- **Action:** Scanned all 47 Markdown files in the current full-document workflow scope for semicolons and selected structural lint patterns.
- **Result:** The preliminary scan found 20 semicolon occurrences in six editable files. Removed all 20. The six files are `skills/github-actions/SKILL.md`, `skills/SESSION_START.md`, `skills/drawing/SKILL.md`, `skills/session-archiving/references/archive-records-and-image-prompts.md`, `workspace/task_board.md`, and this task record. Two semicolons in this task record's copied audit history were later restored to preserve the source text.
- **Preserved exceptions:** Did not edit archived task records. The ASD-STE100 writing-rules reference contains a quoted semicolon example and its wrapper disables the semicolon rule for that file. The ASD-STE100 skill contains intentional rule examples and retains its recorded baseline.
- **Commits:** GitHub Actions skill `9a12123fadc3776ebe0ef16750168f2437389b04`, Session Start `b01570973ee52391bafa9a02bceab6cf09b67db6`, Drawing skill `a6e665e99f0dff10b8a43c2cf32d89e91a2a5184`, archive reference `6b99a7fa7d5af1b8ec93d4870f925b2d498552c4`, task board `a71692b6118068667d18f37aa06fd8de662613f2`, audit task `f7c17ef3838af9cff0fa5ffdba862a939ba47b07`.
- **Read-back:** Fetched all six paths from branch `gpt`. Confirmed that five contain no semicolons. Restored the two historical semicolons in this task record.
- **Validation limit:** This was a targeted text scan, not an execution of the official linter. The repository execution environment remains unavailable. No CI run was manually triggered or inspected.
- **Next:** Review remaining supported lint patterns and obtain a fresh full lint result in an authorized repository execution environment.

### 2026-11-20 13:02 UTC

- **Action:** Reviewed the nominalization candidate in `archive/README.md`.
- **Result:** Replaced "performs the deletion" with direct actions. The workflow now states that it deletes the contents of `archive/tasks/`.
- **Commit:** `dac406fcad86586f4108fcdc149dc25f96e14115`.
- **Read-back:** Fetched `archive/README.md` from branch `gpt`. Confirmed the direct wording and the absence of the matched nominalization pattern.
- **Next:** Continue the supported-rule review. Obtain a fresh official lint result in an authorized repository execution environment.

### 2026-11-20 13:03 UTC

- **Action:** Compared the current linter wrapper with its Version 19 version at commit `837f415b040c8d0cbcc16eff77cedc732433acce`.
- **Result:** The historical wrapper had 21 baseline entries totaling 179. The current wrapper has 17 entries totaling 170. Two entries totaling four were removed earlier after their findings were cleared. Two entries totaling five referred to deleted novelist-initiation files and were removed in commit `94cedba3c786ff78ec57385f8a18d0b1f5475bfd`.
- **Verification:** Checked the current wrapper against the current branch tree. All 17 remaining baseline paths exist. The aggregate baseline is a configured threshold, not a current lint result.
- **Next:** Continue the review of supported lint findings. Do not report the current lint count until the official linter runs.

### 2026-11-20 13:03 UTC

- **Action:** Reviewed lint and active-link validation scope for archived task records.
- **Finding:** The full lint workflow and changed-file workflow included `archive/tasks/`. The active-link checker also scanned archived records as source files. These records are historical snapshots. The audit task prohibits edits to them without user authorization.
- **Decision:** Exclude `archive/tasks/` from full and incremental lint source sets and from active link-source scans. Keep archived Markdown files in the link-target inventory. Keep `archive/README.md` in the active documentation scope.
- **Changed paths:** `.github/workflows/ste-lint-full-docs.yml`, `.github/workflows/ste-lint-changed.yml`, `skills/asd-ste100/scripts/check_markdown_anchors.py`, and `skills/asd-ste100/references/repository-writing-policy.md`.
- **Commits:** Full workflow `6a8fb7886a5c47cb9f0b3fb484d5025c517b02d8`, changed workflow `a87d2c1e8b81f7844500ee5e638c19b7310c687e`, link checker `ea32a73d0e01ac48ecc8b39d3984c85d283acf15`, writing policy `f9ca178b721df1d086ac7e741405c5e8dec23788`.
- **Read-back:** Fetched all four paths from branch `gpt`. Confirmed that both lint modes and the active-link checker exclude archived task records as sources. Confirmed that the policy keeps those files available as link targets.
- **Next:** Continue reviewing current in-scope technical documentation and validation coverage. Do not edit archived task records.

### 2026-11-20 13:04 UTC

- **Action:** Compared the copied audit history with the source policy at the parent of the move commit.
- **Result:** Confirmed an exact text match for all 28 entries from Version 5 through Version 32. The source stored Versions 5–9 and Versions 10–32 in separate locations. The task record joins both ranges without changing their text.
- **Lint exception:** The wrapper disables only the semicolon rule for this task record. This preserves the two semicolons in the verbatim historical entries. All other supported rules remain active.
- **Read-back:** Fetched the task record and wrapper from branch `gpt`. Confirmed the exact historical match and the path-specific rule exception.
- **Next:** Continue the audit without changing the copied historical entries.

## 7. Current State

The historical Version 19 inventory contained 166 Markdown files and 119 active source files. The Version 17 count of 121 used the same exclusions except for `skills/asd-ste100/examples/`. That directory contained two Markdown files, which explains the exact difference.

The current branch contains 176 Markdown files. The same Version 19 source-file exclusions produce 129 active source files. The full-document lint workflow uses a different exclusion set and currently selects 47 Markdown files. These counts describe different scopes.

The Version 19 full lint reported 179 hard findings and 300 advisory findings. Those are historical results, not a fresh result for the current branch. The linter wrapper now has 17 baseline entries totaling 170. Every entry maps to an existing file. The historical 179-point threshold fell by four when two active-file baselines cleared. It fell by five when two deleted-file baselines were removed. The 170-point total is a configured threshold, not a current lint result.

The active-link scan at Version 19 found zero unresolved local Markdown targets or heading anchors in its 119-file source scope. Current validation now excludes `archive/tasks/` as a source while retaining archived files as link targets. The historical-link review and external URL review remain open. No fresh full lint has run.

## 8. Remaining Work

- Reduce the recorded 179 hard lint findings without raising per-file baselines.
- Re-run the official linter and its self-test in a repository execution environment.
- Review historical archive links only after the user authorizes changes to those records.
- Review external URL availability if it remains within the approved audit scope.
- Confirm current audit scope and completion criteria against the repository state before closing the task.

## 9. Next Actions

1. Review remaining supported lint rules in the current full-document scope. Focus on long sentences, synonym rotation, and dangling conjunctions.
2. Inspect any candidate finding in its full document context before editing.
3. Keep historical audit entries and archived task records unchanged.
4. Run the official linter self-test and full-document lint in an authorized repository execution environment.
5. Review external URL availability if it remains within the approved audit scope.

## 10. References

- `skills/INITIALIZATION_POLICY.md` — current initialization policy. It retains Versions 1–4 and the policy review material.
- `skills/asd-ste100/scripts/ste-lint.py` — official linter.
- `skills/asd-ste100/scripts/ste-lint-repository.sh` — repository lint modes and per-file baselines.
- `.github/workflows/ste-lint-full-docs.yml` — full-document lint workflow.
- `.github/workflows/ste-lint-changed.yml` — changed-document lint workflow.
- `workspace/task_board.md` — task index.

## 11. Verification

- **Check:** Identify and preserve all audit history from Version 5 onward.
- **Method:** Compare the copied history with the source policy at parent commit `5358dace526dc38808dac3a8d2ad4eaea1214af2`.
- **Result:** Passed. Confirmed an exact text match for all 28 entries from Version 5 through Version 32.
- **Check:** Reconcile the Version 17 and Version 19 active-source counts.
- **Method:** Rebuild both counts from the Version 19 commit tree and compare the exclusion sets.
- **Result:** Passed. The two excluded ASD-STE100 example files explain the 121-versus-119 difference.
- **Check:** Verify current lint baseline paths.
- **Method:** Compare every configured baseline path with the current branch tree.
- **Result:** Passed. All 17 current baseline paths exist. Their configured total is 170.
- **Limitations:** The official linter and self-test have not run on the current branch. Historical lint and CI results do not establish the current repository's lint status.

## 12. Handoff Instructions

Continue from the Next Actions. Keep this task In Progress until the remaining audit work is resolved or explicitly descoped by the user. Do not modify historical archive records without approval. Record new audit findings here, not in `skills/INITIALIZATION_POLICY.md`.

## Audit History — Versions 5–32

### Version 5 — First repository documentation audit pass

- **Date:** 2026-11-20
- **Change:** Rewrite five technical documents under the repository ASD-STE100 policy.
- **Files modified:**
  - `skills/session-archiving/references/image-processing-scripts.md`
  - `skills/session-archiving/references/drawing-session-closeout.md`
  - `novels/README.md`
  - `novels/WORKFLOW.md`
  - `images/takeout/README.md`
- **Verification:** Retrieved each changed path from branch `gpt` after the write. The read-back matched the committed content and required sections.
- **Validation limit:** The ASD-STE100 linter and the full repository audit have not run. The audit remains in progress.
- **Commits:** `683d0367f0fd171403990189dca0e2169b8f491e`, `8dd008db79fe086728d97cf85802e40ebc1b8fc1`, `44a624833db2e82f86da0dd34c140ee5eb5cffbf`, `8832f92875c057c1d4903f6ed800eb9481830e11`, and `48fd5805622c66f1a27786ee1640a1929cc5e479`.

### Version 6 — Second repository documentation audit pass

- **Date:** 2026-11-20
- **Change:** Revise additional skill instructions, references, image documentation, and current novel templates.
- **Files modified:**
  - `skills/SESSION_START.md`
  - `skills/novelist-initiation/INITIATION.md`
  - `skills/drawing/SKILL.md` (reviewed, not rewritten)
  - `skills/drawing/references/image-editing-protocol.md`
  - `skills/drawing/references/archive-and-delivery.md`
  - `skills/drawing/references/generation-recovery-and-provenance.md`
  - `skills/drawing/references/series-continuity-and-iteration.md`
  - `skills/conversation-mode/SKILL.md`
  - `skills/agent-skill-authoring/SKILL.md`
  - `skills/session-archiving/SKILL.md`
  - `skills/session-archiving/references/image-provenance-and-webp.md`
  - `skills/session-archiving/references/archive-records-and-image-prompts.md`
  - `skills/romantic-storyteller-visual-artist/references/novel-production-workflow.md`
  - `skills/philosophy-religion-asceticism/README.md`
  - `skills/philosophy-religion-asceticism/SKILL.md`
  - `skills/philosophy-religion-asceticism/references/research-method.md`
  - `skills/philosophy-religion-asceticism/references/source-standards.md`
  - `skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md`
  - `images/README.md`
  - `novels/templates/scene-v1.1.md`
  - `novels/templates/illustration-prompt-v1.1.md`
  - `novels/README.md`
- **Verification:** Fetched changed paths from branch `gpt` after each write. Read-back checked the committed content.
- **Validation limit:** The repository linter has not run. This environment has no repository shell or GitHub Action dispatch tool. Manual screening does not replace the linter.
- **Manual screening:** Scans checked semicolons, selected phrasal verbs, marketing adjectives, selected nominalizations, and instruction sentence length in revised files. The scans found two semicolons, one missing sentence boundary, one nominalized verb phrase, and several long instructions. Those findings were corrected and read back.
- **Latest reference scan:** A targeted scan of four Drawing, archive, and curriculum references found no semicolons, selected phrasal verbs, marketing adjectives, or tested nominalization patterns. The scans do not test every STE rule.
- **Path-policy conflict:** The Session Archiving skill lists five approved roots: `images/`, `master/`, `novels/`, `drawings/`, and `skills/`. The same skill and its references also direct non-novel drawing assets to `drawings/YYYY-MM-DD/images/`. That path is outside the listed roots. I did not change the boundary or access the `drawings/` path. Resolve this conflict before further work in that path.
- **Master inventory:** The initial fetch of `master/README.md` returned 404. A later read-only directory listing found `master/Images.md`, `master/Poses.md`, and `master/Prompts.md`. The directory has no README. Review classified these files as prompt, pose, and creative source material. They remain unchanged.
- **Remaining work:** Continue auditing any unreviewed technical documents. Run the official linter in a repository execution environment and review its findings. Resolve the `drawings/` workspace conflict before following historical archive links. The `drawings/` directory listing returned 404, so its contents remain unverified.
- **Commits:** `1cc5e5d623e8200316d009dc2219a74287c591fc`, `f898c0bd2fc68a123df16f1b0b6ce44d13ba7e9d`, `82df4add11b03428ac1a49ba948e24ccf9e78e35`, `5bf95f28bc4cbbd645ae86fc4407fbdc32826b01`, `29a58b17304c56e986e39af15d2867b955e17665`, `2333a0378f0f6aebad5bdd7b31801d57ee04dfb0`, `5f1a78b68e655e10160d852fd81be65d937f4111`, `f47d07242b7605dded9d17b2ba82425e34e48cd2`, `3f223f69f1aaff0da7643f81ea58ce950746085d`, `11752c6e9eeaabe66580ae3d69de46e3ef6f649a`, `29103811aba608d25914d699473685f6b06cebc3`, `f56f8385c2f96ca0f8a29e64f925071511aa8363`, `91e427e1f4a63246a78b1c0eab596d2abb649284`, `01fde065c45c98b4ee7b4cce399417cfc2595e85`, `50a972bbbaa0a84231cc0dfeaf9b0305f3a19374`, `0e5e4d60adcd319fa0ad252d6bebed7e06b02122`, `2b3e4591b72bb32b61707c1e73efef4f03a99cf9`, `eae21daa515a6c6838259e72722f773c698c3d2e`, `055ee65bfe5b288100a69ea9087b7cbee469da88`, `cd8764c39910e6fd84e00824b4d506fa0408a80b`, `7071f87b33911da4f76a59aca9ffd64226b78a47`, `bfb881d37aa96b3efffcbe628053cc235ea1fbac`, `9dc453ea7df070edaa5a38bd5fa49b4459631a11`, `548fe068a33a5be753b55f0f04b96268c990b871`, `7148f3a9218845fc46a55d7d461c6b252fb73442`, `dcc8f6cc9eef17ae14babc2d9d7ee2cea398452d`, `248e444a8a8865b7e77efa0f89f63848f7cbe93b`, `2e68385e3cf4d8c9c8a8ac57c3e78f3cdd467b87`, `703e9f258adc015d76962f7e8484313cea6e0fbb`, `dbab4dbb61a714d53962cd2968e331ca9b61325c`, and `af6fac5b108cdfa061e72ee4f75f4837fb4b3f1c`.

### Version 7 — Third repository documentation audit pass

- **Date:** 2026-11-20
- **Change:** Revise Prompt Master, Romantic Storyteller, and Drawing pattern documentation. Expand read-only directory inventory for approved repository roots.
- **Files modified:**
  - `skills/romantic-storyteller-visual-artist/SKILL.md`
  - `skills/prompt-master/SKILL.md`
  - `skills/prompt-master/references/templates.md`
  - `skills/drawing/references/patterns/README.md`
  - `skills/drawing/references/patterns/PATTERN-TEMPLATES.md`
  - `skills/drawing/references/patterns/failure-patterns.md`
  - `skills/drawing/references/patterns/successful-patterns.md`
- **Review-only files:** `skills/prompt-master/references/patterns.md`, `skills/drawing/README.md`, `skills/asd-ste100/README.md`, `skills/philosophy-religion-asceticism/CHANGELOG.md`, and `skills/prompt-master/README.md`. The Prompt Master README contains marketing copy and product examples. The policy excludes marketing copy and approved examples from controlled-language rewrites.
- **Preserved source material:** `master/Images.md`, `master/Poses.md`, and `master/Prompts.md` contain prompts, pose ideas, and creative text. They were inspected and left unchanged. Prompt templates, worked examples, and historical pattern evidence were also preserved except for nearby explanatory prose.
- **Inventory:** Read-only listings verified the contents of `skills/`, `skills/*/references/`, `skills/drawing/references/patterns/`, and `master/`. The root `drawings/` listing returned 404. Do not infer that the directory is empty.
- **Drawing archive links:** The pattern indexes contain historical links into `drawings/`. That root remains outside the approved workspace roots listed by Session Archiving. I did not follow or change those links. Their targets remain unverified.
- **Link checks:** Internal links in the revised Prompt Master, Romantic Storyteller, and Drawing pattern files point to existing repository paths. Historical `drawings/` links remain unverified.
- **Manual screening:** The edited prose was checked for semicolons and selected sentence-length, phrasal-verb, and structural patterns. The identified findings were revised and read back. These checks are limited and do not replace the official linter.
- **Validation limit:** The official `skills/asd-ste100/scripts/ste-lint.py` was not run. This environment provides repository file and read-only GitHub API operations, but no repository shell or workflow-dispatch action.
- **Read-back verification:** Every changed file was fetched from branch `gpt` after its write. The returned content matched the submitted content.
- **Commits:** `67d88bab7ae188d7c4c5651ebce2e631e88cdda1`, `b7c6d71540efa42d6537cb26cf4ff289a7d69691`, `67ef8472779deac010ba294650fbaa708dab1db1`, `9fa6cbaf7251014a84de3d6f90fda9a1602b467b`, `32d2b9b28e43e9166149bb9e8614ee46ec1b90f4`, `b9f1a49c61e5523eaa1f07d8f22d366869fda82d`, `7157070e5fc3182140ae2bfb5a43ef9d16f96030`, `75b7a9a9c577e48c2fa76b149c6328fbd4e88f4a`, `0a07bcedfa8d1f08a57885c68006dc418cfd1e70`, `b45db648a96f7043de442c5749ecf6b2eab169dc`, `3c5ef19ffc65eeadacad930e916eb90c40b62903`, and `07b42dad84ddda25eb14f242d62850918e876dc0`.

### Version 8 — Active novel template review

- **Date:** 2026-11-20
- **Change:** Complete the review of the active v1.1 novel templates. Remove semicolons from two template placeholder fields.
- **Files modified:**
  - `novels/templates/novel-v1.1.md`
  - `novels/templates/illustration-note-v1.1.md`
- **Review-only files:** `novels/templates/arc-v1.1.md`, `novels/templates/character-profile-v1.1.md`, `novels/templates/development-outline-v1.1.md`, and `novels/templates/open-discussion-v1.1.md` had no identified findings. The v1.1 scene and illustration-prompt templates were reviewed in the earlier pass. Their apparent long lines contain multiple short sentences or creative-writing placeholders.
- **Preserved files:** The v1.0 templates remain historical references. No mass migration or rewrite was performed.
- **Validation:** The two edited files were fetched after each write. Their read-back content matched the submitted text. Both now contain zero semicolons. The official ASD-STE100 linter has not run.
- **Commits:** `0f0a381d042d08aaf3afe29cd8647c1f35d2ea9a` and `2acb3b2511aa8dcd3cd27c5f5574967805877888`.

### Version 9 — Linter and CI capability review

- **Date:** 2026-11-20
- **Change:** Review the official linter source and existing GitHub Actions workflows to identify a valid execution route.
- **Files reviewed:** `skills/asd-ste100/scripts/ste-lint.py`, `.github/workflows/convert-images-to-webp.yml`, and `.github/workflows/notification.yml`.
- **Linter scope:** The linter checks semicolons, selected phrasal verbs, marketing adjectives, nominalizations, long sentences, synonym rotation, and dangling conjunctions. Passive voice and present-perfect findings are advisory. It protects hedges and does not claim to check noun clusters.
- **Self-test:** Not run. This environment cannot execute the repository script.
- **CI review:** Existing workflows process image takeout and send tag notifications. Neither runs the STE linter. No workflow-dispatch action is available through the connected GitHub tools.
- **Next validation step:** Run `python3 skills/asd-ste100/scripts/ste-lint.py --selftest` in a repository shell. Then run it against the applicable operational files and review each finding.
- **Validation status:** Source review only. The linter remains unexecuted.

### Version 10 — Workspace root renamed to drawings

- **Date:** 2026-11-20
- **Requested change:** Replace the former `prompts/` workspace root with `drawings/`.
- **Reason:** The workspace folder was renamed.
- **Behavioral impact:** Session records, session briefs, non-novel prompt histories, and drawing assets now use paths under `drawings/`. The approved roots are `images/`, `master/`, `novels/`, `drawings/`, and `skills/`.
- **Files modified:** `skills/INITIALIZATION_POLICY.md`, `skills/session-archiving/SKILL.md`, `skills/session-archiving/references/archive-records-and-image-prompts.md`, `skills/drawing/SKILL.md`, `skills/SESSION_START.md`, and `skills/novelist-initiation/INITIATION.md`.
- **Verification:** Updated files were fetched from branch `gpt` after each write. Directory listings confirmed that `drawings/`, `drawings/history/`, and `drawings/2026-11-20/` exist. The prior root name `prompts/` is no longer used as a workspace path in the revised policy files.
- **Commits:** 70c2148b6cd72be0085ab69129c86b0ce1020993, 2ec76f3eda760d6332ec94d579c731c1fe1712e0, 0f418426f7c787f76bb2ecfac46e8fadcfc2790e, 6e91db2546e201e899753844878ed3e970c0c78c, 624fec7c749e65ebec2f096a33aebddab2168d76, 3de6ea1ca5e735fd088760d3a3f5a86ad25675ef, and 1f57cf5ab070f60281abae37d1658a1cd287e26a.

### Version 11 — Changed-file STE lint workflow

- **Date:** 2026-11-20
- **Requested change:** Add a GitHub Actions workflow that runs the STE linter on each push to branch `gpt` and checks changed Markdown files only.
- **Implementation:** Added `.github/workflows/ste-lint-changed.yml`. The workflow runs the linter self-test and then lints changed Markdown files from the push range.
- **Scope filters:** Excludes creative and historical content under `novels/`, `drawings/`, and `master/`, plus the Romantic Storyteller, Prompt Master, and STE example directories.
- **Safety:** The changed-file list passes through an environment variable rather than shell-script interpolation.
- **Verification:** Workflow source was fetched after each write. GitHub Actions execution is not yet confirmed.
- **Commits:** ca7292d89b9967776bb456060f2c111762e709c0, a2573e61dd651fffb3bfdfda8f17e5670f03f990, and 4e1ab6dc9239514fb374aaa45e4685127bb23838.

### Version 12 — Remaining drawing and technical reference review

- **Date:** 2026-11-20
- **Files reviewed:** `skills/drawing/references/style-guide.md`, `skills/drawing/references/prompt-fidelity.md`, `skills/philosophy-religion-asceticism/references/answer-patterns.md`, `skills/philosophy-religion-asceticism/references/source-standards.md`, and `skills/agent-skill-authoring/SKILL.md`.
- **Review:** Checked sentence structure, semicolon usage, long sentences, and local Markdown references.
- **Disposition:** Review only. No edits in this pass. The prompt-fidelity note contains explicit user-direction preservation language. Any rewrite needs sentence-level comparison to avoid changing scope or intent.
- **Link check:** Checked local Markdown links in the files reviewed. The internal references listed in those files were present in the fetched content.
- **Limit:** This was a manual review. The STE linter and GitHub Actions run were not executed in this environment.

### Version 13 — Skills index and technical-reference review

- **Date:** 2026-11-20
- **Files reviewed:** `skills/README.md`, `skills/philosophy-religion-asceticism/README.md`, `skills/philosophy-religion-asceticism/CHANGELOG.md`, `skills/session-archiving/references/image-processing-scripts.md`, `skills/session-archiving/references/drawing-session-closeout.md`, and `skills/drawing/references/prompt-fidelity.md`.
- **Review:** Checked instructions, technical descriptions, sentence length, semicolons, and scope. Also checked directory references against the current `skills/` listing.
- **Disposition:** Review only. No edits were needed. Preserve the product-access notes because their availability statements contain qualifications. Preserve the prompt-fidelity note because it records explicit user authority and restrictions on assistant-authored prompt changes.
- **Limit:** This was a manual review. The official linter and the GitHub Actions workflow have not run in this environment.

### Version 14 — Correct obsolete prompt archive path

- **Date:** 2026-11-20
- **File updated:** `skills/drawing/references/image-editing-protocol.md`
- **Issue:** Section 6 still directed non-novel prompts to the former `prompts/YYYY-MM-DD/` location.
- **Correction:** Changed that path to `drawings/YYYY-MM-DD/`, the canonical non-novel prompt and session archive.
- **Verification:** Updated the file using its fetched SHA and read it back. Commit: `4914e860d12e7303cf770cd5909ef88aac8f91f3`. Read-back SHA: `dbf2f7fdf20c20a9a640362070f4f559ac5b7f77`.
- **Limit:** This pass confirms the exact correction. It does not establish that every obsolete path in the repository has been found.

### Version 15 — Historical prompt paths and archive template

- **Date:** 2026-11-20
- **Files updated:** `skills/drawing/references/generation-recovery-and-provenance.md` and `skills/session-archiving/references/archive-records-and-image-prompts.md`.
- **Issues:** Two historical prompt records were linked through the obsolete `prompts/` root. The non-novel daily archive template also showed the former root.
- **Corrections:** Updated the historical references to `drawings/history/2026-11-12-image-prompts.md` and `drawings/history/2026-11-13-image-prompts.md`. Updated the daily archive tree to use `drawings/`.
- **Verification:** Fetched each file before editing and read each updated file back. Recovery-reference commit: `1fc167c692a4af5ada5a411b485247aa7714ff34`. Archive-template commit: `bc0a0b880409e162e39871c6c040123cee7d598a`.
- **Limit:** Reviewed these exact references only. Other obsolete path references may remain.

### Version 16 — Scene illustration archive-link consistency

- **Date:** 2026-11-20
- **Scope:** Checked links in active Scene-002 records to the archived 2026-11-16 image prompts after the workspace rename from `prompts/` to `drawings/`.
- **Files updated:**
  - `drawings/2026-11-20/session-01-brief.md`
  - `drawings/2026-11-19/attempt-34.md`
  - `novels/Novel-01/Arc-01/Scene-001/scene.md`
  - `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-01.md`
  - `novels/Novel-01/Arc-01/Scene-002/scene.md`
  - `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-03.md`
- **Corrections:** Replaced stale active archive links with the correct `drawings/history/2026-11-16-image-prompts.md` target. Used four parent-directory levels from `Scene-002/scene.md` and five from files under `illustrations/`.
- **Review-only file:** `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-02.md` already used the correct five-level relative path. No update was needed.
- **Target verification:** Confirmed that `drawings/history/2026-11-16-image-prompts.md` exists. Its exact headings match the links for Attempts 04, 05, and 06.
- **Link verification:** Read back the updated Scene-002 scene and Illustration 03 files. All three scene links and the Illustration 02 and 03 links now use the correct archive root and anchors. The hand-off records the prior read-back verification for the other four updated files.
- **Historical-content handling:** Preserved historical mentions of `prompts/` where they record the former directory structure or earlier events. This pass changed active broken links only.
- **Commits:** Session brief `ffc46b6d1f9b1fad3741b97e6d03db2f78fd815a`, session brief second correction `4d9c16c8a6187622f6af966db2755049b2445bee`, attempt 34 `5fddd54ff1430ac28f7f21c18348a8f0c393895e`, Scene-001 `dd92093dbe7eac3c3e55776c61dca17f63de0e01`, Scene-002 Illustration 01 `3ad0dda79692f0c46135c4814fd5519a47e8efcf`, Scene-002 scene `2536c559bc20cae41e5b966a85ada23738c7334f`, and Scene-002 Illustration 03 `cec4af32f6fe0e4e940ea71528dfe74da3dcc417`.
- **CI result:** The workflow self-test passed. The linter reported four hard findings and 21 advisory findings in this existing file. The four hard findings predate Version 16.
- **Baseline:** The workflow now allows a baseline of four findings for this file only. Other changed Markdown files retain the default zero-finding threshold. This preserves the audit history without weakening checks for other files.
- **Workflow change:** Updated `.github/workflows/ste-lint-changed.yml` in commit `45b9fa4bee248637cf2d13cd33319e5b6030f00d`.
- **CI result:** GitHub Actions run `44695536218` passed. The linter self-test passed. The changed-file lint passed with four hard findings at the documented baseline and 21 advisory findings.
- **Additional path scan:** Read the 20 November brief, Attempt 34, Scene-001, and the Drawing recovery, editing, and archive references on branch `gpt`. None contains an active `prompts/` root path.
- **Historical exceptions:** The 12 November history, summary, and prompt-log files retain `prompts/`, `promts/`, and former `ChatGPT/` paths as records of earlier events. Preserved these historical statements without edits.
- **Search limitation:** GitHub code search indexes the default branch `main`. Used its results only to identify candidate files. Fetched each reviewed file from branch `gpt` before classifying it.
- **CI result:** GitHub Actions run `44695617915` passed after this audit update. The linter self-test and changed-file lint passed. The initialization policy file used its documented baseline of four hard findings.
- **Validation limit:** The full 170-file Markdown/YAML path scan is not complete. The linter run covered the changed initialization policy file, not every technical document in the repository.

### Version 17 — Active-link and full-document lint audit

- **Date:** 2026-11-20
- **Repository inventory:** The complete branch tree contains 170 Markdown and YAML files. The inventory contains 166 Markdown files and four YAML files.
- **Active-link scope:** The relative-link scan covered 121 active Markdown files. It excluded historical archives, novel templates, master source files, and Prompt Master material.
- **Active-link result:** All relative Markdown file targets in the 121-file scope resolve to files in branch `gpt`.
- **Link corrections:** Updated one image path, three Story Arc links, and one Novel 02 Open Discussion link.
- **Historical exceptions:** Nine historical archive files retain unresolved relative links to former image, skill, and novel paths. Some links target records that no longer exist. Preserved these historical records.
- **Template exceptions:** Three novel templates contain placeholder asset or relative paths. These paths do not identify committed assets. Left the templates unchanged.
- **Link-scan limit:** The scan did not check Markdown heading anchors or external URL availability.
- **Technical lint scope:** The full-document workflow checked 37 in-scope technical Markdown files. The linter self-test passed.
- **Mode handling:** The runner disables synonym rotation for STE-flavored prose. It disables the semicolon rule only for the writing-rules reference, which quotes the prohibited mark.
- **Baseline policy:** Twenty-one files use recorded per-file baselines. The combined hard-finding baseline is 179. The full run reported 179 hard findings and 299 advisory findings. No file exceeded its baseline.
- **Intentional examples:** The ASD-STE100 skill has a baseline of 31 hard findings because it contains examples that intentionally violate the rules it teaches.
- **CI interpretation:** Both lint workflows passed against the recorded baselines. The 179 hard findings remain open technical debt. The baselines do not indicate full writing-policy compliance.
- **Lint configuration:** `skills/asd-ste100/scripts/ste-lint-repository.sh` defines the modes and per-file baselines.
- **Lint documentation:** Updated the repository writing policy to document the wrapper. Commit `2b82c740fd36f65eeafd69636df6fbaaf7399554`.
- **Full-document workflow:** `.github/workflows/ste-lint-full-docs.yml`.
- **Changed-file workflow:** `.github/workflows/ste-lint-changed.yml`.
- **CI runs:** Full-document run `44697789997` passed. Changed-file run `44697789995` passed.
- **Relevant commits:** Image index `93d1bb6f6df4250736cf6dd55fb56eb6e799d69e`, Scene-002 Illustration 01 `b39eed6a2d04cf4581a8e01967435467a5a44ae5`, Illustration 02 `6aa685c6f2d30da3eb137d31b6124e9b40071bf2`, Illustration 03 `79dfb067d1f4b299ebe498df43975e8a85390bb0`, Novel 02 link `4a1acd71cbacb4cc0db64cdde5c51ba00a72d164`, lint helper `20eb2e71ec88248dcc52259af122f814f00376da`, changed workflow `a961b693fdfacff11cf355e6e7689e7d92923616`, full workflow `ee628081f7909aa822d53026b3a1f42150c70011`.
- **Remaining work:** Reduce the existing hard findings. Review historical links only after the user authorizes changes to those records. Check heading anchors in a separate pass.

### Version 18 — Markdown and YAML inventory reconciliation

- **Date:** 2026-11-20
- **Scope:** Reconcile the Version 17 file count with the current recursive branch tree.
- **Current inventory:** The branch contains 166 Markdown files and five YAML files, for 171 files in total.
- **Count correction:** Version 17 recorded 166 Markdown files and four YAML files. The earlier count omitted `images/takeout/HANDOFF.yml`.
- **Additional file review:** Fetched `images/takeout/HANDOFF.yml` from branch `gpt`. It contains current `drawings/2026-11-19/images` destination paths. It contains no obsolete `prompts/`, `promts/`, or `ChatGPT/` workspace-root reference.
- **Disposition:** No file change was needed. This entry corrects the inventory count. It does not claim a new full-repository link scan.
- **Audit status:** The Version 17 relative-link and full-document lint results remain as recorded. The audit remains open while the 179 hard lint findings and the documented historical-link and heading-anchor work remain unresolved.

### Version 19 — Active Markdown heading-anchor audit

- **Date:** 2026-11-20
- **Scope:** Checked links in 119 active Markdown files. The scan excluded `drawings/history/`, `master/`, `novels/templates/`, `skills/prompt-master/`, and `skills/asd-ste100/examples/` as source files.
- **Destination inventory:** The checker indexed all 166 Markdown files. Excluded files remained valid link destinations.
- **Link result:** Checked 262 local Markdown links. Found zero unresolved Markdown targets or heading anchors.
- **Link update:** The five image-inventory links in `drawings/2026-11-19/README.md` now use the GitHub heading anchor with a double hyphen for the em dash.
- **Checker:** Added `skills/asd-ste100/scripts/check_markdown_anchors.py`. Added the check to `.github/workflows/ste-lint-full-docs.yml`.
- **CI:** Full-document run `44698774629` passed. Changed-document run `44698774600` passed. Both runs checked commit `837f415b040c8d0cbcc16eff77cedc732433acce`.
- **Lint result:** The full run checked 37 technical Markdown files. It reported 179 hard findings and 300 advisory findings. Each file stayed at or below its recorded hard-finding baseline. The linter self-test passed.
- **Scope reconciliation:** Version 17 reported 121 active Markdown files. This repeatable scan found 119 files under the exclusions listed above. The Version 17 entry does not record its exact file list, so the two counts are not equivalent. Keep this discrepancy open until the earlier scan scope can be reconstructed.
- **Validation limits:** The checker does not test external URLs. It checks local Markdown file targets and GitHub-style heading anchors from active source files. It indexes excluded files as link destinations.
- **Remaining work:** Reduce the 179 existing hard findings without raising baselines. Review historical link records only after the user authorizes changes. Reconcile the 121-file and 119-file scan scopes.

### Version 20 — Audit-log lint cleanup

- **Date:** 2026-11-20
- **Scope:** Reword four audit statements in this file to address synonym-rotation findings from the previous full lint.
- **Baseline policy:** No lint baseline changed.
- **Commit:** `939d19a16e533ab1e08e4f78ba7dbdb8c70c2fd5`.
- **CI:** Validated by the descendant commit and runs recorded in Version 21.

### Version 21 — Additional technical-document lint cleanup

- **Date:** 2026-11-20
- **Scope:** Reword one synonym-rotation finding in the novelist-initiation skill. Split one long sentence in the scholarly source-standards reference.
- **Baseline policy:** No lint baseline changed.
- **Commits:** `e63664c41c381c7d769965103136f3f4178fbbc2` and `d7b12def70dfb49e8063243345cc328d7c348eea`.
- **CI:** Full-document run `44700856846` passed. Changed-document run `44700856776` passed. Both runs checked descendant commit `d0f77537732af092a62a472d37425f0c41abeff`, which includes these changes.

### Version 22 — Further technical-document lint cleanup

- **Date:** 2026-11-20
- **Scope:** Reworded three synonym-rotation findings in the conversation-mode skill and two in this audit log.
- **Files changed:** `skills/conversation-mode/SKILL.md` and `skills/INITIALIZATION_POLICY.md`.
- **Baseline policy:** No lint baseline changed.
- **Read-back:** Both committed files were fetched from branch `gpt`. The requested text changes were present.
- **Commits:** `4cb4445ff4be63853e24a03312e9b290275dd2af`, `6df11cd446aeaf68def816db91e1b59d2f3fa69a`, and `55c54b11d9c2f941c4c553bcbc726db74a6cba18`.
- **CI:** Pending. Check the result on the next user turn.

### Version 23 — Novelist initiation lint cleanup

- **Date:** 2026-11-20
- **Scope:** Align verification terms and reduce synonym-rotation findings in the novelist initiation protocol. Preserve all initiation gates and user-authority conditions.
- **File changed:** `skills/novelist-initiation/INITIATION.md`.
- **Baseline policy:** No lint baseline changed.
- **Read-back:** The committed file was fetched from branch `gpt`. The revised instructions were present.
- **Commits:** `0653ef18680613263b415b95bea5e283128e1cea` and `e0a78c077559c9b2b95c53f2681d9c6fe24a8f04`.
- **CI:** Pending. Check the result on the next user turn.

### Version 24 — GitHub Actions skill separation and foundational loading

- **Date:** 2026-11-20
- **Change:** Move GitHub Actions workflow instructions out of Conversation Mode and into a dedicated foundational skill.
- **New skill:** `skills/github-actions/SKILL.md`.
- **Imported source:** `skills/github-actions/references/user-supplied-optimization-notes.md`.
- **Integration:** Add the skill to the foundational initialization sequence, mandatory execution gate, skills index, and copyable project instructions.
- **Conversation Mode:** Retain only a link to the specialist workflow skill. Remove GitHub Actions procedures and repository workflow details.
- **Reason:** Keep collaboration behavior separate from CI and workflow engineering.

### Version 25 — Consolidate novelist initiation procedure

- **Date:** 2026-11-20
- **Change:** Move the detailed novelist onboarding procedure into the canonical `skills/SESSION_START.md` file.
- **Historical entry point:** The task-specific `skills/novelist-initiation/SKILL.md` entry point was retained at that time. Version 30 records its later removal.
- **Removed duplicate:** Delete `skills/novelist-initiation/INITIATION.md`.
- **Activation:** The `Be the novelist` cue requires foundational initialization before novelist-specific work.
- **Reason:** Keep the full initialization sequence and specialist procedure in one authoritative startup document.

### Version 26 — Add CI checkpoint rules to copyable instructions

- **Date:** 2026-11-20
- **Change:** Add the repository CI checkpoint policy to the copyable custom-instructions block.
- **Historical behavior:** The former preflight and pending-run checks were later superseded by Version 30. The current policy is maintained only in `skills/github-actions/SKILL.md`.
- **Reason:** This records the earlier policy state.
- **File changed:** `skills/INITIALIZATION_POLICY.md`.

### Version 27 — Use one session-start cue

- **Date:** 2026-11-20
- **Change:** Make `start session` the only session-start cue.
- **Canonical instructions:** Keep all session-start procedures in `skills/SESSION_START.md` and its mandatory execution gate.
- **Copyable instructions:** Reduce the custom-instructions block to one sentence that points to Session Start and names the sole cue.
- **Specialist roles:** Require successful session initialization before role-specific onboarding.

### Version 28 — Expand copyable repository instructions

- **Date:** 2026-11-20
- **Requested change:** Include the repository name, branch, sole-source-of-truth rule, conditional initialization rule, and startup-note reference in the copyable instructions.
- **Behavioral impact:** The copyable block now contains the complete three-paragraph instruction text supplied by the user.
- **File changed:** `skills/INITIALIZATION_POLICY.md`.


### Version 29 — Make Drawing an on-demand prerequisite

- **Date:** 2026-11-20
- **Change:** Remove Drawing from foundational initialization. Add the separate `start a drawing session` cue. Retain Drawing as a prerequisite for novelist-role initialization.
- **Behavioral impact:** Load Drawing and its required references only for drawing sessions or novelist initialization. Reuse files already verified in the current conversation.
- **Reason:** Avoid loading specialist drawing procedures during unrelated sessions.
- **Canonical procedure:** `skills/SESSION_START.md`; mandatory foundational gate: `skills/session-archiving/SKILL.md`.


### Version 30 — Remove duplicate novelist entry point and centralize CI policy

- **Date:** 2026-11-20
- **Change:** Delete `skills/novelist-initiation/SKILL.md` because the complete novelist initialization procedure is already maintained in `skills/SESSION_START.md`. Remove its active references.
- **CI ownership:** Move the former Conversation Mode Sections 7 and 8 into `skills/github-actions/SKILL.md`. Remove the duplicate sections from Conversation Mode.
- **Behavioral impact:** GitHub Actions is the sole authority for CI behavior. The current policy is implementation-first: use normal GitHub events, do not manually stimulate or routinely inspect CI, and treat a user-requested CI investigation as a separate task.
- **Reason:** Remove duplicate entry points and conflicting CI instructions.


### Version 31 — Enforce the foundational → Drawing → Novelist hierarchy

- **Date:** 2026-11-20
- **Change:** Define three ordered dependency tiers and a per-conversation verified-load ledger.
- **Behavioral impact:** Drawing and novelist requests automatically load missing prerequisite tiers. Successfully read files are reused when moving between tiers or returning to a prior tier. Only missing or explicitly invalidated files are retrieved.
- **Reason:** Prevent duplicate skill and reference loading while preserving dependency order.
- **Canonical procedure:** `skills/SESSION_START.md`; execution gate: `skills/session-archiving/SKILL.md`.


### Version 32 — Add The Worker and workspace continuity

- **Date:** 2026-11-20
- **Change:** Add The Worker as a foundational, conversation-mode-independent task continuity skill.
- **Workspace:** Add the task board, task template, task records, and workspace instructions under `workspace/`.
- **Archive:** Add `archive/` with a 14-day retention policy for archived task files.
- **Integration:** Add The Worker to the canonical foundational sequence, mandatory execution gate, and skills index. Expand the Session Archiving workspace boundary.
- **Conversation Mode:** Make Condensed Mode reports minimal and navigation-first. Keep task operations under The Worker.
- **Task policy:** Use UTC timestamp IDs, every-step meaningful progress logs, automatic necessary follow-ups, and Proposed optional improvements.
- **Initialization:** Preserve conditional initialization and the sole `start session` cue.

