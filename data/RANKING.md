# RANKING - generated 2026-08-16T19:07:48Z, block 8859209

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
| 1 | 107 | Minos | 78.2 | 1.0 | 116 | 33,559 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.2d ago |
| 2 | 67 | Harnyx | 72.5 | 1.0 | 23.59 | 417 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.5d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.64 | 74.55 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.2d ago |
| 4 | 1 | Apex | 70.0 | 0.85 | 751 | 1,038 | rtx4090 | 0.558 | 4 | 56% | RELEASE 3.2d ago |
| 5 | 76 | Phylax | 70.0 | 1.0 | 11.51 | 156 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.3d ago |
| 6 | 41 | Almanac | 69.9 | 1.0 | 12.83 | 47.89 | cpu-small | 0.653 | 75 | 65% | SCORING_COMMIT 3.8d ago |
| 7 | 96 | Verathos | 69.8 | 1.0 | 31.31 | 269 | rtx4090 | 0.409 | 62 | 41% | RELEASE 2.0d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 566 | 2,288 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.8d ago |
| 9 | 85 | Vidaio | 68.8 | 0.85 | 518 | 685 | rtx4090 | 0.000 | 10 | 22% | SCORING_COMMIT 0.1d ago |
| 10 | 15 | ORO | 68.8 | 1.0 | 12.65 | 20.92 | cpu-small | 0.000 | 64 | 94% | SCORING_COMMIT 2.9d ago |
| 11 | 56 | Gradients | 68.7 | 0.85 | 505 | 962 | rtx4090 | 0.678 | 7 | 68% | SCORING_COMMIT 4.2d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 476 | 2,207 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.9d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.67 | 34.37 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.3d ago |
| 14 | 11 | TrajectoryRL | 67.1 | 0.85 | 4,168 | 4,168 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 98.14 | 1,342 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.1d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 225 | 722 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.2d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.70 | 479 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.0d ago |
| 18 | 28 | gm | 61.1 | 0.85 | 52.91 | 2,655 | rtx4090 | 0.045 | 41 | 30% | RELEASE 4.2d ago |
| 19 | 2 | DSperse | 60.7 | 0.85 | 46.00 | 144 | rtx4090 | 0.822 | 6 | 82% | RELEASE 5.9d ago |
| 20 | 102 | ConnitoAI | 59.8 | 0.85 | 1,233 | 1,427 | rtx4090 | 0.250 | 5 | 27% | RELEASE 16d ago |
| 21 | 60 | Bitsec.ai | 59.0 | 0.85 | 373 | 373 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 22 | 51 | lium.io | 58.5 | 0.85 | 30.60 | 2,510 | rtx4090 | 0.000 | 53 | 77% | SCORING_COMMIT 2.4d ago |
| 23 | 74 | Gittensor | 58.4 | 0.85 | 24.97 | 209 | rtx4090 | 0.631 | 14 | 63% | RELEASE 5.0d ago |
| 24 | 61 | RedTeam | 57.0 | 0.85 | 14.47 | 404 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.5d ago |
| 25 | 120 | Affine | 55.2 | 0.6 | 8,394 | 8,394 | rtx4090 | 0.254 | 4 | 25% | SCORING_COMMIT 4.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 244.13901029898375 |
| 54 | Yanez | -3.90 | a4000 | 950.1644024231517 |
| 104 | Masx.ai | -0.65 | rtx4090 | 10.64549905022137 |
| 75 | Hippius | -7.38 | rtx4090 | 10875.483027708899 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 134.2611067322121 |
| 101 | Tag101 | -0.03 | cpu-small | 1.9936445776229874 |
| 13 | Data Universe | -3.41 | rtx4090 | 5.854619937675666 |
| 88 | Investing | -5.46 | rtx4090 | 1114.6614137823583 |
| 8 | Vanta | -7.70 | rtx4090 | 2916.533533501773 |
| 114 | SOMA | -8.13 | rtx4090 | 614.9376363686716 |
| 43 | Graphite | -0.78 | cpu-small | 16.725803681033902 |
| 45 | AlphaRidge.ai | -2.44 | rtx4090 | 21.132805369406906 |
| 22 | Desearch | -2.98 | rtx4090 | 53.307876211600835 |
| 18 | Zeus | -3.45 | rtx4090 | 1399.3042575105965 |
| 123 | MANTIS | -6.18 | rtx4090 | 74.8881629844734 |
| 19 | blockmachine | -7.08 | rtx4090 | 437.9800410046628 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07593173494733288 |
| 105 | Beam | -2.96 | rtx4090 | 115.93472784056347 |
| 84 | ansuz | -8.16 | rtx4090 | 440.4290498431262 |
| 34 | BitMind | -20.06 | a100-80 | 21.520791618094492 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.8 | 35.0 | 15.0 | 9.44 | 1.0 |
| 67 | 12.65 | 35.0 | 15.0 | 9.89 | 1.0 |
| 26 | 14.73 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.16 | 35.0 | 11.25 | 10.0 | 0.85 |
| 76 | 9.98 | 35.0 | 15.0 | 10.0 | 1.0 |
| 41 | 10.38 | 35.0 | 15.0 | 9.49 | 1.0 |
| 96 | 13.73 | 35.0 | 11.25 | 9.79 | 1.0 |
| 91 | 25.04 | 35.0 | 11.25 | 9.99 | 0.85 |
| 85 | 24.69 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 10.32 | 35.0 | 15.0 | 8.51 | 1.0 |
| 56 | 24.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.53 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 32.92 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.16 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.41 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.75 | 35.0 | 11.25 | 9.88 | 0.85 |
| 2 | 15.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 28.11 | 21.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.4 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 13.64 | 35.0 | 11.25 | 8.93 | 0.85 |
| 74 | 12.86 | 35.0 | 11.25 | 9.6 | 0.85 |
| 61 | 10.82 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.69 | 35.0 | 11.25 | 9.99 | 0.6 |
