# Subnet watch — dashboard

_snapshot 2026-08-01T01:01:49Z · block 8745803 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 32 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 570 | 570 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 77.9 | 92.48 | 155 | cpu-small | 4 | 82% |
| 3 | sn107 Minos | 77.6 | 99.56 | 29,511 | cpu-small | 20 | 91% |
| 4 | sn98 NeverPlayAlone | 76 | 1,734 | 1,734 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 73 | 27.02 | 1,015 | cpu-small | 130 | 21% |
| 6 | sn62 Ridges | 71 | 987 | 4,545 | rtx4090* | 6 | 57% |
| 7 | sn102 ConnitoAI | 70.8 | 929 | 929 = | rtx4090* | 4 | 25% |
| 8 | sn56 Gradients | 69.6 | 665 | 1,226 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 69 | 26.10 | 206 | rtx3060 | 11 | 50% |
| 10 | sn15 ORO | 67.7 | 9.32 | 19.64 | cpu-small | 82 | 93% |
| 11 | sn124 Swarm | 66.9 | 306 | 709 | rtx4090* | 20 | 12% |
| 12 | sn85 Vidaio | 64.9 | 163 | 618 | rtx4090* | 10 | 20% |
| 13 | sn38 ChronoLLM | 63.3 | 112 | 1,615 | rtx4090* | 10 | 52% |
| 14 | sn53 engy | 63.3 | 101 | 2,523 | rtx4090 | 34 | 13% |
| 15 | sn71 Leadpoet | 62.3 | 72.90 | 143 | rtx4090* | 11 | 71% |
| 16 | sn28 gm | 61.4 | 57.10 | 2,956 | rtx4090* | 12 | 53% |
| 17 | sn61 RedTeam | 58.5 | 23.07 | 109 | rtx4090* | 96 | 3% |
| 18 | sn51 lium.io | 56.2 | 17.97 | 6,832 | rtx4090* | 40 | 41% |
| 19 | sn9 iota | 55.2 | 8,471 | 14,956 | rtx4090* | 3 | 75% |
| 20 | sn97 Albedo | 52.9 | 3,238 | 3,238 = | rtx4090* | 5 | 20% |

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
| dominated (60–90%) | 22 |
| captured (>90%) | 26 |

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
| 2026-08-01T01:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound receipt ancestry validation and per |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

