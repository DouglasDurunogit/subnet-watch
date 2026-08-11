# Subnet watch — dashboard

_snapshot 2026-08-11T22:57:58Z · block 8824369 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 36 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 110 | 31,713 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.5 | 64.28 | 194 | cpu-small | 10 | 34% |
| 3 | sn100 BASE | 70.9 | 958 | 1,925 | rtx4090* | 3 | 50% |
| 4 | sn67 Harnyx | 70.4 | 13.81 | 799 | cpu-small | 151 | 21% |
| 5 | sn96 Verathos | 70.1 | 34.16 | 469 | rtx4090 | 48 | 41% |
| 6 | sn91 cascade | 69.1 | 563 | 1,285 | rtx4090* | 5 | 50% |
| 7 | sn41 Almanac | 69.1 | 10.61 | 22.75 | cpu-small | 68 | 72% |
| 8 | sn62 Ridges | 68.9 | 536 | 1,940 | rtx4090* | 7 | 35% |
| 9 | sn85 Vidaio | 68.7 | 502 | 502 = | rtx4090* | 10 | 16% |
| 10 | sn26 Perturb | 68.7 | 24.37 | 176 | rtx3060 | 11 | 50% |
| 11 | sn15 ORO | 68.1 | 10.58 | 22.35 | cpu-small | 89 | 92% |
| 12 | sn21 AdTAO | 67.6 | 7.54 | 33.85 | cpu-small | 88 | 45% |
| 13 | sn56 Gradients | 66.6 | 272 | 982 | rtx4090* | 8 | 72% |
| 14 | sn124 Swarm | 65.8 | 218 | 662 | rtx4090* | 23 | 11% |
| 15 | sn80 OpenRoboto | 64.6 | 148 | 540 | rtx4090* | 4 | 91% |
| 16 | sn38 ChronoLLM | 63.2 | 108 | 1,569 | rtx4090* | 10 | 52% |
| 17 | sn28 gm | 61.5 | 59.21 | 2,782 | rtx4090* | 25 | 28% |
| 18 | sn51 lium.io | 59.4 | 37.97 | 2,581 | rtx4090* | 52 | 70% |
| 19 | sn2 DSperse | 59.1 | 27.69 | 86.93 | rtx4090* | 13 | 83% |
| 20 | sn61 RedTeam | 58.8 | 25.39 | 1,699 | rtx4090* | 53 | 35% |

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
| dominated (60–90%) | 19 |
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
| 2026-08-11T22:58 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: update validator api changes |
| 2026-08-11T19:50 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse bounded artifact verification sessi |
| 2026-08-11T18:27 | sn74 | RELEASE | sn74 released release-20260811-182518: chore(weights): drop the linked |
| 2026-08-11T18:27 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: one submission counter for both signe |
| 2026-08-11T17:27 | sn9 | BURN_DROP | sn9 burn fell 1.000 -> 0.950 - miners can earn again |
| 2026-08-11T17:27 | sn28 | RELEASE | sn28 released v0.4.3-dev |
| 2026-08-11T17:27 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #51 from score-technol |
| 2026-08-11T17:27 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: fix: update max 24h miner payout test to  |
| 2026-08-11T17:27 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.635 - miners can earn again |
| 2026-08-11T16:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Seed required miner in Git-tree rehearsal |
| 2026-08-11T16:24 | sn100 | RELEASE | sn100 released v3.3.18 — design tip-emit from latest scored round only |
| 2026-08-11T15:13 | sn1 | RELEASE | sn1 released v4.2.22 |
| 2026-08-11T15:13 | sn28 | RELEASE | sn28 released v0.4.2-dev |
| 2026-08-11T15:13 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Improve Silver adjudication and scoring |
| 2026-08-11T15:13 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge per-process validator session and  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

