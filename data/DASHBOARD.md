# Subnet watch — dashboard

_snapshot 2026-09-02T15:21:03Z · block 8980471 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 34 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 75.3 | 3,617 | 3,617 = | rtx4090* | 5 | 20% |
| 2 | sn76 Phylax | 74.4 | 39.30 | 82.97 | cpu-small | 21 | 20% |
| 3 | sn23 Trishool | 72 | 518 | 518 = | cpu-small | 2 | 80% |
| 4 | sn67 Harnyx | 71.4 | 18.03 | 1,215 | cpu-small | 131 | 35% |
| 5 | sn15 ORO | 69.9 | 19.36 | 20,682 | cpu-small | 80 | 92% |
| 6 | sn92 MicroTensor | 69.8 | 12.93 | 1,656 | cpu-small | 9 | 60% |
| 7 | sn91 cascade | 69 | 554 | 2,992 | rtx4090* | 5 | 52% |
| 8 | sn102 ConnitoAI | 68.9 | 532 | 1,781 | rtx4090* | 7 | 33% |
| 9 | sn56 Gradients | 68.8 | 523 | 1,319 | rtx4090* | 5 | 74% |
| 10 | sn96 Verathos | 68.7 | 24.45 | 142 | rtx4090 | 84 | 40% |
| 11 | sn11 TrajectoryRL | 67.7 | 4,951 | 4,951 = | cpu-small | 1 | 100% |
| 12 | sn111 Claims | 67 | 312 | 2,794 | rtx4090* | 5 | 70% |
| 13 | sn124 Swarm | 66.2 | 249 | 768 | rtx4090* | 25 | 11% |
| 14 | sn79 MVTRX | 65.8 | 5.30 | 397 | cpu-small | 203 | 9% |
| 15 | sn61 RedTeam | 64.8 | 155 | 223 | rtx4090* | 46 | 3% |
| 16 | sn121 sundae_bar | 62.8 | 1,153 | 1,153 = | cpu-small | 2 | 60% |
| 17 | sn54 Yanez | 62.7 | 4.17 | 875 | a4000 | 93 | 35% |
| 18 | sn65 True Performance | 62.3 | 82.38 | 173 | rtx4090* | 6 | 75% |
| 19 | sn101 Tag101 | 61.9 | 0.71 | 0.88 | cpu-small | 242 | 90% |
| 20 | sn21 AdTAO | 61 | 2.08 | 196 | cpu-small | 16 | 45% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 22 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 100 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-02T15:21 | sn28 | RELEASE | sn28 released v0.4.13-dev |
| 2026-09-02T15:21 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2828, feat(validator): quote path for |
| 2026-09-02T15:21 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-02T15:21 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-02T15:21 | sn102 | RELEASE | sn102 released v0.5.4 — restore validator_baseline_loss telemetry |
| 2026-09-02T15:21 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 📊 telemetry: restore validator_baseline_ |
| 2026-09-02T11:39 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Update evaluation parameters |
| 2026-09-02T11:39 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Rate-limit validator verification attempt |
| 2026-09-02T11:39 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: validator improvements + database threadi |
| 2026-09-02T11:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-02T11:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair validator supersession test driver |
| 2026-09-02T11:39 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs(validator): update bucket policy an |
| 2026-09-02T06:28 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Join miner and validator lifecycle owners |
| 2026-09-02T06:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2701: withhold incentive from executo |
| 2026-09-02T06:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Handle SOURCE_ADD chain reward quantizati |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

