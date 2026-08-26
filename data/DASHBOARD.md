# Subnet watch — dashboard

_snapshot 2026-08-26T01:54:59Z · block 8926044 · run_status **ok**_

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
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.1 | 165 | 371 | cpu-small | 13 | 20% |
| 2 | sn11 TrajectoryRL | 79.6 | 5,032 | 5,032 = | cpu-small | 1 | 100% |
| 3 | sn3 Teutonic | 75.7 | 4,033 | 4,033 = | rtx4090* | 5 | 20% |
| 4 | sn23 Trishool | 72.1 | 545 | 545 = | cpu-small | 2 | 80% |
| 5 | sn67 Harnyx | 71.6 | 18.67 | 447 | cpu-small | 143 | 12% |
| 6 | sn38 ChronoLLM | 71.1 | 417 | 1,613 | cpu-small | 6 | 53% |
| 7 | sn15 ORO | 71 | 23.31 | 40.30 | cpu-small | 91 | 91% |
| 8 | sn91 cascade | 69.9 | 725 | 2,925 | rtx4090* | 5 | 52% |
| 9 | sn56 Gradients | 69.6 | 662 | 1,094 | rtx4090* | 6 | 73% |
| 10 | sn26 Perturb | 68.1 | 20.94 | 399 | rtx3060 | 10 | 70% |
| 11 | sn124 Swarm | 66.7 | 284 | 855 | rtx4090* | 25 | 10% |
| 12 | sn21 AdTAO | 66.7 | 6.34 | 1,173 | cpu-small | 16 | 45% |
| 13 | sn1 Apex | 66.1 | 229 | 2,034 | rtx4090* | 4 | 53% |
| 14 | sn92 MicroTensor | 66.1 | 91.60 | 148 | cpu-small | 3 | 95% |
| 15 | sn107 Minos | 64.9 | 138 | 40,235 | cpu-small | 20 | 90% |
| 16 | sn81 Reliquary | 63.8 | 117 | 265 | rtx4090* | 38 | 6% |
| 17 | sn121 sundae_bar | 63 | 1,234 | 1,234 = | cpu-small | 2 | 60% |
| 18 | sn108 Prometheon | 62.3 | 74.35 | 208 | rtx4090* | 9 | 29% |
| 19 | sn61 RedTeam | 61.1 | 51.68 | 220 | rtx4090* | 80 | 5% |
| 20 | sn102 ConnitoAI | 60.7 | 46.38 | 2,071 | rtx4090* | 8 | 31% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 17 |
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
| 2026-08-26T01:55 | sn25 | RELEASE | sn25 released v2026.8.25-1029027010 |
| 2026-08-26T01:55 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): close submission ingress  |
| 2026-08-25T23:10 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Add unit tests for get_base_contestant to |
| 2026-08-25T23:10 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(scoring): plan.metadata is not alway |
| 2026-08-25T21:53 | sn28 | RELEASE | sn28 released v0.4.10 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

