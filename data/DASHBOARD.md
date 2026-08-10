# Subnet watch — dashboard

_snapshot 2026-08-10T12:07:41Z · block 8813917 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 53 | `████████████████████████████` |
| 0–0.2 | 5 | `███` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 39 | `█████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 110 | 33,059 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.8 | 69.17 | 208 | cpu-small | 10 | 33% |
| 3 | sn67 Harnyx | 71.3 | 17.44 | 756 | cpu-small | 129 | 19% |
| 4 | sn91 cascade | 70.3 | 822 | 2,813 | rtx4090* | 5 | 50% |
| 5 | sn96 Verathos | 70.1 | 33.99 | 341 | rtx4090 | 52 | 41% |
| 6 | sn1 Apex | 69.8 | 694 | 1,598 | rtx4090* | 4 | 52% |
| 7 | sn41 Almanac | 69.3 | 11.18 | 35.06 | cpu-small | 69 | 70% |
| 8 | sn62 Ridges | 69 | 553 | 1,999 | rtx4090* | 7 | 35% |
| 9 | sn26 Perturb | 68.2 | 21.10 | 38.78 | rtx3060 | 11 | 50% |
| 10 | sn11 TrajectoryRL | 67.4 | 4,577 | 4,577 = | cpu-small | 1 | 100% |
| 11 | sn15 ORO | 67.4 | 10.16 | 20.51 | cpu-small | 79 | 93% |
| 12 | sn38 ChronoLLM | 65.7 | 218 | 3,658 | rtx4090* | 10 | 52% |
| 13 | sn21 AdTAO | 65.5 | 4.75 | 22.09 | cpu-small | 142 | 45% |
| 14 | sn80 OpenRoboto | 64.8 | 156 | 565 | rtx4090* | 4 | 91% |
| 15 | sn28 gm | 63.4 | 104 | 3,921 | rtx4090* | 26 | 40% |
| 16 | sn100 BASE | 63.4 | 102 | 323 | rtx4090* | 8 | 50% |
| 17 | sn61 RedTeam | 63.1 | 93.17 | 387 | rtx4090* | 45 | 8% |
| 18 | sn51 lium.io | 58.7 | 32.50 | 3,230 | rtx4090* | 52 | 55% |
| 19 | sn6 Numinous | 58 | 23.41 | 459 | cpu-small | 18 | 26% |
| 20 | sn2 DSperse | 57 | 14.57 | 116 | rtx4090* | 11 | 83% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-10T12:08 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf: import time — hf_scoring_config() rai |
| 2026-08-10T09:57 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Fix degenerate-dataset filter for DPO bos |
| 2026-08-10T08:13 | sn61 | RELEASE | sn61 released 4.9.4 |
| 2026-08-10T08:13 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Gate daily scoring and autoresearch readi |
| 2026-08-10T08:13 | sn96 | RELEASE | sn96 released Verathos v0.1.34 — Reliable Miner Updates |
| 2026-08-10T08:13 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: resume deferred miner updates at idl |
| 2026-08-10T06:20 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner: `cascade duel` — full settled-roun |
| 2026-08-10T06:20 | sn96 | RELEASE | sn96 released v0.1.33 - Maximum-Concurrency Proof Serving |
| 2026-08-10T03:01 | sn58 | BURN_DROP | sn58 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-10T03:01 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Retire MINER_EMISSION_CAP, and make it re |
| 2026-08-10T03:01 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Tell a validator when no directive exists |
| 2026-08-09T22:14 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Referrer: score recruiters across every c |
| 2026-08-09T20:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Close and verify dev snapshot request set |
| 2026-08-09T19:56 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Document miner training benchmark |
| 2026-08-09T19:56 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

