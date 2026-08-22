# RANKING - generated 2026-08-22T18:00:16Z, block 8902070

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 75.73 | 134 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.3d ago |
| 2 | 67 | Harnyx | 72.4 | 1.0 | 23.07 | 119 | cpu-small | 0.052 | 151 | 12% | SCORING_COMMIT 1.3d ago |
| 3 | 62 | Ridges | 71.7 | 0.85 | 1,221 | 3,006 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.8d ago |
| 4 | 56 | Gradients | 70.0 | 0.85 | 735 | 1,081 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.7d ago |
| 5 | 15 | ORO | 70.0 | 1.0 | 18.85 | 22,477 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.8d ago |
| 6 | 102 | ConnitoAI | 69.8 | 0.85 | 702 | 2,214 | rtx4090 | 0.250 | 7 | 32% | RELEASE 1.1d ago |
| 7 | 91 | cascade | 69.7 | 0.85 | 686 | 2,770 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.8d ago |
| 8 | 1 | Apex | 68.7 | 0.85 | 503 | 1,284 | rtx4090 | 0.513 | 5 | 51% | RELEASE 1.1d ago |
| 9 | 11 | TrajectoryRL | 67.5 | 0.85 | 4,653 | 4,653 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 10 | 26 | Perturb | 67.5 | 1.0 | 18.06 | 259 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.7d ago |
| 11 | 96 | Verathos | 67.2 | 1.0 | 16.84 | 460 | rtx4090 | 0.405 | 95 | 41% | RELEASE 4.1d ago |
| 12 | 38 | ChronoLLM | 66.6 | 0.85 | 115 | 1,576 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.9d ago |
| 13 | 107 | Minos | 65.2 | 1.0 | 151 | 43,984 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 14 | 85 | Vidaio | 64.3 | 0.85 | 136 | 401 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.4d ago |
| 15 | 108 | Prometheon | 63.9 | 0.85 | 120 | 129 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.2d ago |
| 16 | 81 | Reliquary | 63.7 | 0.85 | 114 | 215 | rtx4090 | 0.003 | 39 | 5% | SCORING_COMMIT 0.0d ago |
| 17 | 28 | gm | 60.7 | 0.85 | 46.83 | 1,705 | rtx4090 | 0.031 | 55 | 15% | RELEASE 2.2d ago |
| 18 | 51 | lium.io | 60.6 | 0.85 | 52.76 | 4,591 | rtx4090 | 0.000 | 53 | 68% | SCORING_COMMIT 2.4d ago |
| 19 | 60 | Bitsec.ai | 59.9 | 0.85 | 490 | 490 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 20 | 53 | engy | 59.6 | 0.85 | 32.56 | 220 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.6d ago |
| 21 | 61 | RedTeam | 57.7 | 0.85 | 18.14 | 282 | rtx4090 | 0.000 | 87 | 6% | RELEASE 0.4d ago |
| 22 | 41 | Almanac | 55.4 | 1.0 | 11.64 | 24.21 | cpu-small | 0.726 | 78 | 73% | SCORING_COMMIT 10d ago |
| 23 | 68 | NOVA | 55.3 | 0.6 | 8,784 | 8,784 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.2d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,182 | 7,182 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.9d ago |
| 25 | 124 | Swarm | 54.6 | 0.85 | 270 | 2,356 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.28 | a4000 | 1223.7287629797393 |
| 13 | Data Universe | -2.75 | rtx4090 | 6.567362624136035 |
| 89 | InfiniteQuant | -2.88 | rtx4090 | 120.93338376653068 |
| 18 | Zeus | -4.34 | rtx4090 | 1734.9440583383393 |
| 123 | MANTIS | -5.53 | rtx4090 | 110.81254270429922 |
| 75 | Hippius | -6.25 | rtx4090 | 11552.184275053678 |
| 34 | BitMind | -19.85 | a100-80 | 327.0789568899961 |
| 6 | Numinous | -0.94 | cpu-small | 290.5982351155691 |
| 104 | Masx.ai | -0.46 | rtx4090 | 8.739089281922052 |
| 50 | Synth | -1.36 | rtx4090 | 71.24047803246859 |
| 88 | Investing | -3.15 | rtx4090 | 696.4953183793101 |
| 8 | Vanta | -7.37 | rtx4090 | 1091.8895314567499 |
| 43 | Graphite | -0.45 | cpu-small | 192.9141597723506 |
| 19 | blockmachine | -1.35 | rtx4090 | 545.7213720981064 |
| 45 | AlphaRidge.ai | -4.64 | rtx4090 | 11.893472925826016 |
| 22 | Desearch | -4.89 | rtx4090 | 98.1087287547451 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08363633509403397 |
| 105 | Beam | -2.18 | rtx4090 | 81.96714094886369 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07037199759663154 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.14 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.57 | 35.0 | 15.0 | 9.8 | 1.0 |
| 62 | 28.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 26.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.8 | 35.0 | 15.0 | 8.21 | 1.0 |
| 102 | 25.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.8 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.36 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.64 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.38 | 35.0 | 11.25 | 9.55 | 1.0 |
| 38 | 18.79 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.83 | 21.0 | 15.0 | 9.38 | 1.0 |
| 85 | 19.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.93 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.73 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.28 | 35.0 | 11.25 | 9.84 | 0.85 |
| 51 | 15.74 | 35.0 | 11.25 | 9.29 | 0.85 |
| 60 | 24.47 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.66 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.02 | 21.0 | 15.0 | 9.35 | 1.0 |
| 68 | 35.87 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.07 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.13 | 21.0 | 11.25 | 9.86 | 0.85 |
