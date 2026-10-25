# Subnet watch — dashboard

_snapshot 2026-10-25T05:22:42Z · block 9358514 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,120 | 4,248 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,812 | 1,812 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 71.2 | 1,054 | 5,709 | rtx4090* | 6 | 51% |
| 4 | sn67 Harnyx | 70.4 | 13.72 | 143 | cpu-small | 124 | 7% |
| 5 | sn46 Instant | 69.2 | 226 | 263 | cpu-small | 6 | 42% |
| 6 | sn1 Apex | 68.2 | 438 | 886 | rtx4090* | 5 | 54% |
| 7 | sn82 Noah | 67.8 | 600 | 606 | rtx4090* | 63 | 2% |
| 8 | sn41 Almanac | 67.2 | 7.36 | 132 | cpu-small | 167 | 4% |
| 9 | sn53 engy | 66.9 | 292 | 2,395 | rtx4090 | 36 | 11% |
| 10 | sn107 Minos | 66.9 | 218 | 18,536 | cpu-small | 20 | 80% |
| 11 | sn125 Refinery | 66 | 227 | 864 | rtx4090* | 4 | 50% |
| 12 | sn120 Affine | 65.1 | 187 | 1,168 | rtx4090* | 119 | 4% |
| 13 | sn15 ORO | 63.7 | 4.55 | 14,544 | cpu-small | 48 | 98% |
| 14 | sn66 conjectures | 63.3 | 101 | 210 | rtx4090* | 4 | 80% |
| 15 | sn62 Ridges | 62.7 | 83.13 | 925 | rtx4090* | 44 | 15% |
| 16 | sn23 Trishool | 62.6 | 1,082 | 1,082 = | cpu-small | 2 | 80% |
| 17 | sn55 NIOME | 61.7 | 62.03 | 519 | rtx4090* | 11 | 30% |
| 18 | sn81 Reliquary | 61.7 | 62.02 | 178 | rtx4090* | 20 | 59% |
| 19 | sn28 SayGM | 61.6 | 61.51 | 1,509 | rtx4090* | 136 | 24% |
| 20 | sn111 Claims | 58.9 | 27.55 | 2,667 | rtx4090* | 6 | 90% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 27 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-25T05:23 | sn15 | RELEASE | sn15 released v3.0.4: fix: gate BYOK cost fields on usage.is_byok (#39 |
| 2026-10-25T05:23 | sn25 | RELEASE | sn25 released v2026.10.24-1080878340 |
| 2026-10-25T05:23 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.982 - miners can earn again |
| 2026-10-25T05:23 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #417 from reliquadotai |
| 2026-10-25T00:29 | sn15 | RELEASE | sn15 released v3.0.3: feat: capture BYOK upstream inference cost per c |
| 2026-10-25T00:29 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore: remove dead _upload_logs method fr |
| 2026-10-25T00:29 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Publish compatible model-only cohort read |
| 2026-10-24T22:26 | sn25 | RELEASE | sn25 released v2026.10.24-1080739690 |
| 2026-10-24T19:51 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Keep threshold shape validation on failed |
| 2026-10-24T19:51 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #416 from reliquadotai |
| 2026-10-24T19:51 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.926 - miners can earn again |
| 2026-10-24T17:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve source metadata and validated co |
| 2026-10-24T17:39 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reset evaluation forecasts when evaluator |
| 2026-10-24T14:45 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #413 from reliquadotai |
| 2026-10-24T11:23 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): the measurement amendment  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

