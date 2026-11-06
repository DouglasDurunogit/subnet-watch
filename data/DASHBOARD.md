# Subnet watch — dashboard

_snapshot 2026-11-06T07:08:33Z · block 9445435 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 65 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 104 | `miner_burn` < 0.99 |
| Ranked | 104 | passed every gate |
| **Positive margin** | **65** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 24 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.3 | 2,732 | 2,732 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.9 | 1,774 | 3,557 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.2 | 1,446 | 1,446 = | rtx4090* | 5 | 20% |
| 4 | sn36 Weir | 70.6 | 892 | 1,492 | rtx4090* | 8 | 24% |
| 5 | sn41 Almanac | 68.9 | 10.26 | 140 | cpu-small | 175 | 2% |
| 6 | sn58 Attune | 68.3 | 453 | 730 | rtx4090* | 5 | 70% |
| 7 | sn103 Terza Inference | 67.7 | 378 | 918 | rtx4090* | 5 | 33% |
| 8 | sn1 Apex | 67.6 | 363 | 723 | rtx4090* | 4 | 70% |
| 9 | sn46 Instant | 67.6 | 140 | 211 | cpu-small | 9 | 46% |
| 10 | sn56 Gradients | 66.8 | 289 | 4,774 | rtx4090* | 7 | 51% |
| 11 | sn102 ConnitoAI | 66.7 | 274 | 1,437 | rtx4090* | 7 | 46% |
| 12 | sn67 Harnyx | 66.6 | 5.12 | 234 | cpu-small | 126 | 13% |
| 13 | sn15 ORO | 66.3 | 6.83 | 11,276 | cpu-small | 66 | 96% |
| 14 | sn82 Noah | 66.2 | 346 | 418 | rtx4090* | 64 | 2% |
| 15 | sn107 Minos | 65.8 | 168 | 14,284 | cpu-small | 20 | 80% |
| 16 | sn127 Zils | 65.4 | 187 | 188 | rtx4090* | 4 | 78% |
| 17 | sn53 engy | 65 | 169 | 2,789 | rtx4090 | 31 | 21% |
| 18 | sn38 ChronoLLM | 63.4 | 51.48 | 459 | cpu-small | 10 | 52% |
| 19 | sn121 sundae_bar | 61.8 | 866 | 866 = | cpu-small | 2 | 60% |
| 20 | sn62 Ridges | 61.7 | 61.15 | 1,147 | rtx4090* | 37 | 22% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 29 |
| captured (>90%) | 25 |

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
| 2026-11-06T07:08 | sn66 | RELEASE | sn66 released v2026.11.06.2 |
| 2026-11-06T07:08 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Finalize exact unused ninth review after  |
| 2026-11-06T07:08 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Pass retained coverage through reward ser |
| 2026-11-06T07:08 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |
| 2026-11-06T00:09 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Shorten the new-miner ramp to 12 observati |
| 2026-11-06T00:09 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Describe prospective seeded crawl coverag |
| 2026-11-06T00:09 | sn66 | RELEASE | sn66 released v2026.11.06 |
| 2026-11-06T00:09 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Pin task documentation for part iii displ |
| 2026-11-06T00:09 | sn76 | BURN_DROP | sn76 burn fell 0.990 -> 0.973 - miners can earn again |
| 2026-11-06T00:09 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Validator: read blobs from extra bases (S |
| 2026-11-06T00:09 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Support audited competition amendments a |
| 2026-11-06T00:09 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: sn120: gate-pool-v2 = gate-pool-v1 + har |
| 2026-11-06T00:09 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Validator: weights never wait for a soup |
| 2026-11-05T19:03 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(status): each miner's model start, d |
| 2026-11-05T19:03 | sn46 | RELEASE | sn46 released v0.1.5 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

