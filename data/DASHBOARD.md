# Subnet watch — dashboard

_snapshot 2026-11-09T02:52:04Z · block 9465748 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 6 | `██` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,731 | 2,731 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.8 | 1,708 | 3,425 | rtx4090* | 7 | 25% |
| 3 | sn56 Gradients | 70.6 | 880 | 4,766 | rtx4090* | 5 | 52% |
| 4 | sn41 Almanac | 70.4 | 14.84 | 162 | cpu-small | 170 | 2% |
| 5 | sn1 Apex | 69.7 | 681 | 737 | rtx4090* | 4 | 54% |
| 6 | sn58 Attune | 69 | 549 | 883 | rtx4090* | 5 | 70% |
| 7 | sn36 Weir | 68.9 | 540 | 605 | rtx4090* | 8 | 24% |
| 8 | sn46 Instant | 67.8 | 149 | 177 | cpu-small | 9 | 46% |
| 9 | sn103 Terza Inference | 67.5 | 351 | 639 | rtx4090* | 5 | 38% |
| 10 | sn15 ORO | 66.8 | 6.87 | 14.00 | cpu-small | 75 | 95% |
| 11 | sn82 Noah | 66.5 | 312 | 399 | rtx4090* | 65 | 2% |
| 12 | sn67 Harnyx | 65.3 | 3.50 | 294 | cpu-small | 121 | 17% |
| 13 | sn38 ChronoLLM | 62.5 | 42.12 | 377 | cpu-small | 10 | 52% |
| 14 | sn66 conjectures | 61 | 50.51 | 139 | rtx4090* | 5 | 80% |
| 15 | sn55 NIOME | 60.7 | 45.91 | 398 | rtx4090* | 11 | 30% |
| 16 | sn97 Ingot | 60.3 | 1,444 | 1,444 = | rtx4090* | 4 | 40% |
| 17 | sn117 everyframe.studi | 58.6 | 24.66 | 283 | rtx4090* | 27 | 45% |
| 18 | sn28 SayGM | 58.5 | 26.55 | 2,284 | rtx4090* | 112 | 19% |
| 19 | sn111 Claims | 58.5 | 23.82 | 2,394 | rtx4090* | 6 | 90% |
| 20 | sn102 ConnitoAI | 58 | 723 | 724 | rtx4090* | 4 | 25% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 23 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-09T02:52 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Remove grader versions from prepared task |
| 2026-11-09T02:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1136 from leadpoet/fi |
| 2026-11-09T02:52 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Door chain reader: an uncollected SDK se |
| 2026-11-08T23:11 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: feat(validator): report each episode's en |
| 2026-11-08T23:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1132 from leadpoet/fi |
| 2026-11-08T19:38 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify full recovery function security on |
| 2026-11-08T19:38 | sn76 | BURN_DROP | sn76 burn fell 0.996 -> 0.985 - miners can earn again |
| 2026-11-08T19:38 | sn90 | RELEASE | sn90 released v1.4.2 |
| 2026-11-08T19:38 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(subnet): consolidate miner node onbo |
| 2026-11-08T19:38 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-11-08T15:05 | sn11 | RELEASE | sn11 released v0.7.8 |
| 2026-11-08T15:05 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Burn all SN11 miner emission to owner UID |
| 2026-11-08T08:01 | sn17 | RELEASE | sn17 released witness-gateway-fence-poll-20261108 |
| 2026-11-08T08:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify delegated admission deferral in re |
| 2026-11-08T01:42 | sn17 | RELEASE | sn17 released witness-gateway-disconnect-20261108 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

