# Subnet watch — dashboard

_snapshot 2026-08-21T19:06:16Z · block 8895200 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

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
| 1 | sn76 Phylax | 77.2 | 78.72 | 132 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.7 | 1,171 | 1,171 = | cpu-small | 2 | 61% |
| 3 | sn102 ConnitoAI | 72.4 | 1,525 | 1,526 | rtx4090* | 4 | 25% |
| 4 | sn23 Trishool | 72.3 | 571 | 571 = | cpu-small | 2 | 80% |
| 5 | sn62 Ridges | 71.1 | 1,016 | 1,990 | rtx4090* | 5 | 36% |
| 6 | sn15 ORO | 70.2 | 21.36 | 20,878 | cpu-small | 77 | 93% |
| 7 | sn1 Apex | 70.1 | 752 | 1,229 | rtx4090* | 4 | 52% |
| 8 | sn67 Harnyx | 70.1 | 13.03 | 899 | cpu-small | 160 | 23% |
| 9 | sn56 Gradients | 69.8 | 703 | 1,083 | rtx4090* | 5 | 73% |
| 10 | sn91 cascade | 69.6 | 653 | 2,636 | rtx4090* | 5 | 52% |
| 11 | sn26 Perturb | 67.9 | 20.22 | 386 | rtx3060 | 10 | 70% |
| 12 | sn38 ChronoLLM | 67.8 | 160 | 3,397 | cpu-small | 10 | 52% |
| 13 | sn96 Verathos | 66.1 | 13.04 | 856 | rtx4090 | 86 | 40% |
| 14 | sn107 Minos | 65.4 | 155 | 44,774 | cpu-small | 20 | 90% |
| 15 | sn85 Vidaio | 65 | 165 | 417 | rtx4090* | 13 | 42% |
| 16 | sn55 NIOME | 61.9 | 66.00 | 548 | rtx4090* | 11 | 29% |
| 17 | sn81 Reliquary | 61.9 | 66.00 | 245 | rtx4090* | 54 | 6% |
| 18 | sn51 lium.io | 61.8 | 72.57 | 1,366 | rtx4090* | 48 | 82% |
| 19 | sn108 Prometheon | 61.4 | 56.94 | 394 | rtx4090* | 8 | 66% |
| 20 | sn53 engy | 60.1 | 37.49 | 248 | rtx4090 | 144 | 63% |

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
| 2026-08-21T19:06 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Scoring: build the qualified-win as-of wi |
| 2026-08-21T19:06 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-21T19:06 | sn92 | RELEASE | sn92 released v0.1.0 |
| 2026-08-21T19:06 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Install the signer's keypair and verify t |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

