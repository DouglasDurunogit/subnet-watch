# RANKING - generated 2026-08-23T04:08:35Z, block 8905112

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
| 1 | 76 | Phylax | 76.7 | 1.0 | 68.72 | 76.78 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.8d ago |
| 2 | 67 | Harnyx | 72.3 | 1.0 | 22.16 | 115 | cpu-small | 0.019 | 159 | 12% | SCORING_COMMIT 1.7d ago |
| 3 | 23 | Trishool | 72.1 | 0.85 | 543 | 543 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.0d ago |
| 4 | 62 | Ridges | 71.6 | 0.85 | 1,176 | 2,895 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.2d ago |
| 5 | 102 | ConnitoAI | 71.1 | 0.85 | 1,033 | 2,832 | rtx4090 | 0.250 | 5 | 42% | RELEASE 1.5d ago |
| 6 | 56 | Gradients | 69.8 | 0.85 | 701 | 1,040 | rtx4090 | 0.729 | 5 | 73% | SCORING_COMMIT 5.2d ago |
| 7 | 15 | ORO | 69.8 | 1.0 | 17.61 | 36.91 | cpu-small | 0.000 | 60 | 95% | SCORING_COMMIT 1.2d ago |
| 8 | 91 | cascade | 69.7 | 0.85 | 674 | 2,721 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.2d ago |
| 9 | 1 | Apex | 68.6 | 0.85 | 481 | 1,180 | rtx4090 | 0.526 | 5 | 53% | RELEASE 1.6d ago |
| 10 | 26 | Perturb | 67.3 | 1.0 | 17.26 | 249 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.1d ago |
| 11 | 96 | Verathos | 67.2 | 1.0 | 16.97 | 274 | rtx4090 | 0.402 | 92 | 40% | RELEASE 4.5d ago |
| 12 | 38 | ChronoLLM | 66.4 | 0.85 | 110 | 1,498 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.3d ago |
| 13 | 107 | Minos | 65.0 | 1.0 | 141 | 41,551 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 14 | 98 | NeverPlayAlone | 64.4 | 0.85 | 1,856 | 1,856 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 16d ago |
| 15 | 85 | Vidaio | 64.4 | 0.85 | 139 | 389 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.9d ago |
| 16 | 108 | Prometheon | 63.8 | 0.85 | 116 | 125 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.6d ago |
| 17 | 81 | Reliquary | 63.1 | 0.85 | 94.95 | 233 | rtx4090 | 0.089 | 41 | 9% | SCORING_COMMIT 0.4d ago |
| 18 | 51 | lium.io | 62.2 | 0.85 | 80.27 | 4,239 | rtx4090 | 0.000 | 50 | 71% | SCORING_COMMIT 2.8d ago |
| 19 | 28 | gm | 61.0 | 0.85 | 51.45 | 1,470 | rtx4090 | 0.005 | 54 | 14% | RELEASE 2.6d ago |
| 20 | 60 | Bitsec.ai | 59.7 | 0.85 | 464 | 464 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 21 | 53 | engy | 59.7 | 0.85 | 33.59 | 226 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.0d ago |
| 22 | 61 | RedTeam | 57.2 | 0.85 | 15.30 | 286 | rtx4090 | 0.000 | 87 | 6% | RELEASE 0.8d ago |
| 23 | 41 | Almanac | 56.3 | 1.0 | 14.58 | 27.73 | cpu-small | 0.625 | 79 | 63% | SCORING_COMMIT 10d ago |
| 24 | 68 | NOVA | 55.2 | 0.6 | 8,447 | 8,447 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.6d ago |
| 25 | 120 | Affine | 54.7 | 0.6 | 6,901 | 6,901 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.31 | cpu-small | 5.634579651164237 |
| 54 | Yanez | -3.42 | a4000 | 1182.1489852401194 |
| 13 | Data Universe | -3.36 | rtx4090 | 7.340692233441636 |
| 89 | InfiniteQuant | -3.64 | rtx4090 | 110.59116336205017 |
| 18 | Zeus | -4.56 | rtx4090 | 1395.3093694099387 |
| 123 | MANTIS | -5.76 | rtx4090 | 106.60764965476146 |
| 75 | Hippius | -6.48 | rtx4090 | 11246.672428770089 |
| 34 | BitMind | -18.67 | a100-80 | 314.5431867412764 |
| 6 | Numinous | -0.93 | cpu-small | 170.40979648617565 |
| 104 | Masx.ai | -0.71 | rtx4090 | 8.445225610772987 |
| 50 | Synth | -2.18 | rtx4090 | 59.14927838089417 |
| 88 | Investing | -3.28 | rtx4090 | 620.7103039972027 |
| 8 | Vanta | -7.40 | rtx4090 | 1039.7112986494908 |
| 43 | Graphite | -0.26 | cpu-small | 180.40072366202642 |
| 32 | ItsAI | -0.29 | rtx4090 | 11.150371925726471 |
| 22 | Desearch | -1.05 | rtx4090 | 47.202070883957425 |
| 19 | blockmachine | -1.28 | rtx4090 | 529.8524256735371 |
| 45 | AlphaRidge.ai | -4.46 | rtx4090 | 14.762163878935441 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08047984579755293 |
| 105 | Beam | -2.45 | rtx4090 | 77.59515811593347 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.77 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 12.41 | 35.0 | 15.0 | 9.91 | 1.0 |
| 23 | 24.88 | 35.0 | 15.0 | 9.99 | 0.85 |
| 62 | 27.93 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 25.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.55 | 35.0 | 15.0 | 8.3 | 1.0 |
| 91 | 25.73 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.4 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 11.47 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.41 | 35.0 | 11.25 | 9.57 | 1.0 |
| 38 | 18.59 | 35.0 | 15.0 | 9.51 | 0.85 |
| 107 | 19.56 | 21.0 | 15.0 | 9.42 | 1.0 |
| 98 | 29.73 | 21.0 | 15.0 | 10.0 | 0.85 |
| 85 | 19.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.8 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 17.37 | 35.0 | 11.25 | 9.55 | 0.85 |
| 28 | 15.64 | 35.0 | 11.25 | 9.86 | 0.85 |
| 60 | 24.26 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 14.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.03 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 10.85 | 21.0 | 15.0 | 9.5 | 1.0 |
| 68 | 35.71 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.92 | 35.0 | 11.25 | 9.99 | 0.6 |
