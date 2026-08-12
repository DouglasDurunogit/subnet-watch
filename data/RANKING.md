# RANKING - generated 2026-08-12T21:58:09Z, block 8831262

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
| 1 | 107 | Minos | 77.6 | 1.0 | 101 | 31,271 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 2.3d ago |
| 2 | 76 | Phylax | 76.3 | 1.0 | 61.22 | 186 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 4.0d ago |
| 3 | 67 | Harnyx | 71.4 | 1.0 | 17.89 | 745 | cpu-small | 0.038 | 131 | 20% | SCORING_COMMIT 0.4d ago |
| 4 | 96 | Verathos | 70.7 | 1.0 | 39.05 | 394 | rtx4090 | 0.418 | 51 | 42% | RELEASE 0.3d ago |
| 5 | 91 | cascade | 70.1 | 0.85 | 760 | 2,621 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.7d ago |
| 6 | 114 | SOMA | 69.7 | 0.85 | 670 | 4,398 | rtx4090 | 0.000 | 4 | 65% | SCORING_COMMIT 5.5d ago |
| 7 | 41 | Almanac | 69.1 | 1.0 | 10.59 | 29.69 | cpu-small | 0.715 | 68 | 72% | SCORING_COMMIT 5.9d ago |
| 8 | 62 | Ridges | 69.0 | 0.85 | 544 | 1,969 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 1.0d ago |
| 9 | 56 | Gradients | 68.9 | 0.85 | 531 | 975 | rtx4090 | 0.647 | 7 | 65% | SCORING_COMMIT 0.3d ago |
| 10 | 100 | BASE | 68.3 | 0.85 | 451 | 1,828 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.5d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.26 | 36.56 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 6.3d ago |
| 12 | 21 | AdTAO | 67.5 | 1.0 | 7.47 | 33.56 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 1.4d ago |
| 13 | 11 | TrajectoryRL | 67.1 | 0.85 | 4,175 | 4,175 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 10d ago |
| 14 | 15 | ORO | 67.0 | 1.0 | 8.97 | 12,187 | cpu-small | 0.000 | 69 | 94% | RELEASE 6.5d ago |
| 15 | 124 | Swarm | 65.8 | 0.85 | 219 | 667 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 1.3d ago |
| 16 | 80 | OpenRoboto | 65.0 | 0.85 | 164 | 596 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 4.7d ago |
| 17 | 38 | ChronoLLM | 64.6 | 0.85 | 160 | 3,493 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 4.5d ago |
| 18 | 85 | Vidaio | 64.2 | 0.85 | 129 | 441 | rtx4090 | 0.000 | 10 | 20% | SCORING_COMMIT 0.5d ago |
| 19 | 28 | gm | 62.8 | 0.85 | 88.61 | 2,668 | rtx4090 | 0.079 | 30 | 27% | RELEASE 0.3d ago |
| 20 | 51 | lium.io | 60.4 | 0.85 | 49.83 | 2,256 | rtx4090 | 0.000 | 46 | 71% | RELEASE 0.4d ago |
| 21 | 74 | Gittensor | 58.4 | 0.85 | 25.24 | 214 | rtx4090 | 0.630 | 13 | 63% | RELEASE 1.1d ago |
| 22 | 61 | RedTeam | 58.3 | 0.85 | 21.58 | 1,622 | rtx4090 | 0.000 | 59 | 35% | RELEASE 1.6d ago |
| 23 | 6 | Numinous | 56.3 | 1.0 | 15.75 | 475 | cpu-small | 0.000 | 20 | 26% | README_TASK_DIFF 14d ago |
| 24 | 2 | DSperse | 55.5 | 0.85 | 9.01 | 99.77 | rtx4090 | 0.827 | 14 | 83% | RELEASE 2.1d ago |
| 25 | 120 | Affine | 54.7 | 0.6 | 6,898 | 6,898 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.75 | a4000 | 996.6803522733173 |
| 104 | Masx.ai | -0.69 | rtx4090 | 10.21163643774032 |
| 75 | Hippius | -7.70 | rtx4090 | 11179.059627963692 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 139.8270687919095 |
| 13 | Data Universe | -3.19 | rtx4090 | 5.674068996955694 |
| 88 | Investing | -5.01 | rtx4090 | 641.4201386743547 |
| 8 | Vanta | -7.95 | rtx4090 | 3256.863942703884 |
| 32 | ItsAI | -0.17 | rtx4090 | 11.0800495302035 |
| 19 | blockmachine | -2.24 | rtx4090 | 549.4305289465187 |
| 18 | Zeus | -3.31 | rtx4090 | 1738.1470796044916 |
| 123 | MANTIS | -6.09 | rtx4090 | 81.06036509719891 |
| 45 | AlphaRidge.ai | -6.24 | rtx4090 | 7.289937152496639 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07489546812741894 |
| 105 | Beam | -2.17 | rtx4090 | 81.84889868809735 |
| 84 | ansuz | -8.15 | rtx4090 | 474.632509739711 |
| 34 | BitMind | -19.82 | a100-80 | 289.57063348873675 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn108, sn109, sn111, sn113, sn115, sn116, sn118, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.26 | 35.0 | 15.0 | 9.35 | 1.0 |
| 76 | 16.32 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 11.61 | 35.0 | 15.0 | 9.82 | 1.0 |
| 96 | 14.58 | 35.0 | 11.25 | 9.83 | 1.0 |
| 91 | 26.21 | 35.0 | 11.25 | 9.99 | 0.85 |
| 114 | 25.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.68 | 35.0 | 15.0 | 9.37 | 1.0 |
| 62 | 24.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.79 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 24.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 11.88 | 35.0 | 11.25 | 9.66 | 1.0 |
| 21 | 8.44 | 35.0 | 15.0 | 9.11 | 1.0 |
| 11 | 32.93 | 21.0 | 15.0 | 10.0 | 0.85 |
| 15 | 9.08 | 35.0 | 15.0 | 7.95 | 1.0 |
| 124 | 21.3 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 20.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 20.07 | 35.0 | 11.25 | 9.69 | 0.85 |
| 85 | 19.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 17.76 | 35.0 | 11.25 | 9.93 | 0.85 |
| 51 | 15.52 | 35.0 | 11.25 | 9.33 | 0.85 |
| 74 | 12.91 | 35.0 | 11.25 | 9.61 | 0.85 |
| 61 | 12.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.13 | 21.0 | 15.0 | 9.16 | 1.0 |
| 2 | 9.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.91 | 35.0 | 11.25 | 9.99 | 0.6 |
