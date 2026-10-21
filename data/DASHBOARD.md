# Subnet watch — dashboard

_snapshot 2026-10-21T11:40:19Z · block 9331602 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 1 | `` |
| ≥0.99 dead | 34 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 79.2 | 4,399 | 4,399 = | cpu-small | 2 | 75% |
| 2 | sn121 sundae_bar | 74.7 | 1,169 | 1,169 = | cpu-small | 2 | 60% |
| 3 | sn3 Teutonic | 74.4 | 2,745 | 7,335 | rtx4090* | 5 | 40% |
| 4 | sn120 Affine | 73.8 | 2,325 | 11,472 | rtx4090* | 10 | 33% |
| 5 | sn97 Ingot | 73.4 | 2,028 | 2,028 = | rtx4090* | 5 | 20% |
| 6 | sn91 cascade | 71.2 | 410 | 1,643 | cpu-small | 5 | 52% |
| 7 | sn102 ConnitoAI | 71.1 | 1,024 | 1,024 | rtx4090* | 4 | 25% |
| 8 | sn1 Apex | 68.5 | 474 | 1,011 | rtx4090* | 5 | 57% |
| 9 | sn82 Noah | 68 | 667 | 672 | rtx4090* | 61 | 2% |
| 10 | sn67 Harnyx | 68 | 8.26 | 236 | cpu-small | 132 | 10% |
| 11 | sn125 Refinery | 67.4 | 337 | 994 | rtx4090* | 4 | 50% |
| 12 | sn53 engy | 67.3 | 332 | 2,810 | rtx4090 | 36 | 12% |
| 13 | sn107 Minos | 67.2 | 235 | 20,988 | cpu-small | 20 | 80% |
| 14 | sn15 ORO | 66.7 | 8.08 | 16.38 | cpu-small | 63 | 97% |
| 15 | sn66 conjectures | 63.8 | 115 | 239 | rtx4090* | 4 | 80% |
| 16 | sn26 Perturb | 63 | 194 | 262 | rtx3060 | 4 | 61% |
| 17 | sn81 Reliquary | 63 | 90.61 | 221 | rtx4090* | 12 | 76% |
| 18 | sn55 NIOME | 62.2 | 70.82 | 585 | rtx4090* | 11 | 30% |
| 19 | sn23 Trishool | 61.5 | 794 | 794 = | cpu-small | 2 | 80% |
| 20 | sn92 REAX | 60.1 | 75.86 | 3,023 | rtx4090 | 245 | 11% |

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
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 26 |
| captured (>90%) | 21 |

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
| 2026-10-21T11:40 | sn51 | RELEASE | sn51 released miner-v1.009 |
| 2026-10-21T11:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4860 - [P2] validator: CPU truth chec |
| 2026-10-21T11:40 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-21T11:40 | sn92 | RELEASE | sn92 released v1.2.0-rc10 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

