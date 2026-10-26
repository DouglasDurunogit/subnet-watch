# Subnet watch — dashboard

_snapshot 2026-10-26T05:27:24Z · block 9365738 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.4 | 2,100 | 4,208 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,800 | 1,800 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 71.2 | 1,045 | 5,660 | rtx4090* | 6 | 51% |
| 4 | sn46 Instant | 69.3 | 236 | 276 | cpu-small | 6 | 43% |
| 5 | sn1 Apex | 68.1 | 422 | 900 | rtx4090* | 5 | 55% |
| 6 | sn67 Harnyx | 67.9 | 7.35 | 189 | cpu-small | 122 | 9% |
| 7 | sn82 Noah | 67.8 | 576 | 582 | rtx4090* | 63 | 2% |
| 8 | sn41 Almanac | 67.8 | 8.39 | 133 | cpu-small | 161 | 2% |
| 9 | sn53 engy | 66.8 | 288 | 2,495 | rtx4090 | 36 | 11% |
| 10 | sn107 Minos | 66.8 | 212 | 18,039 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 66.1 | 6.78 | 14,577 | cpu-small | 55 | 97% |
| 12 | sn120 Affine | 63.9 | 142 | 1,454 | rtx4090* | 138 | 5% |
| 13 | sn66 conjectures | 63.3 | 101 | 210 | rtx4090* | 4 | 80% |
| 14 | sn62 Ridges | 62.7 | 82.23 | 916 | rtx4090* | 44 | 15% |
| 15 | sn23 Trishool | 62.6 | 1,081 | 1,081 = | cpu-small | 2 | 80% |
| 16 | sn91 cascade | 61.5 | 799 | 1,599 | cpu-small | 5 | 52% |
| 17 | sn28 SayGM | 60.8 | 49.48 | 2,114 | rtx4090* | 132 | 19% |
| 18 | sn34 BitMind | 59.9 | 8,440 | 8,440 = | a100-80 | 3 | 85% |
| 19 | sn81 Reliquary | 59.2 | 28.44 | 220 | rtx4090* | 41 | 48% |
| 20 | sn111 Claims | 58.9 | 27.43 | 2,667 | rtx4090* | 6 | 90% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 23 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-26T05:27 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4568 - [P1] Remove the GPU alias flag |
| 2026-10-26T05:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Classify verified provider output failure |
| 2026-10-26T05:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Expose native checkpoint metadata progres |
| 2026-10-26T00:45 | sn25 | RELEASE | sn25 released v2026.10.25-1081686250 |
| 2026-10-26T00:45 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Project the verified retained predecessor |
| 2026-10-26T00:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record final live verification of all twe |
| 2026-10-26T00:45 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-10-26T00:45 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Score failed paired model candidates with |
| 2026-10-25T22:30 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse native request closure verification |
| 2026-10-25T22:30 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.955 - miners can earn again |
| 2026-10-25T20:01 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.965 - miners can earn again |
| 2026-10-25T20:01 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #412 from Umi-BitSign/ |
| 2026-10-25T14:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5061 - [P1] Validator: re-anchor an i |
| 2026-10-25T14:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Materialize eligible closed score runs be |
| 2026-10-25T14:20 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat(eval): score agent turns mid-traject |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

