# Subnet watch — dashboard

_snapshot 2026-08-05T00:53:27Z · block 8774548 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 11 | `██████` |
| ≥0.99 dead | 36 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.6 | 514 | 514 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.4 | 95.76 | 28,307 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.3 | 79.52 | 160 | cpu-small | 7 | 67% |
| 4 | sn60 Bitsec.ai | 76.8 | 2,163 | 2,163 = | cpu-small | 2 | 90% |
| 5 | sn98 NeverPlayAlone | 76 | 1,695 | 1,695 = | cpu-small | 1 | 100% |
| 6 | sn114 SOMA | 72.5 | 1,575 | 4,107 | rtx4090* | 3 | 65% |
| 7 | sn67 Harnyx | 72.1 | 21.65 | 730 | cpu-small | 157 | 17% |
| 8 | sn62 Ridges | 69.2 | 588 | 2,127 | rtx4090* | 7 | 35% |
| 9 | sn26 Perturb | 68.9 | 25.27 | 200 | rtx3060 | 11 | 50% |
| 10 | sn15 ORO | 67.4 | 8.52 | 18.56 | cpu-small | 76 | 94% |
| 11 | sn124 Swarm | 66.2 | 243 | 614 | rtx4090* | 22 | 10% |
| 12 | sn38 ChronoLLM | 65.5 | 206 | 3,466 | rtx4090* | 10 | 52% |
| 13 | sn41 Almanac | 65.4 | 4.60 | 66.90 | cpu-small | 36 | 89% |
| 14 | sn21 AdTAO | 65.3 | 4.53 | 21.06 | cpu-small | 142 | 45% |
| 15 | sn74 Gittensor | 65.2 | 181 | 302 | rtx4090* | 9 | 18% |
| 16 | sn53 engy | 64.1 | 128 | 2,766 | rtx4090 | 28 | 17% |
| 17 | sn28 gm | 62.8 | 88.03 | 1,004 | rtx4090* | 18 | 63% |
| 18 | sn80 OpenRoboto | 62.3 | 72.81 | 276 | rtx4090* | 4 | 91% |
| 19 | sn102 ConnitoAI | 60.1 | 37.56 | 3,738 | rtx4090* | 4 | 73% |
| 20 | sn101 Tag101 | 58.9 | 0.10 | 0.77 | cpu-small | 240 | 90% |

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
| dominated (60–90%) | 23 |
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
| 2026-08-05T00:53 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Improve silver alignment and scoring |
| 2026-08-04T23:16 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #473 from ridgesai/upd |
| 2026-08-04T18:47 | sn12 | RELEASE | sn12 released validator-staging-2026-08-04-30935079890-625-1: chore: b |
| 2026-08-04T18:47 | sn21 | RELEASE | sn21 released archive/per-cell-consensus-2026-06: feat(consensus): epo |
| 2026-08-04T18:47 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(validator): burn follows Rob's dated |
| 2026-08-04T18:47 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-04T18:47 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Release validator deployment gate 0.2.4 |
| 2026-08-04T17:01 | sn62 | RELEASE | sn62 released v0.2.4 |
| 2026-08-04T17:01 | sn120 | BURN_DROP | sn120 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-04T12:25 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.968 - miners can earn again |
| 2026-08-04T12:25 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Improve agent validation and source grou |
| 2026-08-04T12:25 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Improve validation and sandbox dispatch  |
| 2026-08-04T12:25 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Ensure validators adopt the 70 percent b |
| 2026-08-04T12:25 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |
| 2026-08-04T10:09 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #11 from conjectures-i |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

