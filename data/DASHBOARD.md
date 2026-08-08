# Subnet watch — dashboard

_snapshot 2026-08-08T11:15:56Z · block 8799258 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

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
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 38 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.7 | 128 | 34,113 | cpu-small | 19 | 90% |
| 2 | sn76 Phylax | 76.2 | 60.17 | 183 | cpu-small | 10 | 31% |
| 3 | sn67 Harnyx | 71.2 | 17.01 | 740 | cpu-small | 141 | 19% |
| 4 | sn91 cascade | 70.1 | 769 | 2,635 | rtx4090* | 5 | 48% |
| 5 | sn1 Apex | 69.6 | 666 | 1,539 | rtx4090* | 4 | 44% |
| 6 | sn62 Ridges | 69 | 553 | 2,002 | rtx4090* | 7 | 35% |
| 7 | sn41 Almanac | 68.3 | 8.76 | 26.85 | cpu-small | 69 | 76% |
| 8 | sn26 Perturb | 68.2 | 21.46 | 40.34 | rtx3060 | 11 | 50% |
| 9 | sn96 Verathos | 67.9 | 20.06 | 259 | rtx4090 | 69 | 42% |
| 10 | sn15 ORO | 67.3 | 9.02 | 10,632 | cpu-small | 68 | 94% |
| 11 | sn100 BASE | 67.2 | 319 | 1,956 | rtx4090* | 5 | 60% |
| 12 | sn38 ChronoLLM | 65.7 | 216 | 3,627 | rtx4090* | 10 | 52% |
| 13 | sn124 Swarm | 65.7 | 211 | 642 | rtx4090* | 23 | 11% |
| 14 | sn21 AdTAO | 65.6 | 4.84 | 22.30 | cpu-small | 142 | 45% |
| 15 | sn80 OpenRoboto | 63.3 | 98.88 | 367 | rtx4090* | 4 | 91% |
| 16 | sn61 RedTeam | 62.1 | 69.47 | 190 | rtx4090* | 36 | 6% |
| 17 | sn28 gm | 60.5 | 44.57 | 2,072 | rtx4090* | 19 | 29% |
| 18 | sn102 ConnitoAI | 58.8 | 916 | 1,775 | rtx4090* | 6 | 34% |
| 19 | sn51 lium.io | 58.5 | 30.70 | 2,840 | rtx4090* | 46 | 67% |
| 20 | sn85 Vidaio | 57 | 531 | 534 | rtx4090* | 10 | 16% |

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
| dominated (60–90%) | 21 |
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

