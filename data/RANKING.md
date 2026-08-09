# RANKING - generated 2026-08-09T11:40:03Z, block 8806579

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
| 1 | 107 | Minos | 78.7 | 1.0 | 128 | 35,175 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.3d ago |
| 2 | 76 | Phylax | 75.0 | 1.0 | 43.24 | 206 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.6d ago |
| 3 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,243 | 1,243 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.7d ago |
| 4 | 67 | Harnyx | 70.7 | 1.0 | 15.06 | 861 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.0d ago |
| 5 | 91 | cascade | 70.2 | 0.85 | 791 | 2,709 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.3d ago |
| 6 | 1 | Apex | 70.2 | 0.85 | 777 | 1,602 | rtx4090 | 0.462 | 4 | 46% | RELEASE 1.6d ago |
| 7 | 41 | Almanac | 69.4 | 1.0 | 11.55 | 34.72 | cpu-small | 0.717 | 67 | 72% | SCORING_COMMIT 2.5d ago |
| 8 | 96 | Verathos | 69.0 | 1.0 | 26.28 | 285 | rtx4090 | 0.408 | 71 | 41% | RELEASE 0.0d ago |
| 9 | 26 | Perturb | 68.4 | 1.0 | 22.44 | 42.24 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 2.9d ago |
| 10 | 62 | Ridges | 68.3 | 0.85 | 441 | 2,043 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.6d ago |
| 11 | 100 | BASE | 68.1 | 0.85 | 419 | 1,702 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 0.6d ago |
| 12 | 11 | TrajectoryRL | 67.5 | 0.85 | 4,784 | 4,784 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 7d ago |
| 13 | 15 | ORO | 67.1 | 1.0 | 8.89 | 19.13 | cpu-small | 0.000 | 71 | 94% | RELEASE 3.1d ago |
| 14 | 38 | ChronoLLM | 65.6 | 0.85 | 214 | 3,599 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.1d ago |
| 15 | 21 | AdTAO | 65.6 | 1.0 | 4.89 | 22.50 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.9d ago |
| 16 | 80 | OpenRoboto | 64.9 | 0.85 | 162 | 588 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 1.3d ago |
| 17 | 28 | gm | 64.9 | 0.85 | 161 | 4,126 | rtx4090 | 0.227 | 24 | 42% | RELEASE 1.6d ago |
| 18 | 61 | RedTeam | 63.2 | 0.85 | 96.67 | 273 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.0d ago |
| 19 | 51 | lium.io | 59.1 | 0.85 | 35.71 | 3,008 | rtx4090 | 0.000 | 48 | 65% | SCORING_COMMIT 1.6d ago |
| 20 | 6 | Numinous | 59.1 | 1.0 | 29.65 | 340 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 477 | 1,005 | rtx4090 | 0.705 | 7 | 71% | SCORING_COMMIT 12d ago |
| 22 | 85 | Vidaio | 56.3 | 0.85 | 436 | 589 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 12d ago |
| 23 | 102 | ConnitoAI | 56.0 | 0.85 | 390 | 1,751 | rtx4090 | 0.250 | 7 | 37% | RELEASE 9d ago |
| 24 | 2 | DSperse | 55.6 | 0.85 | 9.22 | 124 | rtx4090 | 0.826 | 12 | 83% | RELEASE 3.3d ago |
| 25 | 120 | Affine | 54.8 | 0.6 | 7,279 | 7,279 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.76 | a4000 | 1025.6737231182485 |
| 104 | Masx.ai | -1.49 | rtx4090 | 7.818964134736525 |
| 13 | Data Universe | -2.82 | rtx4090 | 6.998545517284605 |
| 88 | Investing | -5.72 | rtx4090 | 494.43428275956967 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 128.01139855242536 |
| 8 | Vanta | -7.39 | rtx4090 | 3388.7739145542932 |
| 32 | ItsAI | -0.01 | rtx4090 | 10.245669455372228 |
| 22 | Desearch | -0.93 | rtx4090 | 96.4312930604995 |
| 19 | blockmachine | -1.42 | rtx4090 | 259.50228450404234 |
| 18 | Zeus | -4.32 | rtx4090 | 1332.0275348397822 |
| 45 | AlphaRidge.ai | -4.36 | rtx4090 | 19.041183096784465 |
| 75 | Hippius | -4.41 | rtx4090 | 5.668223971119538 |
| 123 | MANTIS | -6.21 | rtx4090 | 73.85631893739472 |
| 63 | Enigma | -8.14 | rtx4090 | 5001.719039758321 |
| 105 | Beam | -4.51 | rtx4090 | 174.2573851950304 |
| 84 | ansuz | -8.15 | rtx4090 | 500.49372622226974 |
| 34 | BitMind | -18.44 | a100-80 | 298.6823897324449 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 19.18 | 35.0 | 15.0 | 9.47 | 1.0 |
| 76 | 14.97 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.15 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 10.97 | 35.0 | 15.0 | 9.69 | 1.0 |
| 91 | 26.37 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.99 | 35.0 | 15.0 | 9.41 | 1.0 |
| 96 | 13.06 | 35.0 | 11.25 | 9.74 | 1.0 |
| 26 | 12.46 | 35.0 | 11.25 | 9.7 | 1.0 |
| 62 | 24.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 23.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.47 | 21.0 | 15.0 | 10.0 | 0.85 |
| 15 | 9.05 | 35.0 | 15.0 | 8.05 | 1.0 |
| 38 | 21.22 | 35.0 | 11.25 | 9.76 | 0.85 |
| 21 | 7.0 | 35.0 | 15.0 | 8.6 | 1.0 |
| 80 | 20.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 20.09 | 35.0 | 11.25 | 9.96 | 0.85 |
| 61 | 18.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.23 | 35.0 | 11.25 | 9.04 | 0.85 |
| 6 | 13.52 | 21.0 | 15.0 | 9.54 | 1.0 |
| 56 | 24.37 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.02 | 21.0 | 11.25 | 10.0 | 0.85 |
| 102 | 23.58 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.13 | 35.0 | 11.25 | 9.99 | 0.6 |
