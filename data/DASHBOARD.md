# Subnet watch — dashboard

_snapshot 2026-09-03T18:49:06Z · block 8988710 · run_status **ok**_

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
| 0–0.2 | 13 | `██████` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81 | 204 | 558 | cpu-small | 9 | 26% |
| 2 | sn3 Teutonic | 75.5 | 3,819 | 3,819 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 73.8 | 34.26 | 90.44 | cpu-small | 21 | 20% |
| 4 | sn23 Trishool | 72.1 | 539 | 539 = | cpu-small | 2 | 80% |
| 5 | sn91 cascade | 70.4 | 834 | 3,360 | rtx4090* | 5 | 52% |
| 6 | sn15 ORO | 70.4 | 22.23 | 21,879 | cpu-small | 74 | 93% |
| 7 | sn96 Verathos | 69.7 | 31.10 | 170 | rtx4090 | 80 | 41% |
| 8 | sn56 Gradients | 69 | 548 | 1,372 | rtx4090* | 5 | 74% |
| 9 | sn67 Harnyx | 69 | 9.40 | 9.40 = | cpu-small | 221 | 33% |
| 10 | sn111 Claims | 68.9 | 553 | 2,447 | rtx4090* | 5 | 57% |
| 11 | sn124 Swarm | 66.5 | 271 | 836 | rtx4090* | 25 | 11% |
| 12 | sn61 RedTeam | 65.2 | 178 | 249 | rtx4090* | 45 | 3% |
| 13 | sn79 MVTRX | 64.8 | 4.53 | 421 | cpu-small | 220 | 10% |
| 14 | sn60 Bitsec.ai | 64 | 1,661 | 1,661 = | cpu-small | 2 | 50% |
| 15 | sn121 sundae_bar | 62.9 | 1,211 | 1,211 = | cpu-small | 2 | 60% |
| 16 | sn101 Tag101 | 61.9 | 0.67 | 0.82 | cpu-small | 243 | 90% |
| 17 | sn65 True Performance | 61.6 | 68.62 | 145 | rtx4090* | 6 | 80% |
| 18 | sn74 Gittensor | 61.4 | 63.78 | 369 | rtx4090 | 11 | 64% |
| 19 | sn2 DSperse | 60.9 | 47.77 | 147 | rtx4090* | 9 | 82% |
| 20 | sn28 SayGM | 60.5 | 44.98 | 903 | rtx4090* | 41 | 43% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 21 |
| captured (>90%) | 24 |

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
| 2026-09-03T06:32 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.974 - miners can earn again |
| 2026-09-03T06:32 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: ci: run the non-scoring tests on every pu |
| 2026-09-03T06:32 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: scoring: block-scheduled fresh-king margi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

