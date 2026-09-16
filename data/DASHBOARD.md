# Subnet watch — dashboard

_snapshot 2026-09-16T01:22:32Z · block 9076895 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 4 | `██` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 37 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80 | 5,574 | 5,574 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 79.8 | 152 | 339 | cpu-small | 8 | 30% |
| 3 | sn91 cascade | 72.4 | 592 | 2,371 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 71.7 | 1,247 | 1,261 | rtx4090* | 4 | 29% |
| 5 | sn1 Apex | 69.4 | 628 | 858 | rtx4090* | 4 | 57% |
| 6 | sn107 Minos | 68.7 | 332 | 27,642 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.6 | 8.79 | 913 | cpu-small | 140 | 32% |
| 8 | sn111 Claims | 68.1 | 432 | 1,916 | rtx4090* | 5 | 60% |
| 9 | sn38 ChronoLLM | 66.5 | 113 | 1,543 | cpu-small | 10 | 52% |
| 10 | sn124 Swarm | 66.2 | 244 | 787 | rtx4090* | 25 | 11% |
| 11 | sn28 SayGM | 63.7 | 113 | 1,920 | rtx4090* | 49 | 14% |
| 12 | sn61 RedTeam | 62.8 | 88.37 | 132 | rtx4090* | 103 | 1% |
| 13 | sn81 Reliquary | 62.6 | 80.89 | 170 | rtx4090* | 40 | 15% |
| 14 | sn55 NIOME | 61.6 | 59.55 | 500 | rtx4090* | 11 | 29% |
| 15 | sn62 Ridges | 60.7 | 44.91 | 1,596 | rtx4090* | 19 | 26% |
| 16 | sn23 Trishool | 60.3 | 554 | 554 = | cpu-small | 2 | 80% |
| 17 | sn51 lium.io | 58.8 | 33.40 | 1,736 | rtx4090* | 64 | 82% |
| 18 | sn120 Affine | 56.7 | 15,768 | 15,768 = | rtx4090* | 2 | 50% |
| 19 | sn9 iota | 56.2 | 13,189 | 13,189 = | rtx4090* | 2 | 74% |
| 20 | sn80 OpenRoboto | 56 | 401 | 1,424 | rtx4090* | 5 | 43% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 14 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-16T01:23 | sn34 | RELEASE | sn34 released 5.0.5 — Generator Qualification & Paid Resubmissions |
| 2026-09-16T01:23 | sn62 | RELEASE | sn62 released v0.3.5 |
| 2026-09-16T01:23 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Verify current installer against signed f |
| 2026-09-15T23:01 | sn15 | RELEASE | sn15 released v2.0.18: search-server sync-worker fix + rebuilt base (O |
| 2026-09-15T23:01 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: test: :white_check_mark: Update tests to  |
| 2026-09-15T23:01 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs: FAQ from the first external miner's |
| 2026-09-15T23:01 | sn102 | RELEASE | sn102 released v0.6.0 — scheduled task switching |
| 2026-09-15T23:01 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: ⚡️ perf(validator): cap the in-shard eva |
| 2026-09-15T20:12 | sn15 | RELEASE | sn15 released v2.0.17 |
| 2026-09-15T20:12 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Fix generative callback staleness and val |
| 2026-09-15T20:12 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs: day-one fixes from the first third- |
| 2026-09-15T20:12 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #107 from Umi-BitSign/ |
| 2026-09-15T16:53 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix: harden validator API binding and ser |
| 2026-09-15T16:53 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Raise proof token limit to one million fo |
| 2026-09-15T16:53 | sn90 | RELEASE | sn90 released v1.2.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

