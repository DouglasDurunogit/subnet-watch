# Subnet watch — dashboard

_snapshot 2026-11-15T00:02:25Z · block 9508100 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.4 | 226 | 226 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.5 | 2,099 | 4,207 | rtx4090* | 4 | 40% |
| 3 | sn97 Ingot | 71.5 | 1,162 | 1,162 = | rtx4090* | 5 | 20% |
| 4 | sn56 Gradients | 69.9 | 715 | 3,773 | rtx4090* | 6 | 50% |
| 5 | sn58 Attune | 68.5 | 483 | 777 | rtx4090* | 5 | 70% |
| 6 | sn41 Almanac | 67.8 | 7.82 | 117 | cpu-small | 154 | 2% |
| 7 | sn67 Harnyx | 67.6 | 6.19 | 189 | cpu-small | 136 | 14% |
| 8 | sn15 ORO | 66 | 5.62 | 11.95 | cpu-small | 72 | 95% |
| 9 | sn124 Swarm | 65.1 | 179 | 750 | rtx4090* | 10 | 31% |
| 10 | sn53 engy | 64.5 | 145 | 6,037 | rtx4090 | 23 | 40% |
| 11 | sn38 ChronoLLM | 62.8 | 42.69 | 295 | cpu-small | 9 | 52% |
| 12 | sn120 Affine | 61.7 | 2,188 | 2,188 = | rtx4090* | 10 | 10% |
| 13 | sn111 Claims | 60 | 37.89 | 153 | rtx4090* | 4 | 88% |
| 14 | sn62 Ridges | 59.5 | 31.55 | 578 | rtx4090* | 44 | 15% |
| 15 | sn4 Targon | 57.5 | 8,782 | 18,834 | rtx4090* | 5 | 62% |
| 16 | sn5 Hone | 56.4 | 17.32 | 38.73 | rtx4090* | 243 | 1% |
| 17 | sn66 conjectures | 56.2 | 11.29 | 944 | rtx4090* | 7 | 80% |
| 18 | sn46 Instant | 55.9 | 148 | 175 | cpu-small | 9 | 29% |
| 19 | sn1 Apex | 54.8 | 276 | 615 | rtx4090* | 4 | 66% |
| 20 | sn107 Minos | 54.6 | 140 | 11,948 | cpu-small | 20 | 80% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 32 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-15T00:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1240 from leadpoet/fi |
| 2026-11-15T00:02 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Queue place: a resubmission of a stop-ca |
| 2026-11-14T20:09 | sn42 | RELEASE | sn42 released v0.6.15 |
| 2026-11-14T20:09 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: v0.6.15: the reference miner hands a fini |
| 2026-11-14T20:09 | sn116 | BURN_DROP | sn116 burn fell 1.000 -> 0.750 - miners can earn again |
| 2026-11-14T20:09 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Tests: a serve stop leaves a queued task |
| 2026-11-14T15:45 | sn25 | RELEASE | sn25 released v2026.11.14-1098667430 |
| 2026-11-14T15:45 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/validator-attempt-upload-lane-r |
| 2026-11-14T15:45 | sn42 | RELEASE | sn42 released v0.6.13 |
| 2026-11-14T15:45 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: tests: stub the agent CLI checks where th |
| 2026-11-14T15:45 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: forward reported cache write t |
| 2026-11-14T15:45 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Bind subnet API publicly and add task sub |
| 2026-11-14T15:45 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(miner): stop agentic children gracefu |
| 2026-11-14T15:45 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Alert the miner operator on a first misse |
| 2026-11-14T08:55 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge release/validator-1114-idle-fleet:  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

