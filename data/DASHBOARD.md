# Subnet watch — dashboard

_snapshot 2026-08-05T16:49:36Z · block 8779328 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 53 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 9 | `█████` |
| ≥0.99 dead | 39 | `█████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.8 | 193 | 388 | cpu-small | 7 | 25% |
| 2 | sn107 Minos | 77.5 | 98.75 | 28,514 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 76.8 | 2,203 | 2,203 = | cpu-small | 2 | 90% |
| 4 | sn98 NeverPlayAlone | 76 | 1,712 | 1,712 = | cpu-small | 1 | 100% |
| 5 | sn114 SOMA | 72.7 | 1,667 | 4,347 | rtx4090* | 3 | 65% |
| 6 | sn67 Harnyx | 72.3 | 22.87 | 979 | cpu-small | 155 | 22% |
| 7 | sn91 cascade | 70.2 | 779 | 3,140 | rtx4090* | 5 | 52% |
| 8 | sn102 ConnitoAI | 69.6 | 660 | 1,652 | rtx4090* | 7 | 26% |
| 9 | sn62 Ridges | 69.5 | 634 | 2,608 | rtx4090* | 7 | 35% |
| 10 | sn26 Perturb | 68.9 | 24.99 | 203 | rtx3060 | 11 | 50% |
| 11 | sn41 Almanac | 68.4 | 9.03 | 66.74 | cpu-small | 60 | 78% |
| 12 | sn15 ORO | 67.1 | 8.80 | 10,883 | cpu-small | 75 | 93% |
| 13 | sn74 Gittensor | 66.2 | 239 | 262 | rtx4090* | 9 | 18% |
| 14 | sn124 Swarm | 65.8 | 221 | 635 | rtx4090* | 23 | 10% |
| 15 | sn38 ChronoLLM | 65.6 | 210 | 3,527 | rtx4090* | 10 | 52% |
| 16 | sn21 AdTAO | 65.5 | 4.77 | 22.06 | cpu-small | 142 | 45% |
| 17 | sn80 OpenRoboto | 62.3 | 72.92 | 276 | rtx4090* | 4 | 91% |
| 18 | sn101 Tag101 | 59.2 | 0.07 | 0.74 | cpu-small | 244 | 90% |
| 19 | sn28 gm | 58.6 | 25.18 | 6,726 | rtx4090* | 15 | 71% |
| 20 | sn61 RedTeam | 58.5 | 23.24 | 105 | rtx4090* | 90 | 3% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 22 |
| captured (>90%) | 24 |

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
| 2026-08-05T16:50 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T16:50 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #24 from conjectures-i |
| 2026-08-05T14:53 | sn21 | RELEASE | sn21 released SN21 training bundle |
| 2026-08-05T14:53 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: resolve the first-basket date ambig |
| 2026-08-05T14:53 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T14:53 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #23 from conjectures-i |
| 2026-08-05T14:53 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Disclose the serving stack so miners can |
| 2026-08-05T12:15 | sn12 | RELEASE | sn12 released miner-staging-2026-08-05-31002481795-421-1: fix: replace |
| 2026-08-05T12:15 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(verifiability): W1+W3 — miners can n |
| 2026-08-05T12:15 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T12:15 | sn61 | RELEASE | sn61 released 4.9.0 |
| 2026-08-05T12:15 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: uncomment validation for miner conta |
| 2026-08-05T12:15 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #17 from conjectures-i |
| 2026-08-05T12:15 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-05T12:15 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

