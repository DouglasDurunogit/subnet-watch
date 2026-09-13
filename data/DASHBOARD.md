# Subnet watch — dashboard

_snapshot 2026-09-13T23:21:22Z · block 9061944 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

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
| 1 | sn92 MicroTensor | 80.5 | 181 | 546 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 71 | 1,014 | 2,718 | rtx4090* | 5 | 52% |
| 3 | sn21 AdTAO | 71 | 17.08 | 107 | cpu-small | 21 | 34% |
| 4 | sn67 Harnyx | 69.6 | 10.93 | 11.26 | cpu-small | 221 | 15% |
| 5 | sn96 Verathos | 69 | 26.30 | 236 | rtx4090 | 74 | 30% |
| 6 | sn107 Minos | 68.9 | 349 | 29,588 | cpu-small | 20 | 80% |
| 7 | sn11 TrajectoryRL | 68.2 | 5,735 | 5,735 = | cpu-small | 1 | 100% |
| 8 | sn80 OpenRoboto | 67.8 | 380 | 1,351 | rtx4090* | 5 | 43% |
| 9 | sn38 ChronoLLM | 66.7 | 122 | 1,661 | cpu-small | 10 | 52% |
| 10 | sn124 Swarm | 66.4 | 262 | 850 | rtx4090* | 25 | 11% |
| 11 | sn61 RedTeam | 64.6 | 150 | 230 | rtx4090* | 82 | 2% |
| 12 | sn111 Claims | 64.4 | 156 | 2,802 | rtx4090* | 5 | 82% |
| 13 | sn55 NIOME | 61.9 | 65.53 | 545 | rtx4090* | 11 | 29% |
| 14 | sn62 Ridges | 59.9 | 36.23 | 1,142 | rtx4090* | 17 | 43% |
| 15 | sn78 Umi | 59.8 | 36.45 | 36.45 = | rtx4090* | 118 | 1% |
| 16 | sn81 Reliquary | 59.1 | 27.45 | 223 | rtx4090* | 86 | 6% |
| 17 | sn102 ConnitoAI | 58.5 | 847 | 1,788 | rtx4090* | 5 | 38% |
| 18 | sn51 lium.io | 58.1 | 28.81 | 2,368 | rtx4090* | 62 | 76% |
| 19 | sn14 Cacheon | 56.7 | 493 | 1,118 | rtx4090* | 12 | 18% |
| 20 | sn74 Gittensor | 56.5 | 15.29 | 179 | rtx4090 | 11 | 64% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 18 |
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
| 2026-09-13T23:21 | sn15 | RELEASE | sn15 released v2.0.11: fix: preserve episode inference telemetry witho |
| 2026-09-13T23:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Match verified US contact state aliases |
| 2026-09-13T23:21 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Connect independent work signing and auto |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

