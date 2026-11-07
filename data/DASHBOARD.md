# Subnet watch — dashboard

_snapshot 2026-11-07T18:42:26Z · block 9456104 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,801 | 2,801 = | rtx4090* | 10 | 10% |
| 2 | sn14 Cacheon | 72.9 | 1,734 | 4,168 | rtx4090* | 3 | 68% |
| 3 | sn3 Teutonic | 72.8 | 1,748 | 3,503 | rtx4090* | 7 | 25% |
| 4 | sn41 Almanac | 69.4 | 11.78 | 141 | cpu-small | 176 | 11% |
| 5 | sn36 Weir | 69.1 | 578 | 774 | rtx4090* | 9 | 24% |
| 6 | sn58 Attune | 69.1 | 567 | 913 | rtx4090* | 5 | 70% |
| 7 | sn56 Gradients | 68.4 | 453 | 1,212 | rtx4090* | 6 | 52% |
| 8 | sn67 Harnyx | 68.4 | 7.91 | 138 | cpu-small | 121 | 8% |
| 9 | sn103 Terza Inference | 67.6 | 357 | 992 | rtx4090* | 5 | 39% |
| 10 | sn46 Instant | 67.5 | 139 | 154 | cpu-small | 10 | 45% |
| 11 | sn82 Noah | 66.9 | 339 | 418 | rtx4090* | 64 | 2% |
| 12 | sn107 Minos | 66.3 | 187 | 15,915 | cpu-small | 20 | 80% |
| 13 | sn15 ORO | 64.9 | 5.91 | 13.37 | cpu-small | 72 | 96% |
| 14 | sn38 ChronoLLM | 62.7 | 43.72 | 391 | cpu-small | 10 | 52% |
| 15 | sn66 conjectures | 61.1 | 51.94 | 142 | rtx4090* | 5 | 80% |
| 16 | sn55 NIOME | 61 | 49.31 | 423 | rtx4090* | 11 | 30% |
| 17 | sn97 Ingot | 60.4 | 1,490 | 1,490 = | rtx4090* | 5 | 20% |
| 18 | sn70 Fugal | 59.4 | 31.90 | 65.03 | rtx4090* | 193 | 1% |
| 19 | sn28 SayGM | 59.2 | 32.75 | 2,457 | rtx4090* | 92 | 25% |
| 20 | sn111 Claims | 58.6 | 24.89 | 2,474 | rtx4090* | 6 | 90% |

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
| concentrated (30–60%) | 17 |
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
| 2026-11-07T18:42 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-11-07T18:42 | sn17 | RELEASE | sn17 released witness-client-v0.2.18 |
| 2026-11-07T18:42 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Apply the request deadline to cached gran |
| 2026-11-07T18:42 | sn66 | RELEASE | sn66 released v2026.11.07 |
| 2026-11-07T18:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Continue evidence-source validation past  |
| 2026-11-07T18:42 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Crown-time D + menu: the Validator's 7 N |
| 2026-11-07T13:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1106 from leadpoet/co |
| 2026-11-07T13:56 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #466 from reliquadotai |
| 2026-11-07T13:56 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: fix: bound miner refreshes and reject pri |
| 2026-11-07T13:56 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Practice on the data kit's verify set fo |
| 2026-11-07T07:02 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Rename the miner command from yugos to yc |
| 2026-11-07T07:02 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.091 - miners can earn again |
| 2026-11-07T07:02 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: fix(miner): support reviewed runtime488 f |
| 2026-11-07T07:02 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-11-07T07:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified identity and complete p |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

