# Subnet watch — dashboard

_snapshot 2026-09-03T21:40:43Z · block 8989568 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

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
| 1 | sn92 MicroTensor | 81 | 206 | 562 | cpu-small | 9 | 26% |
| 2 | sn3 Teutonic | 75.5 | 3,848 | 3,848 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 73.9 | 34.53 | 91.16 | cpu-small | 21 | 20% |
| 4 | sn23 Trishool | 72.1 | 542 | 542 = | cpu-small | 2 | 80% |
| 5 | sn102 ConnitoAI | 71.6 | 1,193 | 1,548 | rtx4090* | 6 | 28% |
| 6 | sn15 ORO | 70.5 | 22.32 | 21,960 | cpu-small | 74 | 93% |
| 7 | sn91 cascade | 70.3 | 820 | 3,305 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 69.6 | 30.11 | 163 | rtx4090 | 80 | 41% |
| 9 | sn56 Gradients | 69 | 551 | 1,378 | rtx4090* | 5 | 74% |
| 10 | sn67 Harnyx | 69 | 9.40 | 9.40 = | cpu-small | 220 | 33% |
| 11 | sn124 Swarm | 66.5 | 268 | 826 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 66.4 | 271 | 3,256 | rtx4090* | 5 | 76% |
| 13 | sn80 OpenRoboto | 65.3 | 184 | 607 | rtx4090* | 5 | 72% |
| 14 | sn61 RedTeam | 65.2 | 176 | 246 | rtx4090* | 45 | 3% |
| 15 | sn79 MVTRX | 65.2 | 4.85 | 424 | cpu-small | 215 | 10% |
| 16 | sn121 sundae_bar | 63.1 | 1,257 | 1,257 = | cpu-small | 2 | 60% |
| 17 | sn65 True Performance | 61.3 | 63.29 | 135 | rtx4090* | 6 | 82% |
| 18 | sn74 Gittensor | 61.2 | 57.47 | 372 | rtx4090 | 11 | 64% |
| 19 | sn101 Tag101 | 60.7 | 0.33 | 0.83 | cpu-small | 245 | 90% |
| 20 | sn2 DSperse | 60.5 | 43.22 | 160 | rtx4090* | 9 | 82% |

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
| concentrated (30–60%) | 19 |
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
| 2026-09-03T06:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

