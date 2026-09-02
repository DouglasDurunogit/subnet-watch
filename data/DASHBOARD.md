# Subnet watch — dashboard

_snapshot 2026-09-02T18:50:48Z · block 8981519 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 75.3 | 3,642 | 3,642 = | rtx4090* | 5 | 20% |
| 2 | sn76 Phylax | 74.4 | 38.69 | 81.68 | cpu-small | 21 | 20% |
| 3 | sn23 Trishool | 72 | 520 | 520 = | cpu-small | 2 | 80% |
| 4 | sn67 Harnyx | 71.5 | 17.91 | 1,207 | cpu-small | 131 | 35% |
| 5 | sn91 cascade | 70 | 748 | 3,016 | rtx4090* | 5 | 52% |
| 6 | sn15 ORO | 69.7 | 19.39 | 42.17 | cpu-small | 80 | 92% |
| 7 | sn92 MicroTensor | 69.7 | 12.42 | 1,595 | cpu-small | 9 | 60% |
| 8 | sn96 Verathos | 68.9 | 25.39 | 144 | rtx4090 | 82 | 41% |
| 9 | sn56 Gradients | 68.8 | 524 | 1,321 | rtx4090* | 5 | 74% |
| 10 | sn102 ConnitoAI | 68.8 | 515 | 1,887 | rtx4090* | 7 | 35% |
| 11 | sn11 TrajectoryRL | 67.7 | 5,021 | 5,021 = | cpu-small | 1 | 100% |
| 12 | sn111 Claims | 67 | 315 | 2,786 | rtx4090* | 5 | 70% |
| 13 | sn124 Swarm | 66.3 | 251 | 773 | rtx4090* | 25 | 11% |
| 14 | sn79 MVTRX | 66.1 | 5.35 | 378 | cpu-small | 204 | 9% |
| 15 | sn61 RedTeam | 64.7 | 151 | 220 | rtx4090* | 47 | 3% |
| 16 | sn121 sundae_bar | 62.7 | 1,144 | 1,144 = | cpu-small | 2 | 60% |
| 17 | sn55 NIOME | 62.4 | 75.96 | 623 | rtx4090* | 11 | 29% |
| 18 | sn65 True Performance | 62.3 | 84.16 | 177 | rtx4090* | 6 | 75% |
| 19 | sn101 Tag101 | 61.8 | 0.67 | 0.88 | cpu-small | 238 | 90% |
| 20 | sn28 SayGM | 61.5 | 60.27 | 3,822 | rtx4090* | 45 | 30% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-02T18:51 | sn13 | RELEASE | sn13 released Release v1.18.72 |
| 2026-09-02T18:51 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: docs(miner): warn that Reddit.json needs  |
| 2026-09-02T18:51 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): absence charges require a f |
| 2026-09-02T18:51 | sn28 | RELEASE | sn28 released v0.4.14 |
| 2026-09-02T18:51 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind automatic SOURCE_ADD reward workflow |
| 2026-09-02T18:51 | sn74 | RELEASE | sn74 released release-20260902-172331 |
| 2026-09-02T18:51 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: serving: compose miner takes host ports a |
| 2026-09-02T18:51 | sn74 | README_TASK_DIFF | sn74 README task/scoring sections changed |
| 2026-09-02T18:51 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-02T18:51 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: weights: the validator was setting them o |
| 2026-09-02T18:51 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Enforce mainnet Silver validator require |
| 2026-09-02T15:21 | sn28 | RELEASE | sn28 released v0.4.13-dev |
| 2026-09-02T15:21 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2828, feat(validator): quote path for |
| 2026-09-02T15:21 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-02T15:21 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

