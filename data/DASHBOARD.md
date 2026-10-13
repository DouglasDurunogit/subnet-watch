# Subnet watch — dashboard

_snapshot 2026-10-13T01:39:03Z · block 9271077 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

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
| 1 | sn107 Minos | 82 | 285 | 24,133 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.8 | 3,094 | 8,264 | rtx4090* | 5 | 40% |
| 3 | sn53 engy | 71.4 | 1,131 | 2,494 | rtx4090 | 18 | 17% |
| 4 | sn101 Tag101 | 70.1 | 13.08 | 14.23 | cpu-small | 242 | 1% |
| 5 | sn58 Attune | 69.4 | 621 | 831 | rtx4090* | 4 | 74% |
| 6 | sn67 Harnyx | 68.8 | 8.65 | 863 | cpu-small | 119 | 32% |
| 7 | sn41 Almanac | 67.4 | 7.71 | 173 | cpu-small | 100 | 3% |
| 8 | sn79 MVTRX | 67.3 | 7.72 | 35.45 | cpu-small | 242 | 1% |
| 9 | sn4 Targon | 66.8 | 9,749 | 28,744 | rtx4090* | 5 | 70% |
| 10 | sn15 ORO | 65.5 | 5.21 | 11.41 | cpu-small | 58 | 98% |
| 11 | sn62 Ridges | 64.2 | 130 | 1,312 | rtx4090* | 37 | 17% |
| 12 | sn120 Affine | 62.7 | 131 | 256 | rtx4090* | 252 | 1% |
| 13 | sn28 SayGM | 60.4 | 43.54 | 2,142 | rtx4090* | 73 | 39% |
| 14 | sn80 OpenRoboto | 59.3 | 1,051 | 3,580 | rtx4090* | 10 | 35% |
| 15 | sn23 Trishool | 58.9 | 370 | 370 = | cpu-small | 3 | 80% |
| 16 | sn26 Perturb | 57.7 | 667 | 1,253 | rtx3060 | 4 | 60% |
| 17 | sn111 Claims | 57.7 | 19.34 | 226 | rtx4090* | 7 | 90% |
| 18 | sn1 Apex | 57.6 | 637 | 1,005 | rtx4090* | 4 | 59% |
| 19 | sn91 cascade | 57.6 | 246 | 493 | cpu-small | 5 | 52% |
| 20 | sn5 Hone | 57.3 | 33.55 | 34.17 | rtx4090* | 242 | 0% |

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
| 2026-10-13T01:39 | sn28 | RELEASE | sn28 released v0.4.28 |
| 2026-10-13T01:39 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.28 ( |
| 2026-10-13T01:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Finish validated bounded evidence reviews |
| 2026-10-13T01:39 | sn74 | RELEASE | sn74 released release-20261012-224627 |
| 2026-10-13T01:39 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: chore(weights): burn all miner emissions  |
| 2026-10-13T01:39 | sn117 | RELEASE | sn117 released everycli v0.3.8 |
| 2026-10-12T19:47 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Optimize evaluator shard downloads with ca |
| 2026-10-12T19:47 | sn9 | RELEASE | sn9 released v4.13.6 |
| 2026-10-12T19:47 | sn12 | MECHANISM_ADDED | sn12 now runs 2 incentive mechanisms (was 1) |
| 2026-10-12T19:47 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Retain audit diagnostics and post bundle  |
| 2026-10-12T19:47 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): the validator site sends  |
| 2026-10-12T19:47 | sn28 | RELEASE | sn28 released v0.4.27 |
| 2026-10-12T19:47 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.27 ( |
| 2026-10-12T19:47 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-10-12T19:47 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to the latest vers |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

