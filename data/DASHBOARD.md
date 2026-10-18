# Subnet watch — dashboard

_snapshot 2026-10-18T21:56:02Z · block 9313162 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 75.6 | 53.71 | 94.68 | cpu-small | 116 | 7% |
| 2 | sn3 Teutonic | 74.3 | 2,702 | 7,220 | rtx4090* | 5 | 40% |
| 3 | sn91 cascade | 71 | 386 | 772 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 70.4 | 826 | 1,428 | rtx4090* | 6 | 34% |
| 5 | sn67 Harnyx | 69.8 | 11.54 | 310 | cpu-small | 127 | 13% |
| 6 | sn53 engy | 69.1 | 572 | 2,378 | rtx4090 | 24 | 16% |
| 7 | sn1 Apex | 68.6 | 486 | 786 | rtx4090* | 5 | 56% |
| 8 | sn82 Noah | 68.1 | 601 | 601 = | rtx4090* | 64 | 2% |
| 9 | sn58 Attune | 67.7 | 379 | 611 | rtx4090* | 5 | 71% |
| 10 | sn107 Minos | 67.2 | 235 | 19,986 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 66.6 | 6.48 | 15,597 | cpu-small | 60 | 97% |
| 12 | sn120 Affine | 64.9 | 176 | 332 | rtx4090* | 211 | 1% |
| 13 | sn14 Cacheon | 63.9 | 118 | 2,887 | rtx4090* | 10 | 43% |
| 14 | sn66 conjectures | 63.6 | 110 | 228 | rtx4090* | 4 | 80% |
| 15 | sn28 SayGM | 62.8 | 88.93 | 1,925 | rtx4090* | 117 | 24% |
| 16 | sn97 Ingot | 61.4 | 1,995 | 1,995 = | rtx4090* | 5 | 20% |
| 17 | sn55 NIOME | 61.4 | 56.31 | 476 | rtx4090* | 11 | 30% |
| 18 | sn61 RedTeam | 61.3 | 56.02 | 99.72 | rtx4090* | 124 | 1% |
| 19 | sn92 REAX | 58.7 | 73.56 | 3,471 | rtx4090 | 246 | 11% |
| 20 | sn81 Reliquary | 58.6 | 24.20 | 98.30 | rtx4090* | 10 | 91% |

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
| dominated (60–90%) | 24 |
| captured (>90%) | 24 |

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
| 2026-10-18T21:56 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Wait for identity-checked validator worke |
| 2026-10-18T19:42 | sn1 | RELEASE | sn1 released v4.4.14 |
| 2026-10-18T19:42 | sn25 | RELEASE | sn25 released v2026.10.18-1075514170 |
| 2026-10-18T19:42 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Release v0.1.0: multisig receipts and sur |
| 2026-10-18T19:42 | sn92 | RELEASE | sn92 released v1.2.0-rc9 |
| 2026-10-18T17:34 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Activate the Mathlib header task release |
| 2026-10-18T17:34 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1423 from carbonphys |
| 2026-10-18T14:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-18T10:56 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs: update stale pack digest and runtim |
| 2026-10-18T10:56 | sn55 | BURN_DROP | sn55 burn fell 1.000 -> 0.010 - miners can earn again |
| 2026-10-18T10:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix(arena): classify unavailable frozen s |
| 2026-10-18T10:56 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: docs: lock bank-version reuse and reward |
| 2026-10-18T05:49 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): send sandbox_metadata whe |
| 2026-10-18T05:49 | sn25 | RELEASE | sn25 released v2026.10.17-1074871400 |
| 2026-10-18T05:49 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: default to half the legs on th |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

