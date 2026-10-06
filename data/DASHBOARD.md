# Subnet watch — dashboard

_snapshot 2026-10-06T06:42:28Z · block 9222199 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 79.2 | 337 | 410 | rtx3060 | 4 | 60% |
| 2 | sn41 Almanac | 74.3 | 39.32 | 123 | cpu-small | 127 | 2% |
| 3 | sn23 Trishool | 74.2 | 1,004 | 1,004 = | cpu-small | 2 | 79% |
| 4 | sn91 cascade | 72.2 | 551 | 2,208 | cpu-small | 5 | 52% |
| 5 | sn53 engy | 72 | 1,343 | 3,679 | rtx4090 | 14 | 22% |
| 6 | sn67 Harnyx | 70.2 | 12.91 | 1,066 | cpu-small | 135 | 35% |
| 7 | sn46 Instant | 69.1 | 220 | 275 | cpu-small | 8 | 50% |
| 8 | sn1 Apex | 68.8 | 521 | 993 | rtx4090* | 4 | 68% |
| 9 | sn80 OpenRoboto | 68.4 | 459 | 2,079 | rtx4090* | 8 | 25% |
| 10 | sn15 ORO | 67.5 | 8.94 | 21,938 | cpu-small | 51 | 98% |
| 11 | sn4 Targon | 67.1 | 10,817 | 31,891 | rtx4090* | 5 | 70% |
| 12 | sn111 Claims | 66.8 | 291 | 2,608 | rtx4090* | 5 | 70% |
| 13 | sn14 Cacheon | 64.1 | 128 | 214 | rtx4090* | 6 | 91% |
| 14 | sn62 Ridges | 63.9 | 121 | 1,605 | rtx4090* | 33 | 19% |
| 15 | sn65 True Performance | 62.4 | 81.32 | 171 | rtx4090* | 6 | 75% |
| 16 | sn61 RedTeam | 61.9 | 67.80 | 122 | rtx4090* | 114 | 1% |
| 17 | sn28 SayGM | 60.7 | 47.66 | 3,740 | rtx4090* | 71 | 19% |
| 18 | sn102 ConnitoAI | 59.5 | 1,121 | 1,215 | rtx4090* | 6 | 25% |
| 19 | sn107 Minos | 58.4 | 350 | 27,117 | cpu-small | 20 | 79% |
| 20 | sn74 Gittensor | 58 | 23.49 | 272 | rtx4090* | 21 | 50% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

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
| 2026-10-06T06:43 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge bounded early miner recovery diagno |
| 2026-10-06T06:43 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: feat(validator)!: default-off master swit |
| 2026-10-06T06:43 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-06T06:43 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify round diagnostics preserve recover |
| 2026-10-06T06:43 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #674 from carbonphysi |
| 2026-10-06T06:43 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: feat: opt into bounded single owned veri |
| 2026-10-06T00:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge executable root validator registrat |
| 2026-10-06T00:24 | sn51 | RELEASE | sn51 released executor-v1.137 |
| 2026-10-06T00:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] verifyx: vendor libverif |
| 2026-10-06T00:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Stop the scoring-readiness tests from exe |
| 2026-10-06T00:24 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: docs: mission-first miner README and one  |
| 2026-10-06T00:24 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: chore: increase scoring timeout |
| 2026-10-06T00:24 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #646 from carbonphysi |
| 2026-10-06T00:24 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Keep verifier polling after a terminal b |
| 2026-10-05T18:46 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Switch evaluator to single-GPU replicas an |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

