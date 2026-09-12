# Subnet watch — dashboard

_snapshot 2026-09-12T19:19:23Z · block 9053550 · run_status **ok**_

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
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79.6 | 145 | 438 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 75.5 | 51.55 | 127 | cpu-small | 21 | 34% |
| 3 | sn91 cascade | 71.3 | 1,079 | 2,890 | rtx4090* | 5 | 52% |
| 4 | sn14 Cacheon | 69.3 | 605 | 1,120 | rtx4090* | 12 | 18% |
| 5 | sn96 Verathos | 69.3 | 28.09 | 223 | rtx4090 | 77 | 30% |
| 6 | sn107 Minos | 68.9 | 347 | 29,434 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.7 | 8.87 | 1,039 | cpu-small | 127 | 33% |
| 8 | sn11 TrajectoryRL | 68.3 | 6,012 | 6,012 = | cpu-small | 1 | 100% |
| 9 | sn80 OpenRoboto | 67.6 | 359 | 1,277 | rtx4090* | 5 | 43% |
| 10 | sn124 Swarm | 66.4 | 265 | 859 | rtx4090* | 25 | 11% |
| 11 | sn38 ChronoLLM | 65.9 | 98.39 | 1,345 | cpu-small | 10 | 52% |
| 12 | sn111 Claims | 65.6 | 215 | 2,808 | rtx4090* | 5 | 77% |
| 13 | sn61 RedTeam | 64.7 | 152 | 234 | rtx4090* | 70 | 2% |
| 14 | sn3 Teutonic | 63.8 | 4,114 | 4,114 = | rtx4090* | 5 | 20% |
| 15 | sn28 SayGM | 62 | 69.72 | 3,057 | rtx4090* | 40 | 22% |
| 16 | sn55 NIOME | 61.8 | 62.98 | 704 | rtx4090* | 10 | 37% |
| 17 | sn62 Ridges | 59.9 | 36.00 | 3,925 | rtx4090* | 16 | 52% |
| 18 | sn74 Gittensor | 57.3 | 18.82 | 325 | rtx4090 | 12 | 64% |
| 19 | sn81 Reliquary | 56.9 | 14.18 | 169 | rtx4090* | 88 | 4% |
| 20 | sn51 lium.io | 56.7 | 21.16 | 2,366 | rtx4090* | 62 | 80% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 16 |
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
| 2026-09-12T11:06 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Remove the OpenRouter paid-validation bud |
| 2026-09-12T11:06 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): separate reveal accountin |
| 2026-09-12T11:06 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: trainer: king rent retries lemon pods and |
| 2026-09-12T11:06 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: fees: a per submission commitment fee; mt |
| 2026-09-12T06:24 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.742 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

