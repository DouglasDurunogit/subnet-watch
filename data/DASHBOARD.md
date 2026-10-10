# Subnet watch — dashboard

_snapshot 2026-10-10T15:35:08Z · block 9253658 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `███` |
| 0.6–0.8 | 6 | `██` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.9 | 279 | 23,672 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.9 | 3,235 | 6,478 | rtx4090* | 5 | 30% |
| 3 | sn41 Almanac | 74.6 | 42.05 | 115 | cpu-small | 123 | 2% |
| 4 | sn101 Tag101 | 70.4 | 13.38 | 16.10 | cpu-small | 241 | 1% |
| 5 | sn80 OpenRoboto | 69.4 | 625 | 3,270 | rtx4090* | 7 | 35% |
| 6 | sn67 Harnyx | 68.9 | 9.18 | 893 | cpu-small | 132 | 31% |
| 7 | sn38 ChronoLLM | 68.8 | 214 | 977 | cpu-small | 9 | 52% |
| 8 | sn79 MVTRX | 66.8 | 7.08 | 39.42 | cpu-small | 245 | 2% |
| 9 | sn15 ORO | 66.6 | 6.63 | 13.95 | cpu-small | 51 | 98% |
| 10 | sn26 Perturb | 66.2 | 237 | 396 | rtx3060 | 4 | 60% |
| 11 | sn62 Ridges | 63.9 | 120 | 1,381 | rtx4090* | 36 | 17% |
| 12 | sn65 True Performance | 62.5 | 83.62 | 175 | rtx4090* | 6 | 75% |
| 13 | sn120 Affine | 62.3 | 129 | 492 | rtx4090* | 237 | 1% |
| 14 | sn61 RedTeam | 61.9 | 66.67 | 103 | rtx4090* | 137 | 1% |
| 15 | sn28 SayGM | 61.4 | 58.33 | 860 | rtx4090* | 67 | 28% |
| 16 | sn14 Cacheon | 60.4 | 41.43 | 5,704 | rtx4090* | 6 | 77% |
| 17 | sn53 engy | 59.9 | 1,279 | 2,455 | rtx4090 | 18 | 17% |
| 18 | sn23 Trishool | 59.4 | 420 | 420 = | cpu-small | 3 | 80% |
| 19 | sn91 cascade | 59.3 | 415 | 1,993 | cpu-small | 5 | 49% |
| 20 | sn81 Reliquary | 59.2 | 28.35 | 269 | rtx4090* | 48 | 52% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 26 |
| captured (>90%) | 20 |

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
| 2026-10-10T15:35 | sn25 | RELEASE | sn25 released v2026.10.10-1068404160 |
| 2026-10-10T15:35 | sn28 | RELEASE | sn28 released v0.4.27-dev |
| 2026-10-10T15:35 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.4.27-dev (#310 |
| 2026-10-10T15:35 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Rejudge Oct10 saved outputs on final ATS  |
| 2026-10-10T09:44 | sn25 | RELEASE | sn25 released v2026.10.10-1068162640 |
| 2026-10-10T09:44 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] validator: cap fresh vlo |
| 2026-10-10T09:44 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #328 from leadpoet/cod |
| 2026-10-10T09:44 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document live epoch 116 distinct-task tr |
| 2026-10-10T02:48 | sn25 | RELEASE | sn25 released v2026.10.9-1067985620 |
| 2026-10-10T02:48 | sn62 | RELEASE | sn62 released v0.3.11 |
| 2026-10-10T02:48 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #322 from leadpoet/cod |
| 2026-10-10T02:48 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Support prospective nine-batch mining an |
| 2026-10-09T23:34 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Notify Discord when new hotkeys receive c |
| 2026-10-09T23:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected scorer manifest for req |
| 2026-10-09T23:34 | sn116 | RELEASE | sn116 released producer-code-r6 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

