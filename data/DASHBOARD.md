# Subnet watch — dashboard

_snapshot 2026-09-26T11:22:15Z · block 9151599 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 72.9 | 679 | 2,718 | cpu-small | 5 | 52% |
| 2 | sn1 Apex | 71.5 | 1,155 | 1,182 | rtx4090* | 4 | 53% |
| 3 | sn56 Gradients | 71.2 | 1,075 | 6,171 | rtx4090* | 8 | 41% |
| 4 | sn38 ChronoLLM | 69.9 | 300 | 2,635 | cpu-small | 10 | 52% |
| 5 | sn67 Harnyx | 69.5 | 10.52 | 1,352 | cpu-small | 118 | 37% |
| 6 | sn15 ORO | 69 | 13.83 | 22,220 | cpu-small | 63 | 96% |
| 7 | sn107 Minos | 68.9 | 357 | 31,662 | cpu-small | 20 | 80% |
| 8 | sn4 Targon | 68.5 | 16,394 | 29,652 | rtx4090* | 5 | 58% |
| 9 | sn14 Cacheon | 68.4 | 453 | 2,549 | rtx4090* | 13 | 30% |
| 10 | sn124 Swarm | 67.2 | 339 | 978 | rtx4090* | 25 | 11% |
| 11 | sn111 Claims | 67.1 | 332 | 2,965 | rtx4090* | 5 | 70% |
| 12 | sn96 Verathos | 67.1 | 17.14 | 259 | rtx4090 | 75 | 30% |
| 13 | sn3 Teutonic | 64.9 | 5,602 | 5,602 = | rtx4090* | 5 | 20% |
| 14 | sn28 SayGM | 64.3 | 138 | 1,114 | rtx4090* | 59 | 24% |
| 15 | sn62 Ridges | 63.4 | 102 | 1,386 | rtx4090* | 24 | 14% |
| 16 | sn23 Trishool | 62.3 | 997 | 997 = | cpu-small | 2 | 80% |
| 17 | sn26 Perturb | 61.5 | 60.47 | 60.47 = | rtx3060 | 5 | 90% |
| 18 | sn100 Cortex | 60.1 | 38.21 | 258 | rtx4090* | 19 | 70% |
| 19 | sn51 lium.io | 59.1 | 39.77 | 2,953 | rtx4090* | 70 | 75% |
| 20 | sn74 Gittensor | 59.1 | 31.95 | 299 | rtx4090* | 17 | 63% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 21 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-26T11:22 | sn25 | README_TASK_DIFF | sn25 README task/scoring sections changed |
| 2026-09-26T11:22 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected verifier manifest to alias |
| 2026-09-26T11:22 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: wvk 25 scoring bundle STAGED (all knobs  |
| 2026-09-26T06:07 | sn62 | RELEASE | sn62 released v0.3.7 |
| 2026-09-26T06:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow focused validation of saved Arena o |
| 2026-09-25T22:43 | sn1 | RELEASE | sn1 released v4.4.10 |
| 2026-09-25T19:26 | sn15 | RELEASE | sn15 released v2.0.31: fix(proxy): re-resolve Backend host for allowli |
| 2026-09-25T19:26 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: refactor(validator): simplify session cal |
| 2026-09-25T19:26 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve terminal verified intent evidenc |
| 2026-09-25T19:26 | sn74 | RELEASE | sn74 released release-20260925-183535 |
| 2026-09-25T19:26 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: test(network): verify opentype 75/25 sea |
| 2026-09-25T15:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: competition: clarify staging finalization |
| 2026-09-25T15:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3467 - [P2] validator: inspect after  |
| 2026-09-25T15:24 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Withhold a miner's source while it is on  |
| 2026-09-25T15:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified activity repair to committe |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

