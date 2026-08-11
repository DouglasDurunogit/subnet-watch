# Subnet watch — dashboard

_snapshot 2026-08-11T12:08:10Z · block 8821120 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
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
| 1 | sn107 Minos | 78 | 111 | 32,326 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.9 | 70.44 | 212 | cpu-small | 10 | 34% |
| 3 | sn96 Verathos | 71 | 42.67 | 613 | rtx4090 | 33 | 45% |
| 4 | sn67 Harnyx | 70.4 | 13.96 | 808 | cpu-small | 143 | 21% |
| 5 | sn91 cascade | 70.1 | 755 | 2,564 | rtx4090* | 5 | 50% |
| 6 | sn41 Almanac | 69 | 10.57 | 27.94 | cpu-small | 67 | 73% |
| 7 | sn62 Ridges | 68.9 | 538 | 1,946 | rtx4090* | 7 | 35% |
| 8 | sn15 ORO | 68.2 | 10.70 | 22.19 | cpu-small | 86 | 92% |
| 9 | sn26 Perturb | 67.8 | 19.39 | 174 | rtx3060 | 11 | 50% |
| 10 | sn100 BASE | 66.9 | 293 | 2,100 | rtx4090* | 5 | 50% |
| 11 | sn56 Gradients | 66.7 | 274 | 990 | rtx4090* | 8 | 72% |
| 12 | sn21 AdTAO | 66.5 | 5.88 | 27.41 | cpu-small | 118 | 45% |
| 13 | sn124 Swarm | 65.7 | 217 | 658 | rtx4090* | 23 | 11% |
| 14 | sn80 OpenRoboto | 64.8 | 157 | 570 | rtx4090* | 4 | 91% |
| 15 | sn38 ChronoLLM | 64.7 | 163 | 3,552 | rtx4090* | 10 | 52% |
| 16 | sn85 Vidaio | 63.9 | 118 | 496 | rtx4090* | 10 | 16% |
| 17 | sn61 RedTeam | 62.4 | 76.95 | 321 | rtx4090* | 46 | 7% |
| 18 | sn28 gm | 61.7 | 62.50 | 2,683 | rtx4090* | 26 | 27% |
| 19 | sn51 lium.io | 59.6 | 40.81 | 2,853 | rtx4090* | 52 | 64% |
| 20 | sn6 Numinous | 57.7 | 21.48 | 473 | cpu-small | 19 | 26% |

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
| dominated (60–90%) | 17 |
| captured (>90%) | 25 |

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
| 2026-08-10T22:55 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Block tournament advancement when a group |
| 2026-08-10T20:26 | sn2 | RELEASE | sn2 released 14.13.3 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

