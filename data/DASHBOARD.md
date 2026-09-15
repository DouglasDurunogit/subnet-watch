# Subnet watch — dashboard

_snapshot 2026-09-15T20:12:02Z · block 9075349 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 37 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.1 | 962 | 7,701 | cpu-small | 4 | 80% |
| 2 | sn92 MicroTensor | 80.4 | 176 | 531 | cpu-small | 8 | 30% |
| 3 | sn11 TrajectoryRL | 80 | 5,664 | 5,664 = | cpu-small | 1 | 100% |
| 4 | sn91 cascade | 72.5 | 611 | 2,447 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 69.6 | 657 | 891 | rtx4090* | 4 | 56% |
| 6 | sn107 Minos | 68.7 | 336 | 28,573 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.7 | 8.95 | 924 | cpu-small | 138 | 32% |
| 8 | sn111 Claims | 68.1 | 438 | 1,945 | rtx4090* | 5 | 60% |
| 9 | sn38 ChronoLLM | 67.8 | 163 | 3,467 | cpu-small | 10 | 52% |
| 10 | sn96 Verathos | 67.6 | 18.70 | 193 | rtx4090 | 72 | 31% |
| 11 | sn124 Swarm | 66.2 | 247 | 796 | rtx4090* | 25 | 11% |
| 12 | sn28 SayGM | 63.6 | 110 | 2,404 | rtx4090* | 47 | 17% |
| 13 | sn61 RedTeam | 62.8 | 87.96 | 131 | rtx4090* | 103 | 1% |
| 14 | sn55 NIOME | 62.5 | 79.61 | 519 | rtx4090* | 10 | 30% |
| 15 | sn81 Reliquary | 62.5 | 77.36 | 183 | rtx4090* | 44 | 10% |
| 16 | sn23 Trishool | 60.3 | 553 | 553 = | cpu-small | 2 | 80% |
| 17 | sn62 Ridges | 60.3 | 40.98 | 1,080 | rtx4090* | 18 | 35% |
| 18 | sn51 lium.io | 58.5 | 31.39 | 1,632 | rtx4090* | 64 | 82% |
| 19 | sn102 ConnitoAI | 58.2 | 774 | 1,555 | rtx4090* | 6 | 35% |
| 20 | sn14 Cacheon | 57.3 | 575 | 902 | rtx4090* | 13 | 15% |

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
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 14 |
| captured (>90%) | 22 |

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
| 2026-09-15T20:12 | sn15 | RELEASE | sn15 released v2.0.17 |
| 2026-09-15T20:12 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Fix generative callback staleness and val |
| 2026-09-15T20:12 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs: day-one fixes from the first third- |
| 2026-09-15T20:12 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #107 from Umi-BitSign/ |
| 2026-09-15T16:53 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix: harden validator API binding and ser |
| 2026-09-15T16:53 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Raise proof token limit to one million fo |
| 2026-09-15T16:53 | sn90 | RELEASE | sn90 released v1.2.0 |
| 2026-09-15T16:53 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(scoring): divide emission pool by the |
| 2026-09-15T11:58 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat: add campaign context coverage and r |
| 2026-09-15T11:58 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Merge pull request #321 from trajectoryRL |
| 2026-09-15T11:58 | sn15 | RELEASE | sn15 released v2.0.15: chore(validator): pin runtime 1.0.6 for generat |
| 2026-09-15T11:58 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): pin runtime 1.0.6 for g |
| 2026-09-15T11:58 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Derive semantic verdicts from validated f |
| 2026-09-15T11:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2834 - [P0] validator consumes the ex |
| 2026-09-15T11:58 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

