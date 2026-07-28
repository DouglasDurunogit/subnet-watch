# 01_SOURCES — the only URLs you may visit

**Before using this file, replace `OWNER/REPO` everywhere below with your actual
public repo path.** Every other file refers back to this one, so this is the
single place that needs editing.

Base (all data files live here):

```
https://raw.githubusercontent.com/OWNER/REPO/main/
```

## ALLOWED — fetch these, in this order

| Purpose | URL |
|---|---|
| **Run metadata. ALWAYS FETCH FIRST.** | `.../main/data/MANIFEST.json` |
| Pre-diffed alarms | `.../main/data/ALARMS.md` |
| Ranking + component points | `.../main/data/RANKING.md` |
| One subnet's evidence pack | `.../main/data/subnets/sn<NN>.md` |
| One subnet's challenge brief | `.../main/briefs/sn<NN>.md` |
| Machine cost table | `.../main/data/machines.csv` |
| Requirement → machine → margin | `.../main/data/MARGIN.csv` |
| Full table (last resort; large) | `.../main/data/SNAPSHOT.csv` |
| Raw event log (auditing only) | `.../main/data/EVENTS.jsonl` |

Also allowed, **only when the user explicitly asks you to read a subnet's own
repository**, and only for a repo whose URL you got from `github_url_resolved`
in an evidence pack you already fetched:

- `https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<file>`
- `https://github.com/<owner>/<repo>/releases.atom`
- `https://github.com/<owner>/<repo>/commits/<branch>.atom`

Anything you learn this way is tagged `[LIVE-READ — not in snapshot]` and may
**never** enter a score, a ranking, or an alarm.

## BANNED — never fetch, never quote, never "sanity check" against

These are not stylistic preferences. Each was tested on 2026-07-27 and each
fails in a way that produces confident, wrong answers.

| Source | What actually happens |
|---|---|
| `taomarketcap.com` | Empty JavaScript shell. Numeric fields render as **placeholder zeros**. The most dangerous source in the ecosystem, because the failure looks exactly like data. |
| `taostats.io/subnets` | Renders only a 10-row deregistration table. No burn, no emission, no reg cost, no GitHub. |
| `taostats.io/subnets/<N>` | Only price, market cap, volume, block. None of the metrics this project needs. |
| `taostats.io/api/*`, `api.taostats.io` | HTTP 401. Requires a paid key. |
| `api.tao.app` | HTTP 401. Requires a key. |
| `api.bittensor.com` | Dead — `DEPLOYMENT_NOT_FOUND`. |
| `bittensor.com/subnets`, `learnbittensor.org/subnets` | HTTP 404. |
| `bittensor-subnet-template` → `template/subnet_links.py` | Frozen at sn37 and still calls sn1 "prompting". A classic hallucination trap. |
| `taostat/subnets-infos` → `subnets.json` | Frozen at netuid 74, last updated March 2025. Names 54 subnets that no longer match chain. |
| Any Substrate RPC endpoint | RPC is POST-only. You cannot reach it. Any answer that appears to come from one is fabricated. |
| Any blog, Medium post, or "list of Bittensor subnets" page | Stale by construction. |

## Why the ban list matters more than it looks

Measured on this repo's own data: **12 of 128 subnets completely changed
identity in the 24 days** between 2026-07-03 and 2026-07-27 — sn27 went from
`neuralinternet/compute-subnet` to `SILX-LABS/Orion`, sn53 from
`EfficientFrontier` to `engy`, sn40 from `chunking_subnet` to `ralph`. A
registry that is 16 months stale is not slightly wrong; it is describing a
different network.

**The netuid → name → repo mapping comes from `SNAPSHOT.csv` and nowhere else.**
If a subnet is not in the snapshot, it does not exist for this project.

## Schedule coupling

`data/config.json` holds `watch_interval_minutes`. If you change how often the
ChatGPT Task runs, change that value **in the same commit** — the alarm window
is computed from it. Run less often than the window and events report late; run
more often and they appear once, then correctly sit in STILL OPEN.
