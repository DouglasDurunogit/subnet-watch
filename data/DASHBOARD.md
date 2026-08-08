# Subnet watch — dashboard

_snapshot 2026-08-08T06:05:01Z · block 8797704 · run_status **ok**_

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
| New events this window | 2 | see ALARMS.md |

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
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 81.8 | 250 | 763 | cpu-small | 4 | 51% |
| 2 | sn107 Minos | 79.2 | 147 | 33,856 | cpu-small | 19 | 90% |
| 3 | sn67 Harnyx | 71.2 | 17.06 | 742 | cpu-small | 131 | 19% |
| 4 | sn91 cascade | 70.1 | 770 | 2,634 | rtx4090* | 5 | 48% |
| 5 | sn1 Apex | 69.7 | 683 | 1,572 | rtx4090* | 4 | 41% |
| 6 | sn62 Ridges | 69.1 | 564 | 2,039 | rtx4090* | 7 | 35% |
| 7 | sn15 ORO | 68.3 | 11.65 | 10,631 | cpu-small | 75 | 92% |
| 8 | sn41 Almanac | 68.3 | 8.95 | 34.34 | cpu-small | 67 | 76% |
| 9 | sn96 Verathos | 68.1 | 20.80 | 139 | rtx4090 | 72 | 42% |
| 10 | sn26 Perturb | 68.1 | 20.55 | 40.28 | rtx3060 | 11 | 50% |
| 11 | sn100 BASE | 67.2 | 321 | 1,049 | rtx4090* | 7 | 32% |
| 12 | sn124 Swarm | 65.7 | 213 | 616 | rtx4090* | 23 | 11% |
| 13 | sn21 AdTAO | 65.6 | 4.81 | 22.19 | cpu-small | 142 | 45% |
| 14 | sn80 OpenRoboto | 63.4 | 103 | 335 | rtx4090* | 4 | 91% |
| 15 | sn61 RedTeam | 62.1 | 70.16 | 187 | rtx4090* | 36 | 6% |
| 16 | sn28 gm | 62 | 68.58 | 3,807 | rtx4090* | 19 | 43% |
| 17 | sn102 ConnitoAI | 61 | 1,780 | 2,004 | rtx4090* | 4 | 39% |
| 18 | sn51 lium.io | 58.1 | 27.83 | 2,759 | rtx4090* | 44 | 68% |
| 19 | sn56 Gradients | 56.5 | 455 | 960 | rtx4090* | 7 | 70% |
| 20 | sn74 Gittensor | 56 | 13.03 | 230 | rtx4090* | 16 | 63% |

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
| 2026-08-08T05:08 | sn80 | SCORING_COMMIT | sn80 commit touches scoring: protocol+docs: champion margin 0.01, unif |
| 2026-08-08T05:08 | sn100 | RELEASE | sn100 released v3.3.8 — Design one-prompt / one-attempt / admin reject |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

