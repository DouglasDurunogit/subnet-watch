# Subnet watch — dashboard

_snapshot 2026-11-20T03:04:03Z · block 9545007 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 106 | `miner_burn` < 0.99 |
| Ranked | 106 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 22 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 235 | 235 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.4 | 2,084 | 2,084 = | rtx4090* | 4 | 41% |
| 3 | sn14 Cacheon | 71.7 | 1,212 | 2,373 | rtx4090* | 5 | 48% |
| 4 | sn67 Harnyx | 66.5 | 4.79 | 5.09 | cpu-small | 231 | 7% |
| 5 | sn15 ORO | 65.7 | 5.86 | 8,898 | cpu-small | 67 | 95% |
| 6 | sn124 Swarm | 65.3 | 189 | 683 | rtx4090* | 11 | 30% |
| 7 | sn56 Gradients | 65.2 | 178 | 518 | rtx4090* | 7 | 49% |
| 8 | sn53 engy | 64.5 | 141 | 11,578 | rtx4090 | 20 | 61% |
| 9 | sn66 conjectures | 62.6 | 81.11 | 1,061 | rtx4090* | 3 | 90% |
| 10 | sn120 Affine | 61.7 | 2,169 | 2,169 = | rtx4090* | 10 | 10% |
| 11 | sn60 Bitsec.ai | 60.7 | 619 | 619 = | cpu-small | 3 | 50% |
| 12 | sn62 Ridges | 60.4 | 41.91 | 508 | rtx4090* | 45 | 12% |
| 13 | sn111 Claims | 60.2 | 39.33 | 158 | rtx4090* | 4 | 88% |
| 14 | sn97 Ingot | 59.5 | 1,141 | 1,141 = | rtx4090* | 5 | 20% |
| 15 | sn102 ConnitoAI | 57.5 | 621 | 642 | rtx4090* | 4 | 26% |
| 16 | sn1 Apex | 57.1 | 550 | 618 | rtx4090* | 4 | 54% |
| 17 | sn5 Hone | 56.8 | 18.21 | 39.73 | rtx4090* | 239 | 1% |
| 18 | sn4 Targon | 55.6 | 4,987 | 19,847 | rtx4090* | 5 | 66% |
| 19 | sn46 Instant | 55.4 | 127 | 150 | cpu-small | 9 | 25% |
| 20 | sn107 Minos | 54.5 | 137 | 11,628 | cpu-small | 20 | 79% |

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
| wide (<30%) | 31 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 27 |
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
| 2026-11-20T03:04 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.936 - miners can earn again |
| 2026-11-20T03:04 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #65 from hanlinai/feat |
| 2026-11-20T03:04 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: A candidate is evaluated on the machine a |
| 2026-11-20T03:04 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Box loss: a live DOWN mark stays DOWN on |
| 2026-11-19T21:51 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Retry incomplete R2 reads and prefetch eva |
| 2026-11-19T21:51 | sn12 | RELEASE | sn12 released validator-testing-2026-11-19-44554669102-9-1: fix: build |
| 2026-11-19T21:51 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix: build compute-horde-validator-nginx  |
| 2026-11-19T21:51 | sn25 | RELEASE | sn25 released v2026.11.19-1103236710 |
| 2026-11-19T21:51 | sn28 | RELEASE | sn28 released v0.5.25 |
| 2026-11-19T21:51 | sn33 | SCORING_COMMIT | sn33 commit touches scoring: Send a single conversation window to all  |
| 2026-11-19T21:51 | sn42 | RELEASE | sn42 released v0.6.25 |
| 2026-11-19T21:51 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: reference miner: one answer register for  |
| 2026-11-19T21:51 | sn51 | RELEASE | sn51 released executor-v1.191 |
| 2026-11-19T21:51 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4689 validator: ignore live volume an |
| 2026-11-19T21:51 | sn66 | RELEASE | sn66 released v2026.11.19.2 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

