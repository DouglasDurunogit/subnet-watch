# Subnet watch — dashboard

_snapshot 2026-09-26T15:03:51Z · block 9152707 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 72.8 | 655 | 2,622 | cpu-small | 5 | 52% |
| 2 | sn1 Apex | 71.6 | 1,178 | 1,207 | rtx4090* | 4 | 54% |
| 3 | sn38 ChronoLLM | 70.3 | 337 | 2,966 | cpu-small | 10 | 52% |
| 4 | sn56 Gradients | 69.5 | 646 | 3,401 | rtx4090* | 8 | 41% |
| 5 | sn67 Harnyx | 69.5 | 10.73 | 1,377 | cpu-small | 120 | 37% |
| 6 | sn107 Minos | 69.2 | 379 | 31,931 | cpu-small | 20 | 80% |
| 7 | sn15 ORO | 69.2 | 14.25 | 22,852 | cpu-small | 63 | 96% |
| 8 | sn4 Targon | 68.6 | 16,832 | 30,446 | rtx4090* | 5 | 58% |
| 9 | sn96 Verathos | 67.5 | 19.20 | 282 | rtx4090 | 74 | 30% |
| 10 | sn124 Swarm | 67.3 | 347 | 1,000 | rtx4090* | 25 | 11% |
| 11 | sn111 Claims | 67.2 | 340 | 3,042 | rtx4090* | 5 | 70% |
| 12 | sn3 Teutonic | 65 | 5,747 | 5,747 = | rtx4090* | 5 | 20% |
| 13 | sn62 Ridges | 63.4 | 104 | 1,412 | rtx4090* | 24 | 14% |
| 14 | sn28 SayGM | 63.3 | 102 | 1,078 | rtx4090* | 61 | 20% |
| 15 | sn14 Cacheon | 63 | 91.46 | 2,515 | rtx4090* | 13 | 29% |
| 16 | sn23 Trishool | 62.4 | 1,026 | 1,026 = | cpu-small | 2 | 80% |
| 17 | sn26 Perturb | 61.6 | 62.03 | 62.03 = | rtx3060 | 5 | 90% |
| 18 | sn100 Cortex | 60.2 | 38.57 | 260 | rtx4090* | 19 | 70% |
| 19 | sn102 ConnitoAI | 60.1 | 38.62 | 1,996 | rtx4090* | 8 | 33% |
| 20 | sn74 Gittensor | 59.1 | 32.28 | 307 | rtx4090* | 17 | 63% |

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
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
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
| 2026-09-25T19:26 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve terminal verified intent evidenc |
| 2026-09-25T19:26 | sn74 | RELEASE | sn74 released release-20260925-183535 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

