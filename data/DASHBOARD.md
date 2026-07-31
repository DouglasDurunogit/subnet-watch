# Subnet watch — dashboard

_snapshot 2026-07-31T23:14:03Z · block 8745264 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 32 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85 | 567 | 567 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 78.1 | 113 | 28,587 | cpu-small | 20 | 89% |
| 3 | sn76 Phylax | 77.1 | 75.21 | 151 | cpu-small | 7 | 70% |
| 4 | sn67 Harnyx | 73.7 | 32.16 | 909 | cpu-small | 118 | 19% |
| 5 | sn62 Ridges | 70.9 | 973 | 4,481 | rtx4090* | 6 | 57% |
| 6 | sn56 Gradients | 69.6 | 661 | 1,219 | rtx4090* | 6 | 64% |
| 7 | sn26 Perturb | 68.9 | 24.95 | 205 | rtx3060 | 11 | 50% |
| 8 | sn85 Vidaio | 68.6 | 491 | 498 | rtx4090* | 10 | 16% |
| 9 | sn102 ConnitoAI | 68.2 | 428 | 1,716 | rtx4090* | 6 | 46% |
| 10 | sn15 ORO | 67.7 | 8.97 | 18.93 | cpu-small | 82 | 93% |
| 11 | sn124 Swarm | 66.9 | 302 | 701 | rtx4090* | 20 | 12% |
| 12 | sn38 ChronoLLM | 63.3 | 111 | 1,613 | rtx4090* | 10 | 52% |
| 13 | sn53 engy | 63.3 | 98.89 | 2,473 | rtx4090 | 34 | 13% |
| 14 | sn71 Leadpoet | 62.2 | 72.14 | 141 | rtx4090* | 11 | 71% |
| 15 | sn61 RedTeam | 58.4 | 22.38 | 106 | rtx4090* | 96 | 3% |
| 16 | sn51 lium.io | 56.7 | 20.08 | 6,669 | rtx4090* | 40 | 43% |
| 17 | sn28 gm | 56.3 | 13.28 | 3,062 | rtx4090* | 13 | 51% |
| 18 | sn9 iota | 55.2 | 8,435 | 14,860 | rtx4090* | 3 | 75% |
| 19 | sn97 Albedo | 52.9 | 3,204 | 3,204 = | rtx4090* | 5 | 20% |
| 20 | sn49 Nepher Robotics | 52.1 | 2,295 | 4,553 | rtx4090* | 2 | 99% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 23 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-31T23:14 | sn102 | RELEASE | sn102 released v0.4.0 |
| 2026-07-31T23:14 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 📊 telemetry: restore round + per-miner t |
| 2026-07-31T21:50 | sn74 | RELEASE | sn74 released release-20260731-214128: chore(weights): point all emiss |
| 2026-07-31T21:50 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: SparkDistill: 3x faster time-decay for me |
| 2026-07-31T21:50 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Merge pull request #16 from praxi-labs/va |
| 2026-07-31T18:52 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: release: enable validator auto-update 0. |
| 2026-07-31T17:12 | sn7 | BURN_DROP | sn7 burn fell 0.995 -> 0.926 - miners can earn again |
| 2026-07-31T17:12 | sn9 | RELEASE | sn9 released v4.9.2 |
| 2026-07-31T17:12 | sn15 | RELEASE | sn15 released v1.2.4 |
| 2026-07-31T17:12 | sn66 | BURN_DROP | sn66 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-31T17:12 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Allocate 90% of validator weight to burn |
| 2026-07-31T17:12 | sn102 | RELEASE | sn102 released v0.3.4 |
| 2026-07-31T17:12 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: fix: protect validator dashboard outbox |
| 2026-07-31T15:28 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: docs: align miner and validator release  |
| 2026-07-31T13:05 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Hold inference keys in the proxy, enforce |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

