# Subnet watch — dashboard

_snapshot 2026-09-10T11:38:39Z · block 9036886 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.1 | 951 | 7,615 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.6 | 409 | 34,683 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 78.5 | 109 | 243 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76 | 4,364 | 4,364 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 72.1 | 1,401 | 5,763 | rtx4090* | 7 | 47% |
| 6 | sn15 ORO | 71.1 | 22.08 | 22,665 | cpu-small | 80 | 92% |
| 7 | sn67 Harnyx | 70.7 | 15.20 | 727 | cpu-small | 145 | 21% |
| 8 | sn91 cascade | 70.4 | 833 | 3,355 | rtx4090* | 5 | 52% |
| 9 | sn14 Cacheon | 69.6 | 666 | 1,233 | rtx4090* | 12 | 18% |
| 10 | sn96 Verathos | 69.5 | 30.00 | 304 | rtx4090 | 84 | 30% |
| 11 | sn11 TrajectoryRL | 68.7 | 6,658 | 6,658 = | cpu-small | 1 | 100% |
| 12 | sn102 ConnitoAI | 68.2 | 439 | 1,852 | rtx4090* | 7 | 33% |
| 13 | sn80 OpenRoboto | 67.5 | 354 | 1,260 | rtx4090* | 5 | 43% |
| 14 | sn38 ChronoLLM | 67.4 | 146 | 3,100 | cpu-small | 10 | 52% |
| 15 | sn61 RedTeam | 67 | 307 | 483 | rtx4090* | 39 | 5% |
| 16 | sn124 Swarm | 66.8 | 298 | 926 | rtx4090* | 25 | 11% |
| 17 | sn111 Claims | 66.1 | 253 | 3,477 | rtx4090* | 5 | 78% |
| 18 | sn121 sundae_bar | 63 | 1,232 | 1,232 = | cpu-small | 2 | 60% |
| 19 | sn81 Reliquary | 61.8 | 63.62 | 236 | rtx4090* | 52 | 14% |
| 20 | sn108 Prometheon | 61.3 | 54.99 | 320 | rtx4090* | 11 | 30% |

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
| dominated (60–90%) | 19 |
| captured (>90%) | 20 |

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
| 2026-09-10T11:39 | sn15 | RELEASE | sn15 released v2.0.0 |
| 2026-09-10T11:39 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Verify scope-bound environment deliveries |
| 2026-09-10T11:39 | sn25 | RELEASE | sn25 released v2026.9.10-1042298530 |
| 2026-09-10T11:39 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: crv4: accept reviewed runtime 455 validat |
| 2026-09-10T11:39 | sn51 | RELEASE | sn51 released executor-v1.125 |
| 2026-09-10T11:39 | sn62 | RELEASE | sn62 released v0.3.3 |
| 2026-09-10T11:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-10T11:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: docs: state midnight continuous evaluatio |
| 2026-09-10T11:39 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: docs: concise miner quickstart for funded |
| 2026-09-10T11:39 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): fail closed on incomplete ha |
| 2026-09-10T06:19 | sn15 | RELEASE | sn15 released shoppingbench-final |
| 2026-09-10T06:19 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-09-10T06:19 | sn25 | RELEASE | sn25 released v2026.9.9-1042199790 |
| 2026-09-10T06:19 | sn51 | RELEASE | sn51 released executor-v1.124 |
| 2026-09-10T06:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3006 - [P1] validator stops serialisi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

