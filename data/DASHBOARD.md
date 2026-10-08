# Subnet watch — dashboard

_snapshot 2026-10-08T07:46:04Z · block 9236917 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 75.5 | 3,811 | 6,387 | rtx4090* | 5 | 30% |
| 2 | sn91 cascade | 71.1 | 405 | 1,082 | cpu-small | 5 | 52% |
| 3 | sn38 ChronoLLM | 69.8 | 287 | 1,950 | cpu-small | 9 | 52% |
| 4 | sn80 OpenRoboto | 69.4 | 619 | 3,236 | rtx4090* | 7 | 35% |
| 5 | sn1 Apex | 68.9 | 528 | 930 | rtx4090* | 4 | 71% |
| 6 | sn46 Instant | 68.7 | 194 | 236 | cpu-small | 9 | 46% |
| 7 | sn67 Harnyx | 68.5 | 8.53 | 1,025 | cpu-small | 133 | 35% |
| 8 | sn15 ORO | 67.6 | 8.55 | 16.57 | cpu-small | 57 | 97% |
| 9 | sn4 Targon | 66.9 | 10,280 | 30,303 | rtx4090* | 5 | 70% |
| 10 | sn26 Perturb | 66.1 | 233 | 390 | rtx3060 | 4 | 60% |
| 11 | sn62 Ridges | 63.7 | 114 | 1,393 | rtx4090* | 34 | 17% |
| 12 | sn120 Affine | 63.2 | 148 | 308 | rtx4090* | 238 | 1% |
| 13 | sn61 RedTeam | 62.6 | 83.58 | 119 | rtx4090* | 126 | 1% |
| 14 | sn65 True Performance | 62.3 | 79.47 | 167 | rtx4090* | 6 | 75% |
| 15 | sn53 engy | 60 | 1,297 | 2,489 | rtx4090 | 18 | 17% |
| 16 | sn14 Cacheon | 59.8 | 34.58 | 2,603 | rtx4090* | 7 | 54% |
| 17 | sn23 Trishool | 59.6 | 448 | 448 = | cpu-small | 3 | 80% |
| 18 | sn28 SayGM | 59 | 29.34 | 1,861 | rtx4090* | 78 | 36% |
| 19 | sn41 Almanac | 58.9 | 27.29 | 120 | cpu-small | 139 | 2% |
| 20 | sn74 Gittensor | 58.2 | 24.78 | 152 | rtx4090* | 21 | 50% |

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
| dominated (60–90%) | 26 |
| captured (>90%) | 25 |

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
| 2026-10-08T07:46 | sn25 | BURN_DROP | sn25 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-08T07:46 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge runtime upgrade tolerance for the p |
| 2026-10-08T07:46 | sn51 | RELEASE | sn51 released executor-v1.138 |
| 2026-10-08T07:46 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: validator: remove the failed container be |
| 2026-10-08T07:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-10-08T07:46 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: docs(repo): remove retired products, add |
| 2026-10-08T07:46 | sn116 | RELEASE | sn116 released producer-code-r2: code-only tag for the producer and th |
| 2026-10-08T07:46 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #780 from carbonphysi |
| 2026-10-08T07:46 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Validate paired held-out trainer optimiz |
| 2026-10-08T01:21 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Assert the owner-validator's root seat ke |
| 2026-10-08T01:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #266: support verified Finney ru |
| 2026-10-08T01:21 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Restore original C5 progression and prese |
| 2026-10-08T01:21 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #782 from carbonphysi |
| 2026-10-08T01:21 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Use signed manifest quotas for miner-bou |
| 2026-10-07T21:28 | sn15 | RELEASE | sn15 released v2.3.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

