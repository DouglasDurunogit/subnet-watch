# RANKING - generated 2026-08-21T22:02:07Z, block 8896079

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
| 1 | 76 | Phylax | 77.3 | 1.0 | 81.28 | 136 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 2.5d ago |
| 2 | 102 | ConnitoAI | 72.6 | 0.85 | 1,617 | 1,617 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.2d ago |
| 3 | 23 | Trishool | 72.4 | 0.85 | 587 | 587 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 1.8d ago |
| 4 | 62 | Ridges | 71.3 | 0.85 | 1,090 | 2,053 | rtx4090 | 0.000 | 5 | 36% | RELEASE 3.0d ago |
| 5 | 15 | ORO | 70.7 | 1.0 | 22.97 | 22,374 | cpu-small | 0.000 | 77 | 93% | SCORING_COMMIT 3.1d ago |
| 6 | 67 | Harnyx | 70.3 | 1.0 | 13.66 | 939 | cpu-small | 0.004 | 162 | 23% | SCORING_COMMIT 0.5d ago |
| 7 | 1 | Apex | 70.2 | 0.85 | 790 | 1,253 | rtx4090 | 0.522 | 4 | 52% | RELEASE 0.3d ago |
| 8 | 56 | Gradients | 69.9 | 0.85 | 726 | 1,119 | rtx4090 | 0.726 | 5 | 73% | SCORING_COMMIT 3.9d ago |
| 9 | 91 | cascade | 69.9 | 0.85 | 711 | 2,868 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.0d ago |
| 10 | 26 | Perturb | 68.1 | 1.0 | 20.96 | 399 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.8d ago |
| 11 | 38 | ChronoLLM | 67.8 | 0.85 | 164 | 3,470 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.0d ago |
| 12 | 96 | Verathos | 66.4 | 1.0 | 13.88 | 649 | rtx4090 | 0.402 | 93 | 40% | RELEASE 3.2d ago |
| 13 | 107 | Minos | 65.7 | 1.0 | 164 | 45,422 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 11d ago |
| 14 | 85 | Vidaio | 65.0 | 0.85 | 167 | 430 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 3.6d ago |
| 15 | 121 | sundae_bar | 63.0 | 0.85 | 1,239 | 1,239 | cpu-small | 0.601 | 2 | 60% | README_TASK_DIFF 7d ago |
| 16 | 81 | Reliquary | 62.1 | 0.85 | 69.08 | 213 | rtx4090 | 0.002 | 52 | 5% | SCORING_COMMIT 0.4d ago |
| 17 | 108 | Prometheon | 61.5 | 0.85 | 58.71 | 405 | rtx4090 | 0.660 | 8 | 66% | SCORING_COMMIT 0.3d ago |
| 18 | 34 | BitMind | 61.2 | 0.85 | 368 | 368 | a100-80 | 0.000 | 3 | 48% | RELEASE 0.8d ago |
| 19 | 51 | lium.io | 60.2 | 0.85 | 47.98 | 2,003 | rtx4090 | 0.000 | 51 | 75% | SCORING_COMMIT 1.6d ago |
| 20 | 53 | engy | 60.2 | 0.85 | 38.88 | 256 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.7d ago |
| 21 | 60 | Bitsec.ai | 59.7 | 0.85 | 463 | 463 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 14d ago |
| 22 | 28 | gm | 58.7 | 0.85 | 26.80 | 1,873 | rtx4090 | 0.199 | 54 | 20% | RELEASE 1.3d ago |
| 23 | 68 | NOVA | 55.4 | 0.6 | 9,099 | 9,099 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 5.3d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,683 | 7,683 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.1d ago |
| 25 | 124 | Swarm | 54.7 | 0.85 | 282 | 2,453 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 10d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.33 | cpu-small | 5.493511354073497 |
| 54 | Yanez | -3.10 | a4000 | 1206.9558777239956 |
| 89 | InfiniteQuant | -1.41 | rtx4090 | 121.0452818918507 |
| 13 | Data Universe | -2.83 | rtx4090 | 6.285861215704629 |
| 18 | Zeus | -3.58 | rtx4090 | 2109.575875285753 |
| 123 | MANTIS | -5.50 | rtx4090 | 106.12244710330069 |
| 75 | Hippius | -6.21 | rtx4090 | 11834.487053475614 |
| 6 | Numinous | -0.93 | cpu-small | 388.90552457805484 |
| 104 | Masx.ai | -1.50 | rtx4090 | 10.260499534940896 |
| 88 | Investing | -4.35 | rtx4090 | 926.5883063275968 |
| 8 | Vanta | -7.35 | rtx4090 | 3276.2488712121713 |
| 43 | Graphite | -0.77 | cpu-small | 27.84177338557808 |
| 19 | blockmachine | -1.16 | rtx4090 | 560.7474313720397 |
| 45 | AlphaRidge.ai | -5.04 | rtx4090 | 9.219949404711008 |
| 22 | Desearch | -5.85 | rtx4090 | 151.02718924044405 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08511958695328484 |
| 105 | Beam | -2.03 | rtx4090 | 80.97770404216095 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07040866372580375 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.42 | 35.0 | 15.0 | 9.91 | 1.0 |
| 102 | 29.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.19 | 35.0 | 15.0 | 9.99 | 0.85 |
| 62 | 27.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 12.55 | 35.0 | 15.0 | 8.14 | 1.0 |
| 67 | 10.61 | 35.0 | 15.0 | 9.66 | 1.0 |
| 1 | 26.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 26.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.94 | 35.0 | 11.25 | 9.99 | 0.85 |
| 26 | 12.2 | 35.0 | 11.25 | 9.63 | 1.0 |
| 38 | 20.16 | 35.0 | 15.0 | 9.65 | 0.85 |
| 96 | 10.67 | 35.0 | 11.25 | 9.44 | 1.0 |
| 107 | 20.16 | 21.0 | 15.0 | 9.53 | 1.0 |
| 85 | 20.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 121 | 28.14 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 16.79 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 16.15 | 35.0 | 11.25 | 9.93 | 0.85 |
| 34 | 23.35 | 35.0 | 3.75 | 9.9 | 0.85 |
| 51 | 15.37 | 35.0 | 11.25 | 9.2 | 0.85 |
| 53 | 14.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.25 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.13 | 35.0 | 11.25 | 9.71 | 0.85 |
| 68 | 36.01 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.34 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.29 | 21.0 | 11.25 | 9.86 | 0.85 |
