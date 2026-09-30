# Subnet watch — dashboard

_snapshot 2026-09-30T15:52:45Z · block 9181750 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 10 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.2 | 37.95 | 114 | cpu-small | 118 | 16% |
| 2 | sn23 Trishool | 74.1 | 965 | 965 = | cpu-small | 2 | 80% |
| 3 | sn53 engy | 72.1 | 1,394 | 3,825 | rtx4090 | 14 | 22% |
| 4 | sn91 cascade | 72.1 | 538 | 2,153 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 70.9 | 964 | 1,041 | rtx4090* | 4 | 56% |
| 6 | sn46 Instant | 69.7 | 260 | 396 | cpu-small | 4 | 71% |
| 7 | sn56 Gradients | 69.6 | 666 | 5,401 | rtx4090* | 9 | 39% |
| 8 | sn107 Minos | 68.8 | 345 | 29,434 | cpu-small | 20 | 80% |
| 9 | sn15 ORO | 68.5 | 13.30 | 20,124 | cpu-small | 83 | 95% |
| 10 | sn96 Verathos | 67.7 | 19.73 | 244 | rtx4090 | 72 | 30% |
| 11 | sn111 Claims | 66.9 | 312 | 1,714 | rtx4090* | 5 | 43% |
| 12 | sn4 Targon | 65.5 | 6,640 | 33,552 | rtx4090* | 5 | 71% |
| 13 | sn14 Cacheon | 64.8 | 159 | 2,335 | rtx4090* | 16 | 29% |
| 14 | sn3 Teutonic | 64.5 | 5,036 | 5,036 = | rtx4090* | 5 | 20% |
| 15 | sn62 Ridges | 64.3 | 135 | 1,170 | rtx4090* | 26 | 13% |
| 16 | sn61 RedTeam | 62.7 | 84.16 | 194 | rtx4090* | 95 | 2% |
| 17 | sn26 Perturb | 62.6 | 82.28 | 126 | rtx3060 | 5 | 90% |
| 18 | sn28 SayGM | 62.1 | 73.02 | 1,020 | rtx4090* | 68 | 13% |
| 19 | sn5 Hone | 59.9 | 41.96 | 44.44 | rtx4090* | 237 | 0% |
| 20 | sn81 Reliquary | 59.8 | 34.27 | 99.12 | rtx4090* | 25 | 83% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 23 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-30T15:53 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Isolate GPU model execution and enforce v |
| 2026-09-30T15:53 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Build mips64 miner targets as softfloat |
| 2026-09-30T15:53 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P2] validator: log repeated  |
| 2026-09-30T15:53 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: accept submits like the bench in eva |
| 2026-09-30T15:53 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(validator): wait for due canonical  |
| 2026-09-30T08:50 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Keep validator credentials out of local G |
| 2026-09-30T08:50 | sn51 | RELEASE | sn51 released lium-core-v0.1.13 |
| 2026-09-30T08:50 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3890 - [P1] validator: unique obfusca |
| 2026-09-30T08:50 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #344 from TensorLink-A |
| 2026-09-30T02:18 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Test this release against the previous rel |
| 2026-09-30T02:18 | sn15 | RELEASE | sn15 released v2.0.39: Translate live Chutes model IDs on OpenRouter r |
| 2026-09-30T02:18 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Record foreground waits for prefetched ch |
| 2026-09-30T02:18 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: feat(snp): emit the validator policy entr |
| 2026-09-29T23:14 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Bind evaluator publications to their wind |
| 2026-09-29T19:33 | sn1 | RELEASE | sn1 released v4.4.11 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

