# Subnet watch — dashboard

_snapshot 2026-09-25T10:08:55Z · block 9144032 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 76.6 | 5,356 | 5,356 = | rtx4090* | 5 | 20% |
| 2 | sn91 cascade | 72.8 | 653 | 2,616 | cpu-small | 5 | 52% |
| 3 | sn26 Perturb | 71.3 | 46.24 | 56.56 | rtx3060 | 5 | 90% |
| 4 | sn1 Apex | 69.6 | 661 | 1,125 | rtx4090* | 4 | 61% |
| 5 | sn107 Minos | 69.1 | 371 | 30,637 | cpu-small | 20 | 80% |
| 6 | sn15 ORO | 68.7 | 12.89 | 20,943 | cpu-small | 57 | 97% |
| 7 | sn38 ChronoLLM | 68.6 | 204 | 1,797 | cpu-small | 10 | 52% |
| 8 | sn56 Gradients | 68.4 | 464 | 5,677 | rtx4090* | 10 | 40% |
| 9 | sn102 ConnitoAI | 68.4 | 462 | 1,634 | rtx4090* | 7 | 29% |
| 10 | sn4 Targon | 68.3 | 15,522 | 28,075 | rtx4090* | 5 | 58% |
| 11 | sn67 Harnyx | 68.3 | 8.03 | 1,392 | cpu-small | 113 | 41% |
| 12 | sn96 Verathos | 67.7 | 19.54 | 235 | rtx4090 | 78 | 30% |
| 13 | sn14 Cacheon | 67.6 | 359 | 2,422 | rtx4090* | 12 | 31% |
| 14 | sn124 Swarm | 67 | 318 | 920 | rtx4090* | 25 | 11% |
| 15 | sn111 Claims | 66.4 | 272 | 2,445 | rtx4090* | 5 | 61% |
| 16 | sn28 SayGM | 63.6 | 113 | 1,096 | rtx4090* | 64 | 7% |
| 17 | sn100 Cortex | 62.8 | 85.86 | 180 | rtx4090* | 13 | 70% |
| 18 | sn23 Trishool | 62.2 | 964 | 964 = | cpu-small | 2 | 80% |
| 19 | sn62 Ridges | 61.8 | 64.32 | 1,696 | rtx4090* | 21 | 19% |
| 20 | sn61 RedTeam | 60.2 | 40.46 | 391 | rtx4090* | 123 | 4% |

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
| captured (>90%) | 26 |

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
| 2026-09-25T10:09 | sn51 | RELEASE | sn51 released miner-v1.005 |
| 2026-09-25T10:09 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retain verified Greenhouse department met |
| 2026-09-25T10:09 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #315 from TensorLink-A |
| 2026-09-25T10:09 | sn96 | RELEASE | sn96 released Verathos v0.2.3 – DeepSeek Mesh Proof Compatibility |
| 2026-09-25T10:09 | sn112 | BURN_DROP | sn112 burn fell 1.000 -> 0.850 - miners can earn again |
| 2026-09-25T04:49 | sn25 | RELEASE | sn25 released v2026.9.24-1054966040 |
| 2026-09-25T04:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected verifier workflows to revi |
| 2026-09-25T04:49 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: bench_fail chat suites: option (i) + rea |
| 2026-09-24T23:51 | sn69 | SCORING_COMMIT | sn69 commit touches scoring: Merge the v2 validator into dev |
| 2026-09-24T23:51 | sn69 | README_TASK_DIFF | sn69 README task/scoring sections changed |
| 2026-09-24T23:51 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: trainer: verify harvested funded checkpoi |
| 2026-09-24T23:51 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: kingboard matrix: leak-audited SWE cells |
| 2026-09-24T20:48 | sn15 | RELEASE | sn15 released v2.0.30: fix(validator): lower default sandbox max worke |
| 2026-09-24T20:48 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): lower default sandbox max |
| 2026-09-24T20:48 | sn25 | RELEASE | sn25 released v2026.9.24-1054792560 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

