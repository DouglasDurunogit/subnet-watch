# Subnet watch — dashboard

_snapshot 2026-07-30T04:17:51Z · block 8732392 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.4 | 620 | 620 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 81 | 201 | 295 | cpu-small | 4 | 65% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,752 | 1,752 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 71.3 | 17.34 | 1,076 | cpu-small | 94 | 23% |
| 5 | sn102 ConnitoAI | 70.4 | 826 | 1,081 | rtx4090* | 5 | 29% |
| 6 | sn56 Gradients | 69.1 | 571 | 1,339 | rtx4090* | 6 | 63% |
| 7 | sn101 Tag101 | 69 | 9.51 | 29.86 | cpu-small | 239 | 1% |
| 8 | sn15 ORO | 68.4 | 11.11 | 20.21 | cpu-small | 77 | 93% |
| 9 | sn124 Swarm | 66.6 | 278 | 859 | rtx4090* | 13 | 30% |
| 10 | sn53 engy | 62.8 | 85.41 | 1,975 | rtx4090 | 34 | 13% |
| 11 | sn71 Leadpoet | 62 | 68.34 | 119 | rtx4090* | 4 | 91% |
| 12 | sn61 RedTeam | 58.2 | 21.29 | 133 | rtx4090* | 87 | 5% |
| 13 | sn28 gm | 58.1 | 21.89 | 2,341 | rtx4090* | 10 | 62% |
| 14 | sn26 Perturb | 55.6 | 1.50 | 5.78 | rtx3060 | 51 | 50% |
| 15 | sn51 lium.io | 54 | 11.65 | 2,849 | rtx4090* | 40 | 68% |
| 16 | sn9 iota | 53.9 | 5,016 | 9,638 | rtx4090* | 3 | 50% |
| 17 | sn6 Numinous | 50 | -0.93 | 301 | cpu-small | 214 | 17% |
| 18 | sn11 TrajectoryRL | 49.9 | 5,114 | 5,114 = | cpu-small | 1 | 100% |
| 19 | sn120 Affine | 47.5 | 6,361 | 6,361 = | rtx4090* | 5 | 20% |
| 20 | sn85 Vidaio | 47.4 | 313 | 489 | rtx4090* | 10 | 16% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-30T04:18 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-07-29T22:43 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(agent-challenge): make Terminal-Benc |
| 2026-07-29T22:43 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Add tests for agent v1 Silver scoring |
| 2026-07-29T19:39 | sn6 | README_TASK_DIFF | sn6 README task/scoring sections changed |
| 2026-07-29T19:39 | sn7 | RELEASE | sn7 released release-20260729-181714 |
| 2026-07-29T19:39 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Add BURN_RATE with pools scaled to the min |
| 2026-07-29T19:39 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Introduce tiered solver task pool |
| 2026-07-29T19:39 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-07-29T19:39 | sn74 | RELEASE | sn74 released release-20260729-181654 |
| 2026-07-29T19:39 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(agent-challenge): supply LLM_MODEL t |
| 2026-07-29T19:39 | sn103 | RELEASE | sn103 released v2006: validator: start signer balance gauge at the unk |
| 2026-07-29T19:39 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: start signer balance gauge at |
| 2026-07-29T16:38 | sn9 | RELEASE | sn9 released v4.9.1 |
| 2026-07-29T16:38 | sn15 | RELEASE | sn15 released v1.2.2 |
| 2026-07-29T16:38 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #30 from hanlinai/docs |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

