# Subnet watch — dashboard

_snapshot 2026-08-24T21:14:32Z · block 8917441 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.7 | 5,104 | 5,104 = | cpu-small | 1 | 100% |
| 2 | sn76 Phylax | 79.4 | 136 | 203 | cpu-small | 13 | 20% |
| 3 | sn3 Teutonic | 76 | 4,433 | 4,433 = | rtx4090* | 5 | 20% |
| 4 | sn60 Bitsec.ai | 76 | 1,718 | 1,718 = | cpu-small | 2 | 50% |
| 5 | sn38 ChronoLLM | 72.6 | 631 | 3,700 | cpu-small | 6 | 53% |
| 6 | sn62 Ridges | 72.4 | 1,535 | 3,136 | rtx4090* | 6 | 39% |
| 7 | sn15 ORO | 71.8 | 26.95 | 46.36 | cpu-small | 81 | 93% |
| 8 | sn67 Harnyx | 71.8 | 19.41 | 167 | cpu-small | 179 | 4% |
| 9 | sn102 ConnitoAI | 70.3 | 819 | 3,780 | rtx4090* | 5 | 52% |
| 10 | sn91 cascade | 68.9 | 541 | 1,456 | rtx4090* | 5 | 52% |
| 11 | sn1 Apex | 68.9 | 534 | 1,308 | rtx4090* | 5 | 52% |
| 12 | sn96 Verathos | 68.3 | 21.95 | 194 | rtx4090 | 92 | 40% |
| 13 | sn21 AdTAO | 67.9 | 8.43 | 1,005 | cpu-small | 16 | 37% |
| 14 | sn26 Perturb | 67.8 | 19.48 | 276 | rtx3060 | 10 | 70% |
| 15 | sn124 Swarm | 66.1 | 241 | 2,102 | rtx4090* | 22 | 24% |
| 16 | sn92 MicroTensor | 65.4 | 74.48 | 120 | cpu-small | 3 | 95% |
| 17 | sn107 Minos | 65.2 | 151 | 43,946 | cpu-small | 20 | 90% |
| 18 | sn85 Vidaio | 64.7 | 154 | 438 | rtx4090* | 13 | 42% |
| 19 | sn81 Reliquary | 64 | 122 | 342 | rtx4090* | 35 | 7% |
| 20 | sn108 Prometheon | 63.7 | 113 | 125 | rtx4090* | 9 | 66% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 18 |
| captured (>90%) | 25 |

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
| 2026-08-24T21:15 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Correct the validator setup path end to e |
| 2026-08-24T19:54 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Enforce ordered evaluations |
| 2026-08-24T19:10 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-24T19:10 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF board: read the live tail, so a miner  |
| 2026-08-24T18:16 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): retire the no-zero-for-mis |
| 2026-08-24T18:16 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: Merge pull request #44 from Bitsec-AI/fea |
| 2026-08-24T18:16 | sn92 | BURN_DROP | sn92 burn fell 1.000 -> 0.971 - miners can earn again |
| 2026-08-24T17:42 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Rename the office challenge family to cf |
| 2026-08-24T17:42 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |
| 2026-08-24T16:53 | sn11 | RELEASE | sn11 released v0.6.34 |
| 2026-08-24T16:53 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): leaderboard vs chain timin |
| 2026-08-24T16:05 | sn25 | RELEASE | sn25 released v2026.8.24-1027859650 |
| 2026-08-24T15:24 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Show provisional LCB during evaluations |
| 2026-08-24T15:24 | sn7 | RELEASE | sn7 released release-20260824-151246: Bump allways to 3.3.0 (#705) |
| 2026-08-24T15:24 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(miner): match fee-path test to the si |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

