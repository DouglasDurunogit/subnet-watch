# Subnet watch — dashboard

_snapshot 2026-08-08T10:47:13Z · block 8799115 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 9 | `█████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 79 | 140 | 33,891 | cpu-small | 20 | 89% |
| 2 | sn76 Phylax | 76.2 | 60.09 | 186 | cpu-small | 10 | 31% |
| 3 | sn67 Harnyx | 71.2 | 17.02 | 740 | cpu-small | 140 | 19% |
| 4 | sn91 cascade | 70.1 | 776 | 2,655 | rtx4090* | 5 | 48% |
| 5 | sn1 Apex | 69.7 | 669 | 1,545 | rtx4090* | 4 | 43% |
| 6 | sn62 Ridges | 69.1 | 559 | 2,020 | rtx4090* | 7 | 35% |
| 7 | sn26 Perturb | 68.2 | 21.52 | 40.38 | rtx3060 | 11 | 50% |
| 8 | sn41 Almanac | 68.2 | 8.74 | 26.89 | cpu-small | 69 | 76% |
| 9 | sn96 Verathos | 68.1 | 20.51 | 252 | rtx4090 | 70 | 42% |
| 10 | sn100 BASE | 67.2 | 322 | 1,971 | rtx4090* | 5 | 60% |
| 11 | sn15 ORO | 67.2 | 9.03 | 10,643 | cpu-small | 68 | 94% |
| 12 | sn38 ChronoLLM | 65.7 | 215 | 3,606 | rtx4090* | 10 | 52% |
| 13 | sn124 Swarm | 65.7 | 211 | 643 | rtx4090* | 23 | 11% |
| 14 | sn21 AdTAO | 65.3 | 4.84 | 22.32 | cpu-small | 142 | 45% |
| 15 | sn80 OpenRoboto | 63.4 | 103 | 380 | rtx4090* | 4 | 91% |
| 16 | sn61 RedTeam | 62.1 | 69.77 | 190 | rtx4090* | 36 | 6% |
| 17 | sn28 gm | 61.6 | 61.03 | 2,209 | rtx4090* | 18 | 30% |
| 18 | sn51 lium.io | 57.8 | 26.17 | 2,837 | rtx4090* | 46 | 66% |
| 19 | sn102 ConnitoAI | 57.3 | 578 | 1,430 | rtx4090* | 7 | 27% |
| 20 | sn56 Gradients | 56.5 | 457 | 964 | rtx4090* | 7 | 70% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 22 |
| captured (>90%) | 25 |

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
| 2026-08-08T09:51 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Add miner self-test endpoint and dynamic  |
| 2026-08-08T08:06 | sn100 | RELEASE | sn100 released v3.3.10: Prism similarity precheck + stuck-sweep fix |
| 2026-08-08T07:12 | sn100 | RELEASE | sn100 released v3.3.9: fix(prism): stuck-sweep grace 10h + harness log |
| 2026-08-08T05:08 | sn80 | SCORING_COMMIT | sn80 commit touches scoring: protocol+docs: champion margin 0.01, unif |
| 2026-08-08T05:08 | sn100 | RELEASE | sn100 released v3.3.8 — Design one-prompt / one-attempt / admin reject |
| 2026-08-07T23:45 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(validator): note proxy requires vali |
| 2026-08-07T22:54 | sn61 | RELEASE | sn61 released 4.9.1 |
| 2026-08-07T22:54 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update bot virus challenge dependen |
| 2026-08-07T21:11 | sn28 | RELEASE | sn28 released v0.4.1 |
| 2026-08-07T20:24 | sn1 | RELEASE | sn1 released v4.2.21 |
| 2026-08-07T20:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Fix A10 GPU model normalization in valida |
| 2026-08-07T19:28 | sn28 | RELEASE | sn28 released v0.4.0 |
| 2026-08-07T19:28 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: removed Chutes for miner submission |
| 2026-08-07T19:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Authorize isolated autoresearch validatio |
| 2026-08-07T18:10 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: refactor(scoring): one behavioural detect |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

