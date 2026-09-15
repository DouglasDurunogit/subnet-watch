# Subnet watch — dashboard

_snapshot 2026-09-15T11:58:18Z · block 9072892 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 37 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.7 | 192 | 578 | cpu-small | 8 | 30% |
| 2 | sn11 TrajectoryRL | 80.1 | 5,723 | 5,723 = | cpu-small | 1 | 100% |
| 3 | sn114 SOMA | 79.1 | 4,376 | 7,781 | cpu-small | 3 | 80% |
| 4 | sn91 cascade | 72.7 | 647 | 2,590 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 69.8 | 700 | 865 | rtx4090* | 4 | 57% |
| 6 | sn107 Minos | 68.7 | 334 | 28,361 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.6 | 8.98 | 927 | cpu-small | 127 | 32% |
| 8 | sn38 ChronoLLM | 68.1 | 173 | 3,670 | cpu-small | 10 | 52% |
| 9 | sn96 Verathos | 68.1 | 21.07 | 286 | rtx4090 | 81 | 31% |
| 10 | sn111 Claims | 66.9 | 314 | 1,402 | rtx4090* | 5 | 42% |
| 11 | sn124 Swarm | 66.3 | 253 | 821 | rtx4090* | 25 | 11% |
| 12 | sn3 Teutonic | 63.7 | 3,949 | 3,949 = | rtx4090* | 5 | 20% |
| 13 | sn28 SayGM | 63.7 | 114 | 2,087 | rtx4090* | 44 | 14% |
| 14 | sn61 RedTeam | 63.3 | 105 | 160 | rtx4090* | 91 | 2% |
| 15 | sn81 Reliquary | 62.5 | 77.42 | 258 | rtx4090* | 46 | 6% |
| 16 | sn55 NIOME | 61.9 | 65.67 | 546 | rtx4090* | 11 | 29% |
| 17 | sn62 Ridges | 60.4 | 42.09 | 1,111 | rtx4090* | 18 | 35% |
| 18 | sn23 Trishool | 60.1 | 517 | 517 = | cpu-small | 2 | 80% |
| 19 | sn74 Gittensor | 59 | 30.12 | 179 | rtx4090 | 9 | 64% |
| 20 | sn51 lium.io | 58.8 | 33.76 | 1,510 | rtx4090* | 63 | 81% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 29 |
| dominated (60–90%) | 15 |
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
| 2026-09-15T11:58 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat: add campaign context coverage and r |
| 2026-09-15T11:58 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Merge pull request #321 from trajectoryRL |
| 2026-09-15T11:58 | sn15 | RELEASE | sn15 released v2.0.15: chore(validator): pin runtime 1.0.6 for generat |
| 2026-09-15T11:58 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): pin runtime 1.0.6 for g |
| 2026-09-15T11:58 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Derive semantic verdicts from validated f |
| 2026-09-15T11:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2834 - [P0] validator consumes the ex |
| 2026-09-15T11:58 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-15T11:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test: prove normal scoring collision roll |
| 2026-09-15T11:58 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Stop miner HTTP service after terminal ba |
| 2026-09-15T11:58 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(roadmap): move scoring-expansion ite |
| 2026-09-15T11:58 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-09-15T11:58 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix: king rents first — challengers yield |
| 2026-09-15T06:08 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.793 - miners can earn again |
| 2026-09-15T06:08 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve declared homepage encodings duri |
| 2026-09-15T06:08 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs(protocol): production runs one opera |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

