# Subnet watch — dashboard

_snapshot 2026-09-18T14:26:39Z · block 9095122 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.4 | 6,356 | 6,356 = | cpu-small | 1 | 100% |
| 2 | sn4 Targon | 77.8 | 7,607 | 21,355 | rtx4090* | 6 | 51% |
| 3 | sn3 Teutonic | 76.2 | 4,752 | 4,752 = | rtx4090* | 5 | 20% |
| 4 | sn91 cascade | 72.8 | 669 | 2,677 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 71.4 | 1,135 | 1,346 | rtx4090* | 6 | 27% |
| 6 | sn67 Harnyx | 69.1 | 10.03 | 1,282 | cpu-small | 112 | 41% |
| 7 | sn107 Minos | 68.8 | 344 | 28,878 | cpu-small | 20 | 79% |
| 8 | sn56 Gradients | 68.3 | 443 | 5,363 | rtx4090* | 10 | 46% |
| 9 | sn15 ORO | 66.9 | 8.36 | 19,973 | cpu-small | 49 | 98% |
| 10 | sn124 Swarm | 66.6 | 280 | 897 | rtx4090* | 25 | 11% |
| 11 | sn38 ChronoLLM | 65.9 | 99.14 | 877 | cpu-small | 10 | 52% |
| 12 | sn111 Claims | 65 | 188 | 1,710 | rtx4090* | 5 | 48% |
| 13 | sn62 Ridges | 63.2 | 96.52 | 1,484 | rtx4090* | 21 | 21% |
| 14 | sn55 NIOME | 62.3 | 73.78 | 607 | rtx4090* | 11 | 29% |
| 15 | sn74 Gittensor | 61 | 59.00 | 248 | rtx4090* | 10 | 62% |
| 16 | sn51 lium.io | 60.3 | 49.95 | 1,471 | rtx4090* | 64 | 82% |
| 17 | sn81 Reliquary | 60.2 | 39.55 | 120 | rtx4090* | 36 | 60% |
| 18 | sn28 SayGM | 60 | 39.16 | 2,720 | rtx4090* | 62 | 18% |
| 19 | sn61 RedTeam | 58.8 | 26.89 | 2,241 | rtx4090* | 117 | 21% |
| 20 | sn80 OpenRoboto | 56.9 | 514 | 1,819 | rtx4090* | 5 | 43% |

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
| dominated (60–90%) | 17 |
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
| 2026-09-18T14:27 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add category-stratified evaluation samplin |
| 2026-09-18T14:27 | sn9 | RELEASE | sn9 released v4.13.1 |
| 2026-09-18T14:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse exact retained miner scores for Sep |
| 2026-09-18T14:27 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: Merge pull request #13 from taostatus/fe |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

