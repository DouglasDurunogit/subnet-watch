# Subnet watch — dashboard

_snapshot 2026-11-28T09:29:23Z · block 9604508 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 130

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 130 | everything on chain |
| Pays miners at all | 105 | `miner_burn` < 0.99 |
| Ranked | 105 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 16 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 75 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `█` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 25 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 80.6 | 183 | 183 = | cpu-small | 5 | 20% |
| 2 | sn35 TTedu | 78.7 | 3,825 | 3,825 = | cpu-small | 2 | 70% |
| 3 | sn116 Carbon | 73.7 | 2,258 | 2,258 = | rtx4090* | 3 | 38% |
| 4 | sn53 engy | 71.8 | 1,265 | 2,994 | rtx4090 | 8 | 49% |
| 5 | sn111 Claims | 65.8 | 209 | 753 | rtx4090* | 4 | 43% |
| 6 | sn39 Kokoah | 65.5 | 193 | 793 | rtx4090* | 8 | 48% |
| 7 | sn67 Harnyx | 65.4 | 2.91 | 379 | cpu-small | 111 | 30% |
| 8 | sn124 Swarm | 64.9 | 170 | 1,136 | rtx4090* | 10 | 29% |
| 9 | sn56 Gradients | 62 | 462 | 2,398 | a100-80 | 9 | 33% |
| 10 | sn66 conjectures | 61.9 | 65.80 | 816 | rtx4090* | 4 | 81% |
| 11 | sn3 Teutonic | 60.8 | 1,658 | 1,658 = | rtx4090* | 4 | 40% |
| 12 | sn28 SayGM | 60.1 | 40.52 | 749 | rtx4090* | 124 | 17% |
| 13 | sn127 Zils | 58.5 | 23.25 | 44.25 | rtx4090 | 6 | 88% |
| 14 | sn120 Affine | 57.2 | 19,568 | 19,568 = | rtx4090* | 1 | 100% |
| 15 | sn1 Apex | 56.7 | 492 | 537 | rtx4090* | 4 | 55% |
| 16 | sn38 ChronoLLM | 54.3 | 102 | 259 | cpu-small | 6 | 53% |
| 17 | sn113 Elo | 53.7 | 4,531 | 4,531 = | rtx4090* | 1 | 100% |
| 18 | sn107 Minos | 53.4 | 107 | 9,002 | cpu-small | 20 | 80% |
| 19 | sn46 Instant | 53.3 | 69.89 | 81.12 | cpu-small | 17 | 12% |
| 20 | sn99 Axonry | 52.6 | 2,817 | 2,817 = | rtx4090* | 2 | 50% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 20 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 12 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-28T09:29 | sn25 | RELEASE | sn25 released v2026.11.27-1110314090 |
| 2026-11-28T09:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/pkg-managed-update-1128: a pac |
| 2026-11-28T09:29 | sn35 | BURN_DROP | sn35 burn fell 1.000 -> 0.700 - miners can earn again |
| 2026-11-28T09:29 | sn35 | SCORING_COMMIT | sn35 commit touches scoring: The validator guide says how to publish t |
| 2026-11-28T09:29 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: docs: record the runtime 497 serving and  |
| 2026-11-28T09:29 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-11-28T09:29 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Incoming change: image eval update and ha |
| 2026-11-28T09:29 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: docs: update the documentation of ada cha |
| 2026-11-28T09:29 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify registered programs end to end and |
| 2026-11-28T09:29 | sn76 | BURN_DROP | sn76 burn fell 0.999 -> 0.950 - miners can earn again |
| 2026-11-28T09:29 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #601 from reliquadotai |
| 2026-11-28T09:29 | sn91 | RELEASE | sn91 released worker-v2.1.0-mkt-rc3 |
| 2026-11-28T09:29 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(lanes): miner-visible queue reasons  |
| 2026-11-28T09:29 | sn111 | RELEASE | sn111 released v2.1.0 |
| 2026-11-28T09:29 | sn117 | RELEASE | sn117 released everycli v1.3.5 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

