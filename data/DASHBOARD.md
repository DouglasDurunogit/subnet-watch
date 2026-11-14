# Subnet watch — dashboard

_snapshot 2026-11-14T20:09:15Z · block 9506934 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.8 | 246 | 246 = | cpu-small | 5 | 20% |
| 2 | sn97 Ingot | 71.7 | 1,226 | 1,226 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 70.1 | 753 | 3,973 | rtx4090* | 6 | 50% |
| 4 | sn34 Yugos | 69.6 | 671 | 5,767 | rtx4090* | 3 | 85% |
| 5 | sn58 Attune | 68.7 | 515 | 828 | rtx4090* | 5 | 70% |
| 6 | sn41 Almanac | 68.1 | 8.43 | 124 | cpu-small | 154 | 2% |
| 7 | sn67 Harnyx | 67.3 | 5.85 | 200 | cpu-small | 134 | 14% |
| 8 | sn15 ORO | 66.3 | 5.89 | 12.61 | cpu-small | 71 | 95% |
| 9 | sn124 Swarm | 65.3 | 189 | 792 | rtx4090* | 10 | 31% |
| 10 | sn53 engy | 64.8 | 155 | 6,423 | rtx4090 | 23 | 40% |
| 11 | sn38 ChronoLLM | 63 | 44.96 | 310 | cpu-small | 9 | 52% |
| 12 | sn120 Affine | 61.9 | 2,313 | 2,313 = | rtx4090* | 10 | 10% |
| 13 | sn111 Claims | 60.3 | 40.58 | 163 | rtx4090* | 4 | 88% |
| 14 | sn62 Ridges | 59.7 | 33.74 | 611 | rtx4090* | 44 | 15% |
| 15 | sn4 Targon | 57.7 | 9,297 | 19,937 | rtx4090* | 5 | 62% |
| 16 | sn102 ConnitoAI | 57.2 | 560 | 563 | rtx4090* | 4 | 25% |
| 17 | sn66 conjectures | 56.5 | 12.48 | 1,003 | rtx4090* | 7 | 80% |
| 18 | sn5 Hone | 56.4 | 18.57 | 41.23 | rtx4090* | 241 | 1% |
| 19 | sn46 Instant | 55.5 | 132 | 188 | cpu-small | 9 | 34% |
| 20 | sn1 Apex | 55 | 297 | 660 | rtx4090* | 4 | 65% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 30 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-14T20:09 | sn42 | RELEASE | sn42 released v0.6.15 |
| 2026-11-14T20:09 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: v0.6.15: the reference miner hands a fini |
| 2026-11-14T20:09 | sn116 | BURN_DROP | sn116 burn fell 1.000 -> 0.750 - miners can earn again |
| 2026-11-14T20:09 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Tests: a serve stop leaves a queued task |
| 2026-11-14T15:45 | sn25 | RELEASE | sn25 released v2026.11.14-1098667430 |
| 2026-11-14T15:45 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/validator-attempt-upload-lane-r |
| 2026-11-14T15:45 | sn42 | RELEASE | sn42 released v0.6.13 |
| 2026-11-14T15:45 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: tests: stub the agent CLI checks where th |
| 2026-11-14T15:45 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: forward reported cache write t |
| 2026-11-14T15:45 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Bind subnet API publicly and add task sub |
| 2026-11-14T15:45 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(miner): stop agentic children gracefu |
| 2026-11-14T15:45 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Alert the miner operator on a first misse |
| 2026-11-14T08:55 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge release/validator-1114-idle-fleet:  |
| 2026-11-14T08:55 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Admit miner hotels on a declared capacity |
| 2026-11-14T08:55 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.800 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

