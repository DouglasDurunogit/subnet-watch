# Subnet watch — dashboard

_snapshot 2026-09-02T11:39:32Z · block 8979363 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 78.1 | 97.49 | 1,769 | cpu-small | 9 | 60% |
| 2 | sn3 Teutonic | 75.3 | 3,549 | 3,549 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 74.5 | 40.58 | 85.63 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 71.5 | 18.37 | 1,237 | cpu-small | 128 | 35% |
| 5 | sn23 Trishool | 71.1 | 398 | 398 = | cpu-small | 2 | 85% |
| 6 | sn102 ConnitoAI | 70.2 | 794 | 1,622 | rtx4090* | 6 | 30% |
| 7 | sn15 ORO | 69.7 | 19.10 | 20,423 | cpu-small | 80 | 92% |
| 8 | sn91 cascade | 69.1 | 571 | 3,079 | rtx4090* | 5 | 52% |
| 9 | sn96 Verathos | 68 | 20.20 | 156 | rtx4090 | 84 | 41% |
| 10 | sn11 TrajectoryRL | 67.6 | 4,930 | 4,930 = | cpu-small | 1 | 100% |
| 11 | sn56 Gradients | 67.6 | 357 | 1,000 | rtx4090* | 7 | 72% |
| 12 | sn111 Claims | 67 | 316 | 2,829 | rtx4090* | 5 | 70% |
| 13 | sn124 Swarm | 66.3 | 257 | 792 | rtx4090* | 25 | 11% |
| 14 | sn79 MVTRX | 64.9 | 4.84 | 397 | cpu-small | 210 | 10% |
| 15 | sn61 RedTeam | 64.8 | 155 | 221 | rtx4090* | 46 | 3% |
| 16 | sn81 Reliquary | 64.6 | 146 | 209 | rtx4090* | 34 | 5% |
| 17 | sn54 Yanez | 63.1 | 4.62 | 893 | a4000 | 93 | 35% |
| 18 | sn121 sundae_bar | 62.8 | 1,171 | 1,171 = | cpu-small | 2 | 60% |
| 19 | sn65 True Performance | 62.3 | 82.92 | 174 | rtx4090* | 6 | 75% |
| 20 | sn55 NIOME | 62.2 | 71.84 | 592 | rtx4090* | 11 | 29% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 22 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 100 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-02T11:39 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Update evaluation parameters |
| 2026-09-02T11:39 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Rate-limit validator verification attempt |
| 2026-09-02T11:39 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: validator improvements + database threadi |
| 2026-09-02T11:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-02T11:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair validator supersession test driver |
| 2026-09-02T11:39 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs(validator): update bucket policy an |
| 2026-09-02T06:28 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Join miner and validator lifecycle owners |
| 2026-09-02T06:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2701: withhold incentive from executo |
| 2026-09-02T06:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Handle SOURCE_ADD chain reward quantizati |
| 2026-09-02T01:27 | sn25 | RELEASE | sn25 released v2026.9.1-1035082030 |
| 2026-09-02T01:27 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-01T23:29 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: multiple llm key and improve the scoring |
| 2026-09-01T23:29 | sn104 | README_TASK_DIFF | sn104 README task/scoring sections changed |
| 2026-09-01T21:25 | sn25 | RELEASE | sn25 released v2026.9.1-1034943860 |
| 2026-09-01T21:25 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Run the validator image on the pinned int |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

