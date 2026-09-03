# Subnet watch — dashboard

_snapshot 2026-09-03T06:32:10Z · block 8985026 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.5 | 181 | 545 | cpu-small | 9 | 26% |
| 2 | sn3 Teutonic | 75.4 | 3,658 | 3,658 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 74.2 | 37.13 | 76.95 | cpu-small | 21 | 22% |
| 4 | sn23 Trishool | 72 | 518 | 518 = | cpu-small | 2 | 80% |
| 5 | sn102 ConnitoAI | 70.4 | 826 | 1,898 | rtx4090* | 6 | 34% |
| 6 | sn91 cascade | 70.1 | 772 | 3,114 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.1 | 20.50 | 21,249 | cpu-small | 82 | 92% |
| 8 | sn96 Verathos | 69.1 | 26.62 | 162 | rtx4090 | 79 | 41% |
| 9 | sn56 Gradients | 68.9 | 530 | 1,332 | rtx4090* | 5 | 74% |
| 10 | sn67 Harnyx | 68.9 | 9.15 | 9.15 = | cpu-small | 222 | 32% |
| 11 | sn11 TrajectoryRL | 67.7 | 5,073 | 5,073 = | cpu-small | 1 | 100% |
| 12 | sn111 Claims | 67 | 318 | 2,843 | rtx4090* | 5 | 70% |
| 13 | sn124 Swarm | 66.4 | 262 | 810 | rtx4090* | 25 | 11% |
| 14 | sn79 MVTRX | 65.6 | 4.72 | 399 | cpu-small | 212 | 9% |
| 15 | sn61 RedTeam | 64.8 | 158 | 228 | rtx4090* | 46 | 3% |
| 16 | sn98 NeverPlayAlone | 64.4 | 1,848 | 1,848 = | cpu-small | 1 | 100% |
| 17 | sn60 Bitsec.ai | 63.8 | 1,576 | 1,576 = | cpu-small | 2 | 50% |
| 18 | sn121 sundae_bar | 62.8 | 1,159 | 1,159 = | cpu-small | 2 | 60% |
| 19 | sn2 DSperse | 62.6 | 80.67 | 101 | rtx4090* | 6 | 82% |
| 20 | sn65 True Performance | 62.5 | 87.54 | 183 | rtx4090* | 6 | 75% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 20 |
| captured (>90%) | 25 |

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
| 2026-09-03T06:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-03T06:32 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.974 - miners can earn again |
| 2026-09-03T06:32 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: ci: run the non-scoring tests on every pu |
| 2026-09-03T06:32 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: scoring: block-scheduled fresh-king margi |
| 2026-09-03T06:32 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-09-03T01:31 | sn105 | BURN_DROP | sn105 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-02T23:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair SOURCE_ADD provenance origin rewar |
| 2026-09-02T21:47 | sn2 | RELEASE | sn2 released 14.14.1 |
| 2026-09-02T21:47 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Resolve slow validator recovery after exte |
| 2026-09-02T21:47 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(validator): reference partner valida |
| 2026-09-02T21:47 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Revalidate topology for each release plan |
| 2026-09-02T18:51 | sn13 | RELEASE | sn13 released Release v1.18.72 |
| 2026-09-02T18:51 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: docs(miner): warn that Reddit.json needs  |
| 2026-09-02T18:51 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): absence charges require a f |
| 2026-09-02T18:51 | sn28 | RELEASE | sn28 released v0.4.14 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

