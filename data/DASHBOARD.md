# Subnet watch — dashboard

_snapshot 2026-11-21T00:54:23Z · block 9551553 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 106 | `miner_burn` < 0.99 |
| Ranked | 106 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 22 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.4 | 226 | 226 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73 | 1,845 | 3,699 | rtx4090* | 4 | 40% |
| 3 | sn67 Harnyx | 66.6 | 4.42 | 4.42 = | cpu-small | 227 | 8% |
| 4 | sn15 ORO | 65.6 | 5.32 | 11.36 | cpu-small | 77 | 95% |
| 5 | sn124 Swarm | 65.1 | 179 | 649 | rtx4090* | 11 | 30% |
| 6 | sn66 conjectures | 64.7 | 154 | 937 | rtx4090* | 3 | 83% |
| 7 | sn53 engy | 62.4 | 76.79 | 823 | rtx4090 | 20 | 61% |
| 8 | sn56 Gradients | 62.1 | 468 | 2,461 | a100-80 | 6 | 43% |
| 9 | sn120 Affine | 61.3 | 1,948 | 1,948 = | rtx4090* | 10 | 10% |
| 10 | sn58 Attune | 61.3 | 54.79 | 138 | rtx4090* | 57 | 30% |
| 11 | sn62 Ridges | 60.3 | 40.76 | 496 | rtx4090* | 45 | 12% |
| 12 | sn111 Claims | 60 | 37.08 | 150 | rtx4090* | 4 | 88% |
| 13 | sn97 Ingot | 59.4 | 1,081 | 1,081 = | rtx4090* | 4 | 40% |
| 14 | sn25 UR | 57.8 | 18.86 | 18.86 = | rtx4090* | 9 | 46% |
| 15 | sn34 Yugos | 57.5 | 631 | 5,425 | rtx4090* | 3 | 85% |
| 16 | sn28 SayGM | 57.4 | 19.40 | 1,529 | rtx4090* | 100 | 45% |
| 17 | sn102 ConnitoAI | 57.2 | 568 | 582 | rtx4090* | 4 | 26% |
| 18 | sn5 Hone | 56.8 | 16.88 | 37.46 | rtx4090* | 241 | 1% |
| 19 | sn1 Apex | 56.5 | 466 | 592 | rtx4090* | 4 | 57% |
| 20 | sn4 Targon | 55.4 | 4,735 | 18,842 | rtx4090* | 5 | 66% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 28 |
| captured (>90%) | 24 |

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
| 2026-11-21T00:54 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6863 - [P3] Validator runs each pod w |
| 2026-11-21T00:54 | sn66 | RELEASE | sn66 released v2026.11.20.2 |
| 2026-11-21T00:54 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Publish verification holds for RH, Erdős  |
| 2026-11-21T00:54 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve bounded validator readiness deli |
| 2026-11-21T00:54 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: miner_lookup fix: ruff --fix + black (re |
| 2026-11-20T19:14 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/runtime-492-1119 (3e9e6f2b) ont |
| 2026-11-20T19:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6769 - [P4] Validator: a readable upp |
| 2026-11-20T19:14 | sn56 | README_TASK_DIFF | sn56 README task/scoring sections changed |
| 2026-11-20T19:14 | sn58 | BURN_DROP | sn58 burn fell 1.000 -> 0.300 - miners can earn again |
| 2026-11-20T19:14 | sn58 | SCORING_COMMIT | sn58 commit touches scoring: feat(horizon): Horizon miners share Horiz |
| 2026-11-20T19:14 | sn66 | RELEASE | sn66 released v2026.11.20 |
| 2026-11-20T19:14 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Update unknown-runtime control after veri |
| 2026-11-20T19:14 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: task.json drops parent (starts lists it); |
| 2026-11-20T19:14 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Client refusal text: miner-x's wording ( |
| 2026-11-20T19:14 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

