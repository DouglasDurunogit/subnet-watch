# Subnet watch — dashboard

_snapshot 2026-09-08T20:19:25Z · block 9025105 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.3 | 1,007 | 8,066 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.8 | 430 | 34,888 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 79.1 | 127 | 384 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76 | 4,486 | 4,486 = | rtx4090* | 5 | 20% |
| 5 | sn102 ConnitoAI | 71.8 | 1,262 | 1,663 | rtx4090* | 5 | 29% |
| 6 | sn67 Harnyx | 70.8 | 15.32 | 1,352 | cpu-small | 124 | 37% |
| 7 | sn96 Verathos | 70.2 | 35.47 | 550 | rtx4090 | 81 | 33% |
| 8 | sn91 cascade | 70.1 | 767 | 3,092 | rtx4090* | 5 | 52% |
| 9 | sn14 Cacheon | 69.7 | 685 | 1,268 | rtx4090* | 12 | 18% |
| 10 | sn11 TrajectoryRL | 68.7 | 6,768 | 6,768 = | cpu-small | 1 | 100% |
| 11 | sn62 Ridges | 68.2 | 427 | 1,268 | rtx4090* | 13 | 26% |
| 12 | sn56 Gradients | 67.8 | 384 | 5,955 | rtx4090* | 9 | 47% |
| 13 | sn80 OpenRoboto | 67.7 | 372 | 1,322 | rtx4090* | 5 | 43% |
| 14 | sn38 ChronoLLM | 65.9 | 99.08 | 1,354 | cpu-small | 10 | 52% |
| 15 | sn111 Claims | 65.8 | 233 | 3,508 | rtx4090* | 5 | 80% |
| 16 | sn121 sundae_bar | 63.3 | 1,345 | 1,345 = | cpu-small | 2 | 60% |
| 17 | sn28 SayGM | 62.8 | 86.79 | 5,920 | rtx4090* | 45 | 36% |
| 18 | sn65 True Performance | 62.7 | 92.94 | 194 | rtx4090* | 6 | 75% |
| 19 | sn41 Almanac | 60.7 | 42.67 | 118 | cpu-small | 84 | 3% |
| 20 | sn51 lium.io | 57.6 | 26.64 | 2,752 | rtx4090* | 65 | 80% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 21 |
| captured (>90%) | 19 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-08T20:19 | sn2 | RELEASE | sn2 released 14.14.3 |
| 2026-09-08T20:19 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Introduce weight commit guard for epochs w |
| 2026-09-08T20:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-08T20:19 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Fix bootstrap image revision validation |
| 2026-09-08T20:19 | sn96 | RELEASE | sn96 released Verathos v0.2.2 – Consistent Validator Decisions and Mic |
| 2026-09-08T17:34 | sn25 | RELEASE | sn25 released v2026.9.8-1040779940 |
| 2026-09-08T17:34 | sn34 | BURN_DROP | sn34 burn fell 1.000 -> 0.799 - miners can earn again |
| 2026-09-08T17:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-08T17:34 | sn74 | RELEASE | sn74 released release-20260908-144557 |
| 2026-09-08T17:34 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: tracks: support is the one live track; ca |
| 2026-09-08T17:34 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Sync validator + eval design (2026-09-07 |
| 2026-09-08T17:34 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.610 - miners can earn again |
| 2026-09-08T13:32 | sn9 | RELEASE | sn9 released v4.12.14 |
| 2026-09-08T13:32 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: Merge pull request #145 from Pareton-ai/b |
| 2026-09-08T13:32 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Bump version to 5.0.2 so validators autou |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

