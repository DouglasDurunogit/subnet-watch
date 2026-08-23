# RANKING - generated 2026-08-23T19:10:14Z, block 8909620

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 75.75 | 84.80 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.1d ago |
| 2 | 67 | Harnyx | 72.9 | 1.0 | 25.60 | 820 | cpu-small | 0.026 | 125 | 20% | SCORING_COMMIT 2.4d ago |
| 3 | 23 | Trishool | 72.4 | 0.85 | 595 | 595 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.6d ago |
| 4 | 102 | ConnitoAI | 72.0 | 0.85 | 1,361 | 2,541 | rtx4090 | 0.252 | 5 | 36% | RELEASE 2.1d ago |
| 5 | 62 | Ridges | 71.9 | 0.85 | 1,289 | 3,173 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.8d ago |
| 6 | 15 | ORO | 71.8 | 1.0 | 26.76 | 45.75 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 1.8d ago |
| 7 | 56 | Gradients | 69.9 | 0.85 | 728 | 1,143 | rtx4090 | 0.730 | 5 | 73% | SCORING_COMMIT 5.8d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 561 | 1,509 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.8d ago |
| 9 | 1 | Apex | 68.9 | 0.85 | 537 | 1,213 | rtx4090 | 0.543 | 5 | 54% | RELEASE 2.2d ago |
| 10 | 96 | Verathos | 68.6 | 1.0 | 23.80 | 310 | rtx4090 | 0.403 | 88 | 40% | RELEASE 5.1d ago |
| 11 | 26 | Perturb | 67.7 | 1.0 | 19.28 | 275 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.7d ago |
| 12 | 124 | Swarm | 66.8 | 0.85 | 293 | 2,550 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.3d ago |
| 13 | 38 | ChronoLLM | 66.7 | 0.85 | 120 | 1,644 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.9d ago |
| 14 | 108 | Prometheon | 65.5 | 0.85 | 192 | 211 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.2d ago |
| 15 | 107 | Minos | 65.4 | 1.0 | 154 | 43,538 | cpu-small | 0.000 | 20 | 89% | README_TASK_DIFF 13d ago |
| 16 | 81 | Reliquary | 64.9 | 0.85 | 161 | 271 | rtx4090 | 0.006 | 36 | 6% | SCORING_COMMIT 1.0d ago |
| 17 | 85 | Vidaio | 64.7 | 0.85 | 152 | 438 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.5d ago |
| 18 | 51 | lium.io | 61.5 | 0.85 | 68.34 | 2,113 | rtx4090 | 0.000 | 53 | 71% | SCORING_COMMIT 3.5d ago |
| 19 | 53 | engy | 60.2 | 0.85 | 39.22 | 13,034 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.6d ago |
| 20 | 60 | Bitsec.ai | 60.1 | 0.85 | 518 | 518 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 21 | 28 | gm | 59.3 | 0.85 | 31.75 | 1,644 | rtx4090 | 0.238 | 55 | 24% | RELEASE 3.2d ago |
| 22 | 61 | RedTeam | 57.1 | 0.85 | 14.87 | 303 | rtx4090 | 0.000 | 85 | 6% | RELEASE 1.5d ago |
| 23 | 41 | Almanac | 56.5 | 1.0 | 15.31 | 29.90 | cpu-small | 0.641 | 79 | 64% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,593 | 7,593 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.9d ago |
| 25 | 33 | ReadyAI | 54.3 | 0.85 | 6.87 | 11.82 | rtx4090 | 0.000 | 243 | 1% | SCORING_COMMIT 3.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.15 | a4000 | 1238.5256268585076 |
| 89 | InfiniteQuant | -1.08 | rtx4090 | 117.97555232870418 |
| 13 | Data Universe | -2.57 | rtx4090 | 7.725428723478407 |
| 18 | Zeus | -3.19 | rtx4090 | 1901.51583322549 |
| 123 | MANTIS | -5.62 | rtx4090 | 121.03640741525953 |
| 75 | Hippius | -6.29 | rtx4090 | 12510.107170983862 |
| 34 | BitMind | -18.69 | a100-80 | 346.34993035756594 |
| 6 | Numinous | -0.92 | cpu-small | 187.47097414982383 |
| 50 | Synth | -1.21 | rtx4090 | 67.21222674152688 |
| 104 | Masx.ai | -2.21 | rtx4090 | 10.513829454998069 |
| 88 | Investing | -2.68 | rtx4090 | 693.5945509711541 |
| 8 | Vanta | -7.32 | rtx4090 | 3373.857872697672 |
| 43 | Graphite | -0.25 | cpu-small | 198.73354889328027 |
| 22 | Desearch | -0.18 | rtx4090 | 68.66108027380511 |
| 19 | blockmachine | -0.56 | rtx4090 | 584.3201287969254 |
| 45 | AlphaRidge.ai | -3.77 | rtx4090 | 14.157193089032972 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08729008254516105 |
| 105 | Beam | -1.72 | rtx4090 | 85.80225701510042 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07283682053221081 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.15 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 12.96 | 35.0 | 15.0 | 9.9 | 1.0 |
| 23 | 25.24 | 35.0 | 15.0 | 9.99 | 0.85 |
| 102 | 28.51 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 28.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 13.13 | 35.0 | 15.0 | 8.63 | 1.0 |
| 56 | 26.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.01 | 35.0 | 11.25 | 9.98 | 0.85 |
| 1 | 24.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.68 | 35.0 | 11.25 | 9.67 | 1.0 |
| 26 | 11.89 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.45 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.96 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.79 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.91 | 21.0 | 15.0 | 9.49 | 1.0 |
| 81 | 20.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.74 | 35.0 | 11.25 | 9.42 | 0.85 |
| 53 | 14.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.7 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.78 | 35.0 | 11.25 | 9.75 | 0.85 |
| 61 | 10.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 11.03 | 21.0 | 15.0 | 9.48 | 1.0 |
| 120 | 35.29 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 8.15 | 35.0 | 11.25 | 9.45 | 0.85 |
