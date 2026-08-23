# Subnet watch — dashboard

_snapshot 2026-08-23T07:55:44Z · block 8906247 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.7 | 69.91 | 78.07 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.5 | 23.76 | 763 | cpu-small | 121 | 20% |
| 3 | sn23 Trishool | 72.2 | 551 | 551 = | cpu-small | 2 | 80% |
| 4 | sn102 ConnitoAI | 72.1 | 1,385 | 2,778 | rtx4090* | 4 | 41% |
| 5 | sn62 Ridges | 71.6 | 1,192 | 2,935 | rtx4090* | 6 | 39% |
| 6 | sn15 ORO | 70.7 | 21.38 | 39.06 | cpu-small | 77 | 93% |
| 7 | sn56 Gradients | 69.9 | 709 | 1,055 | rtx4090* | 5 | 73% |
| 8 | sn91 cascade | 69.7 | 683 | 2,757 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.5 | 480 | 1,178 | rtx4090* | 5 | 53% |
| 10 | sn96 Verathos | 67.7 | 18.97 | 261 | rtx4090 | 92 | 40% |
| 11 | sn26 Perturb | 67.4 | 17.58 | 253 | rtx3060 | 10 | 70% |
| 12 | sn38 ChronoLLM | 66.4 | 111 | 1,520 | cpu-small | 10 | 52% |
| 13 | sn107 Minos | 65.2 | 145 | 42,282 | cpu-small | 20 | 90% |
| 14 | sn85 Vidaio | 64.4 | 139 | 395 | rtx4090* | 13 | 42% |
| 15 | sn108 Prometheon | 63.8 | 117 | 127 | rtx4090* | 8 | 66% |
| 16 | sn81 Reliquary | 63 | 90.70 | 237 | rtx4090* | 38 | 9% |
| 17 | sn51 lium.io | 61.7 | 70.89 | 4,335 | rtx4090* | 51 | 71% |
| 18 | sn60 Bitsec.ai | 59.8 | 471 | 471 = | cpu-small | 3 | 50% |
| 19 | sn53 engy | 59.7 | 33.92 | 11,577 | rtx4090 | 144 | 63% |
| 20 | sn28 gm | 57.7 | 19.97 | 1,524 | rtx4090* | 53 | 17% |

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

