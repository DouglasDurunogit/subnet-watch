# Subnet watch — dashboard

_snapshot 2026-10-28T01:48:11Z · block 9379042 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,145 | 4,403 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73.2 | 1,927 | 1,927 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 70.8 | 933 | 1,875 | rtx4090* | 5 | 52% |
| 4 | sn60 Bitsec.ai | 69.9 | 278 | 278 = | cpu-small | 3 | 50% |
| 5 | sn56 Gradients | 68.8 | 515 | 5,646 | rtx4090* | 6 | 51% |
| 6 | sn1 Apex | 68.1 | 423 | 887 | rtx4090* | 5 | 57% |
| 7 | sn67 Harnyx | 67.6 | 6.82 | 393 | cpu-small | 136 | 18% |
| 8 | sn46 Instant | 67.4 | 134 | 248 | cpu-small | 9 | 44% |
| 9 | sn107 Minos | 67 | 221 | 18,768 | cpu-small | 20 | 80% |
| 10 | sn120 Affine | 66.4 | 265 | 1,084 | rtx4090* | 117 | 3% |
| 11 | sn125 Refinery | 65.8 | 214 | 883 | rtx4090* | 4 | 50% |
| 12 | sn15 ORO | 65.8 | 6.49 | 13.97 | cpu-small | 66 | 97% |
| 13 | sn66 conjectures | 63.4 | 103 | 215 | rtx4090* | 4 | 80% |
| 14 | sn62 Ridges | 62.7 | 82.30 | 917 | rtx4090* | 44 | 15% |
| 15 | sn23 Trishool | 62.5 | 1,072 | 1,072 = | cpu-small | 2 | 80% |
| 16 | sn28 SayGM | 62.4 | 81.20 | 986 | rtx4090* | 142 | 18% |
| 17 | sn6 Numinous | 60.5 | 49.76 | 168 | rtx4090* | 30 | 11% |
| 18 | sn111 Claims | 59 | 27.80 | 2,693 | rtx4090* | 6 | 90% |
| 19 | sn78 Umi | 58.3 | 28.92 | 469 | rtx4090* | 21 | 30% |
| 20 | sn58 Attune | 57.5 | 622 | 1,000 | rtx4090* | 5 | 70% |

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
| 2026-10-28T01:48 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #27 from BitMind-AI/fe |
| 2026-10-28T01:48 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: docs: update Discord invite link |
| 2026-10-28T01:48 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #381 from TensorLink-A |
| 2026-10-28T01:48 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Require AMD-verified attestation before p |
| 2026-10-27T22:29 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: MinerAccountManager: one lock order (accou |
| 2026-10-27T22:29 | sn51 | RELEASE | sn51 released executor-v1.157 |
| 2026-10-27T22:29 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: docs: scope Tyche capture verification an |
| 2026-10-27T22:29 | sn92 | RELEASE | sn92 released v1.2.0-rc11.post8.1 |
| 2026-10-27T22:29 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: 1.2.0rc11.post8.1: validator release for  |
| 2026-10-27T18:24 | sn9 | RELEASE | sn9 released v4.13.10 |
| 2026-10-27T18:24 | sn25 | RELEASE | sn25 released v2026.10.27-1083160450 |
| 2026-10-27T18:24 | sn33 | SCORING_COMMIT | sn33 commit touches scoring: Enable 25% burn and shuffle task dispatch |
| 2026-10-27T18:24 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: fix(validator): resync the metagraph afte |
| 2026-10-27T18:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record verified SSM cutover and permanent |
| 2026-10-27T18:24 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Cap C7+ evaluation sources and preserve h |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

