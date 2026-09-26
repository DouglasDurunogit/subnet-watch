# Subnet watch — dashboard

_snapshot 2026-09-26T21:36:39Z · block 9154671 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 72.6 | 616 | 2,467 | cpu-small | 5 | 52% |
| 2 | sn102 ConnitoAI | 71.8 | 1,272 | 1,672 | rtx4090* | 6 | 28% |
| 3 | sn1 Apex | 71.4 | 1,124 | 1,234 | rtx4090* | 4 | 52% |
| 4 | sn38 ChronoLLM | 70.6 | 358 | 3,146 | cpu-small | 10 | 52% |
| 5 | sn56 Gradients | 69.5 | 634 | 3,294 | rtx4090* | 8 | 40% |
| 6 | sn67 Harnyx | 69.4 | 10.37 | 1,335 | cpu-small | 121 | 37% |
| 7 | sn107 Minos | 69.1 | 367 | 30,756 | cpu-small | 20 | 80% |
| 8 | sn15 ORO | 69 | 13.40 | 22,106 | cpu-small | 64 | 96% |
| 9 | sn4 Targon | 68.5 | 16,307 | 29,496 | rtx4090* | 5 | 58% |
| 10 | sn96 Verathos | 68.2 | 22.06 | 204 | rtx4090 | 77 | 30% |
| 11 | sn124 Swarm | 67.2 | 337 | 974 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 67.1 | 329 | 2,942 | rtx4090* | 5 | 70% |
| 13 | sn14 Cacheon | 66.8 | 288 | 2,499 | rtx4090* | 14 | 30% |
| 14 | sn3 Teutonic | 64.9 | 5,578 | 5,578 = | rtx4090* | 5 | 20% |
| 15 | sn62 Ridges | 64 | 122 | 1,268 | rtx4090* | 25 | 13% |
| 16 | sn28 SayGM | 62.4 | 78.84 | 879 | rtx4090* | 65 | 26% |
| 17 | sn23 Trishool | 62.2 | 974 | 974 = | cpu-small | 2 | 80% |
| 18 | sn100 Cortex | 60.2 | 38.55 | 260 | rtx4090* | 19 | 69% |
| 19 | sn26 Perturb | 59.9 | 38.39 | 42.18 | rtx3060 | 5 | 90% |
| 20 | sn74 Gittensor | 58.1 | 24.49 | 297 | rtx4090* | 19 | 63% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

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
| 2026-09-26T06:07 | sn62 | RELEASE | sn62 released v0.3.7 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

