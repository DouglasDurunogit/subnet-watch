# Subnet watch — dashboard

_snapshot 2026-11-08T15:04:50Z · block 9462216 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,817 | 2,817 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.9 | 1,785 | 3,578 | rtx4090* | 7 | 25% |
| 3 | sn14 Cacheon | 72.9 | 1,747 | 4,197 | rtx4090* | 3 | 68% |
| 4 | sn56 Gradients | 70.7 | 907 | 4,912 | rtx4090* | 5 | 52% |
| 5 | sn41 Almanac | 70.2 | 14.11 | 160 | cpu-small | 175 | 2% |
| 6 | sn1 Apex | 70 | 730 | 747 | rtx4090* | 4 | 54% |
| 7 | sn36 Weir | 69.8 | 693 | 786 | rtx4090* | 8 | 24% |
| 8 | sn58 Attune | 69.1 | 571 | 919 | rtx4090* | 5 | 70% |
| 9 | sn103 Terza Inference | 67.8 | 386 | 495 | rtx4090* | 5 | 39% |
| 10 | sn46 Instant | 67.8 | 148 | 159 | cpu-small | 9 | 46% |
| 11 | sn82 Noah | 67.1 | 334 | 420 | rtx4090* | 64 | 2% |
| 12 | sn15 ORO | 66 | 7.15 | 11,678 | cpu-small | 72 | 95% |
| 13 | sn67 Harnyx | 65.5 | 3.66 | 305 | cpu-small | 116 | 17% |
| 14 | sn38 ChronoLLM | 62.7 | 43.53 | 389 | cpu-small | 10 | 52% |
| 15 | sn66 conjectures | 61.2 | 52.34 | 143 | rtx4090* | 5 | 80% |
| 16 | sn55 NIOME | 60.9 | 48.36 | 416 | rtx4090* | 11 | 30% |
| 17 | sn97 Ingot | 60.5 | 1,493 | 1,493 = | rtx4090* | 4 | 40% |
| 18 | sn111 Claims | 58.6 | 24.96 | 2,481 | rtx4090* | 6 | 90% |
| 19 | sn70 Fugal | 58.4 | 22.57 | 72.46 | rtx4090* | 221 | 1% |
| 20 | sn5 Hone | 57.7 | 23.69 | 49.26 | rtx4090* | 243 | 1% |

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
| wide (<30%) | 33 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 25 |
| captured (>90%) | 23 |

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
| 2026-11-07T22:21 | sn90 | RELEASE | sn90 released v1.3.6: feat(subnet): show Chutes median GPU revenue on  |
| 2026-11-07T22:21 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: chore(subnet): bump validator fallback ve |
| 2026-11-07T22:21 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Miner terms for mainnet subnet 127 and t |
| 2026-11-07T18:42 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-11-07T18:42 | sn17 | RELEASE | sn17 released witness-client-v0.2.18 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

