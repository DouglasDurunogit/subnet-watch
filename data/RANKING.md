# RANKING - generated 2026-08-20T17:40:42Z, block 8887572

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
| 1 | 76 | Phylax | 76.8 | 1.0 | 70.83 | 126 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.3d ago |
| 2 | 67 | Harnyx | 72.1 | 1.0 | 21.50 | 286 | cpu-small | 0.032 | 178 | 8% | SCORING_COMMIT 0.3d ago |
| 3 | 23 | Trishool | 72.0 | 0.85 | 523 | 523 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.6d ago |
| 4 | 15 | ORO | 69.8 | 1.0 | 18.98 | 18,547 | cpu-small | 0.000 | 82 | 92% | SCORING_COMMIT 1.9d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 679 | 1,035 | rtx4090 | 0.723 | 5 | 72% | SCORING_COMMIT 2.7d ago |
| 6 | 1 | Apex | 69.5 | 0.85 | 647 | 1,436 | rtx4090 | 0.529 | 4 | 53% | RELEASE 0.9d ago |
| 7 | 91 | cascade | 69.3 | 0.85 | 611 | 2,470 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.5d ago |
| 8 | 38 | ChronoLLM | 67.7 | 0.85 | 158 | 3,348 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.9d ago |
| 9 | 11 | TrajectoryRL | 67.3 | 0.85 | 4,492 | 4,492 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 18d ago |
| 10 | 26 | Perturb | 67.3 | 1.0 | 17.26 | 249 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.7d ago |
| 11 | 96 | Verathos | 66.8 | 1.0 | 15.24 | 369 | rtx4090 | 0.406 | 95 | 41% | RELEASE 2.1d ago |
| 12 | 85 | Vidaio | 64.6 | 0.85 | 146 | 420 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.4d ago |
| 13 | 107 | Minos | 64.6 | 1.0 | 127 | 39,106 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 14 | 108 | Prometheon | 63.8 | 0.85 | 118 | 174 | rtx4090 | 0.664 | 7 | 66% | SCORING_COMMIT 0.7d ago |
| 15 | 28 | gm | 63.3 | 0.85 | 103 | 932 | rtx4090 | 0.000 | 49 | 8% | RELEASE 0.1d ago |
| 16 | 60 | Bitsec.ai | 62.4 | 0.85 | 1,027 | 1,027 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 17 | 81 | Reliquary | 61.9 | 0.85 | 65.13 | 212 | rtx4090 | 0.002 | 52 | 5% | SCORING_COMMIT 0.8d ago |
| 18 | 55 | NIOME | 61.7 | 0.85 | 61.36 | 514 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 5.9d ago |
| 19 | 51 | lium.io | 61.3 | 0.85 | 63.28 | 1,197 | rtx4090 | 0.000 | 47 | 82% | SCORING_COMMIT 0.4d ago |
| 20 | 102 | ConnitoAI | 60.5 | 0.85 | 1,508 | 1,510 | rtx4090 | 0.250 | 4 | 25% | RELEASE 20d ago |
| 21 | 53 | engy | 59.9 | 0.85 | 36.09 | 240 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.1d ago |
| 22 | 41 | Almanac | 55.4 | 1.0 | 11.59 | 24.69 | cpu-small | 0.719 | 76 | 72% | SCORING_COMMIT 8d ago |
| 23 | 68 | NOVA | 55.2 | 0.6 | 8,419 | 8,419 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.2d ago |
| 24 | 120 | Affine | 54.7 | 0.6 | 7,078 | 7,078 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.9d ago |
| 25 | 124 | Swarm | 54.4 | 0.85 | 258 | 751 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.42 | cpu-small | 4.73447866949054 |
| 54 | Yanez | -3.46 | a4000 | 1090.4375090154117 |
| 123 | MANTIS | -5.68 | rtx4090 | 94.5863189845413 |
| 75 | Hippius | -6.08 | rtx4090 | 12576.785663119144 |
| 114 | SOMA | -8.12 | rtx4090 | 4262.096929232547 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 109.88984144235042 |
| 6 | Numinous | -0.96 | cpu-small | 383.0307452152553 |
| 104 | Masx.ai | -1.86 | rtx4090 | 9.46122675695313 |
| 13 | Data Universe | -3.42 | rtx4090 | 5.687609817963737 |
| 88 | Investing | -4.33 | rtx4090 | 985.800684630771 |
| 8 | Vanta | -7.95 | rtx4090 | 2935.791477865656 |
| 43 | Graphite | -0.84 | cpu-small | 24.592021209485672 |
| 18 | Zeus | -4.09 | rtx4090 | 1585.4906715698976 |
| 45 | AlphaRidge.ai | -4.99 | rtx4090 | 11.611919624801162 |
| 19 | blockmachine | -7.88 | rtx4090 | 70.75721876983516 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07925064734014625 |
| 105 | Beam | -2.39 | rtx4090 | 78.18917819010115 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06495257081884506 |
| 34 | BitMind | -19.27 | a100-80 | 309.29419893983936 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn78, sn87, sn92, sn94, sn95, sn109, sn111, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.88 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.3 | 35.0 | 15.0 | 9.81 | 1.0 |
| 23 | 24.74 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 11.83 | 35.0 | 15.0 | 7.98 | 1.0 |
| 56 | 25.76 | 35.0 | 11.25 | 10.0 | 0.85 |
| 1 | 25.57 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.35 | 35.0 | 11.25 | 9.99 | 0.85 |
| 38 | 20.02 | 35.0 | 15.0 | 9.67 | 0.85 |
| 11 | 33.22 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.47 | 35.0 | 11.25 | 9.59 | 1.0 |
| 96 | 11.01 | 35.0 | 11.25 | 9.53 | 1.0 |
| 85 | 19.72 | 35.0 | 11.25 | 10.0 | 0.85 |
| 107 | 19.18 | 21.0 | 15.0 | 9.45 | 1.0 |
| 108 | 18.89 | 35.0 | 11.25 | 9.97 | 0.85 |
| 28 | 18.34 | 35.0 | 11.25 | 9.93 | 0.85 |
| 60 | 27.39 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 16.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.44 | 35.0 | 11.25 | 9.44 | 0.85 |
| 102 | 28.91 | 21.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.27 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.0 | 21.0 | 15.0 | 9.39 | 1.0 |
| 68 | 35.7 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.02 | 35.0 | 11.25 | 9.96 | 0.6 |
| 124 | 21.94 | 21.0 | 11.25 | 9.86 | 0.85 |
