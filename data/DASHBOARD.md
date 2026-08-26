# Subnet watch — dashboard

_snapshot 2026-08-26T09:53:48Z · block 8928438 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80 | 162 | 364 | cpu-small | 13 | 20% |
| 2 | sn11 TrajectoryRL | 79.6 | 5,024 | 5,024 = | cpu-small | 1 | 100% |
| 3 | sn60 Bitsec.ai | 76.2 | 1,836 | 1,836 = | cpu-small | 2 | 50% |
| 4 | sn3 Teutonic | 75.5 | 3,851 | 3,851 = | rtx4090* | 5 | 20% |
| 5 | sn23 Trishool | 72.1 | 542 | 542 = | cpu-small | 2 | 80% |
| 6 | sn15 ORO | 70.7 | 22.23 | 42.43 | cpu-small | 94 | 92% |
| 7 | sn67 Harnyx | 70.4 | 14.34 | 255 | cpu-small | 137 | 7% |
| 8 | sn38 ChronoLLM | 70.2 | 319 | 806 | cpu-small | 6 | 53% |
| 9 | sn56 Gradients | 69.6 | 661 | 1,092 | rtx4090* | 6 | 73% |
| 10 | sn91 cascade | 68.9 | 537 | 1,445 | rtx4090* | 5 | 52% |
| 11 | sn26 Perturb | 68.1 | 20.90 | 398 | rtx3060 | 10 | 70% |
| 12 | sn124 Swarm | 66.7 | 286 | 861 | rtx4090* | 25 | 10% |
| 13 | sn1 Apex | 65.9 | 219 | 1,954 | rtx4090* | 4 | 55% |
| 14 | sn21 AdTAO | 65.1 | 4.54 | 590 | cpu-small | 16 | 45% |
| 15 | sn107 Minos | 64.6 | 127 | 41,258 | cpu-small | 19 | 90% |
| 16 | sn81 Reliquary | 63.7 | 113 | 278 | rtx4090* | 39 | 6% |
| 17 | sn121 sundae_bar | 63 | 1,233 | 1,233 = | cpu-small | 2 | 60% |
| 18 | sn28 gm | 62.7 | 84.73 | 2,464 | rtx4090* | 41 | 20% |
| 19 | sn108 Prometheon | 62.6 | 81.14 | 208 | rtx4090* | 9 | 29% |
| 20 | sn61 RedTeam | 60.9 | 48.04 | 292 | rtx4090* | 78 | 5% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 16 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-26T09:54 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(selection): retain serving miners an |
| 2026-08-26T09:54 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: feat(scoring): give the JS sandbox the A |
| 2026-08-26T08:58 | sn25 | RELEASE | sn25 released v2026.8.26-1029312040 |
| 2026-08-26T08:58 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #55 from score-technol |
| 2026-08-26T08:58 | sn61 | RELEASE | sn61 released 4.10.0 |
| 2026-08-26T08:58 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update bot virus challenge image ve |
| 2026-08-26T08:58 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(964): optimizeYield can be scored —  |
| 2026-08-26T07:56 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validation): make claim assessments  |
| 2026-08-26T05:48 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: fix: score title fights by complete topic |
| 2026-08-26T04:09 | sn25 | RELEASE | sn25 released v2026.8.25-1029146630 |
| 2026-08-26T01:55 | sn25 | RELEASE | sn25 released v2026.8.25-1029027010 |
| 2026-08-26T01:55 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): close submission ingress  |
| 2026-08-25T23:10 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Add unit tests for get_base_contestant to |
| 2026-08-25T23:10 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(scoring): plan.metadata is not alway |
| 2026-08-25T21:53 | sn28 | RELEASE | sn28 released v0.4.10 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

