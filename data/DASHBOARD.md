# Subnet watch — dashboard

_snapshot 2026-11-03T01:50:21Z · block 9422246 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,764 | 2,764 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73 | 1,838 | 3,685 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.5 | 1,552 | 1,552 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 70 | 733 | 1,376 | rtx4090* | 5 | 33% |
| 5 | sn67 Harnyx | 69.7 | 11.60 | 173 | cpu-small | 129 | 9% |
| 6 | sn53 engy | 67.7 | 367 | 1,997 | rtx4090 | 29 | 26% |
| 7 | sn1 Apex | 67.5 | 346 | 685 | rtx4090* | 4 | 69% |
| 8 | sn15 ORO | 66.3 | 6.11 | 11,213 | cpu-small | 80 | 95% |
| 9 | sn107 Minos | 65.7 | 165 | 14,018 | cpu-small | 20 | 80% |
| 10 | sn102 ConnitoAI | 65.2 | 176 | 980 | rtx4090* | 10 | 27% |
| 11 | sn56 Gradients | 64.6 | 146 | 4,882 | rtx4090* | 9 | 51% |
| 12 | sn38 ChronoLLM | 63.4 | 52.23 | 466 | cpu-small | 10 | 52% |
| 13 | sn124 Swarm | 62.1 | 78.97 | 1,798 | rtx4090* | 15 | 31% |
| 14 | sn121 sundae_bar | 61.9 | 900 | 900 = | cpu-small | 2 | 60% |
| 15 | sn62 Ridges | 61.5 | 58.58 | 1,388 | rtx4090* | 36 | 25% |
| 16 | sn66 conjectures | 60.5 | 42.41 | 144 | rtx4090* | 5 | 82% |
| 17 | sn60 Bitsec.ai | 59.8 | 480 | 739 | cpu-small | 3 | 50% |
| 18 | sn80 OpenRoboto | 57.2 | 565 | 1,100 | rtx4090* | 12 | 17% |
| 19 | sn58 Attune | 56.4 | 456 | 735 | rtx4090* | 5 | 70% |
| 20 | sn9 iota | 56 | 12,058 | 12,058 = | rtx4090* | 2 | 80% |

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
| wide (<30%) | 31 |
| concentrated (30–60%) | 16 |
| dominated (60–90%) | 26 |
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
| 2026-11-03T01:50 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Document audited evaluator recovery metad |
| 2026-11-03T01:50 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: docs: use pack versions in miner scoring  |
| 2026-11-03T01:50 | sn48 | README_TASK_DIFF | sn48 README task/scoring sections changed |
| 2026-11-03T01:50 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(funding): miner-set total budget per |
| 2026-11-03T01:50 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Crown re-measure tests: the fake adapter |
| 2026-11-03T01:50 | sn117 | RELEASE | sn117 released everycli v0.9.2 |
| 2026-11-03T01:50 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-11-03T01:50 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: miner/README: point the pass-rate refere |
| 2026-11-02T19:40 | sn1 | RELEASE | sn1 released v4.6.1 |
| 2026-11-02T19:40 | sn17 | RELEASE | sn17 released witness-diagnostics-20261102 |
| 2026-11-02T19:40 | sn17 | README_TASK_DIFF | sn17 README task/scoring sections changed |
| 2026-11-02T19:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: Performance Max campaigns in MINER_ |
| 2026-11-02T19:40 | sn31 | BURN_DROP | sn31 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-02T19:40 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image in docker-compose. |
| 2026-11-02T19:40 | sn51 | RELEASE | sn51 released lium-protocol-v2.1.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

