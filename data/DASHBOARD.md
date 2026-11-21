# Subnet watch — dashboard

_snapshot 2026-11-21T21:46:57Z · block 9557796 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 106 | `miner_burn` < 0.99 |
| Ranked | 106 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 8 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 22 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 238 | 238 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.1 | 1,897 | 3,751 | rtx4090* | 4 | 40% |
| 3 | sn14 Cacheon | 71.5 | 1,172 | 2,294 | rtx4090* | 5 | 48% |
| 4 | sn15 ORO | 66.6 | 6.22 | 11.36 | cpu-small | 71 | 95% |
| 5 | sn124 Swarm | 65.4 | 198 | 1,260 | rtx4090* | 11 | 29% |
| 6 | sn56 Gradients | 63.8 | 787 | 3,236 | a100-80 | 6 | 43% |
| 7 | sn67 Harnyx | 63.7 | 1.83 | 412 | cpu-small | 153 | 30% |
| 8 | sn53 engy | 63.1 | 94.17 | 12,247 | rtx4090 | 20 | 61% |
| 9 | sn66 conjectures | 62.5 | 78.59 | 933 | rtx4090* | 4 | 80% |
| 10 | sn120 Affine | 61.4 | 2,006 | 2,006 = | rtx4090* | 10 | 10% |
| 11 | sn58 Attune | 61.4 | 57.35 | 144 | rtx4090* | 57 | 30% |
| 12 | sn62 Ridges | 60.4 | 41.00 | 443 | rtx4090* | 46 | 11% |
| 13 | sn111 Claims | 60.1 | 38.20 | 154 | rtx4090* | 4 | 88% |
| 14 | sn97 Ingot | 59.2 | 1,029 | 1,029 = | rtx4090* | 4 | 40% |
| 15 | sn28 SayGM | 58 | 22.56 | 3,478 | rtx4090* | 155 | 22% |
| 16 | sn25 UR | 58 | 19.64 | 19.64 = | rtx4090* | 10 | 45% |
| 17 | sn102 ConnitoAI | 57 | 530 | 532 | rtx4090* | 4 | 25% |
| 18 | sn46 Instant | 55.6 | 135 | 170 | cpu-small | 9 | 20% |
| 19 | sn4 Targon | 55.5 | 4,869 | 19,386 | rtx4090* | 5 | 66% |
| 20 | sn107 Minos | 54.3 | 131 | 11,511 | cpu-small | 20 | 81% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 25 |
| captured (>90%) | 29 |

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
| 2026-11-21T21:47 | sn57 | BURN_DROP | sn57 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-21T21:47 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Add verified public development roster to |
| 2026-11-21T21:47 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Complete scientific result worker delive |
| 2026-11-21T21:47 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: DATA: the door holds verified inference  |
| 2026-11-21T21:47 | sn117 | RELEASE | sn117 released everycli v1.2.6 |
| 2026-11-21T21:47 | sn122 | BURN_DROP | sn122 burn fell 1.000 -> 0.115 - miners can earn again |
| 2026-11-21T16:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate canonical Bittensor accounts on  |
| 2026-11-21T16:18 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Harden report checkpoints and independent |
| 2026-11-21T16:18 | sn82 | README_TASK_DIFF | sn82 README task/scoring sections changed |
| 2026-11-21T16:18 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: validator: post-gate kings keep their cro |
| 2026-11-21T16:18 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-11-21T16:18 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Verify teacher metadata is independent of |
| 2026-11-21T16:18 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: Validator: a set whose reply was lost cou |
| 2026-11-21T16:18 | sn117 | RELEASE | sn117 released everycli v1.2.5 |
| 2026-11-21T08:14 | sn90 | RELEASE | sn90 released v1.4.5 — Finney oracle and validator reliability |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

