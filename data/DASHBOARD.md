# Subnet watch — dashboard

_snapshot 2026-08-22T01:47:06Z · block 8897204 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.3 | 81.13 | 136 | cpu-small | 13 | 20% |
| 2 | sn23 Trishool | 72.4 | 583 | 583 = | cpu-small | 2 | 80% |
| 3 | sn15 ORO | 70.3 | 20.92 | 38.93 | cpu-small | 78 | 93% |
| 4 | sn67 Harnyx | 70.2 | 13.35 | 920 | cpu-small | 162 | 23% |
| 5 | sn1 Apex | 70.1 | 772 | 1,220 | rtx4090* | 4 | 53% |
| 6 | sn56 Gradients | 69.9 | 719 | 1,108 | rtx4090* | 5 | 73% |
| 7 | sn91 cascade | 69.9 | 718 | 2,896 | rtx4090* | 5 | 52% |
| 8 | sn26 Perturb | 68 | 20.75 | 395 | rtx3060 | 10 | 70% |
| 9 | sn38 ChronoLLM | 66.5 | 114 | 1,553 | cpu-small | 10 | 52% |
| 10 | sn96 Verathos | 66.1 | 13.15 | 569 | rtx4090 | 94 | 41% |
| 11 | sn107 Minos | 65.6 | 161 | 44,764 | cpu-small | 20 | 90% |
| 12 | sn98 NeverPlayAlone | 64.5 | 1,959 | 1,959 = | cpu-small | 1 | 100% |
| 13 | sn85 Vidaio | 64.3 | 136 | 424 | rtx4090* | 13 | 42% |
| 14 | sn81 Reliquary | 63.2 | 97.98 | 256 | rtx4090* | 45 | 6% |
| 15 | sn121 sundae_bar | 63 | 1,230 | 1,230 = | cpu-small | 2 | 60% |
| 16 | sn51 lium.io | 62.8 | 96.02 | 1,619 | rtx4090* | 51 | 71% |
| 17 | sn108 Prometheon | 61.5 | 58.48 | 403 | rtx4090* | 8 | 66% |
| 18 | sn53 engy | 59.9 | 35.76 | 238 | rtx4090 | 144 | 63% |
| 19 | sn60 Bitsec.ai | 59.7 | 465 | 465 = | cpu-small | 3 | 50% |
| 20 | sn28 gm | 58.5 | 25.20 | 1,799 | rtx4090* | 56 | 17% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 22 |
| captured (>90%) | 24 |

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
| 2026-08-22T01:47 | sn25 | RELEASE | sn25 released v2026.8.21-1025613560 |
| 2026-08-22T00:02 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: weighted reference-anchored scoring |
| 2026-08-21T23:35 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore: remove dead BackendClient top-mine |
| 2026-08-21T22:02 | sn90 | RELEASE | sn90 released v1.1.5 |
| 2026-08-21T22:02 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(validator): fall back to CoinGecko TA |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

