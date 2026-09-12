# Subnet watch — dashboard

_snapshot 2026-09-12T11:06:14Z · block 9051093 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79.9 | 153 | 462 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 75.6 | 53.13 | 131 | cpu-small | 21 | 34% |
| 3 | sn91 cascade | 71.4 | 1,127 | 3,019 | rtx4090* | 5 | 52% |
| 4 | sn96 Verathos | 70.3 | 35.63 | 311 | rtx4090 | 73 | 30% |
| 5 | sn14 Cacheon | 69.4 | 614 | 1,139 | rtx4090* | 12 | 18% |
| 6 | sn107 Minos | 68.9 | 349 | 29,642 | cpu-small | 20 | 80% |
| 7 | sn67 Harnyx | 68.7 | 9.05 | 1,058 | cpu-small | 125 | 33% |
| 8 | sn56 Gradients | 68 | 409 | 5,310 | rtx4090* | 9 | 48% |
| 9 | sn80 OpenRoboto | 67.5 | 354 | 1,254 | rtx4090* | 5 | 43% |
| 10 | sn124 Swarm | 66.5 | 269 | 871 | rtx4090* | 25 | 11% |
| 11 | sn38 ChronoLLM | 66 | 99.71 | 1,363 | cpu-small | 10 | 52% |
| 12 | sn111 Claims | 65.9 | 235 | 3,004 | rtx4090* | 5 | 77% |
| 13 | sn61 RedTeam | 65.7 | 207 | 307 | rtx4090* | 56 | 3% |
| 14 | sn28 SayGM | 62.5 | 80.16 | 2,567 | rtx4090* | 47 | 18% |
| 15 | sn55 NIOME | 62.2 | 72.71 | 599 | rtx4090* | 11 | 29% |
| 16 | sn23 Trishool | 60.3 | 552 | 552 = | cpu-small | 2 | 80% |
| 17 | sn62 Ridges | 60 | 37.04 | 4,018 | rtx4090* | 16 | 52% |
| 18 | sn74 Gittensor | 57.8 | 21.40 | 330 | rtx4090 | 12 | 64% |
| 19 | sn81 Reliquary | 56.6 | 12.55 | 190 | rtx4090* | 88 | 7% |
| 20 | sn9 iota | 56.4 | 13,916 | 13,916 = | rtx4090* | 3 | 74% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 16 |
| captured (>90%) | 19 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-12T11:06 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: gather responses before scoring |
| 2026-09-12T11:06 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Remove the OpenRouter paid-validation bud |
| 2026-09-12T11:06 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): separate reveal accountin |
| 2026-09-12T11:06 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: trainer: king rent retries lemon pods and |
| 2026-09-12T11:06 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: fees: a per submission commitment fee; mt |
| 2026-09-12T06:24 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.742 - miners can earn again |
| 2026-09-12T06:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Reuse verified historical deployment comp |
| 2026-09-12T06:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3439 - [P0] validator: outdated execu |
| 2026-09-12T06:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Use current billing schema in normal vali |
| 2026-09-12T06:24 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-12T01:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Sync disposable replay scratch once after |
| 2026-09-12T01:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve Arena miner credential failure e |
| 2026-09-11T21:21 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Add grounded video scoring and hybrid mai |
| 2026-09-11T21:21 | sn25 | RELEASE | sn25 released v2026.9.11-1043550030 |
| 2026-09-11T21:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify in-flight Arena leases survive par |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

