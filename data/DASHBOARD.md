# Subnet watch — dashboard

_snapshot 2026-09-24T12:41:41Z · block 9137596 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 80 | 14,434 | 26,108 | rtx4090* | 5 | 58% |
| 2 | sn3 Teutonic | 76.4 | 4,999 | 4,999 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.5 | 606 | 2,428 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 69.9 | 720 | 928 | rtx4090* | 4 | 61% |
| 5 | sn107 Minos | 68.5 | 321 | 26,628 | cpu-small | 20 | 80% |
| 6 | sn67 Harnyx | 68.4 | 8.42 | 1,112 | cpu-small | 119 | 35% |
| 7 | sn56 Gradients | 68.3 | 440 | 5,382 | rtx4090* | 10 | 40% |
| 8 | sn38 ChronoLLM | 68.2 | 184 | 1,621 | cpu-small | 10 | 52% |
| 9 | sn15 ORO | 67.4 | 9.57 | 21.05 | cpu-small | 58 | 97% |
| 10 | sn124 Swarm | 66.8 | 295 | 870 | rtx4090* | 25 | 11% |
| 11 | sn111 Claims | 65.1 | 190 | 3,015 | rtx4090* | 5 | 80% |
| 12 | sn14 Cacheon | 64.5 | 143 | 899 | rtx4090* | 11 | 50% |
| 13 | sn100 Cortex | 63 | 91.83 | 152 | rtx4090* | 11 | 70% |
| 14 | sn23 Trishool | 61.7 | 838 | 838 = | cpu-small | 2 | 80% |
| 15 | sn62 Ridges | 61.6 | 59.17 | 1,784 | rtx4090* | 20 | 21% |
| 16 | sn28 SayGM | 61.1 | 53.64 | 588 | rtx4090* | 70 | 33% |
| 17 | sn74 Gittensor | 59.1 | 35.74 | 110 | rtx4090* | 18 | 64% |
| 18 | sn26 Perturb | 58.8 | 27.54 | 46.67 | rtx3060 | 5 | 90% |
| 19 | sn61 RedTeam | 58.7 | 25.81 | 624 | rtx4090* | 119 | 7% |
| 20 | sn51 lium.io | 57.9 | 29.22 | 1,386 | rtx4090* | 67 | 84% |

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
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-24T12:42 | sn1 | RELEASE | sn1 released v4.4.9 |
| 2026-09-24T12:42 | sn9 | RELEASE | sn9 released v4.13.3 |
| 2026-09-24T12:42 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: feat: reject sources a miner could have s |
| 2026-09-24T12:42 | sn28 | RELEASE | sn28 released v0.4.21 |
| 2026-09-24T12:42 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.21 ( |
| 2026-09-24T12:42 | sn51 | RELEASE | sn51 released executor-v1.135 |
| 2026-09-24T12:42 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Validator: pull a present image when the  |
| 2026-09-24T12:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve local visible article headers in |
| 2026-09-24T06:47 | sn21 | RELEASE | sn21 released SN21 rich training data v3 (slice 2) |
| 2026-09-24T06:47 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3521 - [P1] validator: a custom build |
| 2026-09-24T06:47 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.783 - miners can earn again |
| 2026-09-24T06:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind final verifier extraction release to |
| 2026-09-24T01:35 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: rollouts.prepass: --uids-file restricts  |
| 2026-09-23T23:14 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Merge PR #66 (cursor/band-backfill-outco |
| 2026-09-23T20:35 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Drain evaluation workers and remove redun |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

