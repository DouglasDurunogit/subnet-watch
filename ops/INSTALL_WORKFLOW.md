# Activating the hourly sweep

`ops/sweep.yml` is the GitHub Actions workflow. It is parked here rather than at
`.github/workflows/sweep.yml` because the push that created this repo used an
OAuth token without the `workflow` scope, and GitHub refuses any push that
creates or updates a file under `.github/workflows/`.

Nothing is wrong with the file. Pick either route.

## Route A — web UI (no scope needed, ~1 minute)

1. Open the repo → **Actions** → **New workflow** → **set up a workflow yourself**.
2. Name it `sweep.yml`.
3. Paste the entire contents of `ops/sweep.yml`.
4. **Commit changes.**
5. Delete `ops/sweep.yml` afterwards so there is only one copy to maintain.

## Route B — grant the scope, then move it (keeps one commit)

```bash
gh auth refresh -h github.com -s workflow      # retry if it says slow_down
mkdir -p .github/workflows
git mv ops/sweep.yml .github/workflows/sweep.yml
git rm ops/INSTALL_WORKFLOW.md
git commit -m "ci: activate the hourly sweep workflow"
git push
```

## Either way, then

- **Actions → sweep → Run workflow** once manually to confirm it goes green.
- Check that `data/MANIFEST.json` gets a fresh `generated_utc`.
- The schedule is `7 * * * *` (hourly at :07). If you change it, change
  `watch_interval_minutes` in `data/config.json` in the same commit, or alarms
  report late.
