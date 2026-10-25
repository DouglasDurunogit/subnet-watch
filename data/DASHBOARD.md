# Subnet watch — dashboard

_snapshot 2026-10-25T14:19:31Z · block 9361198 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 34 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.4 | 2,071 | 4,151 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 72.9 | 1,778 | 1,778 = | rtx4090* | 5 | 20% |
| 3 | sn67 Harnyx | 70.3 | 13.41 | 140 | cpu-small | 128 | 7% |
| 4 | sn56 Gradients | 69.7 | 675 | 5,581 | rtx4090* | 6 | 51% |
| 5 | sn46 Instant | 69.2 | 224 | 231 | cpu-small | 6 | 42% |
| 6 | sn1 Apex | 68.1 | 414 | 839 | rtx4090* | 5 | 56% |
| 7 | sn82 Noah | 67.8 | 584 | 590 | rtx4090* | 63 | 2% |
| 8 | sn41 Almanac | 67.7 | 8.06 | 127 | cpu-small | 159 | 3% |
| 9 | sn53 engy | 66.9 | 294 | 2,414 | rtx4090 | 36 | 11% |
| 10 | sn107 Minos | 66.8 | 213 | 18,093 | cpu-small | 20 | 80% |
| 11 | sn120 Affine | 64.5 | 159 | 1,116 | rtx4090* | 130 | 4% |
| 12 | sn66 conjectures | 63.3 | 99.12 | 206 | rtx4090* | 4 | 80% |
| 13 | sn15 ORO | 63 | 4.37 | 9.94 | cpu-small | 48 | 98% |
| 14 | sn62 Ridges | 62.6 | 81.80 | 911 | rtx4090* | 44 | 15% |
| 15 | sn23 Trishool | 62.3 | 1,003 | 1,003 = | cpu-small | 2 | 80% |
| 16 | sn14 Cacheon | 60.7 | 1,594 | 4,100 | rtx4090* | 3 | 65% |
| 17 | sn28 SayGM | 59.8 | 37.02 | 2,605 | rtx4090* | 134 | 38% |
| 18 | sn111 Claims | 58.9 | 27.04 | 2,628 | rtx4090* | 6 | 90% |
| 19 | sn81 Reliquary | 58.8 | 25.66 | 231 | rtx4090* | 38 | 30% |
| 20 | sn92 REAX | 58 | 34.73 | 2,706 | rtx4090 | 225 | 15% |

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
| dominated (60–90%) | 26 |
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
| 2026-10-25T14:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5061 - [P1] Validator: re-anchor an i |
| 2026-10-25T14:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Materialize eligible closed score runs be |
| 2026-10-25T14:20 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat(eval): score agent turns mid-traject |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

