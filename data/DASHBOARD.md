# Subnet watch — dashboard

_snapshot 2026-11-13T15:34:38Z · block 9498361 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 17 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 82.2 | 278 | 278 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 74.2 | 2,597 | 2,597 = | rtx4090* | 10 | 10% |
| 3 | sn3 Teutonic | 74 | 2,441 | 4,890 | rtx4090* | 4 | 40% |
| 4 | sn97 Ingot | 72.1 | 1,371 | 1,371 = | rtx4090* | 5 | 20% |
| 5 | sn34 Yugos | 70 | 738 | 6,339 | rtx4090* | 3 | 85% |
| 6 | sn41 Almanac | 69.5 | 11.90 | 144 | cpu-small | 159 | 2% |
| 7 | sn58 Attune | 69.2 | 590 | 950 | rtx4090* | 5 | 70% |
| 8 | sn67 Harnyx | 68.4 | 7.67 | 131 | cpu-small | 133 | 8% |
| 9 | sn56 Gradients | 67.8 | 390 | 4,799 | rtx4090* | 6 | 55% |
| 10 | sn124 Swarm | 65.6 | 210 | 877 | rtx4090* | 10 | 31% |
| 11 | sn15 ORO | 65.4 | 6.21 | 10,424 | cpu-small | 77 | 95% |
| 12 | sn53 engy | 65.2 | 174 | 5,434 | rtx4090 | 23 | 40% |
| 13 | sn38 ChronoLLM | 63.5 | 52.54 | 362 | cpu-small | 9 | 52% |
| 14 | sn121 sundae_bar | 61.7 | 835 | 835 = | cpu-small | 2 | 60% |
| 15 | sn62 Ridges | 60.8 | 46.56 | 671 | rtx4090* | 44 | 15% |
| 16 | sn111 Claims | 60.7 | 46.51 | 183 | rtx4090* | 4 | 88% |
| 17 | sn60 Bitsec.ai | 59.3 | 406 | 625 | cpu-small | 3 | 50% |
| 18 | sn4 Targon | 58.3 | 11,274 | 21,328 | rtx4090* | 5 | 60% |
| 19 | sn102 ConnitoAI | 57.1 | 545 | 545 | rtx4090* | 4 | 25% |
| 20 | sn66 conjectures | 56.9 | 14.02 | 1,078 | rtx4090* | 7 | 80% |

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
| dominated (60–90%) | 29 |
| captured (>90%) | 25 |

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
| 2026-11-13T15:34 | sn69 | SCORING_COMMIT | sn69 commit touches scoring: Port the validator to bittensor 11.3.2 |
| 2026-11-13T15:34 | sn69 | README_TASK_DIFF | sn69 README task/scoring sections changed |
| 2026-11-13T15:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record deployed Arena migration access an |
| 2026-11-13T15:34 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: docs(design): Terminal-Bench 2.1 gold che |
| 2026-11-13T15:34 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Document Silver data in evaluation expor |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

