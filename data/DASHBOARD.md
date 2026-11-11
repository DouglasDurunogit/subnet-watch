# Subnet watch — dashboard

_snapshot 2026-11-11T15:29:56Z · block 9483937 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,754 | 2,754 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.6 | 1,627 | 3,263 | rtx4090* | 7 | 25% |
| 3 | sn54 Yanez | 72.5 | 1,566 | 2,013 | a4000 | 3 | 61% |
| 4 | sn97 Ingot | 72.3 | 1,461 | 1,461 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 70.6 | 877 | 4,624 | rtx4090* | 6 | 50% |
| 6 | sn41 Almanac | 70.5 | 15.32 | 172 | cpu-small | 160 | 3% |
| 7 | sn58 Attune | 69.8 | 709 | 1,140 | rtx4090* | 5 | 70% |
| 8 | sn1 Apex | 68.8 | 512 | 639 | rtx4090* | 4 | 62% |
| 9 | sn67 Harnyx | 68.7 | 8.22 | 140 | cpu-small | 137 | 8% |
| 10 | sn124 Swarm | 67.2 | 331 | 1,693 | rtx4090* | 10 | 29% |
| 11 | sn103 Terza Inference | 67.2 | 321 | 650 | rtx4090* | 5 | 35% |
| 12 | sn46 Instant | 67.2 | 126 | 138 | cpu-small | 10 | 46% |
| 13 | sn82 Noah | 66 | 278 | 367 | rtx4090* | 66 | 2% |
| 14 | sn53 engy | 65.1 | 171 | 921 | rtx4090 | 23 | 40% |
| 15 | sn15 ORO | 65.1 | 6.82 | 11,153 | cpu-small | 78 | 95% |
| 16 | sn14 Cacheon | 62.6 | 81.45 | 207 | rtx4090* | 4 | 95% |
| 17 | sn127 Zils | 62.2 | 72.43 | 72.43 = | rtx4090* | 4 | 88% |
| 18 | sn121 sundae_bar | 61.8 | 865 | 865 = | cpu-small | 2 | 60% |
| 19 | sn62 Ridges | 61.1 | 50.60 | 890 | rtx4090* | 41 | 18% |
| 20 | sn60 Bitsec.ai | 59.4 | 427 | 658 | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 16 |
| dominated (60–90%) | 31 |
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
| 2026-11-11T15:30 | sn17 | RELEASE | sn17 released Witness SDK 0.3.0 |
| 2026-11-11T15:30 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Run resumable candidate validation on Run |
| 2026-11-11T15:30 | sn51 | RELEASE | sn51 released watchtower-v1.2.2: DAH-5053: lium-watchtower 1.2.2, the  |
| 2026-11-11T15:30 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Miner: name the executors a pubkey upload |
| 2026-11-11T15:30 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify additive attempt bindings without  |
| 2026-11-11T15:30 | sn76 | BURN_DROP | sn76 burn fell 0.995 -> 0.983 - miners can earn again |
| 2026-11-11T15:30 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(orders): the admin job status says w |
| 2026-11-11T15:30 | sn117 | RELEASE | sn117 released everycli v1.1.3 |
| 2026-11-11T15:30 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: Retain reviewed worker artifact for atte |
| 2026-11-11T07:14 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Rented pool 10%, capped per miner at the  |
| 2026-11-11T07:14 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: 3.9.15: starter claims what the validator |
| 2026-11-11T07:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5845 - [P1] Validator: the rental cac |
| 2026-11-11T07:14 | sn62 | RELEASE | sn62 released v0.3.17 |
| 2026-11-11T07:14 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #540 from ridgesai/fix |
| 2026-11-11T07:14 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Expose private source-backed admission re |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

