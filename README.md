# subnet-watch

Hourly, read-only monitor over all ~128 Bittensor subnets. A GitHub Action sweeps
the chain and GitHub and commits the results to `data/`; a **ChatGPT Project**
reads those files and does the alarming, ranking and explaining.

**Governing principle: the pipeline produces numbers, ChatGPT produces prose.
Neither crosses over.** Every number in a ChatGPT reply is a quotation from a
file in this repo, with a citation.

## Why the split

ChatGPT browsing was tested against every candidate source on 2026-07-27:

| Source | Result |
|---|---|
| `raw.githubusercontent.com/.../README.md` | ✅ full content |
| `github.com/<o>/<r>/{releases,commits/main}.atom` | ✅ real timestamps, unauthenticated, no rate limit |
| `taostats.io/subnets` | ⚠️ a 10-row deregistration table only |
| `taostats.io/subnets/<N>` | ⚠️ price / market cap / volume only |
| `taostats.io/api/subnets`, `api.tao.app` | ❌ HTTP 401 |
| `taomarketcap.com/subnets` | ❌ JS shell serving **placeholder zeros** |
| Substrate RPC | ❌ POST-only; unreachable from browsing |

So ChatGPT can do the GitHub side natively and well, and **cannot** obtain burn,
income, incentive structure or registration cost at all. Those come from the
chain sweep in this repo.

The stale sources are worse than they look: **12 of 128 subnets completely
changed identity in the 24 days** to 2026-07-27 (sn27 `compute-subnet` →
`SILX-LABS/Orion`, sn53 `EfficientFrontier` → `engy`, sn40 `chunking_subnet` →
`ralph`). A registry frozen in March 2025 describes a different network.

## Layout

```
collector/           the sweep
  chain.py           read-only chain access + MinerBurned / WeightsVersionKey /
                     MechanismCount raw storage maps
  econ.py            dTAO income, distribution, and COMPETITIVE miner income
  gh.py              repo URL hygiene, atom feeds, README, min_compute
  events.py          the new-challenge detector + alarm window
  margin.py          requirement -> cheapest machine -> net margin
  score.py           gates, weights, deterministic ranking
  render.py          the files ChatGPT reads
  briefs.py          bootstrap one challenge brief per subnet
data/                published every hour (MANIFEST, SNAPSHOT, ALARMS, RANKING, ...)
briefs/sn<NN>.md     the 128 challenge briefs
chatgpt/             the files to attach to the ChatGPT Project
tests/               regression tests for the parts that fail silently
```

## Run locally

```bash
python -m collector.run                # full sweep (~80 s)
python -m collector.run --skip-github  # chain only (~20 s)
python -m collector.run --seed         # record events without alarming
python -m collector.briefs             # regenerate all briefs
python -m pytest tests/ -q
```

Needs `bittensor` and `requests`. No API key, no wallet, nothing is ever spent.

## The two numbers that matter most

**`miner_burn`** — the fraction of miner emission withheld by owner-controlled
hotkeys and destroyed. **38 of 128 subnets sit at ≥0.99 today**: miners there earn
nothing regardless of any other figure. Those are gated out of the ranking.

**`competitive_miner_usd_day`** — the best miner that is neither owner-controlled
nor validator-permitted. This is the only income figure quotable as achievable,
and the gap is not academic:

| Subnet | headline top miner | competitive |
|---|---|---|
| sn95 Actual | $27,976/day | **$0 — 100% burn** |
| sn46 Zipcode | $3,297/day | **$6.40/day** |
| sn26 Perturb | $1,501/day | **$8.98/day** |

## What counts as a new challenge

`NEW_SUBNET`, `WEIGHTS_VERSION_BUMP`, `MECHANISM_ADDED`, `BURN_DROP`, `RELEASE`,
`SCORING_COMMIT`, `README_TASK_DIFF`, `REGISTRATION_OPENED`.

**Not** an advancing `last_step` / scoring epoch. That ticks several times an hour
on every subnet; reporting it would mean ~3000 alarms a day and the feed would be
ignored within a week. Two consecutive sweeps of this pipeline produce **0**
events.

## Setup

See `chatgpt/PROJECT_SETUP.md`. Replace `OWNER/REPO` in `chatgpt/01_SOURCES.md`
first — it is the only file that needs editing.

**Do the acceptance test before trusting the monitor:** disable the workflow, wait
90 minutes, and confirm the ChatGPT task replies `STALE FEED` and not `QUIET`. A
dead cron produces a confident all-clear forever and looks exactly like success.
It is the only failure here that can mislead indefinitely.
