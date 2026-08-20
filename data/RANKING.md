# RANKING - generated 2026-08-20T20:41:08Z, block 8888474

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 74.32 | 125 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.5d ago |
| 2 | 67 | Harnyx | 72.1 | 1.0 | 21.34 | 283 | cpu-small | 0.032 | 176 | 8% | SCORING_COMMIT 0.5d ago |
| 3 | 23 | Trishool | 72.0 | 0.85 | 516 | 516 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.7d ago |
| 4 | 15 | ORO | 70.1 | 1.0 | 19.06 | 18,619 | cpu-small | 0.000 | 82 | 92% | SCORING_COMMIT 2.1d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 670 | 1,023 | rtx4090 | 0.723 | 5 | 72% | SCORING_COMMIT 2.9d ago |
| 6 | 91 | cascade | 69.3 | 0.85 | 603 | 2,436 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.7d ago |
| 7 | 1 | Apex | 68.1 | 0.85 | 426 | 1,206 | rtx4090 | 0.527 | 5 | 53% | RELEASE 1.0d ago |
| 8 | 38 | ChronoLLM | 67.6 | 0.85 | 154 | 3,268 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.0d ago |
| 9 | 11 | TrajectoryRL | 67.3 | 0.85 | 4,439 | 4,439 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 18d ago |
| 10 | 26 | Perturb | 67.2 | 1.0 | 16.93 | 246 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.8d ago |
| 11 | 96 | Verathos | 67.1 | 1.0 | 16.26 | 370 | rtx4090 | 0.404 | 94 | 40% | RELEASE 2.2d ago |
| 12 | 107 | Minos | 64.7 | 1.0 | 128 | 37,164 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 13 | 85 | Vidaio | 64.6 | 0.85 | 146 | 415 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.6d ago |
| 14 | 108 | Prometheon | 63.8 | 0.85 | 118 | 174 | rtx4090 | 0.662 | 7 | 66% | SCORING_COMMIT 0.8d ago |
| 15 | 28 | gm | 63.4 | 0.85 | 104 | 1,656 | rtx4090 | 0.033 | 53 | 15% | RELEASE 0.3d ago |
| 16 | 55 | NIOME | 61.7 | 0.85 | 62.15 | 520 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 6.0d ago |
| 17 | 51 | lium.io | 61.5 | 0.85 | 65.58 | 1,173 | rtx4090 | 0.000 | 47 | 82% | SCORING_COMMIT 0.5d ago |
| 18 | 81 | Reliquary | 61.4 | 0.85 | 56.93 | 204 | rtx4090 | 0.002 | 50 | 5% | SCORING_COMMIT 1.0d ago |
| 19 | 60 | Bitsec.ai | 61.2 | 0.85 | 724 | 1,013 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 20 | 102 | ConnitoAI | 60.1 | 0.85 | 1,351 | 1,623 | rtx4090 | 0.250 | 5 | 28% | RELEASE 20d ago |
| 21 | 53 | engy | 59.9 | 0.85 | 35.56 | 237 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.2d ago |
| 22 | 41 | Almanac | 55.3 | 1.0 | 11.30 | 23.35 | cpu-small | 0.721 | 77 | 72% | SCORING_COMMIT 8d ago |
| 23 | 68 | NOVA | 55.1 | 0.6 | 8,323 | 8,323 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.3d ago |
| 24 | 120 | Affine | 54.7 | 0.6 | 7,057 | 7,057 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.0d ago |
| 25 | 124 | Swarm | 54.4 | 0.85 | 253 | 738 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.42 | cpu-small | 4.706169936134414 |
| 54 | Yanez | -3.69 | a4000 | 1079.085641807495 |
| 18 | Zeus | -4.14 | rtx4090 | 1562.6298470931938 |
| 123 | MANTIS | -5.76 | rtx4090 | 94.55640871338481 |
| 75 | Hippius | -6.00 | rtx4090 | 12464.614735008312 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 125.89443919850471 |
| 6 | Numinous | -0.96 | cpu-small | 378.4153411925043 |
| 104 | Masx.ai | -2.67 | rtx4090 | 8.895742252159103 |
| 13 | Data Universe | -3.69 | rtx4090 | 6.363207698396693 |
| 88 | Investing | -4.44 | rtx4090 | 958.0856404838026 |
| 8 | Vanta | -7.95 | rtx4090 | 7379.0863452992835 |
| 43 | Graphite | -0.79 | cpu-small | 25.343662076022493 |
| 32 | ItsAI | -0.30 | rtx4090 | 11.86803672907396 |
| 19 | blockmachine | -1.14 | rtx4090 | 1487.0482604674107 |
| 45 | AlphaRidge.ai | -4.56 | rtx4090 | 10.74298157903617 |
| 63 | Enigma | -8.14 | rtx4090 | 0.078398109753853 |
| 105 | Beam | -2.31 | rtx4090 | 77.63953813273645 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06420669936433095 |
| 34 | BitMind | -19.73 | a100-80 | 3058.0277323526298 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn2, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.07 | 35.0 | 15.0 | 9.91 | 1.0 |
| 67 | 12.27 | 35.0 | 15.0 | 9.83 | 1.0 |
| 23 | 24.68 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 11.84 | 35.0 | 15.0 | 8.24 | 1.0 |
| 56 | 25.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.29 | 35.0 | 11.25 | 9.97 | 0.85 |
| 1 | 23.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.92 | 35.0 | 15.0 | 9.66 | 0.85 |
| 11 | 33.17 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.4 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.25 | 35.0 | 11.25 | 9.57 | 1.0 |
| 107 | 19.2 | 21.0 | 15.0 | 9.46 | 1.0 |
| 85 | 19.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.89 | 35.0 | 11.25 | 9.97 | 0.85 |
| 28 | 18.39 | 35.0 | 11.25 | 9.93 | 0.85 |
| 55 | 16.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.58 | 35.0 | 11.25 | 9.46 | 0.85 |
| 81 | 16.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.01 | 21.0 | 15.0 | 10.0 | 0.85 |
| 102 | 28.48 | 21.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.91 | 21.0 | 15.0 | 9.38 | 1.0 |
| 68 | 35.66 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.0 | 35.0 | 11.25 | 9.98 | 0.6 |
| 124 | 21.88 | 21.0 | 11.25 | 9.83 | 0.85 |
