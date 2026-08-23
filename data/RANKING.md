# RANKING - generated 2026-08-23T22:00:03Z, block 8910469

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 76.98 | 86.18 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.2d ago |
| 2 | 102 | ConnitoAI | 73.0 | 0.85 | 1,816 | 1,816 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.1d ago |
| 3 | 67 | Harnyx | 72.9 | 1.0 | 26.14 | 837 | cpu-small | 0.020 | 127 | 20% | SCORING_COMMIT 2.5d ago |
| 4 | 62 | Ridges | 72.5 | 0.85 | 1,560 | 3,188 | rtx4090 | 0.000 | 6 | 39% | RELEASE 5.0d ago |
| 5 | 23 | Trishool | 72.5 | 0.85 | 600 | 600 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.8d ago |
| 6 | 15 | ORO | 71.9 | 1.0 | 27.54 | 47.06 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 1.9d ago |
| 7 | 56 | Gradients | 70.0 | 0.85 | 740 | 1,165 | rtx4090 | 0.731 | 5 | 73% | SCORING_COMMIT 5.9d ago |
| 8 | 91 | cascade | 70.0 | 0.85 | 733 | 2,958 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 3.0d ago |
| 9 | 1 | Apex | 69.0 | 0.85 | 544 | 1,227 | rtx4090 | 0.549 | 5 | 55% | RELEASE 2.3d ago |
| 10 | 96 | Verathos | 68.6 | 1.0 | 23.85 | 315 | rtx4090 | 0.403 | 90 | 40% | RELEASE 5.2d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.70 | 280 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.8d ago |
| 12 | 124 | Swarm | 66.8 | 0.85 | 297 | 2,582 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.4d ago |
| 13 | 38 | ChronoLLM | 66.8 | 0.85 | 123 | 1,676 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.0d ago |
| 14 | 108 | Prometheon | 65.5 | 0.85 | 194 | 199 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.3d ago |
| 15 | 107 | Minos | 65.5 | 1.0 | 159 | 44,617 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 16 | 81 | Reliquary | 65.3 | 0.85 | 182 | 272 | rtx4090 | 0.002 | 30 | 6% | SCORING_COMMIT 1.2d ago |
| 17 | 85 | Vidaio | 64.5 | 0.85 | 143 | 444 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.6d ago |
| 18 | 60 | Bitsec.ai | 61.5 | 0.85 | 787 | 1,106 | cpu-small | 0.555 | 3 | 55% | SCORING_COMMIT 16d ago |
| 19 | 51 | lium.io | 60.7 | 0.85 | 55.50 | 2,069 | rtx4090 | 0.000 | 53 | 75% | SCORING_COMMIT 3.6d ago |
| 20 | 53 | engy | 60.3 | 0.85 | 40.26 | 338 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.7d ago |
| 21 | 28 | gm | 59.1 | 0.85 | 30.13 | 1,799 | rtx4090 | 0.135 | 54 | 15% | RELEASE 3.3d ago |
| 22 | 61 | RedTeam | 57.1 | 0.85 | 15.11 | 315 | rtx4090 | 0.000 | 83 | 6% | RELEASE 1.6d ago |
| 23 | 41 | Almanac | 56.4 | 1.0 | 15.06 | 29.59 | cpu-small | 0.653 | 79 | 65% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 55.0 | 0.6 | 7,742 | 7,742 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.1d ago |
| 25 | 33 | ReadyAI | 54.5 | 0.85 | 7.22 | 11.44 | rtx4090 | 0.000 | 246 | 1% | SCORING_COMMIT 3.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.32 | a4000 | 1236.2619121077373 |
| 13 | Data Universe | -2.46 | rtx4090 | 7.485057684323241 |
| 18 | Zeus | -3.66 | rtx4090 | 1722.189867218384 |
| 89 | InfiniteQuant | -3.84 | rtx4090 | 120.21075917023666 |
| 123 | MANTIS | -5.58 | rtx4090 | 123.16293545987463 |
| 75 | Hippius | -5.93 | rtx4090 | 12856.422541610464 |
| 34 | BitMind | -17.32 | a100-80 | 353.48010666218335 |
| 6 | Numinous | -0.92 | cpu-small | 193.6317072581293 |
| 50 | Synth | -0.78 | rtx4090 | 68.45474624530465 |
| 104 | Masx.ai | -1.71 | rtx4090 | 11.781111727072409 |
| 88 | Investing | -2.56 | rtx4090 | 709.2610572030615 |
| 8 | Vanta | -7.31 | rtx4090 | 3432.618991206837 |
| 43 | Graphite | -0.47 | cpu-small | 202.66571266917165 |
| 19 | blockmachine | -0.15 | rtx4090 | 703.9323960005519 |
| 22 | Desearch | -1.41 | rtx4090 | 104.70388274608699 |
| 45 | AlphaRidge.ai | -4.28 | rtx4090 | 11.377480576933666 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08908284949745358 |
| 105 | Beam | -1.53 | rtx4090 | 87.58666985235965 |
| 84 | ansuz | -8.14 | rtx4090 | 539.7897860677854 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.21 | 35.0 | 15.0 | 9.89 | 1.0 |
| 102 | 29.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 13.04 | 35.0 | 15.0 | 9.9 | 1.0 |
| 62 | 29.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.28 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 13.24 | 35.0 | 15.0 | 8.67 | 1.0 |
| 56 | 26.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.69 | 35.0 | 11.25 | 9.66 | 1.0 |
| 26 | 11.97 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.5 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 19.03 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.83 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 20.04 | 21.0 | 15.0 | 9.49 | 1.0 |
| 81 | 20.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.62 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.34 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 15.93 | 35.0 | 11.25 | 9.27 | 0.85 |
| 53 | 14.69 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.58 | 35.0 | 11.25 | 9.73 | 0.85 |
| 61 | 10.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.97 | 21.0 | 15.0 | 9.46 | 1.0 |
| 120 | 35.37 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 8.32 | 35.0 | 11.25 | 9.58 | 0.85 |
