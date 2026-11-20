---
created: 2026-11-20T15:22
updated: 2026-11-20T15:29
---

---

Pro Tip: Override Per Artifact

You do not have to apply the same rule to everything. Keep your repository-wide retention at **14 days** for logs, and set a shorter `retention-days` limit directly inside your workflow YAML file for heavy build artifacts:

yaml

```
- uses: actions/upload-artifact@v4
  with:
    name: my-large-build
    path: dist/
    retention-days: 5
```

---

To save the most minutes and storage on a private repository, ==**start by caching dependencies, canceling redundant runs, and filtering triggers so workflows only execute when relevant files change.**==

Because every GitHub Actions job rounds up to the nearest full minute and Linux runners cost significantly less than Windows or macOS, combining a few workflow tweaks can cut your monthly usage in half.

1. Cancel Redundant In-Progress Runs

If you push three quick commits in a row, GitHub runs all three workflows simultaneously by default—wasting minutes on outdated commits. Add a `concurrency` block at the top of your workflow file to automatically cancel older runs on the same branch or PR:

yaml

```
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

---

3. Cache Package Dependencies

Downloading `node_modules`, Python packages, or Go/Rust dependencies on every run burns minutes. Most official `setup-*` actions have built-in caching you can enable with one line:

yaml

```
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm' # Also supports 'yarn' or 'pnpm'
```

_(Similar built-in `cache:` flags exist for `actions/setup-python`, `actions/setup-go`, and `actions/setup-java`.)_

---

4. Choose the Cheapest Runner & Set Timeouts

- **Stick to `ubuntu-latest`:** Standard Linux runners consume 1x minutes ($0.006/min), whereas Windows consumes ~1.6x and macOS consumes ~10x. Only use macOS or Windows when building platform-specific binaries.
- **Prevent hung jobs:** A frozen test script can burn 360 minutes (6 hours) before timing out. Always add `timeout-minutes` to your jobs:

yaml

```
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 15
```

---

5. Keep Artifact Storage Under 500 MB

Standard workflow text logs are free, so storage limits only hit when you use `upload-artifact`.

- **Compress before uploading:**
    
    Zip folders or only upload failing test screenshots rather than full build directories.
- **Expire artifacts early:** Set `retention-days: 3` or `5` directly inside `actions/upload-artifact@v4` so temporary builds do not eat into your 500 MB allowance for 90 days.

---
