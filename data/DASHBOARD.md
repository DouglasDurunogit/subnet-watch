# Subnet watch — dashboard

_snapshot 2026-10-27T01:26:40Z · block 9371734 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,092 | 4,192 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,792 | 1,792 = | rtx4090* | 5 | 20% |
| 3 | sn60 Bitsec.ai | 70 | 286 | 286 = | cpu-small | 3 | 50% |
| 4 | sn46 Instant | 68.6 | 190 | 227 | cpu-small | 7 | 45% |
| 5 | sn1 Apex | 68.2 | 431 | 864 | rtx4090* | 5 | 55% |
| 6 | sn67 Harnyx | 67.9 | 7.08 | 208 | cpu-small | 127 | 10% |
| 7 | sn56 Gradients | 67.4 | 338 | 5,561 | rtx4090* | 8 | 51% |
| 8 | sn120 Affine | 67.2 | 345 | 1,053 | rtx4090* | 91 | 3% |
| 9 | sn107 Minos | 66.7 | 210 | 17,837 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 65.9 | 6.51 | 12.85 | cpu-small | 57 | 97% |
| 11 | sn125 Refinery | 65.7 | 207 | 856 | rtx4090* | 4 | 50% |
| 12 | sn66 conjectures | 63.3 | 99.94 | 208 | rtx4090* | 4 | 80% |
| 13 | sn62 Ridges | 62.6 | 80.39 | 897 | rtx4090* | 44 | 15% |
| 14 | sn111 Claims | 60 | 38.05 | 2,644 | rtx4090* | 5 | 90% |
| 15 | sn28 SayGM | 59.1 | 29.58 | 1,160 | rtx4090* | 143 | 33% |
| 16 | sn58 Attune | 57.3 | 593 | 954 | rtx4090* | 5 | 70% |
| 17 | sn5 Hone | 57.3 | 28.84 | 38.47 | rtx4090* | 241 | 1% |
| 18 | sn81 Reliquary | 56.6 | 12.56 | 92.07 | rtx4090* | 65 | 55% |
| 19 | sn101 Tag101 | 56.3 | 12.90 | 12.98 | cpu-small | 240 | 1% |
| 20 | sn92 REAX | 56.1 | 25.20 | 2,354 | rtx4090 | 234 | 14% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 22 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-27T01:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record the authorized evidence-verificati |
| 2026-10-27T01:27 | sn76 | BURN_DROP | sn76 burn fell 0.998 -> 0.978 - miners can earn again |
| 2026-10-27T01:27 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Accept a list of AMD ARK pins in the brok |
| 2026-10-27T01:27 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |
| 2026-10-27T01:27 | sn125 | README_TASK_DIFF | sn125 README task/scoring sections changed |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

