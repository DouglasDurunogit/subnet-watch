# Subnet watch — dashboard

_snapshot 2026-08-23T04:08:35Z · block 8905112 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.7 | 68.72 | 76.78 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.3 | 22.16 | 115 | cpu-small | 159 | 12% |
| 3 | sn23 Trishool | 72.1 | 543 | 543 = | cpu-small | 2 | 80% |
| 4 | sn62 Ridges | 71.6 | 1,176 | 2,895 | rtx4090* | 6 | 39% |
| 5 | sn102 ConnitoAI | 71.1 | 1,033 | 2,832 | rtx4090* | 5 | 42% |
| 6 | sn56 Gradients | 69.8 | 701 | 1,040 | rtx4090* | 5 | 73% |
| 7 | sn15 ORO | 69.8 | 17.61 | 36.91 | cpu-small | 60 | 95% |
| 8 | sn91 cascade | 69.7 | 674 | 2,721 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.6 | 481 | 1,180 | rtx4090* | 5 | 53% |
| 10 | sn26 Perturb | 67.3 | 17.26 | 249 | rtx3060 | 10 | 70% |
| 11 | sn96 Verathos | 67.2 | 16.97 | 274 | rtx4090 | 92 | 40% |
| 12 | sn38 ChronoLLM | 66.4 | 110 | 1,498 | cpu-small | 10 | 52% |
| 13 | sn107 Minos | 65 | 141 | 41,551 | cpu-small | 20 | 90% |
| 14 | sn98 NeverPlayAlone | 64.4 | 1,856 | 1,856 = | cpu-small | 1 | 100% |
| 15 | sn85 Vidaio | 64.4 | 139 | 389 | rtx4090* | 13 | 42% |
| 16 | sn108 Prometheon | 63.8 | 116 | 125 | rtx4090* | 8 | 66% |
| 17 | sn81 Reliquary | 63.1 | 94.95 | 233 | rtx4090* | 41 | 9% |
| 18 | sn51 lium.io | 62.2 | 80.27 | 4,239 | rtx4090* | 50 | 71% |
| 19 | sn28 gm | 61 | 51.45 | 1,470 | rtx4090* | 54 | 14% |
| 20 | sn60 Bitsec.ai | 59.7 | 464 | 464 = | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-23T04:09 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: fix: replace MSA prefill score-sheet ABI |
| 2026-08-23T03:13 | sn25 | RELEASE | sn25 released v2026.8.22-1026545240 |
| 2026-08-22T22:00 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(api): app creation accepted code it  |
| 2026-08-22T18:00 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix: train-worker compose must override t |
| 2026-08-22T17:32 | sn25 | RELEASE | sn25 released v2026.8.22-1026185650 |
| 2026-08-22T16:37 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Build the validator registry from the per |
| 2026-08-22T16:00 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat: validator checkpoint intake — stage |
| 2026-08-22T14:35 | sn92 | RELEASE | sn92 released v0.1.14 |
| 2026-08-22T13:41 | sn92 | RELEASE | sn92 released v0.1.13 |
| 2026-08-22T12:57 | sn92 | RELEASE | sn92 released v0.1.11 |
| 2026-08-22T12:57 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Make the validator guide match the code a |
| 2026-08-22T12:01 | sn92 | RELEASE | sn92 released v0.1.9 |
| 2026-08-22T11:32 | sn92 | RELEASE | sn92 released v0.1.7 |
| 2026-08-22T10:36 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #54 from score-technol |
| 2026-08-22T10:36 | sn92 | RELEASE | sn92 released v0.1.6 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

