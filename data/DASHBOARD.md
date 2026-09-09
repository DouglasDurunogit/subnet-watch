# Subnet watch — dashboard

_snapshot 2026-09-09T18:45:51Z · block 9031830 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.3 | 1,004 | 8,041 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.8 | 434 | 35,229 | cpu-small | 20 | 79% |
| 3 | sn92 MicroTensor | 78.7 | 116 | 260 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76.1 | 4,535 | 4,535 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 72.3 | 1,448 | 5,952 | rtx4090* | 7 | 47% |
| 6 | sn15 ORO | 72 | 28.44 | 25,955 | cpu-small | 76 | 92% |
| 7 | sn67 Harnyx | 71.8 | 19.38 | 101 | cpu-small | 125 | 15% |
| 8 | sn102 ConnitoAI | 71.5 | 1,151 | 1,924 | rtx4090* | 6 | 32% |
| 9 | sn91 cascade | 70.4 | 837 | 3,374 | rtx4090* | 5 | 52% |
| 10 | sn96 Verathos | 69.9 | 32.59 | 182 | rtx4090 | 83 | 30% |
| 11 | sn14 Cacheon | 69.8 | 691 | 1,280 | rtx4090* | 12 | 18% |
| 12 | sn11 TrajectoryRL | 68.8 | 6,970 | 6,970 = | cpu-small | 1 | 100% |
| 13 | sn62 Ridges | 68 | 405 | 1,274 | rtx4090* | 13 | 26% |
| 14 | sn80 OpenRoboto | 67.7 | 378 | 1,228 | rtx4090* | 5 | 43% |
| 15 | sn124 Swarm | 66.8 | 296 | 941 | rtx4090* | 25 | 11% |
| 16 | sn61 RedTeam | 66.7 | 278 | 449 | rtx4090* | 42 | 4% |
| 17 | sn38 ChronoLLM | 66.2 | 106 | 1,447 | cpu-small | 10 | 52% |
| 18 | sn111 Claims | 65.3 | 200 | 3,557 | rtx4090* | 5 | 82% |
| 19 | sn121 sundae_bar | 63.1 | 1,275 | 1,275 = | cpu-small | 2 | 60% |
| 20 | sn108 Prometheon | 61 | 51.58 | 124 | rtx4090* | 11 | 33% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 19 |
| captured (>90%) | 21 |

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
| 2026-09-09T18:46 | sn28 | RELEASE | sn28 released v0.4.17-dev |
| 2026-09-09T18:46 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-09T18:46 | sn62 | RELEASE | sn62 released v0.3.1 |
| 2026-09-09T18:46 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: feat: prevent cluster-autoscaler from dra |
| 2026-09-09T18:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-09T18:46 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Publish verified bootstrap service state |
| 2026-09-09T18:46 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-09-09T18:46 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validator): recover failed Silver ad |
| 2026-09-09T18:46 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Keep leased seeds through a validator re |
| 2026-09-09T15:20 | sn1 | RELEASE | sn1 released v4.4.5 |
| 2026-09-09T15:20 | sn28 | RELEASE | sn28 released v0.4.16-dev |
| 2026-09-09T15:20 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Anchor deployment staleness to the last s |
| 2026-09-09T15:20 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-09T15:20 | sn45 | README_TASK_DIFF | sn45 README task/scoring sections changed |
| 2026-09-09T15:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind dead preflight verifier removal |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

