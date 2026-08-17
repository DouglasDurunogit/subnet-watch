# RANKING - generated 2026-08-17T05:07:30Z, block 8862207

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
| 1 | 107 | Minos | 78.1 | 1.0 | 113 | 32,873 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.6d ago |
| 2 | 67 | Harnyx | 72.0 | 1.0 | 20.94 | 391 | cpu-small | 0.008 | 128 | 11% | SCORING_COMMIT 1.0d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.70 | 74.65 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.6d ago |
| 4 | 1 | Apex | 70.6 | 0.85 | 882 | 989 | rtx4090 | 0.538 | 4 | 54% | RELEASE 3.6d ago |
| 5 | 76 | Phylax | 70.6 | 1.0 | 13.47 | 157 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.7d ago |
| 6 | 85 | Vidaio | 69.7 | 0.85 | 672 | 834 | rtx4090 | 0.000 | 10 | 27% | SCORING_COMMIT 0.5d ago |
| 7 | 96 | Verathos | 69.6 | 1.0 | 29.83 | 422 | rtx4090 | 0.407 | 55 | 41% | RELEASE 2.4d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 570 | 2,304 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 3.2d ago |
| 9 | 15 | ORO | 68.8 | 1.0 | 12.70 | 21.55 | cpu-small | 0.000 | 67 | 94% | SCORING_COMMIT 3.3d ago |
| 10 | 56 | Gradients | 68.7 | 0.85 | 503 | 961 | rtx4090 | 0.682 | 7 | 68% | SCORING_COMMIT 4.6d ago |
| 11 | 41 | Almanac | 68.7 | 1.0 | 9.71 | 53.61 | cpu-small | 0.695 | 75 | 70% | SCORING_COMMIT 4.3d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 467 | 2,162 | rtx4090 | 0.000 | 6 | 40% | RELEASE 2.3d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.66 | 34.33 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.7d ago |
| 14 | 38 | ChronoLLM | 66.1 | 0.85 | 100 | 1,372 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.5d ago |
| 15 | 124 | Swarm | 65.9 | 0.85 | 225 | 721 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.6d ago |
| 16 | 98 | NeverPlayAlone | 64.1 | 0.85 | 1,696 | 1,696 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 10d ago |
| 17 | 55 | NIOME | 61.5 | 0.85 | 57.29 | 478 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.4d ago |
| 18 | 60 | Bitsec.ai | 59.0 | 0.85 | 373 | 373 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 19 | 28 | gm | 58.9 | 0.85 | 28.21 | 2,321 | rtx4090 | 0.220 | 39 | 25% | RELEASE 4.6d ago |
| 20 | 74 | Gittensor | 58.3 | 0.85 | 23.91 | 214 | rtx4090 | 0.630 | 14 | 63% | RELEASE 5.4d ago |
| 21 | 61 | RedTeam | 57.1 | 0.85 | 14.71 | 408 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.9d ago |
| 22 | 68 | NOVA | 55.1 | 0.6 | 8,068 | 8,068 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.6d ago |
| 23 | 120 | Affine | 54.6 | 0.6 | 6,596 | 6,596 | rtx4090 | 0.200 | 5 | 20% | SCORING_COMMIT 4.6d ago |
| 24 | 51 | lium.io | 54.6 | 0.85 | 13.26 | 2,519 | rtx4090 | 0.000 | 58 | 79% | SCORING_COMMIT 2.8d ago |
| 25 | 93 | Bitcast | 54.4 | 0.85 | 245 | 461 | rtx4090 | 0.000 | 4 | 84% | SCORING_COMMIT 19d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 226.7114629017263 |
| 54 | Yanez | -4.39 | a4000 | 953.9030681157149 |
| 75 | Hippius | -7.21 | rtx4090 | 10887.272237617519 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 151.79809328787826 |
| 13 | Data Universe | -3.69 | rtx4090 | 6.240192158576596 |
| 88 | Investing | -5.20 | rtx4090 | 268.7406157929102 |
| 8 | Vanta | -7.96 | rtx4090 | 2855.6992521184025 |
| 114 | SOMA | -8.12 | rtx4090 | 638.2592131737515 |
| 43 | Graphite | -0.78 | cpu-small | 16.711150760520948 |
| 45 | AlphaRidge.ai | -3.79 | rtx4090 | 16.921387457597675 |
| 22 | Desearch | -4.43 | rtx4090 | 57.00817153947056 |
| 18 | Zeus | -5.28 | rtx4090 | 1176.2215919791697 |
| 123 | MANTIS | -6.16 | rtx4090 | 75.77737800433462 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07659126641432713 |
| 105 | Beam | -2.94 | rtx4090 | 111.11128747577227 |
| 84 | ansuz | -8.16 | rtx4090 | 438.92994329777036 |
| 34 | BitMind | -19.85 | a100-80 | 28.588085489809423 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.72 | 35.0 | 15.0 | 9.43 | 1.0 |
| 67 | 12.2 | 35.0 | 15.0 | 9.84 | 1.0 |
| 26 | 14.74 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 76 | 10.55 | 35.0 | 15.0 | 10.0 | 1.0 |
| 85 | 25.72 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 13.54 | 35.0 | 11.25 | 9.78 | 1.0 |
| 91 | 25.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.34 | 35.0 | 15.0 | 8.5 | 1.0 |
| 56 | 24.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.37 | 35.0 | 15.0 | 9.32 | 1.0 |
| 62 | 24.28 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.53 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.24 | 35.0 | 15.0 | 9.52 | 0.85 |
| 124 | 21.4 | 35.0 | 11.25 | 9.85 | 0.85 |
| 98 | 29.37 | 21.0 | 15.0 | 10.0 | 0.85 |
| 55 | 16.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.4 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.33 | 35.0 | 11.25 | 9.77 | 0.85 |
| 74 | 12.7 | 35.0 | 11.25 | 9.59 | 0.85 |
| 61 | 10.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.53 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.74 | 35.0 | 11.25 | 9.99 | 0.6 |
| 51 | 10.5 | 35.0 | 11.25 | 7.52 | 0.85 |
| 93 | 21.75 | 21.0 | 11.25 | 10.0 | 0.85 |
