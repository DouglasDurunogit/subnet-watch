# Subnet watch — dashboard

_snapshot 2026-08-29T15:09:57Z · block 8951617 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 76.3 | 62.80 | 1,146 | cpu-small | 9 | 67% |
| 2 | sn3 Teutonic | 75.7 | 4,051 | 4,051 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 75.2 | 47.75 | 193 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 73 | 26.70 | 502 | cpu-small | 116 | 13% |
| 5 | sn102 ConnitoAI | 71 | 1,011 | 2,369 | rtx4090* | 6 | 38% |
| 6 | sn15 ORO | 70.7 | 22.25 | 23,201 | cpu-small | 70 | 94% |
| 7 | sn96 Verathos | 68.7 | 24.14 | 134 | rtx4090 | 79 | 41% |
| 8 | sn56 Gradients | 68.4 | 453 | 1,078 | rtx4090* | 7 | 70% |
| 9 | sn80 OpenRoboto | 67.9 | 400 | 1,805 | rtx4090* | 5 | 71% |
| 10 | sn111 Claims | 67.6 | 381 | 3,400 | rtx4090* | 5 | 70% |
| 11 | sn91 cascade | 67.3 | 328 | 665 | rtx4090* | 5 | 52% |
| 12 | sn124 Swarm | 66.7 | 284 | 874 | rtx4090* | 25 | 11% |
| 13 | sn79 MVTRX | 66.2 | 4.43 | 462 | cpu-small | 227 | 10% |
| 14 | sn61 RedTeam | 65 | 165 | 252 | rtx4090* | 39 | 4% |
| 15 | sn107 Minos | 64.5 | 126 | 37,306 | cpu-small | 20 | 90% |
| 16 | sn81 Reliquary | 64 | 123 | 232 | rtx4090* | 37 | 5% |
| 17 | sn54 Yanez | 64 | 6.19 | 1,061 | a4000 | 102 | 35% |
| 18 | sn121 sundae_bar | 62.9 | 1,214 | 1,214 = | cpu-small | 2 | 61% |
| 19 | sn65 True Performance | 62.8 | 94.41 | 197 | rtx4090* | 6 | 75% |
| 20 | sn55 NIOME | 62.3 | 73.65 | 606 | rtx4090* | 11 | 29% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 20 |
| captured (>90%) | 29 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-29T15:10 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): honour the reference exemp |
| 2026-08-29T15:10 | sn49 | BURN_DROP | sn49 burn fell 0.990 -> 0.000 - miners can earn again |
| 2026-08-29T15:10 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: chore(config): shorten validator query i |
| 2026-08-29T10:19 | sn25 | RELEASE | sn25 released v2026.8.28-1031763440 |
| 2026-08-29T10:19 | sn47 | SCORING_COMMIT | sn47 commit touches scoring: rollout verification rules |
| 2026-08-29T10:19 | sn47 | README_TASK_DIFF | sn47 README task/scoring sections changed |
| 2026-08-29T10:19 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-29T10:19 | sn100 | README_TASK_DIFF | sn100 README task/scoring sections changed |
| 2026-08-29T03:23 | sn15 | RELEASE | sn15 released v1.2.10 |
| 2026-08-29T03:23 | sn25 | RELEASE | sn25 released v2026.8.28-1031618120 |
| 2026-08-28T21:28 | sn15 | RELEASE | sn15 released v1.2.9 |
| 2026-08-28T21:28 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): use revealed top as weigh |
| 2026-08-28T21:28 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(reporting): each miner's row carries |
| 2026-08-28T21:28 | sn25 | RELEASE | sn25 released v2026.8.28-1031286130 |
| 2026-08-28T21:28 | sn28 | RELEASE | sn28 released v0.4.12 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

