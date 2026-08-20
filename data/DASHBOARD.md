# Subnet watch — dashboard

_snapshot 2026-08-20T23:49:36Z · block 8889417 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.1 | 75.82 | 127 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.2 | 21.77 | 289 | cpu-small | 172 | 8% |
| 3 | sn23 Trishool | 72 | 526 | 526 = | cpu-small | 2 | 80% |
| 4 | sn15 ORO | 70.3 | 20.16 | 19,673 | cpu-small | 81 | 92% |
| 5 | sn56 Gradients | 69.7 | 683 | 1,044 | rtx4090* | 5 | 72% |
| 6 | sn91 cascade | 69.4 | 621 | 2,508 | rtx4090* | 5 | 52% |
| 7 | sn1 Apex | 68.2 | 428 | 1,214 | rtx4090* | 5 | 53% |
| 8 | sn38 ChronoLLM | 67.6 | 154 | 3,268 | cpu-small | 10 | 52% |
| 9 | sn11 TrajectoryRL | 67.4 | 4,535 | 4,535 = | cpu-small | 1 | 100% |
| 10 | sn96 Verathos | 67.4 | 17.55 | 367 | rtx4090 | 92 | 40% |
| 11 | sn26 Perturb | 67.4 | 17.44 | 251 | rtx3060 | 10 | 70% |
| 12 | sn107 Minos | 64.4 | 122 | 37,629 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 64.3 | 135 | 1,491 | rtx4090* | 13 | 42% |
| 14 | sn108 Prometheon | 63.9 | 122 | 179 | rtx4090* | 7 | 66% |
| 15 | sn51 lium.io | 61.9 | 73.19 | 1,261 | rtx4090* | 46 | 82% |
| 16 | sn55 NIOME | 61.9 | 64.63 | 538 | rtx4090* | 11 | 29% |
| 17 | sn60 Bitsec.ai | 61.3 | 739 | 1,035 | cpu-small | 3 | 50% |
| 18 | sn81 Reliquary | 60.8 | 47.01 | 192 | rtx4090* | 51 | 5% |
| 19 | sn28 gm | 60.7 | 47.22 | 1,417 | rtx4090* | 52 | 13% |
| 20 | sn53 engy | 60.1 | 37.52 | 248 | rtx4090 | 144 | 63% |

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
| dominated (60–90%) | 19 |
| captured (>90%) | 27 |

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
| 2026-08-20T23:08 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: fix: restore validator config parsing (#4 |
| 2026-08-20T23:08 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #203 from TensorLink-A |
| 2026-08-20T22:40 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Drop the task generator in favour of uplo |
| 2026-08-20T21:53 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: tune: double generator challenge frequenc |
| 2026-08-20T21:13 | sn13 | RELEASE | sn13 released Release v1.18.71 |
| 2026-08-20T21:13 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: fix(s3): stop charging miners for passing |
| 2026-08-20T21:13 | sn25 | RELEASE | sn25 released v2026.8.20-1024590520 |
| 2026-08-20T21:13 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Fix miner Windows arm64 cross-build |
| 2026-08-20T20:41 | sn25 | RELEASE | sn25 released v2026.8.20-1024555910 |
| 2026-08-20T19:55 | sn18 | RELEASE | sn18 released Release 2.1.2 |
| 2026-08-20T18:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair release verifier test isolation |
| 2026-08-20T18:15 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: apply owner-hosted miner integrity ve |
| 2026-08-20T18:15 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.611 - miners can earn again |
| 2026-08-20T17:41 | sn25 | README_TASK_DIFF | sn25 README task/scoring sections changed |
| 2026-08-20T17:41 | sn33 | SCORING_COMMIT | sn33 commit touches scoring: Merge pull request #136 from afterpartyai |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

