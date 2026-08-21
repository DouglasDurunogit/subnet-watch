# RANKING - generated 2026-08-21T22:36:57Z, block 8896254

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
| 1 | 76 | Phylax | 77.3 | 1.0 | 81.64 | 137 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 2.5d ago |
| 2 | 102 | ConnitoAI | 72.6 | 0.85 | 1,624 | 1,624 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.3d ago |
| 3 | 23 | Trishool | 72.4 | 0.85 | 590 | 590 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 1.8d ago |
| 4 | 62 | Ridges | 71.3 | 0.85 | 1,094 | 2,061 | rtx4090 | 0.000 | 5 | 36% | RELEASE 3.0d ago |
| 5 | 15 | ORO | 70.7 | 1.0 | 22.29 | 21,747 | cpu-small | 0.000 | 77 | 93% | SCORING_COMMIT 3.1d ago |
| 6 | 67 | Harnyx | 70.3 | 1.0 | 13.72 | 944 | cpu-small | 0.004 | 162 | 23% | SCORING_COMMIT 0.5d ago |
| 7 | 1 | Apex | 70.2 | 0.85 | 794 | 1,256 | rtx4090 | 0.522 | 4 | 52% | RELEASE 0.3d ago |
| 8 | 91 | cascade | 70.0 | 0.85 | 739 | 2,982 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.0d ago |
| 9 | 56 | Gradients | 69.9 | 0.85 | 729 | 1,123 | rtx4090 | 0.726 | 5 | 73% | SCORING_COMMIT 3.9d ago |
| 10 | 26 | Perturb | 68.1 | 1.0 | 21.07 | 401 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.9d ago |
| 11 | 38 | ChronoLLM | 67.9 | 0.85 | 164 | 3,486 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.1d ago |
| 12 | 96 | Verathos | 66.4 | 1.0 | 14.18 | 658 | rtx4090 | 0.402 | 93 | 40% | RELEASE 3.3d ago |
| 13 | 107 | Minos | 65.6 | 1.0 | 164 | 45,613 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 11d ago |
| 14 | 85 | Vidaio | 65.0 | 0.85 | 167 | 431 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 3.6d ago |
| 15 | 121 | sundae_bar | 63.0 | 0.85 | 1,244 | 1,244 | cpu-small | 0.601 | 2 | 60% | README_TASK_DIFF 7d ago |
| 16 | 81 | Reliquary | 62.1 | 0.85 | 69.40 | 214 | rtx4090 | 0.002 | 52 | 5% | SCORING_COMMIT 0.4d ago |
| 17 | 108 | Prometheon | 61.5 | 0.85 | 59.01 | 407 | rtx4090 | 0.660 | 8 | 66% | SCORING_COMMIT 0.4d ago |
| 18 | 34 | BitMind | 61.2 | 0.85 | 369 | 369 | a100-80 | 0.000 | 3 | 48% | RELEASE 0.9d ago |
| 19 | 51 | lium.io | 60.2 | 0.85 | 48.41 | 2,019 | rtx4090 | 0.000 | 51 | 75% | SCORING_COMMIT 1.6d ago |
| 20 | 53 | engy | 60.2 | 0.85 | 38.94 | 256 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.7d ago |
| 21 | 60 | Bitsec.ai | 59.7 | 0.85 | 465 | 465 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 14d ago |
| 22 | 28 | gm | 58.8 | 0.85 | 26.97 | 1,882 | rtx4090 | 0.199 | 54 | 20% | RELEASE 1.4d ago |
| 23 | 68 | NOVA | 55.4 | 0.6 | 9,129 | 9,129 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 5.4d ago |
| 24 | 120 | Affine | 55.0 | 0.6 | 7,714 | 7,714 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.1d ago |
| 25 | 124 | Swarm | 54.7 | 0.85 | 282 | 2,452 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 10d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.32 | cpu-small | 5.515937244395685 |
| 54 | Yanez | -3.10 | a4000 | 1207.2227424205232 |
| 89 | InfiniteQuant | -1.38 | rtx4090 | 121.5732132576594 |
| 13 | Data Universe | -2.81 | rtx4090 | 6.308783608175179 |
| 18 | Zeus | -3.56 | rtx4090 | 2118.7767598137857 |
| 123 | MANTIS | -5.49 | rtx4090 | 106.64071116039493 |
| 75 | Hippius | -6.20 | rtx4090 | 11857.128966515376 |
| 6 | Numinous | -0.93 | cpu-small | 390.7091972022309 |
| 104 | Masx.ai | -1.47 | rtx4090 | 10.308671774825575 |
| 88 | Investing | -4.33 | rtx4090 | 931.1229476659527 |
| 8 | Vanta | -7.34 | rtx4090 | 3285.6058422351816 |
| 43 | Graphite | -0.77 | cpu-small | 27.963206034723378 |
| 19 | blockmachine | -1.13 | rtx4090 | 563.1877365463213 |
| 45 | AlphaRidge.ai | -5.02 | rtx4090 | 9.289979456795898 |
| 22 | Desearch | -5.84 | rtx4090 | 151.68592762847672 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08539768046852168 |
| 105 | Beam | -2.00 | rtx4090 | 81.28110586775401 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07071576663806434 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.44 | 35.0 | 15.0 | 9.91 | 1.0 |
| 102 | 29.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.21 | 35.0 | 15.0 | 9.99 | 0.85 |
| 62 | 27.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 12.44 | 35.0 | 15.0 | 8.27 | 1.0 |
| 67 | 10.62 | 35.0 | 15.0 | 9.7 | 1.0 |
| 1 | 26.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.1 | 35.0 | 11.25 | 9.99 | 0.85 |
| 56 | 26.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.22 | 35.0 | 11.25 | 9.63 | 1.0 |
| 38 | 20.18 | 35.0 | 15.0 | 9.65 | 0.85 |
| 96 | 10.74 | 35.0 | 11.25 | 9.45 | 1.0 |
| 107 | 20.17 | 21.0 | 15.0 | 9.45 | 1.0 |
| 85 | 20.25 | 35.0 | 11.25 | 10.0 | 0.85 |
| 121 | 28.15 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 16.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 16.17 | 35.0 | 11.25 | 9.93 | 0.85 |
| 34 | 23.36 | 35.0 | 3.75 | 9.9 | 0.85 |
| 51 | 15.41 | 35.0 | 11.25 | 9.2 | 0.85 |
| 53 | 14.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.27 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.16 | 35.0 | 11.25 | 9.71 | 0.85 |
| 68 | 36.02 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.36 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.29 | 21.0 | 11.25 | 9.86 | 0.85 |
