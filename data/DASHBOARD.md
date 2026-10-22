# Subnet watch — dashboard

_snapshot 2026-10-22T07:29:24Z · block 9337548 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.6 | 2,214 | 8,054 | rtx4090* | 5 | 46% |
| 2 | sn67 Harnyx | 73.2 | 28.89 | 266 | cpu-small | 39 | 18% |
| 3 | sn91 cascade | 71 | 388 | 1,553 | cpu-small | 5 | 52% |
| 4 | sn120 Affine | 70.4 | 849 | 6,368 | rtx4090* | 22 | 20% |
| 5 | sn102 ConnitoAI | 70.1 | 761 | 1,145 | rtx4090* | 6 | 32% |
| 6 | sn1 Apex | 68.5 | 470 | 894 | rtx4090* | 5 | 54% |
| 7 | sn82 Noah | 67.6 | 594 | 610 | rtx4090* | 62 | 2% |
| 8 | sn15 ORO | 67.6 | 9.02 | 14,900 | cpu-small | 73 | 96% |
| 9 | sn125 Refinery | 67.2 | 325 | 961 | rtx4090* | 4 | 50% |
| 10 | sn53 engy | 67.1 | 313 | 2,563 | rtx4090 | 36 | 11% |
| 11 | sn107 Minos | 67.1 | 230 | 19,575 | cpu-small | 20 | 80% |
| 12 | sn66 conjectures | 63.5 | 105 | 217 | rtx4090* | 4 | 80% |
| 13 | sn26 Perturb | 62.9 | 189 | 237 | rtx3060 | 4 | 60% |
| 14 | sn41 Almanac | 62.2 | 2.81 | 130 | cpu-small | 155 | 3% |
| 15 | sn55 NIOME | 62 | 67.18 | 557 | rtx4090* | 11 | 30% |
| 16 | sn23 Trishool | 61.7 | 843 | 843 = | cpu-small | 2 | 80% |
| 17 | sn92 REAX | 61.4 | 92.50 | 323 | rtx4090 | 243 | 1% |
| 18 | sn111 Claims | 59.4 | 31.35 | 2,825 | rtx4090* | 6 | 90% |
| 19 | sn80 OpenRoboto | 59.1 | 997 | 4,199 | rtx4090* | 11 | 25% |
| 20 | sn117 everyframe.studi | 58.5 | 23.91 | 85.56 | rtx4090* | 8 | 84% |

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
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-22T07:29 | sn28 | RELEASE | sn28 released v0.5.8 |
| 2026-10-22T07:29 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.8 (#343) |
| 2026-10-22T07:29 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4954 - [P0] Validator: revert the alw |
| 2026-10-22T07:29 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-22T07:29 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate Arena round IDs before store fil |
| 2026-10-22T07:29 | sn78 | README_TASK_DIFF | sn78 README task/scoring sections changed |
| 2026-10-22T07:29 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #383 from reliquadotai |
| 2026-10-22T01:57 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Add finalized-chain observer for validator |
| 2026-10-22T01:57 | sn25 | RELEASE | sn25 released v2026.10.21-1078274420 |
| 2026-10-22T01:57 | sn117 | RELEASE | sn117 released everycli v0.7.0 |
| 2026-10-22T01:57 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: test: record final v0.6.3 offline update |
| 2026-10-21T23:30 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.571 - miners can earn again |
| 2026-10-21T23:30 | sn25 | RELEASE | sn25 released v2026.10.21-1078195620 |
| 2026-10-21T23:30 | sn28 | RELEASE | sn28 released v0.5.7 |
| 2026-10-21T23:30 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.7 (#340) |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

