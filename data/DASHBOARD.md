# Subnet watch — dashboard

_snapshot 2026-08-20T01:53:22Z · block 8882837 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.8 | 68.89 | 122 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.6 | 1,126 | 1,126 = | cpu-small | 2 | 60% |
| 3 | sn67 Harnyx | 72.4 | 23.21 | 310 | cpu-small | 147 | 9% |
| 4 | sn23 Trishool | 72 | 524 | 524 = | cpu-small | 2 | 80% |
| 5 | sn26 Perturb | 71 | 43.07 | 1,716 | rtx3060 | 10 | 70% |
| 6 | sn15 ORO | 70.3 | 18.53 | 17,673 | cpu-small | 84 | 92% |
| 7 | sn56 Gradients | 69.6 | 664 | 1,006 | rtx4090* | 5 | 72% |
| 8 | sn91 cascade | 69.2 | 580 | 2,345 | rtx4090* | 5 | 52% |
| 9 | sn38 ChronoLLM | 67.5 | 150 | 3,175 | cpu-small | 10 | 52% |
| 10 | sn96 Verathos | 66.4 | 13.66 | 305 | rtx4090 | 92 | 41% |
| 11 | sn107 Minos | 64.6 | 125 | 37,092 | cpu-small | 20 | 90% |
| 12 | sn85 Vidaio | 64.1 | 127 | 195 | rtx4090* | 13 | 42% |
| 13 | sn81 Reliquary | 62.2 | 70.98 | 187 | rtx4090* | 52 | 5% |
| 14 | sn60 Bitsec.ai | 61.9 | 902 | 902 = | cpu-small | 3 | 50% |
| 15 | sn55 NIOME | 61.6 | 59.61 | 501 | rtx4090* | 11 | 29% |
| 16 | sn51 lium.io | 61.2 | 61.97 | 1,099 | rtx4090* | 50 | 81% |
| 17 | sn53 engy | 59.8 | 34.14 | 229 | rtx4090 | 144 | 63% |
| 18 | sn21 AdTAO | 58.6 | 1.42 | 385 | cpu-small | 16 | 37% |
| 19 | sn28 gm | 58.1 | 22.01 | 1,441 | rtx4090* | 49 | 34% |
| 20 | sn68 NOVA | 55.1 | 8,106 | 8,106 = | rtx4090* | 1 | 100% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 18 |
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
| 2026-08-20T01:53 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: Merge pull request #51 from 0xsigurd/feat |
| 2026-08-20T01:53 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-08-20T01:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verifier literals in restart boo |
| 2026-08-20T01:53 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: fix(cli): model verify printed fields th |
| 2026-08-20T00:02 | sn7 | RELEASE | sn7 released release-20260819-235753: Activate: quorum short-circuit + |
| 2026-08-19T21:50 | sn7 | RELEASE | sn7 released release-20260819-213008: Record the finney TAO bond vault |
| 2026-08-19T21:50 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Trim pre-window crown tails before the sco |
| 2026-08-19T21:50 | sn7 | README_TASK_DIFF | sn7 README task/scoring sections changed |
| 2026-08-19T21:50 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(validator): pipelined window collect |
| 2026-08-19T21:11 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(bench): harness round mode with a si |
| 2026-08-19T21:11 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Add multi-layer dedup and weighted leak e |
| 2026-08-19T20:41 | sn1 | RELEASE | sn1 released v4.3.5 |
| 2026-08-19T20:41 | sn89 | README_TASK_DIFF | sn89 README task/scoring sections changed |
| 2026-08-19T20:02 | sn25 | RELEASE | sn25 released v2026.8.19-1023689220 |
| 2026-08-19T20:02 | sn51 | RELEASE | sn51 released executor-v1.123 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

