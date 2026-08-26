# Subnet watch — dashboard

_snapshot 2026-08-26T22:22:49Z · block 8932183 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.1 | 77.21 | 387 | cpu-small | 20 | 20% |
| 2 | sn60 Bitsec.ai | 76.1 | 1,787 | 1,787 = | cpu-small | 2 | 50% |
| 3 | sn3 Teutonic | 75.4 | 3,732 | 3,732 = | rtx4090* | 5 | 20% |
| 4 | sn23 Trishool | 72.1 | 535 | 535 = | cpu-small | 2 | 80% |
| 5 | sn102 ConnitoAI | 71.4 | 1,112 | 2,232 | rtx4090* | 6 | 35% |
| 6 | sn15 ORO | 70.9 | 22.62 | 43.16 | cpu-small | 96 | 92% |
| 7 | sn67 Harnyx | 70.5 | 14.35 | 255 | cpu-small | 138 | 7% |
| 8 | sn1 Apex | 70 | 742 | 1,273 | rtx4090* | 4 | 57% |
| 9 | sn91 cascade | 69.8 | 695 | 2,803 | rtx4090* | 5 | 52% |
| 10 | sn56 Gradients | 69.6 | 650 | 1,073 | rtx4090* | 6 | 74% |
| 11 | sn26 Perturb | 68.5 | 23.42 | 440 | rtx3060 | 10 | 70% |
| 12 | sn124 Swarm | 66.7 | 285 | 857 | rtx4090* | 25 | 10% |
| 13 | sn61 RedTeam | 65.1 | 171 | 241 | rtx4090* | 32 | 4% |
| 14 | sn107 Minos | 64.8 | 133 | 39,782 | cpu-small | 20 | 90% |
| 15 | sn28 gm | 64.6 | 150 | 1,631 | rtx4090* | 40 | 29% |
| 16 | sn121 sundae_bar | 63 | 1,223 | 1,223 = | cpu-small | 2 | 61% |
| 17 | sn81 Reliquary | 62.9 | 89.64 | 332 | rtx4090* | 43 | 8% |
| 18 | sn54 Yanez | 62.2 | 3.54 | 1,127 | a4000 | 135 | 35% |
| 19 | sn38 ChronoLLM | 59.3 | 419 | 1,619 | cpu-small | 6 | 53% |
| 20 | sn108 Prometheon | 59.1 | 28.91 | 132 | rtx4090* | 9 | 29% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 14 |
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
| 2026-08-26T11:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2467, mixed scoring for partially ren |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

