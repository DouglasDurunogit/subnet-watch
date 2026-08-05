# Subnet watch — dashboard

_snapshot 2026-08-05T10:05:48Z · block 8777310 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 38 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.8 | 192 | 385 | cpu-small | 7 | 24% |
| 2 | sn107 Minos | 77.6 | 99.79 | 28,538 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 76.8 | 2,194 | 2,194 = | cpu-small | 2 | 90% |
| 4 | sn67 Harnyx | 72 | 21.93 | 941 | cpu-small | 155 | 22% |
| 5 | sn102 ConnitoAI | 71.8 | 1,258 | 1,421 | rtx4090* | 6 | 26% |
| 6 | sn91 cascade | 69.7 | 682 | 2,754 | rtx4090* | 5 | 52% |
| 7 | sn62 Ridges | 69.5 | 636 | 2,615 | rtx4090* | 7 | 35% |
| 8 | sn26 Perturb | 69 | 25.67 | 203 | rtx3060 | 11 | 50% |
| 9 | sn41 Almanac | 68.4 | 9.07 | 66.32 | cpu-small | 60 | 78% |
| 10 | sn15 ORO | 67.2 | 8.90 | 10,922 | cpu-small | 72 | 94% |
| 11 | sn74 Gittensor | 66.1 | 236 | 277 | rtx4090* | 9 | 18% |
| 12 | sn124 Swarm | 65.9 | 226 | 611 | rtx4090* | 23 | 10% |
| 13 | sn38 ChronoLLM | 65.5 | 207 | 3,481 | rtx4090* | 10 | 52% |
| 14 | sn21 AdTAO | 65.4 | 4.65 | 21.58 | cpu-small | 142 | 45% |
| 15 | sn53 engy | 64.2 | 130 | 2,806 | rtx4090 | 28 | 17% |
| 16 | sn80 OpenRoboto | 62.3 | 73.35 | 277 | rtx4090* | 4 | 91% |
| 17 | sn101 Tag101 | 59.8 | 0.07 | 0.83 | cpu-small | 243 | 90% |
| 18 | sn61 RedTeam | 58.8 | 25.08 | 85.94 | rtx4090* | 91 | 3% |
| 19 | sn28 gm | 58.7 | 26.48 | 1,145 | rtx4090* | 19 | 67% |
| 20 | sn51 lium.io | 56.1 | 17.92 | 5,092 | rtx4090* | 47 | 65% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 22 |
| captured (>90%) | 24 |

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
| 2026-08-05T10:06 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Make task slug id's permanent |
| 2026-08-05T10:06 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Scope repeated validator weight evidence |
| 2026-08-05T07:16 | sn15 | RELEASE | sn15 released v1.2.5 |
| 2026-08-05T07:16 | sn62 | RELEASE | sn62 released v0.2.5 |
| 2026-08-05T04:24 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(verifiability): daily scoring receip |
| 2026-08-05T04:24 | sn91 | RELEASE | sn91 released worker-v0.5.0 |
| 2026-08-05T00:53 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Improve silver alignment and scoring |
| 2026-08-04T23:16 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #473 from ridgesai/upd |
| 2026-08-04T18:47 | sn12 | RELEASE | sn12 released validator-staging-2026-08-04-30935079890-625-1: chore: b |
| 2026-08-04T18:47 | sn21 | RELEASE | sn21 released archive/per-cell-consensus-2026-06: feat(consensus): epo |
| 2026-08-04T18:47 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(validator): burn follows Rob's dated |
| 2026-08-04T18:47 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-04T18:47 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Release validator deployment gate 0.2.4 |
| 2026-08-04T17:01 | sn62 | RELEASE | sn62 released v0.2.4 |
| 2026-08-04T17:01 | sn120 | BURN_DROP | sn120 burn fell 1.000 -> 0.000 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

