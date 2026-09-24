# Subnet watch — dashboard

_snapshot 2026-09-24T20:48:11Z · block 9140029 · run_status **ok**_

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
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 80.2 | 15,324 | 27,719 | rtx4090* | 5 | 58% |
| 2 | sn3 Teutonic | 76.6 | 5,266 | 5,266 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.7 | 647 | 2,589 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 72 | 1,330 | 1,595 | rtx4090* | 5 | 28% |
| 5 | sn26 Perturb | 71.2 | 45.30 | 49.62 | rtx3060 | 5 | 90% |
| 6 | sn1 Apex | 69.9 | 719 | 1,175 | rtx4090* | 4 | 58% |
| 7 | sn67 Harnyx | 68.7 | 8.92 | 1,177 | cpu-small | 126 | 35% |
| 8 | sn107 Minos | 68.6 | 328 | 29,350 | cpu-small | 20 | 80% |
| 9 | sn14 Cacheon | 68.5 | 476 | 2,441 | rtx4090* | 12 | 31% |
| 10 | sn38 ChronoLLM | 68.5 | 202 | 1,777 | cpu-small | 10 | 52% |
| 11 | sn56 Gradients | 68.4 | 460 | 5,624 | rtx4090* | 10 | 40% |
| 12 | sn15 ORO | 67.9 | 10.47 | 22.94 | cpu-small | 58 | 97% |
| 13 | sn124 Swarm | 67.1 | 323 | 934 | rtx4090* | 25 | 11% |
| 14 | sn111 Claims | 65.5 | 214 | 1,933 | rtx4090* | 5 | 49% |
| 15 | sn100 Cortex | 62.6 | 80.25 | 169 | rtx4090* | 13 | 70% |
| 16 | sn23 Trishool | 62 | 917 | 917 = | cpu-small | 2 | 80% |
| 17 | sn62 Ridges | 61.8 | 64.14 | 1,916 | rtx4090* | 20 | 21% |
| 18 | sn28 SayGM | 61.6 | 62.22 | 2,913 | rtx4090* | 80 | 16% |
| 19 | sn61 RedTeam | 59.8 | 35.71 | 373 | rtx4090* | 126 | 4% |
| 20 | sn81 Reliquary | 58.8 | 25.78 | 52.96 | rtx4090* | 29 | 84% |

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
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 18 |
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
| 2026-09-24T17:35 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Ground native semantic scoring in clip ev |
| 2026-09-24T17:35 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Derive policy rollover activations from v |
| 2026-09-24T17:35 | sn28 | RELEASE | sn28 released v0.4.22-dev |
| 2026-09-24T17:35 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.4.22-dev (#277 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

