# Subnet watch — dashboard

_snapshot 2026-11-08T19:38:04Z · block 9463578 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,807 | 2,807 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.9 | 1,766 | 3,541 | rtx4090* | 7 | 25% |
| 3 | sn56 Gradients | 70.7 | 904 | 4,896 | rtx4090* | 5 | 52% |
| 4 | sn1 Apex | 69.9 | 725 | 782 | rtx4090* | 4 | 53% |
| 5 | sn41 Almanac | 69.8 | 12.88 | 157 | cpu-small | 174 | 2% |
| 6 | sn36 Weir | 69.4 | 620 | 746 | rtx4090* | 8 | 24% |
| 7 | sn58 Attune | 69.1 | 568 | 914 | rtx4090* | 5 | 70% |
| 8 | sn103 Terza Inference | 68 | 407 | 677 | rtx4090* | 5 | 37% |
| 9 | sn82 Noah | 67 | 327 | 412 | rtx4090* | 64 | 2% |
| 10 | sn46 Instant | 66.9 | 116 | 254 | cpu-small | 9 | 46% |
| 11 | sn15 ORO | 66.9 | 7.08 | 14.40 | cpu-small | 73 | 95% |
| 12 | sn67 Harnyx | 65.4 | 3.63 | 302 | cpu-small | 120 | 17% |
| 13 | sn38 ChronoLLM | 62.6 | 43.27 | 387 | cpu-small | 10 | 52% |
| 14 | sn66 conjectures | 61.2 | 52.27 | 143 | rtx4090* | 5 | 80% |
| 15 | sn55 NIOME | 60.9 | 48.14 | 415 | rtx4090* | 11 | 30% |
| 16 | sn97 Ingot | 60.4 | 1,486 | 1,486 = | rtx4090* | 4 | 40% |
| 17 | sn111 Claims | 58.6 | 24.82 | 2,471 | rtx4090* | 6 | 90% |
| 18 | sn70 Fugal | 58.2 | 22.58 | 64.19 | rtx4090* | 218 | 1% |
| 19 | sn102 ConnitoAI | 58.1 | 737 | 738 | rtx4090* | 4 | 25% |
| 20 | sn5 Hone | 57.9 | 23.13 | 48.92 | rtx4090* | 243 | 1% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 24 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-08T19:38 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify full recovery function security on |
| 2026-11-08T19:38 | sn76 | BURN_DROP | sn76 burn fell 0.996 -> 0.985 - miners can earn again |
| 2026-11-08T19:38 | sn90 | RELEASE | sn90 released v1.4.2 |
| 2026-11-08T19:38 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(subnet): consolidate miner node onbo |
| 2026-11-08T19:38 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-11-08T15:05 | sn11 | RELEASE | sn11 released v0.7.8 |
| 2026-11-08T15:05 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Burn all SN11 miner emission to owner UID |
| 2026-11-08T08:01 | sn17 | RELEASE | sn17 released witness-gateway-fence-poll-20261108 |
| 2026-11-08T08:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify delegated admission deferral in re |
| 2026-11-08T01:42 | sn17 | RELEASE | sn17 released witness-gateway-disconnect-20261108 |
| 2026-11-08T01:42 | sn76 | BURN_DROP | sn76 burn fell 0.992 -> 0.984 - miners can earn again |
| 2026-11-08T01:42 | sn90 | RELEASE | sn90 released v1.4.1: feat(pricing): lower three-provider markup to fi |
| 2026-11-08T01:42 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Held-contender view, miner side: signed  |
| 2026-11-08T01:42 | sn126 | BURN_DROP | sn126 burn fell 1.000 -> 0.985 - miners can earn again |
| 2026-11-07T22:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Integrate current training permission met |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

