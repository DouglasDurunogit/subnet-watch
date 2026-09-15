# Subnet watch — dashboard

_snapshot 2026-09-15T06:07:40Z · block 9071146 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 37 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.9 | 199 | 600 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 74.2 | 1,008 | 2,689 | cpu-small | 5 | 52% |
| 3 | sn1 Apex | 70 | 746 | 915 | rtx4090* | 4 | 56% |
| 4 | sn96 Verathos | 69.1 | 26.76 | 236 | rtx4090 | 72 | 31% |
| 5 | sn107 Minos | 69 | 360 | 30,584 | cpu-small | 20 | 80% |
| 6 | sn67 Harnyx | 68.7 | 9.35 | 962 | cpu-small | 114 | 32% |
| 7 | sn11 TrajectoryRL | 68.1 | 5,717 | 5,717 = | cpu-small | 1 | 100% |
| 8 | sn38 ChronoLLM | 68 | 170 | 3,608 | cpu-small | 10 | 52% |
| 9 | sn80 OpenRoboto | 67.6 | 366 | 1,301 | rtx4090* | 5 | 43% |
| 10 | sn124 Swarm | 66.4 | 264 | 856 | rtx4090* | 25 | 11% |
| 11 | sn111 Claims | 65.3 | 197 | 2,729 | rtx4090* | 5 | 78% |
| 12 | sn28 SayGM | 63.9 | 122 | 1,816 | rtx4090* | 47 | 12% |
| 13 | sn3 Teutonic | 63.8 | 4,085 | 4,085 = | rtx4090* | 5 | 20% |
| 14 | sn61 RedTeam | 63.6 | 114 | 174 | rtx4090* | 94 | 2% |
| 15 | sn81 Reliquary | 62.8 | 85.97 | 328 | rtx4090* | 44 | 8% |
| 16 | sn55 NIOME | 62 | 67.91 | 563 | rtx4090* | 11 | 29% |
| 17 | sn23 Trishool | 60.2 | 534 | 534 = | cpu-small | 2 | 80% |
| 18 | sn62 Ridges | 60.2 | 38.89 | 1,151 | rtx4090* | 18 | 35% |
| 19 | sn74 Gittensor | 59.2 | 31.77 | 186 | rtx4090 | 9 | 64% |
| 20 | sn51 lium.io | 58.6 | 32.39 | 1,682 | rtx4090* | 63 | 83% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 16 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-15T06:08 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.793 - miners can earn again |
| 2026-09-15T06:08 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve declared homepage encodings duri |
| 2026-09-15T06:08 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs(protocol): production runs one opera |
| 2026-09-15T06:08 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #97 from Umi-BitSign/c |
| 2026-09-15T06:08 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: fix: burn the full allocation when no mi |
| 2026-09-15T00:51 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh reviewed scorer workflow protecti |
| 2026-09-15T00:51 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #267 from reliquadotai |
| 2026-09-14T22:27 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: add PublicEvaluationRun model |
| 2026-09-14T22:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected source for verified par |
| 2026-09-14T22:27 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs(miner): credential path leads INSTAL |
| 2026-09-14T22:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Publish runtime-independent validator hos |
| 2026-09-14T22:27 | sn111 | RELEASE | sn111 released v0.2.0 |
| 2026-09-14T18:48 | sn1 | RELEASE | sn1 released v4.4.6 |
| 2026-09-14T18:48 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: scoring: the settle schedule is 10 / 17 / |
| 2026-09-14T18:48 | sn25 | RELEASE | sn25 released v2026.9.14-1046068620 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

