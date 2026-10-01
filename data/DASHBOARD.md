# Subnet watch — dashboard

_snapshot 2026-10-01T13:42:25Z · block 9188299 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 65 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **65** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.5 | 40.81 | 558 | cpu-small | 121 | 8% |
| 2 | sn23 Trishool | 74.1 | 974 | 974 = | cpu-small | 2 | 80% |
| 3 | sn53 engy | 72.2 | 1,427 | 3,913 | rtx4090 | 14 | 22% |
| 4 | sn102 ConnitoAI | 71.9 | 1,320 | 1,781 | rtx4090* | 4 | 36% |
| 5 | sn91 cascade | 71.3 | 428 | 1,143 | cpu-small | 5 | 52% |
| 6 | sn1 Apex | 70.8 | 932 | 1,100 | rtx4090* | 4 | 57% |
| 7 | sn120 Affine | 70.5 | 897 | 897 = | rtx4090* | 47 | 2% |
| 8 | sn107 Minos | 68.9 | 356 | 28,762 | cpu-small | 20 | 80% |
| 9 | sn46 Instant | 68.8 | 201 | 224 | cpu-small | 6 | 69% |
| 10 | sn15 ORO | 68.7 | 11.56 | 20,476 | cpu-small | 68 | 96% |
| 11 | sn56 Gradients | 68.6 | 484 | 5,261 | rtx4090* | 9 | 39% |
| 12 | sn111 Claims | 68.4 | 469 | 2,082 | rtx4090* | 5 | 54% |
| 13 | sn96 Verathos | 67.5 | 18.90 | 300 | rtx4090 | 73 | 31% |
| 14 | sn4 Targon | 65.4 | 6,455 | 32,616 | rtx4090* | 5 | 71% |
| 15 | sn3 Teutonic | 64.4 | 4,930 | 4,930 = | rtx4090* | 5 | 20% |
| 16 | sn62 Ridges | 63.7 | 113 | 1,403 | rtx4090* | 25 | 15% |
| 17 | sn61 RedTeam | 62.7 | 87.16 | 158 | rtx4090* | 112 | 2% |
| 18 | sn28 SayGM | 60.5 | 45.77 | 1,002 | rtx4090* | 69 | 19% |
| 19 | sn5 Hone | 59.6 | 39.48 | 41.93 | rtx4090* | 241 | 0% |
| 20 | sn80 OpenRoboto | 59.2 | 1,038 | 3,505 | rtx4090* | 8 | 34% |

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
| wide (<30%) | 21 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 24 |
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
| 2026-10-01T13:42 | sn13 | RELEASE | sn13 released Release v1.18.73 |
| 2026-10-01T13:42 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: docs(agents): rewrite from code-verified  |
| 2026-10-01T13:42 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): take an upload before wa |
| 2026-10-01T13:42 | sn25 | RELEASE | sn25 released v2026.10.1-1060587890 |
| 2026-10-01T13:42 | sn51 | RELEASE | sn51 released validator-v2026.10.01 |
| 2026-10-01T13:42 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P2] validator: remove INSPEC |
| 2026-10-01T13:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Release October 1 provider hold with exac |
| 2026-10-01T13:42 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: docs(design): evaluation on SN81, rulings |
| 2026-10-01T13:42 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #347 from TensorLink-A |
| 2026-10-01T13:42 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: snp friend probe: an unavailable AMD veri |
| 2026-10-01T13:42 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-10-01T13:42 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document original Trivia Abstain tasks a |
| 2026-10-01T06:20 | sn25 | RELEASE | sn25 released v2026.9.30-1060350310 |
| 2026-10-01T06:20 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify and aggregate pinned mainnet image |
| 2026-10-01T06:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected workflows to verifier reco |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

