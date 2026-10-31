# Subnet watch — dashboard

_snapshot 2026-10-31T00:56:04Z · block 9400381 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.2 | 1,956 | 3,921 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 72.8 | 1,701 | 1,701 = | rtx4090* | 5 | 20% |
| 3 | sn103 Terza Inference | 71.6 | 1,179 | 2,197 | rtx4090* | 4 | 43% |
| 4 | sn60 Bitsec.ai | 69.5 | 244 | 244 = | cpu-small | 3 | 50% |
| 5 | sn53 engy | 67.9 | 401 | 2,163 | rtx4090 | 29 | 26% |
| 6 | sn67 Harnyx | 67.8 | 6.97 | 366 | cpu-small | 136 | 18% |
| 7 | sn1 Apex | 67.7 | 372 | 857 | rtx4090* | 5 | 61% |
| 8 | sn91 cascade | 67.6 | 367 | 1,491 | rtx4090* | 5 | 52% |
| 9 | sn15 ORO | 67 | 7.08 | 12,677 | cpu-small | 70 | 96% |
| 10 | sn102 ConnitoAI | 65.9 | 221 | 677 | rtx4090* | 10 | 25% |
| 11 | sn107 Minos | 65.8 | 168 | 14,275 | cpu-small | 20 | 80% |
| 12 | sn125 Refinery | 64.7 | 153 | 828 | rtx4090* | 4 | 50% |
| 13 | sn120 Affine | 62.7 | 2,913 | 2,913 = | rtx4090* | 10 | 10% |
| 14 | sn121 sundae_bar | 62.2 | 966 | 966 = | cpu-small | 2 | 60% |
| 15 | sn62 Ridges | 62 | 67.84 | 712 | rtx4090* | 44 | 15% |
| 16 | sn124 Swarm | 61.7 | 70.68 | 218 | rtx4090* | 11 | 85% |
| 17 | sn66 conjectures | 58.9 | 25.83 | 162 | rtx4090* | 7 | 80% |
| 18 | sn4 Targon | 58.4 | 11,550 | 25,865 | rtx4090* | 4 | 64% |
| 19 | sn58 Attune | 57.2 | 578 | 929 | rtx4090* | 5 | 70% |
| 20 | sn56 Gradients | 56.6 | 475 | 1,293 | rtx4090* | 6 | 51% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 25 |
| captured (>90%) | 26 |

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
| 2026-10-31T00:56 | sn25 | RELEASE | sn25 released v2026.10.30-1086064830 |
| 2026-10-31T00:56 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add quality-gated CPU efficiency rewards  |
| 2026-10-31T00:56 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: bench data: a completion marker only for  |
| 2026-10-31T00:56 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: MINING: help contact is the owner's Tele |
| 2026-10-30T21:08 | sn15 | RELEASE | sn15 released v3.0.6: fix(validator): keep sandbox output from blockin |
| 2026-10-30T21:08 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): keep sandbox output from  |
| 2026-10-30T21:08 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Require verified empty EMA prior for head |
| 2026-10-30T21:08 | sn76 | BURN_DROP | sn76 burn fell 0.993 -> 0.964 - miners can earn again |
| 2026-10-30T21:08 | sn117 | RELEASE | sn117 released everycli v0.8.2 |
| 2026-10-30T21:08 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: Document the combined v0.8.2 miner and C |
| 2026-10-30T16:41 | sn28 | RELEASE | sn28 released v0.5.16 |
| 2026-10-30T16:41 | sn51 | RELEASE | sn51 released lium-protocol-v1.18.0 |
| 2026-10-30T16:41 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5393 - [P0] Validator: a full set of  |
| 2026-10-30T16:41 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #59 from hanlinai/feat |
| 2026-10-30T16:41 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: score all candidates |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

