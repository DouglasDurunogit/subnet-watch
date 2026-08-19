# Subnet watch — dashboard

_snapshot 2026-08-19T08:02:06Z · block 8877480 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 36 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 82 | 264 | 440 | cpu-small | 4 | 35% |
| 2 | sn67 Harnyx | 72 | 21.53 | 289 | cpu-small | 144 | 9% |
| 3 | sn26 Perturb | 70.7 | 39.53 | 72.57 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.1 | 761 | 1,033 | rtx4090* | 4 | 56% |
| 5 | sn15 ORO | 70 | 16.46 | 14,602 | cpu-small | 80 | 92% |
| 6 | sn56 Gradients | 69.4 | 616 | 928 | rtx4090* | 5 | 72% |
| 7 | sn91 cascade | 69.1 | 568 | 2,296 | rtx4090* | 5 | 52% |
| 8 | sn38 ChronoLLM | 67.4 | 142 | 3,019 | cpu-small | 10 | 52% |
| 9 | sn41 Almanac | 65.9 | 5.08 | 27.31 | cpu-small | 76 | 81% |
| 10 | sn96 Verathos | 65.5 | 11.00 | 293 | rtx4090 | 93 | 41% |
| 11 | sn107 Minos | 64.1 | 113 | 33,307 | cpu-small | 20 | 90% |
| 12 | sn21 AdTAO | 64.1 | 3.49 | 718 | cpu-small | 16 | 37% |
| 13 | sn98 NeverPlayAlone | 64 | 1,651 | 1,651 = | cpu-small | 1 | 100% |
| 14 | sn85 Vidaio | 63.9 | 118 | 370 | rtx4090* | 13 | 42% |
| 15 | sn53 engy | 62.8 | 86.96 | 2,053 | rtx4090 | 144 | 11% |
| 16 | sn81 Reliquary | 62.3 | 73.72 | 211 | rtx4090* | 48 | 5% |
| 17 | sn55 NIOME | 61.4 | 55.83 | 464 | rtx4090* | 11 | 29% |
| 18 | sn51 lium.io | 61.2 | 61.11 | 928 | rtx4090* | 54 | 79% |
| 19 | sn28 gm | 61.1 | 52.61 | 1,477 | rtx4090* | 45 | 15% |
| 20 | sn68 NOVA | 54.9 | 7,605 | 7,605 = | rtx4090* | 1 | 100% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 16 |
| captured (>90%) | 31 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-19T08:02 | sn62 | BURN_DROP | sn62 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-19T08:02 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Declare pynacl for token verification |
| 2026-08-19T07:15 | sn100 | RELEASE | sn100 released v3.3.25: fix(prism): stop control-plane OOM restarts |
| 2026-08-19T05:42 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(validator): tell operators to re-po |
| 2026-08-19T04:51 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.839 - miners can earn again |
| 2026-08-19T03:08 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Merge pull request #20 from instant-subne |
| 2026-08-19T03:08 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.607 - miners can earn again |
| 2026-08-19T01:50 | sn14 | BURN_DROP | sn14 burn fell 1.000 -> 0.298 - miners can earn again |
| 2026-08-19T01:50 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Merge pull request #18 from instant-subne |
| 2026-08-19T01:50 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Isolate parity scoring cache |
| 2026-08-19T01:50 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix validator batch reliability and prov |
| 2026-08-19T00:01 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: test: freeze validator report contract |
| 2026-08-18T23:03 | sn62 | RELEASE | sn62 released v0.2.9 |
| 2026-08-18T22:37 | sn28 | RELEASE | sn28 released v0.4.6-dev |
| 2026-08-18T22:37 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Release gm-miner v0.4.6-dev |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

