# Subnet watch — dashboard

_snapshot 2026-10-02T20:10:41Z · block 9197440 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.6 | 41.54 | 122 | cpu-small | 121 | 2% |
| 2 | sn23 Trishool | 74.5 | 1,094 | 1,094 = | cpu-small | 2 | 75% |
| 3 | sn91 cascade | 72.6 | 620 | 2,482 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 71.8 | 1,283 | 3,522 | rtx4090 | 14 | 22% |
| 5 | sn56 Gradients | 70.7 | 920 | 4,953 | rtx4090* | 8 | 39% |
| 6 | sn1 Apex | 69.9 | 726 | 1,099 | rtx4090* | 4 | 58% |
| 7 | sn46 Instant | 69.2 | 228 | 284 | cpu-small | 7 | 51% |
| 8 | sn120 Affine | 69.1 | 596 | 596 = | rtx4090* | 65 | 2% |
| 9 | sn67 Harnyx | 68.7 | 8.66 | 1,055 | cpu-small | 120 | 35% |
| 10 | sn107 Minos | 68.5 | 320 | 27,199 | cpu-small | 20 | 80% |
| 11 | sn14 Cacheon | 67 | 301 | 1,734 | rtx4090* | 13 | 23% |
| 12 | sn111 Claims | 66.7 | 287 | 2,571 | rtx4090* | 5 | 70% |
| 13 | sn4 Targon | 65.3 | 6,410 | 30,322 | rtx4090* | 5 | 70% |
| 14 | sn3 Teutonic | 64 | 4,317 | 4,317 = | rtx4090* | 5 | 20% |
| 15 | sn61 RedTeam | 62.4 | 77.22 | 140 | rtx4090* | 113 | 2% |
| 16 | sn62 Ridges | 60.5 | 45.08 | 2,733 | rtx4090* | 28 | 31% |
| 17 | sn28 SayGM | 59.2 | 30.85 | 1,088 | rtx4090* | 76 | 38% |
| 18 | sn5 Hone | 59.1 | 36.39 | 38.35 | rtx4090* | 245 | 0% |
| 19 | sn80 OpenRoboto | 58.8 | 903 | 3,374 | rtx4090* | 8 | 33% |
| 20 | sn38 ChronoLLM | 58.3 | 322 | 4,369 | cpu-small | 10 | 52% |

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
| wide (<30%) | 20 |
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 22 |
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
| 2026-10-02T20:11 | sn1 | RELEASE | sn1 released v4.4.12 |
| 2026-10-02T20:11 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Capture cached input tokens in private ev |
| 2026-10-02T20:11 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Preserve qualification headroom with veri |
| 2026-10-02T20:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Archive October 1 optional-signal scores  |
| 2026-10-02T20:11 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(corpus): a GPU process that scores e |
| 2026-10-02T20:11 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Fix fork sentinel command verification (# |
| 2026-10-02T20:11 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: Merge pull request #15 from taostatus/fe |
| 2026-10-02T20:11 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Project the separated math pilot and pub |
| 2026-10-02T15:44 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record scoped native miner monitor and ba |
| 2026-10-02T15:44 | sn51 | RELEASE | sn51 released validator-v2026.10.02.2 |
| 2026-10-02T15:44 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: check a present Doc |
| 2026-10-02T15:44 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify extended recovery schedule on migr |
| 2026-10-02T15:44 | sn74 | RELEASE | sn74 released release-20261002-144641 |
| 2026-10-02T15:44 | sn74 | README_TASK_DIFF | sn74 README task/scoring sections changed |
| 2026-10-02T15:44 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Alert when successor validators stop reco |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

