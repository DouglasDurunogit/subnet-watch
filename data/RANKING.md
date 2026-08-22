# RANKING - generated 2026-08-22T19:45:06Z, block 8902594

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 76.24 | 135 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.4d ago |
| 2 | 102 | ConnitoAI | 72.9 | 0.85 | 1,776 | 1,777 | rtx4090 | 0.250 | 4 | 25% | RELEASE 1.1d ago |
| 3 | 67 | Harnyx | 72.4 | 1.0 | 23.24 | 120 | cpu-small | 0.052 | 151 | 12% | SCORING_COMMIT 1.4d ago |
| 4 | 62 | Ridges | 71.7 | 0.85 | 1,229 | 3,026 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.9d ago |
| 5 | 15 | ORO | 70.6 | 1.0 | 19.40 | 23,098 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.8d ago |
| 6 | 56 | Gradients | 70.0 | 0.85 | 739 | 1,088 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.8d ago |
| 7 | 91 | cascade | 69.8 | 0.85 | 705 | 2,845 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.9d ago |
| 8 | 1 | Apex | 68.7 | 0.85 | 502 | 1,283 | rtx4090 | 0.517 | 5 | 52% | RELEASE 1.2d ago |
| 9 | 96 | Verathos | 67.6 | 1.0 | 18.42 | 440 | rtx4090 | 0.402 | 90 | 40% | RELEASE 4.1d ago |
| 10 | 26 | Perturb | 67.5 | 1.0 | 18.20 | 260 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.7d ago |
| 11 | 38 | ChronoLLM | 66.6 | 0.85 | 116 | 1,588 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.9d ago |
| 12 | 107 | Minos | 65.5 | 1.0 | 156 | 43,805 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 13 | 85 | Vidaio | 64.3 | 0.85 | 135 | 408 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.5d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 120 | 130 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.2d ago |
| 15 | 81 | Reliquary | 63.7 | 0.85 | 113 | 226 | rtx4090 | 0.003 | 39 | 5% | SCORING_COMMIT 0.1d ago |
| 16 | 51 | lium.io | 61.5 | 0.85 | 67.14 | 4,470 | rtx4090 | 0.000 | 51 | 69% | SCORING_COMMIT 2.5d ago |
| 17 | 28 | gm | 60.1 | 0.85 | 39.46 | 1,909 | rtx4090 | 0.082 | 53 | 17% | RELEASE 2.2d ago |
| 18 | 60 | Bitsec.ai | 59.8 | 0.85 | 482 | 482 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 19 | 53 | engy | 59.4 | 0.85 | 30.68 | 210 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.6d ago |
| 20 | 61 | RedTeam | 57.8 | 0.85 | 18.39 | 287 | rtx4090 | 0.000 | 87 | 6% | RELEASE 0.5d ago |
| 21 | 68 | NOVA | 55.3 | 0.6 | 8,842 | 8,842 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.3d ago |
| 22 | 41 | Almanac | 55.3 | 1.0 | 11.42 | 24.23 | cpu-small | 0.731 | 78 | 73% | SCORING_COMMIT 10d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,234 | 7,234 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.0d ago |
| 24 | 124 | Swarm | 54.6 | 0.85 | 273 | 2,383 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |
| 25 | 33 | ReadyAI | 53.9 | 0.85 | 6.43 | 10.27 | rtx4090 | 0.000 | 245 | 1% | SCORING_COMMIT 2.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.07 | a4000 | 1225.6934454345092 |
| 13 | Data Universe | -2.61 | rtx4090 | 6.7412624489241075 |
| 89 | InfiniteQuant | -3.03 | rtx4090 | 119.5639228059543 |
| 18 | Zeus | -4.32 | rtx4090 | 1743.1114827699328 |
| 123 | MANTIS | -5.69 | rtx4090 | 104.13319371888873 |
| 75 | Hippius | -6.41 | rtx4090 | 11730.071525633804 |
| 34 | BitMind | -19.29 | a100-80 | 329.27352911522206 |
| 6 | Numinous | -0.94 | cpu-small | 292.51581220085086 |
| 104 | Masx.ai | -1.30 | rtx4090 | 8.573949521655107 |
| 50 | Synth | -1.49 | rtx4090 | 58.564349977871046 |
| 88 | Investing | -3.17 | rtx4090 | 693.0999067630123 |
| 8 | Vanta | -7.37 | rtx4090 | 1099.29300522462 |
| 43 | Graphite | -0.45 | cpu-small | 194.7000714752423 |
| 19 | blockmachine | -0.96 | rtx4090 | 553.7934804600952 |
| 45 | AlphaRidge.ai | -4.46 | rtx4090 | 11.017402663687502 |
| 22 | Desearch | -4.71 | rtx4090 | 80.73886189131373 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08419764512808707 |
| 105 | Beam | -2.21 | rtx4090 | 80.95733857566871 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07083294274454892 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.17 | 35.0 | 15.0 | 9.9 | 1.0 |
| 102 | 29.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.59 | 35.0 | 15.0 | 9.86 | 1.0 |
| 62 | 28.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.91 | 35.0 | 15.0 | 8.72 | 1.0 |
| 56 | 26.09 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.91 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.57 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 11.72 | 35.0 | 11.25 | 9.59 | 1.0 |
| 26 | 11.67 | 35.0 | 11.25 | 9.58 | 1.0 |
| 38 | 18.82 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.97 | 21.0 | 15.0 | 9.52 | 1.0 |
| 85 | 19.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.95 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.67 | 35.0 | 11.25 | 9.44 | 0.85 |
| 28 | 14.62 | 35.0 | 11.25 | 9.81 | 0.85 |
| 60 | 24.41 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.9 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.95 | 21.0 | 15.0 | 9.34 | 1.0 |
| 120 | 35.1 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.18 | 21.0 | 11.25 | 9.86 | 0.85 |
| 33 | 7.92 | 35.0 | 11.25 | 9.2 | 0.85 |
