# Subnet watch — dashboard

_snapshot 2026-08-08T03:59:11Z · block 8797075 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 11 | `██████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 82.8 | 323 | 602 | cpu-small | 4 | 40% |
| 2 | sn107 Minos | 78.5 | 122 | 33,992 | cpu-small | 20 | 90% |
| 3 | sn67 Harnyx | 71.3 | 17.13 | 746 | cpu-small | 129 | 19% |
| 4 | sn91 cascade | 70.2 | 783 | 2,606 | rtx4090* | 5 | 47% |
| 5 | sn1 Apex | 69.8 | 692 | 1,593 | rtx4090* | 4 | 41% |
| 6 | sn62 Ridges | 69.1 | 567 | 2,051 | rtx4090* | 7 | 35% |
| 7 | sn15 ORO | 68.6 | 11.77 | 10,665 | cpu-small | 74 | 93% |
| 8 | sn41 Almanac | 68.4 | 9.03 | 34.48 | cpu-small | 67 | 76% |
| 9 | sn26 Perturb | 68.1 | 20.67 | 40.46 | rtx3060 | 11 | 50% |
| 10 | sn96 Verathos | 67.4 | 17.49 | 161 | rtx4090 | 76 | 42% |
| 11 | sn100 BASE | 67.2 | 324 | 1,060 | rtx4090* | 7 | 32% |
| 12 | sn124 Swarm | 65.7 | 215 | 621 | rtx4090* | 23 | 11% |
| 13 | sn21 AdTAO | 65.6 | 4.83 | 22.28 | cpu-small | 142 | 45% |
| 14 | sn61 RedTeam | 62.2 | 70.73 | 187 | rtx4090* | 36 | 6% |
| 15 | sn28 gm | 62.1 | 70.26 | 3,937 | rtx4090* | 18 | 44% |
| 16 | sn102 ConnitoAI | 59 | 971 | 1,706 | rtx4090* | 6 | 31% |
| 17 | sn51 lium.io | 58.5 | 30.51 | 2,768 | rtx4090* | 44 | 69% |
| 18 | sn56 Gradients | 56.5 | 457 | 964 | rtx4090* | 7 | 70% |
| 19 | sn74 Gittensor | 56.1 | 13.42 | 231 | rtx4090* | 16 | 63% |
| 20 | sn2 DSperse | 55.2 | 8.06 | 154 | rtx4090* | 12 | 83% |

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
| wide (<30%) | 21 |
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
| 2026-08-07T23:45 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(validator): note proxy requires vali |
| 2026-08-07T22:54 | sn61 | RELEASE | sn61 released 4.9.1 |
| 2026-08-07T22:54 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update bot virus challenge dependen |
| 2026-08-07T21:11 | sn28 | RELEASE | sn28 released v0.4.1 |
| 2026-08-07T20:24 | sn1 | RELEASE | sn1 released v4.2.21 |
| 2026-08-07T20:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Fix A10 GPU model normalization in valida |
| 2026-08-07T19:28 | sn28 | RELEASE | sn28 released v0.4.0 |
| 2026-08-07T19:28 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: removed Chutes for miner submission |
| 2026-08-07T19:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Authorize isolated autoresearch validatio |
| 2026-08-07T18:10 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: refactor(scoring): one behavioural detect |
| 2026-08-07T17:22 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): wire the anti-clone layers |
| 2026-08-07T17:22 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Add localnet miner validator and platform |
| 2026-08-07T17:22 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.828 - miners can earn again |
| 2026-08-07T16:08 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): bind the medoid closure exp |
| 2026-08-07T16:08 | sn74 | RELEASE | sn74 released release-20260807-154750 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

