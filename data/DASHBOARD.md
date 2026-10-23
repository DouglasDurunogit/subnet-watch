# Subnet watch — dashboard

_snapshot 2026-10-23T10:21:32Z · block 9345608 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn121 sundae_bar | 74.5 | 1,100 | 1,100 = | cpu-small | 2 | 60% |
| 2 | sn3 Teutonic | 73.6 | 2,174 | 6,538 | rtx4090* | 6 | 37% |
| 3 | sn91 cascade | 73.2 | 740 | 1,480 | cpu-small | 5 | 52% |
| 4 | sn104 TAOstatus | 69.6 | 405 | 405 = | cpu-small | 7 | 14% |
| 5 | sn46 Instant | 68.9 | 208 | 254 | cpu-small | 12 | 10% |
| 6 | sn67 Harnyx | 68.5 | 8.71 | 226 | cpu-small | 123 | 10% |
| 7 | sn1 Apex | 68.4 | 461 | 899 | rtx4090* | 5 | 53% |
| 8 | sn82 Noah | 68.1 | 624 | 632 | rtx4090* | 62 | 2% |
| 9 | sn102 ConnitoAI | 67.4 | 349 | 989 | rtx4090* | 7 | 29% |
| 10 | sn56 Gradients | 67.3 | 333 | 5,337 | rtx4090* | 9 | 46% |
| 11 | sn53 engy | 67.2 | 321 | 2,846 | rtx4090 | 36 | 11% |
| 12 | sn107 Minos | 67.2 | 236 | 19,756 | cpu-small | 20 | 80% |
| 13 | sn125 Refinery | 66.7 | 277 | 935 | rtx4090* | 4 | 50% |
| 14 | sn66 conjectures | 63.5 | 107 | 208 | rtx4090* | 4 | 81% |
| 15 | sn120 Affine | 62 | 87.78 | 252 | rtx4090* | 279 | 1% |
| 16 | sn55 NIOME | 61.7 | 61.96 | 518 | rtx4090* | 11 | 30% |
| 17 | sn41 Almanac | 60.3 | 2.09 | 166 | cpu-small | 158 | 3% |
| 18 | sn92 REAX | 59.9 | 55.80 | 4,040 | rtx4090 | 224 | 17% |
| 19 | sn34 BitMind | 59.7 | 7,884 | 7,884 = | a100-80 | 2 | 85% |
| 20 | sn111 Claims | 59.2 | 29.63 | 2,822 | rtx4090* | 6 | 90% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 28 |
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
| 2026-10-23T10:21 | sn12 | RELEASE | sn12 released miner-staging-2026-10-23-39921557432-424-1: fix: eMudhra |
| 2026-10-23T10:21 | sn28 | RELEASE | sn28 released v0.5.11-dev |
| 2026-10-23T10:21 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.11-dev (#350 |
| 2026-10-23T10:21 | sn46 | RELEASE | sn46 released Merge pull request #10 from Subnet46/release/v0.1.4 |
| 2026-10-23T10:21 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: miner run.sh: retry the database migratio |
| 2026-10-23T10:21 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-23T10:21 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse verified model references in legacy |
| 2026-10-23T10:21 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Merge pull request #230 from DendriteHQ/ |
| 2026-10-23T05:10 | sn15 | RELEASE | sn15 released v3.0.2: security: patch Python dependencies and supporte |
| 2026-10-23T05:10 | sn21 | RELEASE | sn21 released SN21 training data v5 (rules from 30 Oct 2026) |
| 2026-10-23T05:10 | sn28 | RELEASE | sn28 released v0.5.10 |
| 2026-10-23T05:10 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.10 (#348) |
| 2026-10-23T05:10 | sn51 | RELEASE | sn51 released executor-v1.152 |
| 2026-10-23T05:10 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5012 - [P0] Validator: a killed fille |
| 2026-10-23T05:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Carry verified numeric LinkedIn identity  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

