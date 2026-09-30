# Subnet watch — dashboard

_snapshot 2026-09-30T08:50:20Z · block 9179639 · run_status **ok**_

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
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.4 | 40.24 | 121 | cpu-small | 118 | 13% |
| 2 | sn23 Trishool | 74 | 948 | 948 = | cpu-small | 2 | 80% |
| 3 | sn91 cascade | 72.1 | 540 | 2,163 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 71 | 987 | 1,063 | rtx4090* | 4 | 56% |
| 5 | sn67 Harnyx | 69.4 | 10.47 | 1,098 | cpu-small | 117 | 34% |
| 6 | sn111 Claims | 69 | 573 | 2,536 | rtx4090* | 5 | 64% |
| 7 | sn107 Minos | 69 | 364 | 29,525 | cpu-small | 20 | 79% |
| 8 | sn15 ORO | 69 | 13.12 | 19,879 | cpu-small | 83 | 95% |
| 9 | sn56 Gradients | 68.6 | 490 | 5,329 | rtx4090* | 9 | 39% |
| 10 | sn96 Verathos | 68.3 | 22.87 | 217 | rtx4090 | 75 | 31% |
| 11 | sn102 ConnitoAI | 67.2 | 324 | 1,889 | rtx4090* | 7 | 37% |
| 12 | sn4 Targon | 65.5 | 6,642 | 33,513 | rtx4090* | 5 | 71% |
| 13 | sn14 Cacheon | 64.8 | 157 | 2,307 | rtx4090* | 16 | 29% |
| 14 | sn3 Teutonic | 64.5 | 5,027 | 5,027 = | rtx4090* | 5 | 20% |
| 15 | sn62 Ridges | 64.3 | 133 | 1,154 | rtx4090* | 26 | 13% |
| 16 | sn61 RedTeam | 62.8 | 88.75 | 204 | rtx4090* | 95 | 2% |
| 17 | sn28 SayGM | 61.1 | 54.44 | 717 | rtx4090* | 71 | 36% |
| 18 | sn5 Hone | 59.9 | 41.93 | 44.21 | rtx4090* | 233 | 0% |
| 19 | sn38 ChronoLLM | 59.5 | 447 | 9,455 | cpu-small | 10 | 52% |
| 20 | sn26 Perturb | 59.5 | 34.06 | 37.59 | rtx3060 | 5 | 90% |

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
| wide (<30%) | 21 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 24 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-30T08:50 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Keep validator credentials out of local G |
| 2026-09-30T08:50 | sn51 | RELEASE | sn51 released lium-core-v0.1.13 |
| 2026-09-30T08:50 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3890 - [P1] validator: unique obfusca |
| 2026-09-30T08:50 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #344 from TensorLink-A |
| 2026-09-30T02:18 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Test this release against the previous rel |
| 2026-09-30T02:18 | sn15 | RELEASE | sn15 released v2.0.39: Translate live Chutes model IDs on OpenRouter r |
| 2026-09-30T02:18 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Record foreground waits for prefetched ch |
| 2026-09-30T02:18 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: feat(snp): emit the validator policy entr |
| 2026-09-29T23:14 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Bind evaluator publications to their wind |
| 2026-09-29T19:33 | sn1 | RELEASE | sn1 released v4.4.11 |
| 2026-09-29T19:33 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Merge pull request #10 from hone-subnet-or |
| 2026-09-29T19:33 | sn5 | README_TASK_DIFF | sn5 README task/scoring sections changed |
| 2026-09-29T19:33 | sn15 | RELEASE | sn15 released v2.0.38: fix(agent): retry a 200 inference response whos |
| 2026-09-29T19:33 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.799 - miners can earn again |
| 2026-09-29T19:33 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Separate website from the public subnet a |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

