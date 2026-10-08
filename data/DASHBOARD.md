# Subnet watch — dashboard

_snapshot 2026-10-08T01:21:26Z · block 9234994 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 70.9 | 379 | 1,013 | cpu-small | 5 | 52% |
| 2 | sn38 ChronoLLM | 69.9 | 292 | 1,984 | cpu-small | 9 | 52% |
| 3 | sn46 Instant | 69.7 | 262 | 321 | cpu-small | 7 | 46% |
| 4 | sn1 Apex | 69 | 557 | 986 | rtx4090* | 4 | 70% |
| 5 | sn80 OpenRoboto | 68.9 | 535 | 2,092 | rtx4090* | 7 | 35% |
| 6 | sn67 Harnyx | 68.9 | 9.05 | 1,014 | cpu-small | 137 | 34% |
| 7 | sn15 ORO | 67.7 | 9.10 | 20,048 | cpu-small | 63 | 97% |
| 8 | sn26 Perturb | 67.6 | 362 | 401 | rtx3060 | 4 | 60% |
| 9 | sn4 Targon | 67 | 10,560 | 31,128 | rtx4090* | 5 | 70% |
| 10 | sn62 Ridges | 63.8 | 117 | 1,428 | rtx4090* | 34 | 17% |
| 11 | sn120 Affine | 63.3 | 166 | 269 | rtx4090* | 231 | 1% |
| 12 | sn61 RedTeam | 62.6 | 84.73 | 121 | rtx4090* | 130 | 1% |
| 13 | sn65 True Performance | 62.4 | 81.14 | 171 | rtx4090* | 6 | 75% |
| 14 | sn28 SayGM | 60.7 | 48.25 | 2,757 | rtx4090* | 73 | 13% |
| 15 | sn53 engy | 60.1 | 1,333 | 2,556 | rtx4090 | 18 | 17% |
| 16 | sn14 Cacheon | 59.9 | 35.70 | 2,671 | rtx4090* | 7 | 54% |
| 17 | sn23 Trishool | 59.7 | 462 | 462 = | cpu-small | 3 | 80% |
| 18 | sn41 Almanac | 58.9 | 27.50 | 121 | cpu-small | 139 | 2% |
| 19 | sn102 ConnitoAI | 58.4 | 803 | 1,399 | rtx4090* | 6 | 29% |
| 20 | sn74 Gittensor | 58.4 | 25.66 | 158 | rtx4090* | 21 | 50% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 26 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-08T01:21 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Assert the owner-validator's root seat ke |
| 2026-10-08T01:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #266: support verified Finney ru |
| 2026-10-08T01:21 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Restore original C5 progression and prese |
| 2026-10-08T01:21 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #782 from carbonphysi |
| 2026-10-08T01:21 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Use signed manifest quotas for miner-bou |
| 2026-10-07T21:28 | sn15 | RELEASE | sn15 released v2.3.0 |
| 2026-10-07T21:28 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge the sole validator's activation-pen |
| 2026-10-07T21:28 | sn50 | RELEASE | sn50 released v1.14.0 |
| 2026-10-07T21:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - validator: encrypted volume an |
| 2026-10-07T21:28 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: help miners to sign message |
| 2026-10-07T21:28 | sn54 | README_TASK_DIFF | sn54 README task/scoring sections changed |
| 2026-10-07T21:28 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: tasks: an unusable identity home is an id |
| 2026-10-07T21:28 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-10-07T21:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #265: refresh protected verifier |
| 2026-10-07T21:28 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Fix pinned operator generation task admis |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

