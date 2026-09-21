# Subnet watch — dashboard

_snapshot 2026-09-21T07:15:26Z · block 9114372 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78 | 8,139 | 22,848 | rtx4090* | 6 | 53% |
| 2 | sn91 cascade | 72.8 | 659 | 2,640 | cpu-small | 5 | 52% |
| 3 | sn102 ConnitoAI | 71 | 1,008 | 1,525 | rtx4090* | 5 | 32% |
| 4 | sn107 Minos | 68.7 | 333 | 28,234 | cpu-small | 20 | 80% |
| 5 | sn56 Gradients | 68.5 | 472 | 1,959 | rtx4090* | 9 | 46% |
| 6 | sn111 Claims | 68.4 | 475 | 2,289 | rtx4090* | 5 | 62% |
| 7 | sn67 Harnyx | 68.2 | 8.28 | 1,137 | cpu-small | 134 | 36% |
| 8 | sn15 ORO | 67.5 | 8.74 | 18.15 | cpu-small | 54 | 98% |
| 9 | sn124 Swarm | 66.5 | 274 | 875 | rtx4090* | 25 | 11% |
| 10 | sn38 ChronoLLM | 66.3 | 110 | 974 | cpu-small | 10 | 52% |
| 11 | sn28 SayGM | 62.7 | 86.79 | 1,428 | rtx4090* | 60 | 9% |
| 12 | sn62 Ridges | 62.1 | 68.98 | 2,504 | rtx4090* | 19 | 30% |
| 13 | sn74 Gittensor | 62 | 70.14 | 275 | rtx4090* | 12 | 61% |
| 14 | sn51 lium.io | 61.9 | 76.34 | 2,447 | rtx4090* | 66 | 79% |
| 15 | sn81 Reliquary | 59.4 | 31.00 | 107 | rtx4090* | 23 | 82% |
| 16 | sn61 RedTeam | 58.2 | 21.52 | 838 | rtx4090* | 126 | 10% |
| 17 | sn80 OpenRoboto | 56.6 | 478 | 1,694 | rtx4090* | 5 | 43% |
| 18 | sn9 iota | 56 | 11,717 | 11,717 = | rtx4090* | 2 | 56% |
| 19 | sn98 NeverPlayAlone | 55.7 | 2,001 | 2,001 = | cpu-small | 1 | 100% |
| 20 | sn11 TrajectoryRL | 54.6 | 6,546 | 6,546 = | rtx4090* | 1 | 100% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 19 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-21T07:15 | sn11 | RELEASE | sn11 released v0.7.3 |
| 2026-09-21T07:15 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: feat(validator): report health on the hea |
| 2026-09-21T07:15 | sn51 | RELEASE | sn51 released executor-v1.132 |
| 2026-09-21T07:15 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3677 - [P2] validator scrape: disk_ty |
| 2026-09-21T07:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep single contact role ID validation si |
| 2026-09-20T23:36 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: validator: preserve client key batch stee |
| 2026-09-20T23:36 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: keep unrelated verifier guidance out |
| 2026-09-20T23:36 | sn74 | RELEASE | sn74 released release-20260920-225500 |
| 2026-09-20T21:45 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: validator: admit reviewed successor on pr |
| 2026-09-20T21:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix normal validator scoring preflight an |
| 2026-09-20T21:45 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-20T21:45 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-20T19:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected verifier manifest to commi |
| 2026-09-20T19:25 | sn78 | RELEASE | sn78 released Open competition miner bundle v1 (feed config + pinned a |
| 2026-09-20T17:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Expose public scoring validator attributi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

