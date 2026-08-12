# Subnet watch — dashboard

_snapshot 2026-08-12T02:39:13Z · block 8825468 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 36 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.9 | 137 | 31,661 | cpu-small | 20 | 87% |
| 2 | sn76 Phylax | 76 | 56.71 | 171 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.5 | 18.37 | 765 | cpu-small | 120 | 20% |
| 4 | sn100 BASE | 71 | 1,009 | 2,027 | rtx4090* | 3 | 50% |
| 5 | sn96 Verathos | 69.8 | 31.77 | 410 | rtx4090 | 57 | 41% |
| 6 | sn91 cascade | 69.2 | 593 | 1,353 | rtx4090* | 5 | 50% |
| 7 | sn41 Almanac | 69.2 | 11.14 | 13.81 | cpu-small | 63 | 76% |
| 8 | sn62 Ridges | 69 | 553 | 2,002 | rtx4090* | 7 | 35% |
| 9 | sn56 Gradients | 69 | 553 | 1,008 | rtx4090* | 7 | 64% |
| 10 | sn26 Perturb | 68.9 | 25.16 | 176 | rtx3060 | 11 | 50% |
| 11 | sn85 Vidaio | 68.6 | 493 | 493 | rtx4090* | 10 | 16% |
| 12 | sn15 ORO | 68.3 | 10.86 | 23.13 | cpu-small | 89 | 92% |
| 13 | sn21 AdTAO | 67.7 | 7.80 | 34.91 | cpu-small | 88 | 45% |
| 14 | sn124 Swarm | 65.9 | 224 | 679 | rtx4090* | 23 | 11% |
| 15 | sn80 OpenRoboto | 64.6 | 147 | 509 | rtx4090* | 4 | 91% |
| 16 | sn38 ChronoLLM | 63.3 | 111 | 1,611 | rtx4090* | 10 | 52% |
| 17 | sn28 gm | 61.4 | 58.04 | 3,368 | rtx4090* | 24 | 33% |
| 18 | sn51 lium.io | 59.4 | 38.19 | 2,111 | rtx4090* | 52 | 72% |
| 19 | sn2 DSperse | 59.1 | 27.87 | 70.43 | rtx4090* | 16 | 83% |
| 20 | sn61 RedTeam | 59 | 27.03 | 1,771 | rtx4090* | 53 | 35% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 25 |
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
| 2026-08-12T02:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Isolate concurrent artifact verification  |
| 2026-08-11T23:54 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse artifact verification transport poo |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

