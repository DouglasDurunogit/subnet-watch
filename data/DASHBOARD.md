# Subnet watch — dashboard

_snapshot 2026-08-09T07:15:16Z · block 8805255 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 87 | `miner_burn` < 0.99 |
| Ranked | 87 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 51 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 12 | `███████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 41 | `███████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.5 | 4,878 | 4,878 = | cpu-small | 1 | 100% |
| 2 | sn107 Minos | 78.4 | 119 | 35,353 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 76.7 | 67.27 | 203 | cpu-small | 10 | 33% |
| 4 | sn60 Bitsec.ai | 74.9 | 1,252 | 1,252 = | cpu-small | 2 | 50% |
| 5 | sn67 Harnyx | 70.7 | 15.12 | 864 | cpu-small | 155 | 22% |
| 6 | sn1 Apex | 70.2 | 795 | 1,639 | rtx4090* | 4 | 44% |
| 7 | sn91 cascade | 70.2 | 780 | 2,668 | rtx4090* | 5 | 48% |
| 8 | sn100 BASE | 69.9 | 721 | 1,516 | rtx4090* | 4 | 45% |
| 9 | sn41 Almanac | 69.4 | 11.53 | 30.36 | cpu-small | 67 | 72% |
| 10 | sn26 Perturb | 68.4 | 22.46 | 42.23 | rtx3060 | 11 | 50% |
| 11 | sn96 Verathos | 68.4 | 22.34 | 283 | rtx4090 | 75 | 41% |
| 12 | sn62 Ridges | 68.3 | 439 | 2,037 | rtx4090* | 7 | 35% |
| 13 | sn21 AdTAO | 65.7 | 4.98 | 22.89 | cpu-small | 142 | 45% |
| 14 | sn38 ChronoLLM | 65.6 | 214 | 3,598 | rtx4090* | 10 | 52% |
| 15 | sn15 ORO | 64.6 | 5.81 | 17.01 | cpu-small | 71 | 96% |
| 16 | sn80 OpenRoboto | 64.5 | 142 | 518 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 62.4 | 75.95 | 217 | rtx4090* | 42 | 6% |
| 18 | sn51 lium.io | 59.3 | 37.34 | 2,909 | rtx4090* | 48 | 69% |
| 19 | sn6 Numinous | 59.1 | 29.96 | 344 | cpu-small | 18 | 19% |
| 20 | sn28 gm | 58.3 | 23.56 | 2,720 | rtx4090* | 25 | 58% |

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
| dominated (60–90%) | 19 |
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
| 2026-08-09T05:16 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Move inference cost off the validator and |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

