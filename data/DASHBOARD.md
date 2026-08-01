# Subnet watch — dashboard

_snapshot 2026-08-01T23:28:25Z · block 8752533 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 34 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85 | 567 | 567 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 77.1 | 74.87 | 151 | cpu-small | 7 | 70% |
| 3 | sn107 Minos | 76.9 | 86.72 | 29,031 | cpu-small | 19 | 90% |
| 4 | sn67 Harnyx | 72.9 | 26.25 | 958 | cpu-small | 132 | 21% |
| 5 | sn102 ConnitoAI | 70.6 | 895 | 1,007 | rtx4090* | 5 | 26% |
| 6 | sn62 Ridges | 70.3 | 820 | 1,311 | rtx4090* | 6 | 57% |
| 7 | sn26 Perturb | 69.7 | 31.11 | 929 | rtx3060 | 11 | 51% |
| 8 | sn56 Gradients | 69.2 | 577 | 1,215 | rtx4090* | 6 | 64% |
| 9 | sn85 Vidaio | 68.2 | 435 | 515 | rtx4090* | 10 | 17% |
| 10 | sn15 ORO | 68 | 9.30 | 18.55 | cpu-small | 65 | 94% |
| 11 | sn74 Gittensor | 66.3 | 246 | 249 | rtx4090* | 7 | 40% |
| 12 | sn124 Swarm | 66 | 231 | 678 | rtx4090* | 20 | 12% |
| 13 | sn38 ChronoLLM | 63.2 | 108 | 1,570 | rtx4090* | 10 | 52% |
| 14 | sn53 engy | 63 | 90.94 | 2,289 | rtx4090 | 34 | 13% |
| 15 | sn71 Leadpoet | 62.7 | 83.12 | 169 | rtx4090* | 10 | 70% |
| 16 | sn28 gm | 61.2 | 54.67 | 2,248 | rtx4090* | 12 | 55% |
| 17 | sn101 Tag101 | 58.5 | 0.13 | 0.96 | cpu-small | 240 | 90% |
| 18 | sn61 RedTeam | 58.3 | 21.68 | 89.27 | rtx4090* | 97 | 3% |
| 19 | sn9 iota | 54.8 | 7,075 | 12,915 | rtx4090* | 3 | 65% |
| 20 | sn97 Albedo | 52.8 | 3,062 | 3,062 = | rtx4090* | 5 | 20% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 22 |
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
| 2026-08-01T23:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Protect validator settlement constants |
| 2026-08-01T21:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix baseline replay and compact weight va |
| 2026-08-01T21:07 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Wire production Silver run metadata into |
| 2026-08-01T20:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh validator ancestry workflow manif |
| 2026-08-01T17:45 | sn99 | BURN_DROP | sn99 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-01T16:29 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Wire silver adjudication into validator  |
| 2026-08-01T14:06 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Fly next-epoch seeds for pre-evaluation  |
| 2026-08-01T12:13 | sn103 | RELEASE | sn103 released v2007 |
| 2026-08-01T12:13 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: release v2007 |
| 2026-08-01T11:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind v8 artifact verification into protec |
| 2026-08-01T09:32 | sn61 | RELEASE | sn61 released 4.8.2 |
| 2026-08-01T09:32 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: set default value for user_id in _co |
| 2026-08-01T09:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-01T09:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate concurrent restart state continu |
| 2026-08-01T09:32 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: docs: introduce Poker44 evaluation netwo |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

