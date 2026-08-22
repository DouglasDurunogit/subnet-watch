# RANKING - generated 2026-08-22T14:01:18Z, block 8900875

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
| 1 | 76 | Phylax | 77.2 | 1.0 | 79.16 | 133 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.2d ago |
| 2 | 102 | ConnitoAI | 72.8 | 0.85 | 1,731 | 1,731 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.9d ago |
| 3 | 23 | Trishool | 72.3 | 0.85 | 563 | 563 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 2.4d ago |
| 4 | 67 | Harnyx | 72.3 | 1.0 | 22.83 | 445 | cpu-small | 0.071 | 145 | 12% | SCORING_COMMIT 1.1d ago |
| 5 | 62 | Ridges | 71.6 | 0.85 | 1,210 | 2,978 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.6d ago |
| 6 | 56 | Gradients | 70.0 | 0.85 | 730 | 1,071 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.6d ago |
| 7 | 15 | ORO | 69.9 | 1.0 | 18.20 | 21,735 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.6d ago |
| 8 | 91 | cascade | 69.8 | 0.85 | 693 | 2,797 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.6d ago |
| 9 | 1 | Apex | 68.5 | 0.85 | 475 | 1,119 | rtx4090 | 0.550 | 5 | 55% | RELEASE 1.0d ago |
| 10 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,625 | 4,625 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 11 | 26 | Perturb | 67.4 | 1.0 | 17.86 | 256 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.5d ago |
| 12 | 96 | Verathos | 67.1 | 1.0 | 16.30 | 501 | rtx4090 | 0.405 | 86 | 41% | RELEASE 3.9d ago |
| 13 | 38 | ChronoLLM | 66.5 | 0.85 | 114 | 1,551 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.7d ago |
| 14 | 107 | Minos | 65.3 | 1.0 | 148 | 43,511 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 15 | 85 | Vidaio | 64.5 | 0.85 | 141 | 403 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.3d ago |
| 16 | 81 | Reliquary | 64.1 | 0.85 | 127 | 217 | rtx4090 | 0.006 | 40 | 5% | SCORING_COMMIT 1.0d ago |
| 17 | 108 | Prometheon | 63.9 | 0.85 | 119 | 128 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.0d ago |
| 18 | 60 | Bitsec.ai | 59.7 | 0.85 | 465 | 465 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 19 | 53 | engy | 59.6 | 0.85 | 32.84 | 222 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.4d ago |
| 20 | 51 | lium.io | 59.5 | 0.85 | 40.49 | 4,501 | rtx4090 | 0.000 | 55 | 66% | SCORING_COMMIT 2.2d ago |
| 21 | 28 | gm | 58.4 | 0.85 | 24.28 | 1,963 | rtx4090 | 0.090 | 56 | 17% | RELEASE 2.0d ago |
| 22 | 61 | RedTeam | 57.9 | 0.85 | 19.12 | 277 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.2d ago |
| 23 | 68 | NOVA | 55.3 | 0.6 | 8,741 | 8,741 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.0d ago |
| 24 | 41 | Almanac | 55.3 | 1.0 | 11.32 | 23.83 | cpu-small | 0.729 | 78 | 73% | SCORING_COMMIT 10d ago |
| 25 | 120 | Affine | 54.8 | 0.6 | 7,278 | 7,278 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.39 | a4000 | 1167.9362951749506 |
| 89 | InfiniteQuant | -1.86 | rtx4090 | 110.68688351803641 |
| 13 | Data Universe | -3.02 | rtx4090 | 6.626543721719247 |
| 18 | Zeus | -3.54 | rtx4090 | 2102.584713982524 |
| 123 | MANTIS | -5.57 | rtx4090 | 108.35320839478355 |
| 75 | Hippius | -6.27 | rtx4090 | 11481.982466804637 |
| 34 | BitMind | -19.09 | a100-80 | 323.84237897558364 |
| 101 | Tag101 | -0.01 | cpu-small | 2.365711283478619 |
| 6 | Numinous | -0.93 | cpu-small | 339.87710488771194 |
| 50 | Synth | -1.06 | rtx4090 | 102.90190553019829 |
| 104 | Masx.ai | -1.85 | rtx4090 | 13.22242292731649 |
| 88 | Investing | -3.29 | rtx4090 | 676.935782445365 |
| 8 | Vanta | -7.38 | rtx4090 | 1069.8426416832747 |
| 43 | Graphite | -0.46 | cpu-small | 191.69849876872334 |
| 19 | blockmachine | -1.42 | rtx4090 | 540.229120261914 |
| 45 | AlphaRidge.ai | -4.55 | rtx4090 | 13.49670209308297 |
| 22 | Desearch | -5.21 | rtx4090 | 101.98092031305315 |
| 63 | Enigma | -8.14 | rtx4090 | 5427.5874612847065 |
| 105 | Beam | -2.14 | rtx4090 | 81.28246740722261 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06966346534259592 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.32 | 35.0 | 15.0 | 9.91 | 1.0 |
| 102 | 29.45 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.02 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.53 | 35.0 | 15.0 | 9.75 | 1.0 |
| 62 | 28.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 26.05 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.67 | 35.0 | 15.0 | 8.18 | 1.0 |
| 91 | 25.84 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.34 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.6 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.26 | 35.0 | 11.25 | 9.54 | 1.0 |
| 38 | 18.73 | 35.0 | 15.0 | 9.51 | 0.85 |
| 107 | 19.78 | 21.0 | 15.0 | 9.5 | 1.0 |
| 85 | 19.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 19.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.9 | 35.0 | 11.25 | 9.97 | 0.85 |
| 60 | 24.27 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.72 | 35.0 | 11.25 | 9.08 | 0.85 |
| 28 | 12.76 | 35.0 | 11.25 | 9.69 | 0.85 |
| 61 | 11.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.85 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.92 | 21.0 | 15.0 | 9.34 | 1.0 |
| 120 | 35.13 | 35.0 | 11.25 | 9.99 | 0.6 |
