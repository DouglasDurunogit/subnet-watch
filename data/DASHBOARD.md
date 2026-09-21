# Subnet watch — dashboard

_snapshot 2026-09-21T14:25:35Z · block 9116523 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78.2 | 8,637 | 24,246 | rtx4090* | 6 | 53% |
| 2 | sn3 Teutonic | 76.7 | 5,427 | 5,427 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 73 | 695 | 2,785 | cpu-small | 5 | 52% |
| 4 | sn107 Minos | 69 | 359 | 30,391 | cpu-small | 20 | 80% |
| 5 | sn67 Harnyx | 68.7 | 8.80 | 1,202 | cpu-small | 142 | 36% |
| 6 | sn15 ORO | 67 | 9.44 | 18.90 | cpu-small | 55 | 97% |
| 7 | sn124 Swarm | 66.8 | 294 | 938 | rtx4090* | 25 | 11% |
| 8 | sn38 ChronoLLM | 66.8 | 125 | 1,102 | cpu-small | 10 | 52% |
| 9 | sn111 Claims | 66.1 | 244 | 2,196 | rtx4090* | 5 | 55% |
| 10 | sn28 SayGM | 62.7 | 86.05 | 1,319 | rtx4090* | 61 | 17% |
| 11 | sn104 TAOstatus | 62.6 | 41.04 | 41.04 = | cpu-small | 2 | 99% |
| 12 | sn62 Ridges | 62.3 | 73.65 | 2,656 | rtx4090* | 19 | 30% |
| 13 | sn51 lium.io | 60.8 | 58.28 | 1,653 | rtx4090* | 67 | 80% |
| 14 | sn81 Reliquary | 59.1 | 27.86 | 96.36 | rtx4090* | 23 | 83% |
| 15 | sn61 RedTeam | 58.9 | 26.53 | 905 | rtx4090* | 120 | 10% |
| 16 | sn74 Gittensor | 58.7 | 28.88 | 285 | rtx4090* | 13 | 62% |
| 17 | sn102 ConnitoAI | 58.1 | 20.55 | 1,278 | rtx4090* | 8 | 26% |
| 18 | sn80 OpenRoboto | 56.9 | 520 | 1,840 | rtx4090* | 5 | 43% |
| 19 | sn9 iota | 56.1 | 12,257 | 12,257 = | rtx4090* | 2 | 56% |
| 20 | sn11 TrajectoryRL | 54.7 | 6,889 | 6,889 = | rtx4090* | 1 | 100% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 17 |
| captured (>90%) | 25 |

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
| 2026-09-21T14:26 | sn15 | RELEASE | sn15 released v2.0.28: chore(validator): split hosted and local runtim |
| 2026-09-21T14:26 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): split hosted and local  |
| 2026-09-21T14:26 | sn25 | RELEASE | sn25 released v2026.9.21-1051772980 |
| 2026-09-21T14:26 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Avoid whole-fleet rendering in validator  |
| 2026-09-21T14:26 | sn28 | RELEASE | sn28 released v0.4.20-dev |
| 2026-09-21T14:26 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore: prepare KubeTEE FLUX miner release |
| 2026-09-21T14:26 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: fix: increase max_new_tokens from 50 to 1 |
| 2026-09-21T14:26 | sn51 | RELEASE | sn51 released executor-v1.133 |
| 2026-09-21T14:26 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3678 - [P2] validator: explain add_pu |
| 2026-09-21T14:26 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Keep prep-failed task rows when replacing |
| 2026-09-21T07:15 | sn11 | RELEASE | sn11 released v0.7.3 |
| 2026-09-21T07:15 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: feat(validator): report health on the hea |
| 2026-09-21T07:15 | sn51 | RELEASE | sn51 released executor-v1.132 |
| 2026-09-21T07:15 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3677 - [P2] validator scrape: disk_ty |
| 2026-09-21T07:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep single contact role ID validation si |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

