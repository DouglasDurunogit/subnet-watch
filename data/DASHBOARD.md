# Subnet watch — dashboard

_snapshot 2026-11-04T17:57:33Z · block 9434280 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 64 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **64** | income beats machine cost |
| New events this window | 19 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.6 | 2,951 | 2,951 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,931 | 3,871 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.6 | 1,609 | 1,609 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 69.5 | 636 | 1,023 | rtx4090* | 5 | 32% |
| 5 | sn14 Cacheon | 69.5 | 630 | 5,132 | rtx4090* | 3 | 80% |
| 6 | sn41 Almanac | 68.7 | 9.93 | 131 | cpu-small | 176 | 7% |
| 7 | sn56 Gradients | 68.5 | 478 | 5,150 | rtx4090* | 7 | 51% |
| 8 | sn70 Fugal | 67.8 | 388 | 1,517 | rtx4090* | 19 | 13% |
| 9 | sn1 Apex | 67.7 | 375 | 829 | rtx4090* | 4 | 68% |
| 10 | sn82 Noah | 66.5 | 401 | 457 | rtx4090* | 64 | 2% |
| 11 | sn107 Minos | 66.2 | 183 | 15,573 | cpu-small | 20 | 80% |
| 12 | sn53 engy | 65.4 | 188 | 3,262 | rtx4090 | 31 | 21% |
| 13 | sn15 ORO | 65.4 | 7.17 | 11,822 | cpu-small | 77 | 95% |
| 14 | sn67 Harnyx | 64.9 | 3.59 | 494 | cpu-small | 135 | 26% |
| 15 | sn38 ChronoLLM | 63.8 | 57.66 | 513 | cpu-small | 10 | 52% |
| 16 | sn124 Swarm | 62.9 | 99.02 | 1,889 | rtx4090* | 15 | 31% |
| 17 | sn121 sundae_bar | 62.1 | 947 | 947 = | cpu-small | 2 | 60% |
| 18 | sn62 Ridges | 61.8 | 63.17 | 1,227 | rtx4090* | 37 | 22% |
| 19 | sn55 NIOME | 61.2 | 53.06 | 452 | rtx4090* | 11 | 30% |
| 20 | sn66 conjectures | 59.9 | 36.14 | 124 | rtx4090* | 5 | 86% |

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
| dominated (60–90%) | 30 |
| captured (>90%) | 22 |

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
| 2026-11-04T17:58 | sn1 | RELEASE | sn1 released v4.7.0 |
| 2026-11-04T17:58 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Set document evaluation lower bound to 2 t |
| 2026-11-04T17:58 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.605 - miners can earn again |
| 2026-11-04T17:58 | sn28 | RELEASE | sn28 released v0.5.21 |
| 2026-11-04T17:58 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: miner: builder-sign request sends only {m |
| 2026-11-04T17:58 | sn51 | RELEASE | sn51 released executor-v1.169 |
| 2026-11-04T17:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2786 - [P2] Validator: clear the fill |
| 2026-11-04T17:58 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #190 from conjectures-i |
| 2026-11-04T17:58 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-04T17:58 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-11-04T17:58 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: docs: MINER_GUIDE: reveal bucket; no GPU  |
| 2026-11-04T17:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse verified clean text in final traini |
| 2026-11-04T17:58 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(admin): skip retired zero-cap tasks i |
| 2026-11-04T17:58 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Scope validator collateral reads to the c |
| 2026-11-04T17:58 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

