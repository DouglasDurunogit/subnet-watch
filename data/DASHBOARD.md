# Subnet watch — dashboard

_snapshot 2026-10-02T15:44:26Z · block 9196109 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.9 | 45.03 | 133 | cpu-small | 121 | 2% |
| 2 | sn23 Trishool | 74 | 946 | 946 = | cpu-small | 2 | 80% |
| 3 | sn91 cascade | 72.8 | 669 | 2,677 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 72.1 | 1,376 | 3,775 | rtx4090 | 14 | 22% |
| 5 | sn56 Gradients | 70.8 | 946 | 5,497 | rtx4090* | 8 | 40% |
| 6 | sn1 Apex | 70.3 | 814 | 985 | rtx4090* | 4 | 61% |
| 7 | sn120 Affine | 69.6 | 712 | 712 = | rtx4090* | 59 | 2% |
| 8 | sn107 Minos | 68.8 | 347 | 29,488 | cpu-small | 20 | 80% |
| 9 | sn67 Harnyx | 68.8 | 9.44 | 1,141 | cpu-small | 119 | 35% |
| 10 | sn46 Instant | 67.9 | 154 | 191 | cpu-small | 7 | 69% |
| 11 | sn14 Cacheon | 67.3 | 327 | 1,879 | rtx4090* | 13 | 23% |
| 12 | sn111 Claims | 67.1 | 322 | 2,517 | rtx4090* | 6 | 63% |
| 13 | sn4 Targon | 65.6 | 6,918 | 32,724 | rtx4090* | 5 | 70% |
| 14 | sn3 Teutonic | 64.3 | 4,685 | 4,685 = | rtx4090* | 5 | 20% |
| 15 | sn61 RedTeam | 62.7 | 84.12 | 152 | rtx4090* | 113 | 2% |
| 16 | sn28 SayGM | 61.3 | 57.44 | 1,032 | rtx4090* | 67 | 19% |
| 17 | sn62 Ridges | 60.8 | 49.28 | 3,420 | rtx4090* | 27 | 36% |
| 18 | sn5 Hone | 59.5 | 40.03 | 42.15 | rtx4090* | 243 | 0% |
| 19 | sn80 OpenRoboto | 58.9 | 942 | 3,520 | rtx4090* | 8 | 33% |
| 20 | sn38 ChronoLLM | 58.5 | 342 | 4,649 | cpu-small | 10 | 52% |

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
| 2026-10-02T15:44 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record scoped native miner monitor and ba |
| 2026-10-02T15:44 | sn51 | RELEASE | sn51 released validator-v2026.10.02.2 |
| 2026-10-02T15:44 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: check a present Doc |
| 2026-10-02T15:44 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify extended recovery schedule on migr |
| 2026-10-02T15:44 | sn74 | RELEASE | sn74 released release-20261002-144641 |
| 2026-10-02T15:44 | sn74 | README_TASK_DIFF | sn74 README task/scoring sections changed |
| 2026-10-02T15:44 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Alert when successor validators stop reco |
| 2026-10-02T15:44 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(corpus): auditor miners.json on the j |
| 2026-10-02T15:44 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf: diversity-blocked qualified miners ke |
| 2026-10-02T15:44 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: swesmith tasks are served as one ups |
| 2026-10-02T15:44 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Bootstrap external MATH miners from auth |
| 2026-10-02T08:53 | sn51 | RELEASE | sn51 released validator-v2026.10.02 |
| 2026-10-02T08:53 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] validator: a shell lost  |
| 2026-10-02T08:53 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-02T08:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #200 from leadpoet/cod |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

