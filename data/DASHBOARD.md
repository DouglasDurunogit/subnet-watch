# Subnet watch — dashboard

_snapshot 2026-08-26T05:04:57Z · block 8926994 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
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
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.1 | 165 | 371 | cpu-small | 13 | 20% |
| 2 | sn11 TrajectoryRL | 79.6 | 5,023 | 5,023 = | cpu-small | 1 | 100% |
| 3 | sn60 Bitsec.ai | 76.2 | 1,792 | 1,792 = | cpu-small | 2 | 50% |
| 4 | sn3 Teutonic | 75.6 | 3,977 | 3,977 = | rtx4090* | 5 | 20% |
| 5 | sn23 Trishool | 72.1 | 539 | 539 = | cpu-small | 2 | 80% |
| 6 | sn38 ChronoLLM | 71.2 | 418 | 1,615 | cpu-small | 6 | 53% |
| 7 | sn15 ORO | 71.1 | 23.62 | 40.83 | cpu-small | 91 | 91% |
| 8 | sn67 Harnyx | 70.5 | 14.68 | 253 | cpu-small | 130 | 7% |
| 9 | sn91 cascade | 69.9 | 719 | 2,902 | rtx4090* | 5 | 52% |
| 10 | sn56 Gradients | 69.6 | 663 | 1,095 | rtx4090* | 6 | 73% |
| 11 | sn102 ConnitoAI | 68.4 | 456 | 2,327 | rtx4090* | 7 | 36% |
| 12 | sn26 Perturb | 68.1 | 20.98 | 399 | rtx3060 | 10 | 70% |
| 13 | sn124 Swarm | 66.7 | 284 | 854 | rtx4090* | 25 | 10% |
| 14 | sn21 AdTAO | 66.7 | 6.39 | 1,181 | cpu-small | 16 | 45% |
| 15 | sn92 MicroTensor | 66.1 | 89.67 | 145 | cpu-small | 3 | 95% |
| 16 | sn1 Apex | 66 | 226 | 2,006 | rtx4090* | 4 | 54% |
| 17 | sn107 Minos | 65 | 140 | 41,242 | cpu-small | 20 | 90% |
| 18 | sn81 Reliquary | 63.3 | 100 | 296 | rtx4090* | 37 | 7% |
| 19 | sn121 sundae_bar | 63 | 1,236 | 1,236 = | cpu-small | 2 | 60% |
| 20 | sn108 Prometheon | 62.5 | 80.29 | 206 | rtx4090* | 9 | 29% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 14 |
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
| 2026-08-26T04:09 | sn25 | RELEASE | sn25 released v2026.8.25-1029146630 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

