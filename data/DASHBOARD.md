# Subnet watch — dashboard

_snapshot 2026-10-13T16:28:48Z · block 9275526 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 17 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82 | 285 | 24,223 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.7 | 3,068 | 3,068 = | rtx4090* | 5 | 40% |
| 3 | sn53 engy | 71.6 | 1,202 | 2,649 | rtx4090 | 18 | 17% |
| 4 | sn101 Tag101 | 70.4 | 13.78 | 15.05 | cpu-small | 244 | 1% |
| 5 | sn14 Cacheon | 69.9 | 722 | 5,849 | rtx4090* | 3 | 83% |
| 6 | sn67 Harnyx | 69.9 | 11.97 | 697 | cpu-small | 144 | 26% |
| 7 | sn58 Attune | 69.3 | 607 | 812 | rtx4090* | 4 | 74% |
| 8 | sn79 MVTRX | 67 | 7.28 | 42.88 | cpu-small | 247 | 2% |
| 9 | sn4 Targon | 66.8 | 9,917 | 29,238 | rtx4090* | 5 | 70% |
| 10 | sn41 Almanac | 66.1 | 5.96 | 162 | cpu-small | 103 | 3% |
| 11 | sn15 ORO | 65.9 | 6.57 | 17,910 | cpu-small | 57 | 98% |
| 12 | sn62 Ridges | 64.1 | 125 | 1,265 | rtx4090* | 37 | 17% |
| 13 | sn120 Affine | 62.9 | 129 | 238 | rtx4090* | 251 | 1% |
| 14 | sn61 RedTeam | 61.8 | 67.48 | 91.64 | rtx4090* | 134 | 1% |
| 15 | sn28 SayGM | 61.5 | 60.03 | 1,892 | rtx4090* | 69 | 28% |
| 16 | sn111 Claims | 59.8 | 36.08 | 3,157 | rtx4090* | 6 | 90% |
| 17 | sn23 Trishool | 59.2 | 398 | 398 = | cpu-small | 3 | 80% |
| 18 | sn91 cascade | 59 | 376 | 2,012 | cpu-small | 5 | 52% |
| 19 | sn80 OpenRoboto | 58.7 | 886 | 3,549 | rtx4090* | 10 | 35% |
| 20 | sn5 Hone | 57.7 | 34.35 | 34.82 | rtx4090* | 246 | 0% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 19 |
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
| 2026-10-13T16:29 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): the configured goal is rank |
| 2026-10-13T16:29 | sn25 | RELEASE | sn25 released v2026.10.13-1070979130 |
| 2026-10-13T16:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge the validator trail fixes and bound |
| 2026-10-13T16:29 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: Replace the legacy public tree with the v |
| 2026-10-13T16:29 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-10-13T16:29 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: A create that fails on the node itself ke |
| 2026-10-13T16:29 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #53 from hanlinai/fix/ |
| 2026-10-13T16:29 | sn61 | RELEASE | sn61 released 4.10.10 |
| 2026-10-13T16:29 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: adjust challenge incentive weights a |
| 2026-10-13T16:29 | sn68 | SCORING_COMMIT | sn68 commit touches scoring: route all validator chain calls through o |
| 2026-10-13T16:29 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(envscaler): one call per message in  |
| 2026-10-13T16:29 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Merge pull request #229 from DendriteHQ/ |
| 2026-10-13T16:29 | sn116 | RELEASE | sn116 released producer-code-r8.5 |
| 2026-10-13T16:29 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1281 from carbonphys |
| 2026-10-13T16:29 | sn117 | RELEASE | sn117 released everycli v0.4.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

