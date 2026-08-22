# RANKING - generated 2026-08-22T20:35:29Z, block 8902846

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 75.60 | 134 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.5d ago |
| 2 | 67 | Harnyx | 72.4 | 1.0 | 23.05 | 119 | cpu-small | 0.052 | 151 | 12% | SCORING_COMMIT 1.4d ago |
| 3 | 62 | Ridges | 71.7 | 0.85 | 1,220 | 3,003 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.9d ago |
| 4 | 15 | ORO | 70.7 | 1.0 | 19.38 | 23,073 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.9d ago |
| 5 | 56 | Gradients | 70.0 | 0.85 | 733 | 1,079 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.9d ago |
| 6 | 91 | cascade | 69.8 | 0.85 | 691 | 2,787 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.9d ago |
| 7 | 1 | Apex | 68.7 | 0.85 | 496 | 1,267 | rtx4090 | 0.518 | 5 | 52% | RELEASE 1.2d ago |
| 8 | 102 | ConnitoAI | 68.5 | 0.85 | 481 | 2,312 | rtx4090 | 0.250 | 7 | 33% | RELEASE 1.2d ago |
| 9 | 96 | Verathos | 67.8 | 1.0 | 19.57 | 440 | rtx4090 | 0.402 | 91 | 40% | RELEASE 4.2d ago |
| 10 | 26 | Perturb | 67.5 | 1.0 | 18.04 | 258 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.8d ago |
| 11 | 38 | ChronoLLM | 66.6 | 0.85 | 115 | 1,575 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.0d ago |
| 12 | 107 | Minos | 65.2 | 1.0 | 150 | 43,402 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 13 | 85 | Vidaio | 64.2 | 0.85 | 130 | 405 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.6d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 119 | 129 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.3d ago |
| 15 | 81 | Reliquary | 63.3 | 0.85 | 99.08 | 222 | rtx4090 | 0.002 | 43 | 5% | SCORING_COMMIT 0.1d ago |
| 16 | 51 | lium.io | 61.5 | 0.85 | 66.60 | 4,438 | rtx4090 | 0.000 | 51 | 69% | SCORING_COMMIT 2.5d ago |
| 17 | 28 | gm | 60.1 | 0.85 | 39.24 | 1,901 | rtx4090 | 0.082 | 53 | 17% | RELEASE 2.3d ago |
| 18 | 60 | Bitsec.ai | 59.8 | 0.85 | 481 | 481 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 19 | 53 | engy | 59.4 | 0.85 | 30.84 | 211 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.7d ago |
| 20 | 61 | RedTeam | 57.7 | 0.85 | 18.19 | 285 | rtx4090 | 0.000 | 87 | 6% | RELEASE 0.5d ago |
| 21 | 68 | NOVA | 55.3 | 0.6 | 8,771 | 8,771 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.3d ago |
| 22 | 41 | Almanac | 55.3 | 1.0 | 11.31 | 24.02 | cpu-small | 0.731 | 78 | 73% | SCORING_COMMIT 10d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,174 | 7,174 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.0d ago |
| 24 | 124 | Swarm | 54.6 | 0.85 | 272 | 2,368 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |
| 25 | 33 | ReadyAI | 53.8 | 0.85 | 6.25 | 10.05 | rtx4090 | 0.000 | 243 | 1% | SCORING_COMMIT 2.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.06 | a4000 | 1227.7689195815963 |
| 13 | Data Universe | -2.66 | rtx4090 | 6.682657423733514 |
| 89 | InfiniteQuant | -3.25 | rtx4090 | 118.36496675558696 |
| 18 | Zeus | -4.37 | rtx4090 | 1717.9057803495027 |
| 123 | MANTIS | -5.69 | rtx4090 | 106.58372167228792 |
| 75 | Hippius | -6.42 | rtx4090 | 11663.445850184984 |
| 34 | BitMind | -19.37 | a100-80 | 326.51936705012866 |
| 6 | Numinous | -0.94 | cpu-small | 290.1227062121176 |
| 50 | Synth | -1.63 | rtx4090 | 57.32929353644422 |
| 104 | Masx.ai | -1.80 | rtx4090 | 8.282297071096423 |
| 88 | Investing | -3.25 | rtx4090 | 682.3320587235933 |
| 8 | Vanta | -7.37 | rtx4090 | 1090.4149884400583 |
| 43 | Graphite | -0.45 | cpu-small | 193.10713166621218 |
| 19 | blockmachine | -1.02 | rtx4090 | 549.3123664715737 |
| 45 | AlphaRidge.ai | -4.47 | rtx4090 | 10.942438819307831 |
| 22 | Desearch | -4.74 | rtx4090 | 80.07684070242819 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08351937144080139 |
| 105 | Beam | -2.16 | rtx4090 | 80.1339385223365 |
| 84 | ansuz | -8.15 | rtx4090 | 0.070228559862821 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.14 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.56 | 35.0 | 15.0 | 9.86 | 1.0 |
| 62 | 28.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.91 | 35.0 | 15.0 | 8.76 | 1.0 |
| 56 | 26.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.83 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 24.4 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 11.94 | 35.0 | 11.25 | 9.62 | 1.0 |
| 26 | 11.64 | 35.0 | 11.25 | 9.58 | 1.0 |
| 38 | 18.79 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.83 | 21.0 | 15.0 | 9.39 | 1.0 |
| 85 | 19.25 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.92 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.64 | 35.0 | 11.25 | 9.44 | 0.85 |
| 28 | 14.59 | 35.0 | 11.25 | 9.81 | 0.85 |
| 60 | 24.41 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.86 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.92 | 21.0 | 15.0 | 9.34 | 1.0 |
| 120 | 35.07 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.15 | 21.0 | 11.25 | 9.86 | 0.85 |
| 33 | 7.83 | 35.0 | 11.25 | 9.2 | 0.85 |
