# Subnet watch — dashboard

_snapshot 2026-08-26T14:29:28Z · block 8929816 · run_status **ok**_

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
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.2 | 169 | 380 | cpu-small | 13 | 20% |
| 2 | sn60 Bitsec.ai | 76.2 | 1,808 | 1,808 = | cpu-small | 2 | 50% |
| 3 | sn3 Teutonic | 75.5 | 3,777 | 3,777 = | rtx4090* | 5 | 20% |
| 4 | sn102 ConnitoAI | 72.9 | 1,753 | 2,107 | rtx4090* | 4 | 33% |
| 5 | sn23 Trishool | 72.1 | 538 | 538 = | cpu-small | 2 | 80% |
| 6 | sn38 ChronoLLM | 71.1 | 414 | 1,599 | cpu-small | 6 | 53% |
| 7 | sn15 ORO | 70.6 | 22.47 | 42.52 | cpu-small | 95 | 92% |
| 8 | sn67 Harnyx | 70.4 | 14.21 | 253 | cpu-small | 138 | 7% |
| 9 | sn1 Apex | 70.1 | 761 | 1,174 | rtx4090* | 4 | 58% |
| 10 | sn91 cascade | 69.8 | 697 | 2,812 | rtx4090* | 5 | 52% |
| 11 | sn56 Gradients | 69.5 | 645 | 1,064 | rtx4090* | 6 | 74% |
| 12 | sn26 Perturb | 68.1 | 20.84 | 397 | rtx3060 | 10 | 70% |
| 13 | sn124 Swarm | 66.7 | 285 | 861 | rtx4090* | 25 | 11% |
| 14 | sn21 AdTAO | 66.6 | 6.29 | 1,163 | cpu-small | 16 | 45% |
| 15 | sn61 RedTeam | 65.1 | 170 | 254 | rtx4090* | 30 | 5% |
| 16 | sn107 Minos | 64.8 | 132 | 38,894 | cpu-small | 20 | 90% |
| 17 | sn81 Reliquary | 63.1 | 93.61 | 297 | rtx4090* | 40 | 7% |
| 18 | sn108 Prometheon | 62.5 | 78.30 | 201 | rtx4090* | 9 | 29% |
| 19 | sn28 gm | 61.6 | 61.55 | 1,475 | rtx4090* | 37 | 36% |
| 20 | sn51 lium.io | 58.9 | 35.17 | 2,349 | rtx4090* | 56 | 77% |

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
| 2026-08-26T08:58 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(964): optimizeYield can be scored —  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

