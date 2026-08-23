# Subnet watch — dashboard

_snapshot 2026-08-23T05:01:42Z · block 8905377 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
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
| 1 | sn76 Phylax | 76.6 | 68.39 | 76.42 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.5 | 23.48 | 755 | cpu-small | 118 | 20% |
| 3 | sn23 Trishool | 72.1 | 540 | 540 = | cpu-small | 2 | 80% |
| 4 | sn62 Ridges | 71.5 | 1,168 | 2,877 | rtx4090* | 6 | 39% |
| 5 | sn102 ConnitoAI | 71.1 | 1,037 | 2,842 | rtx4090* | 5 | 42% |
| 6 | sn15 ORO | 69.9 | 17.51 | 36.73 | cpu-small | 60 | 95% |
| 7 | sn56 Gradients | 69.8 | 696 | 1,033 | rtx4090* | 5 | 73% |
| 8 | sn91 cascade | 69.7 | 669 | 2,702 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.5 | 476 | 1,167 | rtx4090* | 5 | 53% |
| 10 | sn96 Verathos | 67.5 | 18.20 | 271 | rtx4090 | 92 | 40% |
| 11 | sn26 Perturb | 67.2 | 17.14 | 247 | rtx3060 | 10 | 70% |
| 12 | sn38 ChronoLLM | 66.4 | 109 | 1,489 | cpu-small | 10 | 52% |
| 13 | sn107 Minos | 64.4 | 124 | 41,472 | cpu-small | 19 | 90% |
| 14 | sn98 NeverPlayAlone | 64.3 | 1,845 | 1,845 = | cpu-small | 1 | 100% |
| 15 | sn85 Vidaio | 64.3 | 135 | 387 | rtx4090* | 13 | 42% |
| 16 | sn108 Prometheon | 63.7 | 115 | 124 | rtx4090* | 8 | 66% |
| 17 | sn81 Reliquary | 63 | 92.38 | 229 | rtx4090* | 39 | 10% |
| 18 | sn51 lium.io | 62.2 | 79.74 | 4,216 | rtx4090* | 50 | 71% |
| 19 | sn28 gm | 61 | 51.13 | 1,462 | rtx4090* | 54 | 14% |
| 20 | sn60 Bitsec.ai | 59.8 | 470 | 470 = | cpu-small | 3 | 50% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 21 |
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
| 2026-08-23T05:02 | sn25 | RELEASE | sn25 released v2026.8.22-1026600400 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

