# Subnet watch — dashboard

_snapshot 2026-08-27T14:32:40Z · block 8937032 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 14 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn60 Bitsec.ai | 76.6 | 2,042 | 2,042 = | cpu-small | 2 | 50% |
| 2 | sn3 Teutonic | 75.8 | 4,185 | 4,185 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 75.4 | 50.47 | 204 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 74.1 | 35.92 | 245 | cpu-small | 104 | 7% |
| 5 | sn23 Trishool | 72.4 | 584 | 584 = | cpu-small | 2 | 80% |
| 6 | sn1 Apex | 70.5 | 851 | 1,406 | rtx4090* | 4 | 57% |
| 7 | sn15 ORO | 70.4 | 22.24 | 42.70 | cpu-small | 92 | 92% |
| 8 | sn102 ConnitoAI | 69.7 | 684 | 2,033 | rtx4090* | 7 | 29% |
| 9 | sn91 cascade | 69 | 556 | 1,498 | rtx4090* | 5 | 52% |
| 10 | sn56 Gradients | 68.7 | 497 | 1,194 | rtx4090* | 7 | 70% |
| 11 | sn92 MicroTensor | 67.1 | 121 | 195 | cpu-small | 3 | 95% |
| 12 | sn124 Swarm | 67 | 314 | 943 | rtx4090* | 25 | 10% |
| 13 | sn61 RedTeam | 65.6 | 198 | 283 | rtx4090* | 32 | 5% |
| 14 | sn107 Minos | 64.9 | 138 | 40,820 | cpu-small | 20 | 90% |
| 15 | sn54 Yanez | 64.6 | 7.20 | 1,202 | a4000 | 100 | 35% |
| 16 | sn81 Reliquary | 63.4 | 103 | 246 | rtx4090* | 44 | 5% |
| 17 | sn28 gm | 63.3 | 101 | 3,129 | rtx4090* | 44 | 36% |
| 18 | sn65 True Performance | 63 | 101 | 210 | rtx4090* | 6 | 76% |
| 19 | sn55 NIOME | 62.4 | 76.48 | 627 | rtx4090* | 11 | 29% |
| 20 | sn51 lium.io | 61 | 60.49 | 2,727 | rtx4090* | 56 | 73% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 14 |
| captured (>90%) | 28 |

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
| 2026-08-27T14:33 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Refactor evaluation section in index.html  |
| 2026-08-27T14:33 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: perf(rewards): per-day fingerprint index  |
| 2026-08-27T14:33 | sn25 | RELEASE | sn25 released v2026.8.27-1030161880 |
| 2026-08-27T14:33 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: update validation block number |
| 2026-08-27T14:33 | sn61 | RELEASE | sn61 released 4.10.1 |
| 2026-08-27T14:33 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: chore: update scoring criteria and clarif |
| 2026-08-27T14:33 | sn65 | BURN_DROP | sn65 burn fell 1.000 -> 0.762 - miners can earn again |
| 2026-08-27T14:33 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-27T14:33 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: validator: attest rejected runs so miners |
| 2026-08-27T14:33 | sn92 | BURN_DROP | sn92 burn fell 1.000 -> 0.952 - miners can earn again |
| 2026-08-27T14:33 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Let a miner restore a pointer a reveal ov |
| 2026-08-27T14:33 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(validator): re-post every 30 minute |
| 2026-08-27T14:33 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-08-27T14:33 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(sandbox): scoring JS had no RPC for  |
| 2026-08-27T03:26 | sn25 | RELEASE | sn25 released v2026.8.26-1029908500 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

