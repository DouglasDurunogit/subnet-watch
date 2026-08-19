# Subnet watch — dashboard

_snapshot 2026-08-19T04:06:53Z · block 8876304 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.1 | 97.37 | 188 | cpu-small | 10 | 20% |
| 2 | sn67 Harnyx | 71.8 | 19.97 | 426 | cpu-small | 140 | 13% |
| 3 | sn26 Perturb | 70.7 | 39.34 | 336 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.1 | 772 | 1,045 | rtx4090* | 4 | 55% |
| 5 | sn56 Gradients | 69.4 | 615 | 924 | rtx4090* | 5 | 72% |
| 6 | sn91 cascade | 69.1 | 572 | 2,313 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 68.8 | 12.96 | 15,270 | cpu-small | 68 | 94% |
| 8 | sn38 ChronoLLM | 67.4 | 143 | 3,032 | cpu-small | 10 | 52% |
| 9 | sn41 Almanac | 65.9 | 5.05 | 35.76 | cpu-small | 75 | 81% |
| 10 | sn96 Verathos | 65.2 | 10.38 | 339 | rtx4090 | 92 | 41% |
| 11 | sn107 Minos | 64.1 | 112 | 33,208 | cpu-small | 20 | 90% |
| 12 | sn21 AdTAO | 64.1 | 3.47 | 715 | cpu-small | 16 | 37% |
| 13 | sn98 NeverPlayAlone | 64 | 1,644 | 1,644 = | cpu-small | 1 | 100% |
| 14 | sn85 Vidaio | 63.8 | 117 | 368 | rtx4090* | 13 | 42% |
| 15 | sn53 engy | 62.8 | 85.83 | 2,028 | rtx4090 | 144 | 11% |
| 16 | sn81 Reliquary | 61.8 | 63.39 | 193 | rtx4090* | 48 | 12% |
| 17 | sn55 NIOME | 61.3 | 54.67 | 463 | rtx4090* | 11 | 29% |
| 18 | sn51 lium.io | 60.3 | 48.25 | 1,096 | rtx4090* | 55 | 78% |
| 19 | sn102 ConnitoAI | 58.8 | 903 | 2,040 | rtx4090* | 6 | 38% |
| 20 | sn28 gm | 57.6 | 19.22 | 2,200 | rtx4090* | 41 | 26% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 15 |
| captured (>90%) | 30 |

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
| 2026-08-19T03:08 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Merge pull request #20 from instant-subne |
| 2026-08-19T03:08 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.607 - miners can earn again |
| 2026-08-19T01:50 | sn14 | BURN_DROP | sn14 burn fell 1.000 -> 0.298 - miners can earn again |
| 2026-08-19T01:50 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Merge pull request #18 from instant-subne |
| 2026-08-19T01:50 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Isolate parity scoring cache |
| 2026-08-19T01:50 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix validator batch reliability and prov |
| 2026-08-19T00:01 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: test: freeze validator report contract |
| 2026-08-18T23:03 | sn62 | RELEASE | sn62 released v0.2.9 |
| 2026-08-18T22:37 | sn28 | RELEASE | sn28 released v0.4.6-dev |
| 2026-08-18T22:37 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Release gm-miner v0.4.6-dev |
| 2026-08-18T22:37 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-08-18T22:37 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: pass pre_screening_policy_version and rem |
| 2026-08-18T21:35 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify restored parity database contract |
| 2026-08-18T21:04 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(weights): burn to this validator's ow |
| 2026-08-18T20:36 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.838 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

