# Subnet watch — dashboard

_snapshot 2026-11-15T14:11:31Z · block 9512345 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.7 | 241 | 241 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.6 | 2,191 | 4,391 | rtx4090* | 4 | 40% |
| 3 | sn97 Ingot | 71.6 | 1,212 | 1,212 = | rtx4090* | 5 | 20% |
| 4 | sn56 Gradients | 70 | 746 | 3,936 | rtx4090* | 6 | 50% |
| 5 | sn34 Yugos | 69.6 | 665 | 5,717 | rtx4090* | 3 | 85% |
| 6 | sn58 Attune | 68.9 | 533 | 858 | rtx4090* | 5 | 70% |
| 7 | sn41 Almanac | 68.1 | 8.42 | 127 | cpu-small | 154 | 2% |
| 8 | sn15 ORO | 66.5 | 6.06 | 12.19 | cpu-small | 67 | 95% |
| 9 | sn67 Harnyx | 65.3 | 3.11 | 253 | cpu-small | 195 | 18% |
| 10 | sn124 Swarm | 65.2 | 185 | 778 | rtx4090* | 10 | 31% |
| 11 | sn53 engy | 65 | 164 | 6,579 | rtx4090 | 23 | 40% |
| 12 | sn38 ChronoLLM | 62.9 | 44.57 | 308 | cpu-small | 9 | 52% |
| 13 | sn120 Affine | 61.9 | 2,291 | 2,291 = | rtx4090* | 10 | 10% |
| 14 | sn111 Claims | 60.2 | 39.91 | 160 | rtx4090* | 4 | 88% |
| 15 | sn62 Ridges | 59.7 | 33.15 | 602 | rtx4090* | 44 | 15% |
| 16 | sn4 Targon | 57.6 | 9,245 | 19,827 | rtx4090* | 5 | 62% |
| 17 | sn102 ConnitoAI | 57 | 533 | 534 | rtx4090* | 4 | 25% |
| 18 | sn5 Hone | 56.9 | 18.72 | 41.04 | rtx4090* | 240 | 1% |
| 19 | sn28 SayGM | 56.6 | 15.72 | 1,095 | rtx4090* | 128 | 26% |
| 20 | sn66 conjectures | 56.4 | 11.86 | 972 | rtx4090* | 7 | 80% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 30 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-15T14:11 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore: remove dead load_episode_artifact  |
| 2026-11-15T14:11 | sn25 | RELEASE | sn25 released v2026.11.15-1099387180 |
| 2026-11-15T14:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow measured baselines with capture gap |
| 2026-11-15T14:11 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(miner): install reliquary-terminal so |
| 2026-11-15T14:11 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Miner kit: check_result says why a try e |
| 2026-11-15T06:17 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.975 - miners can earn again |
| 2026-11-15T06:17 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1433: Dashboard on e |
| 2026-11-15T06:17 | sn117 | RELEASE | sn117 released everycli v1.2.3 |
| 2026-11-15T00:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1240 from leadpoet/fi |
| 2026-11-15T00:02 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Queue place: a resubmission of a stop-ca |
| 2026-11-14T20:09 | sn42 | RELEASE | sn42 released v0.6.15 |
| 2026-11-14T20:09 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: v0.6.15: the reference miner hands a fini |
| 2026-11-14T20:09 | sn116 | BURN_DROP | sn116 burn fell 1.000 -> 0.750 - miners can earn again |
| 2026-11-14T20:09 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Tests: a serve stop leaves a queued task |
| 2026-11-14T15:45 | sn25 | RELEASE | sn25 released v2026.11.14-1098667430 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

