# Subnet watch — dashboard

_snapshot 2026-10-09T06:48:15Z · block 9243824 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82 | 286 | 24,510 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.8 | 3,129 | 6,266 | rtx4090* | 5 | 30% |
| 3 | sn41 Almanac | 73.7 | 33.04 | 113 | cpu-small | 136 | 2% |
| 4 | sn80 OpenRoboto | 71.9 | 1,323 | 6,312 | rtx4090* | 7 | 35% |
| 5 | sn91 cascade | 71.2 | 410 | 1,095 | cpu-small | 5 | 52% |
| 6 | sn1 Apex | 71 | 985 | 1,029 | rtx4090* | 4 | 52% |
| 7 | sn67 Harnyx | 69.3 | 10.36 | 776 | cpu-small | 136 | 28% |
| 8 | sn38 ChronoLLM | 68.8 | 214 | 974 | cpu-small | 9 | 52% |
| 9 | sn4 Targon | 66.8 | 9,949 | 29,333 | rtx4090* | 5 | 70% |
| 10 | sn26 Perturb | 66.3 | 247 | 412 | rtx3060 | 4 | 60% |
| 11 | sn15 ORO | 66.3 | 6.23 | 18,580 | cpu-small | 46 | 98% |
| 12 | sn62 Ridges | 63.5 | 107 | 1,316 | rtx4090* | 34 | 17% |
| 13 | sn120 Affine | 63.2 | 140 | 383 | rtx4090* | 245 | 1% |
| 14 | sn65 True Performance | 62.4 | 79.56 | 167 | rtx4090* | 6 | 75% |
| 15 | sn61 RedTeam | 62.4 | 79.38 | 106 | rtx4090* | 125 | 1% |
| 16 | sn101 Tag101 | 62.4 | 0.87 | 1.24 | cpu-small | 160 | 91% |
| 17 | sn53 engy | 60.1 | 1,327 | 4,389 | rtx4090 | 18 | 17% |
| 18 | sn28 SayGM | 59.6 | 34.48 | 2,995 | rtx4090* | 74 | 32% |
| 19 | sn23 Trishool | 59.4 | 426 | 426 = | cpu-small | 3 | 80% |
| 20 | sn102 ConnitoAI | 59 | 969 | 1,200 | rtx4090* | 6 | 29% |

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
| 2026-10-09T06:48 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4001 - validator: no settled window k |
| 2026-10-09T06:48 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #342 from reliquadotai |
| 2026-10-09T06:48 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: README: IQ Markets for players (web app,  |
| 2026-10-09T06:48 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Add v1.1 scoring, AWS corpus leasing, we |
| 2026-10-09T06:48 | sn101 | README_TASK_DIFF | sn101 README task/scoring sections changed |
| 2026-10-09T06:48 | sn107 | SCORING_COMMIT | sn107 commit touches scoring: Merge pull request #40 from minos-protoc |
| 2026-10-09T06:48 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #854 from carbonphysi |
| 2026-10-09T06:48 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Bind native recovery imports and keep ev |
| 2026-10-09T00:42 | sn25 | RELEASE | sn25 released v2026.10.8-1066946420 |
| 2026-10-09T00:42 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-09T00:42 | sn62 | RELEASE | sn62 released v0.3.10 |
| 2026-10-09T00:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #295 from leadpoet/fix |
| 2026-10-09T00:42 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Select policy-budget miner release and re |
| 2026-10-09T00:42 | sn116 | RELEASE | sn116 released worker-images-v3 |
| 2026-10-09T00:42 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #846 from carbonphysi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

