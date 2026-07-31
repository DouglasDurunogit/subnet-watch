# Subnet watch — dashboard

_snapshot 2026-07-31T20:35:22Z · block 8744471 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 11 | `█████` |
| ≥0.99 dead | 31 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 572 | 572 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.9 | 107 | 28,838 | cpu-small | 20 | 88% |
| 3 | sn76 Phylax | 77.2 | 76.01 | 153 | cpu-small | 7 | 70% |
| 4 | sn67 Harnyx | 73.8 | 32.66 | 923 | cpu-small | 118 | 19% |
| 5 | sn62 Ridges | 70.9 | 969 | 4,462 | rtx4090* | 6 | 57% |
| 6 | sn56 Gradients | 69.6 | 663 | 1,223 | rtx4090* | 6 | 64% |
| 7 | sn102 ConnitoAI | 69.1 | 558 | 1,644 | rtx4090* | 5 | 44% |
| 8 | sn26 Perturb | 68.9 | 25.16 | 207 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 67.5 | 8.99 | 18.97 | cpu-small | 82 | 93% |
| 10 | sn85 Vidaio | 67.4 | 338 | 588 | rtx4090* | 10 | 19% |
| 11 | sn124 Swarm | 66.9 | 304 | 705 | rtx4090* | 20 | 12% |
| 12 | sn38 ChronoLLM | 63.3 | 112 | 1,620 | rtx4090* | 10 | 52% |
| 13 | sn53 engy | 63.3 | 99.57 | 2,489 | rtx4090 | 34 | 13% |
| 14 | sn71 Leadpoet | 62.2 | 72.30 | 142 | rtx4090* | 11 | 71% |
| 15 | sn61 RedTeam | 58.3 | 21.57 | 104 | rtx4090* | 96 | 3% |
| 16 | sn28 gm | 58.1 | 22.24 | 2,746 | rtx4090* | 13 | 55% |
| 17 | sn51 lium.io | 56.1 | 17.84 | 5,120 | rtx4090* | 42 | 52% |
| 18 | sn9 iota | 55.2 | 8,369 | 14,386 | rtx4090* | 3 | 72% |
| 19 | sn97 Albedo | 52.9 | 3,205 | 3,205 = | rtx4090* | 5 | 20% |
| 20 | sn49 Nepher Robotics | 52.1 | 2,328 | 4,618 | rtx4090* | 2 | 99% |

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
| concentrated (30–60%) | 24 |
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
| 2026-07-31T11:05 | sn8 | BURN_DROP | sn8 burn fell 0.998 -> 0.000 - miners can earn again |
| 2026-07-31T11:05 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Evaluate two agents at a time within a tr |
| 2026-07-31T08:08 | sn80 | SCORING_COMMIT | sn80 commit touches scoring: docs: document public /api/v1/scan-reject |
| 2026-07-30T23:33 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: create subaccount elimination cache on ent |
| 2026-07-30T23:33 | sn62 | RELEASE | sn62 released v0.2.3 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

