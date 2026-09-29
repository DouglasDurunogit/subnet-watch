# Subnet watch — dashboard

_snapshot 2026-09-29T23:13:44Z · block 9176755 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 0 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **0** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn67 Harnyx | 50 | n/a | n/a | cpu-small | 129 | 38% |
| 2 | sn41 Almanac | 50 | n/a | n/a | cpu-small | 117 | 2% |
| 3 | sn21 AdTAO | 50 | n/a | n/a | cpu-small | 20 | 40% |
| 4 | sn23 Trishool | 50 | n/a | n/a | cpu-small | 2 | 80% |
| 5 | sn15 ORO | 50 | n/a | n/a | cpu-small | 77 | 95% |
| 6 | sn96 Verathos | 46.2 | n/a | n/a | rtx4090 | 74 | 30% |
| 7 | sn26 Perturb | 46.2 | n/a | n/a | rtx3060 | 5 | 91% |
| 8 | sn91 cascade | 42.5 | n/a | n/a | cpu-small | 5 | 52% |
| 9 | sn46 Instant | 42.5 | n/a | n/a | cpu-small | 3 | 71% |
| 10 | sn53 engy | 39.3 | n/a | n/a | rtx4090 | 66 | 26% |
| 11 | sn81 Reliquary | 39.3 | n/a | n/a | rtx4090* | 32 | 82% |
| 12 | sn100 Cortex | 39.3 | n/a | n/a | rtx4090* | 26 | 70% |
| 13 | sn14 Cacheon | 39.3 | n/a | n/a | rtx4090* | 15 | 29% |
| 14 | sn56 Gradients | 39.3 | n/a | n/a | rtx4090* | 9 | 39% |
| 15 | sn1 Apex | 39.3 | n/a | n/a | rtx4090* | 4 | 54% |
| 16 | sn9 iota | 39.3 | n/a | n/a | rtx4090* | 3 | 74% |
| 17 | sn71 Leadpoet | 39.3 | n/a | n/a | rtx4090* | 2 | 70% |
| 18 | sn45 AlphaRidge.ai | 39.3 | n/a | n/a | rtx4090* | 237 | 62% |
| 19 | sn88 Investing | 39.3 | n/a | n/a | rtx4090* | 60 | 44% |
| 20 | sn102 ConnitoAI | 39.3 | n/a | n/a | rtx4090* | 6 | 31% |

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
| concentrated (30–60%) | 23 |
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
| 2026-09-29T14:13 | sn15 | RELEASE | sn15 released v2.0.37: fix(proxy): sum inference counters across Proxy |
| 2026-09-29T14:13 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Merge pull request #57 from TrishoolAI/va |
| 2026-09-29T14:13 | sn46 | RELEASE | sn46 released v0.1.2 |
| 2026-09-29T14:13 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Burn whatever leaves the miners the summa |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

