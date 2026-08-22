# RANKING - generated 2026-08-22T15:32:21Z, block 8901331

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
| 1 | 76 | Phylax | 77.2 | 1.0 | 77.96 | 131 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.2d ago |
| 2 | 102 | ConnitoAI | 72.8 | 0.85 | 1,709 | 1,709 | rtx4090 | 0.250 | 4 | 25% | RELEASE 1.0d ago |
| 3 | 67 | Harnyx | 72.3 | 1.0 | 22.54 | 439 | cpu-small | 0.058 | 148 | 12% | SCORING_COMMIT 1.2d ago |
| 4 | 62 | Ridges | 71.6 | 0.85 | 1,192 | 2,935 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.7d ago |
| 5 | 56 | Gradients | 69.9 | 0.85 | 719 | 1,055 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.6d ago |
| 6 | 91 | cascade | 69.7 | 0.85 | 689 | 2,779 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.7d ago |
| 7 | 15 | ORO | 69.6 | 1.0 | 17.60 | 36.53 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.7d ago |
| 8 | 1 | Apex | 68.4 | 0.85 | 465 | 1,095 | rtx4090 | 0.553 | 5 | 55% | RELEASE 1.0d ago |
| 9 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,514 | 4,514 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.55 | 252 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.6d ago |
| 11 | 96 | Verathos | 66.7 | 1.0 | 15.10 | 462 | rtx4090 | 0.405 | 92 | 41% | RELEASE 4.0d ago |
| 12 | 38 | ChronoLLM | 66.5 | 0.85 | 113 | 1,537 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.8d ago |
| 13 | 107 | Minos | 64.8 | 1.0 | 132 | 43,370 | cpu-small | 0.000 | 19 | 91% | README_TASK_DIFF 12d ago |
| 14 | 85 | Vidaio | 64.2 | 0.85 | 129 | 400 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.3d ago |
| 15 | 108 | Prometheon | 63.8 | 0.85 | 117 | 126 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.1d ago |
| 16 | 81 | Reliquary | 63.8 | 0.85 | 116 | 211 | rtx4090 | 0.004 | 39 | 5% | SCORING_COMMIT 1.1d ago |
| 17 | 51 | lium.io | 61.1 | 0.85 | 60.39 | 4,428 | rtx4090 | 0.000 | 55 | 67% | SCORING_COMMIT 2.3d ago |
| 18 | 28 | gm | 59.9 | 0.85 | 37.21 | 1,658 | rtx4090 | 0.000 | 55 | 15% | RELEASE 2.1d ago |
| 19 | 60 | Bitsec.ai | 59.7 | 0.85 | 456 | 456 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 20 | 53 | engy | 59.5 | 0.85 | 31.91 | 217 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.5d ago |
| 21 | 61 | RedTeam | 57.8 | 0.85 | 18.70 | 273 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.3d ago |
| 22 | 68 | NOVA | 55.2 | 0.6 | 8,615 | 8,615 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.1d ago |
| 23 | 41 | Almanac | 55.2 | 1.0 | 11.19 | 23.47 | cpu-small | 0.729 | 78 | 73% | SCORING_COMMIT 10d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,135 | 7,135 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.8d ago |
| 25 | 124 | Swarm | 54.6 | 0.85 | 266 | 2,319 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.01 | cpu-small | 855.9203681833827 |
| 54 | Yanez | -3.65 | a4000 | 1147.8916709592713 |
| 89 | InfiniteQuant | -2.31 | rtx4090 | 117.52260861707333 |
| 13 | Data Universe | -2.97 | rtx4090 | 6.467806293595713 |
| 18 | Zeus | -4.41 | rtx4090 | 1700.0383529255498 |
| 123 | MANTIS | -5.61 | rtx4090 | 106.99464192574615 |
| 75 | Hippius | -6.30 | rtx4090 | 11309.41898322982 |
| 34 | BitMind | -19.42 | a100-80 | 319.1042097588985 |
| 101 | Tag101 | -0.03 | cpu-small | 2.330643430327361 |
| 6 | Numinous | -0.93 | cpu-small | 335.2675025747088 |
| 50 | Synth | -1.26 | rtx4090 | 91.63583078562107 |
| 104 | Masx.ai | -1.34 | rtx4090 | 12.551291076993511 |
| 88 | Investing | -3.33 | rtx4090 | 670.9064447975039 |
| 8 | Vanta | -7.39 | rtx4090 | 1065.5206411753686 |
| 43 | Graphite | -0.46 | cpu-small | 188.8711138939098 |
| 32 | ItsAI | -0.08 | rtx4090 | 10.69629068390075 |
| 19 | blockmachine | -1.52 | rtx4090 | 532.3153351487422 |
| 22 | Desearch | -4.84 | rtx4090 | 101.22491622925685 |
| 45 | AlphaRidge.ai | -4.96 | rtx4090 | 12.923602914028276 |
| 63 | Enigma | -8.14 | rtx4090 | 5345.981338230923 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.26 | 35.0 | 15.0 | 9.91 | 1.0 |
| 102 | 29.4 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.48 | 35.0 | 15.0 | 9.79 | 1.0 |
| 62 | 27.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 25.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.82 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 11.55 | 35.0 | 15.0 | 8.06 | 1.0 |
| 1 | 24.27 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.24 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.54 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 10.98 | 35.0 | 11.25 | 9.51 | 1.0 |
| 38 | 18.69 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.31 | 21.0 | 15.0 | 9.45 | 1.0 |
| 85 | 19.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.84 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.81 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.26 | 35.0 | 11.25 | 9.39 | 0.85 |
| 28 | 14.39 | 35.0 | 11.25 | 9.8 | 0.85 |
| 60 | 24.2 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.77 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.79 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.88 | 21.0 | 15.0 | 9.34 | 1.0 |
| 120 | 35.05 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.07 | 21.0 | 11.25 | 9.86 | 0.85 |
