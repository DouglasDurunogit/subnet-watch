# Subnet watch — dashboard

_snapshot 2026-10-26T11:28:02Z · block 9367541 · run_status **ok**_

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
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.4 | 2,091 | 4,191 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,795 | 1,795 = | rtx4090* | 5 | 20% |
| 3 | sn56 Gradients | 71.1 | 1,036 | 5,609 | rtx4090* | 6 | 51% |
| 4 | sn46 Instant | 69.2 | 230 | 287 | cpu-small | 6 | 43% |
| 5 | sn1 Apex | 68 | 409 | 874 | rtx4090* | 5 | 56% |
| 6 | sn82 Noah | 67.8 | 563 | 569 | rtx4090* | 63 | 2% |
| 7 | sn41 Almanac | 67.8 | 8.30 | 134 | cpu-small | 160 | 2% |
| 8 | sn67 Harnyx | 67.7 | 7.21 | 211 | cpu-small | 122 | 10% |
| 9 | sn107 Minos | 66.9 | 216 | 17,997 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 65.7 | 6.86 | 14,728 | cpu-small | 55 | 97% |
| 11 | sn104 TAOstatus | 65.6 | 2,690 | 2,690 = | cpu-small | 1 | 100% |
| 12 | sn120 Affine | 63.9 | 138 | 1,411 | rtx4090* | 137 | 5% |
| 13 | sn66 conjectures | 63.3 | 101 | 196 | rtx4090* | 4 | 81% |
| 14 | sn62 Ridges | 62.6 | 81.76 | 911 | rtx4090* | 44 | 15% |
| 15 | sn23 Trishool | 62.5 | 1,056 | 1,056 = | cpu-small | 2 | 80% |
| 16 | sn91 cascade | 61.6 | 806 | 1,613 | cpu-small | 5 | 52% |
| 17 | sn28 SayGM | 61.3 | 55.90 | 2,099 | rtx4090* | 139 | 33% |
| 18 | sn34 BitMind | 59.9 | 8,390 | 8,390 = | a100-80 | 3 | 85% |
| 19 | sn81 Reliquary | 59 | 27.17 | 356 | rtx4090* | 41 | 39% |
| 20 | sn111 Claims | 58.9 | 27.28 | 2,656 | rtx4090* | 6 | 90% |

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
| dominated (60–90%) | 23 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-26T11:28 | sn9 | RELEASE | sn9 released v4.13.9 |
| 2026-10-26T11:28 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: chore(validators): one upload schema and  |
| 2026-10-26T11:28 | sn51 | RELEASE | sn51 released executor-v1.155 |
| 2026-10-26T11:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5075 - [P0] Central miner: retry an e |
| 2026-10-26T11:28 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-26T11:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #794 from leadpoet/fix |
| 2026-10-26T11:28 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Bound native HD suite decode threads with |
| 2026-10-26T11:28 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(validator): name every declared card |
| 2026-10-26T11:28 | sn92 | RELEASE | sn92 released v1.2.0-rc11.post7 |
| 2026-10-26T11:28 | sn123 | SCORING_COMMIT | sn123 commit touches scoring: Update validator.py |
| 2026-10-26T05:27 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4568 - [P1] Remove the GPU alias flag |
| 2026-10-26T05:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Classify verified provider output failure |
| 2026-10-26T05:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Expose native checkpoint metadata progres |
| 2026-10-26T00:45 | sn25 | RELEASE | sn25 released v2026.10.25-1081686250 |
| 2026-10-26T00:45 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Project the verified retained predecessor |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

