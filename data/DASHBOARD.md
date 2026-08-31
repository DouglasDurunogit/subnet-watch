# Subnet watch — dashboard

_snapshot 2026-08-31T06:59:49Z · block 8963566 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 36 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.8 | 5,312 | 5,312 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 78.6 | 111 | 1,092 | cpu-small | 10 | 42% |
| 3 | sn3 Teutonic | 75.5 | 3,850 | 3,850 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 75 | 45.28 | 172 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 72.8 | 24.59 | 640 | cpu-small | 118 | 18% |
| 6 | sn23 Trishool | 72.1 | 543 | 543 = | cpu-small | 2 | 80% |
| 7 | sn102 ConnitoAI | 71.3 | 1,085 | 1,813 | rtx4090* | 6 | 32% |
| 8 | sn111 Claims | 70.7 | 926 | 3,260 | rtx4090* | 3 | 70% |
| 9 | sn15 ORO | 70.1 | 18.90 | 37.10 | cpu-small | 70 | 94% |
| 10 | sn21 AdTAO | 70.1 | 13.67 | 1,173 | cpu-small | 14 | 45% |
| 11 | sn96 Verathos | 68.3 | 22.08 | 197 | rtx4090 | 78 | 41% |
| 12 | sn56 Gradients | 67.1 | 316 | 646 | rtx4090* | 7 | 71% |
| 13 | sn91 cascade | 67 | 308 | 625 | rtx4090* | 5 | 52% |
| 14 | sn124 Swarm | 66.7 | 286 | 928 | rtx4090* | 25 | 11% |
| 15 | sn61 RedTeam | 65.4 | 188 | 280 | rtx4090* | 42 | 4% |
| 16 | sn80 OpenRoboto | 64.9 | 159 | 578 | rtx4090* | 5 | 71% |
| 17 | sn79 MVTRX | 64.9 | 4.76 | 440 | cpu-small | 213 | 10% |
| 18 | sn81 Reliquary | 64.7 | 151 | 242 | rtx4090* | 32 | 5% |
| 19 | sn107 Minos | 64.5 | 125 | 37,484 | cpu-small | 20 | 90% |
| 20 | sn54 Yanez | 64.3 | 6.63 | 1,005 | a4000 | 95 | 35% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 18 |
| captured (>90%) | 27 |

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
| 2026-08-31T07:00 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: validator: multi-horizon calibration tele |
| 2026-08-31T07:00 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Score module-shaped tasks in miner simula |
| 2026-08-31T07:00 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Harden tag normalization and duplicate-s |
| 2026-08-31T07:00 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(selection): make adaptive miner sam |
| 2026-08-30T22:43 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Lock the evaluation environment to the fl |
| 2026-08-30T22:43 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(selection): expand miner pool with  |
| 2026-08-30T20:05 | sn25 | RELEASE | sn25 released v2026.8.30-1033129380 |
| 2026-08-30T17:40 | sn15 | RELEASE | sn15 released v1.2.11 |
| 2026-08-30T17:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(reporting): tenure rows state how man |
| 2026-08-30T13:20 | sn9 | RELEASE | sn9 released v4.12.10 |
| 2026-08-30T13:20 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(validator): stop implying a second v |
| 2026-08-30T13:20 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-08-30T07:32 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator-api): serve the daily feeds |
| 2026-08-30T07:32 | sn45 | README_TASK_DIFF | sn45 README task/scoring sections changed |
| 2026-08-30T07:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

