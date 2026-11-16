# Subnet watch — dashboard

_snapshot 2026-11-16T06:15:37Z · block 9517166 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.7 | 243 | 243 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.6 | 2,177 | 2,177 = | rtx4090* | 4 | 40% |
| 3 | sn14 Cacheon | 71.7 | 1,232 | 2,440 | rtx4090* | 4 | 49% |
| 4 | sn97 Ingot | 71.6 | 1,199 | 1,199 = | rtx4090* | 5 | 20% |
| 5 | sn24 ms.computer | 71.4 | 1,126 | 1,582 | rtx4090* | 6 | 29% |
| 6 | sn58 Attune | 69 | 562 | 904 | rtx4090* | 5 | 70% |
| 7 | sn41 Almanac | 69 | 10.28 | 116 | cpu-small | 155 | 3% |
| 8 | sn56 Gradients | 68.8 | 512 | 3,906 | rtx4090* | 6 | 50% |
| 9 | sn70 Fugal | 66.9 | 295 | 2,570 | rtx4090* | 3 | 85% |
| 10 | sn15 ORO | 66.3 | 6.08 | 12.24 | cpu-small | 69 | 95% |
| 11 | sn67 Harnyx | 65.5 | 3.06 | 250 | cpu-small | 191 | 18% |
| 12 | sn124 Swarm | 65.2 | 183 | 767 | rtx4090* | 10 | 31% |
| 13 | sn53 engy | 65 | 167 | 6,902 | rtx4090 | 23 | 40% |
| 14 | sn38 ChronoLLM | 62.8 | 43.41 | 300 | cpu-small | 9 | 52% |
| 15 | sn120 Affine | 61.8 | 2,265 | 2,265 = | rtx4090* | 10 | 10% |
| 16 | sn60 Bitsec.ai | 60.4 | 571 | 571 = | cpu-small | 3 | 50% |
| 17 | sn111 Claims | 60.2 | 39.53 | 159 | rtx4090* | 4 | 88% |
| 18 | sn62 Ridges | 59.5 | 31.91 | 597 | rtx4090* | 44 | 15% |
| 19 | sn4 Targon | 57.6 | 9,235 | 19,806 | rtx4090* | 5 | 62% |
| 20 | sn102 ConnitoAI | 57.3 | 591 | 592 | rtx4090* | 4 | 25% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 27 |
| captured (>90%) | 22 |

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
| 2026-11-16T06:16 | sn24 | RELEASE | sn24 released v0.2.1 |
| 2026-11-16T06:16 | sn25 | RELEASE | sn25 released v2026.11.15-1100072900 |
| 2026-11-16T06:16 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge release/validator-1115-transient-wa |
| 2026-11-16T06:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6295 - [P0] Validator: a node on anot |
| 2026-11-16T06:16 | sn66 | RELEASE | sn66 released v2026.11.16.3 |
| 2026-11-16T06:16 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Admit reward statements for Hilbert 12 an |
| 2026-11-16T06:16 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: deploy gate: refuse unsafe trainer/valida |
| 2026-11-16T06:16 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Evaluation key test: the committed row r |
| 2026-11-16T06:16 | sn127 | RELEASE | sn127 released Release 26830a1 |
| 2026-11-15T23:57 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Merge pull request #161 from latent-to/cl |
| 2026-11-15T23:57 | sn25 | RELEASE | sn25 released v2026.11.15-1099862510 |
| 2026-11-15T23:57 | sn26 | BURN_DROP | sn26 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-15T23:57 | sn42 | RELEASE | sn42 released v0.6.16 |
| 2026-11-15T23:57 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: docs: the baseline was the setup of CADmi |
| 2026-11-15T23:57 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(subnet): enter Phase 1 with external |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

