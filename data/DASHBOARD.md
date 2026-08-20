# Subnet watch — dashboard

_snapshot 2026-08-20T04:48:52Z · block 8883714 · run_status **ok**_

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
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.7 | 67.83 | 120 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.5 | 1,109 | 1,109 = | cpu-small | 2 | 60% |
| 3 | sn67 Harnyx | 72.4 | 22.81 | 305 | cpu-small | 147 | 9% |
| 4 | sn23 Trishool | 72 | 520 | 520 = | cpu-small | 2 | 80% |
| 5 | sn15 ORO | 70.4 | 18.32 | 17,477 | cpu-small | 84 | 92% |
| 6 | sn56 Gradients | 69.6 | 653 | 991 | rtx4090* | 5 | 72% |
| 7 | sn91 cascade | 69.1 | 571 | 2,309 | rtx4090* | 5 | 52% |
| 8 | sn38 ChronoLLM | 67.5 | 147 | 3,129 | cpu-small | 10 | 52% |
| 9 | sn26 Perturb | 67 | 16.05 | 228 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 66.2 | 13.23 | 292 | rtx4090 | 91 | 41% |
| 11 | sn107 Minos | 64.5 | 125 | 36,865 | cpu-small | 20 | 90% |
| 12 | sn85 Vidaio | 64.1 | 127 | 191 | rtx4090* | 13 | 42% |
| 13 | sn28 gm | 63 | 93.56 | 832 | rtx4090* | 48 | 19% |
| 14 | sn60 Bitsec.ai | 62 | 917 | 917 = | cpu-small | 3 | 50% |
| 15 | sn81 Reliquary | 61.6 | 58.93 | 222 | rtx4090* | 55 | 6% |
| 16 | sn55 NIOME | 61.5 | 58.56 | 493 | rtx4090* | 11 | 29% |
| 17 | sn51 lium.io | 61.3 | 61.93 | 1,103 | rtx4090* | 50 | 81% |
| 18 | sn102 ConnitoAI | 60 | 1,304 | 1,554 | rtx4090* | 6 | 27% |
| 19 | sn53 engy | 59.7 | 33.72 | 227 | rtx4090 | 144 | 63% |
| 20 | sn21 AdTAO | 58.5 | 1.39 | 380 | cpu-small | 16 | 37% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 20 |
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
| 2026-08-20T04:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve restart timing across miner boot |
| 2026-08-20T03:58 | sn21 | RELEASE | sn21 released SN21 rich training data v2 |
| 2026-08-20T03:58 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Merge pull request #48 from TrishoolAI/fe |
| 2026-08-20T03:58 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: Merge pull request #166 from BaseIntelli |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

