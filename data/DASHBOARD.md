# Subnet watch — dashboard

_snapshot 2026-10-21T16:08:02Z · block 9332941 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 81.5 | 8,748 | 13,123 | cpu-small | 2 | 75% |
| 2 | sn121 sundae_bar | 74.8 | 1,188 | 1,188 = | cpu-small | 2 | 60% |
| 3 | sn3 Teutonic | 74.4 | 2,784 | 7,437 | rtx4090* | 5 | 40% |
| 4 | sn97 Ingot | 73.4 | 2,057 | 2,057 = | rtx4090* | 5 | 20% |
| 5 | sn120 Affine | 73 | 1,835 | 18,058 | rtx4090* | 10 | 51% |
| 6 | sn91 cascade | 71.2 | 418 | 1,673 | cpu-small | 5 | 52% |
| 7 | sn102 ConnitoAI | 69.1 | 576 | 1,877 | rtx4090* | 5 | 45% |
| 8 | sn1 Apex | 68.5 | 472 | 1,008 | rtx4090* | 5 | 58% |
| 9 | sn67 Harnyx | 68.4 | 8.37 | 239 | cpu-small | 140 | 9% |
| 10 | sn82 Noah | 68 | 670 | 675 | rtx4090* | 61 | 2% |
| 11 | sn125 Refinery | 67.4 | 343 | 1,011 | rtx4090* | 4 | 50% |
| 12 | sn107 Minos | 67.4 | 247 | 21,034 | cpu-small | 20 | 80% |
| 13 | sn53 engy | 67.3 | 335 | 2,738 | rtx4090 | 36 | 11% |
| 14 | sn15 ORO | 66.7 | 8.02 | 16.26 | cpu-small | 63 | 97% |
| 15 | sn66 conjectures | 63.5 | 106 | 221 | rtx4090* | 4 | 80% |
| 16 | sn26 Perturb | 63.3 | 208 | 261 | rtx3060 | 4 | 60% |
| 17 | sn55 NIOME | 62.1 | 70.44 | 582 | rtx4090* | 11 | 30% |
| 18 | sn23 Trishool | 61.2 | 732 | 732 = | cpu-small | 2 | 80% |
| 19 | sn92 REAX | 60 | 79.19 | 2,685 | rtx4090 | 242 | 10% |
| 20 | sn49 Nepher Robotics | 59.6 | 1,149 | 4,043 | rtx4090* | 3 | 70% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 24 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-21T16:08 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Fix category dataset validation and hide r |
| 2026-10-21T16:08 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: feat(validator): one VHFT competition per |
| 2026-10-21T16:08 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4937 - [P1] Validator: a create waits |
| 2026-10-21T16:08 | sn66 | RELEASE | sn66 released v2026.10.21.2 |
| 2026-10-21T16:08 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #375 from reliquadotai |
| 2026-10-21T16:08 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix: retry backend 503 responses for min |
| 2026-10-21T16:08 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-10-21T16:08 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Improve competition operations and valid |
| 2026-10-21T16:08 | sn117 | RELEASE | sn117 released v0.6.1: Merge pull request #39 from everyframe-studio/f |
| 2026-10-21T16:08 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-21T11:40 | sn51 | RELEASE | sn51 released miner-v1.009 |
| 2026-10-21T11:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4860 - [P2] validator: CPU truth chec |
| 2026-10-21T11:40 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-21T11:40 | sn92 | RELEASE | sn92 released v1.2.0-rc10 |
| 2026-10-21T05:59 | sn25 | RELEASE | sn25 released v2026.10.20-1077553990 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

