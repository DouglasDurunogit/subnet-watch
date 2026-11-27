# Subnet watch — dashboard

_snapshot 2026-11-27T00:03:35Z · block 9594479 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 129

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 129 | everything on chain |
| Pays miners at all | 104 | `miner_burn` < 0.99 |
| Ranked | 104 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 80.9 | 195 | 195 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 75.5 | 3,897 | 3,897 = | rtx4090* | 5 | 20% |
| 3 | sn53 engy | 72.2 | 1,430 | 3,383 | rtx4090 | 8 | 49% |
| 4 | sn121 sundae_bar | 71.4 | 434 | 695 | cpu-small | 3 | 50% |
| 5 | sn124 Swarm | 64.9 | 171 | 1,137 | rtx4090* | 10 | 29% |
| 6 | sn67 Harnyx | 64.1 | 1.87 | 453 | cpu-small | 95 | 35% |
| 7 | sn66 conjectures | 62.1 | 68.92 | 850 | rtx4090* | 4 | 81% |
| 8 | sn54 Yanez | 61.6 | 2,087 | 2,087 = | a4000 | 2 | 96% |
| 9 | sn58 Attune | 61.1 | 52.54 | 1,498 | rtx4090* | 57 | 30% |
| 10 | sn3 Teutonic | 60.8 | 1,676 | 1,676 = | rtx4090* | 4 | 40% |
| 11 | sn28 SayGM | 60.4 | 45.16 | 1,121 | rtx4090* | 110 | 22% |
| 12 | sn111 Claims | 59.8 | 35.50 | 145 | rtx4090* | 4 | 88% |
| 13 | sn97 Ingot | 59.5 | 1,130 | 1,130 = | rtx4090* | 4 | 25% |
| 14 | sn117 everyframe.studi | 59 | 27.88 | 444 | rtx4090* | 30 | 18% |
| 15 | sn56 Gradients | 58.6 | 167 | 3,120 | a100-80 | 7 | 43% |
| 16 | sn127 Zils | 58.5 | 23.42 | 44.53 | rtx4090 | 6 | 88% |
| 17 | sn25 UR | 58 | 19.54 | 28.79 | rtx4090* | 10 | 45% |
| 18 | sn34 Yugos | 57.6 | 654 | 5,326 | rtx4090* | 3 | 84% |
| 19 | sn1 Apex | 57.1 | 556 | 567 | rtx4090* | 4 | 52% |
| 20 | sn102 ConnitoAI | 55.7 | 366 | 366 = | rtx4090* | 5 | 25% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 22 |
| captured (>90%) | 28 |

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
| 2026-11-27T00:03 | sn6 | README_TASK_DIFF | sn6 README task/scoring sections changed |
| 2026-11-27T00:03 | sn12 | RELEASE | sn12 released miner-staging-2026-11-26-45857591810-467-1: fix: stop th |
| 2026-11-27T00:03 | sn51 | RELEASE | sn51 released watchtower-v1.2.5 |
| 2026-11-27T00:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5238 - [P4] Validator reads liumd's c |
| 2026-11-27T00:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Explain consensus-based payouts before a  |
| 2026-11-27T00:03 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(attestation): registry-lookup verifi |
| 2026-11-27T00:03 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Roll guest-TLS and miner-mode sealed hote |
| 2026-11-27T00:03 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge miner error rows 630c36c4 onto the |
| 2026-11-27T00:03 | sn117 | RELEASE | sn117 released everycli v1.3.4 |
| 2026-11-27T00:03 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |
| 2026-11-26T15:34 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Start the scored span at the cold-round r |
| 2026-11-26T15:34 | sn42 | RELEASE | sn42 released v0.6.27 |
| 2026-11-26T15:34 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: miners: work an improvement job; the prac |
| 2026-11-26T15:34 | sn42 | README_TASK_DIFF | sn42 README task/scoring sections changed |
| 2026-11-26T15:34 | sn51 | RELEASE | sn51 released executor-v1.201 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

