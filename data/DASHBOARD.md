# Subnet watch — dashboard

_snapshot 2026-10-25T09:59:37Z · block 9359899 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.4 | 2,081 | 4,170 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 72.9 | 1,773 | 1,773 = | rtx4090* | 5 | 20% |
| 3 | sn67 Harnyx | 70.4 | 13.40 | 140 | cpu-small | 128 | 7% |
| 4 | sn46 Instant | 69.2 | 227 | 230 | cpu-small | 6 | 41% |
| 5 | sn56 Gradients | 68.8 | 512 | 1,399 | rtx4090* | 6 | 51% |
| 6 | sn1 Apex | 68.1 | 421 | 853 | rtx4090* | 5 | 55% |
| 7 | sn82 Noah | 67.8 | 589 | 595 | rtx4090* | 63 | 2% |
| 8 | sn41 Almanac | 67.2 | 7.23 | 129 | cpu-small | 167 | 3% |
| 9 | sn53 engy | 66.9 | 290 | 2,377 | rtx4090 | 36 | 11% |
| 10 | sn107 Minos | 66.8 | 213 | 18,115 | cpu-small | 20 | 80% |
| 11 | sn120 Affine | 64.5 | 162 | 1,114 | rtx4090* | 125 | 4% |
| 12 | sn66 conjectures | 63.3 | 98.88 | 206 | rtx4090* | 4 | 80% |
| 13 | sn15 ORO | 63.2 | 4.45 | 14,288 | cpu-small | 48 | 98% |
| 14 | sn62 Ridges | 62.6 | 81.65 | 910 | rtx4090* | 44 | 15% |
| 15 | sn23 Trishool | 62.5 | 1,062 | 1,062 = | cpu-small | 2 | 80% |
| 16 | sn28 SayGM | 62 | 68.59 | 1,423 | rtx4090* | 138 | 27% |
| 17 | sn14 Cacheon | 60.7 | 1,589 | 4,088 | rtx4090* | 3 | 65% |
| 18 | sn81 Reliquary | 59.7 | 33.41 | 222 | rtx4090* | 37 | 32% |
| 19 | sn111 Claims | 58.9 | 26.94 | 2,621 | rtx4090* | 6 | 90% |
| 20 | sn92 REAX | 58.4 | 34.78 | 3,282 | rtx4090 | 221 | 18% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 27 |
| captured (>90%) | 20 |

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
| 2026-10-25T10:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow miner execution alongside baseline  |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

