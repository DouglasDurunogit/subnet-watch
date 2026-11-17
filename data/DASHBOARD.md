# Subnet watch — dashboard

_snapshot 2026-11-17T17:44:27Z · block 9527810 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 16 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.5 | 231 | 231 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.6 | 2,178 | 4,364 | rtx4090* | 4 | 40% |
| 3 | sn58 Attune | 68.3 | 448 | 722 | rtx4090* | 5 | 70% |
| 4 | sn56 Gradients | 67.8 | 378 | 3,877 | rtx4090* | 7 | 49% |
| 5 | sn70 Fugal | 66.9 | 297 | 2,586 | rtx4090* | 3 | 85% |
| 6 | sn14 Cacheon | 66.6 | 270 | 2,505 | rtx4090* | 5 | 50% |
| 7 | sn124 Swarm | 66.4 | 260 | 1,406 | rtx4090* | 10 | 31% |
| 8 | sn67 Harnyx | 66 | 3.72 | 178 | cpu-small | 147 | 13% |
| 9 | sn53 engy | 65.8 | 210 | 8,337 | rtx4090 | 23 | 40% |
| 10 | sn15 ORO | 65.6 | 5.90 | 8,964 | cpu-small | 70 | 95% |
| 11 | sn120 Affine | 61.8 | 2,228 | 2,228 = | rtx4090* | 10 | 10% |
| 12 | sn38 ChronoLLM | 61.7 | 33.18 | 299 | cpu-small | 10 | 52% |
| 13 | sn60 Bitsec.ai | 60.6 | 607 | 607 = | cpu-small | 3 | 50% |
| 14 | sn62 Ridges | 60.3 | 40.35 | 491 | rtx4090* | 45 | 12% |
| 15 | sn117 everyframe.studi | 60.2 | 40.18 | 70.19 | rtx4090* | 27 | 54% |
| 16 | sn111 Claims | 60.2 | 39.71 | 160 | rtx4090* | 4 | 88% |
| 17 | sn97 Ingot | 59.6 | 1,168 | 1,168 = | rtx4090* | 5 | 20% |
| 18 | sn4 Targon | 57.5 | 8,901 | 19,113 | rtx4090* | 5 | 62% |
| 19 | sn102 ConnitoAI | 57.5 | 625 | 626 | rtx4090* | 4 | 25% |
| 20 | sn24 ms.computer | 57.5 | 18.57 | 125 | rtx4090* | 191 | 2% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 26 |
| captured (>90%) | 25 |

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
| 2026-11-17T17:44 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add 8×H200 evaluator support with TP2 MiMo |
| 2026-11-17T17:44 | sn7 | RELEASE | sn7 released release-20261117-160316 |
| 2026-11-17T17:44 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Drop VALIDATOR_MODE: the validator always  |
| 2026-11-17T17:44 | sn12 | RELEASE | sn12 released validator-staging-2026-11-17-44119698793-630-1: fix: fai |
| 2026-11-17T17:44 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix: failure to connect to miner creates  |
| 2026-11-17T17:44 | sn25 | RELEASE | sn25 released v2026.11.17-1101053110 |
| 2026-11-17T17:44 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/one-extender-stack-per-miner-1 |
| 2026-11-17T17:44 | sn42 | RELEASE | sn42 released v0.6.21 |
| 2026-11-17T17:44 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: reference miner: find a fitted product's  |
| 2026-11-17T17:44 | sn51 | RELEASE | sn51 released lium-protocol-v2.16.0 |
| 2026-11-17T17:44 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6579 - [P1] Validator refuses a reser |
| 2026-11-17T17:44 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-17T17:44 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Add cathedral_sealed_hotels_v1 schema, pi |
| 2026-11-17T17:44 | sn113 | BURN_DROP | sn113 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-17T17:44 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Reduce validator prefetch load, reuse a  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

