# Subnet watch — dashboard

_snapshot 2026-09-09T23:25:13Z · block 9033224 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.2 | 974 | 7,801 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.7 | 426 | 33,992 | cpu-small | 20 | 79% |
| 3 | sn92 MicroTensor | 78.5 | 110 | 247 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76 | 4,406 | 4,406 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 72.1 | 1,398 | 5,746 | rtx4090* | 7 | 47% |
| 6 | sn15 ORO | 72.1 | 25.19 | 47.52 | cpu-small | 78 | 92% |
| 7 | sn67 Harnyx | 71.6 | 18.66 | 529 | cpu-small | 125 | 15% |
| 8 | sn91 cascade | 70.3 | 800 | 3,226 | rtx4090* | 5 | 52% |
| 9 | sn14 Cacheon | 69.6 | 665 | 1,232 | rtx4090* | 12 | 18% |
| 10 | sn96 Verathos | 69.5 | 29.88 | 173 | rtx4090 | 85 | 30% |
| 11 | sn11 TrajectoryRL | 68.7 | 6,659 | 6,659 = | cpu-small | 1 | 100% |
| 12 | sn62 Ridges | 67.9 | 394 | 1,241 | rtx4090* | 13 | 26% |
| 13 | sn102 ConnitoAI | 67.8 | 386 | 2,139 | rtx4090* | 7 | 37% |
| 14 | sn80 OpenRoboto | 67 | 300 | 962 | rtx4090* | 5 | 44% |
| 15 | sn124 Swarm | 66.8 | 294 | 915 | rtx4090* | 25 | 11% |
| 16 | sn61 RedTeam | 66.8 | 283 | 453 | rtx4090* | 40 | 4% |
| 17 | sn38 ChronoLLM | 66 | 102 | 1,396 | cpu-small | 10 | 52% |
| 18 | sn111 Claims | 65.4 | 205 | 2,193 | rtx4090* | 5 | 50% |
| 19 | sn121 sundae_bar | 63 | 1,232 | 1,232 = | cpu-small | 2 | 60% |
| 20 | sn108 Prometheon | 60.8 | 48.44 | 117 | rtx4090* | 11 | 33% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 16 |
| captured (>90%) | 20 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-09T23:25 | sn25 | RELEASE | sn25 released v2026.9.9-1041947070 |
| 2026-09-09T23:25 | sn28 | RELEASE | sn28 released v0.4.17 |
| 2026-09-09T23:25 | sn61 | RELEASE | sn61 released 4.10.4 |
| 2026-09-09T23:25 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #498 from ridgesai/fea |
| 2026-09-09T23:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Cover encoded miner-key echoes through pr |
| 2026-09-09T23:25 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Fix OCI archive annotation verification |
| 2026-09-09T23:25 | sn100 | RELEASE | sn100 released ctx CLI v3.3.30 |
| 2026-09-09T23:25 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(proof): continuous leaf emitter wit |
| 2026-09-09T21:17 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Document model-independent miner extensio |
| 2026-09-09T21:17 | sn20 | README_TASK_DIFF | sn20 README task/scoring sections changed |
| 2026-09-09T21:17 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Merge pull request #5 from EpagoFoundatio |
| 2026-09-09T21:17 | sn62 | RELEASE | sn62 released v0.3.2 |
| 2026-09-09T21:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-09T21:17 | sn78 | WEIGHTS_VERSION_BUMP | sn78 weights_version 1 -> 4294967296 |
| 2026-09-09T21:17 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add prerequisite-gated validator supervis |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

