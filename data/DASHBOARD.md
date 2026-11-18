# Subnet watch — dashboard

_snapshot 2026-11-18T07:14:32Z · block 9531860 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 64 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **64** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 86.4 | 801 | 3,206 | cpu-small | 8 | 40% |
| 2 | sn42 CADmind | 81.6 | 238 | 238 = | cpu-small | 5 | 20% |
| 3 | sn3 Teutonic | 73.6 | 2,204 | 2,204 = | rtx4090* | 4 | 40% |
| 4 | sn58 Attune | 68.3 | 457 | 736 | rtx4090* | 5 | 70% |
| 5 | sn56 Gradients | 67.9 | 390 | 3,997 | rtx4090* | 7 | 49% |
| 6 | sn67 Harnyx | 66.6 | 4.72 | 4.72 = | cpu-small | 227 | 11% |
| 7 | sn15 ORO | 66 | 6.06 | 9,122 | cpu-small | 72 | 95% |
| 8 | sn53 engy | 65.9 | 220 | 8,691 | rtx4090 | 23 | 40% |
| 9 | sn124 Swarm | 65.4 | 197 | 882 | rtx4090* | 11 | 30% |
| 10 | sn120 Affine | 61.9 | 2,294 | 2,294 = | rtx4090* | 10 | 10% |
| 11 | sn38 ChronoLLM | 61.7 | 33.93 | 305 | cpu-small | 10 | 52% |
| 12 | sn60 Bitsec.ai | 60.6 | 605 | 605 = | cpu-small | 3 | 50% |
| 13 | sn62 Ridges | 60.4 | 41.58 | 504 | rtx4090* | 45 | 12% |
| 14 | sn111 Claims | 60.3 | 41.08 | 164 | rtx4090* | 4 | 88% |
| 15 | sn97 Ingot | 59.7 | 1,198 | 1,198 = | rtx4090* | 5 | 20% |
| 16 | sn4 Targon | 57.6 | 9,246 | 19,854 | rtx4090* | 5 | 62% |
| 17 | sn5 Hone | 56.9 | 18.56 | 41.28 | rtx4090* | 244 | 1% |
| 18 | sn66 conjectures | 56.6 | 12.54 | 1,012 | rtx4090* | 8 | 81% |
| 19 | sn46 Instant | 55.9 | 148 | 221 | cpu-small | 9 | 21% |
| 20 | sn107 Minos | 55.2 | 160 | 12,771 | cpu-small | 20 | 79% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 27 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-18T07:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6566 - [P0] Validator writes the need |
| 2026-11-18T07:14 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-18T07:14 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(rl): a pod's link reaches its task's  |
| 2026-11-18T07:14 | sn127 | RELEASE | sn127 released Release b5a248c |
| 2026-11-18T07:14 | sn127 | README_TASK_DIFF | sn127 README task/scoring sections changed |
| 2026-11-18T00:00 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-18T00:00 | sn12 | RELEASE | sn12 released validator-staging-2026-11-17-44146334658-631-1: fix: sup |
| 2026-11-18T00:00 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: Merge pull request #410 from Desearch-ai/ |
| 2026-11-18T00:00 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/verify-cohort-v2-validator-111 |
| 2026-11-18T00:00 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6466 - Validator: retry the s3fs volu |
| 2026-11-18T00:00 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: validator: approve only images that can p |
| 2026-11-18T00:00 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Crowns: the official-score rule is the d |
| 2026-11-18T00:00 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Add Swarm Test Field and close two evalu |
| 2026-11-18T00:00 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |
| 2026-11-17T17:44 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add 8×H200 evaluator support with TP2 MiMo |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

