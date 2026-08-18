# Subnet watch — dashboard

_snapshot 2026-08-18T18:13:15Z · block 8873336 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 37 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.2 | 98.18 | 190 | cpu-small | 10 | 20% |
| 2 | sn21 AdTAO | 76.6 | 66.92 | 271 | cpu-small | 16 | 30% |
| 3 | sn67 Harnyx | 71.9 | 20.05 | 428 | cpu-small | 131 | 13% |
| 4 | sn26 Perturb | 70.7 | 39.27 | 72.11 | rtx3060 | 10 | 70% |
| 5 | sn1 Apex | 70.3 | 813 | 1,098 | rtx4090* | 4 | 53% |
| 6 | sn56 Gradients | 69.4 | 628 | 929 | rtx4090* | 5 | 72% |
| 7 | sn41 Almanac | 69.1 | 10.54 | 35.94 | cpu-small | 75 | 67% |
| 8 | sn91 cascade | 69 | 546 | 2,207 | rtx4090* | 5 | 52% |
| 9 | sn62 Ridges | 68.4 | 453 | 2,101 | rtx4090* | 6 | 40% |
| 10 | sn15 ORO | 67.6 | 10.22 | 19.62 | cpu-small | 67 | 95% |
| 11 | sn38 ChronoLLM | 67.4 | 143 | 3,032 | cpu-small | 10 | 52% |
| 12 | sn96 Verathos | 67.1 | 16.36 | 427 | rtx4090 | 84 | 41% |
| 13 | sn11 TrajectoryRL | 67 | 4,064 | 4,064 = | cpu-small | 1 | 100% |
| 14 | sn85 Vidaio | 63.9 | 119 | 1,323 | rtx4090* | 13 | 42% |
| 15 | sn107 Minos | 63.7 | 102 | 33,612 | cpu-small | 19 | 90% |
| 16 | sn81 Reliquary | 63.3 | 98.53 | 388 | rtx4090* | 34 | 9% |
| 17 | sn53 engy | 63 | 91.17 | 2,144 | rtx4090 | 144 | 11% |
| 18 | sn55 NIOME | 61.4 | 56.01 | 474 | rtx4090* | 11 | 29% |
| 19 | sn28 gm | 60.9 | 50.14 | 2,234 | rtx4090* | 40 | 23% |
| 20 | sn51 lium.io | 59.7 | 40.92 | 896 | rtx4090* | 55 | 81% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 17 |
| captured (>90%) | 29 |

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
| 2026-08-18T15:42 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: miner: tee_miner, a pure gateway leg with |
| 2026-08-18T15:42 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Burn 60% of miner emission, split the ot |
| 2026-08-18T14:48 | sn1 | RELEASE | sn1 released v4.3.3 |
| 2026-08-18T14:48 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Merge pull request #47 from TrishoolAI/fe |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

