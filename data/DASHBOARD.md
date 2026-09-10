# Subnet watch — dashboard

_snapshot 2026-09-10T01:20:01Z · block 9033797 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.1 | 971 | 7,773 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.5 | 406 | 34,495 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 78.6 | 112 | 249 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76 | 4,398 | 4,398 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 72.1 | 1,396 | 5,742 | rtx4090* | 7 | 47% |
| 6 | sn15 ORO | 71.6 | 25.53 | 48.16 | cpu-small | 78 | 92% |
| 7 | sn67 Harnyx | 71.5 | 18.54 | 526 | cpu-small | 125 | 15% |
| 8 | sn91 cascade | 70.2 | 795 | 3,204 | rtx4090* | 5 | 52% |
| 9 | sn14 Cacheon | 69.6 | 664 | 1,231 | rtx4090* | 12 | 18% |
| 10 | sn96 Verathos | 69.6 | 30.59 | 177 | rtx4090 | 85 | 30% |
| 11 | sn11 TrajectoryRL | 68.7 | 6,650 | 6,650 = | cpu-small | 1 | 100% |
| 12 | sn102 ConnitoAI | 67.8 | 388 | 2,146 | rtx4090* | 7 | 37% |
| 13 | sn80 OpenRoboto | 67.6 | 362 | 1,183 | rtx4090* | 5 | 43% |
| 14 | sn62 Ridges | 67.6 | 358 | 1,240 | rtx4090* | 13 | 26% |
| 15 | sn124 Swarm | 66.8 | 295 | 916 | rtx4090* | 25 | 11% |
| 16 | sn61 RedTeam | 66.8 | 283 | 456 | rtx4090* | 40 | 4% |
| 17 | sn38 ChronoLLM | 66 | 102 | 1,394 | cpu-small | 10 | 52% |
| 18 | sn111 Claims | 65.4 | 204 | 2,185 | rtx4090* | 5 | 50% |
| 19 | sn121 sundae_bar | 63 | 1,231 | 1,231 = | cpu-small | 2 | 60% |
| 20 | sn81 Reliquary | 62.5 | 77.78 | 272 | rtx4090* | 51 | 6% |

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
| dominated (60–90%) | 17 |
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
| 2026-09-10T01:20 | sn25 | RELEASE | sn25 released v2026.9.9-1042000000 |
| 2026-09-10T01:20 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-10T01:20 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix: validate sampled entropy coverage at |
| 2026-09-10T01:20 | sn100 | RELEASE | sn100 released ctx CLI v3.3.31 |
| 2026-09-10T01:20 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(proof): require miner hotkey signat |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

