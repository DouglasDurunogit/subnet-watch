# Subnet watch — dashboard

_snapshot 2026-09-01T18:42:19Z · block 8974277 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.7 | 131 | 36,887 | cpu-small | 20 | 90% |
| 2 | sn3 Teutonic | 75.3 | 3,621 | 3,621 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 74.8 | 42.78 | 90.19 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 72.4 | 22.69 | 1,165 | cpu-small | 125 | 32% |
| 5 | sn15 ORO | 71.3 | 26.19 | 42.22 | cpu-small | 66 | 93% |
| 6 | sn92 MicroTensor | 70.6 | 15.59 | 355 | cpu-small | 9 | 60% |
| 7 | sn91 cascade | 70.3 | 802 | 3,234 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 69.3 | 27.96 | 197 | rtx4090 | 76 | 41% |
| 9 | sn102 ConnitoAI | 68.9 | 528 | 1,650 | rtx4090* | 7 | 30% |
| 10 | sn11 TrajectoryRL | 67.7 | 5,055 | 5,055 = | cpu-small | 1 | 100% |
| 11 | sn56 Gradients | 67.6 | 364 | 1,009 | rtx4090* | 7 | 71% |
| 12 | sn111 Claims | 67.1 | 329 | 2,946 | rtx4090* | 5 | 70% |
| 13 | sn124 Swarm | 66.5 | 266 | 864 | rtx4090* | 25 | 11% |
| 14 | sn61 RedTeam | 64.7 | 153 | 223 | rtx4090* | 48 | 3% |
| 15 | sn21 AdTAO | 64.4 | 3.91 | 522 | cpu-small | 16 | 45% |
| 16 | sn81 Reliquary | 64.3 | 134 | 244 | rtx4090* | 34 | 6% |
| 17 | sn79 MVTRX | 64.1 | 3.97 | 407 | cpu-small | 228 | 10% |
| 18 | sn54 Yanez | 63.2 | 4.84 | 902 | a4000 | 95 | 35% |
| 19 | sn121 sundae_bar | 62.9 | 1,186 | 1,186 = | cpu-small | 2 | 61% |
| 20 | sn55 NIOME | 62.4 | 75.52 | 620 | rtx4090* | 11 | 29% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 23 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-01T18:42 | sn7 | RELEASE | sn7 released release-20260901-182140: Set miner burn to 0% (v3.3.1) (# |
| 2026-09-01T18:42 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Set miner burn to 0% (v3.3.1) (#710) |
| 2026-09-01T18:42 | sn7 | README_TASK_DIFF | sn7 README task/scoring sections changed |
| 2026-09-01T18:42 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): focus column shows per-typ |
| 2026-09-01T18:42 | sn25 | RELEASE | sn25 released v2026.9.1-1034848790 |
| 2026-09-01T18:42 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: sim-testnet: verify direct Connect ingres |
| 2026-09-01T18:42 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: fix: show scoring-aligned augmented metri |
| 2026-09-01T18:42 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge pull request #120 from swarm-subne |
| 2026-09-01T15:14 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.922 - miners can earn again |
| 2026-09-01T15:14 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Merge pull request #51 from TrishoolAI/q- |
| 2026-09-01T15:14 | sn92 | RELEASE | sn92 released v0.3.2 |
| 2026-09-01T15:14 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: Fixed private hotkey_already_validat |
| 2026-09-01T15:14 | sn107 | SCORING_COMMIT | sn107 commit touches scoring: Merge pull request #37 from minos-protoc |
| 2026-09-01T15:14 | sn107 | README_TASK_DIFF | sn107 README task/scoring sections changed |
| 2026-09-01T15:14 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(scoring): the split section still d |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

