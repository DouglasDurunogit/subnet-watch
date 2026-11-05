# Subnet watch — dashboard

_snapshot 2026-11-05T03:45:43Z · block 9437220 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.7 | 2,997 | 2,997 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,943 | 3,895 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.6 | 1,604 | 1,604 = | rtx4090* | 5 | 20% |
| 4 | sn58 Attune | 68.7 | 509 | 820 | rtx4090* | 5 | 70% |
| 5 | sn56 Gradients | 68.6 | 481 | 5,178 | rtx4090* | 7 | 51% |
| 6 | sn1 Apex | 67.6 | 360 | 826 | rtx4090* | 4 | 69% |
| 7 | sn102 ConnitoAI | 67.4 | 341 | 1,122 | rtx4090* | 7 | 33% |
| 8 | sn41 Almanac | 67.3 | 7.29 | 136 | cpu-small | 177 | 4% |
| 9 | sn82 Noah | 66.5 | 392 | 460 | rtx4090* | 64 | 2% |
| 10 | sn107 Minos | 66.2 | 185 | 15,708 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 66 | 6.31 | 12,087 | cpu-small | 71 | 96% |
| 12 | sn53 engy | 65.4 | 189 | 3,113 | rtx4090 | 31 | 21% |
| 13 | sn67 Harnyx | 65 | 3.61 | 496 | cpu-small | 142 | 26% |
| 14 | sn70 Fugal | 64.5 | 146 | 398 | rtx4090* | 48 | 5% |
| 15 | sn38 ChronoLLM | 63.5 | 53.39 | 476 | cpu-small | 10 | 52% |
| 16 | sn66 conjectures | 63 | 92.42 | 193 | rtx4090* | 4 | 80% |
| 17 | sn124 Swarm | 62.8 | 98.56 | 1,881 | rtx4090* | 15 | 31% |
| 18 | sn62 Ridges | 61.9 | 65.93 | 1,226 | rtx4090* | 37 | 22% |
| 19 | sn55 NIOME | 61.3 | 53.85 | 457 | rtx4090* | 11 | 30% |
| 20 | sn60 Bitsec.ai | 60.1 | 514 | 792 | cpu-small | 3 | 50% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 26 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-05T03:46 | sn27 | RELEASE | sn27 released archive/worktrees-2026-11-04 |
| 2026-11-05T03:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Recover only the infrastructure-damaged N |
| 2026-11-05T03:46 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Merge pull request #6: Improve validator  |
| 2026-11-05T03:46 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Owner manifest migration: encode the Val |
| 2026-11-05T03:46 | sn126 | BURN_DROP | sn126 burn fell 1.000 -> 0.955 - miners can earn again |
| 2026-11-04T23:36 | sn12 | RELEASE | sn12 released sdk-v0.0.20: feat: local executor and local bind mount v |
| 2026-11-04T23:36 | sn58 | SCORING_COMMIT | sn58 commit touches scoring: feat(validator): only a permitted Hub acc |
| 2026-11-04T23:36 | sn58 | README_TASK_DIFF | sn58 README task/scoring sections changed |
| 2026-11-04T23:36 | sn70 | RELEASE | sn70 released image-v2026.11.05 |
| 2026-11-04T23:36 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Pin reviewed scorer checkpoint imports in |
| 2026-11-04T23:36 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(admin): deliver evaluation files to t |
| 2026-11-04T23:36 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: local-gsm8k: a reply over 100 KB is pass |
| 2026-11-04T17:58 | sn1 | RELEASE | sn1 released v4.7.0 |
| 2026-11-04T17:58 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Set document evaluation lower bound to 2 t |
| 2026-11-04T17:58 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.605 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

