# Subnet watch — dashboard

_snapshot 2026-08-21T14:49:40Z · block 8893917 · run_status **ok**_

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
| New events this window | 3 | see ALARMS.md |

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
| 1 | sn76 Phylax | 77.3 | 81.31 | 136 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.9 | 1,241 | 1,241 = | cpu-small | 2 | 60% |
| 3 | sn23 Trishool | 72.4 | 591 | 591 = | cpu-small | 2 | 80% |
| 4 | sn62 Ridges | 71.2 | 1,055 | 2,065 | rtx4090* | 5 | 36% |
| 5 | sn15 ORO | 70.4 | 21.69 | 39.05 | cpu-small | 77 | 93% |
| 6 | sn1 Apex | 70.2 | 792 | 1,295 | rtx4090* | 4 | 51% |
| 7 | sn67 Harnyx | 70.1 | 13.70 | 942 | cpu-small | 158 | 23% |
| 8 | sn56 Gradients | 70 | 731 | 1,124 | rtx4090* | 5 | 73% |
| 9 | sn91 cascade | 69.6 | 655 | 2,646 | rtx4090* | 5 | 52% |
| 10 | sn38 ChronoLLM | 67.9 | 166 | 3,511 | cpu-small | 10 | 52% |
| 11 | sn26 Perturb | 67.7 | 18.93 | 269 | rtx3060 | 10 | 70% |
| 12 | sn96 Verathos | 65.7 | 11.93 | 242 | rtx4090 | 90 | 58% |
| 13 | sn107 Minos | 65.4 | 152 | 44,686 | cpu-small | 20 | 90% |
| 14 | sn85 Vidaio | 65.1 | 170 | 1,548 | rtx4090* | 13 | 42% |
| 15 | sn98 NeverPlayAlone | 64.6 | 1,980 | 1,980 = | cpu-small | 1 | 100% |
| 16 | sn81 Reliquary | 62.5 | 78.46 | 259 | rtx4090* | 52 | 6% |
| 17 | sn28 gm | 62 | 69.33 | 1,780 | rtx4090* | 53 | 15% |
| 18 | sn55 NIOME | 62 | 68.13 | 563 | rtx4090* | 11 | 29% |
| 19 | sn60 Bitsec.ai | 61.6 | 803 | 1,125 | cpu-small | 3 | 50% |
| 20 | sn108 Prometheon | 61.5 | 58.88 | 406 | rtx4090* | 8 | 66% |

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
| 2026-08-21T09:49 | sn14 | RELEASE | sn14 released Fused-epilogue kernel submission archive (2026-08-21) |
| 2026-08-21T07:23 | sn100 | RELEASE | sn100 released v3.3.28 |
| 2026-08-21T07:23 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(prism): miner Verda BYOK alongside  |
| 2026-08-21T05:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-21T05:04 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: absorb the reference miner's n |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

