# Subnet watch — dashboard

_snapshot 2026-09-26T18:33:48Z · block 9153757 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 72.6 | 632 | 2,531 | cpu-small | 5 | 52% |
| 2 | sn1 Apex | 71.4 | 1,140 | 1,168 | rtx4090* | 4 | 54% |
| 3 | sn38 ChronoLLM | 70.7 | 368 | 3,232 | cpu-small | 10 | 52% |
| 4 | sn56 Gradients | 69.6 | 649 | 3,371 | rtx4090* | 8 | 40% |
| 5 | sn67 Harnyx | 69.5 | 10.65 | 1,367 | cpu-small | 121 | 37% |
| 6 | sn107 Minos | 69.2 | 382 | 31,510 | cpu-small | 20 | 79% |
| 7 | sn4 Targon | 68.6 | 16,698 | 30,202 | rtx4090* | 5 | 58% |
| 8 | sn15 ORO | 68.4 | 13.71 | 22,573 | cpu-small | 64 | 96% |
| 9 | sn124 Swarm | 67.3 | 345 | 995 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 67.2 | 337 | 3,013 | rtx4090* | 5 | 70% |
| 11 | sn96 Verathos | 66.8 | 16.09 | 270 | rtx4090 | 77 | 30% |
| 12 | sn14 Cacheon | 66.6 | 269 | 2,607 | rtx4090* | 14 | 31% |
| 13 | sn3 Teutonic | 64.9 | 5,705 | 5,705 = | rtx4090* | 5 | 20% |
| 14 | sn62 Ridges | 64.1 | 126 | 1,302 | rtx4090* | 25 | 13% |
| 15 | sn26 Perturb | 62.9 | 91.89 | 141 | rtx3060 | 5 | 90% |
| 16 | sn23 Trishool | 62.3 | 1,018 | 1,018 = | cpu-small | 2 | 80% |
| 17 | sn28 SayGM | 62.3 | 76.66 | 1,122 | rtx4090* | 65 | 15% |
| 18 | sn100 Cortex | 61 | 49.33 | 2,323 | rtx4090* | 18 | 65% |
| 19 | sn51 lium.io | 59 | 38.62 | 2,962 | rtx4090* | 69 | 77% |
| 20 | sn74 Gittensor | 58.3 | 25.36 | 305 | rtx4090* | 19 | 62% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-26T18:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected manifest to evidence quali |
| 2026-09-26T18:34 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #281 from reliquadotai |
| 2026-09-26T15:04 | sn7 | RELEASE | sn7 released release-20260926-135859 |
| 2026-09-26T15:04 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Hide alpha price flags from alw miner quot |
| 2026-09-26T15:04 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Show potential winners and link scoring b |
| 2026-09-26T15:04 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: feat: burn all emission and stop querying |
| 2026-09-26T15:04 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: docs(corpus): the task has no seats; audi |
| 2026-09-26T11:22 | sn25 | README_TASK_DIFF | sn25 README task/scoring sections changed |
| 2026-09-26T11:22 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected verifier manifest to alias |
| 2026-09-26T11:22 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: wvk 25 scoring bundle STAGED (all knobs  |
| 2026-09-26T06:07 | sn62 | RELEASE | sn62 released v0.3.7 |
| 2026-09-26T06:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow focused validation of saved Arena o |
| 2026-09-25T22:43 | sn1 | RELEASE | sn1 released v4.4.10 |
| 2026-09-25T19:26 | sn15 | RELEASE | sn15 released v2.0.31: fix(proxy): re-resolve Backend host for allowli |
| 2026-09-25T19:26 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: refactor(validator): simplify session cal |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

