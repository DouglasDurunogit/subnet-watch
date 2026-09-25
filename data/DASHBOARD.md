# Subnet watch — dashboard

_snapshot 2026-09-25T15:24:11Z · block 9145609 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 72.7 | 642 | 2,571 | cpu-small | 5 | 52% |
| 2 | sn26 Perturb | 71.3 | 46.55 | 56.65 | rtx3060 | 5 | 90% |
| 3 | sn56 Gradients | 70.3 | 820 | 5,839 | rtx4090* | 8 | 42% |
| 4 | sn38 ChronoLLM | 69.6 | 269 | 2,369 | cpu-small | 10 | 52% |
| 5 | sn1 Apex | 69.5 | 634 | 1,098 | rtx4090* | 4 | 62% |
| 6 | sn107 Minos | 69 | 360 | 30,507 | cpu-small | 20 | 80% |
| 7 | sn14 Cacheon | 68.7 | 500 | 2,444 | rtx4090* | 13 | 31% |
| 8 | sn4 Targon | 68.3 | 15,566 | 28,155 | rtx4090* | 5 | 58% |
| 9 | sn15 ORO | 68.2 | 12.63 | 22.27 | cpu-small | 57 | 97% |
| 10 | sn67 Harnyx | 68.2 | 7.84 | 1,396 | cpu-small | 119 | 41% |
| 11 | sn124 Swarm | 67.1 | 320 | 926 | rtx4090* | 25 | 11% |
| 12 | sn96 Verathos | 66.7 | 15.63 | 261 | rtx4090 | 78 | 30% |
| 13 | sn111 Claims | 66.4 | 273 | 2,448 | rtx4090* | 5 | 61% |
| 14 | sn3 Teutonic | 64.7 | 5,321 | 5,321 = | rtx4090* | 5 | 20% |
| 15 | sn28 SayGM | 62.5 | 82.05 | 1,083 | rtx4090* | 78 | 6% |
| 16 | sn23 Trishool | 62.3 | 1,003 | 1,003 = | cpu-small | 2 | 80% |
| 17 | sn62 Ridges | 61.5 | 58.45 | 1,707 | rtx4090* | 21 | 19% |
| 18 | sn61 RedTeam | 60.4 | 42.08 | 391 | rtx4090* | 121 | 4% |
| 19 | sn100 Cortex | 59.4 | 30.97 | 203 | rtx4090* | 19 | 72% |
| 20 | sn74 Gittensor | 59.3 | 33.47 | 306 | rtx4090* | 16 | 64% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 22 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-25T15:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: competition: clarify staging finalization |
| 2026-09-25T15:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3467 - [P2] validator: inspect after  |
| 2026-09-25T15:24 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Withhold a miner's source while it is on  |
| 2026-09-25T15:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified activity repair to committe |
| 2026-09-25T15:24 | sn102 | RELEASE | sn102 released v0.6.4 — the reference miner trains the full model |
| 2026-09-25T15:24 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #283 from Connito-AI/ |
| 2026-09-25T15:24 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs(miner): update V1 consensus review  |
| 2026-09-25T15:24 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-09-25T10:09 | sn51 | RELEASE | sn51 released miner-v1.005 |
| 2026-09-25T10:09 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retain verified Greenhouse department met |
| 2026-09-25T10:09 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #315 from TensorLink-A |
| 2026-09-25T10:09 | sn96 | RELEASE | sn96 released Verathos v0.2.3 – DeepSeek Mesh Proof Compatibility |
| 2026-09-25T10:09 | sn112 | BURN_DROP | sn112 burn fell 1.000 -> 0.850 - miners can earn again |
| 2026-09-25T04:49 | sn25 | RELEASE | sn25 released v2026.9.24-1054966040 |
| 2026-09-25T04:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected verifier workflows to revi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

