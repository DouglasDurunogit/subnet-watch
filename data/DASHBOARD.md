# Subnet watch — dashboard

_snapshot 2026-08-23T20:35:21Z · block 8910046 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.1 | 77.10 | 86.31 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 73 | 1,809 | 1,809 = | rtx4090* | 4 | 25% |
| 3 | sn67 Harnyx | 73 | 26.16 | 838 | cpu-small | 125 | 20% |
| 4 | sn62 Ridges | 72.5 | 1,576 | 3,220 | rtx4090* | 6 | 39% |
| 5 | sn23 Trishool | 72.5 | 604 | 604 = | cpu-small | 2 | 80% |
| 6 | sn15 ORO | 72.1 | 27.83 | 47.54 | cpu-small | 80 | 93% |
| 7 | sn56 Gradients | 70 | 742 | 1,166 | rtx4090* | 5 | 73% |
| 8 | sn91 cascade | 70 | 741 | 2,988 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 69 | 547 | 1,234 | rtx4090* | 5 | 55% |
| 10 | sn96 Verathos | 68.6 | 23.98 | 303 | rtx4090 | 90 | 40% |
| 11 | sn26 Perturb | 67.8 | 19.72 | 280 | rtx3060 | 10 | 70% |
| 12 | sn124 Swarm | 66.8 | 297 | 2,585 | rtx4090* | 21 | 30% |
| 13 | sn38 ChronoLLM | 66.8 | 123 | 1,679 | cpu-small | 10 | 52% |
| 14 | sn108 Prometheon | 65.5 | 194 | 199 | rtx4090* | 5 | 66% |
| 15 | sn107 Minos | 65.3 | 152 | 45,068 | cpu-small | 20 | 90% |
| 16 | sn81 Reliquary | 65.2 | 178 | 263 | rtx4090* | 30 | 6% |
| 17 | sn85 Vidaio | 64.5 | 144 | 447 | rtx4090* | 13 | 42% |
| 18 | sn60 Bitsec.ai | 61.9 | 883 | 1,237 | cpu-small | 3 | 50% |
| 19 | sn51 lium.io | 60.8 | 56.39 | 2,081 | rtx4090* | 54 | 73% |
| 20 | sn53 engy | 60.3 | 40.65 | 13,427 | rtx4090 | 144 | 63% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 17 |
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
| 2026-08-23T19:44 | sn102 | RELEASE | sn102 released v0.5.1 — release the finished round on swap |
| 2026-08-23T19:44 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 🩹 fix(validator): release the finished r |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

