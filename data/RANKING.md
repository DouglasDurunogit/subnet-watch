# RANKING - generated 2026-08-18T16:57:18Z, block 8872956

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
| 1 | 76 | Phylax | 78.2 | 1.0 | 98.17 | 190 | cpu-small | 0.000 | 10 | 20% | SCORING_COMMIT 2.2d ago |
| 2 | 21 | AdTAO | 76.5 | 1.0 | 66.31 | 269 | cpu-small | 0.301 | 16 | 30% | SCORING_COMMIT 0.0d ago |
| 3 | 67 | Harnyx | 71.9 | 1.0 | 19.89 | 424 | cpu-small | 0.062 | 131 | 13% | SCORING_COMMIT 0.3d ago |
| 4 | 26 | Perturb | 70.7 | 1.0 | 39.26 | 72.10 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 5.1d ago |
| 5 | 1 | Apex | 70.3 | 0.85 | 819 | 1,104 | rtx4090 | 0.524 | 4 | 52% | RELEASE 0.1d ago |
| 6 | 56 | Gradients | 69.5 | 0.85 | 635 | 932 | rtx4090 | 0.716 | 5 | 72% | SCORING_COMMIT 0.7d ago |
| 7 | 41 | Almanac | 69.0 | 1.0 | 10.52 | 35.94 | cpu-small | 0.668 | 75 | 67% | SCORING_COMMIT 5.8d ago |
| 8 | 91 | cascade | 68.7 | 0.85 | 501 | 2,027 | rtx4090 | 0.000 | 5 | 51% | README_TASK_DIFF 0.5d ago |
| 9 | 62 | Ridges | 68.4 | 0.85 | 453 | 2,100 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.8d ago |
| 10 | 38 | ChronoLLM | 67.5 | 0.85 | 146 | 3,092 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 5.0d ago |
| 11 | 15 | ORO | 67.5 | 1.0 | 10.21 | 19.61 | cpu-small | 0.000 | 67 | 95% | RELEASE 0.6d ago |
| 12 | 11 | TrajectoryRL | 67.0 | 0.85 | 4,064 | 4,064 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 16d ago |
| 13 | 96 | Verathos | 66.9 | 1.0 | 15.28 | 419 | rtx4090 | 0.405 | 79 | 41% | RELEASE 0.0d ago |
| 14 | 107 | Minos | 64.2 | 1.0 | 115 | 33,441 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 8d ago |
| 15 | 85 | Vidaio | 64.1 | 0.85 | 125 | 1,297 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 0.4d ago |
| 16 | 81 | Reliquary | 63.3 | 0.85 | 99.45 | 392 | rtx4090 | 0.000 | 34 | 9% | SCORING_COMMIT 0.1d ago |
| 17 | 53 | engy | 63.0 | 0.85 | 91.09 | 2,142 | rtx4090 | 0.000 | 144 | 11% | SCORING_COMMIT 0.1d ago |
| 18 | 55 | NIOME | 61.4 | 0.85 | 56.57 | 478 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 3.9d ago |
| 19 | 28 | gm | 60.5 | 0.85 | 43.94 | 2,369 | rtx4090 | 0.069 | 41 | 25% | RELEASE 0.1d ago |
| 20 | 51 | lium.io | 59.6 | 0.85 | 40.27 | 907 | rtx4090 | 0.000 | 55 | 80% | SCORING_COMMIT 0.3d ago |
| 21 | 60 | Bitsec.ai | 58.9 | 0.85 | 367 | 367 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 11d ago |
| 22 | 74 | Gittensor | 58.0 | 0.85 | 22.10 | 197 | rtx4090 | 0.631 | 14 | 63% | RELEASE 6.9d ago |
| 23 | 102 | ConnitoAI | 57.2 | 0.85 | 568 | 1,365 | rtx4090 | 0.250 | 7 | 27% | RELEASE 18d ago |
| 24 | 68 | NOVA | 55.0 | 0.6 | 7,955 | 7,955 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 2.1d ago |
| 25 | 120 | Affine | 54.5 | 0.6 | 6,304 | 6,304 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 6.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.94 | cpu-small | 285.1781784757262 |
| 54 | Yanez | -3.56 | a4000 | 957.0500159732344 |
| 123 | MANTIS | -6.09 | rtx4090 | 79.57820345718739 |
| 75 | Hippius | -6.25 | rtx4090 | 11089.99289109579 |
| 114 | SOMA | -8.12 | rtx4090 | 4108.2096356068105 |
| 89 | InfiniteQuant | -8.16 | rtx4090 | 169.2416931536983 |
| 101 | Tag101 | -0.14 | cpu-small | 2.1022504390763355 |
| 104 | Masx.ai | -2.12 | rtx4090 | 7.155644330510048 |
| 13 | Data Universe | -3.99 | rtx4090 | 4.820735717179523 |
| 88 | Investing | -5.25 | rtx4090 | 636.1892854175852 |
| 8 | Vanta | -7.97 | rtx4090 | 2797.745824984944 |
| 43 | Graphite | -0.83 | cpu-small | 22.376237159534675 |
| 32 | ItsAI | -0.35 | rtx4090 | 10.637569375666523 |
| 19 | blockmachine | -2.10 | rtx4090 | 528.4768594371554 |
| 22 | Desearch | -3.19 | rtx4090 | 56.392822094814434 |
| 18 | Zeus | -4.32 | rtx4090 | 1448.8824170564612 |
| 45 | AlphaRidge.ai | -5.51 | rtx4090 | 8.88736560640728 |
| 63 | Enigma | -8.15 | rtx4090 | 4653.883642936698 |
| 105 | Beam | -2.81 | rtx4090 | 70.61807584865242 |
| 84 | ansuz | -8.16 | rtx4090 | 0.059287823004396716 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 18.16 | 35.0 | 15.0 | 10.0 | 1.0 |
| 21 | 16.63 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.01 | 35.0 | 15.0 | 9.86 | 1.0 |
| 26 | 14.6 | 35.0 | 11.25 | 9.82 | 1.0 |
| 1 | 26.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 25.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.65 | 35.0 | 15.0 | 9.39 | 1.0 |
| 91 | 24.56 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 24.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.7 | 35.0 | 15.0 | 9.68 | 0.85 |
| 15 | 9.55 | 35.0 | 15.0 | 7.99 | 1.0 |
| 11 | 32.82 | 21.0 | 15.0 | 10.0 | 0.85 |
| 96 | 11.02 | 35.0 | 11.25 | 9.58 | 1.0 |
| 107 | 18.77 | 21.0 | 15.0 | 9.42 | 1.0 |
| 85 | 19.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 18.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 17.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.03 | 35.0 | 11.25 | 9.85 | 0.85 |
| 51 | 14.69 | 35.0 | 11.25 | 9.21 | 0.85 |
| 60 | 23.34 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.4 | 35.0 | 11.25 | 9.57 | 0.85 |
| 102 | 25.06 | 21.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.48 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.56 | 35.0 | 11.25 | 9.98 | 0.6 |
