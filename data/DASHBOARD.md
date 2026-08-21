# Subnet watch — dashboard

_snapshot 2026-08-21T18:14:27Z · block 8894941 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.3 | 80.52 | 135 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.8 | 1,196 | 1,196 = | cpu-small | 2 | 61% |
| 3 | sn102 ConnitoAI | 72.5 | 1,560 | 1,561 | rtx4090* | 4 | 25% |
| 4 | sn23 Trishool | 72.4 | 583 | 583 = | cpu-small | 2 | 80% |
| 5 | sn62 Ridges | 71.1 | 1,040 | 2,037 | rtx4090* | 5 | 36% |
| 6 | sn15 ORO | 70.6 | 21.78 | 21,265 | cpu-small | 77 | 93% |
| 7 | sn67 Harnyx | 70.2 | 13.35 | 919 | cpu-small | 160 | 23% |
| 8 | sn1 Apex | 70.1 | 772 | 1,263 | rtx4090* | 4 | 52% |
| 9 | sn56 Gradients | 69.9 | 719 | 1,108 | rtx4090* | 5 | 73% |
| 10 | sn91 cascade | 69.5 | 631 | 2,551 | rtx4090* | 5 | 52% |
| 11 | sn26 Perturb | 68.5 | 23.10 | 395 | rtx3060 | 10 | 70% |
| 12 | sn38 ChronoLLM | 67.8 | 164 | 3,473 | cpu-small | 10 | 52% |
| 13 | sn96 Verathos | 66.3 | 13.52 | 875 | rtx4090 | 86 | 40% |
| 14 | sn107 Minos | 65.5 | 155 | 44,651 | cpu-small | 20 | 90% |
| 15 | sn85 Vidaio | 65.1 | 171 | 431 | rtx4090* | 13 | 42% |
| 16 | sn55 NIOME | 62 | 67.71 | 561 | rtx4090* | 11 | 29% |
| 17 | sn81 Reliquary | 62 | 67.55 | 250 | rtx4090* | 54 | 6% |
| 18 | sn51 lium.io | 61.9 | 74.82 | 1,404 | rtx4090* | 48 | 82% |
| 19 | sn108 Prometheon | 61.5 | 58.74 | 405 | rtx4090* | 8 | 66% |
| 20 | sn53 engy | 60.2 | 38.77 | 255 | rtx4090 | 144 | 63% |

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
| captured (>90%) | 27 |

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
| 2026-08-21T18:14 | sn25 | RELEASE | sn25 released v2026.8.21-1025339670 |
| 2026-08-21T17:00 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Turn provenance off until the run store c |
| 2026-08-21T16:15 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: quickstart matches production — mir |
| 2026-08-21T16:15 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-21T16:15 | sn102 | RELEASE | sn102 released v0.5.0 |
| 2026-08-21T16:15 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #223 from Connito-AI/ |
| 2026-08-21T14:50 | sn1 | RELEASE | sn1 released v4.3.6 |
| 2026-08-21T14:50 | sn25 | RELEASE | sn25 released v2026.8.21-1025223880 |
| 2026-08-21T13:57 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: fix(evaluation): reuse the prefix cache  |
| 2026-08-21T13:07 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(verify): mirror the daily verificati |
| 2026-08-21T13:07 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: verify short (<CHALLENGE_K) completions a |
| 2026-08-21T13:07 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Verify the gguf pin inline, since tests a |
| 2026-08-21T13:07 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(miner): eligibility now requires ac |
| 2026-08-21T11:52 | sn25 | RELEASE | sn25 released v2026.8.21-1025114260 |
| 2026-08-21T11:11 | sn25 | RELEASE | sn25 released v2026.8.21-1025093570 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

