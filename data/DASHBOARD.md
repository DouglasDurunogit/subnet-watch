# Subnet watch — dashboard

_snapshot 2026-11-18T00:00:21Z · block 9529689 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 86.4 | 809 | 3,238 | cpu-small | 6 | 40% |
| 2 | sn42 CADmind | 81.7 | 240 | 240 = | cpu-small | 5 | 20% |
| 3 | sn3 Teutonic | 73.7 | 2,224 | 2,224 = | rtx4090* | 4 | 40% |
| 4 | sn58 Attune | 68.4 | 464 | 748 | rtx4090* | 5 | 70% |
| 5 | sn56 Gradients | 67.9 | 392 | 4,012 | rtx4090* | 7 | 49% |
| 6 | sn14 Cacheon | 66.7 | 278 | 2,584 | rtx4090* | 5 | 50% |
| 7 | sn124 Swarm | 66.3 | 254 | 1,379 | rtx4090* | 11 | 30% |
| 8 | sn15 ORO | 66.2 | 5.88 | 9,232 | cpu-small | 71 | 95% |
| 9 | sn67 Harnyx | 66.2 | 3.86 | 183 | cpu-small | 147 | 13% |
| 10 | sn53 engy | 66 | 222 | 8,795 | rtx4090 | 23 | 40% |
| 11 | sn120 Affine | 61.9 | 2,304 | 2,304 = | rtx4090* | 10 | 10% |
| 12 | sn38 ChronoLLM | 61.7 | 34.20 | 308 | cpu-small | 10 | 52% |
| 13 | sn60 Bitsec.ai | 60.7 | 618 | 618 = | cpu-small | 3 | 50% |
| 14 | sn62 Ridges | 60.4 | 41.77 | 506 | rtx4090* | 45 | 12% |
| 15 | sn111 Claims | 60.3 | 41.26 | 165 | rtx4090* | 4 | 88% |
| 16 | sn97 Ingot | 59.7 | 1,207 | 1,207 = | rtx4090* | 5 | 20% |
| 17 | sn102 ConnitoAI | 57.7 | 653 | 653 | rtx4090* | 4 | 25% |
| 18 | sn4 Targon | 57.6 | 9,198 | 19,750 | rtx4090* | 5 | 62% |
| 19 | sn5 Hone | 56.8 | 19.28 | 42.05 | rtx4090* | 241 | 1% |
| 20 | sn66 conjectures | 56.6 | 12.58 | 1,011 | rtx4090* | 8 | 81% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 25 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
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
| 2026-11-17T17:44 | sn7 | RELEASE | sn7 released release-20261117-160316 |
| 2026-11-17T17:44 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Drop VALIDATOR_MODE: the validator always  |
| 2026-11-17T17:44 | sn12 | RELEASE | sn12 released validator-staging-2026-11-17-44119698793-630-1: fix: fai |
| 2026-11-17T17:44 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix: failure to connect to miner creates  |
| 2026-11-17T17:44 | sn25 | RELEASE | sn25 released v2026.11.17-1101053110 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

