# Subnet watch — dashboard

_snapshot 2026-09-18T09:57:47Z · block 9093790 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.4 | 6,330 | 6,330 = | cpu-small | 1 | 100% |
| 2 | sn4 Targon | 77.8 | 7,582 | 21,286 | rtx4090* | 6 | 51% |
| 3 | sn91 cascade | 72.8 | 664 | 2,659 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 70.8 | 946 | 1,463 | rtx4090* | 6 | 30% |
| 5 | sn67 Harnyx | 69.2 | 9.98 | 1,276 | cpu-small | 111 | 41% |
| 6 | sn107 Minos | 68.8 | 338 | 28,336 | cpu-small | 20 | 79% |
| 7 | sn56 Gradients | 68.3 | 442 | 5,351 | rtx4090* | 10 | 46% |
| 8 | sn124 Swarm | 66.6 | 281 | 907 | rtx4090* | 25 | 11% |
| 9 | sn15 ORO | 66.2 | 7.40 | 19,592 | cpu-small | 49 | 98% |
| 10 | sn38 ChronoLLM | 65.9 | 98.79 | 874 | cpu-small | 10 | 52% |
| 11 | sn111 Claims | 64.5 | 163 | 2,920 | rtx4090* | 5 | 82% |
| 12 | sn3 Teutonic | 64.3 | 4,714 | 4,714 = | rtx4090* | 5 | 20% |
| 13 | sn62 Ridges | 62.5 | 78.79 | 1,590 | rtx4090* | 20 | 22% |
| 14 | sn28 SayGM | 62.4 | 79.08 | 962 | rtx4090* | 64 | 12% |
| 15 | sn55 NIOME | 62.2 | 71.18 | 587 | rtx4090* | 11 | 29% |
| 16 | sn74 Gittensor | 61.5 | 61.17 | 259 | rtx4090* | 10 | 62% |
| 17 | sn81 Reliquary | 60.5 | 42.69 | 116 | rtx4090* | 36 | 57% |
| 18 | sn51 lium.io | 58.9 | 35.39 | 1,696 | rtx4090* | 64 | 82% |
| 19 | sn61 RedTeam | 58.8 | 27.46 | 2,283 | rtx4090* | 117 | 21% |
| 20 | sn80 OpenRoboto | 56.8 | 503 | 1,781 | rtx4090* | 5 | 43% |

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
| dominated (60–90%) | 19 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-18T09:58 | sn25 | RELEASE | sn25 released v2026.9.17-1049083750 |
| 2026-09-18T09:58 | sn28 | RELEASE | sn28 released v0.4.19-dev |
| 2026-09-18T09:58 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): bump miner to 0.4.19 |
| 2026-09-18T09:58 | sn51 | RELEASE | sn51 released watchtower-v1.1.0 |
| 2026-09-18T09:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Seal Sep18 baseline rerun for validated p |
| 2026-09-18T05:16 | sn15 | RELEASE | sn15 released v2.0.23 |
| 2026-09-18T05:16 | sn25 | RELEASE | sn25 released v2026.9.17-1048981210 |
| 2026-09-18T05:16 | sn49 | SCORING_COMMIT | sn49 commit touches scoring: Enhance tournament reward structure to su |
| 2026-09-18T05:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified historical local releas |
| 2026-09-18T05:16 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Bind evaluation readiness to the deployed |
| 2026-09-18T05:16 | sn92 | RELEASE | sn92 released v0.4.12 |
| 2026-09-18T05:16 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: scoring: extraction F1 compares leaf fiel |
| 2026-09-18T00:36 | sn15 | RELEASE | sn15 released v2.0.22 |
| 2026-09-18T00:36 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Score partial harness failures alongside  |
| 2026-09-18T00:36 | sn25 | RELEASE | sn25 released v2026.9.17-1048903120 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

