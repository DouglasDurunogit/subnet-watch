# Subnet watch — dashboard

_snapshot 2026-08-21T13:57:18Z · block 8893655 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
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
| 1 | sn76 Phylax | 77.3 | 79.84 | 134 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.8 | 1,205 | 1,205 = | cpu-small | 2 | 61% |
| 3 | sn23 Trishool | 72.3 | 574 | 574 = | cpu-small | 2 | 80% |
| 4 | sn62 Ridges | 71.2 | 1,050 | 2,056 | rtx4090* | 5 | 36% |
| 5 | sn15 ORO | 70.7 | 21.51 | 38.73 | cpu-small | 77 | 93% |
| 6 | sn67 Harnyx | 70.2 | 13.52 | 930 | cpu-small | 156 | 23% |
| 7 | sn1 Apex | 70.1 | 756 | 1,281 | rtx4090* | 4 | 51% |
| 8 | sn56 Gradients | 69.9 | 719 | 1,105 | rtx4090* | 5 | 73% |
| 9 | sn91 cascade | 69.5 | 645 | 2,604 | rtx4090* | 5 | 52% |
| 10 | sn38 ChronoLLM | 67.9 | 165 | 3,495 | cpu-small | 10 | 52% |
| 11 | sn26 Perturb | 67.5 | 18.30 | 262 | rtx3060 | 10 | 70% |
| 12 | sn96 Verathos | 66 | 12.60 | 217 | rtx4090 | 86 | 60% |
| 13 | sn107 Minos | 65.4 | 155 | 44,388 | cpu-small | 20 | 90% |
| 14 | sn85 Vidaio | 65 | 167 | 1,524 | rtx4090* | 13 | 42% |
| 15 | sn98 NeverPlayAlone | 64.5 | 1,950 | 1,950 = | cpu-small | 1 | 100% |
| 16 | sn81 Reliquary | 62.6 | 81.51 | 276 | rtx4090* | 51 | 6% |
| 17 | sn55 NIOME | 62 | 68.26 | 565 | rtx4090* | 11 | 29% |
| 18 | sn51 lium.io | 61.7 | 70.50 | 1,294 | rtx4090* | 46 | 82% |
| 19 | sn60 Bitsec.ai | 61.6 | 802 | 1,124 | cpu-small | 3 | 50% |
| 20 | sn108 Prometheon | 61.5 | 59.56 | 410 | rtx4090* | 8 | 66% |

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
| concentrated (30–60%) | 18 |
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
| 2026-08-21T13:57 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: fix(evaluation): reuse the prefix cache  |
| 2026-08-21T13:07 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(verify): mirror the daily verificati |
| 2026-08-21T13:07 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: verify short (<CHALLENGE_K) completions a |
| 2026-08-21T13:07 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Verify the gguf pin inline, since tests a |
| 2026-08-21T13:07 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(miner): eligibility now requires ac |
| 2026-08-21T11:52 | sn25 | RELEASE | sn25 released v2026.8.21-1025114260 |
| 2026-08-21T11:11 | sn25 | RELEASE | sn25 released v2026.8.21-1025093570 |
| 2026-08-21T10:43 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-21T09:49 | sn14 | RELEASE | sn14 released Fused-epilogue kernel submission archive (2026-08-21) |
| 2026-08-21T07:23 | sn100 | RELEASE | sn100 released v3.3.28 |
| 2026-08-21T07:23 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(prism): miner Verda BYOK alongside  |
| 2026-08-21T05:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-21T05:04 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: absorb the reference miner's n |
| 2026-08-21T01:54 | sn34 | RELEASE | sn34 released Release 4.9.8 |
| 2026-08-20T23:08 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: fix: restore validator config parsing (#4 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

