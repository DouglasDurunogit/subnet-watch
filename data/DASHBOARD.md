# Subnet watch — dashboard

_snapshot 2026-08-18T19:39:50Z · block 8873769 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 37 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.2 | 98.02 | 189 | cpu-small | 10 | 20% |
| 2 | sn67 Harnyx | 71.8 | 20.04 | 427 | cpu-small | 131 | 13% |
| 3 | sn26 Perturb | 70.8 | 40.14 | 73.72 | rtx3060 | 10 | 69% |
| 4 | sn1 Apex | 70.3 | 808 | 1,091 | rtx4090* | 4 | 53% |
| 5 | sn56 Gradients | 69.4 | 625 | 929 | rtx4090* | 5 | 72% |
| 6 | sn41 Almanac | 69.1 | 10.53 | 35.92 | cpu-small | 75 | 67% |
| 7 | sn91 cascade | 69 | 545 | 2,206 | rtx4090* | 5 | 52% |
| 8 | sn62 Ridges | 68.3 | 452 | 2,095 | rtx4090* | 6 | 40% |
| 9 | sn38 ChronoLLM | 67.4 | 143 | 3,026 | cpu-small | 10 | 52% |
| 10 | sn15 ORO | 67.4 | 10.17 | 19.54 | cpu-small | 67 | 95% |
| 11 | sn96 Verathos | 67.1 | 16.09 | 420 | rtx4090 | 84 | 41% |
| 12 | sn21 AdTAO | 65.3 | 4.45 | 580 | cpu-small | 15 | 42% |
| 13 | sn107 Minos | 64.1 | 115 | 33,400 | cpu-small | 20 | 90% |
| 14 | sn85 Vidaio | 63.8 | 117 | 366 | rtx4090* | 13 | 42% |
| 15 | sn81 Reliquary | 63 | 90.02 | 351 | rtx4090* | 34 | 12% |
| 16 | sn53 engy | 62.9 | 88.01 | 2,076 | rtx4090 | 144 | 11% |
| 17 | sn55 NIOME | 61.3 | 55.11 | 453 | rtx4090* | 11 | 29% |
| 18 | sn28 gm | 60.9 | 49.28 | 1,653 | rtx4090* | 38 | 17% |
| 19 | sn51 lium.io | 59.8 | 41.68 | 895 | rtx4090* | 55 | 81% |
| 20 | sn102 ConnitoAI | 57.4 | 603 | 1,312 | rtx4090* | 7 | 26% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 18 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-18T19:40 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: Merge pull request #51 from thenervelab/f |
| 2026-08-18T19:40 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(validator): clarify CHUTES_API_KEY  |
| 2026-08-18T19:07 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs(miner-guide): note that find_product |
| 2026-08-18T19:07 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-08-18T18:13 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #480 from ridgesai/upd |
| 2026-08-18T17:39 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: validator: daily-stream API path crashed  |
| 2026-08-18T17:39 | sn25 | RELEASE | sn25 released v2026.8.17-1021635350 |
| 2026-08-18T17:39 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge pull request #3 from Ryanmello07/fi |
| 2026-08-18T17:39 | sn25 | README_TASK_DIFF | sn25 README task/scoring sections changed |
| 2026-08-18T17:39 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-08-18T16:57 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: validator: daily-stream override was sile |
| 2026-08-18T16:57 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Correct the loopback sample output in the |
| 2026-08-18T16:57 | sn92 | README_TASK_DIFF | sn92 README task/scoring sections changed |
| 2026-08-18T16:12 | sn96 | RELEASE | sn96 released Verathos v0.1.41 - Bounded Replay and Runtime Stability |
| 2026-08-18T16:12 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: prevent validator-created audit over |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

