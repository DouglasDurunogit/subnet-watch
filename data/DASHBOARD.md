# Subnet watch — dashboard

_snapshot 2026-08-12T23:54:36Z · block 8831844 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 2 | `█` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.7 | 111 | 374 | cpu-small | 10 | 27% |
| 2 | sn107 Minos | 77.8 | 105 | 31,092 | cpu-small | 20 | 90% |
| 3 | sn67 Harnyx | 71.4 | 17.92 | 746 | cpu-small | 131 | 20% |
| 4 | sn96 Verathos | 71.1 | 43.58 | 375 | rtx4090 | 49 | 42% |
| 5 | sn91 cascade | 70.1 | 761 | 2,625 | rtx4090* | 5 | 50% |
| 6 | sn114 SOMA | 69.6 | 663 | 4,353 | rtx4090* | 4 | 65% |
| 7 | sn62 Ridges | 69 | 544 | 1,968 | rtx4090* | 7 | 35% |
| 8 | sn41 Almanac | 69 | 10.53 | 29.86 | cpu-small | 68 | 72% |
| 9 | sn56 Gradients | 68.9 | 532 | 977 | rtx4090* | 7 | 65% |
| 10 | sn100 BASE | 68.3 | 448 | 1,815 | rtx4090* | 5 | 50% |
| 11 | sn26 Perturb | 67.8 | 19.32 | 36.66 | rtx3060 | 11 | 50% |
| 12 | sn21 AdTAO | 67.6 | 7.49 | 33.63 | cpu-small | 88 | 45% |
| 13 | sn15 ORO | 67 | 9.03 | 12,259 | cpu-small | 69 | 94% |
| 14 | sn124 Swarm | 66.5 | 266 | 697 | rtx4090* | 21 | 12% |
| 15 | sn80 OpenRoboto | 64.9 | 162 | 587 | rtx4090* | 4 | 91% |
| 16 | sn38 ChronoLLM | 64.6 | 161 | 3,504 | rtx4090* | 10 | 52% |
| 17 | sn85 Vidaio | 63.9 | 119 | 496 | rtx4090* | 10 | 16% |
| 18 | sn28 gm | 61.5 | 58.82 | 2,522 | rtx4090* | 29 | 26% |
| 19 | sn51 lium.io | 59.8 | 42.62 | 2,258 | rtx4090* | 48 | 70% |
| 20 | sn102 ConnitoAI | 59.6 | 1,141 | 1,914 | rtx4090* | 6 | 32% |

`=` after the ceiling means it equals the median exactly - either one competitive
miner exists, or they all earn the same. Both columns use identical precision;
if they ever disagree the data is wrong, since a median cannot exceed its own max.

`net $/day (median)` is what a newcomer should expect: the MEDIAN non-owner,
non-permitted miner, minus machine cost. `ceiling $/day` is the BEST competitive
miner - reachable only by beating everyone already there. Where the two diverge
wildly, the subnet is winner-take-all and the ceiling is not a plan.

`*` = machine is an assumed default; no hardware evidence was found for that subnet.

![top 20 by score](charts/top20.svg)

## Concentration — reported, never scored

A low top-1 share means many miners share the emission. A high one means a
single UID takes almost everything, so the headline income is not reachable.
**This is deliberately excluded from the score** — judge the shape yourself.

| top-1 share | subnets (of those that pay) |
|---|---:|
| wide (<30%) | 25 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-12T23:55 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-12T22:57 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Merge pull request #42 from corvxai/mkt_s |
| 2026-08-12T18:40 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: update miner screen reply readme |
| 2026-08-12T15:29 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Add validator cost profile |
| 2026-08-12T14:09 | sn28 | RELEASE | sn28 released v0.4.4 |
| 2026-08-12T14:09 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Release gm-miner v0.4.4 |
| 2026-08-12T14:09 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Oversample 2026+ models into one R1 and o |
| 2026-08-12T14:09 | sn96 | RELEASE | sn96 released Verathos v0.1.37 — Scoring Integrity and Fairness |
| 2026-08-12T14:09 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: correct validator scoring inputs |
| 2026-08-12T14:09 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: publish bench rollout records: per-task  |
| 2026-08-12T14:09 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |
| 2026-08-12T12:34 | sn28 | RELEASE | sn28 released v0.4.4-dev |
| 2026-08-12T12:34 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Document miner model sourcing options |
| 2026-08-12T12:34 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-08-12T12:34 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

