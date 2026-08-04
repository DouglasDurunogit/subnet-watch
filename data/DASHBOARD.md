# Subnet watch — dashboard

_snapshot 2026-08-04T17:00:48Z · block 8772185 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 12 | `██████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.6 | 501 | 501 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 78.1 | 8,391 | 8,391 = | rtx4090* | 4 | 25% |
| 3 | sn107 Minos | 77.7 | 101 | 28,021 | cpu-small | 20 | 90% |
| 4 | sn76 Phylax | 77.2 | 76.64 | 154 | cpu-small | 7 | 67% |
| 5 | sn60 Bitsec.ai | 76.5 | 1,985 | 1,985 = | cpu-small | 2 | 90% |
| 6 | sn67 Harnyx | 71.8 | 20.63 | 697 | cpu-small | 155 | 17% |
| 7 | sn62 Ridges | 69.6 | 657 | 2,373 | rtx4090* | 7 | 39% |
| 8 | sn26 Perturb | 68.6 | 23.18 | 189 | rtx3060 | 11 | 50% |
| 9 | sn56 Gradients | 67.2 | 323 | 940 | rtx4090* | 7 | 71% |
| 10 | sn15 ORO | 66.9 | 8.01 | 17.67 | cpu-small | 73 | 94% |
| 11 | sn124 Swarm | 66.1 | 239 | 595 | rtx4090* | 22 | 10% |
| 12 | sn74 Gittensor | 65.7 | 204 | 307 | rtx4090* | 8 | 18% |
| 13 | sn38 ChronoLLM | 65.4 | 199 | 3,352 | rtx4090* | 10 | 52% |
| 14 | sn41 Almanac | 65.4 | 4.60 | 66.53 | cpu-small | 36 | 89% |
| 15 | sn21 AdTAO | 65.2 | 4.39 | 20.54 | cpu-small | 142 | 45% |
| 16 | sn53 engy | 64.2 | 129 | 3,015 | rtx4090 | 28 | 17% |
| 17 | sn80 OpenRoboto | 62.3 | 74.86 | 283 | rtx4090* | 4 | 91% |
| 18 | sn28 gm | 59.1 | 29.65 | 1,700 | rtx4090* | 18 | 60% |
| 19 | sn61 RedTeam | 58.5 | 23.27 | 80.10 | rtx4090* | 93 | 3% |
| 20 | sn51 lium.io | 56.9 | 20.92 | 2,840 | rtx4090* | 39 | 78% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 23 |
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
| 2026-08-04T17:01 | sn62 | RELEASE | sn62 released v0.2.4 |
| 2026-08-04T17:01 | sn120 | BURN_DROP | sn120 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-04T12:25 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.968 - miners can earn again |
| 2026-08-04T12:25 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Improve agent validation and source grou |
| 2026-08-04T12:25 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Improve validation and sandbox dispatch  |
| 2026-08-04T12:25 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Ensure validators adopt the 70 percent b |
| 2026-08-04T12:25 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |
| 2026-08-04T10:09 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #11 from conjectures-i |
| 2026-08-04T10:09 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: closers 10% of total miner incentive (was |
| 2026-08-04T07:17 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2546, gate 8x flagship unrented incen |
| 2026-08-04T07:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind scoring artifacts to exact commitmen |
| 2026-08-04T07:17 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: fix the validator task resolution |
| 2026-08-04T07:17 | sn104 | README_TASK_DIFF | sn104 README task/scoring sections changed |
| 2026-08-04T04:26 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #10 from conjectures-i |
| 2026-08-04T04:26 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

