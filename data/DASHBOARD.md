# Subnet watch — dashboard

_snapshot 2026-08-11T04:36:20Z · block 8818860 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 108 | 32,192 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 75 | 43.23 | 172 | cpu-small | 10 | 33% |
| 3 | sn67 Harnyx | 70.5 | 14.04 | 811 | cpu-small | 129 | 21% |
| 4 | sn91 cascade | 70.2 | 786 | 2,663 | rtx4090* | 5 | 50% |
| 5 | sn62 Ridges | 68.9 | 534 | 1,934 | rtx4090* | 7 | 35% |
| 6 | sn96 Verathos | 68.9 | 25.35 | 304 | rtx4090 | 56 | 41% |
| 7 | sn41 Almanac | 68.9 | 10.31 | 33.77 | cpu-small | 66 | 73% |
| 8 | sn15 ORO | 68.1 | 10.39 | 20.95 | cpu-small | 81 | 93% |
| 9 | sn26 Perturb | 67.9 | 19.98 | 173 | rtx3060 | 11 | 50% |
| 10 | sn21 AdTAO | 66.1 | 5.34 | 25.19 | cpu-small | 118 | 45% |
| 11 | sn124 Swarm | 65.6 | 208 | 653 | rtx4090* | 23 | 11% |
| 12 | sn38 ChronoLLM | 64.7 | 162 | 3,535 | rtx4090* | 10 | 52% |
| 13 | sn80 OpenRoboto | 64.7 | 153 | 557 | rtx4090* | 4 | 91% |
| 14 | sn28 gm | 64.7 | 152 | 4,194 | rtx4090* | 25 | 41% |
| 15 | sn100 BASE | 64.5 | 144 | 1,821 | rtx4090* | 7 | 50% |
| 16 | sn61 RedTeam | 62.7 | 82.05 | 336 | rtx4090* | 46 | 7% |
| 17 | sn56 Gradients | 62 | 67.75 | 983 | rtx4090* | 13 | 72% |
| 18 | sn51 lium.io | 59.8 | 42.84 | 2,999 | rtx4090* | 51 | 61% |
| 19 | sn6 Numinous | 57.8 | 21.90 | 482 | cpu-small | 19 | 26% |
| 20 | sn120 Affine | 54.8 | 7,171 | 7,171 = | rtx4090* | 5 | 20% |

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
| dominated (60–90%) | 18 |
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
| 2026-08-10T19:31 | sn100 | RELEASE | sn100 released v3.3.15 — seal epoch sync + Prism submitter WTA |
| 2026-08-10T18:24 | sn103 | BURN_DROP | sn103 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-10T17:25 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: fix validator weight-setting reliability |
| 2026-08-10T16:22 | sn2 | RELEASE | sn2 released 14.13.2 |
| 2026-08-10T16:22 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Reason v3: single-term scoring fork (wei |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

