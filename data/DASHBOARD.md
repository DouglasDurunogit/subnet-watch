# Subnet watch — dashboard

_snapshot 2026-09-02T01:27:20Z · block 8976302 · run_status **ok**_

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
| Ranked | 95 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 78.4 | 106 | 1,929 | cpu-small | 9 | 60% |
| 2 | sn107 Minos | 78.1 | 114 | 35,984 | cpu-small | 19 | 91% |
| 3 | sn3 Teutonic | 75.2 | 3,538 | 3,538 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 74.7 | 42.38 | 89.35 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 72.4 | 22.30 | 1,145 | cpu-small | 125 | 32% |
| 6 | sn15 ORO | 71.6 | 25.97 | 42.07 | cpu-small | 66 | 93% |
| 7 | sn91 cascade | 70.4 | 844 | 3,400 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 68.7 | 24.42 | 175 | rtx4090 | 83 | 41% |
| 9 | sn11 TrajectoryRL | 67.8 | 5,138 | 5,138 = | cpu-small | 1 | 100% |
| 10 | sn56 Gradients | 67.6 | 362 | 1,009 | rtx4090* | 7 | 72% |
| 11 | sn111 Claims | 67.1 | 323 | 2,891 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 66.3 | 258 | 793 | rtx4090* | 25 | 11% |
| 13 | sn61 RedTeam | 64.7 | 152 | 221 | rtx4090* | 47 | 3% |
| 14 | sn98 NeverPlayAlone | 64.4 | 1,847 | 1,847 = | cpu-small | 1 | 100% |
| 15 | sn21 AdTAO | 64.3 | 3.81 | 512 | cpu-small | 16 | 45% |
| 16 | sn81 Reliquary | 64.2 | 132 | 246 | rtx4090* | 33 | 6% |
| 17 | sn79 MVTRX | 63.9 | 3.86 | 408 | cpu-small | 229 | 10% |
| 18 | sn121 sundae_bar | 62.9 | 1,192 | 1,192 = | cpu-small | 2 | 60% |
| 19 | sn54 Yanez | 62.8 | 4.29 | 893 | a4000 | 96 | 35% |
| 20 | sn55 NIOME | 62.3 | 74.04 | 609 | rtx4090* | 11 | 29% |

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
| captured (>90%) | 29 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 100 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-02T01:27 | sn25 | RELEASE | sn25 released v2026.9.1-1035082030 |
| 2026-09-02T01:27 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-01T23:29 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: multiple llm key and improve the scoring |
| 2026-09-01T23:29 | sn104 | README_TASK_DIFF | sn104 README task/scoring sections changed |
| 2026-09-01T21:25 | sn25 | RELEASE | sn25 released v2026.9.1-1034943860 |
| 2026-09-01T21:25 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Run the validator image on the pinned int |
| 2026-09-01T18:42 | sn7 | RELEASE | sn7 released release-20260901-182140: Set miner burn to 0% (v3.3.1) (# |
| 2026-09-01T18:42 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Set miner burn to 0% (v3.3.1) (#710) |
| 2026-09-01T18:42 | sn7 | README_TASK_DIFF | sn7 README task/scoring sections changed |
| 2026-09-01T18:42 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): focus column shows per-typ |
| 2026-09-01T18:42 | sn25 | RELEASE | sn25 released v2026.9.1-1034848790 |
| 2026-09-01T18:42 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: sim-testnet: verify direct Connect ingres |
| 2026-09-01T18:42 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: fix: show scoring-aligned augmented metri |
| 2026-09-01T18:42 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge pull request #120 from swarm-subne |
| 2026-09-01T15:14 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.922 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

