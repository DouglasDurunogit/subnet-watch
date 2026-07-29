# Subnet watch — dashboard

_snapshot 2026-07-29T19:39:31Z · block 8729800 · run_status **ok**_

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
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.3 | 611 | 611 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 80.9 | 197 | 329 | cpu-small | 4 | 60% |
| 3 | sn98 NeverPlayAlone | 76 | 1,730 | 1,730 = | cpu-small | 1 | 100% |
| 4 | sn102 ConnitoAI | 70.7 | 924 | 934 | rtx4090* | 4 | 25% |
| 5 | sn56 Gradients | 69.1 | 569 | 1,368 | rtx4090* | 6 | 62% |
| 6 | sn67 Harnyx | 68.7 | 8.42 | 985 | cpu-small | 115 | 21% |
| 7 | sn15 ORO | 68.5 | 11.19 | 11,578 | cpu-small | 77 | 93% |
| 8 | sn124 Swarm | 67.5 | 359 | 730 | rtx4090* | 16 | 13% |
| 9 | sn101 Tag101 | 67.3 | 5.91 | 50.94 | cpu-small | 240 | 2% |
| 10 | sn28 gm | 66.3 | 247 | 2,636 | rtx4090* | 7 | 56% |
| 11 | sn85 Vidaio | 64.1 | 127 | 552 | rtx4090* | 10 | 20% |
| 12 | sn71 Leadpoet | 63.5 | 105 | 417 | rtx4090* | 6 | 71% |
| 13 | sn53 engy | 63 | 90.86 | 2,090 | rtx4090 | 34 | 13% |
| 14 | sn61 RedTeam | 58.2 | 20.82 | 130 | rtx4090* | 87 | 5% |
| 15 | sn9 iota | 53.9 | 4,916 | 9,367 | rtx4090* | 3 | 49% |
| 16 | sn51 lium.io | 53.6 | 10.77 | 3,075 | rtx4090* | 38 | 67% |
| 17 | sn6 Numinous | 50 | -0.94 | 247 | cpu-small | 215 | 15% |
| 18 | sn120 Affine | 47.4 | 6,289 | 6,289 = | rtx4090* | 5 | 20% |
| 19 | sn4 Targon | 46.5 | 4,817 | 10,029 | rtx4090* | 8 | 31% |
| 20 | sn60 Bitsec.ai | 44.8 | 1,103 | 1,103 = | cpu-small | 2 | 51% |

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
| dominated (60–90%) | 19 |
| captured (>90%) | 25 |

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

