# Subnet watch — dashboard

_snapshot 2026-08-08T19:07:28Z · block 8801616 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 9 | `█████` |
| ≥0.99 dead | 38 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.6 | 4,955 | 4,955 = | cpu-small | 1 | 100% |
| 2 | sn107 Minos | 78.3 | 116 | 34,136 | cpu-small | 20 | 89% |
| 3 | sn76 Phylax | 76.3 | 61.39 | 185 | cpu-small | 10 | 31% |
| 4 | sn67 Harnyx | 71.2 | 17.07 | 742 | cpu-small | 142 | 19% |
| 5 | sn91 cascade | 70.2 | 780 | 2,673 | rtx4090* | 5 | 48% |
| 6 | sn1 Apex | 69.5 | 645 | 1,596 | rtx4090* | 4 | 44% |
| 7 | sn62 Ridges | 69 | 555 | 2,007 | rtx4090* | 7 | 35% |
| 8 | sn26 Perturb | 68.3 | 21.56 | 40.35 | rtx3060 | 11 | 50% |
| 9 | sn41 Almanac | 68.3 | 8.78 | 27.00 | cpu-small | 69 | 76% |
| 10 | sn96 Verathos | 68.1 | 20.98 | 219 | rtx4090 | 65 | 45% |
| 11 | sn15 ORO | 67.1 | 9.10 | 19.18 | cpu-small | 70 | 94% |
| 12 | sn38 ChronoLLM | 65.5 | 205 | 3,456 | rtx4090* | 10 | 52% |
| 13 | sn21 AdTAO | 65.5 | 4.77 | 22.05 | cpu-small | 142 | 45% |
| 14 | sn80 OpenRoboto | 63.3 | 101 | 374 | rtx4090* | 4 | 91% |
| 15 | sn61 RedTeam | 61.5 | 57.91 | 176 | rtx4090* | 43 | 6% |
| 16 | sn28 gm | 60.2 | 40.33 | 3,466 | rtx4090* | 19 | 38% |
| 17 | sn51 lium.io | 58.7 | 31.91 | 2,727 | rtx4090* | 47 | 65% |
| 18 | sn56 Gradients | 56.5 | 460 | 969 | rtx4090* | 7 | 70% |
| 19 | sn85 Vidaio | 55.9 | 382 | 556 | rtx4090* | 10 | 20% |
| 20 | sn74 Gittensor | 55.2 | 10.39 | 235 | rtx4090* | 16 | 63% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 20 |
| captured (>90%) | 26 |

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
| 2026-08-08T17:43 | sn96 | RELEASE | sn96 released v0.1.29 - Gleipnir Validator Reliability |
| 2026-08-08T17:43 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: isolate validator epoch control work |
| 2026-08-08T15:42 | sn93 | BURN_DROP | sn93 burn fell 0.993 -> 0.592 - miners can earn again |
| 2026-08-08T14:48 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix: unblock cross-build ccache hits, mou |
| 2026-08-08T14:48 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: separate weekly-era scoring from th |
| 2026-08-08T13:09 | sn100 | RELEASE | sn100 released v3.3.11: Site arena UID + sealed weight enrichment |
| 2026-08-08T09:51 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Add miner self-test endpoint and dynamic  |
| 2026-08-08T08:06 | sn100 | RELEASE | sn100 released v3.3.10: Prism similarity precheck + stuck-sweep fix |
| 2026-08-08T07:12 | sn100 | RELEASE | sn100 released v3.3.9: fix(prism): stuck-sweep grace 10h + harness log |
| 2026-08-08T05:08 | sn80 | SCORING_COMMIT | sn80 commit touches scoring: protocol+docs: champion margin 0.01, unif |
| 2026-08-08T05:08 | sn100 | RELEASE | sn100 released v3.3.8 — Design one-prompt / one-attempt / admin reject |
| 2026-08-07T23:45 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(validator): note proxy requires vali |
| 2026-08-07T22:54 | sn61 | RELEASE | sn61 released 4.9.1 |
| 2026-08-07T22:54 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update bot virus challenge dependen |
| 2026-08-07T21:11 | sn28 | RELEASE | sn28 released v0.4.1 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

