# Subnet watch — dashboard

_snapshot 2026-08-23T14:02:41Z · block 8908082 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.9 | 73.54 | 82.33 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.7 | 24.88 | 798 | cpu-small | 124 | 20% |
| 3 | sn23 Trishool | 72.3 | 570 | 570 = | cpu-small | 2 | 80% |
| 4 | sn15 ORO | 71.2 | 23.69 | 41.81 | cpu-small | 78 | 93% |
| 5 | sn56 Gradients | 70 | 743 | 1,110 | rtx4090* | 5 | 73% |
| 6 | sn91 cascade | 68.9 | 539 | 1,452 | rtx4090* | 5 | 52% |
| 7 | sn1 Apex | 68.6 | 492 | 1,205 | rtx4090* | 5 | 55% |
| 8 | sn96 Verathos | 68.2 | 21.66 | 273 | rtx4090 | 91 | 40% |
| 9 | sn26 Perturb | 67.6 | 18.67 | 266 | rtx3060 | 10 | 70% |
| 10 | sn124 Swarm | 66.7 | 283 | 2,465 | rtx4090* | 21 | 30% |
| 11 | sn38 ChronoLLM | 66.6 | 117 | 1,596 | cpu-small | 10 | 52% |
| 12 | sn108 Prometheon | 65.4 | 186 | 204 | rtx4090* | 5 | 66% |
| 13 | sn107 Minos | 65.2 | 146 | 43,930 | cpu-small | 20 | 90% |
| 14 | sn85 Vidaio | 64.5 | 143 | 425 | rtx4090* | 13 | 42% |
| 15 | sn81 Reliquary | 63.5 | 106 | 252 | rtx4090* | 38 | 7% |
| 16 | sn51 lium.io | 61.3 | 63.74 | 4,451 | rtx4090* | 53 | 71% |
| 17 | sn102 ConnitoAI | 61.1 | 51.96 | 2,913 | rtx4090* | 6 | 42% |
| 18 | sn53 engy | 60.2 | 38.52 | 12,841 | rtx4090 | 144 | 63% |
| 19 | sn60 Bitsec.ai | 60 | 505 | 505 = | cpu-small | 3 | 50% |
| 20 | sn28 gm | 59.2 | 31.09 | 1,612 | rtx4090* | 55 | 22% |

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
| dominated (60–90%) | 18 |
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
| 2026-08-23T13:42 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(sn28): announce recycler and how to  |
| 2026-08-23T12:59 | sn90 | RELEASE | sn90 released v1.1.6 — subtensor v445 / typed metagraph APIs |
| 2026-08-23T12:59 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: chore(validator): release v1.1.6 |
| 2026-08-23T12:59 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Remove obsolete repo verify flag from do |
| 2026-08-23T12:00 | sn14 | RELEASE | sn14 released msa-block-score-control-20260823: fix: open paged MSA de |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

