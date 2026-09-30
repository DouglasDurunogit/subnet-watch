# Subnet watch — dashboard

_snapshot 2026-09-30T02:18:03Z · block 9177677 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 75.5 | 51.95 | 118 | cpu-small | 118 | 2% |
| 2 | sn23 Trishool | 74 | 950 | 950 = | cpu-small | 2 | 80% |
| 3 | sn91 cascade | 72.3 | 565 | 2,045 | cpu-small | 5 | 49% |
| 4 | sn1 Apex | 71.1 | 1,020 | 1,097 | rtx4090* | 4 | 54% |
| 5 | sn102 ConnitoAI | 71 | 987 | 1,715 | rtx4090* | 6 | 33% |
| 6 | sn26 Perturb | 70.1 | 34.91 | 123 | rtx3060 | 5 | 90% |
| 7 | sn111 Claims | 69 | 567 | 2,509 | rtx4090* | 5 | 64% |
| 8 | sn107 Minos | 69 | 363 | 30,539 | cpu-small | 20 | 80% |
| 9 | sn15 ORO | 68.9 | 13.02 | 19,876 | cpu-small | 75 | 95% |
| 10 | sn67 Harnyx | 68.8 | 8.83 | 1,247 | cpu-small | 130 | 38% |
| 11 | sn56 Gradients | 68.6 | 491 | 5,337 | rtx4090* | 9 | 39% |
| 12 | sn96 Verathos | 68.4 | 23.41 | 249 | rtx4090 | 75 | 30% |
| 13 | sn4 Targon | 67.4 | 11,658 | 32,806 | rtx4090* | 3 | 69% |
| 14 | sn3 Teutonic | 64.5 | 5,075 | 5,075 = | rtx4090* | 5 | 20% |
| 15 | sn14 Cacheon | 64.3 | 136 | 2,312 | rtx4090* | 15 | 29% |
| 16 | sn62 Ridges | 64.2 | 133 | 1,155 | rtx4090* | 26 | 13% |
| 17 | sn61 RedTeam | 62.8 | 88.37 | 204 | rtx4090* | 95 | 2% |
| 18 | sn28 SayGM | 60.4 | 43.71 | 940 | rtx4090* | 71 | 29% |
| 19 | sn5 Hone | 59.9 | 40.23 | 42.51 | rtx4090* | 242 | 0% |
| 20 | sn38 ChronoLLM | 59.5 | 452 | 9,549 | cpu-small | 10 | 52% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 25 |
| captured (>90%) | 24 |

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
| 2026-09-30T02:18 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Test this release against the previous rel |
| 2026-09-30T02:18 | sn15 | RELEASE | sn15 released v2.0.39: Translate live Chutes model IDs on OpenRouter r |
| 2026-09-30T02:18 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Record foreground waits for prefetched ch |
| 2026-09-30T02:18 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: feat(snp): emit the validator policy entr |
| 2026-09-29T23:14 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Bind evaluator publications to their wind |
| 2026-09-29T19:33 | sn1 | RELEASE | sn1 released v4.4.11 |
| 2026-09-29T19:33 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Merge pull request #10 from hone-subnet-or |
| 2026-09-29T19:33 | sn5 | README_TASK_DIFF | sn5 README task/scoring sections changed |
| 2026-09-29T19:33 | sn15 | RELEASE | sn15 released v2.0.38: fix(agent): retry a 200 inference response whos |
| 2026-09-29T19:33 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.799 - miners can earn again |
| 2026-09-29T19:33 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Separate website from the public subnet a |
| 2026-09-29T19:33 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: pillar scoring updates around market-rela |
| 2026-09-29T19:33 | sn46 | BURN_DROP | sn46 burn fell 1.000 -> 0.726 - miners can earn again |
| 2026-09-29T19:33 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: docs(corpus): ledger v2 migration, verify |
| 2026-09-29T19:33 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: cli: export the validator's #256 policy f |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

