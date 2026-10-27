# Subnet watch — dashboard

_snapshot 2026-10-27T22:29:01Z · block 9378046 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.6 | 2,167 | 4,238 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73.1 | 1,874 | 1,874 = | rtx4090* | 5 | 20% |
| 3 | sn60 Bitsec.ai | 69.7 | 263 | 263 = | cpu-small | 3 | 52% |
| 4 | sn56 Gradients | 68.7 | 509 | 5,575 | rtx4090* | 6 | 51% |
| 5 | sn1 Apex | 68.1 | 425 | 891 | rtx4090* | 5 | 57% |
| 6 | sn46 Instant | 67.7 | 146 | 172 | cpu-small | 9 | 44% |
| 7 | sn67 Harnyx | 67.6 | 6.72 | 388 | cpu-small | 136 | 18% |
| 8 | sn107 Minos | 66.9 | 218 | 18,512 | cpu-small | 20 | 80% |
| 9 | sn120 Affine | 66.3 | 263 | 1,076 | rtx4090* | 118 | 3% |
| 10 | sn15 ORO | 66.3 | 6.75 | 14.48 | cpu-small | 67 | 97% |
| 11 | sn125 Refinery | 65.8 | 211 | 872 | rtx4090* | 4 | 50% |
| 12 | sn66 conjectures | 63.4 | 102 | 212 | rtx4090* | 4 | 80% |
| 13 | sn62 Ridges | 62.6 | 81.18 | 905 | rtx4090* | 44 | 15% |
| 14 | sn23 Trishool | 62.5 | 1,063 | 1,063 = | cpu-small | 2 | 80% |
| 15 | sn28 SayGM | 62 | 69.49 | 954 | rtx4090* | 142 | 18% |
| 16 | sn6 Numinous | 60.6 | 49.24 | 166 | rtx4090* | 30 | 11% |
| 17 | sn34 Yugos | 59.1 | 1,007 | 8,624 | rtx4090* | 3 | 85% |
| 18 | sn111 Claims | 58.9 | 27.35 | 2,659 | rtx4090* | 6 | 90% |
| 19 | sn78 Umi | 58.5 | 30.23 | 486 | rtx4090* | 21 | 30% |
| 20 | sn5 Hone | 57.5 | 29.55 | 38.26 | rtx4090* | 238 | 1% |

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
| dominated (60–90%) | 25 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
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
| 2026-10-27T18:24 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(rl-async): never charge miners for th |
| 2026-10-27T18:24 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Signals entity accounts: hosted miners as |
| 2026-10-27T12:46 | sn1 | RELEASE | sn1 released v4.5.0 |
| 2026-10-27T12:46 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Gate unverified miner scores and refresh n |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

