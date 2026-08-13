# Subnet watch — dashboard

_snapshot 2026-08-13T15:30:45Z · block 8836525 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 2 | `█` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 39 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 107 | 31,890 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.6 | 39.34 | 188 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.2 | 17.16 | 706 | cpu-small | 148 | 19% |
| 4 | sn62 Ridges | 69 | 548 | 1,981 | rtx4090* | 7 | 35% |
| 5 | sn91 cascade | 69 | 547 | 1,259 | rtx4090* | 5 | 50% |
| 6 | sn41 Almanac | 69 | 10.41 | 28.69 | cpu-small | 68 | 73% |
| 7 | sn56 Gradients | 68.9 | 532 | 984 | rtx4090* | 7 | 65% |
| 8 | sn96 Verathos | 68.8 | 24.62 | 272 | rtx4090 | 58 | 41% |
| 9 | sn100 BASE | 68.1 | 414 | 1,837 | rtx4090* | 5 | 52% |
| 10 | sn26 Perturb | 67.9 | 19.69 | 843 | rtx3060 | 11 | 50% |
| 11 | sn21 AdTAO | 67.5 | 7.65 | 34.28 | cpu-small | 88 | 45% |
| 12 | sn124 Swarm | 66 | 234 | 499 | rtx4090* | 23 | 11% |
| 13 | sn38 ChronoLLM | 64.7 | 163 | 3,557 | rtx4090* | 10 | 52% |
| 14 | sn85 Vidaio | 64.7 | 150 | 616 | rtx4090* | 10 | 19% |
| 15 | sn80 OpenRoboto | 64.5 | 143 | 591 | rtx4090* | 4 | 91% |
| 16 | sn1 Apex | 63.9 | 119 | 876 | rtx4090* | 4 | 76% |
| 17 | sn28 gm | 61 | 51.52 | 2,907 | rtx4090* | 27 | 30% |
| 18 | sn51 lium.io | 60.1 | 45.90 | 1,816 | rtx4090* | 50 | 71% |
| 19 | sn74 Gittensor | 58.4 | 24.95 | 217 | rtx4090* | 13 | 63% |
| 20 | sn61 RedTeam | 58.4 | 22.51 | 1,648 | rtx4090* | 58 | 35% |

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
| dominated (60–90%) | 18 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-13T15:31 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: Merge pull request #49 from 0xsigurd/feat |
| 2026-08-13T15:31 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-08-13T15:31 | sn51 | RELEASE | sn51 released executor-v1.119 |
| 2026-08-13T15:31 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: updated validator weights submitter |
| 2026-08-13T15:31 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(site): attribute arena weight per ch |
| 2026-08-13T14:10 | sn1 | RELEASE | sn1 released v4.3.1 |
| 2026-08-13T12:36 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-13T10:35 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-13T10:35 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-08-13T09:22 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: blacklist + min common challenges tiebrea |
| 2026-08-13T04:32 | sn70 | BURN_DROP | sn70 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-13T04:32 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: measure miner behaviour above the boa |
| 2026-08-13T02:42 | sn51 | RELEASE | sn51 released executor-v1.118 |
| 2026-08-13T02:42 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Preserve production task retirements |
| 2026-08-13T02:42 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

