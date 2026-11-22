# Subnet watch — dashboard

_snapshot 2026-11-22T17:04:17Z · block 9563582 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 105 | `miner_burn` < 0.99 |
| Ranked | 105 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 23 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 239 | 239 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.1 | 1,907 | 3,821 | rtx4090* | 4 | 40% |
| 3 | sn15 ORO | 65.3 | 5.86 | 11.74 | cpu-small | 78 | 94% |
| 4 | sn124 Swarm | 64.8 | 165 | 1,291 | rtx4090* | 11 | 29% |
| 5 | sn67 Harnyx | 64.5 | 2.48 | 218 | cpu-small | 145 | 16% |
| 6 | sn56 Gradients | 63.9 | 803 | 3,302 | a100-80 | 6 | 43% |
| 7 | sn53 engy | 63.4 | 103 | 3,635 | rtx4090 | 20 | 61% |
| 8 | sn66 conjectures | 62.6 | 80.24 | 951 | rtx4090* | 4 | 80% |
| 9 | sn120 Affine | 61.5 | 2,073 | 2,073 = | rtx4090* | 10 | 10% |
| 10 | sn58 Attune | 61.5 | 59.45 | 149 | rtx4090* | 57 | 30% |
| 11 | sn60 Bitsec.ai | 60.5 | 589 | 589 = | cpu-small | 3 | 50% |
| 12 | sn111 Claims | 60.2 | 39.56 | 159 | rtx4090* | 4 | 88% |
| 13 | sn62 Ridges | 60.2 | 39.50 | 423 | rtx4090* | 46 | 11% |
| 14 | sn41 Almanac | 60.1 | 1.68 | 286 | cpu-small | 119 | 21% |
| 15 | sn97 Ingot | 59.3 | 1,049 | 1,049 = | rtx4090* | 4 | 40% |
| 16 | sn28 SayGM | 59 | 30.38 | 1,806 | rtx4090* | 154 | 10% |
| 17 | sn25 UR | 58.1 | 20.40 | 20.40 = | rtx4090* | 10 | 45% |
| 18 | sn34 Yugos | 57.7 | 663 | 5,700 | rtx4090* | 3 | 85% |
| 19 | sn102 ConnitoAI | 57 | 538 | 543 | rtx4090* | 4 | 25% |
| 20 | sn4 Targon | 55.5 | 4,934 | 19,642 | rtx4090* | 5 | 66% |

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
| dominated (60–90%) | 29 |
| captured (>90%) | 27 |

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
| 2026-11-22T17:04 | sn90 | RELEASE | sn90 released v1.4.6 |
| 2026-11-22T17:04 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(validator): describe Lium B300 AC-on |
| 2026-11-22T17:04 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(laned): W5b scores each window from o |
| 2026-11-22T17:04 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Revalidate the fresh plant incarnation un |
| 2026-11-22T17:04 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: BBH items as the toolkit's build: its 19  |
| 2026-11-22T17:04 | sn99 | README_TASK_DIFF | sn99 README task/scoring sections changed |
| 2026-11-22T08:53 | sn25 | RELEASE | sn25 released v2026.11.22-1105365180 |
| 2026-11-22T08:53 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: docs(im): one-pager matches today — no pe |
| 2026-11-22T08:53 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(laned): W3b2 pod evidence live verify |
| 2026-11-22T08:53 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Document signed scientific evaluation an |
| 2026-11-22T08:53 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Bank provenance record (reward lane, own |
| 2026-11-22T01:42 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: tests(laned): W5d scorer acceptance tests |
| 2026-11-21T21:47 | sn57 | BURN_DROP | sn57 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-21T21:47 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Add verified public development roster to |
| 2026-11-21T21:47 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Complete scientific result worker delive |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

