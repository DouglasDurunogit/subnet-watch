# Subnet watch — dashboard

_snapshot 2026-11-07T13:56:19Z · block 9454673 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

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
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,814 | 2,814 = | rtx4090* | 10 | 10% |
| 2 | sn14 Cacheon | 72.9 | 1,742 | 4,185 | rtx4090* | 3 | 68% |
| 3 | sn3 Teutonic | 72.8 | 1,753 | 3,514 | rtx4090* | 7 | 25% |
| 4 | sn41 Almanac | 69.5 | 12.11 | 145 | cpu-small | 176 | 11% |
| 5 | sn58 Attune | 69.1 | 577 | 928 | rtx4090* | 5 | 70% |
| 6 | sn56 Gradients | 68.4 | 455 | 4,961 | rtx4090* | 7 | 52% |
| 7 | sn67 Harnyx | 68.4 | 7.96 | 139 | cpu-small | 120 | 8% |
| 8 | sn1 Apex | 67.2 | 322 | 790 | rtx4090* | 4 | 72% |
| 9 | sn82 Noah | 66.9 | 344 | 424 | rtx4090* | 64 | 2% |
| 10 | sn103 Terza Inference | 66.9 | 294 | 1,124 | rtx4090* | 5 | 43% |
| 11 | sn46 Instant | 66.8 | 113 | 219 | cpu-small | 10 | 45% |
| 12 | sn107 Minos | 66.3 | 187 | 15,905 | cpu-small | 20 | 80% |
| 13 | sn15 ORO | 65.3 | 6.25 | 11,648 | cpu-small | 71 | 96% |
| 14 | sn38 ChronoLLM | 62.7 | 44.29 | 396 | cpu-small | 10 | 52% |
| 15 | sn66 conjectures | 61.2 | 52.21 | 143 | rtx4090* | 5 | 80% |
| 16 | sn97 Ingot | 60.5 | 1,501 | 1,501 = | rtx4090* | 5 | 20% |
| 17 | sn55 NIOME | 59.9 | 35.42 | 283 | rtx4090* | 11 | 30% |
| 18 | sn111 Claims | 58.6 | 25.04 | 2,485 | rtx4090* | 6 | 90% |
| 19 | sn70 Fugal | 58.5 | 23.73 | 61.13 | rtx4090* | 175 | 1% |
| 20 | sn28 SayGM | 58.2 | 24.62 | 2,424 | rtx4090* | 121 | 21% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 27 |
| captured (>90%) | 25 |

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
| 2026-11-07T13:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1106 from leadpoet/co |
| 2026-11-07T13:56 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #466 from reliquadotai |
| 2026-11-07T13:56 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: fix: bound miner refreshes and reject pri |
| 2026-11-07T13:56 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Practice on the data kit's verify set fo |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

