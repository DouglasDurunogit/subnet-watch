# Subnet watch — dashboard

_snapshot 2026-08-22T21:02:12Z · block 8902980 · run_status **ok**_

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
| New events this window | 0 | see ALARMS.md |

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
| 1 | sn76 Phylax | 77 | 75.29 | 133 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.4 | 22.95 | 119 | cpu-small | 151 | 12% |
| 3 | sn62 Ridges | 71.7 | 1,214 | 2,990 | rtx4090* | 6 | 39% |
| 4 | sn15 ORO | 70.3 | 19.22 | 22,891 | cpu-small | 61 | 95% |
| 5 | sn56 Gradients | 69.9 | 729 | 1,076 | rtx4090* | 5 | 73% |
| 6 | sn91 cascade | 69.8 | 702 | 2,835 | rtx4090* | 5 | 52% |
| 7 | sn1 Apex | 68.6 | 493 | 1,259 | rtx4090* | 5 | 52% |
| 8 | sn102 ConnitoAI | 68.5 | 479 | 2,303 | rtx4090* | 7 | 33% |
| 9 | sn96 Verathos | 67.8 | 19.55 | 440 | rtx4090 | 91 | 40% |
| 10 | sn26 Perturb | 67.5 | 17.95 | 257 | rtx3060 | 10 | 70% |
| 11 | sn38 ChronoLLM | 66.5 | 115 | 1,569 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.3 | 148 | 42,731 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 64.2 | 129 | 403 | rtx4090* | 13 | 42% |
| 14 | sn108 Prometheon | 63.9 | 119 | 128 | rtx4090* | 8 | 66% |
| 15 | sn81 Reliquary | 63.3 | 98.68 | 221 | rtx4090* | 43 | 5% |
| 16 | sn51 lium.io | 60.9 | 57.36 | 4,332 | rtx4090* | 52 | 69% |
| 17 | sn60 Bitsec.ai | 59.8 | 479 | 479 = | cpu-small | 3 | 50% |
| 18 | sn53 engy | 59.4 | 30.23 | 207 | rtx4090 | 144 | 63% |
| 19 | sn28 gm | 58.9 | 28.06 | 1,603 | rtx4090* | 54 | 15% |
| 20 | sn61 RedTeam | 57.7 | 18.08 | 284 | rtx4090* | 87 | 6% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 20 |
| captured (>90%) | 25 |

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

