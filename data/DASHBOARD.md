# Subnet watch — dashboard

_snapshot 2026-10-28T20:27:03Z · block 9384636 · run_status **ok**_

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
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.6 | 2,184 | 4,376 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73.2 | 1,907 | 1,907 = | rtx4090* | 5 | 20% |
| 3 | sn103 Terza Inference | 72 | 1,359 | 3,224 | rtx4090* | 4 | 52% |
| 4 | sn56 Gradients | 71.1 | 1,042 | 5,633 | rtx4090* | 6 | 51% |
| 5 | sn60 Bitsec.ai | 69.6 | 253 | 253 = | cpu-small | 3 | 50% |
| 6 | sn91 cascade | 69.4 | 627 | 1,685 | rtx4090* | 5 | 52% |
| 7 | sn46 Instant | 68.9 | 208 | 218 | cpu-small | 8 | 44% |
| 8 | sn53 engy | 68.4 | 453 | 2,438 | rtx4090 | 29 | 26% |
| 9 | sn1 Apex | 68.2 | 434 | 887 | rtx4090* | 5 | 58% |
| 10 | sn67 Harnyx | 67 | 5.71 | 339 | cpu-small | 157 | 16% |
| 11 | sn107 Minos | 66.9 | 218 | 18,193 | cpu-small | 20 | 80% |
| 12 | sn15 ORO | 65.8 | 6.83 | 14.88 | cpu-small | 65 | 97% |
| 13 | sn125 Refinery | 65.4 | 190 | 886 | rtx4090* | 4 | 50% |
| 14 | sn62 Ridges | 62.7 | 82.26 | 916 | rtx4090* | 44 | 15% |
| 15 | sn23 Trishool | 62.4 | 1,049 | 1,049 = | cpu-small | 2 | 80% |
| 16 | sn28 SayGM | 62.1 | 72.96 | 1,085 | rtx4090* | 150 | 16% |
| 17 | sn4 Targon | 58.1 | 10,663 | 31,472 | rtx4090* | 4 | 72% |
| 18 | sn78 Umi | 57.9 | 26.46 | 90.60 | rtx4090* | 21 | 30% |
| 19 | sn6 Numinous | 57.9 | 23.19 | 227 | rtx4090* | 37 | 14% |
| 20 | sn120 Affine | 57.8 | 31,788 | 31,788 = | rtx4090* | 1 | 100% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 20 |
| captured (>90%) | 27 |

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
| 2026-10-28T15:18 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #165 from conjectures-i |
| 2026-10-28T15:18 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Preserve verified captures and retry tran |
| 2026-10-28T15:18 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: Merge pull request #21 from taostatus/fe |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

