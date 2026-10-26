# Subnet watch — dashboard

_snapshot 2026-10-26T21:55:35Z · block 9370679 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,111 | 4,231 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,815 | 1,815 = | rtx4090* | 5 | 20% |
| 3 | sn60 Bitsec.ai | 70 | 286 | 286 = | cpu-small | 3 | 50% |
| 4 | sn46 Instant | 69.6 | 254 | 292 | cpu-small | 6 | 45% |
| 5 | sn1 Apex | 68.2 | 437 | 880 | rtx4090* | 5 | 55% |
| 6 | sn67 Harnyx | 67.8 | 7.11 | 209 | cpu-small | 127 | 10% |
| 7 | sn82 Noah | 67.6 | 533 | 539 | rtx4090* | 63 | 2% |
| 8 | sn56 Gradients | 67.4 | 340 | 5,579 | rtx4090* | 8 | 51% |
| 9 | sn107 Minos | 66.8 | 211 | 17,923 | cpu-small | 20 | 80% |
| 10 | sn120 Affine | 66.3 | 265 | 949 | rtx4090* | 102 | 3% |
| 11 | sn15 ORO | 66 | 6.52 | 12.88 | cpu-small | 57 | 97% |
| 12 | sn66 conjectures | 63.3 | 100 | 209 | rtx4090* | 4 | 80% |
| 13 | sn62 Ridges | 62.6 | 80.67 | 900 | rtx4090* | 44 | 15% |
| 14 | sn23 Trishool | 62.5 | 1,059 | 1,059 = | cpu-small | 2 | 80% |
| 15 | sn111 Claims | 60 | 38.19 | 2,652 | rtx4090* | 5 | 90% |
| 16 | sn28 SayGM | 59.6 | 35.03 | 2,000 | rtx4090* | 142 | 17% |
| 17 | sn81 Reliquary | 58.3 | 21.95 | 218 | rtx4090* | 56 | 38% |
| 18 | sn34 BitMind | 57.9 | 4,697 | 8,429 | a100-80 | 3 | 85% |
| 19 | sn5 Hone | 57.1 | 28.68 | 37.26 | rtx4090* | 240 | 1% |
| 20 | sn92 REAX | 57 | 23.23 | 2,335 | rtx4090 | 244 | 15% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 22 |
| captured (>90%) | 22 |

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
| 2026-10-26T21:56 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Document live Finney burn validator status |
| 2026-10-26T21:56 | sn2 | README_TASK_DIFF | sn2 README task/scoring sections changed |
| 2026-10-26T21:56 | sn28 | RELEASE | sn28 released v0.5.12 |
| 2026-10-26T21:56 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: attestd: fix the kubetee.attestation.v1 b |
| 2026-10-26T21:56 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4972 - [P1] Validator fails nodes wit |
| 2026-10-26T21:56 | sn123 | SCORING_COMMIT | sn123 commit touches scoring: Update validator.py |
| 2026-10-26T17:40 | sn12 | RELEASE | sn12 released validator-staging-2026-10-26-40344021717-627-1: fix: eMu |
| 2026-10-26T17:40 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix(validator): fix prometheus image |
| 2026-10-26T17:40 | sn51 | RELEASE | sn51 released miner-v1.010 |
| 2026-10-26T17:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5187 - [P1] Validator: re-probe misse |
| 2026-10-26T17:40 | sn60 | SCORING_COMMIT | sn60 commit touches scoring: changed scorer model to DeepSeek-V3.2 |
| 2026-10-26T17:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #796 from leadpoet/fix |
| 2026-10-26T17:40 | sn75 | RELEASE | sn75 released Runtime 92023 rc2 (srtool, 873384f) |
| 2026-10-26T17:40 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Enforce broader C7+ evaluation suites (#4 |
| 2026-10-26T17:40 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix(web): display NaN scores properly |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

