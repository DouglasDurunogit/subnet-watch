# Subnet watch — dashboard

_snapshot 2026-08-24T05:10:50Z · block 8912623 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
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
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77 | 75.64 | 84.67 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 72.9 | 1,733 | 1,734 | rtx4090* | 4 | 25% |
| 3 | sn62 Ridges | 72.4 | 1,503 | 3,073 | rtx4090* | 6 | 39% |
| 4 | sn23 Trishool | 72.3 | 578 | 578 = | cpu-small | 2 | 80% |
| 5 | sn15 ORO | 71.9 | 27.50 | 45.78 | cpu-small | 83 | 92% |
| 6 | sn67 Harnyx | 71.5 | 18.86 | 167 | cpu-small | 160 | 12% |
| 7 | sn56 Gradients | 69.9 | 710 | 1,121 | rtx4090* | 5 | 73% |
| 8 | sn91 cascade | 69.8 | 706 | 2,848 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.8 | 513 | 1,141 | rtx4090* | 5 | 55% |
| 10 | sn96 Verathos | 68 | 20.57 | 265 | rtx4090 | 97 | 41% |
| 11 | sn26 Perturb | 67.6 | 18.86 | 269 | rtx3060 | 10 | 70% |
| 12 | sn11 TrajectoryRL | 67.5 | 4,768 | 4,768 = | cpu-small | 1 | 100% |
| 13 | sn124 Swarm | 66.9 | 301 | 2,620 | rtx4090* | 21 | 30% |
| 14 | sn38 ChronoLLM | 66.6 | 119 | 1,618 | cpu-small | 10 | 52% |
| 15 | sn108 Prometheon | 65.4 | 187 | 191 | rtx4090* | 5 | 66% |
| 16 | sn107 Minos | 65.2 | 147 | 43,617 | cpu-small | 20 | 90% |
| 17 | sn85 Vidaio | 64.6 | 150 | 426 | rtx4090* | 13 | 42% |
| 18 | sn60 Bitsec.ai | 64.1 | 1,712 | 1,712 = | cpu-small | 2 | 50% |
| 19 | sn81 Reliquary | 64 | 125 | 203 | rtx4090* | 38 | 5% |
| 20 | sn51 lium.io | 61.1 | 59.92 | 2,166 | rtx4090* | 53 | 72% |

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
| 2026-08-24T04:14 | sn25 | RELEASE | sn25 released v2026.8.23-1027441210 |
| 2026-08-24T04:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2742: stop transient checks from clea |
| 2026-08-24T03:13 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: withdraw on a health stall tha |
| 2026-08-24T01:55 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: report live KV-cache pressure  |
| 2026-08-23T23:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test: verify pinned model runtime in CI |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

