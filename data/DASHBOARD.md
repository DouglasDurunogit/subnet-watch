# Subnet watch — dashboard

_snapshot 2026-08-22T18:45:46Z · block 8902298 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
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
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77 | 75.38 | 134 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 72.8 | 1,728 | 1,728 | rtx4090* | 4 | 25% |
| 3 | sn67 Harnyx | 72.4 | 22.96 | 119 | cpu-small | 151 | 12% |
| 4 | sn62 Ridges | 71.7 | 1,215 | 2,991 | rtx4090* | 6 | 39% |
| 5 | sn56 Gradients | 70 | 731 | 1,076 | rtx4090* | 5 | 73% |
| 6 | sn15 ORO | 70 | 18.86 | 22,491 | cpu-small | 61 | 95% |
| 7 | sn91 cascade | 69.8 | 703 | 2,764 | rtx4090* | 5 | 51% |
| 8 | sn1 Apex | 68.7 | 498 | 1,272 | rtx4090* | 5 | 52% |
| 9 | sn26 Perturb | 67.5 | 17.96 | 257 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 67.4 | 17.87 | 442 | rtx4090 | 92 | 40% |
| 11 | sn38 ChronoLLM | 66.5 | 115 | 1,569 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65 | 141 | 43,882 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 64.2 | 130 | 405 | rtx4090* | 13 | 42% |
| 14 | sn108 Prometheon | 63.9 | 119 | 129 | rtx4090* | 8 | 66% |
| 15 | sn81 Reliquary | 63.8 | 115 | 212 | rtx4090* | 39 | 5% |
| 16 | sn51 lium.io | 61.4 | 64.66 | 4,456 | rtx4090* | 51 | 69% |
| 17 | sn60 Bitsec.ai | 59.8 | 480 | 480 = | cpu-small | 3 | 50% |
| 18 | sn53 engy | 59.4 | 30.61 | 209 | rtx4090 | 144 | 63% |
| 19 | sn61 RedTeam | 57.7 | 17.99 | 281 | rtx4090* | 87 | 6% |
| 20 | sn28 gm | 57.5 | 19.05 | 1,503 | rtx4090* | 55 | 14% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 19 |
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
| 2026-08-22T09:13 | sn92 | RELEASE | sn92 released v0.1.4 |
| 2026-08-22T08:45 | sn92 | RELEASE | sn92 released v0.1.3 |
| 2026-08-22T08:03 | sn61 | RELEASE | sn61 released 4.9.7 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

