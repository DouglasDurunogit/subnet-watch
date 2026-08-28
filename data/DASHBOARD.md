# Subnet watch — dashboard

_snapshot 2026-08-28T11:17:53Z · block 8943256 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 36 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80 | 5,674 | 5,674 = | cpu-small | 1 | 100% |
| 2 | sn3 Teutonic | 75.6 | 3,927 | 3,927 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 74.7 | 42.36 | 172 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 71.5 | 17.84 | 716 | cpu-small | 116 | 18% |
| 5 | sn15 ORO | 70.5 | 21.00 | 23,242 | cpu-small | 76 | 94% |
| 6 | sn1 Apex | 70.1 | 768 | 1,344 | rtx4090* | 4 | 58% |
| 7 | sn96 Verathos | 69 | 26.11 | 146 | rtx4090 | 80 | 40% |
| 8 | sn91 cascade | 68.8 | 516 | 1,390 | rtx4090* | 5 | 52% |
| 9 | sn56 Gradients | 68.4 | 466 | 1,127 | rtx4090* | 7 | 70% |
| 10 | sn102 ConnitoAI | 68.3 | 443 | 1,929 | rtx4090* | 7 | 30% |
| 11 | sn92 MicroTensor | 67.2 | 126 | 204 | cpu-small | 3 | 95% |
| 12 | sn124 Swarm | 66.7 | 288 | 933 | rtx4090* | 25 | 11% |
| 13 | sn61 RedTeam | 65.3 | 184 | 276 | rtx4090* | 36 | 4% |
| 14 | sn80 OpenRoboto | 65 | 164 | 596 | rtx4090* | 4 | 91% |
| 15 | sn107 Minos | 64.5 | 126 | 37,964 | cpu-small | 20 | 90% |
| 16 | sn54 Yanez | 64.4 | 6.90 | 1,137 | a4000 | 103 | 35% |
| 17 | sn81 Reliquary | 63.5 | 105 | 261 | rtx4090* | 41 | 6% |
| 18 | sn65 True Performance | 62.4 | 86.80 | 182 | rtx4090* | 6 | 76% |
| 19 | sn55 NIOME | 62.3 | 72.94 | 600 | rtx4090* | 11 | 29% |
| 20 | sn28 gm | 61.6 | 61.51 | 3,679 | rtx4090* | 46 | 25% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 15 |
| captured (>90%) | 30 |

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
| 2026-08-28T11:18 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add source scores handling and presentatio |
| 2026-08-28T11:18 | sn14 | BURN_DROP | sn14 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-28T11:18 | sn25 | RELEASE | sn25 released v2026.8.28-1031115710 |
| 2026-08-28T11:18 | sn61 | RELEASE | sn61 released 4.10.2 |
| 2026-08-28T11:18 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: chore: update challenge navigation and fi |
| 2026-08-28T11:18 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-28T11:18 | sn80 | SCORING_COMMIT | sn80 commit touches scoring: docs: point miners to the openroboto CLI  |
| 2026-08-28T11:18 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-08-28T11:18 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Carry the miner's published source throug |
| 2026-08-28T11:18 | sn96 | RELEASE | sn96 released Verathos v0.1.42 – Verified MoE, Account Billing, and Ru |
| 2026-08-28T11:18 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: decay endpoint-gated scores at epoch |
| 2026-08-28T11:18 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(validator): the unanimity abort nee |
| 2026-08-28T00:03 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add evaluation history metrics presentatio |
| 2026-08-28T00:03 | sn25 | RELEASE | sn25 released v2026.8.27-1030474020 |
| 2026-08-28T00:03 | sn59 | BURN_DROP | sn59 burn fell 1.000 -> 0.000 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

