# Subnet watch — dashboard

_snapshot 2026-10-21T05:58:40Z · block 9329894 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 79.1 | 4,322 | 4,322 = | cpu-small | 2 | 75% |
| 2 | sn120 Affine | 75.1 | 3,378 | 6,030 | rtx4090* | 10 | 18% |
| 3 | sn121 sundae_bar | 74.7 | 1,157 | 1,157 = | cpu-small | 2 | 60% |
| 4 | sn3 Teutonic | 74.3 | 2,717 | 7,259 | rtx4090* | 5 | 40% |
| 5 | sn97 Ingot | 73.4 | 2,023 | 2,023 = | rtx4090* | 5 | 20% |
| 6 | sn91 cascade | 71 | 393 | 1,574 | cpu-small | 5 | 52% |
| 7 | sn67 Harnyx | 70.8 | 15.96 | 227 | cpu-small | 137 | 9% |
| 8 | sn53 engy | 69 | 550 | 2,289 | rtx4090 | 24 | 16% |
| 9 | sn82 Noah | 68.7 | 656 | 662 | rtx4090* | 61 | 2% |
| 10 | sn1 Apex | 68.4 | 459 | 985 | rtx4090* | 5 | 56% |
| 11 | sn107 Minos | 67.5 | 252 | 20,946 | cpu-small | 20 | 79% |
| 12 | sn23 Trishool | 67.5 | 232 | 232 = | cpu-small | 4 | 80% |
| 13 | sn15 ORO | 67.4 | 8.09 | 15,948 | cpu-small | 63 | 97% |
| 14 | sn66 conjectures | 63.8 | 114 | 222 | rtx4090* | 4 | 81% |
| 15 | sn26 Perturb | 63.1 | 195 | 262 | rtx3060 | 4 | 61% |
| 16 | sn55 NIOME | 62 | 67.15 | 557 | rtx4090* | 11 | 30% |
| 17 | sn81 Reliquary | 60.8 | 47.12 | 195 | rtx4090* | 13 | 78% |
| 18 | sn111 Claims | 59.5 | 32.27 | 2,888 | rtx4090* | 6 | 90% |
| 19 | sn92 REAX | 59.3 | 78.17 | 2,883 | rtx4090 | 244 | 11% |
| 20 | sn28 SayGM | 59.1 | 29.75 | 3,962 | rtx4090* | 119 | 28% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 27 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-21T05:59 | sn25 | RELEASE | sn25 released v2026.10.20-1077553990 |
| 2026-10-21T05:59 | sn30 | RELEASE | sn30 released v0.1.3 — Identical-forecast pooling, protocol 2044 |
| 2026-10-21T05:59 | sn30 | SCORING_COMMIT | sn30 commit touches scoring: feat(scoring): identical-forecast pooling |
| 2026-10-21T05:59 | sn30 | README_TASK_DIFF | sn30 README task/scoring sections changed |
| 2026-10-21T05:59 | sn51 | RELEASE | sn51 released executor-v1.149 |
| 2026-10-21T05:59 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4266 - [P2] validator: keep a pass-th |
| 2026-10-21T05:59 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #372 from reliquadotai |
| 2026-10-21T05:59 | sn117 | RELEASE | sn117 released everycli v0.6.0 |
| 2026-10-21T05:59 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: docs(release): finalize v0.6.0 routing a |
| 2026-10-21T01:02 | sn25 | RELEASE | sn25 released v2026.10.20-1077406510 |
| 2026-10-21T01:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Evaluate Arena claim admission lazily in  |
| 2026-10-21T01:02 | sn92 | RELEASE | sn92 released v1.2.0-rc9.post7 |
| 2026-10-21T01:02 | sn120 | BURN_DROP | sn120 burn fell 1.000 -> 0.100 - miners can earn again |
| 2026-10-20T22:43 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Keep validator connections alive while min |
| 2026-10-20T22:43 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound composed scorer image tags without  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

