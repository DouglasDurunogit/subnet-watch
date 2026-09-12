# Subnet watch — dashboard

_snapshot 2026-09-12T21:31:56Z · block 9054211 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79.6 | 145 | 438 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 74.7 | 42.17 | 102 | cpu-small | 21 | 34% |
| 3 | sn91 cascade | 71.3 | 1,081 | 2,896 | rtx4090* | 5 | 52% |
| 4 | sn96 Verathos | 69.1 | 27.14 | 222 | rtx4090 | 80 | 30% |
| 5 | sn107 Minos | 68.9 | 347 | 29,461 | cpu-small | 20 | 80% |
| 6 | sn14 Cacheon | 68.7 | 495 | 1,123 | rtx4090* | 12 | 18% |
| 7 | sn67 Harnyx | 68.7 | 8.88 | 1,040 | cpu-small | 127 | 33% |
| 8 | sn11 TrajectoryRL | 68.3 | 6,025 | 6,025 = | cpu-small | 1 | 100% |
| 9 | sn80 OpenRoboto | 68.2 | 429 | 1,521 | rtx4090* | 5 | 51% |
| 10 | sn38 ChronoLLM | 66.5 | 114 | 1,552 | cpu-small | 10 | 52% |
| 11 | sn124 Swarm | 66.4 | 265 | 861 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 65.3 | 203 | 2,789 | rtx4090* | 5 | 78% |
| 13 | sn61 RedTeam | 64.7 | 154 | 238 | rtx4090* | 70 | 2% |
| 14 | sn3 Teutonic | 63.9 | 4,148 | 4,148 = | rtx4090* | 5 | 20% |
| 15 | sn78 Umi | 62.5 | 81.33 | 81.33 = | rtx4090* | 45 | 3% |
| 16 | sn55 NIOME | 62 | 66.94 | 555 | rtx4090* | 11 | 29% |
| 17 | sn28 SayGM | 61.7 | 63.35 | 3,311 | rtx4090* | 37 | 23% |
| 18 | sn62 Ridges | 59.9 | 36.17 | 3,941 | rtx4090* | 16 | 52% |
| 19 | sn51 lium.io | 58.7 | 33.37 | 2,272 | rtx4090* | 63 | 82% |
| 20 | sn102 ConnitoAI | 58.2 | 767 | 2,059 | rtx4090* | 5 | 42% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 15 |
| captured (>90%) | 20 |

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
| 2026-09-12T17:07 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: tracks: the hallucination detection track |
| 2026-09-12T14:06 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify original provider statuses in paid |
| 2026-09-12T14:06 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof-fc-harvest): zero-scored agent |
| 2026-09-12T11:06 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: gather responses before scoring |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

