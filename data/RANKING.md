# RANKING - generated 2026-08-16T16:38:05Z, block 8858460

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
| 1 | 107 | Minos | 78.4 | 1.0 | 121 | 34,113 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.1d ago |
| 2 | 76 | Phylax | 73.7 | 1.0 | 31.30 | 155 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.2d ago |
| 3 | 67 | Harnyx | 72.6 | 1.0 | 23.77 | 420 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.4d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.69 | 74.64 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.0d ago |
| 5 | 1 | Apex | 70.1 | 0.85 | 760 | 1,049 | rtx4090 | 0.553 | 4 | 55% | RELEASE 3.1d ago |
| 6 | 96 | Verathos | 70.1 | 1.0 | 33.95 | 209 | rtx4090 | 0.434 | 54 | 43% | RELEASE 1.8d ago |
| 7 | 41 | Almanac | 69.9 | 1.0 | 12.89 | 47.94 | cpu-small | 0.652 | 75 | 65% | SCORING_COMMIT 3.7d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 566 | 2,288 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.7d ago |
| 9 | 15 | ORO | 68.8 | 1.0 | 12.76 | 21.09 | cpu-small | 0.000 | 62 | 94% | SCORING_COMMIT 2.8d ago |
| 10 | 56 | Gradients | 68.7 | 0.85 | 506 | 963 | rtx4090 | 0.677 | 7 | 68% | SCORING_COMMIT 4.1d ago |
| 11 | 85 | Vidaio | 68.6 | 0.85 | 489 | 559 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 4.3d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 477 | 2,207 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.8d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.68 | 34.40 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.2d ago |
| 14 | 11 | TrajectoryRL | 67.1 | 0.85 | 4,144 | 4,144 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.04 | 1,327 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.0d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 225 | 721 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.1d ago |
| 17 | 2 | DSperse | 64.3 | 0.85 | 134 | 195 | rtx4090 | 0.822 | 4 | 82% | RELEASE 5.8d ago |
| 18 | 55 | NIOME | 61.5 | 0.85 | 57.16 | 482 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.8d ago |
| 19 | 60 | Bitsec.ai | 59.2 | 0.85 | 398 | 398 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 20 | 28 | gm | 58.8 | 0.85 | 27.13 | 2,401 | rtx4090 | 0.216 | 40 | 27% | RELEASE 4.1d ago |
| 21 | 74 | Gittensor | 58.5 | 0.85 | 25.77 | 209 | rtx4090 | 0.631 | 14 | 63% | RELEASE 4.9d ago |
| 22 | 51 | lium.io | 58.3 | 0.85 | 28.97 | 1,464 | rtx4090 | 0.000 | 52 | 82% | SCORING_COMMIT 2.3d ago |
| 23 | 61 | RedTeam | 57.3 | 0.85 | 16.11 | 426 | rtx4090 | 0.000 | 81 | 10% | RELEASE 5.4d ago |
| 24 | 120 | Affine | 55.8 | 0.6 | 11,084 | 11,084 | rtx4090 | 0.333 | 3 | 33% | SCORING_COMMIT 4.1d ago |
| 25 | 68 | NOVA | 55.1 | 0.6 | 8,068 | 8,068 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 244.95709383883235 |
| 54 | Yanez | -4.14 | a4000 | 951.7925518961383 |
| 104 | Masx.ai | -0.41 | rtx4090 | 9.261816043337602 |
| 75 | Hippius | -7.20 | rtx4090 | 11005.210763172057 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 132.9416568537632 |
| 13 | Data Universe | -3.57 | rtx4090 | 6.088137670776308 |
| 88 | Investing | -5.41 | rtx4090 | 1133.081217104148 |
| 8 | Vanta | -7.70 | rtx4090 | 2917.593062392341 |
| 114 | SOMA | -8.13 | rtx4090 | 604.2760625536503 |
| 43 | Graphite | -0.78 | cpu-small | 17.44303092793634 |
| 32 | ItsAI | -0.06 | rtx4090 | 10.683936353088164 |
| 18 | Zeus | -3.44 | rtx4090 | 1400.991291114464 |
| 22 | Desearch | -3.56 | rtx4090 | 51.467425903196684 |
| 45 | AlphaRidge.ai | -4.02 | rtx4090 | 14.662785216406691 |
| 123 | MANTIS | -6.18 | rtx4090 | 75.24298063920128 |
| 19 | blockmachine | -7.08 | rtx4090 | 479.9514045664795 |
| 63 | Enigma | -8.14 | rtx4090 | 5029.2175557406035 |
| 105 | Beam | -3.02 | rtx4090 | 110.75439808012409 |
| 84 | ansuz | -8.16 | rtx4090 | 441.07639013187355 |
| 34 | BitMind | -19.73 | a100-80 | 21.00218346312577 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.97 | 35.0 | 15.0 | 9.46 | 1.0 |
| 76 | 13.73 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.68 | 35.0 | 15.0 | 9.89 | 1.0 |
| 26 | 14.73 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 14.04 | 35.0 | 11.25 | 9.81 | 1.0 |
| 41 | 10.39 | 35.0 | 15.0 | 9.49 | 1.0 |
| 91 | 25.04 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.36 | 35.0 | 15.0 | 8.43 | 1.0 |
| 56 | 24.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.47 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.53 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 32.9 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.11 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.4 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 19.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.05 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.66 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.18 | 35.0 | 11.25 | 9.76 | 0.85 |
| 74 | 12.99 | 35.0 | 11.25 | 9.62 | 0.85 |
| 51 | 13.43 | 35.0 | 11.25 | 8.86 | 0.85 |
| 61 | 11.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 36.79 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.53 | 35.0 | 11.25 | 10.0 | 0.6 |
