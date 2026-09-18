# Subnet watch — dashboard

_snapshot 2026-09-18T17:49:37Z · block 9096127 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 77.8 | 7,575 | 21,266 | rtx4090* | 6 | 51% |
| 2 | sn3 Teutonic | 76.3 | 4,817 | 4,817 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.7 | 636 | 2,546 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 71.2 | 1,049 | 1,401 | rtx4090* | 6 | 29% |
| 5 | sn67 Harnyx | 69.2 | 9.97 | 1,275 | cpu-small | 112 | 41% |
| 6 | sn107 Minos | 68.8 | 338 | 28,616 | cpu-small | 20 | 80% |
| 7 | sn56 Gradients | 68.3 | 451 | 5,336 | rtx4090* | 9 | 46% |
| 8 | sn124 Swarm | 66.6 | 280 | 897 | rtx4090* | 25 | 11% |
| 9 | sn15 ORO | 66.6 | 8.39 | 19,692 | cpu-small | 50 | 98% |
| 10 | sn38 ChronoLLM | 65.9 | 98.92 | 875 | cpu-small | 10 | 52% |
| 11 | sn104 TAOstatus | 65.6 | 10.41 | 10.44 | cpu-small | 5 | 99% |
| 12 | sn111 Claims | 65 | 187 | 2,853 | rtx4090* | 5 | 80% |
| 13 | sn62 Ridges | 63.7 | 112 | 1,660 | rtx4090* | 21 | 21% |
| 14 | sn74 Gittensor | 61.2 | 58.58 | 242 | rtx4090* | 10 | 62% |
| 15 | sn81 Reliquary | 60.4 | 41.46 | 113 | rtx4090* | 34 | 62% |
| 16 | sn51 lium.io | 59.7 | 43.04 | 1,450 | rtx4090* | 65 | 83% |
| 17 | sn28 SayGM | 58.5 | 24.94 | 4,225 | rtx4090* | 57 | 28% |
| 18 | sn61 RedTeam | 58.2 | 23.20 | 2,100 | rtx4090* | 122 | 21% |
| 19 | sn80 OpenRoboto | 56.6 | 477 | 1,688 | rtx4090* | 5 | 43% |
| 20 | sn9 iota | 56.3 | 13,655 | 13,655 = | rtx4090* | 2 | 68% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 17 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-18T17:50 | sn12 | RELEASE | sn12 released validator-staging-2026-09-18-35368036673-626-1: fix: evi |
| 2026-09-18T17:50 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix: evict old neurons in allowance evict |
| 2026-09-18T17:50 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: validator: hard-fail generated runs at >= |
| 2026-09-18T17:50 | sn25 | RELEASE | sn25 released v2026.9.18-1049469180 |
| 2026-09-18T17:50 | sn28 | RELEASE | sn28 released v0.4.19 |
| 2026-09-18T17:50 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Clarify validator credentials and require |
| 2026-09-18T17:50 | sn74 | RELEASE | sn74 released release-20260918-164355 |
| 2026-09-18T17:50 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs: client-facing attestation of infere |
| 2026-09-18T17:50 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: Added scored_output the judge-facin |
| 2026-09-18T17:50 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs: document funding-lineage miner sel |
| 2026-09-18T14:27 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add category-stratified evaluation samplin |
| 2026-09-18T14:27 | sn9 | RELEASE | sn9 released v4.13.1 |
| 2026-09-18T14:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse exact retained miner scores for Sep |
| 2026-09-18T14:27 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: Merge pull request #13 from taostatus/fe |
| 2026-09-18T09:58 | sn25 | RELEASE | sn25 released v2026.9.17-1049083750 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

