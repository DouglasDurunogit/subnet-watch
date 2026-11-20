# Subnet watch — dashboard

_snapshot 2026-11-20T19:13:36Z · block 9549849 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 107 | `miner_burn` < 0.99 |
| Ranked | 107 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 8 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 21 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.3 | 219 | 219 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.2 | 1,914 | 3,886 | rtx4090* | 4 | 40% |
| 3 | sn67 Harnyx | 66.6 | 4.37 | 4.37 = | cpu-small | 229 | 7% |
| 4 | sn124 Swarm | 65 | 176 | 637 | rtx4090* | 11 | 30% |
| 5 | sn15 ORO | 64.9 | 5.19 | 11.11 | cpu-small | 77 | 95% |
| 6 | sn56 Gradients | 63.6 | 741 | 3,135 | a100-80 | 6 | 43% |
| 7 | sn53 engy | 62.4 | 75.78 | 813 | rtx4090 | 20 | 61% |
| 8 | sn120 Affine | 61.5 | 2,042 | 2,042 = | rtx4090* | 10 | 10% |
| 9 | sn58 Attune | 61.2 | 53.91 | 136 | rtx4090* | 57 | 30% |
| 10 | sn66 conjectures | 60.8 | 46.60 | 968 | rtx4090* | 4 | 87% |
| 11 | sn62 Ridges | 60.3 | 39.86 | 487 | rtx4090* | 45 | 12% |
| 12 | sn111 Claims | 59.9 | 36.25 | 147 | rtx4090* | 4 | 88% |
| 13 | sn97 Ingot | 59.3 | 1,062 | 1,062 = | rtx4090* | 4 | 40% |
| 14 | sn34 Yugos | 57.5 | 619 | 5,321 | rtx4090* | 3 | 85% |
| 15 | sn102 ConnitoAI | 57.3 | 576 | 590 | rtx4090* | 4 | 26% |
| 16 | sn28 SayGM | 56.9 | 17.00 | 702 | rtx4090* | 114 | 59% |
| 17 | sn1 Apex | 56.6 | 473 | 596 | rtx4090* | 4 | 56% |
| 18 | sn5 Hone | 56.4 | 16.30 | 36.78 | rtx4090* | 241 | 1% |
| 19 | sn46 Instant | 55.6 | 137 | 154 | cpu-small | 9 | 17% |
| 20 | sn4 Targon | 55.3 | 4,649 | 18,500 | rtx4090* | 5 | 66% |

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
| wide (<30%) | 27 |
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
| 2026-11-20T11:26 | sn25 | RELEASE | sn25 released v2026.11.19-1103608200 |
| 2026-11-20T11:26 | sn51 | RELEASE | sn51 released executor-v1.192 |
| 2026-11-20T11:26 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6666 - [P1] Executor trusts the valid |
| 2026-11-20T11:26 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-20T11:26 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record reviewed scorer changes in protect |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

