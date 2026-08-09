# Subnet watch — dashboard

_snapshot 2026-08-09T03:59:37Z · block 8804277 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 52 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 11 | `██████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 40 | `██████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.6 | 126 | 35,442 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.7 | 68.27 | 206 | cpu-small | 10 | 33% |
| 3 | sn98 NeverPlayAlone | 76.2 | 1,818 | 1,818 = | cpu-small | 1 | 100% |
| 4 | sn60 Bitsec.ai | 75 | 1,264 | 1,264 = | cpu-small | 2 | 50% |
| 5 | sn67 Harnyx | 70.8 | 15.30 | 874 | cpu-small | 151 | 22% |
| 6 | sn100 BASE | 70.5 | 854 | 1,716 | rtx4090* | 3 | 50% |
| 7 | sn1 Apex | 70.3 | 814 | 1,678 | rtx4090* | 4 | 43% |
| 8 | sn91 cascade | 70.3 | 802 | 2,744 | rtx4090* | 5 | 48% |
| 9 | sn41 Almanac | 69.3 | 11.36 | 46.46 | cpu-small | 67 | 72% |
| 10 | sn96 Verathos | 68.9 | 25.23 | 262 | rtx4090 | 73 | 40% |
| 11 | sn26 Perturb | 68.4 | 22.23 | 42.68 | rtx3060 | 11 | 50% |
| 12 | sn62 Ridges | 68.3 | 449 | 2,084 | rtx4090* | 7 | 35% |
| 13 | sn15 ORO | 68 | 9.89 | 20.57 | cpu-small | 71 | 94% |
| 14 | sn28 gm | 67 | 301 | 3,903 | rtx4090* | 25 | 40% |
| 15 | sn38 ChronoLLM | 65.7 | 218 | 3,664 | rtx4090* | 10 | 52% |
| 16 | sn21 AdTAO | 65.7 | 5.05 | 23.16 | cpu-small | 142 | 45% |
| 17 | sn80 OpenRoboto | 64.2 | 131 | 481 | rtx4090* | 4 | 91% |
| 18 | sn61 RedTeam | 62.4 | 75.93 | 217 | rtx4090* | 42 | 6% |
| 19 | sn51 lium.io | 60.7 | 54.12 | 3,048 | rtx4090* | 47 | 67% |
| 20 | sn6 Numinous | 59.1 | 30.26 | 347 | cpu-small | 18 | 19% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 20 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-09T02:25 | sn6 | BURN_DROP | sn6 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-09T02:25 | sn61 | RELEASE | sn61 released 4.9.2 |
| 2026-08-09T02:25 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: refactor: update minimum acceptable score |
| 2026-08-09T02:25 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Document the directive as the source of e |
| 2026-08-08T21:55 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Document the real agent size limits and s |
| 2026-08-08T21:15 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: Merge pull request #101 from BaseIntelli |
| 2026-08-08T20:45 | sn55 | BURN_DROP | sn55 burn fell 1.000 -> 0.021 - miners can earn again |
| 2026-08-08T20:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry signed transient company scoring fa |
| 2026-08-08T20:45 | sn100 | RELEASE | sn100 released v3.3.13 — design screenshot egress proxy + gateway admi |
| 2026-08-08T19:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix evaluator test import isolation |
| 2026-08-08T19:53 | sn100 | RELEASE | sn100 released v3.3.12 |
| 2026-08-08T19:53 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(design): keep challenge-agentic unde |
| 2026-08-08T17:43 | sn96 | RELEASE | sn96 released v0.1.29 - Gleipnir Validator Reliability |
| 2026-08-08T17:43 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: isolate validator epoch control work |
| 2026-08-08T15:42 | sn93 | BURN_DROP | sn93 burn fell 0.993 -> 0.592 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

