# Subnet watch — dashboard

_snapshot 2026-10-14T15:32:41Z · block 9282445 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82 | 280 | 23,318 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.7 | 2,993 | 2,993 = | rtx4090* | 5 | 40% |
| 3 | sn101 Tag101 | 70.3 | 13.47 | 14.46 | cpu-small | 242 | 1% |
| 4 | sn14 Cacheon | 69.8 | 707 | 5,723 | rtx4090* | 3 | 83% |
| 5 | sn53 engy | 69.5 | 630 | 2,623 | rtx4090 | 24 | 16% |
| 6 | sn91 cascade | 69.3 | 236 | 947 | cpu-small | 5 | 52% |
| 7 | sn58 Attune | 68.6 | 500 | 804 | rtx4090* | 5 | 71% |
| 8 | sn67 Harnyx | 68.6 | 8.21 | 665 | cpu-small | 119 | 25% |
| 9 | sn79 MVTRX | 67 | 6.89 | 52.42 | cpu-small | 246 | 2% |
| 10 | sn4 Targon | 66.7 | 9,679 | 28,538 | rtx4090* | 5 | 70% |
| 11 | sn7 Allways | 65.6 | 208 | 497 | rtx4090* | 8 | 28% |
| 12 | sn15 ORO | 65.4 | 6.48 | 16,648 | cpu-small | 72 | 97% |
| 13 | sn26 Perturb | 64.9 | 311 | 384 | rtx3060 | 4 | 60% |
| 14 | sn120 Affine | 63.9 | 129 | 419 | rtx4090* | 249 | 1% |
| 15 | sn62 Ridges | 63.7 | 113 | 1,233 | rtx4090* | 37 | 17% |
| 16 | sn28 SayGM | 63.3 | 101 | 1,334 | rtx4090* | 75 | 22% |
| 17 | sn61 RedTeam | 61.9 | 67.27 | 88.13 | rtx4090* | 126 | 1% |
| 18 | sn41 Almanac | 60.7 | 2.27 | 148 | cpu-small | 126 | 3% |
| 19 | sn111 Claims | 59.6 | 33.47 | 2,974 | rtx4090* | 6 | 90% |
| 20 | sn49 Nepher Robotics | 58.7 | 877 | 3,959 | rtx4090* | 4 | 68% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 26 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-14T15:33 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4035 - [P1] Validator: resolve hostna |
| 2026-10-14T15:33 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: feat: extend leaderboard endpoint (add pa |
| 2026-10-14T15:33 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #434: retain bounded validator e |
| 2026-10-14T15:33 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.953 - miners can earn again |
| 2026-10-14T15:33 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.921 - miners can earn again |
| 2026-10-14T15:33 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1347 from carbonphys |
| 2026-10-14T15:33 | sn117 | RELEASE | sn117 released everycli v0.5.4 |
| 2026-10-14T15:33 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: fix: profile reconnect and miner dashboa |
| 2026-10-14T10:39 | sn25 | RELEASE | sn25 released v2026.10.14-1071632750 |
| 2026-10-14T10:39 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.715 - miners can earn again |
| 2026-10-14T10:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4270 - [P1] Validator: count rented n |
| 2026-10-14T10:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-14T10:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #432: repair verified domain con |
| 2026-10-14T10:39 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: security: repair frozen verifier snapshot |
| 2026-10-14T10:39 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Preserve native reward history through wr |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

