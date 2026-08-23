# Subnet watch — dashboard

_snapshot 2026-08-23T09:51:47Z · block 8906828 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
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
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.8 | 70.51 | 79.56 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 72.8 | 1,729 | 1,729 | rtx4090* | 4 | 25% |
| 3 | sn67 Harnyx | 72.6 | 24.05 | 772 | cpu-small | 124 | 20% |
| 4 | sn23 Trishool | 72.2 | 559 | 559 = | cpu-small | 2 | 80% |
| 5 | sn15 ORO | 71.1 | 22.18 | 39.19 | cpu-small | 78 | 93% |
| 6 | sn56 Gradients | 69.9 | 718 | 1,070 | rtx4090* | 5 | 73% |
| 7 | sn91 cascade | 69.8 | 693 | 2,798 | rtx4090* | 5 | 52% |
| 8 | sn1 Apex | 68.6 | 483 | 1,185 | rtx4090* | 5 | 54% |
| 9 | sn96 Verathos | 68 | 20.45 | 271 | rtx4090 | 91 | 40% |
| 10 | sn26 Perturb | 67.4 | 17.85 | 256 | rtx3060 | 10 | 70% |
| 11 | sn38 ChronoLLM | 66.5 | 113 | 1,547 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.1 | 146 | 42,167 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 64.4 | 140 | 410 | rtx4090* | 13 | 42% |
| 14 | sn108 Prometheon | 63.9 | 119 | 129 | rtx4090* | 8 | 66% |
| 15 | sn81 Reliquary | 63.4 | 104 | 235 | rtx4090* | 38 | 8% |
| 16 | sn51 lium.io | 61.5 | 66.31 | 4,362 | rtx4090* | 52 | 71% |
| 17 | sn60 Bitsec.ai | 59.9 | 490 | 490 = | cpu-small | 3 | 50% |
| 18 | sn53 engy | 59.9 | 35.12 | 11,908 | rtx4090 | 144 | 63% |
| 19 | sn28 gm | 58.2 | 22.66 | 1,397 | rtx4090* | 53 | 19% |
| 20 | sn61 RedTeam | 57 | 14.30 | 309 | rtx4090* | 85 | 7% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
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
| 2026-08-23T07:10 | sn14 | RELEASE | sn14 released MSA block-score mainnet control |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

