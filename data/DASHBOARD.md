# Subnet watch — dashboard

_snapshot 2026-10-11T08:43:09Z · block 9258799 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.3 | 301 | 25,567 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.9 | 3,196 | 8,537 | rtx4090* | 5 | 40% |
| 3 | sn80 OpenRoboto | 72.2 | 1,446 | 6,898 | rtx4090* | 7 | 35% |
| 4 | sn101 Tag101 | 70.2 | 12.85 | 14.86 | cpu-small | 243 | 1% |
| 5 | sn67 Harnyx | 69 | 8.98 | 932 | cpu-small | 120 | 33% |
| 6 | sn38 ChronoLLM | 68.8 | 217 | 990 | cpu-small | 9 | 52% |
| 7 | sn79 MVTRX | 67.6 | 8.43 | 41.02 | cpu-small | 246 | 2% |
| 8 | sn15 ORO | 66.4 | 6.68 | 13.76 | cpu-small | 52 | 98% |
| 9 | sn62 Ridges | 63.9 | 118 | 1,364 | rtx4090* | 36 | 17% |
| 10 | sn120 Affine | 63.4 | 155 | 352 | rtx4090* | 238 | 1% |
| 11 | sn65 True Performance | 62.6 | 85.65 | 180 | rtx4090* | 6 | 75% |
| 12 | sn41 Almanac | 62.5 | 3.06 | 164 | cpu-small | 125 | 3% |
| 13 | sn61 RedTeam | 62.3 | 76.95 | 110 | rtx4090* | 128 | 1% |
| 14 | sn28 SayGM | 60.6 | 46.84 | 737 | rtx4090* | 71 | 27% |
| 15 | sn53 engy | 60.1 | 1,346 | 2,583 | rtx4090 | 18 | 17% |
| 16 | sn23 Trishool | 59.4 | 423 | 423 = | cpu-small | 3 | 80% |
| 17 | sn5 Hone | 58.9 | 35.51 | 36.81 | rtx4090* | 245 | 0% |
| 18 | sn81 Reliquary | 58.9 | 25.88 | 236 | rtx4090* | 50 | 55% |
| 19 | sn111 Claims | 58.2 | 22.47 | 252 | rtx4090* | 7 | 90% |
| 20 | sn91 cascade | 57.8 | 267 | 536 | cpu-small | 5 | 52% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 28 |
| captured (>90%) | 21 |

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
| 2026-10-11T08:43 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): restore rendered recheck |
| 2026-10-11T08:43 | sn25 | RELEASE | sn25 released v2026.10.10-1068958850 |
| 2026-10-11T08:43 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1041 from carbonphys |
| 2026-10-11T08:43 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document independent epoch openings and  |
| 2026-10-11T01:49 | sn25 | RELEASE | sn25 released v2026.10.10-1068748650 |
| 2026-10-11T01:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify guarded natural expiry retains unc |
| 2026-10-10T22:59 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge seeding validator trails from every |
| 2026-10-10T22:59 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #363 from leadpoet/fix |
| 2026-10-10T19:34 | sn25 | RELEASE | sn25 released v2026.10.10-1068595480 |
| 2026-10-10T19:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #354 from leadpoet/fix |
| 2026-10-10T19:34 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: On a baseline_epoch change the validator |
| 2026-10-10T19:34 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Clarify availability of reused historica |
| 2026-10-10T15:35 | sn25 | RELEASE | sn25 released v2026.10.10-1068404160 |
| 2026-10-10T15:35 | sn28 | RELEASE | sn28 released v0.4.27-dev |
| 2026-10-10T15:35 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.4.27-dev (#310 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

