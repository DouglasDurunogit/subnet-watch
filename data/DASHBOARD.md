# Subnet watch — dashboard

_snapshot 2026-11-24T00:10:52Z · block 9572915 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 104 | `miner_burn` < 0.99 |
| Ranked | 104 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 14 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 3 | `█` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 24 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 238 | 238 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.1 | 1,873 | 3,774 | rtx4090* | 4 | 40% |
| 3 | sn15 ORO | 65.1 | 4.80 | 10.32 | cpu-small | 71 | 95% |
| 4 | sn124 Swarm | 64.9 | 172 | 1,337 | rtx4090* | 10 | 31% |
| 5 | sn53 engy | 64.6 | 148 | 12,084 | rtx4090 | 20 | 61% |
| 6 | sn67 Harnyx | 63.8 | 1.65 | 313 | cpu-small | 122 | 23% |
| 7 | sn66 conjectures | 62.5 | 77.45 | 921 | rtx4090* | 4 | 80% |
| 8 | sn120 Affine | 61.8 | 2,249 | 2,249 = | rtx4090* | 9 | 11% |
| 9 | sn58 Attune | 61.6 | 59.75 | 149 | rtx4090* | 57 | 30% |
| 10 | sn127 Zils | 60.9 | 48.88 | 68.88 | rtx4090 | 4 | 90% |
| 11 | sn41 Almanac | 60.7 | 1.83 | 213 | cpu-small | 125 | 15% |
| 12 | sn62 Ridges | 60.6 | 43.95 | 381 | rtx4090* | 47 | 10% |
| 13 | sn111 Claims | 60.1 | 38.80 | 156 | rtx4090* | 4 | 88% |
| 14 | sn25 UR | 58.1 | 20.18 | 20.18 = | rtx4090* | 10 | 45% |
| 15 | sn34 Yugos | 57.7 | 660 | 5,673 | rtx4090* | 3 | 85% |
| 16 | sn4 Targon | 57.1 | 7,964 | 20,031 | rtx4090* | 3 | 67% |
| 17 | sn102 ConnitoAI | 57 | 531 | 543 | rtx4090* | 4 | 25% |
| 18 | sn99 Axonry | 55.7 | 10,398 | 10,398 = | rtx4090* | 1 | 100% |
| 19 | sn46 Instant | 55.6 | 136 | 156 | cpu-small | 9 | 24% |
| 20 | sn117 everyframe.studi | 55 | 8.47 | 48.42 | rtx4090* | 27 | 77% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 29 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-24T00:11 | sn12 | RELEASE | sn12 released validator-staging-2026-11-23-45269217986-635-1: feat: ex |
| 2026-11-24T00:11 | sn18 | RELEASE | sn18 released Release 2.1.5 |
| 2026-11-24T00:11 | sn28 | RELEASE | sn28 released v0.6.0 |
| 2026-11-24T00:11 | sn39 | SCORING_COMMIT | sn39 commit touches scoring: never repair a day scored with its profit |
| 2026-11-24T00:11 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-7005 - [P4] Validator: one miner snap |
| 2026-11-24T00:11 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Reuse the Docker layer cache for miner im |
| 2026-11-24T00:11 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-24T00:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Recover funded pilot attempts without rep |
| 2026-11-24T00:11 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: tests(laned): WB23 miner-chosen lane B le |
| 2026-11-24T00:11 | sn92 | RELEASE | sn92 released v1.2.0-rc11.post8.16 |
| 2026-11-24T00:11 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: 1.2.0rc11.post8.16: validator source as l |
| 2026-11-24T00:11 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Raise validator source and structured re |
| 2026-11-24T00:11 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Ladder: every document a miner was shown |
| 2026-11-24T00:11 | sn117 | RELEASE | sn117 released everycli v1.2.7 |
| 2026-11-23T12:19 | sn12 | RELEASE | sn12 released miner-testing-2026-11-23-45138900060-7-1: feat: preserve |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

