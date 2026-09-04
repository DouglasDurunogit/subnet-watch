# Subnet watch — dashboard

_snapshot 2026-09-04T15:08:52Z · block 8994808 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.1 | 163 | 364 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 77 | 90.37 | 5,404 | cpu-small | 21 | 81% |
| 3 | sn76 Phylax | 73 | 27.53 | 72.99 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 71.2 | 17.15 | 89.88 | cpu-small | 141 | 17% |
| 5 | sn91 cascade | 70.2 | 792 | 3,191 | rtx4090* | 5 | 52% |
| 6 | sn15 ORO | 70 | 20.85 | 21,359 | cpu-small | 59 | 94% |
| 7 | sn56 Gradients | 68.9 | 527 | 1,312 | rtx4090* | 5 | 75% |
| 8 | sn124 Swarm | 66.3 | 257 | 795 | rtx4090* | 25 | 11% |
| 9 | sn111 Claims | 65.2 | 192 | 3,403 | rtx4090* | 5 | 82% |
| 10 | sn80 OpenRoboto | 65.2 | 175 | 577 | rtx4090* | 5 | 72% |
| 11 | sn79 MVTRX | 64.8 | 4.54 | 391 | cpu-small | 226 | 9% |
| 12 | sn121 sundae_bar | 62.9 | 1,186 | 1,186 = | cpu-small | 2 | 60% |
| 13 | sn74 Gittensor | 61.2 | 56.02 | 366 | rtx4090 | 11 | 64% |
| 14 | sn28 SayGM | 60.6 | 46.53 | 9,698 | rtx4090* | 39 | 69% |
| 15 | sn41 Almanac | 59.6 | 32.15 | 95.22 | cpu-small | 87 | 8% |
| 16 | sn102 ConnitoAI | 59 | 27.60 | 1,426 | rtx4090* | 8 | 26% |
| 17 | sn65 True Performance | 58.3 | 29.92 | 68.08 | rtx4090* | 6 | 90% |
| 18 | sn51 lium.io | 57.4 | 24.74 | 2,073 | rtx4090* | 64 | 76% |
| 19 | sn101 Tag101 | 57.3 | 0.11 | 0.90 | cpu-small | 236 | 91% |
| 20 | sn14 Cacheon | 57.2 | 558 | 4,382 | rtx4090* | 6 | 70% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 22 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| code-submission (validator runs it) | 11 |
| min_compute.yml (curated) | 11 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-04T15:09 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Show model digests for queued and active e |
| 2026-09-04T15:09 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): reference loop uses bt.Wa |
| 2026-09-04T15:09 | sn25 | RELEASE | sn25 released v2026.9.4-1037327320 |
| 2026-09-04T15:09 | sn47 | SCORING_COMMIT | sn47 commit touches scoring: new datasets list and verifier |
| 2026-09-04T15:09 | sn47 | README_TASK_DIFF | sn47 README task/scoring sections changed |
| 2026-09-04T11:33 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record semantic verifier parallel qualifi |
| 2026-09-04T11:33 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Derive the verifier image tag, not only i |
| 2026-09-04T11:33 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-04T11:33 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Expose replay-verified public miner solut |
| 2026-09-04T11:33 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Smooth the miner CLI and quiet the archiv |
| 2026-09-04T11:33 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: re-key a registration when the miner |
| 2026-09-04T11:33 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(validator): extract submit outcome h |
| 2026-09-04T11:33 | sn114 | README_TASK_DIFF | sn114 README task/scoring sections changed |
| 2026-09-04T06:21 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: test(validator): prove burn composition m |
| 2026-09-04T06:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected Arena reward compatibility |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

