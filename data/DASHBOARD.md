# Subnet watch — dashboard

_snapshot 2026-11-19T21:51:13Z · block 9543443 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 105 | `miner_burn` < 0.99 |
| Ranked | 105 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 17 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 13 | `█████` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 23 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 236 | 236 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.5 | 2,128 | 4,265 | rtx4090* | 4 | 40% |
| 3 | sn14 Cacheon | 71.7 | 1,221 | 2,390 | rtx4090* | 5 | 48% |
| 4 | sn15 ORO | 66 | 5.69 | 8,969 | cpu-small | 66 | 95% |
| 5 | sn124 Swarm | 65.3 | 190 | 686 | rtx4090* | 11 | 30% |
| 6 | sn56 Gradients | 65.2 | 179 | 521 | rtx4090* | 7 | 49% |
| 7 | sn67 Harnyx | 64.6 | 2.35 | 375 | cpu-small | 131 | 27% |
| 8 | sn53 engy | 63.1 | 93.75 | 3,318 | rtx4090 | 20 | 61% |
| 9 | sn120 Affine | 61.7 | 2,184 | 2,184 = | rtx4090* | 10 | 10% |
| 10 | sn60 Bitsec.ai | 60.7 | 628 | 628 = | cpu-small | 3 | 50% |
| 11 | sn62 Ridges | 60.5 | 43.24 | 522 | rtx4090* | 45 | 12% |
| 12 | sn111 Claims | 60.2 | 39.58 | 159 | rtx4090* | 4 | 88% |
| 13 | sn97 Ingot | 59.6 | 1,148 | 1,148 = | rtx4090* | 5 | 20% |
| 14 | sn102 ConnitoAI | 57.5 | 625 | 646 | rtx4090* | 4 | 26% |
| 15 | sn1 Apex | 57.2 | 568 | 636 | rtx4090* | 4 | 53% |
| 16 | sn5 Hone | 56.8 | 18.07 | 39.92 | rtx4090* | 241 | 1% |
| 17 | sn4 Targon | 55.6 | 5,014 | 19,953 | rtx4090* | 5 | 66% |
| 18 | sn46 Instant | 55.2 | 122 | 166 | cpu-small | 9 | 25% |
| 19 | sn107 Minos | 54.9 | 151 | 11,834 | cpu-small | 20 | 79% |
| 20 | sn99 Axonry | 53.9 | 4,959 | 4,959 = | rtx4090* | 2 | 50% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 29 |
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
| 2026-11-19T21:51 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(cli): let RELIQUARY_HF_REPO_ID set va |
| 2026-11-19T21:51 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Host DNAT 443 to the sealed guest and a D |
| 2026-11-19T21:51 | sn99 | BURN_DROP | sn99 burn fell 1.000 -> 0.500 - miners can earn again |
| 2026-11-19T21:51 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Updates page: current crown rule, rough- |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

