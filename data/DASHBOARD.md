# Subnet watch — dashboard

_snapshot 2026-10-29T19:16:38Z · block 9391484 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 16 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 77.1 | 6,190 | 6,190 = | rtx4090* | 5 | 20% |
| 2 | sn3 Teutonic | 73.5 | 2,102 | 2,102 = | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 73.1 | 1,861 | 1,861 = | rtx4090* | 5 | 20% |
| 4 | sn56 Gradients | 71.1 | 1,018 | 5,504 | rtx4090* | 6 | 51% |
| 5 | sn34 Yugos | 70.9 | 990 | 8,474 | rtx4090* | 3 | 85% |
| 6 | sn60 Bitsec.ai | 69.5 | 243 | 243 = | cpu-small | 3 | 50% |
| 7 | sn91 cascade | 69.4 | 622 | 1,673 | rtx4090* | 5 | 52% |
| 8 | sn103 Terza Inference | 69.3 | 605 | 1,524 | rtx4090* | 5 | 31% |
| 9 | sn53 engy | 68.3 | 444 | 2,390 | rtx4090 | 29 | 26% |
| 10 | sn46 Instant | 68.3 | 172 | 257 | cpu-small | 7 | 45% |
| 11 | sn1 Apex | 68 | 404 | 894 | rtx4090* | 5 | 59% |
| 12 | sn67 Harnyx | 67.3 | 6.11 | 554 | cpu-small | 131 | 26% |
| 13 | sn107 Minos | 66.2 | 187 | 15,895 | cpu-small | 20 | 80% |
| 14 | sn124 Swarm | 66 | 234 | 680 | rtx4090* | 25 | 10% |
| 15 | sn125 Refinery | 65.2 | 174 | 870 | rtx4090* | 4 | 50% |
| 16 | sn15 ORO | 65.1 | 7.35 | 13,632 | cpu-small | 68 | 96% |
| 17 | sn121 sundae_bar | 62.4 | 1,021 | 1,021 = | cpu-small | 2 | 60% |
| 18 | sn62 Ridges | 62.4 | 76.22 | 747 | rtx4090* | 44 | 15% |
| 19 | sn66 conjectures | 59.1 | 27.63 | 171 | rtx4090* | 7 | 80% |
| 20 | sn117 everyframe.studi | 58.6 | 25.03 | 123 | rtx4090* | 7 | 76% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 22 |
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
| 2026-10-29T19:17 | sn92 | RELEASE | sn92 released v1.2.0-rc11.post8.1-kit1: mammoth-1 self-check (miner si |
| 2026-10-29T19:17 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: 1.2.0rc11.post8.1 miner kit 1: mammoth-1  |
| 2026-10-29T19:17 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Room kit: attested guest TLS and hotel ke |
| 2026-10-29T19:17 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix(web): drop the score axis under the d |
| 2026-10-29T19:17 | sn117 | RELEASE | sn117 released everycli v0.8.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

