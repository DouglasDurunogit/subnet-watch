# Subnet watch — dashboard

_snapshot 2026-11-27T08:16:04Z · block 9596941 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 129

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 129 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 27 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 80.9 | 198 | 198 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 76.4 | 4,984 | 4,984 = | rtx4090* | 4 | 25% |
| 3 | sn53 engy | 72.3 | 1,455 | 3,440 | rtx4090 | 8 | 49% |
| 4 | sn121 sundae_bar | 71.5 | 443 | 710 | cpu-small | 3 | 50% |
| 5 | sn124 Swarm | 65 | 174 | 1,158 | rtx4090* | 10 | 29% |
| 6 | sn67 Harnyx | 63.9 | 1.73 | 469 | cpu-small | 95 | 36% |
| 7 | sn56 Gradients | 62.1 | 473 | 3,185 | a100-80 | 7 | 43% |
| 8 | sn66 conjectures | 62.1 | 70.04 | 863 | rtx4090* | 4 | 81% |
| 9 | sn58 Attune | 61.1 | 54.58 | 1,549 | rtx4090* | 57 | 30% |
| 10 | sn28 SayGM | 61 | 53.05 | 1,273 | rtx4090* | 115 | 26% |
| 11 | sn3 Teutonic | 60.9 | 1,713 | 3,433 | rtx4090* | 4 | 40% |
| 12 | sn111 Claims | 59.9 | 36.22 | 147 | rtx4090* | 4 | 88% |
| 13 | sn127 Zils | 58.6 | 23.92 | 45.36 | rtx4090 | 6 | 88% |
| 14 | sn25 UR | 58.1 | 20.36 | 29.89 | rtx4090* | 10 | 45% |
| 15 | sn1 Apex | 57.1 | 551 | 564 | rtx4090* | 4 | 54% |
| 16 | sn117 everyframe.studi | 56.5 | 13.15 | 1,300 | rtx4090* | 28 | 45% |
| 17 | sn102 ConnitoAI | 55.7 | 367 | 367 = | rtx4090* | 5 | 25% |
| 18 | sn99 Axonry | 54.9 | 7,502 | 7,502 = | rtx4090* | 1 | 100% |
| 19 | sn38 ChronoLLM | 54.4 | 106 | 269 | cpu-small | 6 | 53% |
| 20 | sn107 Minos | 53.5 | 110 | 9,381 | cpu-small | 20 | 80% |

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
| concentrated (30–60%) | 28 |
| dominated (60–90%) | 22 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-27T08:16 | sn30 | RELEASE | sn30 released v0.1.4 — Archive resilience and horizon-maturity blend,  |
| 2026-11-27T08:16 | sn51 | RELEASE | sn51 released executor-v1.202 |
| 2026-11-27T08:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-7201 - [P4] Validator: report a resta |
| 2026-11-27T08:16 | sn61 | RELEASE | sn61 released 4.12.0 |
| 2026-11-27T08:16 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: refactor: update bot virus challenge vers |
| 2026-11-27T08:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Run standing funded experiments and verif |
| 2026-11-27T08:16 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(lane-d): public half throughput: warm |
| 2026-11-27T08:16 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: fix(rewards): fix SN116 Subtensor chain  |
| 2026-11-27T08:16 | sn127 | RELEASE | sn127 released Release d92abe3 |
| 2026-11-27T00:03 | sn6 | README_TASK_DIFF | sn6 README task/scoring sections changed |
| 2026-11-27T00:03 | sn12 | RELEASE | sn12 released miner-staging-2026-11-26-45857591810-467-1: fix: stop th |
| 2026-11-27T00:03 | sn51 | RELEASE | sn51 released watchtower-v1.2.5 |
| 2026-11-27T00:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5238 - [P4] Validator reads liumd's c |
| 2026-11-27T00:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Explain consensus-based payouts before a  |
| 2026-11-27T00:03 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(attestation): registry-lookup verifi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

