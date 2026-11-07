# Subnet watch — dashboard

_snapshot 2026-11-07T07:02:05Z · block 9452602 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 65 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **65** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,810 | 2,810 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.9 | 1,763 | 3,533 | rtx4090* | 7 | 25% |
| 3 | sn14 Cacheon | 72.9 | 1,751 | 4,207 | rtx4090* | 3 | 68% |
| 4 | sn36 Weir | 69.6 | 654 | 1,278 | rtx4090* | 9 | 24% |
| 5 | sn41 Almanac | 69.4 | 11.85 | 143 | cpu-small | 176 | 9% |
| 6 | sn58 Attune | 69.2 | 586 | 942 | rtx4090* | 5 | 70% |
| 7 | sn56 Gradients | 68.4 | 458 | 4,982 | rtx4090* | 7 | 51% |
| 8 | sn67 Harnyx | 68.4 | 8.03 | 140 | cpu-small | 120 | 8% |
| 9 | sn1 Apex | 67.3 | 335 | 773 | rtx4090* | 4 | 72% |
| 10 | sn103 Terza Inference | 67.3 | 333 | 1,015 | rtx4090* | 5 | 38% |
| 11 | sn46 Instant | 67.2 | 126 | 212 | cpu-small | 10 | 46% |
| 12 | sn82 Noah | 66.8 | 346 | 426 | rtx4090* | 64 | 2% |
| 13 | sn107 Minos | 66.1 | 178 | 15,128 | cpu-small | 20 | 80% |
| 14 | sn15 ORO | 65.9 | 6.50 | 12,066 | cpu-small | 69 | 96% |
| 15 | sn38 ChronoLLM | 62.7 | 44.31 | 396 | cpu-small | 10 | 52% |
| 16 | sn66 conjectures | 61.2 | 52.77 | 144 | rtx4090* | 5 | 80% |
| 17 | sn55 NIOME | 61 | 50.26 | 431 | rtx4090* | 11 | 30% |
| 18 | sn97 Ingot | 60.5 | 1,515 | 1,515 = | rtx4090* | 5 | 20% |
| 19 | sn111 Claims | 58.5 | 24.35 | 2,434 | rtx4090* | 6 | 90% |
| 20 | sn117 everyframe.studi | 58.3 | 22.46 | 101 | rtx4090* | 27 | 76% |

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
| wide (<30%) | 32 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 27 |
| captured (>90%) | 24 |

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
| 2026-11-07T07:02 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Rename the miner command from yugos to yc |
| 2026-11-07T07:02 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.091 - miners can earn again |
| 2026-11-07T07:02 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: fix(miner): support reviewed runtime488 f |
| 2026-11-07T07:02 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-11-07T07:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified identity and complete p |
| 2026-11-07T07:02 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #518 from Umi-BitSign/ |
| 2026-11-07T07:02 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(order-control): keep an order from m |
| 2026-11-07T07:02 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Queue view: only a built task waits to g |
| 2026-11-07T07:02 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: PE admission: verify every frozen probe  |
| 2026-11-07T00:52 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Publish operator-focused SN2 validator doc |
| 2026-11-07T00:52 | sn66 | RELEASE | sn66 released v2026.11.06.3 |
| 2026-11-07T00:52 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Bound archive validation resources and en |
| 2026-11-07T00:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Test historical verifier finality with it |
| 2026-11-07T00:52 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Queue view: a GET never slows a grade (V |
| 2026-11-07T00:52 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Clarify independent 64K gate limits in m |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

