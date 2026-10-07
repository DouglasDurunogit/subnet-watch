# Subnet watch — dashboard

_snapshot 2026-10-07T21:27:55Z · block 9233826 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 70.9 | 373 | 997 | cpu-small | 5 | 52% |
| 2 | sn38 ChronoLLM | 69.8 | 285 | 1,935 | cpu-small | 9 | 52% |
| 3 | sn1 Apex | 69 | 542 | 990 | rtx4090* | 4 | 69% |
| 4 | sn67 Harnyx | 68.8 | 8.91 | 1,000 | cpu-small | 136 | 34% |
| 5 | sn80 OpenRoboto | 68.6 | 489 | 1,878 | rtx4090* | 8 | 28% |
| 6 | sn46 Instant | 68.6 | 192 | 248 | cpu-small | 9 | 46% |
| 7 | sn15 ORO | 67.8 | 8.90 | 19,636 | cpu-small | 63 | 97% |
| 8 | sn4 Targon | 67 | 10,415 | 30,701 | rtx4090* | 5 | 70% |
| 9 | sn26 Perturb | 66.1 | 236 | 395 | rtx3060 | 4 | 60% |
| 10 | sn62 Ridges | 63.8 | 115 | 1,408 | rtx4090* | 34 | 17% |
| 11 | sn120 Affine | 63.6 | 170 | 228 | rtx4090* | 231 | 1% |
| 12 | sn61 RedTeam | 62.5 | 81.66 | 118 | rtx4090* | 132 | 1% |
| 13 | sn65 True Performance | 62.4 | 80.15 | 169 | rtx4090* | 6 | 75% |
| 14 | sn53 engy | 60 | 1,324 | 2,541 | rtx4090 | 18 | 17% |
| 15 | sn14 Cacheon | 59.8 | 34.93 | 2,624 | rtx4090* | 7 | 54% |
| 16 | sn23 Trishool | 59.6 | 455 | 455 = | cpu-small | 3 | 80% |
| 17 | sn41 Almanac | 58.8 | 26.95 | 119 | cpu-small | 139 | 2% |
| 18 | sn74 Gittensor | 58.3 | 25.41 | 157 | rtx4090* | 21 | 50% |
| 19 | sn28 SayGM | 58.1 | 22.98 | 1,283 | rtx4090* | 75 | 43% |
| 20 | sn107 Minos | 58 | 318 | 26,031 | cpu-small | 20 | 80% |

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
| dominated (60–90%) | 27 |
| captured (>90%) | 25 |

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
| 2026-10-07T21:28 | sn15 | RELEASE | sn15 released v2.3.0 |
| 2026-10-07T21:28 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge the sole validator's activation-pen |
| 2026-10-07T21:28 | sn50 | RELEASE | sn50 released v1.14.0 |
| 2026-10-07T21:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: encrypted volume an |
| 2026-10-07T21:28 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: help miners to sign message |
| 2026-10-07T21:28 | sn54 | README_TASK_DIFF | sn54 README task/scoring sections changed |
| 2026-10-07T21:28 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: tasks: an unusable identity home is an id |
| 2026-10-07T21:28 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-10-07T21:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #265: refresh protected verifier |
| 2026-10-07T21:28 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Fix pinned operator generation task admis |
| 2026-10-07T21:28 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Admit explicitly signed source-bound ver |
| 2026-10-07T16:23 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add math, code, and text competitions with |
| 2026-10-07T16:23 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Bind configured Readers to cancellable mi |
| 2026-10-07T16:23 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.978 - miners can earn again |
| 2026-10-07T16:23 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Leak returns to the score at 30%, over a  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

