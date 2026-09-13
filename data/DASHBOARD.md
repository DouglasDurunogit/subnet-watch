# Subnet watch — dashboard

_snapshot 2026-09-13T21:24:31Z · block 9061360 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.6 | 186 | 560 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 71.1 | 1,029 | 2,758 | rtx4090* | 5 | 52% |
| 3 | sn21 AdTAO | 71 | 17.35 | 108 | cpu-small | 21 | 34% |
| 4 | sn67 Harnyx | 69.5 | 11.02 | 1,208 | cpu-small | 111 | 38% |
| 5 | sn107 Minos | 69 | 359 | 30,391 | cpu-small | 20 | 80% |
| 6 | sn96 Verathos | 68.7 | 24.09 | 217 | rtx4090 | 80 | 33% |
| 7 | sn11 TrajectoryRL | 68.2 | 5,848 | 5,848 = | cpu-small | 1 | 100% |
| 8 | sn80 OpenRoboto | 67.8 | 383 | 1,362 | rtx4090* | 5 | 43% |
| 9 | sn38 ChronoLLM | 66.8 | 124 | 1,693 | cpu-small | 10 | 52% |
| 10 | sn124 Swarm | 66.5 | 267 | 867 | rtx4090* | 25 | 11% |
| 11 | sn61 RedTeam | 64.6 | 152 | 235 | rtx4090* | 83 | 2% |
| 12 | sn111 Claims | 64.5 | 160 | 2,868 | rtx4090* | 5 | 82% |
| 13 | sn55 NIOME | 62 | 67.20 | 558 | rtx4090* | 11 | 29% |
| 14 | sn78 Umi | 60 | 37.51 | 37.51 = | rtx4090* | 117 | 1% |
| 15 | sn62 Ridges | 59.7 | 33.24 | 110 | rtx4090* | 16 | 51% |
| 16 | sn81 Reliquary | 59.1 | 28.17 | 212 | rtx4090* | 86 | 5% |
| 17 | sn102 ConnitoAI | 59 | 979 | 1,472 | rtx4090* | 6 | 30% |
| 18 | sn51 lium.io | 58 | 28.69 | 2,354 | rtx4090* | 62 | 78% |
| 19 | sn14 Cacheon | 56.8 | 503 | 1,141 | rtx4090* | 12 | 18% |
| 20 | sn74 Gittensor | 56.6 | 15.77 | 183 | rtx4090 | 11 | 64% |

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
| dominated (60–90%) | 17 |
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
| 2026-09-13T21:25 | sn15 | RELEASE | sn15 released v2.0.10: Capture complete episode resource telemetry (#2 |
| 2026-09-13T21:25 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Use SDK transient status classification f |
| 2026-09-13T21:25 | sn47 | BURN_DROP | sn47 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-13T21:25 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #65 from Umi-BitSign/c |
| 2026-09-13T21:25 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(validator): explain V1 selection ver |
| 2026-09-13T21:25 | sn99 | BURN_DROP | sn99 burn fell 1.000 -> 0.150 - miners can earn again |
| 2026-09-13T19:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind stage two recovery to tested scorer  |
| 2026-09-13T19:00 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #64 from Umi-BitSign/c |
| 2026-09-13T19:00 | sn125 | BURN_DROP | sn125 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-13T16:33 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #61 from Umi-BitSign/c |
| 2026-09-13T12:20 | sn15 | RELEASE | sn15 released v2.0.9 |
| 2026-09-13T12:20 | sn61 | RELEASE | sn61 released 4.10.5 |
| 2026-09-13T12:20 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update ada_detection challenge imag |
| 2026-09-13T12:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind recovered Arena future stages to the |
| 2026-09-13T12:20 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Accept the verified stopped successor dur |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

