# Subnet watch — dashboard

_snapshot 2026-09-03T23:33:13Z · block 8990130 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 12 | `██████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.1 | 207 | 567 | cpu-small | 9 | 26% |
| 2 | sn3 Teutonic | 75.4 | 3,749 | 3,749 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 73.8 | 33.42 | 88.28 | cpu-small | 21 | 20% |
| 4 | sn23 Trishool | 72.1 | 531 | 531 = | cpu-small | 2 | 80% |
| 5 | sn102 ConnitoAI | 71 | 1,010 | 1,932 | rtx4090* | 6 | 35% |
| 6 | sn91 cascade | 70.3 | 809 | 3,260 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.2 | 21.85 | 21,518 | cpu-small | 74 | 93% |
| 8 | sn96 Verathos | 69.5 | 29.59 | 156 | rtx4090 | 79 | 43% |
| 9 | sn56 Gradients | 68.9 | 538 | 1,347 | rtx4090* | 5 | 74% |
| 10 | sn67 Harnyx | 68.7 | 9.15 | 9.15 = | cpu-small | 218 | 33% |
| 11 | sn111 Claims | 66.4 | 265 | 3,188 | rtx4090* | 5 | 76% |
| 12 | sn124 Swarm | 66.4 | 263 | 811 | rtx4090* | 25 | 11% |
| 13 | sn80 OpenRoboto | 65.2 | 178 | 590 | rtx4090* | 5 | 72% |
| 14 | sn61 RedTeam | 65.1 | 173 | 241 | rtx4090* | 45 | 3% |
| 15 | sn79 MVTRX | 65.1 | 4.49 | 415 | cpu-small | 216 | 10% |
| 16 | sn121 sundae_bar | 62.9 | 1,199 | 1,199 = | cpu-small | 2 | 60% |
| 17 | sn74 Gittensor | 61.2 | 56.58 | 367 | rtx4090 | 11 | 64% |
| 18 | sn101 Tag101 | 61 | 0.42 | 0.75 | cpu-small | 241 | 90% |
| 19 | sn65 True Performance | 60.8 | 56.37 | 121 | rtx4090* | 6 | 83% |
| 20 | sn41 Almanac | 59.2 | 29.34 | 74.30 | cpu-small | 88 | 21% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 20 |
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
| 2026-09-03T23:33 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Tell a rate-limited miner which submissio |
| 2026-09-03T21:41 | sn25 | RELEASE | sn25 released v2026.9.3-1036684010 |
| 2026-09-03T21:41 | sn49 | BURN_DROP | sn49 burn fell 0.990 -> 0.990 - miners can earn again |
| 2026-09-03T21:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind updated scoring protected workflows |
| 2026-09-03T18:49 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: stop dropping the thinking-tok |
| 2026-09-03T18:49 | sn69 | SCORING_COMMIT | sn69 commit touches scoring: Point CLI miners at the console to downlo |
| 2026-09-03T18:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve strict identity boundaries in sc |
| 2026-09-03T18:49 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-03T18:49 | sn74 | RELEASE | sn74 released release-20260903-183804 |
| 2026-09-03T18:49 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.601 - miners can earn again |
| 2026-09-03T15:15 | sn1 | RELEASE | sn1 released v4.4.1 |
| 2026-09-03T15:15 | sn2 | RELEASE | sn2 released 14.14.2 |
| 2026-09-03T11:45 | sn1 | RELEASE | sn1 released v4.4.0 |
| 2026-09-03T11:45 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: base miner: gzip-compress axon responses  |
| 2026-09-03T11:45 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(relearn): pin proven CUDA scoring ev |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

