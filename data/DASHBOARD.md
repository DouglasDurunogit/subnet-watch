# Subnet watch — dashboard

_snapshot 2026-08-26T19:17:20Z · block 8931256 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.4 | 175 | 392 | cpu-small | 13 | 20% |
| 2 | sn60 Bitsec.ai | 76.2 | 1,795 | 1,795 = | cpu-small | 2 | 50% |
| 3 | sn3 Teutonic | 75.4 | 3,684 | 3,684 = | rtx4090* | 5 | 20% |
| 4 | sn23 Trishool | 72 | 525 | 525 = | cpu-small | 2 | 80% |
| 5 | sn38 ChronoLLM | 71.1 | 410 | 1,587 | cpu-small | 6 | 53% |
| 6 | sn15 ORO | 70.6 | 22.27 | 42.50 | cpu-small | 96 | 92% |
| 7 | sn67 Harnyx | 70.5 | 14.05 | 250 | cpu-small | 138 | 7% |
| 8 | sn1 Apex | 70 | 736 | 1,263 | rtx4090* | 4 | 57% |
| 9 | sn91 cascade | 69.7 | 691 | 2,787 | rtx4090* | 5 | 52% |
| 10 | sn56 Gradients | 69.5 | 637 | 1,050 | rtx4090* | 6 | 74% |
| 11 | sn102 ConnitoAI | 69.1 | 566 | 2,223 | rtx4090* | 7 | 35% |
| 12 | sn26 Perturb | 68.5 | 23.15 | 436 | rtx3060 | 10 | 70% |
| 13 | sn124 Swarm | 66.7 | 282 | 849 | rtx4090* | 25 | 11% |
| 14 | sn61 RedTeam | 64.9 | 163 | 231 | rtx4090* | 32 | 4% |
| 15 | sn107 Minos | 64.5 | 125 | 38,999 | cpu-small | 20 | 90% |
| 16 | sn121 sundae_bar | 62.9 | 1,184 | 1,184 = | cpu-small | 2 | 61% |
| 17 | sn81 Reliquary | 62.7 | 83.49 | 313 | rtx4090* | 45 | 7% |
| 18 | sn108 Prometheon | 62.5 | 78.57 | 202 | rtx4090* | 9 | 29% |
| 19 | sn54 Yanez | 62.1 | 3.39 | 1,099 | a4000 | 134 | 35% |
| 20 | sn21 AdTAO | 59.6 | 1.74 | 1,173 | cpu-small | 16 | 45% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 14 |
| captured (>90%) | 26 |

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
| 2026-08-26T19:17 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: updating UAV all miners not just the quer |
| 2026-08-26T19:17 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat: verify the submitter violating cla |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

