# Subnet watch — dashboard

_snapshot 2026-08-22T19:45:06Z · block 8902594 · run_status **ok**_

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
| 1 | sn76 Phylax | 77.1 | 76.24 | 135 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 72.9 | 1,776 | 1,777 | rtx4090* | 4 | 25% |
| 3 | sn67 Harnyx | 72.4 | 23.24 | 120 | cpu-small | 151 | 12% |
| 4 | sn62 Ridges | 71.7 | 1,229 | 3,026 | rtx4090* | 6 | 39% |
| 5 | sn15 ORO | 70.6 | 19.40 | 23,098 | cpu-small | 61 | 95% |
| 6 | sn56 Gradients | 70 | 739 | 1,088 | rtx4090* | 5 | 73% |
| 7 | sn91 cascade | 69.8 | 705 | 2,845 | rtx4090* | 5 | 52% |
| 8 | sn1 Apex | 68.7 | 502 | 1,283 | rtx4090* | 5 | 52% |
| 9 | sn96 Verathos | 67.6 | 18.42 | 440 | rtx4090 | 90 | 40% |
| 10 | sn26 Perturb | 67.5 | 18.20 | 260 | rtx3060 | 10 | 70% |
| 11 | sn38 ChronoLLM | 66.6 | 116 | 1,588 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.5 | 156 | 43,805 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 64.3 | 135 | 408 | rtx4090* | 13 | 42% |
| 14 | sn108 Prometheon | 63.9 | 120 | 130 | rtx4090* | 8 | 66% |
| 15 | sn81 Reliquary | 63.7 | 113 | 226 | rtx4090* | 39 | 5% |
| 16 | sn51 lium.io | 61.5 | 67.14 | 4,470 | rtx4090* | 51 | 69% |
| 17 | sn28 gm | 60.1 | 39.46 | 1,909 | rtx4090* | 53 | 17% |
| 18 | sn60 Bitsec.ai | 59.8 | 482 | 482 = | cpu-small | 3 | 50% |
| 19 | sn53 engy | 59.4 | 30.68 | 210 | rtx4090 | 144 | 63% |
| 20 | sn61 RedTeam | 57.8 | 18.39 | 287 | rtx4090* | 87 | 6% |

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

