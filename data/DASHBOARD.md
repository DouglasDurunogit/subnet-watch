# Subnet watch — dashboard

_snapshot 2026-07-29T07:33:54Z · block 8726172 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.6 | 66.93 | 431 | cpu-small | 4 | 68% |
| 2 | sn98 NeverPlayAlone | 76.1 | 1,742 | 1,742 = | cpu-small | 1 | 100% |
| 3 | sn56 Gradients | 69.2 | 576 | 1,439 | rtx4090* | 6 | 62% |
| 4 | sn67 Harnyx | 68.4 | 8.34 | 977 | cpu-small | 103 | 21% |
| 5 | sn15 ORO | 68.2 | 10.54 | 11,021 | cpu-small | 73 | 93% |
| 6 | sn124 Swarm | 67.4 | 348 | 708 | rtx4090* | 16 | 13% |
| 7 | sn101 Tag101 | 66.5 | 4.59 | 49.39 | cpu-small | 247 | 2% |
| 8 | sn28 gm | 65.4 | 191 | 1,531 | rtx4090* | 7 | 69% |
| 9 | sn85 Vidaio | 64.3 | 135 | 561 | rtx4090* | 10 | 18% |
| 10 | sn61 RedTeam | 58.3 | 21.93 | 152 | rtx4090* | 84 | 5% |
| 11 | sn102 ConnitoAI | 55.2 | 8.15 | 1,206 | rtx4090* | 9 | 32% |
| 12 | sn23 Trishool | 52.2 | 984 | 984 = | cpu-small | 3 | 33% |
| 13 | sn7 Allways | 50.1 | 3.19 | 1,382 | rtx4090* | 5 | 67% |
| 14 | sn120 Affine | 47.6 | 6,569 | 6,569 = | rtx4090* | 5 | 20% |
| 15 | sn4 Targon | 47.3 | 6,140 | 10,142 | rtx4090* | 8 | 31% |
| 16 | sn60 Bitsec.ai | 44.4 | 973 | 973 = | cpu-small | 2 | 51% |
| 17 | sn107 Minos | 43.2 | 114 | 33,934 | cpu-small | 20 | 90% |
| 18 | sn1 Apex | 41.4 | 1,032 | 1,787 | rtx4090* | 5 | 40% |
| 19 | sn71 Leadpoet | 39.3 | -0.10 | 296 | rtx4090* | 19 | 59% |
| 20 | sn13 Data Universe | 39.3 | -2.70 | 0.44 | rtx4090* | 236 | 69% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 20 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 107 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 3 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-29T07:34 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.317 - miners can earn again |
| 2026-07-29T07:34 | sn61 | RELEASE | sn61 released 4.8.1 |
| 2026-07-29T07:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve live validator runtime during re |
| 2026-07-29T07:34 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(agent-challenge): copy golden digest |
| 2026-07-29T04:44 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Create a writable state directory in the  |
| 2026-07-29T04:44 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(master): allowlist public FE agent-c |
| 2026-07-29T04:44 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Penalize incomplete tag submissions in m |
| 2026-07-29T01:13 | sn7 | RELEASE | sn7 released release-20260728-234943 |
| 2026-07-29T01:13 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Verify TAO transfers by settlement rather  |
| 2026-07-29T01:13 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-29T01:13 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-07-29T01:13 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(agent-challenge): remove Phala TEE  |
| 2026-07-28T22:44 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: fix(od): treat scraper ERRORS as "no evid |
| 2026-07-28T22:44 | sn46 | BURN_DROP | sn46 burn fell 1.000 -> 0.760 - miners can earn again |
| 2026-07-28T22:44 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: fix(validator): read the dynamic emission |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

