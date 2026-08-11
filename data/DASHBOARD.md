# Subnet watch — dashboard

_snapshot 2026-08-11T00:39:37Z · block 8817677 · run_status **ok**_

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
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 108 | 32,387 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.7 | 67.77 | 204 | cpu-small | 10 | 33% |
| 3 | sn67 Harnyx | 71.3 | 17.20 | 746 | cpu-small | 129 | 19% |
| 4 | sn96 Verathos | 70.3 | 36.11 | 302 | rtx4090 | 47 | 41% |
| 5 | sn41 Almanac | 69.3 | 11.11 | 33.67 | cpu-small | 69 | 69% |
| 6 | sn91 cascade | 69.2 | 582 | 1,315 | rtx4090* | 5 | 50% |
| 7 | sn62 Ridges | 68.9 | 534 | 1,933 | rtx4090* | 7 | 35% |
| 8 | sn15 ORO | 68 | 10.09 | 20.58 | cpu-small | 81 | 93% |
| 9 | sn26 Perturb | 67.9 | 19.93 | 173 | rtx3060 | 11 | 50% |
| 10 | sn21 AdTAO | 66.1 | 5.42 | 25.51 | cpu-small | 118 | 45% |
| 11 | sn124 Swarm | 65.7 | 212 | 651 | rtx4090* | 23 | 11% |
| 12 | sn38 ChronoLLM | 64.7 | 164 | 3,552 | rtx4090* | 10 | 52% |
| 13 | sn80 OpenRoboto | 64.7 | 150 | 545 | rtx4090* | 4 | 91% |
| 14 | sn100 BASE | 64.4 | 140 | 1,775 | rtx4090* | 7 | 50% |
| 15 | sn28 gm | 62.8 | 86.87 | 4,721 | rtx4090* | 26 | 46% |
| 16 | sn61 RedTeam | 62.5 | 77.79 | 326 | rtx4090* | 47 | 7% |
| 17 | sn102 ConnitoAI | 59.7 | 1,182 | 1,395 | rtx4090* | 6 | 26% |
| 18 | sn51 lium.io | 59.3 | 37.33 | 2,385 | rtx4090* | 50 | 67% |
| 19 | sn2 DSperse | 59 | 26.62 | 118 | rtx4090* | 11 | 83% |
| 20 | sn6 Numinous | 57.8 | 22.09 | 484 | cpu-small | 19 | 27% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 23 |
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
| 2026-08-10T15:13 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #36 from conjectures-i |
| 2026-08-10T15:13 | sn107 | README_TASK_DIFF | sn107 README task/scoring sections changed |
| 2026-08-10T13:54 | sn51 | RELEASE | sn51 released executor-v1.116 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

