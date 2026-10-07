# Subnet watch — dashboard

_snapshot 2026-10-07T16:23:17Z · block 9232303 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 86.7 | 866 | 13,000 | cpu-small | 6 | 75% |
| 2 | sn41 Almanac | 73 | 28.05 | 122 | cpu-small | 137 | 2% |
| 3 | sn91 cascade | 71.2 | 407 | 1,088 | cpu-small | 5 | 52% |
| 4 | sn38 ChronoLLM | 69.9 | 291 | 1,977 | cpu-small | 9 | 52% |
| 5 | sn46 Instant | 69.1 | 221 | 274 | cpu-small | 8 | 47% |
| 6 | sn67 Harnyx | 68.8 | 9.02 | 1,011 | cpu-small | 135 | 34% |
| 7 | sn1 Apex | 68.7 | 502 | 1,033 | rtx4090* | 4 | 69% |
| 8 | sn80 OpenRoboto | 68.3 | 450 | 2,037 | rtx4090* | 8 | 25% |
| 9 | sn15 ORO | 67.3 | 8.93 | 19,708 | cpu-small | 63 | 97% |
| 10 | sn4 Targon | 67 | 10,498 | 30,945 | rtx4090* | 5 | 70% |
| 11 | sn26 Perturb | 66.2 | 239 | 399 | rtx3060 | 4 | 60% |
| 12 | sn62 Ridges | 63.8 | 117 | 1,441 | rtx4090* | 34 | 17% |
| 13 | sn120 Affine | 63.5 | 180 | 242 | rtx4090* | 223 | 1% |
| 14 | sn65 True Performance | 62.4 | 80.09 | 168 | rtx4090* | 6 | 75% |
| 15 | sn61 RedTeam | 61.9 | 67.86 | 114 | rtx4090* | 132 | 1% |
| 16 | sn14 Cacheon | 61.1 | 51.44 | 6,208 | rtx4090* | 7 | 83% |
| 17 | sn28 SayGM | 60.2 | 41.56 | 1,752 | rtx4090* | 71 | 22% |
| 18 | sn53 engy | 60 | 1,309 | 2,512 | rtx4090 | 18 | 17% |
| 19 | sn23 Trishool | 59.8 | 480 | 482 | cpu-small | 3 | 79% |
| 20 | sn74 Gittensor | 58.4 | 26.20 | 157 | rtx4090* | 21 | 50% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 27 |
| captured (>90%) | 25 |

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
| 2026-10-07T16:23 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add math, code, and text competitions with |
| 2026-10-07T16:23 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Bind configured Readers to cancellable mi |
| 2026-10-07T16:23 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.978 - miners can earn again |
| 2026-10-07T16:23 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Leak returns to the score at 30%, over a  |
| 2026-10-07T16:23 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: a customer rent rem |
| 2026-10-07T16:23 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: Document miner decision queries and stagi |
| 2026-10-07T16:23 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Assert current scoring adapter and all ju |
| 2026-10-07T16:23 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Record verified checkpoint-32 full held- |
| 2026-10-07T09:02 | sn25 | RELEASE | sn25 released v2026.10.6-1065506180 |
| 2026-10-07T09:02 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: a filler create sta |
| 2026-10-07T09:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record validator source commits in Arena  |
| 2026-10-07T09:02 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Sync public_subnet: doctor cells/hotkey/c |
| 2026-10-07T09:02 | sn76 | README_TASK_DIFF | sn76 README task/scoring sections changed |
| 2026-10-07T09:02 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Keep failed scorer health and release cha |
| 2026-10-07T09:02 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Validate frozen blacklist freshness at t |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

