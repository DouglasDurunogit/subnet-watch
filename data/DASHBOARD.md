# Subnet watch — dashboard

_snapshot 2026-10-29T23:28:49Z · block 9392745 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 76.9 | 5,817 | 5,817 = | rtx4090* | 5 | 20% |
| 2 | sn3 Teutonic | 73.3 | 1,975 | 1,975 = | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.8 | 1,694 | 1,694 = | rtx4090* | 5 | 20% |
| 4 | sn56 Gradients | 70.9 | 959 | 5,186 | rtx4090* | 6 | 51% |
| 5 | sn34 Yugos | 70.7 | 929 | 7,958 | rtx4090* | 3 | 85% |
| 6 | sn103 Terza Inference | 69.3 | 596 | 1,443 | rtx4090* | 5 | 33% |
| 7 | sn60 Bitsec.ai | 69.3 | 231 | 231 = | cpu-small | 3 | 50% |
| 8 | sn91 cascade | 69 | 549 | 1,478 | rtx4090* | 5 | 52% |
| 9 | sn46 Instant | 68.7 | 193 | 205 | cpu-small | 7 | 42% |
| 10 | sn53 engy | 68.2 | 436 | 2,950 | rtx4090 | 29 | 26% |
| 11 | sn1 Apex | 67.7 | 373 | 828 | rtx4090* | 5 | 60% |
| 12 | sn15 ORO | 67 | 6.90 | 12,732 | cpu-small | 69 | 96% |
| 13 | sn67 Harnyx | 66.9 | 5.68 | 521 | cpu-small | 131 | 26% |
| 14 | sn107 Minos | 65.9 | 173 | 14,714 | cpu-small | 20 | 80% |
| 15 | sn125 Refinery | 64.9 | 163 | 819 | rtx4090* | 4 | 50% |
| 16 | sn62 Ridges | 62.4 | 75.56 | 705 | rtx4090* | 44 | 15% |
| 17 | sn121 sundae_bar | 62.2 | 961 | 961 = | cpu-small | 2 | 60% |
| 18 | sn124 Swarm | 61.8 | 72.13 | 5,411 | rtx4090* | 11 | 85% |
| 19 | sn66 conjectures | 58.8 | 25.46 | 160 | rtx4090* | 7 | 80% |
| 20 | sn4 Targon | 58.6 | 12,161 | 24,674 | rtx4090* | 4 | 61% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 25 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 100 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-29T23:29 | sn1 | RELEASE | sn1 released v4.5.4 |
| 2026-10-29T23:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge leadertop/head-summary-spec: valida |
| 2026-10-29T23:29 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5177 connector lead lock TTL 15 s ->  |
| 2026-10-29T23:29 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #528 from ridgesai/fea |
| 2026-10-29T23:29 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Validate claims-room upload paths and req |
| 2026-10-29T19:17 | sn1 | RELEASE | sn1 released v4.5.3 |
| 2026-10-29T19:17 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Preserve deployed validator recovery in t |
| 2026-10-29T19:17 | sn28 | RELEASE | sn28 released v0.5.15 |
| 2026-10-29T19:17 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3698 - [P2] Validator: pay a split no |
| 2026-10-29T19:17 | sn51 | README_TASK_DIFF | sn51 README task/scoring sections changed |
| 2026-10-29T19:17 | sn66 | RELEASE | sn66 released v2026.10.29 |
| 2026-10-29T19:17 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-29T19:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve legacy baseline comparison autho |
| 2026-10-29T19:17 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #496 from Umi-BitSign/ |
| 2026-10-29T19:17 | sn90 | RELEASE | sn90 released v1.3.3 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

