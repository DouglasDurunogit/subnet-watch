# Subnet watch — dashboard

_snapshot 2026-08-11T09:11:20Z · block 8820235 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 5 | `███` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 110 | 32,232 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 75.1 | 44.68 | 178 | cpu-small | 10 | 34% |
| 3 | sn96 Verathos | 71.8 | 51.34 | 566 | rtx4090 | 33 | 41% |
| 4 | sn67 Harnyx | 70.3 | 13.85 | 802 | cpu-small | 140 | 21% |
| 5 | sn91 cascade | 70 | 749 | 2,540 | rtx4090* | 5 | 50% |
| 6 | sn41 Almanac | 69 | 10.46 | 33.79 | cpu-small | 66 | 72% |
| 7 | sn62 Ridges | 68.9 | 534 | 1,934 | rtx4090* | 7 | 35% |
| 8 | sn100 BASE | 68.5 | 471 | 1,921 | rtx4090* | 5 | 50% |
| 9 | sn26 Perturb | 67.9 | 19.99 | 174 | rtx3060 | 11 | 50% |
| 10 | sn15 ORO | 67.9 | 10.36 | 21.51 | cpu-small | 86 | 92% |
| 11 | sn56 Gradients | 66.6 | 272 | 983 | rtx4090* | 8 | 72% |
| 12 | sn21 AdTAO | 66.1 | 5.37 | 25.28 | cpu-small | 118 | 45% |
| 13 | sn124 Swarm | 65.8 | 218 | 662 | rtx4090* | 23 | 11% |
| 14 | sn80 OpenRoboto | 64.9 | 160 | 582 | rtx4090* | 4 | 91% |
| 15 | sn85 Vidaio | 64.9 | 160 | 626 | rtx4090* | 10 | 20% |
| 16 | sn38 ChronoLLM | 64.6 | 161 | 3,522 | rtx4090* | 10 | 52% |
| 17 | sn61 RedTeam | 62.4 | 75.48 | 310 | rtx4090* | 46 | 7% |
| 18 | sn28 gm | 61.4 | 58.42 | 2,114 | rtx4090* | 27 | 31% |
| 19 | sn51 lium.io | 59.9 | 43.08 | 2,732 | rtx4090* | 52 | 63% |
| 20 | sn6 Numinous | 57.7 | 21.67 | 477 | cpu-small | 19 | 26% |

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
| concentrated (30–60%) | 24 |
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
| 2026-08-10T22:55 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Block tournament advancement when a group |
| 2026-08-10T20:26 | sn2 | RELEASE | sn2 released 14.13.3 |
| 2026-08-10T20:26 | sn100 | RELEASE | sn100 released v3.3.16 — design emit cold-start + permanent seal-sync  |
| 2026-08-10T19:31 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: add discarded questions to scoring  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

