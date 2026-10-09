# Subnet watch — dashboard

_snapshot 2026-10-09T14:19:45Z · block 9246082 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.8 | 274 | 23,221 | cpu-small | 20 | 80% |
| 2 | sn41 Almanac | 74.9 | 44.26 | 111 | cpu-small | 121 | 3% |
| 3 | sn80 OpenRoboto | 71.9 | 1,306 | 6,230 | rtx4090* | 7 | 35% |
| 4 | sn1 Apex | 70.9 | 969 | 1,013 | rtx4090* | 4 | 53% |
| 5 | sn101 Tag101 | 70 | 12.69 | 17.17 | cpu-small | 243 | 1% |
| 6 | sn38 ChronoLLM | 68.7 | 210 | 956 | cpu-small | 9 | 52% |
| 7 | sn67 Harnyx | 68.4 | 7.96 | 828 | cpu-small | 147 | 30% |
| 8 | sn4 Targon | 66.8 | 9,867 | 29,093 | rtx4090* | 5 | 70% |
| 9 | sn26 Perturb | 66.3 | 246 | 411 | rtx3060 | 4 | 60% |
| 10 | sn15 ORO | 65.8 | 6.12 | 18,306 | cpu-small | 46 | 98% |
| 11 | sn62 Ridges | 63.5 | 106 | 1,304 | rtx4090* | 34 | 17% |
| 12 | sn61 RedTeam | 62.4 | 79.15 | 105 | rtx4090* | 124 | 1% |
| 13 | sn65 True Performance | 62.3 | 78.99 | 166 | rtx4090* | 6 | 75% |
| 14 | sn53 engy | 60 | 1,318 | 4,358 | rtx4090 | 18 | 17% |
| 15 | sn23 Trishool | 59.2 | 403 | 403 = | cpu-small | 3 | 80% |
| 16 | sn91 cascade | 59.2 | 401 | 1,072 | cpu-small | 5 | 52% |
| 17 | sn28 SayGM | 59 | 29.67 | 2,821 | rtx4090* | 68 | 24% |
| 18 | sn81 Reliquary | 58.8 | 25.12 | 391 | rtx4090* | 42 | 42% |
| 19 | sn46 Instant | 58.2 | 296 | 393 | cpu-small | 6 | 44% |
| 20 | sn5 Hone | 57.8 | 33.80 | 35.67 | rtx4090* | 244 | 0% |

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
| dominated (60–90%) | 25 |
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
| 2026-10-09T14:20 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add competition filters to evaluation hist |
| 2026-10-09T14:20 | sn21 | RELEASE | sn21 released SN21 training data v4 (live basket shape) |
| 2026-10-09T14:20 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: Avoid a full miner_predictions scan when  |
| 2026-10-09T14:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - Validator: one Docker SDK SSH  |
| 2026-10-09T14:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected judge fit manifest for  |
| 2026-10-09T14:20 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: protected/miner/manifest.json: single adm |
| 2026-10-09T14:20 | sn76 | README_TASK_DIFF | sn76 README task/scoring sections changed |
| 2026-10-09T14:20 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Unblock C5 admission reads and correct hi |
| 2026-10-09T14:20 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scoring: cache z_for_resolve (pure functi |
| 2026-10-09T14:20 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(validator): route verified operator |
| 2026-10-09T14:20 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: VALIDATOR-30 contract: the refusal order |
| 2026-10-09T14:20 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Verify effective-LR evidence for normal  |
| 2026-10-09T06:48 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4001 - validator: no settled window k |
| 2026-10-09T06:48 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #342 from reliquadotai |
| 2026-10-09T06:48 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: README: IQ Markets for players (web app,  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

