# Subnet watch — dashboard

_snapshot 2026-10-02T08:52:05Z · block 9194047 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 75 | 45.97 | 135 | cpu-small | 121 | 2% |
| 2 | sn23 Trishool | 74.3 | 1,025 | 1,025 = | cpu-small | 2 | 79% |
| 3 | sn91 cascade | 72.7 | 636 | 2,304 | cpu-small | 5 | 49% |
| 4 | sn53 engy | 72.3 | 1,470 | 4,032 | rtx4090 | 14 | 22% |
| 5 | sn1 Apex | 70.5 | 860 | 1,033 | rtx4090* | 4 | 59% |
| 6 | sn120 Affine | 69.8 | 718 | 718 = | rtx4090* | 59 | 2% |
| 7 | sn67 Harnyx | 69 | 9.69 | 1,169 | cpu-small | 112 | 35% |
| 8 | sn107 Minos | 68.7 | 340 | 30,387 | cpu-small | 19 | 82% |
| 9 | sn46 Instant | 68.1 | 163 | 200 | cpu-small | 7 | 69% |
| 10 | sn96 Verathos | 68 | 21.21 | 247 | rtx4090 | 76 | 30% |
| 11 | sn14 Cacheon | 67.8 | 384 | 1,904 | rtx4090* | 13 | 23% |
| 12 | sn56 Gradients | 67.3 | 328 | 5,415 | rtx4090* | 9 | 39% |
| 13 | sn111 Claims | 67 | 313 | 2,803 | rtx4090* | 5 | 70% |
| 14 | sn4 Targon | 65.6 | 6,989 | 33,055 | rtx4090* | 5 | 70% |
| 15 | sn3 Teutonic | 64.3 | 4,751 | 4,751 = | rtx4090* | 5 | 20% |
| 16 | sn61 RedTeam | 62.6 | 84.17 | 153 | rtx4090* | 116 | 2% |
| 17 | sn28 SayGM | 61.2 | 56.11 | 884 | rtx4090* | 66 | 26% |
| 18 | sn62 Ridges | 60.7 | 50.02 | 3,464 | rtx4090* | 27 | 36% |
| 19 | sn5 Hone | 59.5 | 40.71 | 42.67 | rtx4090* | 242 | 0% |
| 20 | sn26 Perturb | 59.2 | 31.04 | 31.04 = | rtx3060 | 4 | 90% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 24 |
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
| 2026-10-02T08:53 | sn51 | RELEASE | sn51 released validator-v2026.10.02 |
| 2026-10-02T08:53 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] validator: a shell lost  |
| 2026-10-02T08:53 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-02T08:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #200 from leadpoet/cod |
| 2026-10-02T08:53 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Point C5 miner upgrade at enrollment runt |
| 2026-10-02T08:53 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #297 from reliquadotai |
| 2026-10-02T08:53 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Receipts verify across code versions; a s |
| 2026-10-02T08:53 | sn117 | RELEASE | sn117 released everycli v0.2.2 |
| 2026-10-02T02:26 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Show consumed evaluation credits in dashb |
| 2026-10-02T02:26 | sn111 | RELEASE | sn111 released v1.0.1 |
| 2026-10-02T02:26 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Reproduce per-task Pydantic proposal con |
| 2026-10-01T23:09 | sn14 | RELEASE | sn14 released GLM crowned baseline source — 2026-10-01 |
| 2026-10-01T23:09 | sn15 | RELEASE | sn15 released v2.0.40: Composed situation tasks: validator, proxy and  |
| 2026-10-01T23:09 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Composed situation tasks: validator, prox |
| 2026-10-01T23:09 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

