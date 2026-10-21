# Subnet watch — dashboard

_snapshot 2026-10-21T20:16:27Z · block 9334183 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 13 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 93.1 | 4,335 | 13,006 | cpu-small | 3 | 75% |
| 2 | sn121 sundae_bar | 74.7 | 1,173 | 1,173 = | cpu-small | 2 | 60% |
| 3 | sn3 Teutonic | 74.4 | 2,768 | 7,396 | rtx4090* | 5 | 40% |
| 4 | sn97 Ingot | 73.4 | 2,039 | 2,039 = | rtx4090* | 4 | 40% |
| 5 | sn120 Affine | 72.8 | 1,702 | 17,803 | rtx4090* | 10 | 51% |
| 6 | sn91 cascade | 71.1 | 402 | 1,612 | cpu-small | 5 | 52% |
| 7 | sn102 ConnitoAI | 70.6 | 883 | 1,265 | rtx4090* | 6 | 31% |
| 8 | sn1 Apex | 68.7 | 503 | 984 | rtx4090* | 5 | 57% |
| 9 | sn67 Harnyx | 68.4 | 8.27 | 237 | cpu-small | 147 | 9% |
| 10 | sn82 Noah | 67.6 | 617 | 661 | rtx4090* | 61 | 2% |
| 11 | sn125 Refinery | 67.4 | 340 | 1,004 | rtx4090* | 4 | 50% |
| 12 | sn107 Minos | 67.4 | 245 | 20,747 | cpu-small | 20 | 80% |
| 13 | sn53 engy | 67.3 | 328 | 2,687 | rtx4090 | 36 | 11% |
| 14 | sn15 ORO | 66.9 | 8.00 | 15,782 | cpu-small | 63 | 97% |
| 15 | sn66 conjectures | 63.4 | 103 | 215 | rtx4090* | 4 | 80% |
| 16 | sn26 Perturb | 63.1 | 196 | 246 | rtx3060 | 4 | 60% |
| 17 | sn55 NIOME | 62.1 | 69.92 | 578 | rtx4090* | 11 | 30% |
| 18 | sn23 Trishool | 61.9 | 881 | 881 = | cpu-small | 2 | 80% |
| 19 | sn81 Reliquary | 59.9 | 35.09 | 117 | rtx4090* | 4 | 95% |
| 20 | sn92 REAX | 59.8 | 81.38 | 2,739 | rtx4090 | 245 | 10% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 26 |
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
| 2026-10-21T20:17 | sn7 | RELEASE | sn7 released release-20261021-195318: Scale the miner pool by recent s |
| 2026-10-21T20:17 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Scale the miner pool by recent swap fees ( |
| 2026-10-21T20:17 | sn28 | RELEASE | sn28 released v0.5.6-dev |
| 2026-10-21T20:17 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.6-dev (#337) |
| 2026-10-21T20:17 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-10-21T20:17 | sn30 | BURN_DROP | sn30 burn fell 0.996 -> 0.981 - miners can earn again |
| 2026-10-21T20:17 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.711 - miners can earn again |
| 2026-10-21T20:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retain proofs and receipts for approved s |
| 2026-10-21T20:17 | sn76 | RELEASE | sn76 released v0.0.3: Merge pull request #45 from heroncovelabs/fix/re |
| 2026-10-21T20:17 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: chore(verification): bind qualified basel |
| 2026-10-21T20:17 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #379 from reliquadotai |
| 2026-10-21T20:17 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.883 - miners can earn again |
| 2026-10-21T20:17 | sn117 | RELEASE | sn117 released everycli v0.6.2 |
| 2026-10-21T16:08 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Fix category dataset validation and hide r |
| 2026-10-21T16:08 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: feat(validator): one VHFT competition per |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

