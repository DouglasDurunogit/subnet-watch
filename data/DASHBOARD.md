# Subnet watch — dashboard

_snapshot 2026-10-19T05:03:02Z · block 9315297 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 76.4 | 65.53 | 107 | cpu-small | 116 | 8% |
| 2 | sn3 Teutonic | 74.5 | 2,821 | 7,536 | rtx4090* | 5 | 40% |
| 3 | sn91 cascade | 72.5 | 603 | 1,609 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 69.9 | 12.14 | 325 | cpu-small | 127 | 13% |
| 5 | sn53 engy | 69.2 | 588 | 2,445 | rtx4090 | 24 | 16% |
| 6 | sn82 Noah | 68.9 | 731 | 765 | rtx4090* | 60 | 2% |
| 7 | sn1 Apex | 68.6 | 487 | 781 | rtx4090* | 5 | 58% |
| 8 | sn58 Attune | 67.9 | 400 | 644 | rtx4090* | 5 | 71% |
| 9 | sn107 Minos | 67.4 | 248 | 21,109 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 66.4 | 6.30 | 13.07 | cpu-small | 55 | 98% |
| 11 | sn55 NIOME | 65 | 168 | 520 | rtx4090* | 9 | 31% |
| 12 | sn120 Affine | 64.7 | 177 | 315 | rtx4090* | 228 | 1% |
| 13 | sn14 Cacheon | 64 | 123 | 3,000 | rtx4090* | 10 | 43% |
| 14 | sn66 conjectures | 63.6 | 110 | 228 | rtx4090* | 4 | 80% |
| 15 | sn28 SayGM | 62.7 | 85.11 | 1,828 | rtx4090* | 130 | 14% |
| 16 | sn97 Ingot | 61.6 | 2,082 | 2,082 = | rtx4090* | 5 | 20% |
| 17 | sn61 RedTeam | 61.5 | 60.56 | 110 | rtx4090* | 123 | 1% |
| 18 | sn81 Reliquary | 60.1 | 37.36 | 124 | rtx4090* | 8 | 90% |
| 19 | sn92 REAX | 58.3 | 73.55 | 3,823 | rtx4090 | 241 | 11% |
| 20 | sn4 Targon | 57.9 | 10,054 | 29,642 | rtx4090* | 5 | 70% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 25 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-19T05:03 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(executor): the scored run can wait f |
| 2026-10-19T05:03 | sn25 | RELEASE | sn25 released v2026.10.18-1075707760 |
| 2026-10-19T05:03 | sn51 | RELEASE | sn51 released executor-v1.143 |
| 2026-10-19T05:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - Validator: customer create rem |
| 2026-10-19T05:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Resolve verified LinkedIn company redirec |
| 2026-10-19T05:03 | sn89 | README_TASK_DIFF | sn89 README task/scoring sections changed |
| 2026-10-19T05:03 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Retain admitted cold overlays from verif |
| 2026-10-19T05:03 | sn117 | RELEASE | sn117 released everycli v0.5.8 |
| 2026-10-19T05:03 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: fix: validate provider model availabilit |
| 2026-10-18T21:56 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Wait for identity-checked validator worke |
| 2026-10-18T19:42 | sn1 | RELEASE | sn1 released v4.4.14 |
| 2026-10-18T19:42 | sn25 | RELEASE | sn25 released v2026.10.18-1075514170 |
| 2026-10-18T19:42 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Release v0.1.0: multisig receipts and sur |
| 2026-10-18T19:42 | sn92 | RELEASE | sn92 released v1.2.0-rc9 |
| 2026-10-18T17:34 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Activate the Mathlib header task release |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

