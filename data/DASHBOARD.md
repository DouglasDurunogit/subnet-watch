# Subnet watch — dashboard

_snapshot 2026-10-28T08:21:19Z · block 9381007 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.6 | 2,173 | 4,354 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73.2 | 1,914 | 1,914 = | rtx4090* | 5 | 20% |
| 3 | sn34 Yugos | 71.1 | 1,031 | 8,733 | rtx4090* | 3 | 85% |
| 4 | sn91 cascade | 70.7 | 919 | 1,846 | rtx4090* | 5 | 52% |
| 5 | sn103 Terza Inference | 70.5 | 852 | 1,497 | rtx4090* | 4 | 52% |
| 6 | sn60 Bitsec.ai | 69.9 | 276 | 276 = | cpu-small | 3 | 50% |
| 7 | sn56 Gradients | 68.8 | 515 | 5,645 | rtx4090* | 6 | 51% |
| 8 | sn46 Instant | 68.5 | 184 | 198 | cpu-small | 8 | 45% |
| 9 | sn1 Apex | 68.1 | 420 | 844 | rtx4090* | 5 | 59% |
| 10 | sn107 Minos | 66.9 | 218 | 18,572 | cpu-small | 20 | 80% |
| 11 | sn67 Harnyx | 66.9 | 5.71 | 339 | cpu-small | 150 | 16% |
| 12 | sn15 ORO | 66.5 | 7.16 | 14,966 | cpu-small | 62 | 97% |
| 13 | sn125 Refinery | 65.4 | 189 | 883 | rtx4090* | 4 | 50% |
| 14 | sn120 Affine | 63.7 | 128 | 899 | rtx4090* | 162 | 3% |
| 15 | sn66 conjectures | 63.4 | 104 | 217 | rtx4090* | 4 | 80% |
| 16 | sn62 Ridges | 62.7 | 82.18 | 915 | rtx4090* | 44 | 15% |
| 17 | sn23 Trishool | 62.5 | 1,072 | 1,072 = | cpu-small | 2 | 80% |
| 18 | sn14 Cacheon | 60.8 | 1,678 | 4,318 | rtx4090* | 3 | 65% |
| 19 | sn28 SayGM | 60.7 | 49.81 | 810 | rtx4090* | 145 | 43% |
| 20 | sn6 Numinous | 60.6 | 49.74 | 167 | rtx4090* | 30 | 11% |

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
| dominated (60–90%) | 22 |
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
| 2026-10-28T08:21 | sn1 | RELEASE | sn1 released v4.5.1 |
| 2026-10-28T08:21 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Document wording gate enforcement for new |
| 2026-10-28T08:21 | sn51 | RELEASE | sn51 released lium-protocol-v1.17.0 |
| 2026-10-28T08:21 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5037 - [P1] Validator: attach a defau |
| 2026-10-28T08:21 | sn62 | RELEASE | sn62 released v0.3.14 |
| 2026-10-28T08:21 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #532 from ridgesai/fea |
| 2026-10-28T08:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified pre-dispatch errors in  |
| 2026-10-28T08:21 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #460 from Umi-BitSign/ |
| 2026-10-28T08:21 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(eval): the auditor passes observe to  |
| 2026-10-28T01:48 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #27 from BitMind-AI/fe |
| 2026-10-28T01:48 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: docs: update Discord invite link |
| 2026-10-28T01:48 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #381 from TensorLink-A |
| 2026-10-28T01:48 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Require AMD-verified attestation before p |
| 2026-10-27T22:29 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: MinerAccountManager: one lock order (accou |
| 2026-10-27T22:29 | sn51 | RELEASE | sn51 released executor-v1.157 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

