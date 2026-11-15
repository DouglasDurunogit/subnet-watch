# Subnet watch — dashboard

_snapshot 2026-11-15T23:56:30Z · block 9515270 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.7 | 243 | 243 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.7 | 2,225 | 2,225 = | rtx4090* | 4 | 40% |
| 3 | sn97 Ingot | 71.7 | 1,227 | 1,227 = | rtx4090* | 5 | 20% |
| 4 | sn14 Cacheon | 69.8 | 690 | 4,232 | rtx4090* | 3 | 82% |
| 5 | sn58 Attune | 68.9 | 542 | 872 | rtx4090* | 5 | 70% |
| 6 | sn56 Gradients | 68.8 | 523 | 3,992 | rtx4090* | 6 | 50% |
| 7 | sn41 Almanac | 68.1 | 8.35 | 130 | cpu-small | 155 | 2% |
| 8 | sn15 ORO | 66.6 | 6.27 | 12.44 | cpu-small | 68 | 95% |
| 9 | sn67 Harnyx | 65.5 | 3.16 | 256 | cpu-small | 194 | 18% |
| 10 | sn124 Swarm | 65.3 | 189 | 790 | rtx4090* | 10 | 31% |
| 11 | sn53 engy | 65 | 169 | 6,958 | rtx4090 | 23 | 40% |
| 12 | sn38 ChronoLLM | 63 | 45.22 | 312 | cpu-small | 9 | 52% |
| 13 | sn120 Affine | 61.9 | 2,323 | 2,323 = | rtx4090* | 10 | 10% |
| 14 | sn60 Bitsec.ai | 60.4 | 574 | 574 = | cpu-small | 3 | 50% |
| 15 | sn111 Claims | 60.3 | 40.60 | 163 | rtx4090* | 4 | 88% |
| 16 | sn62 Ridges | 59.6 | 32.85 | 611 | rtx4090* | 44 | 15% |
| 17 | sn117 everyframe.studi | 59.1 | 28.75 | 371 | rtx4090* | 33 | 17% |
| 18 | sn4 Targon | 57.7 | 9,453 | 20,274 | rtx4090* | 5 | 62% |
| 19 | sn102 ConnitoAI | 57.5 | 619 | 620 | rtx4090* | 4 | 25% |
| 20 | sn5 Hone | 56.9 | 18.68 | 41.73 | rtx4090* | 243 | 1% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 29 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-15T23:57 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Merge pull request #161 from latent-to/cl |
| 2026-11-15T23:57 | sn25 | RELEASE | sn25 released v2026.11.15-1099862510 |
| 2026-11-15T23:57 | sn26 | BURN_DROP | sn26 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-15T23:57 | sn42 | RELEASE | sn42 released v0.6.16 |
| 2026-11-15T23:57 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: docs: the baseline was the setup of CADmi |
| 2026-11-15T23:57 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(subnet): enter Phase 1 with external |
| 2026-11-15T23:57 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-11-15T23:57 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Build jit: keep the shared level4 regist |
| 2026-11-15T19:53 | sn25 | RELEASE | sn25 released v2026.11.15-1099669220 |
| 2026-11-15T19:53 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Keep honest batch miners' leases: default |
| 2026-11-15T19:53 | sn106 | BURN_DROP | sn106 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-15T19:53 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Withdraw review fixes (kit): a withdrawn |
| 2026-11-15T14:11 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore: remove dead load_episode_artifact  |
| 2026-11-15T14:11 | sn25 | RELEASE | sn25 released v2026.11.15-1099387180 |
| 2026-11-15T14:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow measured baselines with capture gap |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

