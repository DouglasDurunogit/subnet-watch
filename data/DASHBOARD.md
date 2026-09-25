# Subnet watch — dashboard

_snapshot 2026-09-25T04:49:08Z · block 9142433 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 76.6 | 5,310 | 5,310 = | rtx4090* | 5 | 20% |
| 2 | sn91 cascade | 72.8 | 663 | 2,656 | cpu-small | 5 | 52% |
| 3 | sn26 Perturb | 71.3 | 46.62 | 56.73 | rtx3060 | 5 | 90% |
| 4 | sn1 Apex | 69.7 | 686 | 1,148 | rtx4090* | 4 | 60% |
| 5 | sn102 ConnitoAI | 69.4 | 614 | 1,789 | rtx4090* | 6 | 32% |
| 6 | sn107 Minos | 69.1 | 374 | 30,453 | cpu-small | 20 | 80% |
| 7 | sn15 ORO | 68.9 | 12.80 | 20,802 | cpu-small | 57 | 97% |
| 8 | sn67 Harnyx | 68.8 | 9.00 | 1,187 | cpu-small | 126 | 35% |
| 9 | sn38 ChronoLLM | 68.6 | 205 | 1,802 | cpu-small | 10 | 52% |
| 10 | sn56 Gradients | 68.4 | 464 | 5,678 | rtx4090* | 10 | 40% |
| 11 | sn4 Targon | 68.3 | 15,439 | 27,926 | rtx4090* | 5 | 58% |
| 12 | sn14 Cacheon | 67.6 | 360 | 2,426 | rtx4090* | 12 | 31% |
| 13 | sn124 Swarm | 67 | 319 | 923 | rtx4090* | 25 | 11% |
| 14 | sn111 Claims | 65.8 | 235 | 3,109 | rtx4090* | 5 | 77% |
| 15 | sn100 Cortex | 62.8 | 85.31 | 179 | rtx4090* | 13 | 70% |
| 16 | sn28 SayGM | 62.7 | 87.08 | 831 | rtx4090* | 63 | 28% |
| 17 | sn23 Trishool | 62.1 | 946 | 946 = | cpu-small | 2 | 80% |
| 18 | sn62 Ridges | 61.8 | 64.23 | 1,693 | rtx4090* | 21 | 19% |
| 19 | sn51 lium.io | 60.1 | 48.81 | 2,518 | rtx4090* | 74 | 75% |
| 20 | sn61 RedTeam | 60.1 | 39.24 | 390 | rtx4090* | 126 | 4% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 21 |
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
| 2026-09-24T20:48 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Retain on-chain proof of R42 validator so |
| 2026-09-24T20:48 | sn28 | RELEASE | sn28 released v0.4.23 |
| 2026-09-24T20:48 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.23 ( |
| 2026-09-24T20:48 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Score the stock anchor on a sample of aud |
| 2026-09-24T20:48 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Merge pull request #5 from Subnet46/docs/ |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

