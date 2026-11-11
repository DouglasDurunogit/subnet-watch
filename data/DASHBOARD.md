# Subnet watch — dashboard

_snapshot 2026-11-11T07:13:56Z · block 9481457 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,805 | 2,805 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.7 | 1,684 | 3,377 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.2 | 1,411 | 1,411 = | rtx4090* | 5 | 20% |
| 4 | sn41 Almanac | 70.4 | 14.75 | 168 | cpu-small | 160 | 2% |
| 5 | sn34 Yugos | 70.1 | 771 | 6,619 | rtx4090* | 3 | 85% |
| 6 | sn58 Attune | 69.5 | 652 | 1,048 | rtx4090* | 5 | 70% |
| 7 | sn56 Gradients | 69.3 | 597 | 4,563 | rtx4090* | 6 | 50% |
| 8 | sn1 Apex | 68.7 | 506 | 757 | rtx4090* | 4 | 58% |
| 9 | sn67 Harnyx | 68.6 | 8.04 | 137 | cpu-small | 137 | 8% |
| 10 | sn46 Instant | 67.3 | 130 | 171 | cpu-small | 10 | 46% |
| 11 | sn124 Swarm | 67 | 316 | 1,619 | rtx4090* | 10 | 29% |
| 12 | sn15 ORO | 66.3 | 6.72 | 10,925 | cpu-small | 73 | 95% |
| 13 | sn82 Noah | 65.8 | 273 | 361 | rtx4090* | 66 | 2% |
| 14 | sn53 engy | 65.1 | 173 | 2,690 | rtx4090 | 31 | 21% |
| 15 | sn14 Cacheon | 62.5 | 79.32 | 202 | rtx4090* | 4 | 95% |
| 16 | sn121 sundae_bar | 61.7 | 847 | 847 = | cpu-small | 2 | 60% |
| 17 | sn62 Ridges | 61 | 49.62 | 875 | rtx4090* | 41 | 18% |
| 18 | sn60 Bitsec.ai | 59.4 | 416 | 641 | cpu-small | 3 | 50% |
| 19 | sn55 NIOME | 59.2 | 29.08 | 365 | rtx4090* | 11 | 30% |
| 20 | sn4 Targon | 58.4 | 11,650 | 22,749 | rtx4090* | 5 | 60% |

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
| dominated (60–90%) | 31 |
| captured (>90%) | 22 |

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
| 2026-11-11T07:14 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Rented pool 10%, capped per miner at the  |
| 2026-11-11T07:14 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: 3.9.15: starter claims what the validator |
| 2026-11-11T07:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5845 - [P1] Validator: the rental cac |
| 2026-11-11T07:14 | sn62 | RELEASE | sn62 released v0.3.17 |
| 2026-11-11T07:14 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #540 from ridgesai/fix |
| 2026-11-11T07:14 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Expose private source-backed admission re |
| 2026-11-11T07:14 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: docs: one miner address, https://api.reli |
| 2026-11-11T07:14 | sn81 | README_TASK_DIFF | sn81 README task/scoring sections changed |
| 2026-11-11T07:14 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.823 - miners can earn again |
| 2026-11-11T07:14 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Updates: testnet Motor + Cooling 1.8 swi |
| 2026-11-11T07:14 | sn127 | RELEASE | sn127 released Release ed8326b |
| 2026-11-11T07:14 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: zils-miner report goes through the hoste |
| 2026-11-11T00:37 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Merge pull request #1 from mybelovedstar12 |
| 2026-11-11T00:37 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Add validation worker with manual replays |
| 2026-11-11T00:37 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: Validate validator requests and submissio |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

