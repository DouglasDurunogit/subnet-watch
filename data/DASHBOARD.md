# Subnet watch — dashboard

_snapshot 2026-09-07T17:49:20Z · block 9017159 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.3 | 998 | 7,991 | cpu-small | 3 | 80% |
| 2 | sn92 MicroTensor | 79.4 | 136 | 411 | cpu-small | 9 | 50% |
| 3 | sn107 Minos | 77 | 92.98 | 5,904 | cpu-small | 21 | 80% |
| 4 | sn3 Teutonic | 76.1 | 4,582 | 4,582 = | rtx4090* | 5 | 20% |
| 5 | sn67 Harnyx | 72.8 | 25.15 | 423 | cpu-small | 129 | 11% |
| 6 | sn91 cascade | 70.6 | 883 | 3,555 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.6 | 24.20 | 22,354 | cpu-small | 77 | 92% |
| 8 | sn96 Verathos | 70.3 | 35.82 | 560 | rtx4090 | 76 | 40% |
| 9 | sn80 OpenRoboto | 70.1 | 754 | 4,793 | rtx4090* | 5 | 43% |
| 10 | sn102 ConnitoAI | 68.7 | 506 | 1,827 | rtx4090* | 7 | 32% |
| 11 | sn62 Ridges | 68.2 | 429 | 1,274 | rtx4090* | 13 | 26% |
| 12 | sn124 Swarm | 66.9 | 302 | 928 | rtx4090* | 25 | 11% |
| 13 | sn111 Claims | 66.6 | 289 | 2,592 | rtx4090* | 5 | 55% |
| 14 | sn14 Cacheon | 66.1 | 234 | 3,084 | rtx4090* | 7 | 43% |
| 15 | sn21 AdTAO | 62.8 | 3.12 | 196 | cpu-small | 16 | 34% |
| 16 | sn65 True Performance | 62.6 | 92.49 | 193 | rtx4090* | 6 | 75% |
| 17 | sn108 Prometheon | 60.7 | 46.32 | 137 | rtx4090* | 10 | 33% |
| 18 | sn41 Almanac | 60.5 | 40.64 | 104 | cpu-small | 86 | 7% |
| 19 | sn28 SayGM | 59.7 | 35.57 | 7,498 | rtx4090* | 47 | 47% |
| 20 | sn51 lium.io | 58.4 | 31.99 | 3,228 | rtx4090* | 64 | 73% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 19 |
| captured (>90%) | 22 |

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
| 2026-09-07T17:49 | sn1 | RELEASE | sn1 released v4.4.2 |
| 2026-09-07T17:49 | sn25 | RELEASE | sn25 released v2026.9.7-1039843330 |
| 2026-09-07T17:49 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Set explicit 100% burn and bypass reward  |
| 2026-09-07T17:49 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to the latest vers |
| 2026-09-07T17:49 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #76 from conjectures-i |
| 2026-09-07T12:22 | sn18 | RELEASE | sn18 released Release 2.1.4 |
| 2026-09-07T12:22 | sn18 | SCORING_COMMIT | sn18 commit touches scoring: Stop emissions for non-participating mine |
| 2026-09-07T12:22 | sn25 | RELEASE | sn25 released v2026.9.7-1039747440 |
| 2026-09-07T12:22 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: [P1] feat: run the miners tests and ruff  |
| 2026-09-07T12:22 | sn66 | RELEASE | sn66 released v.1.0.3: Web submissions, payouts, contributions... |
| 2026-09-07T12:22 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-07T12:22 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: chore: bind verified controller upgrade r |
| 2026-09-07T12:22 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Harden macOS validator audit origin |
| 2026-09-07T12:22 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-07T12:22 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: archive: a rewarded system is archived wh |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

