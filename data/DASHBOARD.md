# Subnet watch — dashboard

_snapshot 2026-10-06T00:23:42Z · block 9220305 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 79.2 | 339 | 422 | rtx3060 | 4 | 60% |
| 2 | sn23 Trishool | 74.6 | 1,119 | 1,119 = | cpu-small | 2 | 77% |
| 3 | sn41 Almanac | 73.8 | 34.72 | 101 | cpu-small | 126 | 31% |
| 4 | sn91 cascade | 72.2 | 556 | 2,226 | cpu-small | 5 | 52% |
| 5 | sn53 engy | 72 | 1,341 | 3,675 | rtx4090 | 14 | 22% |
| 6 | sn67 Harnyx | 69.2 | 9.76 | 1,257 | cpu-small | 138 | 40% |
| 7 | sn46 Instant | 69.1 | 222 | 261 | cpu-small | 8 | 51% |
| 8 | sn1 Apex | 69 | 546 | 1,042 | rtx4090* | 4 | 66% |
| 9 | sn80 OpenRoboto | 68.6 | 487 | 2,203 | rtx4090* | 8 | 25% |
| 10 | sn15 ORO | 67.6 | 9.70 | 19.30 | cpu-small | 51 | 98% |
| 11 | sn4 Targon | 67.2 | 10,984 | 32,384 | rtx4090* | 5 | 70% |
| 12 | sn111 Claims | 65.8 | 215 | 2,599 | rtx4090* | 6 | 69% |
| 13 | sn14 Cacheon | 64.5 | 145 | 241 | rtx4090* | 6 | 91% |
| 14 | sn62 Ridges | 64 | 123 | 1,633 | rtx4090* | 33 | 19% |
| 15 | sn65 True Performance | 62.5 | 82.56 | 173 | rtx4090* | 6 | 75% |
| 16 | sn61 RedTeam | 61.8 | 66.92 | 121 | rtx4090* | 117 | 1% |
| 17 | sn28 SayGM | 60.1 | 40.56 | 2,776 | rtx4090* | 71 | 28% |
| 18 | sn107 Minos | 59 | 408 | 27,889 | cpu-small | 20 | 77% |
| 19 | sn5 Hone | 58.5 | 38.38 | 41.52 | rtx4090* | 244 | 0% |
| 20 | sn74 Gittensor | 58.1 | 24.35 | 277 | rtx4090* | 21 | 50% |

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
| wide (<30%) | 21 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-06T00:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge executable root validator registrat |
| 2026-10-06T00:24 | sn51 | RELEASE | sn51 released executor-v1.137 |
| 2026-10-06T00:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] verifyx: vendor libverif |
| 2026-10-06T00:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Stop the scoring-readiness tests from exe |
| 2026-10-06T00:24 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: docs: mission-first miner README and one  |
| 2026-10-06T00:24 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: chore: increase scoring timeout |
| 2026-10-06T00:24 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #646 from carbonphysi |
| 2026-10-06T00:24 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Keep verifier polling after a terminal b |
| 2026-10-05T18:46 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Switch evaluator to single-GPU replicas an |
| 2026-10-05T18:46 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): the reg-index staleness a |
| 2026-10-05T18:46 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(task-api): judge completions when the |
| 2026-10-05T18:46 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: fix(miner): preserve boolean CLI option d |
| 2026-10-05T18:46 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: perf(validator): reuse dendrite process p |
| 2026-10-05T18:46 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: connector reads the |
| 2026-10-05T18:46 | sn61 | RELEASE | sn61 released 4.10.9 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

