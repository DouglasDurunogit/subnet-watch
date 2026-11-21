# Subnet watch — dashboard

_snapshot 2026-11-21T08:14:09Z · block 9553752 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 106 | `miner_burn` < 0.99 |
| Ranked | 106 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 22 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.4 | 226 | 226 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 72.9 | 1,779 | 3,519 | rtx4090* | 4 | 40% |
| 3 | sn14 Cacheon | 66.7 | 279 | 1,925 | rtx4090* | 5 | 48% |
| 4 | sn15 ORO | 66.7 | 6.13 | 7,962 | cpu-small | 67 | 95% |
| 5 | sn124 Swarm | 65.3 | 188 | 1,133 | rtx4090* | 11 | 28% |
| 6 | sn56 Gradients | 63.6 | 735 | 3,028 | a100-80 | 6 | 43% |
| 7 | sn67 Harnyx | 63.3 | 1.65 | 387 | cpu-small | 150 | 30% |
| 8 | sn53 engy | 62.3 | 73.39 | 790 | rtx4090 | 20 | 61% |
| 9 | sn66 conjectures | 62.3 | 72.87 | 871 | rtx4090* | 4 | 80% |
| 10 | sn104 TAOstatus | 62 | 915 | 1,824 | cpu-small | 2 | 100% |
| 11 | sn120 Affine | 61.2 | 1,872 | 1,872 = | rtx4090* | 10 | 10% |
| 12 | sn58 Attune | 61.1 | 52.43 | 132 | rtx4090* | 57 | 30% |
| 13 | sn62 Ridges | 60.2 | 38.67 | 474 | rtx4090* | 45 | 12% |
| 14 | sn28 SayGM | 59.8 | 37.05 | 4,882 | rtx4090* | 123 | 32% |
| 15 | sn111 Claims | 59.8 | 35.40 | 144 | rtx4090* | 4 | 88% |
| 16 | sn97 Ingot | 59.2 | 1,033 | 1,033 = | rtx4090* | 4 | 40% |
| 17 | sn25 UR | 57.6 | 17.41 | 17.41 = | rtx4090* | 10 | 45% |
| 18 | sn102 ConnitoAI | 56.9 | 519 | 522 | rtx4090* | 4 | 25% |
| 19 | sn1 Apex | 56.3 | 429 | 551 | rtx4090* | 4 | 58% |
| 20 | sn46 Instant | 55.7 | 139 | 175 | cpu-small | 9 | 14% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 26 |
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
| 2026-11-21T08:14 | sn90 | RELEASE | sn90 released v1.4.5 — Finney oracle and validator reliability |
| 2026-11-21T08:14 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: feat(validator): prefer Finney oracle for |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

