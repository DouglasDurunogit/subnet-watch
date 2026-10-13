# Subnet watch — dashboard

_snapshot 2026-10-13T21:34:55Z · block 9277056 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.1 | 293 | 24,651 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.8 | 3,137 | 3,137 = | rtx4090* | 5 | 40% |
| 3 | sn53 engy | 71.7 | 1,229 | 2,709 | rtx4090 | 18 | 17% |
| 4 | sn101 Tag101 | 70.5 | 14.30 | 15.80 | cpu-small | 242 | 1% |
| 5 | sn14 Cacheon | 70 | 734 | 5,944 | rtx4090* | 3 | 83% |
| 6 | sn67 Harnyx | 70 | 12.12 | 705 | cpu-small | 144 | 26% |
| 7 | sn58 Attune | 69.4 | 632 | 846 | rtx4090* | 4 | 74% |
| 8 | sn4 Targon | 66.9 | 10,061 | 29,663 | rtx4090* | 5 | 70% |
| 9 | sn79 MVTRX | 66.6 | 7.43 | 40.37 | cpu-small | 245 | 2% |
| 10 | sn41 Almanac | 66.3 | 6.24 | 164 | cpu-small | 103 | 4% |
| 11 | sn15 ORO | 66.1 | 6.44 | 13.86 | cpu-small | 57 | 98% |
| 12 | sn62 Ridges | 63.9 | 119 | 906 | rtx4090* | 37 | 17% |
| 13 | sn120 Affine | 63.5 | 138 | 236 | rtx4090* | 250 | 1% |
| 14 | sn28 SayGM | 62.1 | 72.85 | 3,647 | rtx4090* | 67 | 27% |
| 15 | sn61 RedTeam | 61.9 | 68.49 | 91.66 | rtx4090* | 130 | 1% |
| 16 | sn91 cascade | 60.8 | 638 | 2,043 | cpu-small | 5 | 52% |
| 17 | sn111 Claims | 59.9 | 36.70 | 3,200 | rtx4090* | 6 | 90% |
| 18 | sn23 Trishool | 59.2 | 401 | 401 = | cpu-small | 3 | 80% |
| 19 | sn80 OpenRoboto | 58.7 | 878 | 3,518 | rtx4090* | 10 | 35% |
| 20 | sn81 Reliquary | 58.2 | 20.88 | 358 | rtx4090* | 47 | 66% |

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
| dominated (60–90%) | 29 |
| captured (>90%) | 22 |

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
| 2026-10-13T21:35 | sn15 | RELEASE | sn15 released v2.5.0 |
| 2026-10-13T21:35 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Load v7 and v8 task packs; move to oro-en |
| 2026-10-13T21:35 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Write the validator's settlement v2 adopt |
| 2026-10-13T21:35 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Adding weights version key to validator l |
| 2026-10-13T21:35 | sn63 | SCORING_COMMIT | sn63 commit touches scoring: Track whether a terminal verify update re |
| 2026-10-13T21:35 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Port Mathlib headers to the immutable tas |
| 2026-10-13T21:35 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #415: Verify judge pro |
| 2026-10-13T21:35 | sn116 | RELEASE | sn116 released producer-code-r8.6 |
| 2026-10-13T21:35 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-13T21:35 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Reduce hourly evidence scan cost without |
| 2026-10-13T16:29 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): the configured goal is rank |
| 2026-10-13T16:29 | sn25 | RELEASE | sn25 released v2026.10.13-1070979130 |
| 2026-10-13T16:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge the validator trail fixes and bound |
| 2026-10-13T16:29 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: Replace the legacy public tree with the v |
| 2026-10-13T16:29 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

