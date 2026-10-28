# Subnet watch — dashboard

_snapshot 2026-10-28T15:18:10Z · block 9383092 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn104 TAOstatus | 77.5 | 2,714 | 2,714 = | cpu-small | 1 | 100% |
| 2 | sn3 Teutonic | 73.5 | 2,152 | 4,312 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 73.1 | 1,860 | 1,860 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 71.6 | 1,188 | 2,086 | rtx4090* | 4 | 52% |
| 5 | sn91 cascade | 70.3 | 822 | 1,652 | rtx4090* | 5 | 52% |
| 6 | sn60 Bitsec.ai | 69.7 | 260 | 260 = | cpu-small | 3 | 50% |
| 7 | sn56 Gradients | 68.7 | 506 | 5,545 | rtx4090* | 6 | 51% |
| 8 | sn53 engy | 68.3 | 447 | 2,407 | rtx4090 | 29 | 26% |
| 9 | sn1 Apex | 67.9 | 390 | 885 | rtx4090* | 5 | 59% |
| 10 | sn46 Instant | 67.5 | 136 | 194 | cpu-small | 9 | 45% |
| 11 | sn107 Minos | 66.8 | 214 | 18,140 | cpu-small | 20 | 80% |
| 12 | sn67 Harnyx | 66.8 | 5.58 | 333 | cpu-small | 156 | 16% |
| 13 | sn125 Refinery | 65.4 | 186 | 869 | rtx4090* | 4 | 50% |
| 14 | sn15 ORO | 64.7 | 6.88 | 14.51 | cpu-small | 63 | 97% |
| 15 | sn66 conjectures | 63.4 | 102 | 212 | rtx4090* | 4 | 80% |
| 16 | sn120 Affine | 62.7 | 93.52 | 832 | rtx4090* | 190 | 3% |
| 17 | sn62 Ridges | 62.6 | 80.58 | 899 | rtx4090* | 44 | 15% |
| 18 | sn23 Trishool | 62.4 | 1,023 | 1,023 = | cpu-small | 2 | 80% |
| 19 | sn28 SayGM | 62.2 | 74.89 | 918 | rtx4090* | 146 | 23% |
| 20 | sn6 Numinous | 60.6 | 48.78 | 165 | rtx4090* | 30 | 11% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 24 |
| captured (>90%) | 24 |

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
| 2026-10-28T15:18 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Verify NEAR's GLM-5.3-Flash attested host |
| 2026-10-28T15:18 | sn32 | SCORING_COMMIT | sn32 commit touches scoring: Bump wandb to 0.31.0 so validator logs re |
| 2026-10-28T15:18 | sn50 | RELEASE | sn50 released v1.15.0 |
| 2026-10-28T15:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5194 - [P1] Validator: key sshd boots |
| 2026-10-28T15:18 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #58 from hanlinai/feat |
| 2026-10-28T15:18 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #165 from conjectures-i |
| 2026-10-28T15:18 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Preserve verified captures and retry tran |
| 2026-10-28T15:18 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: Merge pull request #21 from taostatus/fe |
| 2026-10-28T15:18 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Fix validator task image tag resolution |
| 2026-10-28T08:21 | sn1 | RELEASE | sn1 released v4.5.1 |
| 2026-10-28T08:21 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Document wording gate enforcement for new |
| 2026-10-28T08:21 | sn51 | RELEASE | sn51 released lium-protocol-v1.17.0 |
| 2026-10-28T08:21 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5037 - [P1] Validator: attach a defau |
| 2026-10-28T08:21 | sn62 | RELEASE | sn62 released v0.3.14 |
| 2026-10-28T08:21 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #532 from ridgesai/fea |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

