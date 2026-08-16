# RANKING - generated 2026-08-16T13:40:01Z, block 8857570

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
| 1 | 107 | Minos | 78.0 | 1.0 | 109 | 32,846 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.9d ago |
| 2 | 76 | Phylax | 73.8 | 1.0 | 31.72 | 157 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.1d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.65 | 418 | cpu-small | 0.018 | 136 | 11% | SCORING_COMMIT 0.3d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.49 | 74.28 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.9d ago |
| 5 | 1 | Apex | 70.1 | 0.85 | 767 | 1,058 | rtx4090 | 0.547 | 4 | 55% | RELEASE 3.0d ago |
| 6 | 96 | Verathos | 70.1 | 1.0 | 34.72 | 196 | rtx4090 | 0.406 | 56 | 41% | RELEASE 1.7d ago |
| 7 | 41 | Almanac | 69.9 | 1.0 | 12.83 | 47.72 | cpu-small | 0.651 | 75 | 65% | SCORING_COMMIT 3.6d ago |
| 8 | 15 | ORO | 69.0 | 1.0 | 12.86 | 12,797 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 2.6d ago |
| 9 | 56 | Gradients | 68.7 | 0.85 | 504 | 958 | rtx4090 | 0.676 | 7 | 68% | SCORING_COMMIT 4.0d ago |
| 10 | 62 | Ridges | 68.5 | 0.85 | 475 | 2,199 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.6d ago |
| 11 | 91 | cascade | 68.3 | 0.85 | 444 | 2,284 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.6d ago |
| 12 | 85 | Vidaio | 67.9 | 0.85 | 396 | 498 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 4.1d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.63 | 34.21 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.1d ago |
| 14 | 11 | TrajectoryRL | 67.0 | 0.85 | 4,110 | 4,110 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 124 | Swarm | 65.9 | 0.85 | 223 | 717 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.9d ago |
| 16 | 38 | ChronoLLM | 65.9 | 0.85 | 96.52 | 1,320 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.9d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.63 | 478 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.7d ago |
| 18 | 28 | gm | 60.7 | 0.85 | 47.62 | 2,793 | rtx4090 | 0.046 | 43 | 31% | RELEASE 4.0d ago |
| 19 | 60 | Bitsec.ai | 59.3 | 0.85 | 412 | 412 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 20 | 74 | Gittensor | 58.5 | 0.85 | 26.20 | 208 | rtx4090 | 0.630 | 14 | 63% | RELEASE 4.8d ago |
| 21 | 61 | RedTeam | 57.6 | 0.85 | 17.29 | 438 | rtx4090 | 0.000 | 81 | 10% | RELEASE 5.2d ago |
| 22 | 51 | lium.io | 57.2 | 0.85 | 22.41 | 1,353 | rtx4090 | 0.000 | 53 | 82% | SCORING_COMMIT 2.2d ago |
| 23 | 102 | ConnitoAI | 56.9 | 0.85 | 516 | 1,891 | rtx4090 | 0.251 | 7 | 35% | RELEASE 16d ago |
| 24 | 120 | Affine | 55.8 | 0.6 | 10,970 | 11,301 | rtx4090 | 0.340 | 3 | 34% | SCORING_COMMIT 4.0d ago |
| 25 | 68 | NOVA | 55.1 | 0.6 | 8,031 | 8,031 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 244.07728808754754 |
| 54 | Yanez | -4.02 | a4000 | 947.2492956133152 |
| 104 | Masx.ai | -0.06 | rtx4090 | 10.452448899842853 |
| 89 | InfiniteQuant | -4.76 | rtx4090 | 129.43692256485232 |
| 75 | Hippius | -7.21 | rtx4090 | 10919.62650027642 |
| 13 | Data Universe | -3.59 | rtx4090 | 6.009807493997876 |
| 88 | Investing | -5.44 | rtx4090 | 1121.1018448730692 |
| 8 | Vanta | -7.70 | rtx4090 | 2903.6277581048594 |
| 114 | SOMA | -8.13 | rtx4090 | 601.0658479156343 |
| 43 | Graphite | -0.78 | cpu-small | 17.359290000339215 |
| 32 | ItsAI | -0.23 | rtx4090 | 11.00211398033762 |
| 45 | AlphaRidge.ai | -2.00 | rtx4090 | 19.139297999295326 |
| 22 | Desearch | -2.49 | rtx4090 | 48.39425071219102 |
| 18 | Zeus | -3.74 | rtx4090 | 1604.0918941635437 |
| 19 | blockmachine | -5.85 | rtx4090 | 502.66009879809627 |
| 123 | MANTIS | -6.03 | rtx4090 | 75.43219477578043 |
| 63 | Enigma | -8.14 | rtx4090 | 5024.222013073799 |
| 105 | Beam | -3.32 | rtx4090 | 88.92919906037167 |
| 84 | ansuz | -8.16 | rtx4090 | 439.1660035398802 |
| 34 | BitMind | -19.94 | a100-80 | 21.74923158203105 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.57 | 35.0 | 15.0 | 9.41 | 1.0 |
| 76 | 13.78 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.66 | 35.0 | 15.0 | 9.84 | 1.0 |
| 26 | 14.72 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 14.12 | 35.0 | 11.25 | 9.77 | 1.0 |
| 41 | 10.38 | 35.0 | 15.0 | 9.49 | 1.0 |
| 15 | 10.38 | 35.0 | 15.0 | 8.65 | 1.0 |
| 56 | 24.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.35 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.09 | 35.0 | 11.25 | 9.99 | 0.85 |
| 85 | 23.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.51 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 32.87 | 21.0 | 15.0 | 10.0 | 0.85 |
| 124 | 21.38 | 35.0 | 11.25 | 9.85 | 0.85 |
| 38 | 18.09 | 35.0 | 15.0 | 9.5 | 0.85 |
| 55 | 16.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.34 | 35.0 | 11.25 | 9.86 | 0.85 |
| 60 | 23.79 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 13.05 | 35.0 | 11.25 | 9.51 | 0.85 |
| 61 | 11.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.45 | 35.0 | 11.25 | 8.54 | 0.85 |
| 102 | 24.68 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 36.75 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.51 | 35.0 | 11.25 | 10.0 | 0.6 |
