# Subnet watch — dashboard

_snapshot 2026-10-12T19:46:33Z · block 9269315 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 18 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 26 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.1 | 290 | 24,604 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.9 | 3,243 | 8,661 | rtx4090* | 5 | 40% |
| 3 | sn53 engy | 71.5 | 1,171 | 2,581 | rtx4090 | 18 | 17% |
| 4 | sn101 Tag101 | 70.1 | 12.75 | 13.83 | cpu-small | 248 | 0% |
| 5 | sn14 Cacheon | 70 | 738 | 5,975 | rtx4090* | 3 | 83% |
| 6 | sn67 Harnyx | 69.2 | 9.82 | 969 | cpu-small | 119 | 32% |
| 7 | sn38 ChronoLLM | 68.7 | 208 | 949 | cpu-small | 9 | 52% |
| 8 | sn41 Almanac | 68.6 | 10.15 | 176 | cpu-small | 107 | 3% |
| 9 | sn79 MVTRX | 67 | 7.72 | 35.78 | cpu-small | 249 | 1% |
| 10 | sn4 Targon | 66.9 | 10,195 | 30,059 | rtx4090* | 5 | 70% |
| 11 | sn15 ORO | 64.5 | 5.45 | 11.60 | cpu-small | 58 | 98% |
| 12 | sn62 Ridges | 64.1 | 127 | 1,370 | rtx4090* | 36 | 17% |
| 13 | sn120 Affine | 62.8 | 138 | 236 | rtx4090* | 252 | 1% |
| 14 | sn28 SayGM | 61 | 52.72 | 1,371 | rtx4090* | 73 | 16% |
| 15 | sn80 OpenRoboto | 60.1 | 1,350 | 3,777 | rtx4090* | 10 | 36% |
| 16 | sn23 Trishool | 59.2 | 402 | 402 = | cpu-small | 3 | 80% |
| 17 | sn1 Apex | 57.9 | 694 | 1,075 | rtx4090* | 4 | 57% |
| 18 | sn5 Hone | 57.9 | 35.70 | 36.19 | rtx4090* | 243 | 0% |
| 19 | sn111 Claims | 57.9 | 20.42 | 236 | rtx4090* | 7 | 90% |
| 20 | sn26 Perturb | 57.8 | 673 | 1,265 | rtx3060 | 4 | 60% |

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
| dominated (60–90%) | 29 |
| captured (>90%) | 22 |

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
| 2026-10-12T19:47 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Optimize evaluator shard downloads with ca |
| 2026-10-12T19:47 | sn9 | RELEASE | sn9 released v4.13.6 |
| 2026-10-12T19:47 | sn12 | MECHANISM_ADDED | sn12 now runs 2 incentive mechanisms (was 1) |
| 2026-10-12T19:47 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Retain audit diagnostics and post bundle  |
| 2026-10-12T19:47 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): the validator site sends  |
| 2026-10-12T19:47 | sn28 | RELEASE | sn28 released v0.4.27 |
| 2026-10-12T19:47 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.27 ( |
| 2026-10-12T19:47 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-10-12T19:47 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to the latest vers |
| 2026-10-12T19:47 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4001 - validator: report each live we |
| 2026-10-12T19:47 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #52 from hanlinai/fix/ |
| 2026-10-12T19:47 | sn58 | BURN_DROP | sn58 burn fell 1.000 -> 0.833 - miners can earn again |
| 2026-10-12T19:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Apply existing provider failure classific |
| 2026-10-12T19:47 | sn116 | RELEASE | sn116 released producer-code-r8.4 |
| 2026-10-12T19:47 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Record OWNER-BATTERY-CHAMPIONSHIP-04: mi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

