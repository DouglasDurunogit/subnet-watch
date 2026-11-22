# Subnet watch — dashboard

_snapshot 2026-11-22T08:53:37Z · block 9561129 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 105 | `miner_burn` < 0.99 |
| Ranked | 105 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 8 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 23 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.7 | 241 | 241 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.1 | 1,895 | 3,848 | rtx4090* | 4 | 40% |
| 3 | sn15 ORO | 66.3 | 5.84 | 11.55 | cpu-small | 74 | 95% |
| 4 | sn124 Swarm | 64.8 | 165 | 1,285 | rtx4090* | 11 | 29% |
| 5 | sn67 Harnyx | 64.7 | 2.48 | 218 | cpu-small | 143 | 16% |
| 6 | sn56 Gradients | 63.9 | 802 | 3,297 | a100-80 | 6 | 43% |
| 7 | sn53 engy | 62.8 | 87.11 | 924 | rtx4090 | 20 | 61% |
| 8 | sn14 Cacheon | 62.7 | 82.61 | 3,439 | rtx4090* | 6 | 71% |
| 9 | sn66 conjectures | 62.4 | 76.71 | 956 | rtx4090* | 4 | 81% |
| 10 | sn58 Attune | 61.6 | 59.92 | 150 | rtx4090* | 57 | 30% |
| 11 | sn120 Affine | 61.5 | 2,049 | 2,049 = | rtx4090* | 10 | 10% |
| 12 | sn41 Almanac | 60.9 | 1.89 | 301 | cpu-small | 119 | 18% |
| 13 | sn62 Ridges | 60.4 | 41.22 | 445 | rtx4090* | 46 | 11% |
| 14 | sn111 Claims | 60.2 | 39.41 | 159 | rtx4090* | 4 | 88% |
| 15 | sn97 Ingot | 59.3 | 1,046 | 1,046 = | rtx4090* | 4 | 40% |
| 16 | sn25 UR | 58.1 | 20.33 | 20.33 = | rtx4090* | 10 | 45% |
| 17 | sn28 SayGM | 57.6 | 20.46 | 3,720 | rtx4090* | 154 | 21% |
| 18 | sn102 ConnitoAI | 57 | 538 | 542 | rtx4090* | 4 | 25% |
| 19 | sn4 Targon | 55.5 | 4,914 | 19,564 | rtx4090* | 5 | 66% |
| 20 | sn46 Instant | 55.4 | 127 | 170 | cpu-small | 9 | 20% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 26 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-22T08:53 | sn25 | RELEASE | sn25 released v2026.11.22-1105365180 |
| 2026-11-22T08:53 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: docs(im): one-pager matches today — no pe |
| 2026-11-22T08:53 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(laned): W3b2 pod evidence live verify |
| 2026-11-22T08:53 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Document signed scientific evaluation an |
| 2026-11-22T08:53 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Bank provenance record (reward lane, own |
| 2026-11-22T01:42 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: tests(laned): W5d scorer acceptance tests |
| 2026-11-21T21:47 | sn57 | BURN_DROP | sn57 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-21T21:47 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Add verified public development roster to |
| 2026-11-21T21:47 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Complete scientific result worker delive |
| 2026-11-21T21:47 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: DATA: the door holds verified inference  |
| 2026-11-21T21:47 | sn117 | RELEASE | sn117 released everycli v1.2.6 |
| 2026-11-21T21:47 | sn122 | BURN_DROP | sn122 burn fell 1.000 -> 0.115 - miners can earn again |
| 2026-11-21T16:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate canonical Bittensor accounts on  |
| 2026-11-21T16:18 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Harden report checkpoints and independent |
| 2026-11-21T16:18 | sn82 | README_TASK_DIFF | sn82 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

