# RANKING - generated 2026-08-23T17:03:46Z, block 8908988

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
| 1 | 76 | Phylax | 76.9 | 1.0 | 73.57 | 82.37 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.0d ago |
| 2 | 67 | Harnyx | 72.7 | 1.0 | 24.89 | 798 | cpu-small | 0.026 | 125 | 20% | SCORING_COMMIT 2.3d ago |
| 3 | 23 | Trishool | 72.3 | 0.85 | 573 | 573 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.5d ago |
| 4 | 102 | ConnitoAI | 72.0 | 0.85 | 1,336 | 2,493 | rtx4090 | 0.252 | 5 | 36% | RELEASE 2.0d ago |
| 5 | 62 | Ridges | 71.8 | 0.85 | 1,257 | 3,095 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.8d ago |
| 6 | 15 | ORO | 70.5 | 1.0 | 25.20 | 43.46 | cpu-small | 0.000 | 79 | 93% | SCORING_COMMIT 1.7d ago |
| 7 | 56 | Gradients | 69.9 | 0.85 | 709 | 1,113 | rtx4090 | 0.730 | 5 | 73% | SCORING_COMMIT 5.7d ago |
| 8 | 91 | cascade | 69.0 | 0.85 | 546 | 1,469 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.7d ago |
| 9 | 1 | Apex | 68.8 | 0.85 | 522 | 1,194 | rtx4090 | 0.540 | 5 | 54% | RELEASE 2.1d ago |
| 10 | 96 | Verathos | 68.3 | 1.0 | 22.25 | 292 | rtx4090 | 0.402 | 89 | 40% | RELEASE 5.0d ago |
| 11 | 26 | Perturb | 67.6 | 1.0 | 18.77 | 268 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.6d ago |
| 12 | 124 | Swarm | 66.7 | 0.85 | 285 | 2,484 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.2d ago |
| 13 | 38 | ChronoLLM | 66.6 | 0.85 | 117 | 1,599 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.8d ago |
| 14 | 108 | Prometheon | 65.4 | 0.85 | 187 | 205 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.1d ago |
| 15 | 107 | Minos | 65.4 | 1.0 | 153 | 43,616 | cpu-small | 0.000 | 20 | 89% | README_TASK_DIFF 13d ago |
| 16 | 85 | Vidaio | 64.6 | 0.85 | 147 | 426 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.4d ago |
| 17 | 81 | Reliquary | 64.6 | 0.85 | 146 | 267 | rtx4090 | 0.011 | 36 | 6% | SCORING_COMMIT 1.0d ago |
| 18 | 51 | lium.io | 61.0 | 0.85 | 58.77 | 2,043 | rtx4090 | 0.000 | 53 | 73% | SCORING_COMMIT 3.4d ago |
| 19 | 53 | engy | 60.2 | 0.85 | 38.49 | 12,834 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.5d ago |
| 20 | 60 | Bitsec.ai | 60.0 | 0.85 | 507 | 507 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 21 | 28 | gm | 59.4 | 0.85 | 32.93 | 1,517 | rtx4090 | 0.137 | 55 | 14% | RELEASE 3.1d ago |
| 22 | 61 | RedTeam | 57.1 | 0.85 | 14.85 | 300 | rtx4090 | 0.000 | 85 | 6% | RELEASE 1.4d ago |
| 23 | 41 | Almanac | 56.4 | 1.0 | 14.95 | 29.13 | cpu-small | 0.640 | 79 | 64% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,390 | 7,390 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.9d ago |
| 25 | 33 | ReadyAI | 54.0 | 0.85 | 6.47 | 11.72 | rtx4090 | 0.000 | 244 | 1% | SCORING_COMMIT 3.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.24 | a4000 | 1216.9568524236736 |
| 89 | InfiniteQuant | -1.21 | rtx4090 | 115.22264999670162 |
| 13 | Data Universe | -2.79 | rtx4090 | 7.645779107353823 |
| 18 | Zeus | -3.35 | rtx4090 | 1840.8825041831494 |
| 123 | MANTIS | -5.62 | rtx4090 | 120.45509448404533 |
| 75 | Hippius | -6.34 | rtx4090 | 12132.009267835063 |
| 34 | BitMind | -19.24 | a100-80 | 337.07914069271334 |
| 6 | Numinous | -0.93 | cpu-small | 182.48498723760892 |
| 50 | Synth | -1.35 | rtx4090 | 65.52804025232324 |
| 88 | Investing | -2.64 | rtx4090 | 698.6219271823173 |
| 104 | Masx.ai | -2.69 | rtx4090 | 11.878864669090477 |
| 8 | Vanta | -7.35 | rtx4090 | 3283.2005726116035 |
| 43 | Graphite | -0.26 | cpu-small | 185.7162810106381 |
| 19 | blockmachine | -0.79 | rtx4090 | 567.4804165298792 |
| 22 | Desearch | -1.08 | rtx4090 | 47.37278286184791 |
| 77 | Liquidity | -1.88 | rtx4090 | 1002.8389991190897 |
| 45 | AlphaRidge.ai | -4.43 | rtx4090 | 11.340886458077609 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08555661513574471 |
| 105 | Beam | -1.91 | rtx4090 | 83.97936655787183 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07078328166962171 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.03 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 12.85 | 35.0 | 15.0 | 9.87 | 1.0 |
| 23 | 25.09 | 35.0 | 15.0 | 9.99 | 0.85 |
| 102 | 28.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 28.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 12.9 | 35.0 | 15.0 | 7.62 | 1.0 |
| 56 | 25.93 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.9 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.73 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.43 | 35.0 | 11.25 | 9.65 | 1.0 |
| 26 | 11.79 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.35 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.85 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.68 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.89 | 21.0 | 15.0 | 9.5 | 1.0 |
| 85 | 19.75 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 19.72 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.16 | 35.0 | 11.25 | 9.34 | 0.85 |
| 53 | 14.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.61 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.92 | 35.0 | 11.25 | 9.76 | 0.85 |
| 61 | 10.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.94 | 21.0 | 15.0 | 9.48 | 1.0 |
| 120 | 35.19 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 7.94 | 35.0 | 11.25 | 9.39 | 0.85 |
