# Subnet watch — dashboard

_snapshot 2026-10-06T13:39:30Z · block 9224284 · run_status **ok**_

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
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 79.2 | 339 | 412 | rtx3060 | 4 | 60% |
| 2 | sn23 Trishool | 74.5 | 1,085 | 1,085 = | cpu-small | 2 | 77% |
| 3 | sn41 Almanac | 74.1 | 36.70 | 124 | cpu-small | 131 | 2% |
| 4 | sn91 cascade | 72.3 | 573 | 2,058 | cpu-small | 5 | 49% |
| 5 | sn53 engy | 72.1 | 1,395 | 3,822 | rtx4090 | 14 | 22% |
| 6 | sn67 Harnyx | 70.3 | 13.02 | 1,074 | cpu-small | 138 | 35% |
| 7 | sn1 Apex | 69.1 | 569 | 964 | rtx4090* | 4 | 68% |
| 8 | sn46 Instant | 69.1 | 224 | 270 | cpu-small | 8 | 51% |
| 9 | sn80 OpenRoboto | 68.3 | 444 | 2,011 | rtx4090* | 8 | 25% |
| 10 | sn4 Targon | 67.1 | 10,901 | 32,140 | rtx4090* | 5 | 70% |
| 11 | sn111 Claims | 66.9 | 293 | 2,626 | rtx4090* | 5 | 70% |
| 12 | sn15 ORO | 65.1 | 8.52 | 17.03 | cpu-small | 52 | 98% |
| 13 | sn14 Cacheon | 64.8 | 154 | 7,136 | rtx4090* | 6 | 91% |
| 14 | sn62 Ridges | 64 | 122 | 1,617 | rtx4090* | 33 | 19% |
| 15 | sn65 True Performance | 62.5 | 83.88 | 176 | rtx4090* | 6 | 75% |
| 16 | sn61 RedTeam | 62.2 | 74.33 | 133 | rtx4090* | 113 | 1% |
| 17 | sn28 SayGM | 60 | 38.96 | 4,967 | rtx4090* | 70 | 24% |
| 18 | sn5 Hone | 58.3 | 38.01 | 41.30 | rtx4090* | 244 | 0% |
| 19 | sn107 Minos | 58.2 | 333 | 26,670 | cpu-small | 20 | 78% |
| 20 | sn102 ConnitoAI | 58 | 719 | 1,878 | rtx4090* | 6 | 40% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 24 |
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
| 2026-10-06T13:39 | sn9 | RELEASE | sn9 released v4.13.5 |
| 2026-10-06T13:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: start the host prob |
| 2026-10-06T13:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-06T13:39 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Minimum improvement comes from the chall |
| 2026-10-06T13:39 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #679 from carbonphysi |
| 2026-10-06T13:39 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document actual E24 learning and partial |
| 2026-10-06T06:43 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge bounded early miner recovery diagno |
| 2026-10-06T06:43 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: feat(validator)!: default-off master swit |
| 2026-10-06T06:43 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-06T06:43 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify round diagnostics preserve recover |
| 2026-10-06T06:43 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #674 from carbonphysi |
| 2026-10-06T06:43 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: feat: opt into bounded single owned veri |
| 2026-10-06T00:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge executable root validator registrat |
| 2026-10-06T00:24 | sn51 | RELEASE | sn51 released executor-v1.137 |
| 2026-10-06T00:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] verifyx: vendor libverif |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

