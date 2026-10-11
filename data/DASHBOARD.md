# Subnet watch — dashboard

_snapshot 2026-10-11T01:48:55Z · block 9256727 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.4 | 312 | 26,271 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 75 | 3,279 | 8,555 | rtx4090* | 5 | 40% |
| 3 | sn41 Almanac | 74.5 | 40.64 | 112 | cpu-small | 125 | 2% |
| 4 | sn80 OpenRoboto | 72.3 | 1,452 | 6,923 | rtx4090* | 7 | 35% |
| 5 | sn101 Tag101 | 70.3 | 13.25 | 15.38 | cpu-small | 244 | 1% |
| 6 | sn67 Harnyx | 69 | 9.21 | 896 | cpu-small | 132 | 31% |
| 7 | sn38 ChronoLLM | 68.8 | 219 | 997 | cpu-small | 9 | 52% |
| 8 | sn79 MVTRX | 67.8 | 8.41 | 28.10 | cpu-small | 250 | 1% |
| 9 | sn15 ORO | 66.8 | 6.85 | 14.10 | cpu-small | 52 | 98% |
| 10 | sn26 Perturb | 66.2 | 237 | 396 | rtx3060 | 4 | 60% |
| 11 | sn62 Ridges | 63.9 | 120 | 1,379 | rtx4090* | 36 | 17% |
| 12 | sn120 Affine | 63.3 | 152 | 403 | rtx4090* | 239 | 1% |
| 13 | sn65 True Performance | 62.6 | 84.44 | 177 | rtx4090* | 6 | 75% |
| 14 | sn61 RedTeam | 62.2 | 73.45 | 107 | rtx4090* | 137 | 1% |
| 15 | sn28 SayGM | 60.8 | 48.69 | 1,286 | rtx4090* | 69 | 19% |
| 16 | sn53 engy | 60 | 1,312 | 2,518 | rtx4090 | 18 | 17% |
| 17 | sn23 Trishool | 59.4 | 422 | 422 = | cpu-small | 3 | 80% |
| 18 | sn91 cascade | 59.2 | 402 | 2,151 | cpu-small | 5 | 52% |
| 19 | sn81 Reliquary | 59.2 | 28.60 | 245 | rtx4090* | 47 | 54% |
| 20 | sn5 Hone | 59 | 35.59 | 37.05 | rtx4090* | 243 | 0% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 27 |
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
| 2026-10-10T15:35 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Rejudge Oct10 saved outputs on final ATS  |
| 2026-10-10T09:44 | sn25 | RELEASE | sn25 released v2026.10.10-1068162640 |
| 2026-10-10T09:44 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] validator: cap fresh vlo |
| 2026-10-10T09:44 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #328 from leadpoet/cod |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

