# Subnet watch — dashboard

_snapshot 2026-09-04T11:33:24Z · block 8993731 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.6 | 187 | 375 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 77.2 | 95.34 | 5,682 | cpu-small | 21 | 81% |
| 3 | sn76 Phylax | 73.1 | 28.52 | 75.55 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 71.3 | 17.70 | 92.64 | cpu-small | 135 | 17% |
| 5 | sn91 cascade | 70.4 | 834 | 3,363 | rtx4090* | 5 | 52% |
| 6 | sn102 ConnitoAI | 70.3 | 813 | 1,840 | rtx4090* | 6 | 33% |
| 7 | sn15 ORO | 70.1 | 21.57 | 22,072 | cpu-small | 59 | 94% |
| 8 | sn56 Gradients | 69 | 546 | 1,360 | rtx4090* | 5 | 75% |
| 9 | sn124 Swarm | 66.4 | 264 | 814 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 65.3 | 200 | 3,545 | rtx4090* | 5 | 82% |
| 11 | sn80 OpenRoboto | 65.3 | 180 | 653 | rtx4090* | 5 | 71% |
| 12 | sn79 MVTRX | 64.5 | 4.74 | 417 | cpu-small | 225 | 9% |
| 13 | sn121 sundae_bar | 62.9 | 1,207 | 1,207 = | cpu-small | 2 | 61% |
| 14 | sn74 Gittensor | 61.4 | 59.25 | 384 | rtx4090 | 11 | 64% |
| 15 | sn101 Tag101 | 60.1 | 0.24 | 0.83 | cpu-small | 246 | 90% |
| 16 | sn41 Almanac | 59.6 | 32.23 | 95.47 | cpu-small | 87 | 10% |
| 17 | sn65 True Performance | 59 | 35.76 | 79.73 | rtx4090* | 6 | 89% |
| 18 | sn51 lium.io | 58.5 | 32.02 | 2,062 | rtx4090* | 63 | 74% |
| 19 | sn14 Cacheon | 57.9 | 707 | 4,090 | rtx4090* | 6 | 63% |
| 20 | sn28 SayGM | 56.9 | 16.32 | 7,225 | rtx4090* | 36 | 51% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 20 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| code-submission (validator runs it) | 11 |
| min_compute.yml (curated) | 11 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-04T11:33 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record semantic verifier parallel qualifi |
| 2026-09-04T11:33 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Derive the verifier image tag, not only i |
| 2026-09-04T11:33 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-04T11:33 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Expose replay-verified public miner solut |
| 2026-09-04T11:33 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Smooth the miner CLI and quiet the archiv |
| 2026-09-04T11:33 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: re-key a registration when the miner |
| 2026-09-04T11:33 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(validator): extract submit outcome h |
| 2026-09-04T11:33 | sn114 | README_TASK_DIFF | sn114 README task/scoring sections changed |
| 2026-09-04T06:21 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: test(validator): prove burn composition m |
| 2026-09-04T06:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected Arena reward compatibility |
| 2026-09-04T06:21 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(proof): Proof challenge + dynamic t |
| 2026-09-04T06:21 | sn107 | RELEASE | sn107 released v0.3.0: Minos 🧬 — Difficulty-weighted scoring (v2), rou |
| 2026-09-04T01:25 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): commit the daily vector d |
| 2026-09-04T01:25 | sn25 | RELEASE | sn25 released v2026.9.3-1036806790 |
| 2026-09-04T01:25 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: fix semantic reward consensus fixture |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

