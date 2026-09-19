# Subnet watch — dashboard

_snapshot 2026-09-19T11:19:08Z · block 9101316 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 12 | `██████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.6 | 6,713 | 6,713 = | cpu-small | 1 | 100% |
| 2 | sn4 Targon | 78.1 | 8,249 | 23,157 | rtx4090* | 6 | 52% |
| 3 | sn3 Teutonic | 76.6 | 5,246 | 5,246 = | rtx4090* | 5 | 20% |
| 4 | sn91 cascade | 71.9 | 515 | 1,376 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 71.1 | 1,037 | 1,585 | rtx4090* | 5 | 32% |
| 6 | sn1 Apex | 70.4 | 829 | 1,064 | rtx4090* | 4 | 57% |
| 7 | sn67 Harnyx | 69.7 | 11.69 | 1,104 | cpu-small | 117 | 33% |
| 8 | sn107 Minos | 69.1 | 366 | 30,515 | cpu-small | 20 | 80% |
| 9 | sn56 Gradients | 68.6 | 491 | 5,793 | rtx4090* | 9 | 46% |
| 10 | sn111 Claims | 66.8 | 295 | 2,641 | rtx4090* | 5 | 70% |
| 11 | sn124 Swarm | 66.6 | 280 | 898 | rtx4090* | 25 | 11% |
| 12 | sn38 ChronoLLM | 66.2 | 106 | 941 | cpu-small | 10 | 52% |
| 13 | sn15 ORO | 63.5 | 4.12 | 8.20 | cpu-small | 22 | 100% |
| 14 | sn28 SayGM | 62.3 | 74.98 | 1,577 | rtx4090* | 58 | 10% |
| 15 | sn74 Gittensor | 62.1 | 72.94 | 205 | rtx4090* | 11 | 63% |
| 16 | sn62 Ridges | 61.5 | 57.85 | 3,629 | rtx4090* | 17 | 42% |
| 17 | sn23 Trishool | 61.2 | 731 | 731 = | cpu-small | 2 | 80% |
| 18 | sn81 Reliquary | 60.4 | 41.36 | 125 | rtx4090* | 25 | 70% |
| 19 | sn51 lium.io | 59.2 | 39.11 | 2,299 | rtx4090* | 65 | 82% |
| 20 | sn61 RedTeam | 59.1 | 27.95 | 2,324 | rtx4090* | 122 | 21% |

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
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 19 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-19T11:19 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.830 - miners can earn again |
| 2026-09-19T11:19 | sn11 | RELEASE | sn11 released v0.7.0 |
| 2026-09-19T11:19 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Season 2 (transition): routing-policy eva |
| 2026-09-19T11:19 | sn25 | RELEASE | sn25 released v2026.9.19-1050096260 |
| 2026-09-19T11:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Pass saved stage evidence to Arena verifi |
| 2026-09-19T11:19 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(price): publish the target miners are |
| 2026-09-19T11:19 | sn112 | BURN_DROP | sn112 burn fell 1.000 -> 0.867 - miners can earn again |
| 2026-09-19T06:16 | sn15 | RELEASE | sn15 released v2.0.27 |
| 2026-09-19T06:16 | sn25 | RELEASE | sn25 released v2026.9.18-1049819730 |
| 2026-09-19T01:25 | sn61 | RELEASE | sn61 released 4.10.6 |
| 2026-09-19T01:25 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update ada_detection challenge imag |
| 2026-09-19T01:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep baseline source update independent o |
| 2026-09-19T01:25 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(bounty): python subnet with product |
| 2026-09-18T23:15 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.814 - miners can earn again |
| 2026-09-18T23:15 | sn25 | RELEASE | sn25 released v2026.9.18-1049702080 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

