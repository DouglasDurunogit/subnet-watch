# RANKING - generated 2026-08-13T20:25:16Z, block 8837997

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
| 1 | 107 | Minos | 78.2 | 1.0 | 114 | 31,744 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 3.2d ago |
| 2 | 76 | Phylax | 74.6 | 1.0 | 39.18 | 188 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 4.9d ago |
| 3 | 67 | Harnyx | 71.3 | 1.0 | 17.31 | 711 | cpu-small | 0.019 | 148 | 19% | SCORING_COMMIT 0.4d ago |
| 4 | 1 | Apex | 70.5 | 0.85 | 852 | 1,172 | rtx4090 | 0.544 | 4 | 54% | RELEASE 0.3d ago |
| 5 | 91 | cascade | 69.8 | 0.85 | 710 | 2,446 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 2.7d ago |
| 6 | 26 | Perturb | 69.3 | 1.0 | 27.69 | 825 | rtx3060 | 0.506 | 11 | 51% | SCORING_COMMIT 0.2d ago |
| 7 | 62 | Ridges | 69.0 | 0.85 | 550 | 1,988 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 1.9d ago |
| 8 | 41 | Almanac | 69.0 | 1.0 | 10.40 | 28.82 | cpu-small | 0.725 | 68 | 73% | SCORING_COMMIT 0.9d ago |
| 9 | 56 | Gradients | 68.9 | 0.85 | 532 | 986 | rtx4090 | 0.654 | 7 | 65% | SCORING_COMMIT 1.3d ago |
| 10 | 96 | Verathos | 68.6 | 1.0 | 23.60 | 284 | rtx4090 | 0.410 | 58 | 41% | RELEASE 1.3d ago |
| 11 | 38 | ChronoLLM | 67.9 | 0.85 | 166 | 3,472 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.2d ago |
| 12 | 6 | Numinous | 67.9 | 1.0 | 9.59 | 508 | cpu-small | 0.000 | 19 | 29% | WEIGHTS_VERSION_BUMP 0.2d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.67 | 34.35 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 2.3d ago |
| 14 | 124 | Swarm | 66.0 | 0.85 | 230 | 740 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 2.2d ago |
| 15 | 80 | OpenRoboto | 65.2 | 0.85 | 176 | 636 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 5.6d ago |
| 16 | 85 | Vidaio | 64.4 | 0.85 | 139 | 599 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 1.4d ago |
| 17 | 102 | ConnitoAI | 60.5 | 0.85 | 1,528 | 1,534 | rtx4090 | 0.251 | 4 | 25% | RELEASE 13d ago |
| 18 | 51 | lium.io | 60.3 | 0.85 | 48.72 | 1,986 | rtx4090 | 0.000 | 48 | 72% | RELEASE 0.2d ago |
| 19 | 74 | Gittensor | 58.3 | 0.85 | 24.04 | 217 | rtx4090 | 0.630 | 14 | 63% | RELEASE 2.1d ago |
| 20 | 28 | gm | 58.3 | 0.85 | 23.38 | 1,840 | rtx4090 | 0.252 | 32 | 25% | RELEASE 1.3d ago |
| 21 | 61 | RedTeam | 57.7 | 0.85 | 18.28 | 1,616 | rtx4090 | 0.000 | 66 | 35% | RELEASE 2.5d ago |
| 22 | 2 | DSperse | 55.9 | 0.85 | 9.99 | 82.31 | rtx4090 | 0.828 | 13 | 83% | RELEASE 3.0d ago |
| 23 | 15 | ORO | 54.9 | 1.0 | 12.79 | 23.06 | cpu-small | 0.000 | 79 | 93% | RELEASE 7d ago |
| 24 | 120 | Affine | 54.7 | 0.6 | 7,001 | 7,001 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.3d ago |
| 25 | 97 | Albedo | 52.7 | 0.6 | 2,983 | 2,983 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.89 | a4000 | 958.8341867619695 |
| 75 | Hippius | -7.32 | rtx4090 | 11659.264686884311 |
| 114 | SOMA | -8.11 | rtx4090 | 701.4827572163089 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 169.68620402505832 |
| 13 | Data Universe | -3.15 | rtx4090 | 5.806096164309435 |
| 88 | Investing | -5.25 | rtx4090 | 657.5791113393357 |
| 8 | Vanta | -7.95 | rtx4090 | 3422.4332571688888 |
| 43 | Graphite | -0.60 | cpu-small | 41.17049213968911 |
| 19 | blockmachine | -1.72 | rtx4090 | 345.18309356400107 |
| 18 | Zeus | -3.92 | rtx4090 | 1818.1041348815163 |
| 45 | AlphaRidge.ai | -4.83 | rtx4090 | 12.248363847221595 |
| 123 | MANTIS | -5.99 | rtx4090 | 84.27610107025947 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07693621773184531 |
| 105 | Beam | -2.21 | rtx4090 | 84.26516649495328 |
| 84 | ansuz | -8.15 | rtx4090 | 468.6033818821777 |
| 34 | BitMind | -19.65 | a100-80 | 294.496170686501 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.75 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 14.59 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 11.48 | 35.0 | 15.0 | 9.77 | 1.0 |
| 1 | 26.66 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.94 | 35.0 | 11.25 | 9.99 | 0.85 |
| 26 | 13.26 | 35.0 | 11.25 | 9.76 | 1.0 |
| 62 | 24.93 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.61 | 35.0 | 15.0 | 9.35 | 1.0 |
| 56 | 24.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.65 | 35.0 | 11.25 | 9.71 | 1.0 |
| 38 | 20.21 | 35.0 | 15.0 | 9.7 | 0.85 |
| 6 | 9.32 | 35.0 | 15.0 | 8.59 | 1.0 |
| 21 | 8.53 | 35.0 | 15.0 | 9.12 | 1.0 |
| 124 | 21.49 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 20.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.53 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 28.96 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 15.43 | 35.0 | 11.25 | 9.31 | 0.85 |
| 74 | 12.72 | 35.0 | 11.25 | 9.58 | 0.85 |
| 28 | 12.62 | 35.0 | 11.25 | 9.71 | 0.85 |
| 61 | 11.69 | 35.0 | 11.25 | 9.97 | 0.85 |
| 2 | 9.47 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 10.36 | 21.0 | 15.0 | 8.58 | 1.0 |
| 120 | 34.97 | 35.0 | 11.25 | 9.99 | 0.6 |
| 97 | 31.6 | 35.0 | 11.25 | 9.97 | 0.6 |
