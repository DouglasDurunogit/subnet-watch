# Subnet watch — dashboard

_snapshot 2026-09-09T01:12:58Z · block 9026571 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.2 | 992 | 7,941 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.7 | 424 | 34,585 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 79.2 | 130 | 393 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76.1 | 4,500 | 4,500 = | rtx4090* | 5 | 20% |
| 5 | sn15 ORO | 71.1 | 25.37 | 53.46 | cpu-small | 76 | 93% |
| 6 | sn67 Harnyx | 70.7 | 15.22 | 1,344 | cpu-small | 124 | 37% |
| 7 | sn91 cascade | 70.3 | 822 | 3,312 | rtx4090* | 5 | 52% |
| 8 | sn14 Cacheon | 69.7 | 683 | 1,265 | rtx4090* | 12 | 18% |
| 9 | sn96 Verathos | 69.7 | 31.44 | 396 | rtx4090 | 85 | 33% |
| 10 | sn102 ConnitoAI | 68.8 | 523 | 2,022 | rtx4090* | 7 | 35% |
| 11 | sn11 TrajectoryRL | 68.7 | 6,790 | 6,790 = | cpu-small | 1 | 100% |
| 12 | sn62 Ridges | 68.1 | 425 | 1,262 | rtx4090* | 13 | 26% |
| 13 | sn56 Gradients | 67.8 | 383 | 5,940 | rtx4090* | 9 | 47% |
| 14 | sn80 OpenRoboto | 67.5 | 351 | 1,249 | rtx4090* | 5 | 43% |
| 15 | sn38 ChronoLLM | 65.9 | 98.89 | 1,352 | cpu-small | 10 | 52% |
| 16 | sn111 Claims | 65.8 | 230 | 2,077 | rtx4090* | 5 | 48% |
| 17 | sn121 sundae_bar | 63.3 | 1,335 | 1,335 = | cpu-small | 2 | 60% |
| 18 | sn65 True Performance | 62.5 | 89.57 | 187 | rtx4090* | 6 | 75% |
| 19 | sn41 Almanac | 60.7 | 42.74 | 119 | cpu-small | 85 | 3% |
| 20 | sn28 SayGM | 58.9 | 28.42 | 6,816 | rtx4090* | 52 | 40% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 20 |

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
| 2026-09-09T01:13 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: build: refresh protected scoring source m |
| 2026-09-09T01:13 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validator): enable rigor validation  |
| 2026-09-08T22:52 | sn15 | RELEASE | sn15 released v1.2.13: compose: forward SUBTENSOR_CHAIN_ENDPOINT to th |
| 2026-09-08T22:52 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: compose: forward SUBTENSOR_CHAIN_ENDPOINT |
| 2026-09-08T22:52 | sn25 | RELEASE | sn25 released v2026.9.8-1040985530 |
| 2026-09-08T22:52 | sn28 | RELEASE | sn28 released v0.4.15 |
| 2026-09-08T22:52 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: fix(miner): render node secret last and p |
| 2026-09-08T22:52 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-08T22:52 | sn78 | WEIGHTS_VERSION_BUMP | sn78 weights_version 0 -> 1 |
| 2026-09-08T20:19 | sn2 | RELEASE | sn2 released 14.14.3 |
| 2026-09-08T20:19 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Introduce weight commit guard for epochs w |
| 2026-09-08T20:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-08T20:19 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Fix bootstrap image revision validation |
| 2026-09-08T20:19 | sn96 | RELEASE | sn96 released Verathos v0.2.2 – Consistent Validator Decisions and Mic |
| 2026-09-08T17:34 | sn25 | RELEASE | sn25 released v2026.9.8-1040779940 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

