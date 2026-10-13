# Subnet watch — dashboard

_snapshot 2026-10-13T08:31:13Z · block 9273138 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 26 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.2 | 295 | 25,100 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.9 | 3,207 | 3,207 = | rtx4090* | 5 | 40% |
| 3 | sn53 engy | 71.5 | 1,171 | 2,581 | rtx4090 | 18 | 17% |
| 4 | sn101 Tag101 | 70.4 | 14.19 | 15.70 | cpu-small | 242 | 1% |
| 5 | sn67 Harnyx | 69.9 | 11.91 | 693 | cpu-small | 133 | 25% |
| 6 | sn58 Attune | 68.1 | 425 | 858 | rtx4090* | 4 | 79% |
| 7 | sn79 MVTRX | 67.8 | 8.53 | 36.20 | cpu-small | 245 | 1% |
| 8 | sn4 Targon | 66.9 | 10,100 | 29,780 | rtx4090* | 5 | 70% |
| 9 | sn15 ORO | 66.8 | 7.07 | 18,765 | cpu-small | 56 | 98% |
| 10 | sn41 Almanac | 66.3 | 6.22 | 163 | cpu-small | 103 | 4% |
| 11 | sn62 Ridges | 64.1 | 128 | 1,288 | rtx4090* | 37 | 17% |
| 12 | sn120 Affine | 62.8 | 136 | 243 | rtx4090* | 251 | 1% |
| 13 | sn28 SayGM | 61.5 | 60.89 | 1,952 | rtx4090* | 73 | 32% |
| 14 | sn80 OpenRoboto | 59.6 | 1,162 | 3,958 | rtx4090* | 10 | 36% |
| 15 | sn23 Trishool | 59.2 | 399 | 399 = | cpu-small | 3 | 80% |
| 16 | sn46 Instant | 59.1 | 391 | 428 | cpu-small | 8 | 14% |
| 17 | sn91 cascade | 59 | 380 | 2,031 | cpu-small | 5 | 52% |
| 18 | sn111 Claims | 58.2 | 22.02 | 256 | rtx4090* | 6 | 90% |
| 19 | sn5 Hone | 57.8 | 35.02 | 35.65 | rtx4090* | 243 | 0% |
| 20 | sn1 Apex | 57.6 | 630 | 1,040 | rtx4090* | 4 | 59% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 29 |
| captured (>90%) | 23 |

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
| 2026-10-13T08:31 | sn25 | RELEASE | sn25 released v2026.10.13-1070793380 |
| 2026-10-13T08:31 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge the validator steering fixes deploy |
| 2026-10-13T08:31 | sn51 | RELEASE | sn51 released executor-v1.140 |
| 2026-10-13T08:31 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - Validator: install sshd withou |
| 2026-10-13T08:31 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-13T08:31 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #408 from leadpoet/fix |
| 2026-10-13T08:31 | sn117 | RELEASE | sn117 released everycli v0.3.9 |
| 2026-10-13T08:31 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-13T01:39 | sn28 | RELEASE | sn28 released v0.4.28 |
| 2026-10-13T01:39 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.28 ( |
| 2026-10-13T01:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Finish validated bounded evidence reviews |
| 2026-10-13T01:39 | sn74 | RELEASE | sn74 released release-20261012-224627 |
| 2026-10-13T01:39 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: chore(weights): burn all miner emissions  |
| 2026-10-13T01:39 | sn117 | RELEASE | sn117 released everycli v0.3.8 |
| 2026-10-12T19:47 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Optimize evaluator shard downloads with ca |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

