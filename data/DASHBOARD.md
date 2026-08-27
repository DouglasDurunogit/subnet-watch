# Subnet watch — dashboard

_snapshot 2026-08-27T03:26:25Z · block 8933701 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn60 Bitsec.ai | 76.3 | 1,877 | 1,877 = | cpu-small | 2 | 50% |
| 2 | sn3 Teutonic | 75.5 | 3,812 | 3,812 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 75.5 | 52.00 | 498 | cpu-small | 20 | 25% |
| 4 | sn23 Trishool | 72.2 | 555 | 555 = | cpu-small | 2 | 80% |
| 5 | sn102 ConnitoAI | 71.9 | 1,290 | 2,389 | rtx4090* | 5 | 35% |
| 6 | sn15 ORO | 70.9 | 23.24 | 44.32 | cpu-small | 96 | 92% |
| 7 | sn67 Harnyx | 70.6 | 14.76 | 262 | cpu-small | 138 | 7% |
| 8 | sn1 Apex | 70 | 751 | 1,289 | rtx4090* | 4 | 58% |
| 9 | sn91 cascade | 68.9 | 547 | 1,472 | rtx4090* | 5 | 52% |
| 10 | sn56 Gradients | 68.5 | 468 | 1,113 | rtx4090* | 7 | 70% |
| 11 | sn124 Swarm | 66.8 | 295 | 886 | rtx4090* | 25 | 10% |
| 12 | sn61 RedTeam | 65.3 | 181 | 254 | rtx4090* | 32 | 5% |
| 13 | sn28 gm | 65 | 167 | 976 | rtx4090* | 37 | 44% |
| 14 | sn107 Minos | 64.8 | 135 | 40,619 | cpu-small | 20 | 90% |
| 15 | sn98 NeverPlayAlone | 64.7 | 2,044 | 2,044 = | cpu-small | 1 | 100% |
| 16 | sn121 sundae_bar | 63.1 | 1,280 | 1,280 = | cpu-small | 2 | 60% |
| 17 | sn81 Reliquary | 63.1 | 94.14 | 322 | rtx4090* | 42 | 7% |
| 18 | sn54 Yanez | 60.7 | 2.08 | 1,141 | a4000 | 94 | 44% |
| 19 | sn108 Prometheon | 60.5 | 44.26 | 136 | rtx4090* | 9 | 29% |
| 20 | sn51 lium.io | 60.3 | 49.12 | 2,785 | rtx4090* | 57 | 72% |

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
| dominated (60–90%) | 13 |
| captured (>90%) | 27 |

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
| 2026-08-27T03:26 | sn25 | RELEASE | sn25 released v2026.8.26-1029908500 |
| 2026-08-26T22:23 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.910 - miners can earn again |
| 2026-08-26T22:23 | sn28 | RELEASE | sn28 released v0.4.11 |
| 2026-08-26T22:23 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Submit one epoch of reward points to the  |
| 2026-08-26T22:23 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: rewards: top five per track, split 40/25/ |
| 2026-08-26T22:23 | sn76 | README_TASK_DIFF | sn76 README task/scoring sections changed |
| 2026-08-26T22:23 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs(validator): add mainnet profile and |
| 2026-08-26T19:17 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: updating UAV all miners not just the quer |
| 2026-08-26T19:17 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat: verify the submitter violating cla |
| 2026-08-26T16:06 | sn25 | RELEASE | sn25 released v2026.8.26-1029569170 |
| 2026-08-26T14:29 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #56 from score-technol |
| 2026-08-26T13:33 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(proof): release a finished plan's min |
| 2026-08-26T13:33 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Merge feat/mirrored-scoring: submit anot |
| 2026-08-26T12:18 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(rewards): one-payer receipt fingerpri |
| 2026-08-26T12:18 | sn28 | RELEASE | sn28 released v0.4.11-dev |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

