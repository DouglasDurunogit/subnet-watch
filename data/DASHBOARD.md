# Subnet watch — dashboard

_snapshot 2026-09-26T06:06:49Z · block 9150022 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 72.8 | 659 | 2,641 | cpu-small | 5 | 52% |
| 2 | sn1 Apex | 71.5 | 1,153 | 1,180 | rtx4090* | 4 | 52% |
| 3 | sn56 Gradients | 71 | 995 | 5,716 | rtx4090* | 8 | 41% |
| 4 | sn102 ConnitoAI | 69.8 | 708 | 2,326 | rtx4090* | 6 | 41% |
| 5 | sn38 ChronoLLM | 69.7 | 278 | 2,447 | cpu-small | 10 | 52% |
| 6 | sn67 Harnyx | 69.3 | 10.04 | 1,296 | cpu-small | 116 | 37% |
| 7 | sn15 ORO | 69.2 | 13.46 | 21,426 | cpu-small | 62 | 96% |
| 8 | sn107 Minos | 69.1 | 370 | 30,047 | cpu-small | 20 | 80% |
| 9 | sn4 Targon | 68.4 | 15,846 | 28,661 | rtx4090* | 5 | 58% |
| 10 | sn14 Cacheon | 68.3 | 452 | 2,291 | rtx4090* | 13 | 28% |
| 11 | sn96 Verathos | 67.4 | 18.34 | 265 | rtx4090 | 74 | 30% |
| 12 | sn124 Swarm | 67.1 | 328 | 948 | rtx4090* | 25 | 11% |
| 13 | sn111 Claims | 66.5 | 275 | 3,033 | rtx4090* | 5 | 74% |
| 14 | sn3 Teutonic | 64.8 | 5,435 | 5,435 = | rtx4090* | 5 | 20% |
| 15 | sn62 Ridges | 62.6 | 81.89 | 1,510 | rtx4090* | 23 | 16% |
| 16 | sn23 Trishool | 62.3 | 999 | 999 = | cpu-small | 2 | 80% |
| 17 | sn28 SayGM | 61.8 | 66.22 | 957 | rtx4090* | 73 | 22% |
| 18 | sn26 Perturb | 61.4 | 58.20 | 58.20 = | rtx3060 | 5 | 90% |
| 19 | sn100 Cortex | 60 | 36.92 | 251 | rtx4090* | 19 | 70% |
| 20 | sn74 Gittensor | 58.9 | 30.15 | 285 | rtx4090* | 17 | 62% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 21 |
| captured (>90%) | 24 |

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
| 2026-09-26T06:07 | sn62 | RELEASE | sn62 released v0.3.7 |
| 2026-09-26T06:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow focused validation of saved Arena o |
| 2026-09-25T22:43 | sn1 | RELEASE | sn1 released v4.4.10 |
| 2026-09-25T19:26 | sn15 | RELEASE | sn15 released v2.0.31: fix(proxy): re-resolve Backend host for allowli |
| 2026-09-25T19:26 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: refactor(validator): simplify session cal |
| 2026-09-25T19:26 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve terminal verified intent evidenc |
| 2026-09-25T19:26 | sn74 | RELEASE | sn74 released release-20260925-183535 |
| 2026-09-25T19:26 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: test(network): verify opentype 75/25 sea |
| 2026-09-25T15:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: competition: clarify staging finalization |
| 2026-09-25T15:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3467 - [P2] validator: inspect after  |
| 2026-09-25T15:24 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Withhold a miner's source while it is on  |
| 2026-09-25T15:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified activity repair to committe |
| 2026-09-25T15:24 | sn102 | RELEASE | sn102 released v0.6.4 — the reference miner trains the full model |
| 2026-09-25T15:24 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #283 from Connito-AI/ |
| 2026-09-25T15:24 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs(miner): update V1 consensus review  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

