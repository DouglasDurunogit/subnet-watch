# Subnet watch — dashboard

_snapshot 2026-10-25T22:30:25Z · block 9363653 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

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
| 1 | sn3 Teutonic | 73.5 | 2,114 | 4,237 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,818 | 1,818 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 71.2 | 1,053 | 5,705 | rtx4090* | 6 | 51% |
| 4 | sn67 Harnyx | 70.4 | 13.73 | 143 | cpu-small | 129 | 7% |
| 5 | sn46 Instant | 69.2 | 226 | 236 | cpu-small | 6 | 43% |
| 6 | sn1 Apex | 68.2 | 433 | 826 | rtx4090* | 5 | 56% |
| 7 | sn82 Noah | 67.8 | 586 | 593 | rtx4090* | 63 | 2% |
| 8 | sn41 Almanac | 67.8 | 8.37 | 128 | cpu-small | 159 | 5% |
| 9 | sn53 engy | 66.8 | 287 | 2,489 | rtx4090 | 36 | 11% |
| 10 | sn107 Minos | 66.8 | 214 | 18,167 | cpu-small | 20 | 80% |
| 11 | sn120 Affine | 64.3 | 148 | 1,524 | rtx4090* | 122 | 5% |
| 12 | sn15 ORO | 64.1 | 4.50 | 10.21 | cpu-small | 48 | 98% |
| 13 | sn66 conjectures | 63.4 | 101 | 211 | rtx4090* | 4 | 80% |
| 14 | sn62 Ridges | 62.7 | 82.99 | 924 | rtx4090* | 44 | 15% |
| 15 | sn23 Trishool | 62.5 | 1,071 | 1,071 = | cpu-small | 2 | 80% |
| 16 | sn92 REAX | 59 | 36.23 | 3,509 | rtx4090 | 230 | 18% |
| 17 | sn111 Claims | 58.9 | 27.71 | 2,688 | rtx4090* | 6 | 90% |
| 18 | sn81 Reliquary | 58.3 | 21.50 | 195 | rtx4090* | 41 | 42% |
| 19 | sn28 SayGM | 58.2 | 23.38 | 1,191 | rtx4090* | 136 | 50% |
| 20 | sn5 Hone | 57.5 | 29.08 | 35.07 | rtx4090* | 242 | 0% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 23 |
| captured (>90%) | 24 |

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
| 2026-10-25T22:30 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse native request closure verification |
| 2026-10-25T22:30 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.955 - miners can earn again |
| 2026-10-25T20:01 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.965 - miners can earn again |
| 2026-10-25T20:01 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #412 from Umi-BitSign/ |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

