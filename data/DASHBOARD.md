# Subnet watch — dashboard

_snapshot 2026-08-01T21:07:04Z · block 8751826 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 32 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85 | 566 | 566 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.3 | 94.25 | 27,981 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.1 | 74.56 | 150 | cpu-small | 7 | 70% |
| 4 | sn67 Harnyx | 72.9 | 26.22 | 957 | cpu-small | 132 | 21% |
| 5 | sn62 Ridges | 71.2 | 1,044 | 4,806 | rtx4090* | 6 | 57% |
| 6 | sn102 ConnitoAI | 70.7 | 900 | 973 | rtx4090* | 6 | 26% |
| 7 | sn26 Perturb | 69.8 | 31.55 | 928 | rtx3060 | 11 | 51% |
| 8 | sn56 Gradients | 69.2 | 575 | 1,212 | rtx4090* | 6 | 64% |
| 9 | sn85 Vidaio | 68.5 | 470 | 495 | rtx4090* | 10 | 16% |
| 10 | sn15 ORO | 67.9 | 9.47 | 18.87 | cpu-small | 65 | 94% |
| 11 | sn124 Swarm | 66 | 231 | 676 | rtx4090* | 20 | 12% |
| 12 | sn38 ChronoLLM | 63.2 | 108 | 1,565 | rtx4090* | 10 | 52% |
| 13 | sn53 engy | 63.1 | 95.23 | 2,388 | rtx4090 | 34 | 13% |
| 14 | sn71 Leadpoet | 62.6 | 81.49 | 165 | rtx4090* | 10 | 70% |
| 15 | sn28 gm | 61.4 | 57.30 | 2,203 | rtx4090* | 14 | 55% |
| 16 | sn101 Tag101 | 58.9 | 0.12 | 1.07 | cpu-small | 243 | 90% |
| 17 | sn61 RedTeam | 58.4 | 22.55 | 90.07 | rtx4090* | 97 | 3% |
| 18 | sn51 lium.io | 55 | 14.03 | 6,683 | rtx4090* | 41 | 41% |
| 19 | sn9 iota | 54.8 | 7,102 | 12,906 | rtx4090* | 3 | 65% |
| 20 | sn99 Thirty Spokes | 52.9 | 3,226 | 3,226 = | rtx4090* | 1 | 100% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 23 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-01T21:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix baseline replay and compact weight va |
| 2026-08-01T21:07 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Wire production Silver run metadata into |
| 2026-08-01T20:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh validator ancestry workflow manif |
| 2026-08-01T17:45 | sn99 | BURN_DROP | sn99 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-01T16:29 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Wire silver adjudication into validator  |
| 2026-08-01T14:06 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Fly next-epoch seeds for pre-evaluation  |
| 2026-08-01T12:13 | sn103 | RELEASE | sn103 released v2007 |
| 2026-08-01T12:13 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: release v2007 |
| 2026-08-01T11:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind v8 artifact verification into protec |
| 2026-08-01T09:32 | sn61 | RELEASE | sn61 released 4.8.2 |
| 2026-08-01T09:32 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: set default value for user_id in _co |
| 2026-08-01T09:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-01T09:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate concurrent restart state continu |
| 2026-08-01T09:32 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: docs: introduce Poker44 evaluation netwo |
| 2026-08-01T07:17 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Carry a track's standing forward when a p |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

