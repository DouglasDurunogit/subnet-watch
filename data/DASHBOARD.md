# Subnet watch — dashboard

_snapshot 2026-10-30T03:00:18Z · block 9393802 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 76.2 | 4,740 | 4,740 = | rtx4090* | 6 | 17% |
| 2 | sn3 Teutonic | 73.2 | 1,932 | 1,932 = | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.7 | 1,655 | 1,655 = | rtx4090* | 5 | 20% |
| 4 | sn46 Instant | 69.9 | 279 | 303 | cpu-small | 5 | 40% |
| 5 | sn103 Terza Inference | 69.6 | 649 | 1,697 | rtx4090* | 5 | 37% |
| 6 | sn56 Gradients | 69.4 | 617 | 5,073 | rtx4090* | 6 | 51% |
| 7 | sn60 Bitsec.ai | 69.2 | 228 | 228 = | cpu-small | 3 | 50% |
| 8 | sn91 cascade | 68.9 | 537 | 1,446 | rtx4090* | 5 | 52% |
| 9 | sn53 engy | 68 | 409 | 2,204 | rtx4090 | 29 | 26% |
| 10 | sn1 Apex | 67.6 | 358 | 796 | rtx4090* | 5 | 61% |
| 11 | sn67 Harnyx | 66.8 | 5.52 | 508 | cpu-small | 131 | 26% |
| 12 | sn15 ORO | 66.3 | 6.62 | 12,444 | cpu-small | 68 | 96% |
| 13 | sn107 Minos | 65.8 | 166 | 14,132 | cpu-small | 20 | 80% |
| 14 | sn125 Refinery | 64.9 | 160 | 801 | rtx4090* | 4 | 50% |
| 15 | sn121 sundae_bar | 62.1 | 940 | 940 = | cpu-small | 2 | 60% |
| 16 | sn62 Ridges | 62.1 | 69.75 | 690 | rtx4090* | 44 | 15% |
| 17 | sn124 Swarm | 61.7 | 70.36 | 5,292 | rtx4090* | 11 | 85% |
| 18 | sn117 everyframe.studi | 60.6 | 45.66 | 81.63 | rtx4090* | 4 | 89% |
| 19 | sn66 conjectures | 58.7 | 24.60 | 156 | rtx4090* | 7 | 80% |
| 20 | sn28 SayGM | 58.6 | 27.45 | 1,623 | rtx4090* | 152 | 13% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 26 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 100 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-30T03:00 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge leadertop/head-summary-upload: the  |
| 2026-10-30T03:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Ignore validator runtime state at checkou |
| 2026-10-30T03:00 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Agent competition scoreboard builder |
| 2026-10-30T03:00 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge pull request #239 from swarm-subne |
| 2026-10-29T23:29 | sn1 | RELEASE | sn1 released v4.5.4 |
| 2026-10-29T23:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge leadertop/head-summary-spec: valida |
| 2026-10-29T23:29 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5177 connector lead lock TTL 15 s ->  |
| 2026-10-29T23:29 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #528 from ridgesai/fea |
| 2026-10-29T23:29 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Validate claims-room upload paths and req |
| 2026-10-29T19:17 | sn1 | RELEASE | sn1 released v4.5.3 |
| 2026-10-29T19:17 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Preserve deployed validator recovery in t |
| 2026-10-29T19:17 | sn28 | RELEASE | sn28 released v0.5.15 |
| 2026-10-29T19:17 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3698 - [P2] Validator: pay a split no |
| 2026-10-29T19:17 | sn51 | README_TASK_DIFF | sn51 README task/scoring sections changed |
| 2026-10-29T19:17 | sn66 | RELEASE | sn66 released v2026.10.29 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

