# Subnet watch — dashboard

_snapshot 2026-08-12T09:21:36Z · block 8827479 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 5 | `███` |
| 0.2–0.4 | 7 | `████` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.7 | 107 | 32,910 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.5 | 64.29 | 194 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.4 | 18.19 | 757 | cpu-small | 130 | 20% |
| 4 | sn91 cascade | 70.1 | 766 | 2,622 | rtx4090* | 5 | 50% |
| 5 | sn96 Verathos | 70.1 | 34.34 | 399 | rtx4090 | 55 | 41% |
| 6 | sn41 Almanac | 69.1 | 10.63 | 23.59 | cpu-small | 69 | 72% |
| 7 | sn62 Ridges | 69 | 552 | 1,996 | rtx4090* | 7 | 35% |
| 8 | sn56 Gradients | 69 | 548 | 1,002 | rtx4090* | 7 | 64% |
| 9 | sn85 Vidaio | 68.6 | 490 | 490 = | rtx4090* | 10 | 16% |
| 10 | sn26 Perturb | 67.9 | 19.99 | 37.86 | rtx3060 | 11 | 50% |
| 11 | sn15 ORO | 67.8 | 10.10 | 13,225 | cpu-small | 64 | 95% |
| 12 | sn21 AdTAO | 67.6 | 7.60 | 34.10 | cpu-small | 88 | 45% |
| 13 | sn124 Swarm | 65.9 | 226 | 686 | rtx4090* | 23 | 11% |
| 14 | sn38 ChronoLLM | 64.7 | 163 | 3,558 | rtx4090* | 10 | 52% |
| 15 | sn80 OpenRoboto | 64.7 | 150 | 547 | rtx4090* | 4 | 91% |
| 16 | sn28 gm | 62.9 | 90.91 | 2,294 | rtx4090* | 29 | 33% |
| 17 | sn2 DSperse | 59.5 | 31.16 | 89.78 | rtx4090* | 13 | 83% |
| 18 | sn61 RedTeam | 59.1 | 27.60 | 1,762 | rtx4090* | 52 | 35% |
| 19 | sn51 lium.io | 58.5 | 30.74 | 2,065 | rtx4090* | 52 | 73% |
| 20 | sn74 Gittensor | 58.5 | 25.80 | 220 | rtx4090* | 13 | 63% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

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
| 2026-08-11T17:27 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #51 from score-technol |
| 2026-08-11T17:27 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: fix: update max 24h miner payout test to  |
| 2026-08-11T17:27 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.635 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

