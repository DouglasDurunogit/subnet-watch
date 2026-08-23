# Subnet watch — dashboard

_snapshot 2026-08-23T18:44:52Z · block 8909493 · run_status **ok**_

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
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77 | 75.46 | 84.47 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.8 | 25.49 | 817 | cpu-small | 125 | 20% |
| 3 | sn23 Trishool | 72.4 | 592 | 592 = | cpu-small | 2 | 80% |
| 4 | sn102 ConnitoAI | 72.1 | 1,381 | 2,578 | rtx4090* | 5 | 36% |
| 5 | sn62 Ridges | 71.8 | 1,284 | 3,161 | rtx4090* | 6 | 39% |
| 6 | sn15 ORO | 71.8 | 27.09 | 46.30 | cpu-small | 80 | 93% |
| 7 | sn56 Gradients | 69.9 | 725 | 1,139 | rtx4090* | 5 | 73% |
| 8 | sn91 cascade | 69 | 558 | 1,503 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.9 | 536 | 1,210 | rtx4090* | 5 | 54% |
| 10 | sn96 Verathos | 68.5 | 23.50 | 307 | rtx4090 | 88 | 40% |
| 11 | sn26 Perturb | 67.7 | 19.19 | 274 | rtx3060 | 10 | 70% |
| 12 | sn124 Swarm | 66.8 | 293 | 2,549 | rtx4090* | 21 | 30% |
| 13 | sn38 ChronoLLM | 66.7 | 120 | 1,637 | cpu-small | 10 | 52% |
| 14 | sn108 Prometheon | 65.5 | 192 | 210 | rtx4090* | 5 | 66% |
| 15 | sn107 Minos | 65.4 | 153 | 43,389 | cpu-small | 20 | 89% |
| 16 | sn81 Reliquary | 64.9 | 162 | 272 | rtx4090* | 36 | 6% |
| 17 | sn85 Vidaio | 64.7 | 152 | 436 | rtx4090* | 13 | 42% |
| 18 | sn51 lium.io | 61.5 | 68.05 | 2,105 | rtx4090* | 53 | 71% |
| 19 | sn53 engy | 60.2 | 38.76 | 12,908 | rtx4090 | 144 | 63% |
| 20 | sn60 Bitsec.ai | 60.1 | 520 | 520 = | cpu-small | 3 | 50% |

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
| captured (>90%) | 24 |

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
| 2026-08-23T18:45 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(setup): add public miner and valida |
| 2026-08-23T18:45 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-08-23T16:38 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: sandbox: authenticate with the sandbox to |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

