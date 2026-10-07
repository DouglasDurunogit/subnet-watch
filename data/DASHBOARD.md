# Subnet watch — dashboard

_snapshot 2026-10-07T09:02:12Z · block 9230098 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 64 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **64** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 73.4 | 31.34 | 122 | cpu-small | 133 | 2% |
| 2 | sn49 Nepher Robotics | 72.5 | 1,557 | 5,471 | rtx4090* | 4 | 69% |
| 3 | sn91 cascade | 71.2 | 411 | 1,098 | cpu-small | 5 | 52% |
| 4 | sn46 Instant | 70.6 | 346 | 354 | cpu-small | 6 | 48% |
| 5 | sn1 Apex | 68.9 | 536 | 1,090 | rtx4090* | 4 | 68% |
| 6 | sn67 Harnyx | 68.9 | 9.34 | 1,044 | cpu-small | 131 | 34% |
| 7 | sn80 OpenRoboto | 68.5 | 474 | 2,146 | rtx4090* | 8 | 25% |
| 8 | sn15 ORO | 67.7 | 9.30 | 20,430 | cpu-small | 63 | 97% |
| 9 | sn4 Targon | 67.1 | 10,815 | 31,880 | rtx4090* | 5 | 70% |
| 10 | sn26 Perturb | 66.3 | 244 | 408 | rtx3060 | 4 | 60% |
| 11 | sn120 Affine | 63.9 | 202 | 291 | rtx4090* | 210 | 1% |
| 12 | sn62 Ridges | 63.9 | 120 | 1,483 | rtx4090* | 34 | 17% |
| 13 | sn23 Trishool | 62.7 | 1,136 | 1,136 = | cpu-small | 2 | 76% |
| 14 | sn61 RedTeam | 62.5 | 81.47 | 120 | rtx4090* | 125 | 1% |
| 15 | sn65 True Performance | 62.4 | 82.04 | 172 | rtx4090* | 6 | 75% |
| 16 | sn14 Cacheon | 61.2 | 53.23 | 6,395 | rtx4090* | 7 | 83% |
| 17 | sn53 engy | 60.3 | 1,427 | 3,909 | rtx4090 | 14 | 22% |
| 18 | sn28 SayGM | 59.9 | 37.81 | 7,563 | rtx4090* | 74 | 37% |
| 19 | sn74 Gittensor | 58.3 | 25.71 | 142 | rtx4090* | 21 | 50% |
| 20 | sn5 Hone | 58.2 | 36.79 | 41.77 | rtx4090* | 245 | 0% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 26 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-07T09:02 | sn25 | RELEASE | sn25 released v2026.10.6-1065506180 |
| 2026-10-07T09:02 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: a filler create sta |
| 2026-10-07T09:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record validator source commits in Arena  |
| 2026-10-07T09:02 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Sync public_subnet: doctor cells/hotkey/c |
| 2026-10-07T09:02 | sn76 | README_TASK_DIFF | sn76 README task/scoring sections changed |
| 2026-10-07T09:02 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Keep failed scorer health and release cha |
| 2026-10-07T09:02 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Validate frozen blacklist freshness at t |
| 2026-10-07T02:19 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Merge pull request #18 from hone-subnet-or |
| 2026-10-07T02:19 | sn25 | RELEASE | sn25 released v2026.10.6-1065359600 |
| 2026-10-07T02:19 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/operator-discovery-validator |
| 2026-10-07T02:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve commercial terms sources in boun |
| 2026-10-07T02:19 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #723 from carbonphysi |
| 2026-10-07T02:19 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Prepare isolated all750 matched native e |
| 2026-10-06T23:03 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.902 - miners can earn again |
| 2026-10-06T23:03 | sn25 | RELEASE | sn25 released v2026.10.6-1065229510 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

