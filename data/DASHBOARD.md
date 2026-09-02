# Subnet watch — dashboard

_snapshot 2026-09-02T23:36:43Z · block 8982948 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 87 | 933 | 1,144 | cpu-small | 4 | 42% |
| 2 | sn3 Teutonic | 75.3 | 3,606 | 3,606 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 74.1 | 36.59 | 78.23 | cpu-small | 21 | 20% |
| 4 | sn23 Trishool | 71.9 | 509 | 509 = | cpu-small | 2 | 80% |
| 5 | sn102 ConnitoAI | 71.5 | 1,173 | 1,611 | rtx4090* | 5 | 30% |
| 6 | sn67 Harnyx | 71.5 | 17.82 | 1,201 | cpu-small | 131 | 35% |
| 7 | sn91 cascade | 70 | 751 | 3,029 | rtx4090* | 5 | 52% |
| 8 | sn15 ORO | 69.7 | 19.32 | 41.68 | cpu-small | 81 | 92% |
| 9 | sn96 Verathos | 68.9 | 25.48 | 165 | rtx4090 | 81 | 41% |
| 10 | sn56 Gradients | 68.8 | 520 | 1,312 | rtx4090* | 5 | 74% |
| 11 | sn111 Claims | 66.9 | 307 | 2,749 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 66.2 | 250 | 768 | rtx4090* | 25 | 11% |
| 13 | sn79 MVTRX | 65.3 | 4.92 | 393 | cpu-small | 206 | 9% |
| 14 | sn61 RedTeam | 64.6 | 149 | 217 | rtx4090* | 47 | 3% |
| 15 | sn60 Bitsec.ai | 64 | 1,640 | 1,640 = | cpu-small | 2 | 50% |
| 16 | sn121 sundae_bar | 62.7 | 1,136 | 1,136 = | cpu-small | 2 | 60% |
| 17 | sn65 True Performance | 62.4 | 85.48 | 179 | rtx4090* | 6 | 75% |
| 18 | sn55 NIOME | 62.4 | 76.37 | 626 | rtx4090* | 11 | 29% |
| 19 | sn101 Tag101 | 61.8 | 0.65 | 0.87 | cpu-small | 227 | 90% |
| 20 | sn74 Gittensor | 61.1 | 54.13 | 360 | rtx4090 | 11 | 64% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 18 |
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
| 2026-09-02T18:51 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: weights: the validator was setting them o |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

