# Subnet watch — dashboard

_snapshot 2026-09-25T22:42:45Z · block 9147802 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 73 | 699 | 2,512 | cpu-small | 5 | 49% |
| 2 | sn1 Apex | 71.7 | 1,217 | 1,242 | rtx4090* | 4 | 51% |
| 3 | sn56 Gradients | 71.1 | 1,029 | 5,913 | rtx4090* | 8 | 41% |
| 4 | sn38 ChronoLLM | 70.1 | 318 | 2,795 | cpu-small | 10 | 52% |
| 5 | sn107 Minos | 69.2 | 384 | 31,605 | cpu-small | 20 | 79% |
| 6 | sn14 Cacheon | 69 | 555 | 2,539 | rtx4090* | 13 | 31% |
| 7 | sn15 ORO | 68.9 | 13.20 | 23.23 | cpu-small | 57 | 97% |
| 8 | sn4 Targon | 68.5 | 16,251 | 29,394 | rtx4090* | 5 | 58% |
| 9 | sn67 Harnyx | 68.5 | 8.22 | 1,456 | cpu-small | 127 | 41% |
| 10 | sn124 Swarm | 67.2 | 332 | 960 | rtx4090* | 25 | 11% |
| 11 | sn96 Verathos | 66.9 | 16.41 | 253 | rtx4090 | 77 | 31% |
| 12 | sn111 Claims | 66 | 237 | 3,290 | rtx4090* | 5 | 78% |
| 13 | sn3 Teutonic | 64.9 | 5,562 | 5,562 = | rtx4090* | 5 | 20% |
| 14 | sn28 SayGM | 63.4 | 105 | 1,106 | rtx4090* | 59 | 19% |
| 15 | sn23 Trishool | 62.3 | 1,004 | 1,004 = | cpu-small | 2 | 80% |
| 16 | sn62 Ridges | 61.6 | 60.58 | 1,762 | rtx4090* | 21 | 19% |
| 17 | sn26 Perturb | 61.1 | 53.94 | 59.21 | rtx3060 | 5 | 90% |
| 18 | sn61 RedTeam | 60.7 | 46.62 | 324 | rtx4090* | 127 | 3% |
| 19 | sn100 Cortex | 60 | 37.24 | 252 | rtx4090* | 19 | 70% |
| 20 | sn102 ConnitoAI | 59.2 | 29.22 | 2,198 | rtx4090* | 8 | 36% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 22 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-25T22:43 | sn1 | RELEASE | sn1 released v4.4.10 |
| 2026-09-25T19:26 | sn15 | RELEASE | sn15 released v2.0.31: fix(proxy): re-resolve Backend host for allowli |
| 2026-09-25T19:26 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: refactor(validator): simplify session cal |
| 2026-09-25T19:26 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve terminal verified intent evidenc |
| 2026-09-25T19:26 | sn74 | RELEASE | sn74 released release-20260925-183535 |
| 2026-09-25T19:26 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: test(network): verify opentype 75/25 sea |
| 2026-09-25T15:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: competition: clarify staging finalization |
| 2026-09-25T15:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3467 - [P2] validator: inspect after  |
| 2026-09-25T15:24 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Withhold a miner's source while it is on  |
| 2026-09-25T15:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified activity repair to committe |
| 2026-09-25T15:24 | sn102 | RELEASE | sn102 released v0.6.4 — the reference miner trains the full model |
| 2026-09-25T15:24 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #283 from Connito-AI/ |
| 2026-09-25T15:24 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs(miner): update V1 consensus review  |
| 2026-09-25T15:24 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-09-25T10:09 | sn51 | RELEASE | sn51 released miner-v1.005 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

