# Subnet watch — dashboard

_snapshot 2026-08-26T16:05:48Z · block 8930298 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.4 | 178 | 399 | cpu-small | 13 | 20% |
| 2 | sn60 Bitsec.ai | 76.2 | 1,797 | 1,797 = | cpu-small | 2 | 50% |
| 3 | sn3 Teutonic | 75.4 | 3,738 | 3,738 = | rtx4090* | 5 | 20% |
| 4 | sn102 ConnitoAI | 73 | 1,829 | 2,198 | rtx4090* | 4 | 33% |
| 5 | sn23 Trishool | 72.1 | 531 | 531 = | cpu-small | 2 | 80% |
| 6 | sn38 ChronoLLM | 71.1 | 407 | 1,575 | cpu-small | 6 | 53% |
| 7 | sn15 ORO | 70.6 | 22.42 | 42.43 | cpu-small | 95 | 92% |
| 8 | sn67 Harnyx | 70.3 | 14.03 | 250 | cpu-small | 138 | 7% |
| 9 | sn1 Apex | 70 | 746 | 1,150 | rtx4090* | 4 | 59% |
| 10 | sn91 cascade | 69.8 | 695 | 2,804 | rtx4090* | 5 | 52% |
| 11 | sn56 Gradients | 69.5 | 637 | 1,050 | rtx4090* | 6 | 74% |
| 12 | sn26 Perturb | 68 | 20.53 | 392 | rtx3060 | 10 | 70% |
| 13 | sn124 Swarm | 66.6 | 280 | 844 | rtx4090* | 25 | 10% |
| 14 | sn61 RedTeam | 65.1 | 170 | 258 | rtx4090* | 29 | 5% |
| 15 | sn107 Minos | 64.8 | 132 | 39,404 | cpu-small | 20 | 90% |
| 16 | sn81 Reliquary | 62.7 | 84.09 | 285 | rtx4090* | 45 | 7% |
| 17 | sn108 Prometheon | 62.5 | 78.54 | 202 | rtx4090* | 9 | 29% |
| 18 | sn28 gm | 61.7 | 63.67 | 1,446 | rtx4090* | 37 | 36% |
| 19 | sn21 AdTAO | 59.4 | 1.68 | 1,146 | cpu-small | 16 | 45% |
| 20 | sn51 lium.io | 58.4 | 30.89 | 2,323 | rtx4090* | 53 | 78% |

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
| dominated (60–90%) | 15 |
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
| 2026-08-26T16:06 | sn25 | RELEASE | sn25 released v2026.8.26-1029569170 |
| 2026-08-26T14:29 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #56 from score-technol |
| 2026-08-26T13:33 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(proof): release a finished plan's min |
| 2026-08-26T13:33 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Merge feat/mirrored-scoring: submit anot |
| 2026-08-26T12:18 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(rewards): one-payer receipt fingerpri |
| 2026-08-26T12:18 | sn28 | RELEASE | sn28 released v0.4.11-dev |
| 2026-08-26T11:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2467, mixed scoring for partially ren |
| 2026-08-26T10:49 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(rewards): publish the allocation aud |
| 2026-08-26T10:49 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(batch): reuse canonical miner artif |
| 2026-08-26T09:54 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(selection): retain serving miners an |
| 2026-08-26T09:54 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: feat(scoring): give the JS sandbox the A |
| 2026-08-26T08:58 | sn25 | RELEASE | sn25 released v2026.8.26-1029312040 |
| 2026-08-26T08:58 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #55 from score-technol |
| 2026-08-26T08:58 | sn61 | RELEASE | sn61 released 4.10.0 |
| 2026-08-26T08:58 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update bot virus challenge image ve |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

