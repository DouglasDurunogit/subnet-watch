# Subnet watch — dashboard

_snapshot 2026-09-11T15:15:02Z · block 9045150 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.2 | 169 | 509 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 74.2 | 37.87 | 135 | cpu-small | 21 | 37% |
| 3 | sn102 ConnitoAI | 71 | 1,004 | 1,889 | rtx4090* | 5 | 36% |
| 4 | sn67 Harnyx | 70.4 | 13.75 | 1,106 | cpu-small | 126 | 33% |
| 5 | sn91 cascade | 70.2 | 779 | 3,140 | rtx4090* | 5 | 52% |
| 6 | sn96 Verathos | 69.5 | 29.85 | 166 | rtx4090 | 74 | 30% |
| 7 | sn14 Cacheon | 69.4 | 628 | 1,164 | rtx4090* | 12 | 18% |
| 8 | sn107 Minos | 69.1 | 369 | 31,324 | cpu-small | 20 | 80% |
| 9 | sn11 TrajectoryRL | 68.4 | 6,241 | 6,241 = | cpu-small | 1 | 100% |
| 10 | sn56 Gradients | 68.1 | 419 | 5,443 | rtx4090* | 9 | 48% |
| 11 | sn80 OpenRoboto | 67.6 | 361 | 1,283 | rtx4090* | 5 | 43% |
| 12 | sn124 Swarm | 66.6 | 278 | 898 | rtx4090* | 25 | 11% |
| 13 | sn61 RedTeam | 66.6 | 269 | 406 | rtx4090* | 47 | 4% |
| 14 | sn38 ChronoLLM | 66.2 | 106 | 1,446 | cpu-small | 10 | 52% |
| 15 | sn111 Claims | 65.4 | 208 | 3,197 | rtx4090* | 5 | 80% |
| 16 | sn3 Teutonic | 63.9 | 4,198 | 4,198 = | rtx4090* | 5 | 20% |
| 17 | sn108 Prometheon | 62.7 | 83.54 | 267 | rtx4090* | 13 | 27% |
| 18 | sn55 NIOME | 62.4 | 77.68 | 635 | rtx4090* | 11 | 29% |
| 19 | sn28 SayGM | 61.8 | 65.10 | 3,020 | rtx4090* | 40 | 35% |
| 20 | sn41 Almanac | 60.5 | 40.63 | 117 | cpu-small | 82 | 3% |

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
| captured (>90%) | 19 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-11T15:15 | sn9 | RELEASE | sn9 released v4.12.18 |
| 2026-09-11T15:15 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: upload all miners submissions |
| 2026-09-11T15:15 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #90 from conjectures-i |
| 2026-09-11T15:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix normal validator startup defaults and |
| 2026-09-11T15:15 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Clarify miner keepalive requirements duri |
| 2026-09-11T15:15 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): bind keyword-only miner setu |
| 2026-09-11T15:15 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat(validator): a mirror that fell behi |
| 2026-09-11T11:40 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(ops): verify staged units against the |
| 2026-09-11T11:40 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Add scorer v1.1.0 and signed round feedba |
| 2026-09-11T11:40 | sn20 | README_TASK_DIFF | sn20 README task/scoring sections changed |
| 2026-09-11T11:40 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Resume provisional validators from comple |
| 2026-09-11T11:40 | sn51 | RELEASE | sn51 released miner-v1.004 |
| 2026-09-11T11:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3206 - [P2] miner accepts a validator |
| 2026-09-11T11:40 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-11T11:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Remove unused validator V2 release metada |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

