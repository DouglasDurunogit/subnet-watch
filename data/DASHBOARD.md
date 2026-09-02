# Subnet watch — dashboard

_snapshot 2026-09-02T21:46:33Z · block 8982397 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 75.3 | 3,615 | 3,615 = | rtx4090* | 5 | 20% |
| 2 | sn76 Phylax | 74.1 | 36.76 | 78.34 | cpu-small | 21 | 20% |
| 3 | sn23 Trishool | 71.9 | 510 | 510 = | cpu-small | 2 | 80% |
| 4 | sn102 ConnitoAI | 71.6 | 1,179 | 1,621 | rtx4090* | 5 | 30% |
| 5 | sn67 Harnyx | 71.5 | 18.00 | 1,213 | cpu-small | 131 | 35% |
| 6 | sn91 cascade | 70.1 | 758 | 3,057 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 69.9 | 19.22 | 41.82 | cpu-small | 80 | 92% |
| 8 | sn92 MicroTensor | 69.8 | 12.77 | 1,636 | cpu-small | 9 | 60% |
| 9 | sn96 Verathos | 69.2 | 27.04 | 163 | rtx4090 | 77 | 41% |
| 10 | sn56 Gradients | 68.8 | 523 | 1,318 | rtx4090* | 5 | 74% |
| 11 | sn111 Claims | 66.9 | 308 | 2,756 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 66.3 | 251 | 774 | rtx4090* | 25 | 11% |
| 13 | sn79 MVTRX | 65.5 | 4.59 | 393 | cpu-small | 209 | 9% |
| 14 | sn61 RedTeam | 64.7 | 151 | 220 | rtx4090* | 47 | 3% |
| 15 | sn121 sundae_bar | 62.7 | 1,140 | 1,140 = | cpu-small | 2 | 60% |
| 16 | sn65 True Performance | 62.4 | 84.70 | 178 | rtx4090* | 6 | 75% |
| 17 | sn55 NIOME | 62.4 | 75.70 | 621 | rtx4090* | 11 | 29% |
| 18 | sn101 Tag101 | 61.9 | 0.66 | 0.88 | cpu-small | 232 | 90% |
| 19 | sn74 Gittensor | 60.3 | 43.58 | 151 | rtx4090 | 11 | 65% |
| 20 | sn2 DSperse | 59.6 | 32.55 | 39.15 | rtx4090* | 13 | 82% |

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
| 2026-09-02T18:51 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Enforce mainnet Silver validator require |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

