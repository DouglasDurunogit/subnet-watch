# Subnet watch — dashboard

_snapshot 2026-11-04T23:36:19Z · block 9435973 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 10 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.6 | 2,956 | 2,956 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,940 | 3,793 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.6 | 1,599 | 1,599 = | rtx4090* | 5 | 20% |
| 4 | sn14 Cacheon | 69.5 | 629 | 5,118 | rtx4090* | 3 | 80% |
| 5 | sn58 Attune | 68.7 | 508 | 818 | rtx4090* | 5 | 70% |
| 6 | sn103 Terza Inference | 68.7 | 505 | 1,120 | rtx4090* | 5 | 38% |
| 7 | sn56 Gradients | 68.5 | 478 | 5,141 | rtx4090* | 7 | 51% |
| 8 | sn41 Almanac | 68.5 | 9.48 | 130 | cpu-small | 177 | 7% |
| 9 | sn1 Apex | 67.6 | 364 | 833 | rtx4090* | 4 | 69% |
| 10 | sn15 ORO | 67 | 7.26 | 11,954 | cpu-small | 77 | 95% |
| 11 | sn82 Noah | 66.5 | 399 | 454 | rtx4090* | 64 | 2% |
| 12 | sn107 Minos | 66.2 | 183 | 15,532 | cpu-small | 20 | 80% |
| 13 | sn70 Fugal | 65.8 | 211 | 534 | rtx4090* | 45 | 5% |
| 14 | sn53 engy | 65.3 | 182 | 3,164 | rtx4090 | 31 | 21% |
| 15 | sn67 Harnyx | 65.1 | 3.58 | 492 | cpu-small | 139 | 26% |
| 16 | sn102 ConnitoAI | 65 | 166 | 1,478 | rtx4090* | 9 | 44% |
| 17 | sn38 ChronoLLM | 63.5 | 53.53 | 477 | cpu-small | 10 | 52% |
| 18 | sn124 Swarm | 62.9 | 98.22 | 1,875 | rtx4090* | 15 | 31% |
| 19 | sn62 Ridges | 61.8 | 62.82 | 1,221 | rtx4090* | 37 | 22% |
| 20 | sn55 NIOME | 61.2 | 52.62 | 448 | rtx4090* | 11 | 30% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 27 |
| captured (>90%) | 24 |

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
| 2026-11-04T23:36 | sn12 | RELEASE | sn12 released sdk-v0.0.20: feat: local executor and local bind mount v |
| 2026-11-04T23:36 | sn58 | SCORING_COMMIT | sn58 commit touches scoring: feat(validator): only a permitted Hub acc |
| 2026-11-04T23:36 | sn58 | README_TASK_DIFF | sn58 README task/scoring sections changed |
| 2026-11-04T23:36 | sn70 | RELEASE | sn70 released image-v2026.11.05 |
| 2026-11-04T23:36 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Pin reviewed scorer checkpoint imports in |
| 2026-11-04T23:36 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(admin): deliver evaluation files to t |
| 2026-11-04T23:36 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: local-gsm8k: a reply over 100 KB is pass |
| 2026-11-04T17:58 | sn1 | RELEASE | sn1 released v4.7.0 |
| 2026-11-04T17:58 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Set document evaluation lower bound to 2 t |
| 2026-11-04T17:58 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.605 - miners can earn again |
| 2026-11-04T17:58 | sn28 | RELEASE | sn28 released v0.5.21 |
| 2026-11-04T17:58 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: miner: builder-sign request sends only {m |
| 2026-11-04T17:58 | sn51 | RELEASE | sn51 released executor-v1.169 |
| 2026-11-04T17:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2786 - [P2] Validator: clear the fill |
| 2026-11-04T17:58 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #190 from conjectures-i |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

