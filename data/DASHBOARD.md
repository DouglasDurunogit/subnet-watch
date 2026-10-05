# Subnet watch — dashboard

_snapshot 2026-10-05T18:45:48Z · block 9218616 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 79.1 | 326 | 406 | rtx3060 | 4 | 60% |
| 2 | sn23 Trishool | 74.6 | 1,145 | 1,145 = | cpu-small | 2 | 76% |
| 3 | sn41 Almanac | 74 | 36.22 | 104 | cpu-small | 123 | 29% |
| 4 | sn91 cascade | 72.2 | 552 | 2,210 | cpu-small | 5 | 52% |
| 5 | sn53 engy | 71.9 | 1,305 | 3,577 | rtx4090 | 14 | 22% |
| 6 | sn46 Instant | 69.3 | 235 | 299 | cpu-small | 8 | 49% |
| 7 | sn67 Harnyx | 69.1 | 9.55 | 1,233 | cpu-small | 136 | 40% |
| 8 | sn1 Apex | 69 | 549 | 1,049 | rtx4090* | 4 | 65% |
| 9 | sn80 OpenRoboto | 68.6 | 481 | 2,176 | rtx4090* | 8 | 25% |
| 10 | sn4 Targon | 67.1 | 10,750 | 31,696 | rtx4090* | 5 | 70% |
| 11 | sn111 Claims | 66.9 | 293 | 2,625 | rtx4090* | 5 | 70% |
| 12 | sn15 ORO | 64.7 | 9.32 | 18.59 | cpu-small | 51 | 98% |
| 13 | sn62 Ridges | 64.1 | 128 | 1,914 | rtx4090* | 32 | 21% |
| 14 | sn65 True Performance | 62.4 | 81.77 | 172 | rtx4090* | 6 | 75% |
| 15 | sn61 RedTeam | 61.9 | 66.49 | 121 | rtx4090* | 129 | 1% |
| 16 | sn14 Cacheon | 61.1 | 51.84 | 827 | rtx4090* | 13 | 60% |
| 17 | sn28 SayGM | 59.5 | 33.58 | 2,448 | rtx4090* | 64 | 31% |
| 18 | sn5 Hone | 58.4 | 37.60 | 40.85 | rtx4090* | 243 | 0% |
| 19 | sn107 Minos | 58.2 | 340 | 28,247 | cpu-small | 20 | 79% |
| 20 | sn74 Gittensor | 58.1 | 23.98 | 272 | rtx4090* | 21 | 50% |

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
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 23 |
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
| 2026-10-05T18:46 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Switch evaluator to single-GPU replicas an |
| 2026-10-05T18:46 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): the reg-index staleness a |
| 2026-10-05T18:46 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(task-api): judge completions when the |
| 2026-10-05T18:46 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: fix(miner): preserve boolean CLI option d |
| 2026-10-05T18:46 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: perf(validator): reuse dendrite process p |
| 2026-10-05T18:46 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: connector reads the |
| 2026-10-05T18:46 | sn61 | RELEASE | sn61 released 4.10.9 |
| 2026-10-05T18:46 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: refactor: increase max_unique_commits for |
| 2026-10-05T18:46 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: update miner docs |
| 2026-10-05T18:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-05T18:46 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: MINER_TERMS §3: publish rate version earn |
| 2026-10-05T18:46 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Add prospective owned cached native eval |
| 2026-10-05T09:25 | sn49 | SCORING_COMMIT | sn49 commit touches scoring: Upgrade validator sandbox to Isaac Sim 6. |
| 2026-10-05T09:25 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P2] Validator scrape: record |
| 2026-10-05T09:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Document resource-safe model capacity for |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

