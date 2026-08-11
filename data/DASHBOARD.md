# Subnet watch — dashboard

_snapshot 2026-08-11T13:52:55Z · block 8821643 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 7 | `████` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.1 | 112 | 32,424 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.7 | 67.07 | 202 | cpu-small | 10 | 34% |
| 3 | sn96 Verathos | 71.2 | 44.65 | 530 | rtx4090 | 37 | 42% |
| 4 | sn67 Harnyx | 70.3 | 14.02 | 812 | cpu-small | 147 | 21% |
| 5 | sn91 cascade | 70.1 | 760 | 2,580 | rtx4090* | 5 | 50% |
| 6 | sn41 Almanac | 69 | 10.56 | 23.76 | cpu-small | 68 | 73% |
| 7 | sn62 Ridges | 68.9 | 540 | 1,953 | rtx4090* | 7 | 35% |
| 8 | sn15 ORO | 68 | 10.96 | 23.11 | cpu-small | 87 | 92% |
| 9 | sn26 Perturb | 67.9 | 19.87 | 175 | rtx3060 | 11 | 50% |
| 10 | sn21 AdTAO | 67.4 | 7.20 | 32.46 | cpu-small | 88 | 48% |
| 11 | sn85 Vidaio | 66.7 | 276 | 498 | rtx4090* | 10 | 16% |
| 12 | sn100 BASE | 66.7 | 276 | 1,978 | rtx4090* | 5 | 50% |
| 13 | sn56 Gradients | 66.7 | 275 | 994 | rtx4090* | 8 | 72% |
| 14 | sn124 Swarm | 65.8 | 220 | 667 | rtx4090* | 23 | 11% |
| 15 | sn80 OpenRoboto | 64.8 | 156 | 565 | rtx4090* | 4 | 91% |
| 16 | sn38 ChronoLLM | 64.7 | 164 | 3,569 | rtx4090* | 10 | 52% |
| 17 | sn61 RedTeam | 62.7 | 82.78 | 346 | rtx4090* | 46 | 7% |
| 18 | sn28 gm | 62.6 | 81.47 | 2,887 | rtx4090* | 27 | 30% |
| 19 | sn51 lium.io | 59.9 | 43.21 | 3,126 | rtx4090* | 52 | 63% |
| 20 | sn6 Numinous | 57.7 | 21.63 | 476 | cpu-small | 19 | 26% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 16 |
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
| 2026-08-11T13:53 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-08-11T13:53 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: optimise validator competition dataset pr |
| 2026-08-11T12:08 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: merge: daily model intake, multi-miner ex |
| 2026-08-11T12:08 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #38 from conjectures-i |
| 2026-08-11T09:11 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: isolate competition batches in separate m |
| 2026-08-11T09:11 | sn96 | RELEASE | sn96 released Verathos v0.1.35 — Concurrent Proof Serving |
| 2026-08-11T09:11 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: recover shared-checkout miner update |
| 2026-08-11T07:58 | sn61 | RELEASE | sn61 released 4.9.6 |
| 2026-08-11T07:58 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |
| 2026-08-11T04:36 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: validator: record the decided challenger' |
| 2026-08-11T02:55 | sn61 | RELEASE | sn61 released 4.9.5 |
| 2026-08-11T02:55 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: refactor: update bot virus challenge envi |
| 2026-08-11T00:40 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: merge: the canonical miner script and th |
| 2026-08-11T00:40 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-08-10T23:47 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: DEC-CA-0012: Cascade warm-start promotion |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

