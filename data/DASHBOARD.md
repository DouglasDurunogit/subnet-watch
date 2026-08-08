# Subnet watch — dashboard

_snapshot 2026-08-08T21:55:29Z · block 8802456 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 11 | `██████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.6 | 4,973 | 4,973 = | cpu-small | 1 | 100% |
| 2 | sn107 Minos | 78.2 | 116 | 34,921 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 76.6 | 65.59 | 198 | cpu-small | 10 | 33% |
| 4 | sn60 Bitsec.ai | 74.9 | 1,217 | 1,217 = | cpu-small | 2 | 50% |
| 5 | sn67 Harnyx | 71.3 | 17.13 | 744 | cpu-small | 142 | 19% |
| 6 | sn91 cascade | 70.2 | 787 | 2,695 | rtx4090* | 5 | 48% |
| 7 | sn1 Apex | 69.5 | 639 | 1,585 | rtx4090* | 4 | 46% |
| 8 | sn62 Ridges | 69.1 | 559 | 2,023 | rtx4090* | 7 | 35% |
| 9 | sn96 Verathos | 68.3 | 21.83 | 170 | rtx4090 | 72 | 42% |
| 10 | sn26 Perturb | 68.3 | 21.75 | 40.80 | rtx3060 | 11 | 50% |
| 11 | sn41 Almanac | 68.3 | 8.81 | 44.89 | cpu-small | 66 | 76% |
| 12 | sn15 ORO | 67.6 | 9.19 | 19.36 | cpu-small | 70 | 94% |
| 13 | sn21 AdTAO | 65.6 | 4.82 | 22.23 | cpu-small | 142 | 45% |
| 14 | sn38 ChronoLLM | 65.5 | 208 | 3,499 | rtx4090* | 10 | 52% |
| 15 | sn80 OpenRoboto | 63.6 | 110 | 406 | rtx4090* | 4 | 91% |
| 16 | sn61 RedTeam | 61.9 | 64.92 | 188 | rtx4090* | 42 | 6% |
| 17 | sn28 gm | 61.4 | 57.86 | 3,793 | rtx4090* | 24 | 41% |
| 18 | sn51 lium.io | 59.3 | 37.59 | 2,963 | rtx4090* | 47 | 67% |
| 19 | sn85 Vidaio | 57 | 535 | 574 | rtx4090* | 10 | 17% |
| 20 | sn56 Gradients | 56.5 | 463 | 976 | rtx4090* | 7 | 70% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 19 |
| captured (>90%) | 27 |

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
| 2026-08-08T14:48 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix: unblock cross-build ccache hits, mou |
| 2026-08-08T14:48 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: separate weekly-era scoring from th |
| 2026-08-08T13:09 | sn100 | RELEASE | sn100 released v3.3.11: Site arena UID + sealed weight enrichment |
| 2026-08-08T09:51 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Add miner self-test endpoint and dynamic  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

