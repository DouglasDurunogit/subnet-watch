# RANKING - generated 2026-08-09T07:15:16Z, block 8805255

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
| 1 | 11 | TrajectoryRL | 79.5 | 0.85 | 4,878 | 4,878 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.8d ago |
| 2 | 107 | Minos | 78.4 | 1.0 | 119 | 35,353 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.1d ago |
| 3 | 76 | Phylax | 76.7 | 1.0 | 67.27 | 203 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.4d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,252 | 1,252 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.5d ago |
| 5 | 67 | Harnyx | 70.7 | 1.0 | 15.12 | 864 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 2.1d ago |
| 6 | 1 | Apex | 70.2 | 0.85 | 795 | 1,639 | rtx4090 | 0.443 | 4 | 44% | RELEASE 1.5d ago |
| 7 | 91 | cascade | 70.2 | 0.85 | 780 | 2,668 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.1d ago |
| 8 | 100 | BASE | 69.9 | 0.85 | 721 | 1,516 | rtx4090 | 0.000 | 4 | 45% | SCORING_COMMIT 0.4d ago |
| 9 | 41 | Almanac | 69.4 | 1.0 | 11.53 | 30.36 | cpu-small | 0.723 | 67 | 72% | SCORING_COMMIT 2.3d ago |
| 10 | 26 | Perturb | 68.4 | 1.0 | 22.46 | 42.23 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 2.7d ago |
| 11 | 96 | Verathos | 68.4 | 1.0 | 22.34 | 283 | rtx4090 | 0.405 | 75 | 41% | RELEASE 0.6d ago |
| 12 | 62 | Ridges | 68.3 | 0.85 | 439 | 2,037 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.4d ago |
| 13 | 21 | AdTAO | 65.7 | 1.0 | 4.98 | 22.89 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.7d ago |
| 14 | 38 | ChronoLLM | 65.6 | 0.85 | 214 | 3,598 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.9d ago |
| 15 | 15 | ORO | 64.6 | 1.0 | 5.81 | 17.01 | cpu-small | 0.000 | 71 | 96% | RELEASE 2.9d ago |
| 16 | 80 | OpenRoboto | 64.5 | 0.85 | 142 | 518 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 1.1d ago |
| 17 | 61 | RedTeam | 62.4 | 0.85 | 75.95 | 217 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.2d ago |
| 18 | 51 | lium.io | 59.3 | 0.85 | 37.34 | 2,909 | rtx4090 | 0.000 | 48 | 69% | SCORING_COMMIT 1.5d ago |
| 19 | 6 | Numinous | 59.1 | 1.0 | 29.96 | 344 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 10d ago |
| 20 | 28 | gm | 58.3 | 0.85 | 23.56 | 2,720 | rtx4090 | 0.581 | 25 | 58% | RELEASE 1.4d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 478 | 1,007 | rtx4090 | 0.705 | 7 | 70% | SCORING_COMMIT 11d ago |
| 22 | 74 | Gittensor | 55.4 | 0.85 | 11.14 | 244 | rtx4090 | 0.630 | 16 | 63% | RELEASE 1.6d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,220 | 7,220 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.8d ago |
| 24 | 85 | Vidaio | 54.8 | 0.85 | 278 | 621 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 12d ago |
| 25 | 124 | Swarm | 53.9 | 0.85 | 218 | 664 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.85 | a4000 | 1019.1682502042996 |
| 104 | Masx.ai | -1.24 | rtx4090 | 8.461392793838503 |
| 13 | Data Universe | -2.74 | rtx4090 | 6.942140260639461 |
| 88 | Investing | -5.75 | rtx4090 | 487.1993227758005 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 131.69847310095096 |
| 8 | Vanta | -7.39 | rtx4090 | 3390.9784669506 |
| 19 | blockmachine | -1.65 | rtx4090 | 205.7248871679137 |
| 45 | AlphaRidge.ai | -2.26 | rtx4090 | 44.8183868179257 |
| 75 | Hippius | -4.44 | rtx4090 | 5.622885675665023 |
| 18 | Zeus | -4.90 | rtx4090 | 969.182945261353 |
| 123 | MANTIS | -6.20 | rtx4090 | 74.21389108082738 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07760935052389147 |
| 105 | Beam | -4.55 | rtx4090 | 169.1460874164403 |
| 84 | ansuz | -8.15 | rtx4090 | 503.3834186424701 |
| 34 | BitMind | -19.28 | a100-80 | 298.9507162948675 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 41 subnets: sn2, sn9, sn10, sn12, sn14, sn16, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.55 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.92 | 35.0 | 15.0 | 9.43 | 1.0 |
| 76 | 16.68 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.18 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 10.98 | 35.0 | 15.0 | 9.75 | 1.0 |
| 1 | 26.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.31 | 35.0 | 11.25 | 9.99 | 0.85 |
| 100 | 26.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.98 | 35.0 | 15.0 | 9.41 | 1.0 |
| 26 | 12.46 | 35.0 | 11.25 | 9.7 | 1.0 |
| 96 | 12.44 | 35.0 | 11.25 | 9.69 | 1.0 |
| 62 | 24.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 7.07 | 35.0 | 15.0 | 8.63 | 1.0 |
| 38 | 21.22 | 35.0 | 11.25 | 9.76 | 0.85 |
| 15 | 7.58 | 35.0 | 15.0 | 6.99 | 1.0 |
| 80 | 19.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.16 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.4 | 35.0 | 11.25 | 9.08 | 0.85 |
| 6 | 13.56 | 21.0 | 15.0 | 9.54 | 1.0 |
| 28 | 12.64 | 35.0 | 11.25 | 9.71 | 0.85 |
| 56 | 24.38 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.86 | 35.0 | 11.25 | 9.08 | 0.85 |
| 120 | 35.09 | 35.0 | 11.25 | 9.99 | 0.6 |
| 85 | 22.24 | 21.0 | 11.25 | 10.0 | 0.85 |
| 124 | 21.29 | 21.0 | 11.25 | 9.84 | 0.85 |
