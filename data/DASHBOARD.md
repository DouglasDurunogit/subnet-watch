# Subnet watch — dashboard

_snapshot 2026-07-29T20:39:02Z · block 8730098 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.3 | 602 | 602 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 80.5 | 181 | 337 | cpu-small | 4 | 61% |
| 3 | sn98 NeverPlayAlone | 76 | 1,705 | 1,705 = | cpu-small | 1 | 100% |
| 4 | sn102 ConnitoAI | 70.9 | 959 | 1,277 | rtx4090* | 4 | 35% |
| 5 | sn56 Gradients | 69.1 | 560 | 1,344 | rtx4090* | 6 | 62% |
| 6 | sn67 Harnyx | 68.6 | 8.28 | 970 | cpu-small | 116 | 21% |
| 7 | sn15 ORO | 68.5 | 10.81 | 11,212 | cpu-small | 77 | 93% |
| 8 | sn101 Tag101 | 67.5 | 6.21 | 47.42 | cpu-small | 242 | 2% |
| 9 | sn124 Swarm | 67 | 311 | 807 | rtx4090* | 13 | 24% |
| 10 | sn28 gm | 64.3 | 135 | 2,455 | rtx4090* | 8 | 57% |
| 11 | sn85 Vidaio | 63.7 | 113 | 480 | rtx4090* | 10 | 16% |
| 12 | sn53 engy | 62.9 | 89.25 | 2,056 | rtx4090 | 34 | 13% |
| 13 | sn71 Leadpoet | 62.3 | 73.18 | 128 | rtx4090* | 4 | 90% |
| 14 | sn61 RedTeam | 58.1 | 20.40 | 128 | rtx4090* | 87 | 5% |
| 15 | sn51 lium.io | 54.7 | 13.21 | 3,174 | rtx4090* | 39 | 67% |
| 16 | sn9 iota | 53.9 | 4,860 | 9,257 | rtx4090* | 3 | 49% |
| 17 | sn6 Numinous | 50 | -0.94 | 244 | cpu-small | 215 | 15% |
| 18 | sn120 Affine | 47.4 | 6,202 | 6,202 = | rtx4090* | 5 | 20% |
| 19 | sn4 Targon | 46.5 | 4,756 | 9,903 | rtx4090* | 8 | 31% |
| 20 | sn60 Bitsec.ai | 44.7 | 1,083 | 1,083 = | cpu-small | 2 | 51% |

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
| dominated (60–90%) | 18 |
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
| 2026-07-29T16:38 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Raise validator action compute budget |
| 2026-07-29T15:00 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Add universal template support for miners |
| 2026-07-29T15:00 | sn23 | README_TASK_DIFF | sn23 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

