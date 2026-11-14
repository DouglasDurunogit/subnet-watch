# Subnet watch — dashboard

_snapshot 2026-11-14T01:51:42Z · block 9501446 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 82.2 | 277 | 277 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 74.2 | 2,620 | 2,620 = | rtx4090* | 10 | 10% |
| 3 | sn3 Teutonic | 74 | 2,492 | 2,492 = | rtx4090* | 4 | 40% |
| 4 | sn97 Ingot | 72.1 | 1,391 | 1,391 = | rtx4090* | 5 | 20% |
| 5 | sn34 Yugos | 70.1 | 762 | 6,449 | rtx4090* | 3 | 85% |
| 6 | sn58 Attune | 69.2 | 595 | 957 | rtx4090* | 5 | 70% |
| 7 | sn56 Gradients | 69.2 | 586 | 4,463 | rtx4090* | 6 | 50% |
| 8 | sn41 Almanac | 68.8 | 10.04 | 145 | cpu-small | 159 | 2% |
| 9 | sn67 Harnyx | 68.5 | 7.81 | 133 | cpu-small | 135 | 8% |
| 10 | sn15 ORO | 65.8 | 6.33 | 10,583 | cpu-small | 79 | 95% |
| 11 | sn124 Swarm | 65.7 | 216 | 901 | rtx4090* | 10 | 31% |
| 12 | sn53 engy | 65.2 | 176 | 5,479 | rtx4090 | 23 | 40% |
| 13 | sn38 ChronoLLM | 63.6 | 53.31 | 367 | cpu-small | 9 | 52% |
| 14 | sn121 sundae_bar | 61.7 | 843 | 843 = | cpu-small | 2 | 60% |
| 15 | sn62 Ridges | 60.9 | 47.61 | 684 | rtx4090* | 44 | 15% |
| 16 | sn60 Bitsec.ai | 60.8 | 640 | 640 = | cpu-small | 3 | 50% |
| 17 | sn111 Claims | 60.8 | 47.55 | 187 | rtx4090* | 4 | 88% |
| 18 | sn4 Targon | 58.4 | 11,473 | 21,692 | rtx4090* | 5 | 60% |
| 19 | sn5 Hone | 57.6 | 22.20 | 47.39 | rtx4090* | 240 | 1% |
| 20 | sn102 ConnitoAI | 57 | 541 | 541 | rtx4090* | 4 | 25% |

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
| 2026-11-14T01:52 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Lengthen the new-miner ramp to 30 observat |
| 2026-11-14T01:52 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Put new regular miners on the static drawd |
| 2026-11-14T01:52 | sn42 | RELEASE | sn42 released v0.6.11 |
| 2026-11-14T01:52 | sn42 | README_TASK_DIFF | sn42 README task/scoring sections changed |
| 2026-11-14T01:52 | sn66 | RELEASE | sn66 released v2026.11.13.2 |
| 2026-11-14T01:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Expect mandatory reward history reader in |
| 2026-11-14T01:52 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Test: the in-range case rows add no scor |
| 2026-11-13T21:41 | sn25 | RELEASE | sn25 released v2026.11.13-1097983310 |
| 2026-11-13T21:41 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.1.2: re-verify reads a repub |
| 2026-11-13T21:41 | sn66 | RELEASE | sn66 released v2026.11.13 |
| 2026-11-13T21:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified research pairs when jud |
| 2026-11-13T21:41 | sn117 | RELEASE | sn117 released everycli v1.2.2 |
| 2026-11-13T15:34 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Update Horizon scoring, set 60M budgets an |
| 2026-11-13T15:34 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.607 - miners can earn again |
| 2026-11-13T15:34 | sn25 | RELEASE | sn25 released v2026.11.13-1097815580 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

