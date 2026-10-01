# Subnet watch — dashboard

_snapshot 2026-10-01T19:03:51Z · block 9189906 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 66 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **66** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.3 | 38.44 | 637 | cpu-small | 122 | 9% |
| 2 | sn23 Trishool | 74.1 | 963 | 963 = | cpu-small | 2 | 80% |
| 3 | sn102 ConnitoAI | 73 | 1,813 | 1,883 | rtx4090* | 4 | 37% |
| 4 | sn53 engy | 72.2 | 1,426 | 3,912 | rtx4090 | 14 | 22% |
| 5 | sn91 cascade | 71.4 | 432 | 1,154 | cpu-small | 5 | 52% |
| 6 | sn1 Apex | 70.7 | 910 | 1,079 | rtx4090* | 4 | 57% |
| 7 | sn46 Instant | 70.7 | 352 | 368 | cpu-small | 4 | 69% |
| 8 | sn120 Affine | 70.1 | 801 | 801 = | rtx4090* | 52 | 2% |
| 9 | sn107 Minos | 69.8 | 433 | 28,172 | cpu-small | 20 | 78% |
| 10 | sn15 ORO | 69.2 | 11.89 | 20,449 | cpu-small | 70 | 96% |
| 11 | sn56 Gradients | 68.6 | 484 | 5,267 | rtx4090* | 9 | 39% |
| 12 | sn111 Claims | 67.8 | 397 | 2,357 | rtx4090* | 6 | 60% |
| 13 | sn96 Verathos | 67.7 | 19.63 | 260 | rtx4090 | 75 | 31% |
| 14 | sn14 Cacheon | 65.8 | 213 | 2,716 | rtx4090* | 13 | 34% |
| 15 | sn4 Targon | 65.4 | 6,484 | 32,763 | rtx4090* | 5 | 71% |
| 16 | sn3 Teutonic | 64.4 | 4,897 | 4,897 = | rtx4090* | 5 | 20% |
| 17 | sn62 Ridges | 63 | 92.48 | 1,406 | rtx4090* | 25 | 15% |
| 18 | sn61 RedTeam | 62.6 | 82.77 | 150 | rtx4090* | 116 | 2% |
| 19 | sn5 Hone | 59.5 | 39.67 | 41.94 | rtx4090* | 243 | 0% |
| 20 | sn81 Reliquary | 58.9 | 26.21 | 89.04 | rtx4090* | 39 | 76% |

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
| wide (<30%) | 19 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 25 |
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
| 2026-10-01T19:04 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Clarify legacy and event scoring in the b |
| 2026-10-01T19:04 | sn22 | BURN_DROP | sn22 burn fell 1.000 -> 0.809 - miners can earn again |
| 2026-10-01T19:04 | sn46 | RELEASE | sn46 released v0.1.3 |
| 2026-10-01T19:04 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: sn46-validator update: signed, scheduled  |
| 2026-10-01T19:04 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified rebrand homepage eviden |
| 2026-10-01T19:04 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #293 from reliquadotai |
| 2026-10-01T19:04 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Validator logs explain the MIN_IMPROVEME |
| 2026-10-01T19:04 | sn117 | RELEASE | sn117 released everycli v0.2.1 |
| 2026-10-01T19:04 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: fix: explain missing miner profiles in s |
| 2026-10-01T19:04 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-01T19:04 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Record independently verified balanced c |
| 2026-10-01T13:42 | sn13 | RELEASE | sn13 released Release v1.18.73 |
| 2026-10-01T13:42 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: docs(agents): rewrite from code-verified  |
| 2026-10-01T13:42 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): take an upload before wa |
| 2026-10-01T13:42 | sn25 | RELEASE | sn25 released v2026.10.1-1060587890 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

