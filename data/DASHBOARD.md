# Subnet watch — dashboard

_snapshot 2026-08-20T03:07:08Z · block 8883205 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.7 | 67.78 | 120 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.5 | 1,109 | 1,109 = | cpu-small | 2 | 60% |
| 3 | sn67 Harnyx | 72.3 | 22.79 | 305 | cpu-small | 147 | 9% |
| 4 | sn23 Trishool | 72 | 522 | 522 = | cpu-small | 2 | 80% |
| 5 | sn15 ORO | 70.3 | 18.18 | 17,350 | cpu-small | 84 | 92% |
| 6 | sn56 Gradients | 69.6 | 653 | 990 | rtx4090* | 5 | 72% |
| 7 | sn91 cascade | 69.1 | 571 | 2,308 | rtx4090* | 5 | 52% |
| 8 | sn38 ChronoLLM | 67.5 | 147 | 3,126 | cpu-small | 10 | 52% |
| 9 | sn26 Perturb | 67.3 | 17.25 | 249 | rtx3060 | 10 | 69% |
| 10 | sn96 Verathos | 66.3 | 13.39 | 288 | rtx4090 | 92 | 41% |
| 11 | sn107 Minos | 64.5 | 122 | 36,786 | cpu-small | 20 | 90% |
| 12 | sn85 Vidaio | 64.1 | 127 | 192 | rtx4090* | 13 | 42% |
| 13 | sn60 Bitsec.ai | 62 | 909 | 909 = | cpu-small | 3 | 50% |
| 14 | sn81 Reliquary | 61.7 | 62.41 | 231 | rtx4090* | 54 | 6% |
| 15 | sn55 NIOME | 61.6 | 58.95 | 494 | rtx4090* | 11 | 29% |
| 16 | sn28 gm | 61.5 | 59.06 | 1,132 | rtx4090* | 49 | 38% |
| 17 | sn51 lium.io | 61.2 | 60.62 | 1,103 | rtx4090* | 49 | 81% |
| 18 | sn53 engy | 59.7 | 33.57 | 226 | rtx4090 | 144 | 63% |
| 19 | sn21 AdTAO | 58.5 | 1.39 | 380 | cpu-small | 16 | 37% |
| 20 | sn41 Almanac | 55.3 | 11.21 | 28.76 | cpu-small | 75 | 72% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
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
| 2026-08-20T03:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test: rehearse miner maintenance first ro |
| 2026-08-20T03:07 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Show miners the cutoff and what their com |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

