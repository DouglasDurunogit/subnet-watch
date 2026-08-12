# Subnet watch — dashboard

_snapshot 2026-08-12T11:33:33Z · block 8828138 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.1 | 112 | 32,620 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.5 | 63.96 | 194 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.4 | 18.16 | 756 | cpu-small | 131 | 20% |
| 4 | sn91 cascade | 70.1 | 770 | 2,635 | rtx4090* | 5 | 50% |
| 5 | sn114 SOMA | 69.7 | 679 | 1,709 | rtx4090* | 4 | 65% |
| 6 | sn41 Almanac | 69.1 | 10.63 | 23.59 | cpu-small | 69 | 72% |
| 7 | sn62 Ridges | 69 | 557 | 2,016 | rtx4090* | 7 | 35% |
| 8 | sn56 Gradients | 69 | 547 | 1,001 | rtx4090* | 7 | 64% |
| 9 | sn96 Verathos | 69 | 25.79 | 398 | rtx4090 | 68 | 41% |
| 10 | sn100 BASE | 68.7 | 510 | 2,065 | rtx4090* | 5 | 51% |
| 11 | sn26 Perturb | 67.8 | 19.46 | 37.11 | rtx3060 | 11 | 50% |
| 12 | sn15 ORO | 67.6 | 10.11 | 13,231 | cpu-small | 64 | 95% |
| 13 | sn21 AdTAO | 67.6 | 7.65 | 34.27 | cpu-small | 88 | 45% |
| 14 | sn124 Swarm | 65.8 | 224 | 678 | rtx4090* | 23 | 11% |
| 15 | sn85 Vidaio | 65.2 | 177 | 650 | rtx4090* | 10 | 21% |
| 16 | sn38 ChronoLLM | 64.7 | 163 | 3,551 | rtx4090* | 10 | 52% |
| 17 | sn80 OpenRoboto | 64.7 | 152 | 553 | rtx4090* | 4 | 91% |
| 18 | sn28 gm | 62.2 | 74.11 | 2,686 | rtx4090* | 29 | 26% |
| 19 | sn102 ConnitoAI | 60 | 1,291 | 2,019 | rtx4090* | 5 | 32% |
| 20 | sn2 DSperse | 59.6 | 32.58 | 88.58 | rtx4090* | 14 | 83% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 18 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-12T11:33 | sn51 | RELEASE | sn51 released executor-v1.117 |
| 2026-08-12T10:34 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: add audio validation for competitions (#1 |
| 2026-08-12T10:34 | sn100 | RELEASE | sn100 released v3.3.21 — Prism Lium single-GPU hard-reject (#129) |
| 2026-08-12T09:22 | sn96 | RELEASE | sn96 released Verathos v0.1.36 — Runtime and Capacity Stability |
| 2026-08-12T07:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Recover artifact verification from stale  |
| 2026-08-12T06:05 | sn100 | RELEASE | sn100 released v3.3.19 — design auto-enqueue + migration 0019 fix |
| 2026-08-12T06:05 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: Merge pull request #120 from BaseIntelli |
| 2026-08-12T02:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Isolate concurrent artifact verification  |
| 2026-08-11T23:54 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse artifact verification transport poo |
| 2026-08-11T22:58 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: update validator api changes |
| 2026-08-11T19:50 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse bounded artifact verification sessi |
| 2026-08-11T18:27 | sn74 | RELEASE | sn74 released release-20260811-182518: chore(weights): drop the linked |
| 2026-08-11T18:27 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: one submission counter for both signe |
| 2026-08-11T17:27 | sn9 | BURN_DROP | sn9 burn fell 1.000 -> 0.950 - miners can earn again |
| 2026-08-11T17:27 | sn28 | RELEASE | sn28 released v0.4.3-dev |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

