# Subnet watch — dashboard

_snapshot 2026-11-06T15:15:44Z · block 9447870 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 64 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **64** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,802 | 2,802 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73 | 1,832 | 3,673 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.4 | 1,512 | 1,512 = | rtx4090* | 5 | 20% |
| 4 | sn36 Weir | 69.6 | 662 | 1,294 | rtx4090* | 9 | 24% |
| 5 | sn58 Attune | 68.6 | 498 | 802 | rtx4090* | 5 | 70% |
| 6 | sn41 Almanac | 68.5 | 9.55 | 143 | cpu-small | 177 | 2% |
| 7 | sn56 Gradients | 68.3 | 452 | 4,867 | rtx4090* | 7 | 51% |
| 8 | sn46 Instant | 67.7 | 147 | 173 | cpu-small | 9 | 46% |
| 9 | sn1 Apex | 67.6 | 360 | 718 | rtx4090* | 4 | 72% |
| 10 | sn103 Terza Inference | 67.4 | 340 | 1,031 | rtx4090* | 5 | 40% |
| 11 | sn102 ConnitoAI | 67 | 307 | 1,079 | rtx4090* | 8 | 34% |
| 12 | sn67 Harnyx | 66.7 | 5.28 | 240 | cpu-small | 127 | 13% |
| 13 | sn82 Noah | 66.3 | 354 | 428 | rtx4090* | 64 | 2% |
| 14 | sn107 Minos | 65.9 | 173 | 14,690 | cpu-small | 20 | 80% |
| 15 | sn15 ORO | 65.3 | 6.72 | 11,503 | cpu-small | 69 | 96% |
| 16 | sn53 engy | 65.1 | 169 | 2,796 | rtx4090 | 31 | 21% |
| 17 | sn38 ChronoLLM | 62.8 | 45.43 | 406 | cpu-small | 10 | 52% |
| 18 | sn121 sundae_bar | 61.9 | 894 | 894 = | cpu-small | 2 | 60% |
| 19 | sn62 Ridges | 61.3 | 55.24 | 1,162 | rtx4090* | 38 | 22% |
| 20 | sn66 conjectures | 61.2 | 53.42 | 146 | rtx4090* | 5 | 80% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 30 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-06T15:16 | sn51 | RELEASE | sn51 released executor-v1.172 |
| 2026-11-06T15:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5803 - [P1] Validator registry pull:  |
| 2026-11-06T15:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1087 from leadpoet/fi |
| 2026-11-06T15:16 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse each freshly validated proof receip |
| 2026-11-06T15:16 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Neuron 1.0.3: report the EDA server's di |
| 2026-11-06T15:16 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: H5: a door config with no accepted revis |
| 2026-11-06T07:08 | sn66 | RELEASE | sn66 released v2026.11.06.2 |
| 2026-11-06T07:08 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Finalize exact unused ninth review after  |
| 2026-11-06T07:08 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Pass retained coverage through reward ser |
| 2026-11-06T07:08 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |
| 2026-11-06T00:09 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Shorten the new-miner ramp to 12 observati |
| 2026-11-06T00:09 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Describe prospective seeded crawl coverag |
| 2026-11-06T00:09 | sn66 | RELEASE | sn66 released v2026.11.06 |
| 2026-11-06T00:09 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Pin task documentation for part iii displ |
| 2026-11-06T00:09 | sn76 | BURN_DROP | sn76 burn fell 0.990 -> 0.973 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

