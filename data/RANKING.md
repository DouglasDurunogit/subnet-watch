# RANKING - generated 2026-08-17T13:02:50Z, block 8864584

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
| 1 | 76 | Phylax | 78.4 | 1.0 | 104 | 202 | cpu-small | 0.000 | 10 | 20% | SCORING_COMMIT 1.0d ago |
| 2 | 107 | Minos | 78.3 | 1.0 | 117 | 33,470 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.9d ago |
| 3 | 67 | Harnyx | 72.0 | 1.0 | 20.53 | 385 | cpu-small | 0.000 | 129 | 11% | SCORING_COMMIT 0.1d ago |
| 4 | 26 | Perturb | 71.2 | 1.0 | 45.10 | 1,612 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.9d ago |
| 5 | 91 | cascade | 69.1 | 0.85 | 572 | 2,311 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 3.6d ago |
| 6 | 96 | Verathos | 68.9 | 1.0 | 25.26 | 505 | rtx4090 | 0.408 | 63 | 41% | RELEASE 2.7d ago |
| 7 | 41 | Almanac | 68.7 | 1.0 | 9.76 | 53.22 | cpu-small | 0.691 | 75 | 69% | SCORING_COMMIT 4.6d ago |
| 8 | 62 | Ridges | 68.4 | 0.85 | 466 | 2,159 | rtx4090 | 0.000 | 6 | 40% | RELEASE 2.6d ago |
| 9 | 15 | ORO | 67.9 | 1.0 | 10.84 | 12,357 | cpu-small | 0.000 | 66 | 94% | SCORING_COMMIT 3.6d ago |
| 10 | 85 | Vidaio | 67.7 | 0.85 | 376 | 533 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 0.1d ago |
| 11 | 21 | AdTAO | 67.6 | 1.0 | 7.59 | 34.07 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 6.0d ago |
| 12 | 38 | ChronoLLM | 66.1 | 0.85 | 101 | 1,383 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.9d ago |
| 13 | 124 | Swarm | 65.8 | 0.85 | 223 | 715 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.9d ago |
| 14 | 2 | DSperse | 62.8 | 0.85 | 85.15 | 135 | rtx4090 | 0.823 | 5 | 82% | RELEASE 6.7d ago |
| 15 | 55 | NIOME | 61.6 | 0.85 | 60.06 | 486 | rtx4090 | 0.021 | 11 | 29% | SCORING_COMMIT 2.7d ago |
| 16 | 28 | gm | 60.3 | 0.85 | 41.70 | 2,572 | rtx4090 | 0.170 | 41 | 26% | RELEASE 5.0d ago |
| 17 | 60 | Bitsec.ai | 58.9 | 0.85 | 367 | 367 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 10d ago |
| 18 | 74 | Gittensor | 58.1 | 0.85 | 23.15 | 207 | rtx4090 | 0.630 | 14 | 63% | RELEASE 5.8d ago |
| 19 | 61 | RedTeam | 57.0 | 0.85 | 14.55 | 402 | rtx4090 | 0.000 | 83 | 10% | RELEASE 6.2d ago |
| 20 | 51 | lium.io | 56.4 | 0.85 | 18.96 | 2,529 | rtx4090 | 0.000 | 55 | 79% | RELEASE 0.2d ago |
| 21 | 68 | NOVA | 55.1 | 0.6 | 8,002 | 8,002 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 1.0d ago |
| 22 | 120 | Affine | 54.6 | 0.6 | 6,560 | 6,560 | rtx4090 | 0.200 | 5 | 20% | SCORING_COMMIT 5.0d ago |
| 23 | 93 | Bitcast | 54.2 | 0.85 | 234 | 622 | rtx4090 | 0.000 | 4 | 82% | SCORING_COMMIT 19d ago |
| 24 | 80 | OpenRoboto | 53.2 | 0.85 | 171 | 552 | rtx4090 | 0.913 | 4 | 91% | SCORING_COMMIT 9d ago |
| 25 | 97 | Albedo | 52.6 | 0.6 | 2,817 | 2,817 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 224.22637656036437 |
| 54 | Yanez | -4.81 | a4000 | 947.645436511064 |
| 75 | Hippius | -6.78 | rtx4090 | 10978.482466312365 |
| 56 | Gradients | -7.33 | rtx4090 | 959.4418834032566 |
| 114 | SOMA | -8.13 | rtx4090 | 3955.244761985924 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 147.7542820012361 |
| 13 | Data Universe | -3.79 | rtx4090 | 5.8010362049364845 |
| 88 | Investing | -4.96 | rtx4090 | 935.6389424602345 |
| 8 | Vanta | -7.96 | rtx4090 | 2838.9191111141654 |
| 43 | Graphite | -0.78 | cpu-small | 17.130013579963066 |
| 45 | AlphaRidge.ai | -3.94 | rtx4090 | 26.128521616696453 |
| 18 | Zeus | -4.08 | rtx4090 | 1078.5152296246422 |
| 22 | Desearch | -5.65 | rtx4090 | 78.4423163403775 |
| 123 | MANTIS | -6.18 | rtx4090 | 73.68256043066675 |
| 63 | Enigma | -8.14 | rtx4090 | 4982.323089871985 |
| 105 | Beam | -3.32 | rtx4090 | 72.17009057119834 |
| 84 | ansuz | -8.16 | rtx4090 | 0.060282651303340005 |
| 34 | BitMind | -20.34 | a100-80 | 25.824372083036096 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 18.39 | 35.0 | 15.0 | 10.0 | 1.0 |
| 107 | 18.85 | 35.0 | 15.0 | 9.45 | 1.0 |
| 67 | 12.12 | 35.0 | 15.0 | 9.84 | 1.0 |
| 26 | 15.13 | 35.0 | 11.25 | 9.86 | 1.0 |
| 91 | 25.08 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 12.91 | 35.0 | 11.25 | 9.74 | 1.0 |
| 41 | 9.38 | 35.0 | 15.0 | 9.33 | 1.0 |
| 62 | 24.28 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.76 | 35.0 | 15.0 | 8.18 | 1.0 |
| 85 | 23.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.5 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.28 | 35.0 | 15.0 | 9.52 | 0.85 |
| 124 | 21.37 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 17.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.83 | 35.0 | 11.25 | 9.84 | 0.85 |
| 60 | 23.34 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.58 | 35.0 | 11.25 | 9.58 | 0.85 |
| 61 | 10.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 11.83 | 35.0 | 11.25 | 8.28 | 0.85 |
| 68 | 35.5 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.72 | 35.0 | 11.25 | 9.98 | 0.6 |
| 93 | 21.57 | 21.0 | 11.25 | 10.0 | 0.85 |
| 80 | 20.34 | 21.0 | 11.25 | 10.0 | 0.85 |
| 97 | 31.38 | 35.0 | 11.25 | 9.98 | 0.6 |
