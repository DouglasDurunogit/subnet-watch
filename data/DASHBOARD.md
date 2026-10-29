# Subnet watch — dashboard

_snapshot 2026-10-29T00:17:57Z · block 9385791 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.6 | 2,187 | 4,383 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73.1 | 1,891 | 1,891 = | rtx4090* | 5 | 20% |
| 3 | sn103 Terza Inference | 71.8 | 1,255 | 2,337 | rtx4090* | 4 | 52% |
| 4 | sn56 Gradients | 71.1 | 1,042 | 5,635 | rtx4090* | 6 | 51% |
| 5 | sn60 Bitsec.ai | 69.7 | 260 | 260 = | cpu-small | 3 | 50% |
| 6 | sn91 cascade | 69.4 | 623 | 1,676 | rtx4090* | 5 | 52% |
| 7 | sn46 Instant | 68.7 | 193 | 211 | cpu-small | 7 | 46% |
| 8 | sn53 engy | 68.3 | 452 | 2,432 | rtx4090 | 29 | 26% |
| 9 | sn1 Apex | 68.3 | 451 | 867 | rtx4090* | 5 | 58% |
| 10 | sn67 Harnyx | 66.9 | 5.71 | 339 | cpu-small | 157 | 16% |
| 11 | sn107 Minos | 66.8 | 213 | 18,140 | cpu-small | 20 | 80% |
| 12 | sn15 ORO | 66.1 | 6.80 | 14.81 | cpu-small | 65 | 97% |
| 13 | sn125 Refinery | 65.5 | 191 | 893 | rtx4090* | 4 | 50% |
| 14 | sn66 conjectures | 64.5 | 141 | 179 | rtx4090* | 4 | 80% |
| 15 | sn62 Ridges | 62.5 | 77.91 | 763 | rtx4090* | 44 | 15% |
| 16 | sn23 Trishool | 62.4 | 1,044 | 1,044 = | cpu-small | 2 | 80% |
| 17 | sn28 SayGM | 61.7 | 66.04 | 707 | rtx4090* | 135 | 40% |
| 18 | sn4 Targon | 58.1 | 10,545 | 31,231 | rtx4090* | 4 | 72% |
| 19 | sn78 Umi | 57.8 | 26.06 | 89.46 | rtx4090* | 21 | 30% |
| 20 | sn6 Numinous | 57.8 | 23.29 | 228 | rtx4090* | 37 | 14% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 22 |
| captured (>90%) | 25 |

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
| 2026-10-29T00:18 | sn66 | RELEASE | sn66 released v2026.10.28.3 |
| 2026-10-29T00:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow scored Arena publication during aut |
| 2026-10-29T00:18 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Keep reserved participation fair and reus |
| 2026-10-28T20:27 | sn17 | RELEASE | sn17 released witness-client-v0.2.15 |
| 2026-10-28T20:27 | sn32 | BURN_DROP | sn32 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-28T20:27 | sn66 | RELEASE | sn66 released v2026.10.28.2 |
| 2026-10-28T20:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Select preflight process helper before re |
| 2026-10-28T20:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse reservation validation and expose i |
| 2026-10-28T20:27 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat(promoter): credit Bonsai 2 on q2 kin |
| 2026-10-28T20:27 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.982 - miners can earn again |
| 2026-10-28T15:18 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Verify NEAR's GLM-5.3-Flash attested host |
| 2026-10-28T15:18 | sn32 | SCORING_COMMIT | sn32 commit touches scoring: Bump wandb to 0.31.0 so validator logs re |
| 2026-10-28T15:18 | sn50 | RELEASE | sn50 released v1.15.0 |
| 2026-10-28T15:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5194 - [P1] Validator: key sshd boots |
| 2026-10-28T15:18 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #58 from hanlinai/feat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

