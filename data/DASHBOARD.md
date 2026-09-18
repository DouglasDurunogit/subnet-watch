# Subnet watch — dashboard

_snapshot 2026-09-18T00:35:39Z · block 9090997 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.2 | 5,952 | 5,952 = | cpu-small | 1 | 100% |
| 2 | sn4 Targon | 77.6 | 7,069 | 19,846 | rtx4090* | 6 | 51% |
| 3 | sn92 MicroTensor | 76.1 | 60.45 | 175 | cpu-small | 8 | 39% |
| 4 | sn91 cascade | 72.7 | 635 | 2,543 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 70.8 | 941 | 1,454 | rtx4090* | 6 | 32% |
| 6 | sn107 Minos | 69.2 | 372 | 26,214 | cpu-small | 20 | 78% |
| 7 | sn67 Harnyx | 68.5 | 8.45 | 815 | cpu-small | 143 | 28% |
| 8 | sn56 Gradients | 68 | 411 | 4,980 | rtx4090* | 10 | 46% |
| 9 | sn124 Swarm | 66.4 | 264 | 853 | rtx4090* | 25 | 11% |
| 10 | sn38 ChronoLLM | 65.7 | 92.74 | 821 | cpu-small | 10 | 52% |
| 11 | sn111 Claims | 65 | 182 | 2,628 | rtx4090* | 5 | 79% |
| 12 | sn3 Teutonic | 63.9 | 4,192 | 4,192 = | rtx4090* | 5 | 20% |
| 13 | sn28 SayGM | 63 | 93.62 | 1,061 | rtx4090* | 64 | 13% |
| 14 | sn62 Ridges | 62.3 | 73.48 | 1,493 | rtx4090* | 20 | 22% |
| 15 | sn55 NIOME | 61.9 | 65.54 | 545 | rtx4090* | 11 | 29% |
| 16 | sn23 Trishool | 60.7 | 618 | 618 = | cpu-small | 2 | 80% |
| 17 | sn81 Reliquary | 60.7 | 46.04 | 101 | rtx4090* | 36 | 51% |
| 18 | sn15 ORO | 60 | 2.24 | 4.62 | cpu-small | 21 | 100% |
| 19 | sn61 RedTeam | 58.8 | 26.35 | 2,222 | rtx4090* | 118 | 21% |
| 20 | sn51 lium.io | 58.7 | 33.14 | 1,367 | rtx4090* | 67 | 82% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 21 |
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
| 2026-09-18T00:36 | sn15 | RELEASE | sn15 released v2.0.22 |
| 2026-09-18T00:36 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Score partial harness failures alongside  |
| 2026-09-18T00:36 | sn25 | RELEASE | sn25 released v2026.9.17-1048903120 |
| 2026-09-18T00:36 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #460 from BitMind-AI/f |
| 2026-09-18T00:36 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fit Sep18 evaluation schedule to measured |
| 2026-09-18T00:36 | sn74 | RELEASE | sn74 released release-20260917-234413 |
| 2026-09-18T00:36 | sn127 | BURN_DROP | sn127 burn fell 1.000 -> 0.714 - miners can earn again |
| 2026-09-17T22:20 | sn4 | RELEASE | sn4 released v2.0.1 |
| 2026-09-17T22:20 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): delete orphaned retry_que |
| 2026-09-17T22:20 | sn25 | RELEASE | sn25 released v2026.9.17-1048832810 |
| 2026-09-17T22:20 | sn69 | SCORING_COMMIT | sn69 commit touches scoring: Re-submit the latest miner weights on a b |
| 2026-09-17T22:20 | sn74 | RELEASE | sn74 released release-20260917-220301 |
| 2026-09-17T22:20 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: feat(validator): raise minimum node spec  |
| 2026-09-17T22:20 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: docs: replace CLAUDE.md with AGENTS.md +  |
| 2026-09-17T22:20 | sn102 | RELEASE | sn102 released v0.6.2 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

