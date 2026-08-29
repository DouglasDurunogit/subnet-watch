# Subnet watch — dashboard

_snapshot 2026-08-29T21:20:03Z · block 8953467 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 76.2 | 61.42 | 1,121 | cpu-small | 9 | 67% |
| 2 | sn3 Teutonic | 75.7 | 4,072 | 4,072 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 75.1 | 47.04 | 190 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 73 | 26.12 | 492 | cpu-small | 116 | 13% |
| 5 | sn15 ORO | 70.7 | 21.51 | 41.80 | cpu-small | 70 | 94% |
| 6 | sn21 AdTAO | 70.2 | 14.32 | 612 | cpu-small | 14 | 45% |
| 7 | sn102 ConnitoAI | 69 | 543 | 2,110 | rtx4090* | 7 | 34% |
| 8 | sn96 Verathos | 68.5 | 23.16 | 165 | rtx4090 | 79 | 41% |
| 9 | sn56 Gradients | 68.3 | 448 | 1,068 | rtx4090* | 7 | 70% |
| 10 | sn80 OpenRoboto | 68 | 409 | 1,848 | rtx4090* | 5 | 71% |
| 11 | sn111 Claims | 67.7 | 387 | 3,448 | rtx4090* | 5 | 70% |
| 12 | sn91 cascade | 67.1 | 316 | 640 | rtx4090* | 5 | 52% |
| 13 | sn124 Swarm | 66.7 | 288 | 885 | rtx4090* | 25 | 11% |
| 14 | sn79 MVTRX | 66.4 | 4.43 | 407 | cpu-small | 226 | 9% |
| 15 | sn61 RedTeam | 64.6 | 149 | 221 | rtx4090* | 40 | 4% |
| 16 | sn81 Reliquary | 64.6 | 146 | 263 | rtx4090* | 36 | 6% |
| 17 | sn107 Minos | 64.5 | 125 | 37,057 | cpu-small | 20 | 90% |
| 18 | sn54 Yanez | 64.1 | 6.26 | 1,051 | a4000 | 102 | 35% |
| 19 | sn55 NIOME | 63.2 | 95.50 | 614 | rtx4090* | 10 | 30% |
| 20 | sn121 sundae_bar | 63 | 1,249 | 1,249 = | cpu-small | 2 | 60% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 18 |
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
| 2026-08-29T21:20 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: limit-watcher: a miner-drawn band survive |
| 2026-08-29T18:44 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(reporting): a published tier must mea |
| 2026-08-29T18:44 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Measure admitted model verifier latency |
| 2026-08-29T18:44 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: grade the band the miner declared, no |
| 2026-08-29T18:44 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validator): preserve completed run s |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

