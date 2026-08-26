# Subnet watch — dashboard

_snapshot 2026-08-26T12:17:58Z · block 8929159 · run_status **ok**_

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
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.2 | 168 | 377 | cpu-small | 13 | 20% |
| 2 | sn60 Bitsec.ai | 76.3 | 1,852 | 1,852 = | cpu-small | 2 | 50% |
| 3 | sn3 Teutonic | 75.6 | 3,886 | 3,886 = | rtx4090* | 5 | 20% |
| 4 | sn23 Trishool | 72.1 | 540 | 540 = | cpu-small | 2 | 80% |
| 5 | sn15 ORO | 70.9 | 22.80 | 43.14 | cpu-small | 95 | 92% |
| 6 | sn67 Harnyx | 70.5 | 14.45 | 257 | cpu-small | 138 | 7% |
| 7 | sn38 ChronoLLM | 70.3 | 323 | 817 | cpu-small | 6 | 53% |
| 8 | sn91 cascade | 69.9 | 711 | 2,870 | rtx4090* | 5 | 52% |
| 9 | sn56 Gradients | 69.6 | 655 | 1,081 | rtx4090* | 6 | 74% |
| 10 | sn102 ConnitoAI | 69.3 | 604 | 2,381 | rtx4090* | 7 | 37% |
| 11 | sn1 Apex | 68.7 | 498 | 1,203 | rtx4090* | 5 | 54% |
| 12 | sn26 Perturb | 68.1 | 21.30 | 405 | rtx3060 | 10 | 70% |
| 13 | sn21 AdTAO | 66.8 | 6.54 | 1,204 | cpu-small | 16 | 45% |
| 14 | sn124 Swarm | 66.7 | 289 | 867 | rtx4090* | 25 | 10% |
| 15 | sn61 RedTeam | 65.2 | 176 | 263 | rtx4090* | 30 | 5% |
| 16 | sn107 Minos | 64.9 | 137 | 41,071 | cpu-small | 20 | 90% |
| 17 | sn81 Reliquary | 63.2 | 96.60 | 295 | rtx4090* | 40 | 7% |
| 18 | sn121 sundae_bar | 63 | 1,242 | 1,242 = | cpu-small | 2 | 60% |
| 19 | sn108 Prometheon | 62.6 | 80.69 | 207 | rtx4090* | 9 | 29% |
| 20 | sn28 gm | 62.1 | 72.04 | 1,716 | rtx4090* | 37 | 31% |

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
| 2026-08-26T07:56 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validation): make claim assessments  |
| 2026-08-26T05:48 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: fix: score title fights by complete topic |
| 2026-08-26T04:09 | sn25 | RELEASE | sn25 released v2026.8.25-1029146630 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

