# Subnet watch — dashboard

_snapshot 2026-10-26T17:39:35Z · block 9369399 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,142 | 4,190 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,810 | 1,810 = | rtx4090* | 5 | 20% |
| 3 | sn46 Instant | 71.6 | 461 | 463 | cpu-small | 4 | 46% |
| 4 | sn60 Bitsec.ai | 70 | 289 | 289 = | cpu-small | 3 | 50% |
| 5 | sn41 Almanac | 68 | 8.67 | 136 | cpu-small | 159 | 2% |
| 6 | sn67 Harnyx | 67.9 | 7.28 | 213 | cpu-small | 125 | 10% |
| 7 | sn1 Apex | 67.8 | 384 | 921 | rtx4090* | 5 | 56% |
| 8 | sn82 Noah | 67.7 | 554 | 560 | rtx4090* | 63 | 2% |
| 9 | sn107 Minos | 66.8 | 216 | 18,172 | cpu-small | 20 | 80% |
| 10 | sn111 Claims | 64.1 | 127 | 2,690 | rtx4090* | 4 | 90% |
| 11 | sn15 ORO | 63.7 | 6.86 | 13.06 | cpu-small | 55 | 97% |
| 12 | sn28 SayGM | 63.6 | 111 | 1,357 | rtx4090* | 96 | 14% |
| 13 | sn120 Affine | 63.5 | 124 | 1,176 | rtx4090* | 152 | 4% |
| 14 | sn66 conjectures | 63.4 | 102 | 212 | rtx4090* | 4 | 80% |
| 15 | sn62 Ridges | 62.7 | 82.76 | 921 | rtx4090* | 44 | 15% |
| 16 | sn23 Trishool | 62.5 | 1,067 | 1,067 = | cpu-small | 2 | 80% |
| 17 | sn81 Reliquary | 59.5 | 31.92 | 264 | rtx4090* | 54 | 29% |
| 18 | sn34 BitMind | 57.8 | 4,489 | 8,506 | a100-80 | 3 | 85% |
| 19 | sn102 ConnitoAI | 57.8 | 688 | 1,053 | rtx4090* | 5 | 32% |
| 20 | sn5 Hone | 57.6 | 29.92 | 35.21 | rtx4090* | 241 | 0% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 25 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-26T17:40 | sn12 | RELEASE | sn12 released validator-staging-2026-10-26-40344021717-627-1: fix: eMu |
| 2026-10-26T17:40 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix(validator): fix prometheus image |
| 2026-10-26T17:40 | sn51 | RELEASE | sn51 released miner-v1.010 |
| 2026-10-26T17:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5187 - [P1] Validator: re-probe misse |
| 2026-10-26T17:40 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: changed scorer model to DeepSeek-V3.2 |
| 2026-10-26T17:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #796 from leadpoet/fix |
| 2026-10-26T17:40 | sn75 | RELEASE | sn75 released Runtime 92023 rc2 (srtool, 873384f) |
| 2026-10-26T17:40 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Enforce broader C7+ evaluation suites (#4 |
| 2026-10-26T17:40 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix(web): display NaN scores properly |
| 2026-10-26T11:28 | sn9 | RELEASE | sn9 released v4.13.9 |
| 2026-10-26T11:28 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: chore(validators): one upload schema and  |
| 2026-10-26T11:28 | sn51 | RELEASE | sn51 released executor-v1.155 |
| 2026-10-26T11:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5075 - [P0] Central miner: retry an e |
| 2026-10-26T11:28 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-26T11:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #794 from leadpoet/fix |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

