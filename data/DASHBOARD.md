# Subnet watch — dashboard

_snapshot 2026-11-19T04:21:03Z · block 9538193 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 237 | 237 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.6 | 2,160 | 4,327 | rtx4090* | 4 | 40% |
| 3 | sn67 Harnyx | 66.6 | 4.61 | 4.61 = | cpu-small | 208 | 19% |
| 4 | sn56 Gradients | 66.2 | 239 | 3,949 | rtx4090* | 7 | 49% |
| 5 | sn15 ORO | 65.7 | 5.79 | 9,056 | cpu-small | 76 | 95% |
| 6 | sn53 engy | 64.8 | 159 | 12,922 | rtx4090 | 20 | 61% |
| 7 | sn124 Swarm | 63 | 99.54 | 698 | rtx4090* | 13 | 30% |
| 8 | sn120 Affine | 61.8 | 2,237 | 2,237 = | rtx4090* | 10 | 10% |
| 9 | sn38 ChronoLLM | 61.7 | 33.69 | 303 | cpu-small | 10 | 52% |
| 10 | sn60 Bitsec.ai | 60.6 | 608 | 608 = | cpu-small | 3 | 50% |
| 11 | sn111 Claims | 60.2 | 40.41 | 162 | rtx4090* | 4 | 88% |
| 12 | sn62 Ridges | 60.2 | 39.31 | 481 | rtx4090* | 45 | 12% |
| 13 | sn97 Ingot | 59.6 | 1,175 | 1,175 = | rtx4090* | 5 | 20% |
| 14 | sn102 ConnitoAI | 57.6 | 637 | 641 | rtx4090* | 4 | 25% |
| 15 | sn4 Targon | 57.4 | 8,481 | 20,542 | rtx4090* | 5 | 66% |
| 16 | sn5 Hone | 57 | 18.61 | 40.91 | rtx4090* | 241 | 1% |
| 17 | sn66 conjectures | 56.5 | 12.12 | 1,001 | rtx4090* | 8 | 82% |
| 18 | sn46 Instant | 55.4 | 128 | 170 | cpu-small | 9 | 19% |
| 19 | sn107 Minos | 54.8 | 147 | 12,105 | cpu-small | 20 | 79% |
| 20 | sn116 Carbon | 52.9 | 3,271 | 3,271 = | rtx4090* | 2 | 75% |

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
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 28 |
| captured (>90%) | 26 |

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
| 2026-11-19T04:21 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Incoming changes for miners (#1434) |
| 2026-11-19T04:21 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Validator: ignore blobs first stored more |
| 2026-11-19T04:21 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Merge pull request #434 from cathedralai/ |
| 2026-11-19T04:21 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Miner client: 503 capacity retried like  |
| 2026-11-18T23:10 | sn62 | RELEASE | sn62 released v0.3.18 |
| 2026-11-18T23:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow audited published judgment recovery |
| 2026-11-18T23:10 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: feat(validator): score briefs with allowe |
| 2026-11-18T23:10 | sn99 | README_TASK_DIFF | sn99 README task/scoring sections changed |
| 2026-11-18T23:10 | sn109 | BURN_DROP | sn109 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-18T23:10 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Auto retry: a spent cap (3 per failure c |
| 2026-11-18T23:10 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge pull request #246 from swarm-subne |
| 2026-11-18T16:39 | sn12 | RELEASE | sn12 released validator-staging-2026-11-18-44297690409-632-1: feat: mi |
| 2026-11-18T16:39 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: feat: log validator ignored commitments ( |
| 2026-11-18T16:39 | sn25 | RELEASE | sn25 released v2026.11.18-1101975730 |
| 2026-11-18T16:39 | sn42 | RELEASE | sn42 released v0.6.22 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

