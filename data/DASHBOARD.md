# Subnet watch — dashboard

_snapshot 2026-09-03T01:31:00Z · block 8983520 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.2 | 217 | 729 | cpu-small | 9 | 27% |
| 2 | sn3 Teutonic | 75.3 | 3,597 | 3,597 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 73.8 | 33.48 | 180 | cpu-small | 21 | 21% |
| 4 | sn23 Trishool | 71.9 | 510 | 510 = | cpu-small | 2 | 80% |
| 5 | sn67 Harnyx | 71.5 | 17.88 | 1,206 | cpu-small | 131 | 35% |
| 6 | sn91 cascade | 70.1 | 758 | 3,055 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.1 | 19.64 | 42.34 | cpu-small | 81 | 92% |
| 8 | sn102 ConnitoAI | 70 | 751 | 2,117 | rtx4090* | 6 | 39% |
| 9 | sn56 Gradients | 68.8 | 521 | 1,313 | rtx4090* | 5 | 74% |
| 10 | sn96 Verathos | 68.6 | 23.40 | 175 | rtx4090 | 82 | 41% |
| 11 | sn11 TrajectoryRL | 67.7 | 5,026 | 5,026 = | cpu-small | 1 | 100% |
| 12 | sn111 Claims | 66.9 | 307 | 2,754 | rtx4090* | 5 | 70% |
| 13 | sn124 Swarm | 66.2 | 251 | 772 | rtx4090* | 25 | 11% |
| 14 | sn79 MVTRX | 65.8 | 5.10 | 394 | cpu-small | 205 | 9% |
| 15 | sn61 RedTeam | 64.6 | 149 | 218 | rtx4090* | 47 | 3% |
| 16 | sn98 NeverPlayAlone | 64.3 | 1,841 | 1,841 = | cpu-small | 1 | 100% |
| 17 | sn60 Bitsec.ai | 64 | 1,640 | 1,640 = | cpu-small | 2 | 50% |
| 18 | sn121 sundae_bar | 62.7 | 1,139 | 1,139 = | cpu-small | 2 | 60% |
| 19 | sn65 True Performance | 62.5 | 86.96 | 182 | rtx4090* | 6 | 75% |
| 20 | sn55 NIOME | 62.4 | 76.62 | 628 | rtx4090* | 11 | 29% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 21 |
| captured (>90%) | 24 |

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
| 2026-09-02T18:51 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind automatic SOURCE_ADD reward workflow |
| 2026-09-02T18:51 | sn74 | RELEASE | sn74 released release-20260902-172331 |
| 2026-09-02T18:51 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: serving: compose miner takes host ports a |
| 2026-09-02T18:51 | sn74 | README_TASK_DIFF | sn74 README task/scoring sections changed |
| 2026-09-02T18:51 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

