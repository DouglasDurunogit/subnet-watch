# Subnet watch — dashboard

_snapshot 2026-09-17T22:19:51Z · block 9090321 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.1 | 5,857 | 5,857 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 77.8 | 92.06 | 312 | cpu-small | 8 | 39% |
| 3 | sn4 Targon | 77.5 | 6,958 | 19,537 | rtx4090* | 6 | 51% |
| 4 | sn91 cascade | 72.6 | 627 | 2,512 | cpu-small | 5 | 52% |
| 5 | sn67 Harnyx | 68.6 | 8.29 | 801 | cpu-small | 143 | 28% |
| 6 | sn107 Minos | 68.4 | 311 | 26,786 | cpu-small | 20 | 80% |
| 7 | sn111 Claims | 68.2 | 445 | 1,973 | rtx4090* | 5 | 60% |
| 8 | sn56 Gradients | 68 | 404 | 4,900 | rtx4090* | 10 | 46% |
| 9 | sn124 Swarm | 66.3 | 255 | 825 | rtx4090* | 25 | 11% |
| 10 | sn38 ChronoLLM | 65.5 | 88.15 | 781 | cpu-small | 10 | 52% |
| 11 | sn3 Teutonic | 63.8 | 4,124 | 4,124 = | rtx4090* | 5 | 20% |
| 12 | sn28 SayGM | 63.5 | 106 | 1,006 | rtx4090* | 60 | 9% |
| 13 | sn62 Ridges | 62.2 | 71.96 | 1,465 | rtx4090* | 20 | 22% |
| 14 | sn55 NIOME | 61.8 | 64.31 | 536 | rtx4090* | 11 | 29% |
| 15 | sn81 Reliquary | 60.8 | 47.28 | 98.75 | rtx4090* | 35 | 51% |
| 16 | sn23 Trishool | 60.6 | 609 | 609 = | cpu-small | 2 | 80% |
| 17 | sn15 ORO | 59.2 | 2.18 | 4.52 | cpu-small | 21 | 100% |
| 18 | sn51 lium.io | 58.9 | 34.65 | 1,685 | rtx4090* | 66 | 82% |
| 19 | sn61 RedTeam | 58.7 | 25.99 | 2,209 | rtx4090* | 118 | 21% |
| 20 | sn102 ConnitoAI | 57 | 16.14 | 1,715 | rtx4090* | 8 | 38% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 19 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-17T22:20 | sn4 | RELEASE | sn4 released v2.0.1 |
| 2026-09-17T22:20 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): delete orphaned retry_que |
| 2026-09-17T22:20 | sn25 | RELEASE | sn25 released v2026.9.17-1048832810 |
| 2026-09-17T22:20 | sn69 | SCORING_COMMIT | sn69 commit touches scoring: Re-submit the latest miner weights on a b |
| 2026-09-17T22:20 | sn74 | RELEASE | sn74 released release-20260917-220301 |
| 2026-09-17T22:20 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: feat(validator): raise minimum node spec  |
| 2026-09-17T22:20 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: docs: replace CLAUDE.md with AGENTS.md +  |
| 2026-09-17T22:20 | sn102 | RELEASE | sn102 released v0.6.2 |
| 2026-09-17T22:20 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 🐛 fix(validator): drop evaluations that  |
| 2026-09-17T19:19 | sn25 | RELEASE | sn25 released v2026.9.17-1048676710 |
| 2026-09-17T19:19 | sn74 | RELEASE | sn74 released release-20260917-174533 |
| 2026-09-17T19:19 | sn74 | README_TASK_DIFF | sn74 README task/scoring sections changed |
| 2026-09-17T15:41 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix: refresh campaign fees before payment |
| 2026-09-17T15:41 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Update autoupdate_validator_steps.sh to e |
| 2026-09-17T15:41 | sn56 | README_TASK_DIFF | sn56 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

