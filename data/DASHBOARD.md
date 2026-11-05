# Subnet watch — dashboard

_snapshot 2026-11-05T19:03:06Z · block 9441807 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 65 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **65** | income beats machine cost |
| New events this window | 13 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,740 | 2,740 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.9 | 1,797 | 3,602 | rtx4090* | 7 | 25% |
| 3 | sn14 Cacheon | 72.7 | 1,671 | 4,016 | rtx4090* | 3 | 68% |
| 4 | sn97 Ingot | 72.3 | 1,457 | 1,457 = | rtx4090* | 5 | 20% |
| 5 | sn36 Weir | 70.8 | 933 | 1,561 | rtx4090* | 8 | 24% |
| 6 | sn58 Attune | 69.3 | 607 | 4,280 | rtx4090* | 5 | 68% |
| 7 | sn56 Gradients | 68.3 | 445 | 4,794 | rtx4090* | 7 | 51% |
| 8 | sn41 Almanac | 68.3 | 9.13 | 134 | cpu-small | 175 | 2% |
| 9 | sn103 Terza Inference | 67.6 | 361 | 1,092 | rtx4090* | 5 | 40% |
| 10 | sn46 Instant | 67.5 | 136 | 173 | cpu-small | 9 | 47% |
| 11 | sn1 Apex | 67.1 | 307 | 782 | rtx4090* | 4 | 70% |
| 12 | sn102 ConnitoAI | 67 | 299 | 1,017 | rtx4090* | 6 | 33% |
| 13 | sn82 Noah | 66.2 | 356 | 418 | rtx4090* | 64 | 2% |
| 14 | sn107 Minos | 65.9 | 169 | 14,396 | cpu-small | 20 | 80% |
| 15 | sn53 engy | 65 | 168 | 2,786 | rtx4090 | 31 | 21% |
| 16 | sn67 Harnyx | 64.2 | 2.80 | 572 | cpu-small | 133 | 32% |
| 17 | sn15 ORO | 64.1 | 5.87 | 11,345 | cpu-small | 71 | 96% |
| 18 | sn38 ChronoLLM | 63 | 46.64 | 417 | cpu-small | 10 | 52% |
| 19 | sn124 Swarm | 62.8 | 94.83 | 1,473 | rtx4090* | 17 | 27% |
| 20 | sn70 Fugal | 62 | 69.67 | 302 | rtx4090* | 63 | 5% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 29 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-05T19:03 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(status): each miner's model start, d |
| 2026-11-05T19:03 | sn46 | RELEASE | sn46 released v0.1.5 |
| 2026-11-05T19:03 | sn51 | RELEASE | sn51 released lium-protocol-v2.9.0 |
| 2026-11-05T19:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5462 - [P2] Validator: skip the new-n |
| 2026-11-05T19:03 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: report seeds after scoring |
| 2026-11-05T19:03 | sn58 | README_TASK_DIFF | sn58 README task/scoring sections changed |
| 2026-11-05T19:03 | sn66 | RELEASE | sn66 released v2026.11.05 |
| 2026-11-05T19:03 | sn70 | RELEASE | sn70 released image-v2026.11.05b |
| 2026-11-05T19:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1046 from leadpoet/do |
| 2026-11-05T19:03 | sn81 | BURN_DROP | sn81 burn fell 0.999 -> 0.965 - miners can earn again |
| 2026-11-05T19:03 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: build(order-control): signed episode runt |
| 2026-11-05T19:03 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: bench site: references shown if on the s |
| 2026-11-05T19:03 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.602 - miners can earn again |
| 2026-11-05T11:38 | sn51 | RELEASE | sn51 released executor-v1.171 |
| 2026-11-05T11:38 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5664 - [P0] Validator: reclaim a kill |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

