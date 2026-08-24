# Subnet watch — dashboard

_snapshot 2026-08-24T19:09:34Z · block 8916817 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.5 | 4,926 | 4,926 = | cpu-small | 1 | 100% |
| 2 | sn76 Phylax | 79.3 | 134 | 200 | cpu-small | 13 | 20% |
| 3 | sn60 Bitsec.ai | 76 | 1,692 | 1,692 = | cpu-small | 2 | 50% |
| 4 | sn3 Teutonic | 75.9 | 4,355 | 4,355 = | rtx4090* | 5 | 20% |
| 5 | sn102 ConnitoAI | 72.9 | 1,768 | 1,768 = | rtx4090* | 4 | 25% |
| 6 | sn38 ChronoLLM | 72.5 | 620 | 3,640 | cpu-small | 6 | 53% |
| 7 | sn62 Ridges | 72.4 | 1,506 | 3,078 | rtx4090* | 6 | 39% |
| 8 | sn15 ORO | 71.7 | 26.63 | 45.39 | cpu-small | 81 | 93% |
| 9 | sn67 Harnyx | 71.6 | 19.05 | 164 | cpu-small | 179 | 4% |
| 10 | sn91 cascade | 68.9 | 532 | 1,432 | rtx4090* | 5 | 52% |
| 11 | sn1 Apex | 68.6 | 486 | 1,295 | rtx4090* | 5 | 54% |
| 12 | sn96 Verathos | 68.6 | 24.04 | 197 | rtx4090 | 90 | 40% |
| 13 | sn26 Perturb | 67.7 | 19.09 | 272 | rtx3060 | 10 | 70% |
| 14 | sn124 Swarm | 66.7 | 291 | 2,535 | rtx4090* | 21 | 30% |
| 15 | sn21 AdTAO | 66.2 | 5.83 | 1,130 | cpu-small | 16 | 42% |
| 16 | sn107 Minos | 65.3 | 153 | 43,285 | cpu-small | 20 | 90% |
| 17 | sn98 NeverPlayAlone | 64.7 | 2,035 | 2,035 = | cpu-small | 1 | 100% |
| 18 | sn85 Vidaio | 64.7 | 151 | 430 | rtx4090* | 13 | 42% |
| 19 | sn81 Reliquary | 63.7 | 113 | 385 | rtx4090* | 35 | 10% |
| 20 | sn108 Prometheon | 63.6 | 112 | 124 | rtx4090* | 9 | 66% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-24T19:10 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-24T19:10 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF board: read the live tail, so a miner  |
| 2026-08-24T18:16 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): retire the no-zero-for-mis |
| 2026-08-24T18:16 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: Merge pull request #44 from Bitsec-AI/fea |
| 2026-08-24T18:16 | sn92 | BURN_DROP | sn92 burn fell 1.000 -> 0.971 - miners can earn again |
| 2026-08-24T17:42 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Rename the office challenge family to cf |
| 2026-08-24T17:42 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |
| 2026-08-24T16:53 | sn11 | RELEASE | sn11 released v0.6.34 |
| 2026-08-24T16:53 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): leaderboard vs chain timin |
| 2026-08-24T16:05 | sn25 | RELEASE | sn25 released v2026.8.24-1027859650 |
| 2026-08-24T15:24 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Show provisional LCB during evaluations |
| 2026-08-24T15:24 | sn7 | RELEASE | sn7 released release-20260824-151246: Bump allways to 3.3.0 (#705) |
| 2026-08-24T15:24 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(miner): match fee-path test to the si |
| 2026-08-24T14:27 | sn11 | RELEASE | sn11 released v0.6.33 |
| 2026-08-24T13:30 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Enforce miner upload size limit |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

