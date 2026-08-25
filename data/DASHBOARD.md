# Subnet watch — dashboard

_snapshot 2026-08-25T05:04:13Z · block 8919790 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 79.6 | 146 | 217 | cpu-small | 13 | 20% |
| 2 | sn3 Teutonic | 76 | 4,435 | 4,435 = | rtx4090* | 5 | 20% |
| 3 | sn62 Ridges | 72.4 | 1,525 | 3,117 | rtx4090* | 6 | 39% |
| 4 | sn38 ChronoLLM | 72.4 | 602 | 3,535 | cpu-small | 6 | 53% |
| 5 | sn23 Trishool | 72.2 | 555 | 555 = | cpu-small | 2 | 80% |
| 6 | sn67 Harnyx | 71.8 | 20.30 | 465 | cpu-small | 131 | 12% |
| 7 | sn15 ORO | 71 | 25.32 | 43.19 | cpu-small | 83 | 92% |
| 8 | sn91 cascade | 68.9 | 537 | 1,445 | rtx4090* | 5 | 52% |
| 9 | sn26 Perturb | 67.8 | 19.45 | 276 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 67.7 | 19.02 | 203 | rtx4090 | 97 | 40% |
| 11 | sn21 AdTAO | 66.7 | 6.53 | 601 | cpu-small | 16 | 45% |
| 12 | sn1 Apex | 66.6 | 266 | 2,164 | rtx4090* | 4 | 52% |
| 13 | sn124 Swarm | 66 | 236 | 2,063 | rtx4090* | 26 | 24% |
| 14 | sn92 MicroTensor | 65.5 | 77.08 | 124 | cpu-small | 3 | 95% |
| 15 | sn107 Minos | 65.3 | 151 | 43,306 | cpu-small | 20 | 90% |
| 16 | sn85 Vidaio | 64.5 | 142 | 437 | rtx4090* | 13 | 42% |
| 17 | sn81 Reliquary | 64 | 122 | 376 | rtx4090* | 33 | 8% |
| 18 | sn108 Prometheon | 63.4 | 103 | 119 | rtx4090* | 9 | 66% |
| 19 | sn51 lium.io | 60.8 | 55.81 | 2,589 | rtx4090* | 54 | 77% |
| 20 | sn53 engy | 60.1 | 37.30 | 317 | rtx4090 | 144 | 63% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 18 |
| captured (>90%) | 25 |

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
| 2026-08-25T05:04 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify parity bundle through exact empty  |
| 2026-08-25T03:09 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #109 from leadpoet/cod |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

