# Subnet watch — dashboard

_snapshot 2026-09-28T15:21:24Z · block 9167194 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
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
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 76.1 | 60.83 | 132 | cpu-small | 113 | 2% |
| 2 | sn91 cascade | 73.1 | 716 | 1,494 | cpu-small | 5 | 36% |
| 3 | sn1 Apex | 70.8 | 938 | 1,069 | rtx4090* | 4 | 55% |
| 4 | sn67 Harnyx | 69.1 | 9.68 | 1,182 | cpu-small | 116 | 36% |
| 5 | sn107 Minos | 68.7 | 338 | 27,634 | cpu-small | 20 | 80% |
| 6 | sn4 Targon | 68.2 | 15,091 | 27,296 | rtx4090* | 5 | 58% |
| 7 | sn15 ORO | 68.1 | 12.58 | 19,202 | cpu-small | 75 | 95% |
| 8 | sn96 Verathos | 67.6 | 19.05 | 214 | rtx4090 | 78 | 33% |
| 9 | sn124 Swarm | 66.8 | 302 | 897 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 66.6 | 288 | 2,582 | rtx4090* | 5 | 67% |
| 11 | sn3 Teutonic | 64.6 | 5,119 | 5,119 = | rtx4090* | 5 | 20% |
| 12 | sn62 Ridges | 64.2 | 133 | 1,154 | rtx4090* | 26 | 13% |
| 13 | sn61 RedTeam | 62.8 | 87.15 | 252 | rtx4090* | 85 | 3% |
| 14 | sn26 Perturb | 62.4 | 79.43 | 121 | rtx3060 | 5 | 90% |
| 15 | sn28 SayGM | 62 | 71.05 | 1,016 | rtx4090* | 69 | 12% |
| 16 | sn23 Trishool | 61.8 | 864 | 864 = | cpu-small | 2 | 80% |
| 17 | sn14 Cacheon | 61 | 49.35 | 2,272 | rtx4090* | 14 | 30% |
| 18 | sn100 Cortex | 59.6 | 32.64 | 226 | rtx4090* | 19 | 70% |
| 19 | sn80 OpenRoboto | 59 | 959 | 2,966 | rtx4090* | 8 | 33% |
| 20 | sn74 Gittensor | 58.8 | 28.80 | 252 | rtx4090* | 19 | 63% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 22 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-28T15:21 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Initialize public Witness subnet with bou |
| 2026-09-28T15:21 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: fix: seed evaluation sampling from the pi |
| 2026-09-28T15:21 | sn28 | RELEASE | sn28 released v0.4.24 |
| 2026-09-28T15:21 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.24 ( |
| 2026-09-28T15:21 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Merge pull request #49 from corvxai/forec |
| 2026-09-28T15:21 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] validator: an idle node  |
| 2026-09-28T15:21 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #109 from conjectures- |
| 2026-09-28T15:21 | sn111 | RELEASE | sn111 released v1.0.0 |
| 2026-09-28T06:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify cross-domain company rebrands |
| 2026-09-28T01:05 | sn15 | RELEASE | sn15 released v2.0.35: Log nested inference tool types in proxy access |
| 2026-09-28T01:05 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(deps): bump anyio from 4.13.0 to 4. |
| 2026-09-28T01:05 | sn28 | RELEASE | sn28 released v0.4.24-dev |
| 2026-09-28T01:05 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.4.24-dev (#290 |
| 2026-09-28T01:05 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-28T01:05 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind final evidence resolution verifier r |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

