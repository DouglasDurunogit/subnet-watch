# Subnet watch — dashboard

_snapshot 2026-08-25T01:48:51Z · block 8918813 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 87 | `miner_burn` < 0.99 |
| Ranked | 87 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 41 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 79.3 | 134 | 199 | cpu-small | 13 | 20% |
| 2 | sn3 Teutonic | 76 | 4,372 | 4,372 = | rtx4090* | 5 | 20% |
| 3 | sn62 Ridges | 72.4 | 1,508 | 3,082 | rtx4090* | 6 | 39% |
| 4 | sn38 ChronoLLM | 72.3 | 584 | 3,428 | cpu-small | 6 | 53% |
| 5 | sn67 Harnyx | 71.7 | 19.18 | 165 | cpu-small | 175 | 4% |
| 6 | sn15 ORO | 71.4 | 25.46 | 43.09 | cpu-small | 82 | 92% |
| 7 | sn102 ConnitoAI | 69.4 | 627 | 2,709 | rtx4090* | 7 | 38% |
| 8 | sn91 cascade | 68.9 | 532 | 1,433 | rtx4090* | 5 | 52% |
| 9 | sn26 Perturb | 67.7 | 19.13 | 272 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 67.6 | 18.56 | 203 | rtx4090 | 94 | 40% |
| 11 | sn124 Swarm | 66 | 235 | 2,055 | rtx4090* | 26 | 24% |
| 12 | sn107 Minos | 65.7 | 164 | 42,827 | cpu-small | 19 | 90% |
| 13 | sn92 MicroTensor | 65.4 | 73.33 | 118 | cpu-small | 3 | 95% |
| 14 | sn21 AdTAO | 65.3 | 5.15 | 492 | cpu-small | 16 | 37% |
| 15 | sn85 Vidaio | 64.9 | 160 | 433 | rtx4090* | 13 | 42% |
| 16 | sn81 Reliquary | 63.8 | 116 | 340 | rtx4090* | 34 | 7% |
| 17 | sn108 Prometheon | 63.3 | 102 | 118 | rtx4090* | 9 | 66% |
| 18 | sn51 lium.io | 60.1 | 46.59 | 2,730 | rtx4090* | 53 | 75% |
| 19 | sn53 engy | 60 | 37.06 | 316 | rtx4090 | 144 | 63% |
| 20 | sn28 gm | 57.5 | 19.14 | 2,562 | rtx4090* | 58 | 21% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-25T01:49 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: revert: guarded title-corroboration was u |
| 2026-08-24T23:04 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Normalize verifier image source permissio |
| 2026-08-24T22:40 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-24T22:40 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: ♻️ refactor(validator): drop the redunda |
| 2026-08-24T21:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow bounded measured dev evaluation pay |
| 2026-08-24T21:15 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Correct the validator setup path end to e |
| 2026-08-24T19:54 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Enforce ordered evaluations |
| 2026-08-24T19:10 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-24T19:10 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF board: read the live tail, so a miner  |
| 2026-08-24T18:16 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): retire the no-zero-for-mis |
| 2026-08-24T18:16 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: Merge pull request #44 from Bitsec-AI/fea |
| 2026-08-24T18:16 | sn92 | BURN_DROP | sn92 burn fell 1.000 -> 0.971 - miners can earn again |
| 2026-08-24T17:42 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Rename the office challenge family to cf |
| 2026-08-24T17:42 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |
| 2026-08-24T16:53 | sn11 | RELEASE | sn11 released v0.6.34 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

