# Subnet watch — dashboard

_snapshot 2026-08-30T20:04:58Z · block 8960292 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.9 | 5,517 | 5,517 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 79.4 | 137 | 1,344 | cpu-small | 10 | 42% |
| 3 | sn3 Teutonic | 75.7 | 4,030 | 4,030 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 75.1 | 46.84 | 178 | cpu-small | 21 | 20% |
| 5 | sn23 Trishool | 72.3 | 569 | 569 = | cpu-small | 2 | 80% |
| 6 | sn102 ConnitoAI | 72.1 | 1,378 | 1,697 | rtx4090* | 5 | 28% |
| 7 | sn67 Harnyx | 72 | 19.78 | 861 | cpu-small | 132 | 23% |
| 8 | sn111 Claims | 70.8 | 952 | 3,353 | rtx4090* | 3 | 70% |
| 9 | sn15 ORO | 70.7 | 21.54 | 42.59 | cpu-small | 74 | 93% |
| 10 | sn21 AdTAO | 68.9 | 10.45 | 243 | cpu-small | 14 | 45% |
| 11 | sn96 Verathos | 68.1 | 21.34 | 176 | rtx4090 | 73 | 51% |
| 12 | sn56 Gradients | 67.3 | 326 | 666 | rtx4090* | 7 | 71% |
| 13 | sn91 cascade | 67.2 | 319 | 645 | rtx4090* | 5 | 52% |
| 14 | sn124 Swarm | 66.8 | 297 | 962 | rtx4090* | 25 | 11% |
| 15 | sn79 MVTRX | 66.1 | 4.86 | 477 | cpu-small | 217 | 10% |
| 16 | sn108 Prometheon | 65.4 | 186 | 492 | rtx4090* | 9 | 26% |
| 17 | sn80 OpenRoboto | 65 | 165 | 600 | rtx4090* | 5 | 71% |
| 18 | sn81 Reliquary | 64.7 | 153 | 285 | rtx4090* | 31 | 6% |
| 19 | sn61 RedTeam | 64.6 | 149 | 223 | rtx4090* | 42 | 4% |
| 20 | sn107 Minos | 64.6 | 128 | 38,490 | cpu-small | 20 | 90% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 16 |
| captured (>90%) | 28 |

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
| 2026-08-30T20:05 | sn25 | RELEASE | sn25 released v2026.8.30-1033129380 |
| 2026-08-30T17:40 | sn15 | RELEASE | sn15 released v1.2.11 |
| 2026-08-30T17:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(reporting): tenure rows state how man |
| 2026-08-30T13:20 | sn9 | RELEASE | sn9 released v4.12.10 |
| 2026-08-30T13:20 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(validator): stop implying a second v |
| 2026-08-30T13:20 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-08-30T07:32 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator-api): serve the daily feeds |
| 2026-08-30T07:32 | sn45 | README_TASK_DIFF | sn45 README task/scoring sections changed |
| 2026-08-30T07:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-30T07:32 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Satisfy strict typing across the validato |
| 2026-08-30T01:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Document miner SOURCE_ADD inputs (#153) |
| 2026-08-30T01:45 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-08-30T01:45 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scoring: the points qualify gate, and the |
| 2026-08-30T01:45 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Validate commitments at discovery, guard  |
| 2026-08-29T23:29 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scoring: the points gate is per competiti |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

