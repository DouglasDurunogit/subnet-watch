# Subnet watch — dashboard

_snapshot 2026-10-02T02:25:33Z · block 9192115 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.9 | 44.89 | 132 | cpu-small | 121 | 2% |
| 2 | sn23 Trishool | 74.1 | 970 | 970 = | cpu-small | 2 | 80% |
| 3 | sn91 cascade | 72.4 | 586 | 2,348 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 72.3 | 1,456 | 3,994 | rtx4090 | 14 | 22% |
| 5 | sn1 Apex | 70.5 | 870 | 1,038 | rtx4090* | 4 | 58% |
| 6 | sn120 Affine | 69.7 | 719 | 719 = | rtx4090* | 58 | 2% |
| 7 | sn107 Minos | 68.8 | 344 | 29,183 | cpu-small | 20 | 80% |
| 8 | sn46 Instant | 68.6 | 189 | 214 | cpu-small | 6 | 68% |
| 9 | sn15 ORO | 68.5 | 12.28 | 20,779 | cpu-small | 71 | 96% |
| 10 | sn102 ConnitoAI | 68.3 | 451 | 1,845 | rtx4090* | 7 | 37% |
| 11 | sn14 Cacheon | 67.9 | 400 | 1,664 | rtx4090* | 13 | 21% |
| 12 | sn96 Verathos | 67.8 | 20.28 | 255 | rtx4090 | 76 | 33% |
| 13 | sn111 Claims | 67.5 | 361 | 2,146 | rtx4090* | 6 | 55% |
| 14 | sn56 Gradients | 67.2 | 320 | 5,276 | rtx4090* | 9 | 39% |
| 15 | sn4 Targon | 65.4 | 6,506 | 32,876 | rtx4090* | 5 | 71% |
| 16 | sn3 Teutonic | 64.4 | 4,916 | 4,916 = | rtx4090* | 5 | 20% |
| 17 | sn61 RedTeam | 62.5 | 82.32 | 149 | rtx4090* | 116 | 2% |
| 18 | sn28 SayGM | 61.7 | 63.31 | 1,812 | rtx4090* | 65 | 16% |
| 19 | sn62 Ridges | 60.8 | 48.96 | 3,401 | rtx4090* | 27 | 36% |
| 20 | sn5 Hone | 59.5 | 39.58 | 42.20 | rtx4090* | 242 | 0% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 25 |
| captured (>90%) | 23 |

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
| 2026-10-02T02:26 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Show consumed evaluation credits in dashb |
| 2026-10-02T02:26 | sn111 | RELEASE | sn111 released v1.0.1 |
| 2026-10-02T02:26 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Reproduce per-task Pydantic proposal con |
| 2026-10-01T23:09 | sn14 | RELEASE | sn14 released GLM crowned baseline source — 2026-10-01 |
| 2026-10-01T23:09 | sn15 | RELEASE | sn15 released v2.0.40: Composed situation tasks: validator, proxy and  |
| 2026-10-01T23:09 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Composed situation tasks: validator, prox |
| 2026-10-01T23:09 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-10-01T23:09 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Export signed closed-window scores withou |
| 2026-10-01T23:09 | sn62 | RELEASE | sn62 released v0.3.9 |
| 2026-10-01T23:09 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Keep miner upgrades cohort-neutral |
| 2026-10-01T23:09 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #294 from reliquadotai |
| 2026-10-01T23:09 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document independently verified Wiki sig |
| 2026-10-01T19:04 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Clarify legacy and event scoring in the b |
| 2026-10-01T19:04 | sn22 | BURN_DROP | sn22 burn fell 1.000 -> 0.809 - miners can earn again |
| 2026-10-01T19:04 | sn46 | RELEASE | sn46 released v0.1.3 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

