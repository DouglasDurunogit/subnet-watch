# Subnet watch — dashboard

_snapshot 2026-09-04T01:24:49Z · block 8990688 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81 | 207 | 565 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.8 | 86.20 | 5,557 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.5 | 3,760 | 3,760 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 73.5 | 31.29 | 82.75 | cpu-small | 21 | 20% |
| 5 | sn23 Trishool | 72.1 | 532 | 532 = | cpu-small | 2 | 80% |
| 6 | sn102 ConnitoAI | 71.4 | 1,116 | 1,865 | rtx4090* | 5 | 33% |
| 7 | sn15 ORO | 70.6 | 21.95 | 21,614 | cpu-small | 74 | 93% |
| 8 | sn96 Verathos | 69.4 | 28.93 | 152 | rtx4090 | 79 | 44% |
| 9 | sn91 cascade | 69.3 | 610 | 3,291 | rtx4090* | 5 | 52% |
| 10 | sn56 Gradients | 68.9 | 539 | 1,349 | rtx4090* | 5 | 74% |
| 11 | sn67 Harnyx | 68.8 | 9.15 | 9.15 = | cpu-small | 220 | 32% |
| 12 | sn111 Claims | 66.4 | 269 | 3,228 | rtx4090* | 5 | 76% |
| 13 | sn124 Swarm | 66.4 | 263 | 812 | rtx4090* | 25 | 11% |
| 14 | sn79 MVTRX | 65.5 | 4.94 | 406 | cpu-small | 214 | 9% |
| 15 | sn80 OpenRoboto | 65.2 | 176 | 636 | rtx4090* | 5 | 71% |
| 16 | sn61 RedTeam | 65.1 | 174 | 243 | rtx4090* | 45 | 3% |
| 17 | sn98 NeverPlayAlone | 64.4 | 1,857 | 1,857 = | cpu-small | 1 | 100% |
| 18 | sn121 sundae_bar | 62.9 | 1,193 | 1,193 = | cpu-small | 2 | 60% |
| 19 | sn74 Gittensor | 61.2 | 56.56 | 368 | rtx4090 | 11 | 64% |
| 20 | sn65 True Performance | 60.5 | 51.51 | 111 | rtx4090* | 6 | 85% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-04T01:25 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): commit the daily vector d |
| 2026-09-04T01:25 | sn25 | RELEASE | sn25 released v2026.9.3-1036806790 |
| 2026-09-04T01:25 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: fix semantic reward consensus fixture |
| 2026-09-04T01:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Prevent source add reward queue starvatio |
| 2026-09-04T01:25 | sn107 | BURN_DROP | sn107 burn fell 1.000 -> 0.812 - miners can earn again |
| 2026-09-04T01:25 | sn107 | SCORING_COMMIT | sn107 commit touches scoring: Merge pull request #39 from minos-protoc |
| 2026-09-03T23:33 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Tell a rate-limited miner which submissio |
| 2026-09-03T21:41 | sn25 | RELEASE | sn25 released v2026.9.3-1036684010 |
| 2026-09-03T21:41 | sn49 | BURN_DROP | sn49 burn fell 0.990 -> 0.990 - miners can earn again |
| 2026-09-03T21:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind updated scoring protected workflows |
| 2026-09-03T18:49 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: stop dropping the thinking-tok |
| 2026-09-03T18:49 | sn69 | SCORING_COMMIT | sn69 commit touches scoring: Point CLI miners at the console to downlo |
| 2026-09-03T18:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve strict identity boundaries in sc |
| 2026-09-03T18:49 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-03T18:49 | sn74 | RELEASE | sn74 released release-20260903-183804 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

