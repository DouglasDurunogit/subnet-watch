# Subnet watch — dashboard

_snapshot 2026-11-19T13:41:24Z · block 9540994 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 26 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.8 | 247 | 247 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.6 | 2,207 | 4,422 | rtx4090* | 4 | 40% |
| 3 | sn56 Gradients | 66.3 | 245 | 4,042 | rtx4090* | 7 | 49% |
| 4 | sn15 ORO | 65.8 | 5.74 | 9,365 | cpu-small | 63 | 96% |
| 5 | sn124 Swarm | 65.4 | 197 | 712 | rtx4090* | 11 | 30% |
| 6 | sn53 engy | 64.8 | 159 | 12,903 | rtx4090 | 20 | 61% |
| 7 | sn67 Harnyx | 64.5 | 2.53 | 393 | cpu-small | 121 | 27% |
| 8 | sn14 Cacheon | 62.8 | 86.11 | 4,311 | rtx4090* | 5 | 83% |
| 9 | sn120 Affine | 61.9 | 2,289 | 2,289 = | rtx4090* | 10 | 10% |
| 10 | sn111 Claims | 60.3 | 41.46 | 166 | rtx4090* | 4 | 88% |
| 11 | sn62 Ridges | 60.3 | 40.13 | 489 | rtx4090* | 45 | 12% |
| 12 | sn97 Ingot | 59.7 | 1,199 | 1,199 = | rtx4090* | 5 | 20% |
| 13 | sn102 ConnitoAI | 57.7 | 653 | 675 | rtx4090* | 4 | 26% |
| 14 | sn4 Targon | 57.4 | 8,655 | 20,962 | rtx4090* | 5 | 66% |
| 15 | sn5 Hone | 57.3 | 19.65 | 42.35 | rtx4090* | 239 | 1% |
| 16 | sn66 conjectures | 56.5 | 12.48 | 1,024 | rtx4090* | 8 | 82% |
| 17 | sn46 Instant | 55.1 | 117 | 171 | cpu-small | 9 | 22% |
| 18 | sn107 Minos | 54.8 | 146 | 12,196 | cpu-small | 20 | 79% |
| 19 | sn116 Carbon | 52.9 | 3,184 | 3,184 = | rtx4090* | 2 | 75% |
| 20 | sn82 Noah | 52.8 | 178 | 250 | rtx4090* | 70 | 2% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 15 |
| dominated (60–90%) | 29 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-19T13:41 | sn12 | RELEASE | sn12 released validator-staging-2026-11-19-44521972284-633-1: fix: bum |
| 2026-11-19T13:41 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix: build compute-horde-validator-nginx  |
| 2026-11-19T13:41 | sn21 | RELEASE | sn21 released SN21 training data v7 (windows 2026-09-21 to 2026-10-04) |
| 2026-11-19T13:41 | sn24 | RELEASE | sn24 released v0.3.0 |
| 2026-11-19T13:41 | sn42 | RELEASE | sn42 released v0.6.24 |
| 2026-11-19T13:41 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: v0.6.24: the validator's vote scores reac |
| 2026-11-19T13:41 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Quality: each paid claim's pay is fixed b |
| 2026-11-19T13:41 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6714 - [P1] Validator: filler GPU pro |
| 2026-11-19T13:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix review outage recovery lock order and |
| 2026-11-19T13:41 | sn99 | README_TASK_DIFF | sn99 README task/scoring sections changed |
| 2026-11-19T13:41 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Queue places: unmarked is not waiting; a |
| 2026-11-19T04:21 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Incoming changes for miners (#1434) |
| 2026-11-19T04:21 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Validator: ignore blobs first stored more |
| 2026-11-19T04:21 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Merge pull request #434 from cathedralai/ |
| 2026-11-19T04:21 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Miner client: 503 capacity retried like  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

