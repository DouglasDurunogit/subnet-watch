# Subnet watch — dashboard

_snapshot 2026-09-23T17:21:00Z · block 9131793 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 80.2 | 15,594 | 25,071 | rtx4090* | 5 | 54% |
| 2 | sn3 Teutonic | 76.5 | 5,149 | 5,149 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.7 | 639 | 2,561 | cpu-small | 5 | 52% |
| 4 | sn114 SOMA | 72.3 | 786 | 7,870 | cpu-small | 8 | 50% |
| 5 | sn67 Harnyx | 71.2 | 16.81 | 1,162 | cpu-small | 124 | 34% |
| 6 | sn1 Apex | 70.5 | 847 | 1,063 | rtx4090* | 4 | 58% |
| 7 | sn102 ConnitoAI | 70.4 | 841 | 1,746 | rtx4090* | 5 | 37% |
| 8 | sn56 Gradients | 69.3 | 606 | 5,539 | rtx4090* | 10 | 40% |
| 9 | sn15 ORO | 68.9 | 13.18 | 20,667 | cpu-small | 68 | 96% |
| 10 | sn107 Minos | 68.6 | 327 | 27,574 | cpu-small | 20 | 80% |
| 11 | sn38 ChronoLLM | 68.1 | 178 | 2,417 | cpu-small | 10 | 52% |
| 12 | sn124 Swarm | 66.9 | 304 | 963 | rtx4090* | 25 | 11% |
| 13 | sn111 Claims | 66.1 | 254 | 2,953 | rtx4090* | 5 | 75% |
| 14 | sn14 Cacheon | 65.8 | 213 | 4,347 | rtx4090* | 11 | 56% |
| 15 | sn26 Perturb | 64.2 | 135 | 214 | rtx3060 | 4 | 90% |
| 16 | sn100 Cortex | 63 | 92.43 | 153 | rtx4090* | 11 | 70% |
| 17 | sn23 Trishool | 61.5 | 802 | 802 = | cpu-small | 2 | 81% |
| 18 | sn62 Ridges | 61.3 | 55.73 | 2,742 | rtx4090* | 19 | 30% |
| 19 | sn74 Gittensor | 60.6 | 49.04 | 119 | rtx4090* | 17 | 63% |
| 20 | sn28 SayGM | 60.5 | 45.24 | 844 | rtx4090* | 68 | 36% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 22 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-23T17:21 | sn9 | RELEASE | sn9 released v4.13.2 |
| 2026-09-23T17:21 | sn25 | RELEASE | sn25 released v2026.9.23-1053753970 |
| 2026-09-23T17:21 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: chore: show float score instead of a 0/1  |
| 2026-09-23T17:21 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Merge PR #3 (cursor/discord-mirror-1b92) |
| 2026-09-23T12:19 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: ci: validate rendered Envoy configs with  |
| 2026-09-23T12:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3505 - [P2] validator: keep the Docke |
| 2026-09-23T12:19 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-23T12:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Document company-only validator compatibi |
| 2026-09-23T12:19 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: show tasks and trajectories on the d |
| 2026-09-23T06:45 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Retry interrupted miner downloads and red |
| 2026-09-23T06:45 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: wvk 23 live 17:20 UTC: AGENTS.md snapsho |
| 2026-09-23T01:38 | sn25 | RELEASE | sn25 released v2026.9.22-1053244730 |
| 2026-09-23T01:38 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.708 - miners can earn again |
| 2026-09-22T23:08 | sn14 | RELEASE | sn14 released glm53-mock-submission-20260906: Merge m3-runtime-seed-re |
| 2026-09-22T23:08 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Add Runpod evaluation backend via dstack  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

