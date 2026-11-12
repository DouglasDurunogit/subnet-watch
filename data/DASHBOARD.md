# Subnet watch — dashboard

_snapshot 2026-11-12T19:09:59Z · block 9492238 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.1 | 2,548 | 2,548 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.4 | 1,510 | 3,029 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72 | 1,358 | 1,358 = | rtx4090* | 5 | 20% |
| 4 | sn56 Gradients | 70.4 | 824 | 4,344 | rtx4090* | 6 | 50% |
| 5 | sn41 Almanac | 70.2 | 14.14 | 190 | cpu-small | 157 | 3% |
| 6 | sn34 Yugos | 69.9 | 730 | 6,265 | rtx4090* | 3 | 85% |
| 7 | sn67 Harnyx | 68.3 | 7.64 | 131 | cpu-small | 132 | 8% |
| 8 | sn124 Swarm | 67.1 | 323 | 1,739 | rtx4090* | 10 | 31% |
| 9 | sn15 ORO | 66.1 | 6.99 | 10,547 | cpu-small | 75 | 95% |
| 10 | sn53 engy | 64.8 | 158 | 6,554 | rtx4090 | 23 | 40% |
| 11 | sn38 ChronoLLM | 63.5 | 51.60 | 355 | cpu-small | 9 | 52% |
| 12 | sn14 Cacheon | 62.5 | 77.50 | 197 | rtx4090* | 4 | 95% |
| 13 | sn127 Zils | 62.4 | 74.94 | 74.94 = | rtx4090* | 4 | 88% |
| 14 | sn121 sundae_bar | 61.6 | 810 | 810 = | cpu-small | 2 | 60% |
| 15 | sn62 Ridges | 60.2 | 38.82 | 824 | rtx4090* | 43 | 18% |
| 16 | sn4 Targon | 58.2 | 10,806 | 20,607 | rtx4090* | 5 | 60% |
| 17 | sn58 Attune | 58 | 728 | 5,719 | rtx4090* | 5 | 70% |
| 18 | sn5 Hone | 57.6 | 21.53 | 45.85 | rtx4090* | 241 | 1% |
| 19 | sn102 ConnitoAI | 57 | 529 | 531 | rtx4090* | 4 | 25% |
| 20 | sn66 conjectures | 56.8 | 13.89 | 1,071 | rtx4090* | 8 | 81% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 29 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-12T19:10 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #54 from BitMind-AI/fi |
| 2026-11-12T19:10 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Publish miner agent and simplify connecti |
| 2026-11-12T19:10 | sn51 | RELEASE | sn51 released executor-v1.181 |
| 2026-11-12T19:10 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4889 - [P0] validator: a foreign GPU  |
| 2026-11-12T19:10 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-12T19:10 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs: runner keys do not expire; to chang |
| 2026-11-12T19:10 | sn94 | README_TASK_DIFF | sn94 README task/scoring sections changed |
| 2026-11-12T19:10 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge How rewards work (af0e367f) |
| 2026-11-12T11:38 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): the 40-day count belongs t |
| 2026-11-12T11:38 | sn38 | README_TASK_DIFF | sn38 README task/scoring sections changed |
| 2026-11-12T11:38 | sn51 | RELEASE | sn51 released executor-v1.180 |
| 2026-11-12T11:38 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6222 - [P1] Validator: a filler the v |
| 2026-11-12T11:38 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1204 from leadpoet/fi |
| 2026-11-12T11:38 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: perf(audit): score drawn records ahead of |
| 2026-11-12T03:14 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Improve validation Pod recovery and place |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

