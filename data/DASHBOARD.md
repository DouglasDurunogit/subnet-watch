# Subnet watch — dashboard

_snapshot 2026-10-20T05:23:46Z · block 9322601 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.3 | 2,681 | 7,163 | rtx4090* | 5 | 40% |
| 2 | sn41 Almanac | 71.3 | 18.93 | 102 | cpu-small | 125 | 24% |
| 3 | sn91 cascade | 71 | 390 | 1,562 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 69.4 | 10.43 | 262 | cpu-small | 169 | 11% |
| 5 | sn53 engy | 68.9 | 539 | 2,242 | rtx4090 | 24 | 16% |
| 6 | sn82 Noah | 68.7 | 662 | 679 | rtx4090* | 60 | 2% |
| 7 | sn1 Apex | 68.4 | 453 | 942 | rtx4090* | 5 | 56% |
| 8 | sn107 Minos | 67.6 | 256 | 21,755 | cpu-small | 20 | 80% |
| 9 | sn23 Trishool | 67.5 | 233 | 233 = | cpu-small | 4 | 80% |
| 10 | sn102 ConnitoAI | 67.2 | 321 | 1,722 | rtx4090* | 7 | 41% |
| 11 | sn15 ORO | 66.8 | 7.04 | 15,649 | cpu-small | 65 | 97% |
| 12 | sn14 Cacheon | 65 | 165 | 4,277 | rtx4090* | 11 | 63% |
| 13 | sn120 Affine | 64 | 140 | 268 | rtx4090* | 254 | 1% |
| 14 | sn66 conjectures | 63.7 | 113 | 233 | rtx4090* | 4 | 80% |
| 15 | sn55 NIOME | 62.3 | 74.25 | 611 | rtx4090* | 11 | 30% |
| 16 | sn92 REAX | 61.5 | 84.57 | 3,021 | rtx4090 | 246 | 11% |
| 17 | sn61 RedTeam | 61.5 | 61.16 | 111 | rtx4090* | 121 | 1% |
| 18 | sn97 Ingot | 61.4 | 2,002 | 2,002 = | rtx4090* | 5 | 20% |
| 19 | sn76 Ormas | 60.4 | 40.92 | 92.82 | rtx4090* | 4 | 96% |
| 20 | sn81 Reliquary | 59.7 | 33.31 | 364 | rtx4090* | 10 | 82% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 28 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-20T05:24 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: fix(miner): admit reviewed runtime481 fun |
| 2026-10-20T05:24 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-10-20T05:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #583 from leadpoet/aud |
| 2026-10-20T05:24 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): a task on Qwen3.5's text- |
| 2026-10-20T00:43 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): embed checks wait up to  |
| 2026-10-20T00:43 | sn28 | RELEASE | sn28 released v0.5.4 |
| 2026-10-20T00:43 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.4 (# |
| 2026-10-20T00:43 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Regenerate protected scorer manifest from |
| 2026-10-20T00:43 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.989 - miners can earn again |
| 2026-10-20T00:43 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.884 - miners can earn again |
| 2026-10-19T21:39 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.505 - miners can earn again |
| 2026-10-19T21:39 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix: use validator lockfile for local tes |
| 2026-10-19T21:39 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Updating default miner alpha to 3600, or  |
| 2026-10-19T21:39 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: burn 22% of miner emission (#341) |
| 2026-10-19T21:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4195 - [P2] Skip could-not-reach rows |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

