# Subnet watch — dashboard

_snapshot 2026-11-21T16:18:04Z · block 9556151 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 104 | `miner_burn` < 0.99 |
| Ranked | 104 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 2 | `█` |
| 0.2–0.4 | 8 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 11 | `████` |
| ≥0.99 dead | 24 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.7 | 240 | 240 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.1 | 1,889 | 3,837 | rtx4090* | 4 | 40% |
| 3 | sn14 Cacheon | 71.6 | 1,178 | 2,306 | rtx4090* | 5 | 48% |
| 4 | sn15 ORO | 66.5 | 6.31 | 8,541 | cpu-small | 71 | 95% |
| 5 | sn124 Swarm | 65.5 | 199 | 1,267 | rtx4090* | 11 | 29% |
| 6 | sn56 Gradients | 63.8 | 791 | 3,251 | a100-80 | 6 | 43% |
| 7 | sn67 Harnyx | 63.6 | 1.84 | 415 | cpu-small | 153 | 30% |
| 8 | sn53 engy | 62.7 | 82.61 | 880 | rtx4090 | 20 | 61% |
| 9 | sn66 conjectures | 62.6 | 80.49 | 953 | rtx4090* | 4 | 82% |
| 10 | sn58 Attune | 61.5 | 58.72 | 147 | rtx4090* | 57 | 30% |
| 11 | sn120 Affine | 61.4 | 2,015 | 2,015 = | rtx4090* | 10 | 10% |
| 12 | sn62 Ridges | 60.4 | 41.88 | 451 | rtx4090* | 46 | 11% |
| 13 | sn111 Claims | 60.1 | 38.59 | 156 | rtx4090* | 4 | 88% |
| 14 | sn97 Ingot | 59.2 | 1,041 | 1,041 = | rtx4090* | 4 | 40% |
| 15 | sn25 UR | 57.9 | 19.48 | 19.48 = | rtx4090* | 10 | 45% |
| 16 | sn102 ConnitoAI | 57 | 533 | 535 | rtx4090* | 4 | 25% |
| 17 | sn1 Apex | 56.4 | 451 | 523 | rtx4090* | 4 | 61% |
| 18 | sn4 Targon | 55.5 | 4,894 | 19,484 | rtx4090* | 5 | 66% |
| 19 | sn46 Instant | 55.3 | 126 | 162 | cpu-small | 9 | 22% |
| 20 | sn107 Minos | 54.8 | 146 | 11,382 | cpu-small | 20 | 79% |

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
| captured (>90%) | 26 |

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
| 2026-11-21T16:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate canonical Bittensor accounts on  |
| 2026-11-21T16:18 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Harden report checkpoints and independent |
| 2026-11-21T16:18 | sn82 | README_TASK_DIFF | sn82 README task/scoring sections changed |
| 2026-11-21T16:18 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: validator: post-gate kings keep their cro |
| 2026-11-21T16:18 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-11-21T16:18 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Verify teacher metadata is independent of |
| 2026-11-21T16:18 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: Validator: a set whose reply was lost cou |
| 2026-11-21T16:18 | sn117 | RELEASE | sn117 released everycli v1.2.5 |
| 2026-11-21T08:14 | sn90 | RELEASE | sn90 released v1.4.5 — Finney oracle and validator reliability |
| 2026-11-21T08:14 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: feat(validator): prefer Finney oracle for |
| 2026-11-21T00:54 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6863 - [P3] Validator runs each pod w |
| 2026-11-21T00:54 | sn66 | RELEASE | sn66 released v2026.11.20.2 |
| 2026-11-21T00:54 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Publish verification holds for RH, Erdős  |
| 2026-11-21T00:54 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve bounded validator readiness deli |
| 2026-11-21T00:54 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: miner_lookup fix: ruff --fix + black (re |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

