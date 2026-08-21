# Subnet watch — dashboard

_snapshot 2026-08-21T17:00:32Z · block 8894571 · run_status **ok**_

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
| 1 | sn76 Phylax | 77.3 | 81.21 | 136 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.9 | 1,237 | 1,237 = | cpu-small | 2 | 60% |
| 3 | sn23 Trishool | 72.4 | 590 | 590 = | cpu-small | 2 | 80% |
| 4 | sn102 ConnitoAI | 72.3 | 1,488 | 1,647 | rtx4090* | 5 | 26% |
| 5 | sn62 Ridges | 71.2 | 1,048 | 2,053 | rtx4090* | 5 | 36% |
| 6 | sn15 ORO | 70.6 | 21.91 | 21,388 | cpu-small | 77 | 93% |
| 7 | sn67 Harnyx | 70.3 | 13.54 | 932 | cpu-small | 160 | 23% |
| 8 | sn1 Apex | 70.2 | 784 | 1,282 | rtx4090* | 4 | 52% |
| 9 | sn56 Gradients | 69.9 | 727 | 1,120 | rtx4090* | 5 | 73% |
| 10 | sn91 cascade | 69.5 | 640 | 2,585 | rtx4090* | 5 | 52% |
| 11 | sn38 ChronoLLM | 67.9 | 165 | 3,501 | cpu-small | 10 | 52% |
| 12 | sn26 Perturb | 67.6 | 18.85 | 268 | rtx3060 | 10 | 70% |
| 13 | sn96 Verathos | 65.9 | 12.48 | 1,126 | rtx4090 | 89 | 40% |
| 14 | sn107 Minos | 65.6 | 160 | 45,262 | cpu-small | 20 | 90% |
| 15 | sn85 Vidaio | 65 | 168 | 1,530 | rtx4090* | 13 | 42% |
| 16 | sn55 NIOME | 62.1 | 69.42 | 574 | rtx4090* | 11 | 29% |
| 17 | sn81 Reliquary | 62.1 | 68.56 | 247 | rtx4090* | 53 | 5% |
| 18 | sn51 lium.io | 62 | 77.73 | 1,345 | rtx4090* | 46 | 82% |
| 19 | sn60 Bitsec.ai | 61.5 | 784 | 1,098 | cpu-small | 3 | 50% |
| 20 | sn108 Prometheon | 61.5 | 59.08 | 407 | rtx4090* | 8 | 66% |

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
| dominated (60–90%) | 19 |
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
| 2026-08-21T10:43 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

