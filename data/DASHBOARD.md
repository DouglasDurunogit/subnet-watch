# Subnet watch — dashboard

_snapshot 2026-09-24T23:51:26Z · block 9140945 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 76.5 | 5,238 | 5,238 = | rtx4090* | 5 | 20% |
| 2 | sn91 cascade | 72.8 | 668 | 2,675 | cpu-small | 5 | 52% |
| 3 | sn102 ConnitoAI | 72.1 | 1,368 | 1,369 | rtx4090* | 4 | 25% |
| 4 | sn26 Perturb | 71.2 | 45.42 | 49.74 | rtx3060 | 5 | 90% |
| 5 | sn1 Apex | 69.8 | 699 | 1,152 | rtx4090* | 4 | 59% |
| 6 | sn107 Minos | 68.8 | 344 | 28,969 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.7 | 8.83 | 1,166 | cpu-small | 126 | 35% |
| 8 | sn38 ChronoLLM | 68.5 | 203 | 1,786 | cpu-small | 10 | 52% |
| 9 | sn56 Gradients | 68.4 | 456 | 5,583 | rtx4090* | 10 | 40% |
| 10 | sn4 Targon | 68.2 | 15,197 | 27,488 | rtx4090* | 5 | 58% |
| 11 | sn14 Cacheon | 67.6 | 365 | 2,460 | rtx4090* | 12 | 32% |
| 12 | sn15 ORO | 67.6 | 9.44 | 21.19 | cpu-small | 57 | 97% |
| 13 | sn124 Swarm | 67 | 314 | 909 | rtx4090* | 25 | 11% |
| 14 | sn111 Claims | 65.9 | 238 | 3,037 | rtx4090* | 5 | 77% |
| 15 | sn100 Cortex | 62.9 | 87.31 | 183 | rtx4090* | 13 | 70% |
| 16 | sn28 SayGM | 62.6 | 83.32 | 901 | rtx4090* | 62 | 28% |
| 17 | sn23 Trishool | 62 | 922 | 922 = | cpu-small | 2 | 80% |
| 18 | sn62 Ridges | 61.4 | 56.82 | 1,887 | rtx4090* | 20 | 21% |
| 19 | sn51 lium.io | 60 | 48.27 | 2,164 | rtx4090* | 73 | 76% |
| 20 | sn61 RedTeam | 59.9 | 37.44 | 383 | rtx4090* | 126 | 4% |

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
| dominated (60–90%) | 20 |
| captured (>90%) | 27 |

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
| 2026-09-24T20:48 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: chore(release): bind verifier cache and s |
| 2026-09-24T20:48 | sn88 | README_TASK_DIFF | sn88 README task/scoring sections changed |
| 2026-09-24T20:48 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(challenges): load docker challenges |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

