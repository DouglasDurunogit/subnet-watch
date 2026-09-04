# Subnet watch — dashboard

_snapshot 2026-09-04T06:21:31Z · block 8992171 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.6 | 184 | 369 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.8 | 87.97 | 5,589 | cpu-small | 21 | 81% |
| 3 | sn76 Phylax | 73 | 27.79 | 73.66 | cpu-small | 21 | 20% |
| 4 | sn102 ConnitoAI | 71.3 | 1,082 | 3,057 | rtx4090* | 4 | 54% |
| 5 | sn15 ORO | 70.2 | 21.80 | 21,472 | cpu-small | 74 | 93% |
| 6 | sn91 cascade | 69.4 | 623 | 3,359 | rtx4090* | 5 | 52% |
| 7 | sn96 Verathos | 69.2 | 27.64 | 147 | rtx4090 | 76 | 45% |
| 8 | sn56 Gradients | 69 | 541 | 1,352 | rtx4090* | 5 | 74% |
| 9 | sn67 Harnyx | 68.7 | 9.12 | 9.12 = | cpu-small | 210 | 33% |
| 10 | sn11 TrajectoryRL | 67.8 | 5,228 | 5,228 = | cpu-small | 1 | 100% |
| 11 | sn124 Swarm | 66.5 | 266 | 821 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 66.3 | 265 | 2,386 | rtx4090* | 5 | 56% |
| 13 | sn61 RedTeam | 65.2 | 178 | 253 | rtx4090* | 45 | 3% |
| 14 | sn80 OpenRoboto | 65.2 | 177 | 642 | rtx4090* | 5 | 71% |
| 15 | sn79 MVTRX | 64.6 | 4.42 | 421 | cpu-small | 229 | 10% |
| 16 | sn98 NeverPlayAlone | 64.4 | 1,868 | 1,868 = | cpu-small | 1 | 100% |
| 17 | sn121 sundae_bar | 62.9 | 1,200 | 1,200 = | cpu-small | 2 | 61% |
| 18 | sn74 Gittensor | 61.3 | 56.60 | 369 | rtx4090 | 11 | 65% |
| 19 | sn65 True Performance | 59.8 | 43.07 | 94.42 | rtx4090* | 6 | 87% |
| 20 | sn101 Tag101 | 59.6 | 0.41 | 0.77 | cpu-small | 242 | 90% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 20 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-04T06:21 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: test(validator): prove burn composition m |
| 2026-09-04T06:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected Arena reward compatibility |
| 2026-09-04T06:21 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(proof): Proof challenge + dynamic t |
| 2026-09-04T06:21 | sn107 | RELEASE | sn107 released v0.3.0: Minos 🧬 — Difficulty-weighted scoring (v2), rou |
| 2026-09-04T01:25 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): commit the daily vector d |
| 2026-09-04T01:25 | sn25 | RELEASE | sn25 released v2026.9.3-1036806790 |
| 2026-09-04T01:25 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: fix semantic reward consensus fixture |
| 2026-09-04T01:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Prevent source add reward queue starvatio |
| 2026-09-04T01:25 | sn107 | BURN_DROP | sn107 burn fell 1.000 -> 0.812 - miners can earn again |
| 2026-09-04T01:25 | sn107 | SCORING_COMMIT | sn107 commit touches scoring: Merge pull request #39 from minos-protoc |
| 2026-09-03T23:33 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Tell a rate-limited miner which submissio |
| 2026-09-03T21:41 | sn25 | RELEASE | sn25 released v2026.9.3-1036684010 |
| 2026-09-03T21:41 | sn49 | BURN_DROP | sn49 burn fell 0.990 -> 0.990 - miners can earn again |
| 2026-09-03T21:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind updated scoring protected workflows |
| 2026-09-03T18:49 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: stop dropping the thinking-tok |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

