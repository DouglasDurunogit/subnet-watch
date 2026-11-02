# Subnet watch — dashboard

_snapshot 2026-11-02T19:39:37Z · block 9420393 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 18 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,771 | 2,771 = | rtx4090* | 10 | 10% |
| 2 | sn14 Cacheon | 73.3 | 1,991 | 3,536 | rtx4090* | 3 | 57% |
| 3 | sn3 Teutonic | 73 | 1,834 | 1,834 = | rtx4090* | 7 | 25% |
| 4 | sn97 Ingot | 72.5 | 1,551 | 1,551 = | rtx4090* | 5 | 20% |
| 5 | sn67 Harnyx | 69.8 | 11.55 | 172 | cpu-small | 128 | 9% |
| 6 | sn103 Terza Inference | 68.7 | 508 | 1,667 | rtx4090* | 5 | 38% |
| 7 | sn53 engy | 67.6 | 364 | 1,979 | rtx4090 | 29 | 26% |
| 8 | sn1 Apex | 67.5 | 355 | 702 | rtx4090* | 4 | 68% |
| 9 | sn107 Minos | 65.7 | 165 | 14,046 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 65.7 | 6.09 | 11,188 | cpu-small | 80 | 95% |
| 11 | sn102 ConnitoAI | 65.1 | 174 | 754 | rtx4090* | 7 | 25% |
| 12 | sn125 Refinery | 64 | 123 | 762 | rtx4090* | 4 | 50% |
| 13 | sn38 ChronoLLM | 63.3 | 50.20 | 448 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 62.1 | 78.74 | 1,793 | rtx4090* | 15 | 31% |
| 15 | sn121 sundae_bar | 61.9 | 896 | 896 = | cpu-small | 2 | 60% |
| 16 | sn62 Ridges | 61.5 | 58.56 | 1,388 | rtx4090* | 36 | 25% |
| 17 | sn117 everyframe.studi | 60.8 | 47.55 | 78.86 | rtx4090* | 8 | 93% |
| 18 | sn66 conjectures | 58.6 | 24.15 | 154 | rtx4090* | 6 | 81% |
| 19 | sn60 Bitsec.ai | 57.2 | 221 | 221 = | cpu-small | 3 | 50% |
| 20 | sn80 OpenRoboto | 57.1 | 557 | 1,084 | rtx4090* | 12 | 17% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 26 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-02T19:40 | sn1 | RELEASE | sn1 released v4.6.1 |
| 2026-11-02T19:40 | sn17 | RELEASE | sn17 released witness-diagnostics-20261102 |
| 2026-11-02T19:40 | sn17 | README_TASK_DIFF | sn17 README task/scoring sections changed |
| 2026-11-02T19:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: Performance Max campaigns in MINER_ |
| 2026-11-02T19:40 | sn31 | BURN_DROP | sn31 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-02T19:40 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image in docker-compose. |
| 2026-11-02T19:40 | sn51 | RELEASE | sn51 released lium-protocol-v2.1.0 |
| 2026-11-02T19:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5327 - [P1] Validator re-sends the rm |
| 2026-11-02T19:40 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Fix the challenger dependency review modu |
| 2026-11-02T19:40 | sn66 | RELEASE | sn66 released v2026.11.02.3 |
| 2026-11-02T19:40 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-02T19:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Attribute provider telemetry to validated |
| 2026-11-02T19:40 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat: add retail video training inference |
| 2026-11-02T19:40 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Agent scoreboard: per-algo breakdown with |
| 2026-11-02T19:40 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Miner text: a stage conflict after a rec |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

