# Subnet watch — dashboard

_snapshot 2026-11-02T09:22:12Z · block 9417306 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,828 | 2,828 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.1 | 1,880 | 1,880 = | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.6 | 1,608 | 1,608 = | rtx4090* | 5 | 20% |
| 4 | sn60 Bitsec.ai | 71.8 | 487 | 750 | cpu-small | 3 | 50% |
| 5 | sn67 Harnyx | 69.8 | 11.97 | 178 | cpu-small | 124 | 9% |
| 6 | sn103 Terza Inference | 69.7 | 672 | 1,759 | rtx4090* | 5 | 37% |
| 7 | sn14 Cacheon | 69.5 | 641 | 5,431 | rtx4090* | 3 | 84% |
| 8 | sn56 Gradients | 69.4 | 619 | 5,092 | rtx4090* | 6 | 51% |
| 9 | sn53 engy | 67.7 | 377 | 2,047 | rtx4090 | 29 | 26% |
| 10 | sn15 ORO | 66.2 | 6.56 | 11,929 | cpu-small | 80 | 95% |
| 11 | sn107 Minos | 65.7 | 162 | 13,815 | cpu-small | 20 | 80% |
| 12 | sn102 ConnitoAI | 64.6 | 147 | 837 | rtx4090* | 8 | 27% |
| 13 | sn125 Refinery | 64.1 | 127 | 789 | rtx4090* | 4 | 50% |
| 14 | sn124 Swarm | 62.2 | 81.14 | 1,843 | rtx4090* | 15 | 31% |
| 15 | sn62 Ridges | 61.6 | 60.42 | 1,427 | rtx4090* | 36 | 25% |
| 16 | sn28 SayGM | 58.5 | 27.15 | 4,241 | rtx4090* | 107 | 21% |
| 17 | sn80 OpenRoboto | 58.4 | 818 | 1,772 | rtx4090* | 12 | 17% |
| 18 | sn58 Attune | 56.7 | 496 | 799 | rtx4090* | 5 | 70% |
| 19 | sn66 conjectures | 56.5 | 12.43 | 155 | rtx4090* | 6 | 82% |
| 20 | sn117 everyframe.studi | 56.4 | 12.95 | 178 | rtx4090* | 8 | 87% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 25 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-02T09:22 | sn17 | RELEASE | sn17 released renderer-client-v0.1.4 |
| 2026-11-02T09:22 | sn51 | RELEASE | sn51 released lium-protocol-v2.0.0 |
| 2026-11-02T09:22 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5329 - [P1] Validator: fail CC B200/B |
| 2026-11-02T09:22 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Redraw text round 1 tasks longer than 2.5 |
| 2026-11-02T09:22 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep historical source-access fixtures on |
| 2026-11-02T09:22 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #414 from TensorLink-A |
| 2026-11-02T09:22 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Drop deleted MINER_BOX_RUNBOOK from docs  |
| 2026-11-02T09:22 | sn117 | RELEASE | sn117 released everycli v0.8.8 |
| 2026-11-02T09:22 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: gate: task-level cap rule from E507 - RE |
| 2026-11-02T01:55 | sn117 | RELEASE | sn117 released Merge pull request #57: everycli v0.8.7 UI reliability |
| 2026-11-02T01:55 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: bench site: Avg is the first score colum |
| 2026-11-01T22:45 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: [coding-agent] remove automatic alpha bur |
| 2026-11-01T22:45 | sn28 | RELEASE | sn28 released v0.5.18 |
| 2026-11-01T22:45 | sn117 | RELEASE | sn117 released everycli v0.8.6 |
| 2026-11-01T18:53 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: GPU receipt worker: the per-task run dir |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

