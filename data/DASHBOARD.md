# Subnet watch — dashboard

_snapshot 2026-11-28T17:49:50Z · block 9607010 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 130

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 130 | everything on chain |
| Pays miners at all | 106 | `miner_burn` < 0.99 |
| Ranked | 106 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 75 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `█` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 6 | `██` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 24 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.2 | 216 | 216 = | cpu-small | 5 | 20% |
| 2 | sn35 TTedu | 78.8 | 3,916 | 3,916 = | cpu-small | 2 | 70% |
| 3 | sn116 Carbon | 73.6 | 2,188 | 2,188 = | rtx4090* | 3 | 38% |
| 4 | sn53 engy | 69 | 555 | 2,831 | rtx4090 | 8 | 49% |
| 5 | sn61 RedTeam | 68.4 | 456 | 895 | rtx4090* | 4 | 40% |
| 6 | sn39 Kokoah | 66.2 | 238 | 970 | rtx4090* | 8 | 48% |
| 7 | sn111 Claims | 65.7 | 204 | 734 | rtx4090* | 4 | 43% |
| 8 | sn67 Harnyx | 65.3 | 2.81 | 369 | cpu-small | 111 | 30% |
| 9 | sn124 Swarm | 64.9 | 171 | 1,110 | rtx4090* | 10 | 29% |
| 10 | sn56 Gradients | 62 | 452 | 2,344 | a100-80 | 9 | 33% |
| 11 | sn66 conjectures | 61.9 | 64.77 | 808 | rtx4090* | 4 | 81% |
| 12 | sn3 Teutonic | 60.7 | 1,618 | 3,244 | rtx4090* | 4 | 40% |
| 13 | sn28 SayGM | 60.1 | 40.48 | 660 | rtx4090* | 125 | 15% |
| 14 | sn127 Zils | 58.4 | 22.40 | 42.84 | rtx4090 | 6 | 88% |
| 15 | sn120 Affine | 57.1 | 19,186 | 19,186 = | rtx4090* | 1 | 100% |
| 16 | sn1 Apex | 56.6 | 475 | 507 | rtx4090* | 4 | 56% |
| 17 | sn38 ChronoLLM | 54.2 | 99.60 | 253 | cpu-small | 6 | 53% |
| 18 | sn107 Minos | 53.2 | 102 | 8,753 | cpu-small | 20 | 80% |
| 19 | sn46 Instant | 53.2 | 68.08 | 83.46 | cpu-small | 17 | 10% |
| 20 | sn99 Axonry | 52.3 | 2,552 | 2,552 = | rtx4090* | 2 | 50% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 20 |
| captured (>90%) | 28 |

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
| 2026-11-28T17:50 | sn25 | RELEASE | sn25 released v2026.11.28-1110821730 |
| 2026-11-28T17:50 | sn71 | BURN_DROP | sn71 burn fell 0.999 -> 0.959 - miners can earn again |
| 2026-11-28T17:50 | sn91 | BURN_DROP | sn91 burn fell 1.000 -> 0.950 - miners can earn again |
| 2026-11-28T17:50 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(marketcast): the MarketCast pod runs  |
| 2026-11-28T17:50 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Model merge_after_confirm in miner-facin |
| 2026-11-28T17:50 | sn129 | SCORING_COMMIT | sn129 commit touches scoring: Pin validator build 84 and give the one  |
| 2026-11-28T09:29 | sn25 | RELEASE | sn25 released v2026.11.27-1110314090 |
| 2026-11-28T09:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/pkg-managed-update-1128: a pac |
| 2026-11-28T09:29 | sn35 | BURN_DROP | sn35 burn fell 1.000 -> 0.700 - miners can earn again |
| 2026-11-28T09:29 | sn35 | SCORING_COMMIT | sn35 commit touches scoring: The validator guide says how to publish t |
| 2026-11-28T09:29 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: docs: record the runtime 497 serving and  |
| 2026-11-28T09:29 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-11-28T09:29 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Incoming change: image eval update and ha |
| 2026-11-28T09:29 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: docs: update the documentation of ada cha |
| 2026-11-28T09:29 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify registered programs end to end and |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

