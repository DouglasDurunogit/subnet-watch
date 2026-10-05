# Subnet watch — dashboard

_snapshot 2026-10-05T09:25:17Z · block 9215813 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 79.5 | 358 | 1,219 | rtx3060 | 4 | 60% |
| 2 | sn23 Trishool | 74.4 | 1,053 | 1,053 = | cpu-small | 2 | 78% |
| 3 | sn41 Almanac | 74 | 35.94 | 103 | cpu-small | 120 | 30% |
| 4 | sn91 cascade | 73.1 | 717 | 2,295 | cpu-small | 5 | 52% |
| 5 | sn53 engy | 71.9 | 1,312 | 3,595 | rtx4090 | 14 | 22% |
| 6 | sn120 Affine | 69.5 | 734 | 734 = | rtx4090* | 75 | 2% |
| 7 | sn80 OpenRoboto | 69.4 | 624 | 4,965 | rtx4090* | 8 | 25% |
| 8 | sn67 Harnyx | 69.3 | 9.77 | 1,259 | cpu-small | 136 | 40% |
| 9 | sn1 Apex | 69.2 | 581 | 1,112 | rtx4090* | 4 | 63% |
| 10 | sn46 Instant | 69.1 | 223 | 274 | cpu-small | 8 | 50% |
| 11 | sn15 ORO | 67.4 | 9.55 | 19.02 | cpu-small | 51 | 98% |
| 12 | sn111 Claims | 66.9 | 296 | 2,653 | rtx4090* | 5 | 70% |
| 13 | sn4 Targon | 65.6 | 6,823 | 32,271 | rtx4090* | 5 | 70% |
| 14 | sn62 Ridges | 64.8 | 156 | 1,919 | rtx4090* | 31 | 21% |
| 15 | sn61 RedTeam | 62.7 | 86.06 | 153 | rtx4090* | 111 | 2% |
| 16 | sn14 Cacheon | 61.2 | 53.07 | 1,847 | rtx4090* | 13 | 23% |
| 17 | sn28 SayGM | 60.6 | 46.79 | 2,882 | rtx4090* | 67 | 27% |
| 18 | sn107 Minos | 58.5 | 359 | 29,140 | cpu-small | 20 | 79% |
| 19 | sn102 ConnitoAI | 58.4 | 800 | 2,118 | rtx4090* | 5 | 42% |
| 20 | sn5 Hone | 58.3 | 39.11 | 42.24 | rtx4090* | 245 | 0% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 21 |
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
| 2026-10-05T09:25 | sn49 | SCORING_COMMIT | sn49 commit touches scoring: Upgrade validator sandbox to Isaac Sim 6. |
| 2026-10-05T09:25 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P2] Validator scrape: record |
| 2026-10-05T09:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Document resource-safe model capacity for |
| 2026-10-05T09:25 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-10-05T09:25 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs: validator hardware requirements (m |
| 2026-10-05T09:25 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Align current verifier roster and public |
| 2026-10-05T02:18 | sn15 | RELEASE | sn15 released Validator v2.2.0: oro-env-runtime 3.3.0, runtime contrac |
| 2026-10-05T02:18 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Validator v2.2.0: oro-env-runtime 3.3.0,  |
| 2026-10-05T02:18 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Reuse checkpoint evaluation when only so |
| 2026-10-04T23:26 | sn85 | BURN_DROP | sn85 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-04T23:26 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Recommend bounded per-task mining search |
| 2026-10-04T20:09 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record final miner qualification and rema |
| 2026-10-04T20:09 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Authorize qualified verifier additions w |
| 2026-10-04T17:06 | sn9 | RELEASE | sn9 released v4.13.4 |
| 2026-10-04T17:06 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify completed original capture and Yum |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

