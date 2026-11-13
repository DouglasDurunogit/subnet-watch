# Subnet watch — dashboard

_snapshot 2026-11-13T21:40:32Z · block 9500190 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 82.2 | 278 | 278 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 74.2 | 2,623 | 2,623 = | rtx4090* | 10 | 10% |
| 3 | sn3 Teutonic | 74.1 | 2,497 | 2,497 = | rtx4090* | 4 | 40% |
| 4 | sn97 Ingot | 72.1 | 1,391 | 1,391 = | rtx4090* | 5 | 20% |
| 5 | sn34 Yugos | 70 | 753 | 6,459 | rtx4090* | 3 | 85% |
| 6 | sn41 Almanac | 69.3 | 11.27 | 144 | cpu-small | 159 | 2% |
| 7 | sn58 Attune | 69.2 | 596 | 958 | rtx4090* | 5 | 70% |
| 8 | sn56 Gradients | 69.2 | 585 | 4,472 | rtx4090* | 6 | 50% |
| 9 | sn67 Harnyx | 68.4 | 7.81 | 133 | cpu-small | 134 | 8% |
| 10 | sn15 ORO | 66.4 | 6.34 | 10,610 | cpu-small | 77 | 95% |
| 11 | sn124 Swarm | 65.7 | 215 | 897 | rtx4090* | 10 | 31% |
| 12 | sn53 engy | 65.3 | 183 | 5,678 | rtx4090 | 23 | 40% |
| 13 | sn38 ChronoLLM | 63.5 | 53.10 | 365 | cpu-small | 9 | 52% |
| 14 | sn121 sundae_bar | 61.7 | 849 | 849 = | cpu-small | 2 | 60% |
| 15 | sn60 Bitsec.ai | 60.8 | 637 | 637 = | cpu-small | 3 | 50% |
| 16 | sn111 Claims | 60.8 | 47.56 | 187 | rtx4090* | 4 | 88% |
| 17 | sn62 Ridges | 60.8 | 47.53 | 683 | rtx4090* | 44 | 15% |
| 18 | sn4 Targon | 58.4 | 11,472 | 21,692 | rtx4090* | 5 | 60% |
| 19 | sn102 ConnitoAI | 57.1 | 554 | 554 | rtx4090* | 4 | 25% |
| 20 | sn66 conjectures | 57 | 14.30 | 1,092 | rtx4090* | 7 | 80% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 29 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-13T21:41 | sn25 | RELEASE | sn25 released v2026.11.13-1097983310 |
| 2026-11-13T21:41 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.1.2: re-verify reads a repub |
| 2026-11-13T21:41 | sn66 | RELEASE | sn66 released v2026.11.13 |
| 2026-11-13T21:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified research pairs when jud |
| 2026-11-13T21:41 | sn117 | RELEASE | sn117 released everycli v1.2.2 |
| 2026-11-13T15:34 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Update Horizon scoring, set 60M budgets an |
| 2026-11-13T15:34 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.607 - miners can earn again |
| 2026-11-13T15:34 | sn25 | RELEASE | sn25 released v2026.11.13-1097815580 |
| 2026-11-13T15:34 | sn42 | RELEASE | sn42 released v0.6.9 |
| 2026-11-13T15:34 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: v0.6.8: the operator can take a client jo |
| 2026-11-13T15:34 | sn42 | README_TASK_DIFF | sn42 README task/scoring sections changed |
| 2026-11-13T15:34 | sn51 | RELEASE | sn51 released executor-v1.182 |
| 2026-11-13T15:34 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6381 - [P1] Validator: an ownership s |
| 2026-11-13T15:34 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Add next image families and native-loss e |
| 2026-11-13T15:34 | sn58 | README_TASK_DIFF | sn58 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

