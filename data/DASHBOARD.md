# Subnet watch — dashboard

_snapshot 2026-10-30T16:40:30Z · block 9397903 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,872 | 2,872 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,935 | 3,879 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.8 | 1,692 | 1,692 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 71.7 | 1,227 | 2,462 | rtx4090* | 4 | 45% |
| 5 | sn60 Bitsec.ai | 69.4 | 237 | 237 = | cpu-small | 3 | 50% |
| 6 | sn91 cascade | 68.9 | 540 | 1,455 | rtx4090* | 5 | 52% |
| 7 | sn53 engy | 67.8 | 389 | 2,101 | rtx4090 | 29 | 26% |
| 8 | sn67 Harnyx | 67.7 | 6.82 | 359 | cpu-small | 132 | 18% |
| 9 | sn1 Apex | 67.4 | 339 | 844 | rtx4090* | 5 | 61% |
| 10 | sn102 ConnitoAI | 67.3 | 337 | 838 | rtx4090* | 7 | 28% |
| 11 | sn107 Minos | 65.8 | 167 | 14,206 | cpu-small | 20 | 80% |
| 12 | sn15 ORO | 65.8 | 7.06 | 12,495 | cpu-small | 69 | 96% |
| 13 | sn125 Refinery | 64.7 | 150 | 813 | rtx4090* | 4 | 50% |
| 14 | sn121 sundae_bar | 62.1 | 951 | 951 = | cpu-small | 2 | 60% |
| 15 | sn62 Ridges | 61.9 | 66.46 | 699 | rtx4090* | 44 | 15% |
| 16 | sn124 Swarm | 61.7 | 70.51 | 218 | rtx4090* | 11 | 85% |
| 17 | sn28 SayGM | 58.9 | 30.58 | 1,705 | rtx4090* | 153 | 15% |
| 18 | sn66 conjectures | 58.8 | 25.24 | 159 | rtx4090* | 6 | 80% |
| 19 | sn4 Targon | 58.4 | 11,444 | 25,623 | rtx4090* | 4 | 64% |
| 20 | sn58 Attune | 57 | 547 | 880 | rtx4090* | 5 | 70% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 24 |
| captured (>90%) | 27 |

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
| 2026-10-30T16:41 | sn28 | RELEASE | sn28 released v0.5.16 |
| 2026-10-30T16:41 | sn51 | RELEASE | sn51 released lium-protocol-v1.18.0 |
| 2026-10-30T16:41 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5393 - [P0] Validator: a full set of  |
| 2026-10-30T16:41 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #59 from hanlinai/feat |
| 2026-10-30T16:41 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: score all candidates |
| 2026-10-30T16:41 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #176 from conjectures-i |
| 2026-10-30T16:41 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat(eval): KL decides a win, score per s |
| 2026-10-30T16:41 | sn102 | RELEASE | sn102 released v0.7.2: Merge pull request #299 from Connito-AI/feat/va |
| 2026-10-30T16:41 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #299 from Connito-AI/ |
| 2026-10-30T16:41 | sn126 | BURN_DROP | sn126 burn fell 1.000 -> 0.950 - miners can earn again |
| 2026-10-30T09:55 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Expose validator preparation stages throu |
| 2026-10-30T09:55 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5327 - [P1] Validator: a killed fille |
| 2026-10-30T09:55 | sn62 | RELEASE | sn62 released v0.3.15 |
| 2026-10-30T09:55 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #174 from conjectures-i |
| 2026-10-30T09:55 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

