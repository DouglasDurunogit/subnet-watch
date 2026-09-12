# Subnet watch — dashboard

_snapshot 2026-09-12T23:26:52Z · block 9054784 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79.6 | 144 | 435 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 74.7 | 42.14 | 102 | cpu-small | 21 | 34% |
| 3 | sn91 cascade | 71.2 | 1,073 | 2,874 | rtx4090* | 5 | 52% |
| 4 | sn96 Verathos | 69.1 | 26.69 | 218 | rtx4090 | 80 | 30% |
| 5 | sn14 Cacheon | 68.7 | 495 | 1,123 | rtx4090* | 12 | 18% |
| 6 | sn67 Harnyx | 68.7 | 8.88 | 1,040 | cpu-small | 127 | 33% |
| 7 | sn107 Minos | 68.6 | 351 | 29,724 | cpu-small | 20 | 80% |
| 8 | sn11 TrajectoryRL | 68.3 | 5,991 | 5,991 = | cpu-small | 1 | 100% |
| 9 | sn80 OpenRoboto | 67.6 | 360 | 1,282 | rtx4090* | 5 | 43% |
| 10 | sn38 ChronoLLM | 66.5 | 113 | 1,550 | cpu-small | 10 | 52% |
| 11 | sn124 Swarm | 66.4 | 263 | 857 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 65.4 | 201 | 2,774 | rtx4090* | 5 | 78% |
| 13 | sn61 RedTeam | 64.8 | 159 | 245 | rtx4090* | 70 | 2% |
| 14 | sn3 Teutonic | 63.9 | 4,185 | 4,185 = | rtx4090* | 5 | 20% |
| 15 | sn28 SayGM | 62.8 | 86.98 | 3,440 | rtx4090* | 41 | 24% |
| 16 | sn78 Umi | 62.1 | 72.87 | 72.87 = | rtx4090* | 64 | 2% |
| 17 | sn55 NIOME | 62 | 67.41 | 559 | rtx4090* | 11 | 29% |
| 18 | sn62 Ridges | 59.9 | 36.22 | 3,945 | rtx4090* | 16 | 52% |
| 19 | sn51 lium.io | 58 | 28.64 | 2,145 | rtx4090* | 63 | 83% |
| 20 | sn81 Reliquary | 57.9 | 19.05 | 163 | rtx4090* | 89 | 4% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 15 |
| captured (>90%) | 21 |

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
| 2026-09-12T23:27 | sn15 | RELEASE | sn15 released v2.0.7 |
| 2026-09-12T23:27 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): pin oro-env-runtime 0.2 |
| 2026-09-12T23:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Bind historical reward batch RPCs to capt |
| 2026-09-12T23:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Point new validator installations at the  |
| 2026-09-12T21:32 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record sim-testnet validator and contract |
| 2026-09-12T21:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify participation with shared-owner Ar |
| 2026-09-12T21:32 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-12T21:32 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Document live-miner bridge activation and |
| 2026-09-12T21:32 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): qualify proof lanes and p |
| 2026-09-12T19:19 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record strict restart verification and ca |
| 2026-09-12T19:19 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add time-bounded live-miner bridge with e |
| 2026-09-12T19:19 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): bound no-reveal debt per  |
| 2026-09-12T19:19 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: tracks: guard is the one live track on mt |
| 2026-09-12T17:07 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Run calibration once a day on 200 tasks,  |
| 2026-09-12T17:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Set daily Arena admission to twenty chall |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

