# Subnet watch — dashboard

_snapshot 2026-08-25T21:11:04Z · block 8924624 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 79.9 | 156 | 351 | cpu-small | 13 | 20% |
| 2 | sn11 TrajectoryRL | 79.4 | 4,775 | 4,775 = | cpu-small | 1 | 100% |
| 3 | sn60 Bitsec.ai | 75.9 | 1,653 | 1,653 = | cpu-small | 2 | 50% |
| 4 | sn3 Teutonic | 75.6 | 3,885 | 3,885 = | rtx4090* | 5 | 20% |
| 5 | sn62 Ridges | 72.1 | 1,398 | 2,859 | rtx4090* | 6 | 39% |
| 6 | sn23 Trishool | 72 | 524 | 524 = | cpu-small | 2 | 80% |
| 7 | sn67 Harnyx | 71.5 | 18.22 | 436 | cpu-small | 143 | 12% |
| 8 | sn38 ChronoLLM | 71.1 | 406 | 1,572 | cpu-small | 6 | 53% |
| 9 | sn15 ORO | 70.9 | 22.40 | 38.75 | cpu-small | 91 | 91% |
| 10 | sn102 ConnitoAI | 70.7 | 920 | 2,807 | rtx4090* | 6 | 43% |
| 11 | sn91 cascade | 69.8 | 703 | 2,836 | rtx4090* | 5 | 52% |
| 12 | sn26 Perturb | 67.5 | 18.00 | 258 | rtx3060 | 10 | 70% |
| 13 | sn124 Swarm | 66.5 | 275 | 818 | rtx4090* | 25 | 10% |
| 14 | sn1 Apex | 66.1 | 228 | 2,018 | rtx4090* | 4 | 52% |
| 15 | sn92 MicroTensor | 65.6 | 78.10 | 126 | cpu-small | 3 | 95% |
| 16 | sn107 Minos | 64.8 | 135 | 39,535 | cpu-small | 20 | 90% |
| 17 | sn21 AdTAO | 64.6 | 4.12 | 932 | cpu-small | 16 | 37% |
| 18 | sn108 Prometheon | 63.2 | 98.46 | 111 | rtx4090* | 9 | 66% |
| 19 | sn81 Reliquary | 63 | 91.95 | 331 | rtx4090* | 39 | 8% |
| 20 | sn121 sundae_bar | 62.9 | 1,203 | 1,203 = | cpu-small | 2 | 60% |

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
| 2026-08-25T20:41 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(anchor): a validator with no archive |
| 2026-08-25T19:55 | sn28 | RELEASE | sn28 released v0.4.10-dev |
| 2026-08-25T18:17 | sn15 | RELEASE | sn15 released v1.2.8 |
| 2026-08-25T17:05 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: docs: align discriminator taxonomy and sc |
| 2026-08-25T17:05 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Unwrap fenced JSON before strict entity v |
| 2026-08-25T16:08 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Merge pull request #49 from TrishoolAI/fe |
| 2026-08-25T16:08 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Score entity extraction with dataset-leve |
| 2026-08-25T16:08 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(scoring): drop the note about asser |
| 2026-08-25T15:14 | sn25 | RELEASE | sn25 released v2026.8.25-1028682810 |
| 2026-08-25T15:14 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: fix(evaluation): recover from out of mem |
| 2026-08-25T14:13 | sn102 | RELEASE | sn102 released v0.5.2 — background-eval resume + validator memory fixe |
| 2026-08-25T14:13 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.657 - miners can earn again |
| 2026-08-25T13:08 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Note the operator-driven submission windo |
| 2026-08-25T11:14 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(chain): validator-side set_weights w |
| 2026-08-25T11:14 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

