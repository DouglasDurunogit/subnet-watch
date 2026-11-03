# Subnet watch — dashboard

_snapshot 2026-11-03T22:26:45Z · block 9428428 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 14 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 88 | 1,189 | 7,733 | cpu-small | 7 | 65% |
| 2 | sn120 Affine | 74.5 | 2,822 | 2,822 = | rtx4090* | 10 | 10% |
| 3 | sn97 Ingot | 72.5 | 1,580 | 1,580 = | rtx4090* | 5 | 20% |
| 4 | sn14 Cacheon | 69.5 | 633 | 5,156 | rtx4090* | 3 | 80% |
| 5 | sn103 Terza Inference | 68 | 413 | 1,362 | rtx4090* | 5 | 36% |
| 6 | sn1 Apex | 67.9 | 396 | 798 | rtx4090* | 4 | 67% |
| 7 | sn53 engy | 67.6 | 357 | 2,010 | rtx4090 | 29 | 26% |
| 8 | sn67 Harnyx | 67.3 | 6.30 | 80.46 | cpu-small | 148 | 4% |
| 9 | sn56 Gradients | 67 | 301 | 4,972 | rtx4090* | 7 | 51% |
| 10 | sn15 ORO | 66.5 | 6.62 | 11,436 | cpu-small | 76 | 95% |
| 11 | sn82 Noah | 66.4 | 403 | 442 | rtx4090* | 64 | 2% |
| 12 | sn107 Minos | 66 | 176 | 15,018 | cpu-small | 20 | 80% |
| 13 | sn102 ConnitoAI | 65.1 | 171 | 948 | rtx4090* | 8 | 27% |
| 14 | sn38 ChronoLLM | 63.6 | 54.98 | 490 | cpu-small | 10 | 52% |
| 15 | sn124 Swarm | 62.2 | 80.39 | 1,827 | rtx4090* | 15 | 31% |
| 16 | sn121 sundae_bar | 62 | 914 | 914 = | cpu-small | 2 | 60% |
| 17 | sn62 Ridges | 61.6 | 59.61 | 1,410 | rtx4090* | 36 | 25% |
| 18 | sn3 Teutonic | 61.2 | 1,873 | 3,755 | rtx4090* | 7 | 25% |
| 19 | sn117 everyframe.studi | 60.8 | 47.77 | 92.10 | rtx4090* | 15 | 80% |
| 20 | sn111 Claims | 58.6 | 24.59 | 2,452 | rtx4090* | 6 | 90% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 28 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-03T22:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/validator-ledger-startup-prefix |
| 2026-11-03T22:27 | sn28 | RELEASE | sn28 released v0.5.19-dev |
| 2026-11-03T22:27 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5635 - [P1] Validator: hide an unreac |
| 2026-11-03T22:27 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: fix(validator): keep a proof's JSON numbe |
| 2026-11-03T22:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #988 from leadpoet/fea |
| 2026-11-03T22:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge PR #503: reuse completed work and p |
| 2026-11-03T22:27 | sn78 | README_TASK_DIFF | sn78 README task/scoring sections changed |
| 2026-11-03T22:27 | sn82 | README_TASK_DIFF | sn82 README task/scoring sections changed |
| 2026-11-03T22:27 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(trainer): carry infra-failed challeng |
| 2026-11-03T22:27 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Neuron 1.0.1: when the challenge server  |
| 2026-11-03T22:27 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Separate competition intake from sequent |
| 2026-11-03T22:27 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Kit local scorer: a thin caller of the o |
| 2026-11-03T22:27 | sn126 | BURN_DROP | sn126 burn fell 1.000 -> 0.956 - miners can earn again |
| 2026-11-03T22:27 | sn127 | README_TASK_DIFF | sn127 README task/scoring sections changed |
| 2026-11-03T17:17 | sn1 | RELEASE | sn1 released v4.6.3 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

