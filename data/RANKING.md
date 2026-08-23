# RANKING - generated 2026-08-23T20:35:21Z, block 8910046

Weights: income 40 / new-challenge freshness 35 / resource cost 15 / registration 10.
Incentive structure is weight ZERO by explicit decision - it is reported per subnet
but never scored, and no incentive-structure subscore is published to re-weight.

Income is the MEDIAN non-owner, non-validator-permitted miner - what a newcomer
should actually expect. The best competitive miner is shown separately as the
ceiling: on a winner-take-all subnet the two differ by orders of magnitude (sn15
ORO's best clears $10k/day while its median earner makes $10.20), and scoring the
ceiling ranked winner-take-all subnets above genuinely open ones.

## TOP 25

| # | netuid | name | score | conf | net $/day (median) | ceiling $/day | machine | burn | earners | top1% | freshness |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 76 | Phylax | 77.1 | 1.0 | 77.10 | 86.31 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.2d ago |
| 2 | 102 | ConnitoAI | 73.0 | 0.85 | 1,809 | 1,809 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.0d ago |
| 3 | 67 | Harnyx | 73.0 | 1.0 | 26.16 | 838 | cpu-small | 0.026 | 125 | 20% | SCORING_COMMIT 2.4d ago |
| 4 | 62 | Ridges | 72.5 | 0.85 | 1,576 | 3,221 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.9d ago |
| 5 | 23 | Trishool | 72.5 | 0.85 | 604 | 604 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.7d ago |
| 6 | 15 | ORO | 72.1 | 1.0 | 27.83 | 47.54 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 1.9d ago |
| 7 | 56 | Gradients | 70.0 | 0.85 | 742 | 1,166 | rtx4090 | 0.731 | 5 | 73% | SCORING_COMMIT 5.9d ago |
| 8 | 91 | cascade | 70.0 | 0.85 | 741 | 2,988 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.9d ago |
| 9 | 1 | Apex | 69.0 | 0.85 | 547 | 1,234 | rtx4090 | 0.546 | 5 | 55% | RELEASE 2.2d ago |
| 10 | 96 | Verathos | 68.6 | 1.0 | 23.98 | 303 | rtx4090 | 0.402 | 90 | 40% | RELEASE 5.2d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.72 | 280 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.8d ago |
| 12 | 124 | Swarm | 66.8 | 0.85 | 297 | 2,585 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.3d ago |
| 13 | 38 | ChronoLLM | 66.8 | 0.85 | 123 | 1,679 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.0d ago |
| 14 | 108 | Prometheon | 65.5 | 0.85 | 194 | 199 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.3d ago |
| 15 | 107 | Minos | 65.3 | 1.0 | 152 | 45,068 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 16 | 81 | Reliquary | 65.2 | 0.85 | 178 | 263 | rtx4090 | 0.003 | 30 | 6% | SCORING_COMMIT 1.1d ago |
| 17 | 85 | Vidaio | 64.5 | 0.85 | 144 | 447 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.6d ago |
| 18 | 60 | Bitsec.ai | 61.9 | 0.85 | 883 | 1,237 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 19 | 51 | lium.io | 60.8 | 0.85 | 56.39 | 2,081 | rtx4090 | 0.000 | 54 | 73% | SCORING_COMMIT 3.5d ago |
| 20 | 53 | engy | 60.3 | 0.85 | 40.65 | 13,427 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.7d ago |
| 21 | 28 | gm | 59.9 | 0.85 | 37.65 | 1,712 | rtx4090 | 0.141 | 52 | 14% | RELEASE 3.3d ago |
| 22 | 61 | RedTeam | 57.2 | 0.85 | 15.37 | 316 | rtx4090 | 0.000 | 85 | 6% | RELEASE 1.5d ago |
| 23 | 41 | Almanac | 56.6 | 1.0 | 15.55 | 30.40 | cpu-small | 0.643 | 79 | 64% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 55.0 | 0.6 | 7,757 | 7,757 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.0d ago |
| 25 | 33 | ReadyAI | 54.5 | 0.85 | 7.19 | 12.59 | rtx4090 | 0.000 | 244 | 1% | SCORING_COMMIT 3.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.26 | a4000 | 1257.1230487142127 |
| 13 | Data Universe | -2.45 | rtx4090 | 7.823636726812477 |
| 18 | Zeus | -3.02 | rtx4090 | 1968.1283993265022 |
| 89 | InfiniteQuant | -3.76 | rtx4090 | 120.43321255288157 |
| 123 | MANTIS | -5.57 | rtx4090 | 123.40123662450944 |
| 75 | Hippius | -5.95 | rtx4090 | 12781.054927225634 |
| 34 | BitMind | -18.79 | a100-80 | 353.7748462365494 |
| 6 | Numinous | -0.92 | cpu-small | 193.81465469337118 |
| 50 | Synth | -1.01 | rtx4090 | 68.14668383475093 |
| 104 | Masx.ai | -1.32 | rtx4090 | 11.696436476080441 |
| 88 | Investing | -2.57 | rtx4090 | 707.9048099260739 |
| 8 | Vanta | -7.30 | rtx4090 | 3625.492447360924 |
| 43 | Graphite | -0.23 | cpu-small | 194.80139782903078 |
| 19 | blockmachine | -0.22 | rtx4090 | 697.4415478295017 |
| 45 | AlphaRidge.ai | -4.79 | rtx4090 | 11.114171794866646 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08916879766922205 |
| 105 | Beam | -1.52 | rtx4090 | 87.68067725644967 |
| 84 | ansuz | -8.14 | rtx4090 | 0.07438783570843378 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.21 | 35.0 | 15.0 | 9.89 | 1.0 |
| 102 | 29.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 13.04 | 35.0 | 15.0 | 9.91 | 1.0 |
| 62 | 29.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.3 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 13.28 | 35.0 | 15.0 | 8.82 | 1.0 |
| 56 | 26.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.11 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.71 | 35.0 | 11.25 | 9.66 | 1.0 |
| 26 | 11.97 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.51 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 19.04 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.83 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.87 | 21.0 | 15.0 | 9.47 | 1.0 |
| 81 | 20.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.8 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 16.0 | 35.0 | 11.25 | 9.28 | 0.85 |
| 53 | 14.73 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.44 | 35.0 | 11.25 | 9.78 | 0.85 |
| 61 | 11.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 11.08 | 21.0 | 15.0 | 9.48 | 1.0 |
| 120 | 35.38 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 8.31 | 35.0 | 11.25 | 9.52 | 0.85 |
