# Subnet watch — dashboard

_snapshot 2026-09-26T23:56:13Z · block 9155369 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

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
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 72.7 | 635 | 2,543 | cpu-small | 5 | 52% |
| 2 | sn1 Apex | 71.4 | 1,118 | 1,228 | rtx4090* | 4 | 53% |
| 3 | sn56 Gradients | 71.3 | 1,089 | 6,194 | rtx4090* | 8 | 40% |
| 4 | sn38 ChronoLLM | 70.7 | 372 | 3,271 | cpu-small | 10 | 52% |
| 5 | sn102 ConnitoAI | 70.1 | 760 | 1,737 | rtx4090* | 6 | 29% |
| 6 | sn67 Harnyx | 69.4 | 10.45 | 1,344 | cpu-small | 124 | 37% |
| 7 | sn107 Minos | 69 | 360 | 31,193 | cpu-small | 20 | 80% |
| 8 | sn15 ORO | 69 | 13.50 | 22,258 | cpu-small | 64 | 96% |
| 9 | sn4 Targon | 68.5 | 16,409 | 29,680 | rtx4090* | 5 | 58% |
| 10 | sn96 Verathos | 67.5 | 19.07 | 250 | rtx4090 | 77 | 33% |
| 11 | sn124 Swarm | 67.2 | 336 | 988 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 67.2 | 335 | 2,993 | rtx4090* | 5 | 70% |
| 13 | sn3 Teutonic | 64.9 | 5,610 | 5,610 = | rtx4090* | 5 | 20% |
| 14 | sn14 Cacheon | 64.4 | 140 | 2,515 | rtx4090* | 14 | 30% |
| 15 | sn62 Ridges | 64 | 123 | 1,275 | rtx4090* | 25 | 13% |
| 16 | sn23 Trishool | 62.2 | 982 | 982 = | cpu-small | 2 | 80% |
| 17 | sn28 SayGM | 61.7 | 64.44 | 840 | rtx4090* | 66 | 32% |
| 18 | sn100 Cortex | 60.1 | 37.62 | 254 | rtx4090* | 19 | 70% |
| 19 | sn26 Perturb | 59.9 | 38.80 | 42.63 | rtx3060 | 5 | 90% |
| 20 | sn74 Gittensor | 58.2 | 24.86 | 298 | rtx4090* | 19 | 63% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 23 |
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
| 2026-09-26T23:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified homepage navigation source |
| 2026-09-26T21:37 | sn15 | RELEASE | sn15 released v2.0.32: fix(validator): save downloaded agent source as |
| 2026-09-26T21:37 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): save downloaded agent sou |
| 2026-09-26T21:37 | sn25 | RELEASE | sn25 released v2026.9.26-1056505490 |
| 2026-09-26T21:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse verified investigator source for at |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

