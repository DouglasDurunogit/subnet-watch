# RANKING - generated 2026-08-16T12:57:21Z, block 8857356

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
| 1 | 107 | Minos | 78.1 | 1.0 | 113 | 32,627 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.9d ago |
| 2 | 76 | Phylax | 73.9 | 1.0 | 32.52 | 158 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.0d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.59 | 417 | cpu-small | 0.018 | 136 | 11% | SCORING_COMMIT 0.3d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.38 | 74.08 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.9d ago |
| 5 | 96 | Verathos | 70.2 | 1.0 | 35.07 | 197 | rtx4090 | 0.406 | 56 | 41% | RELEASE 1.7d ago |
| 6 | 1 | Apex | 70.1 | 0.85 | 768 | 1,059 | rtx4090 | 0.545 | 4 | 55% | RELEASE 2.9d ago |
| 7 | 41 | Almanac | 69.9 | 1.0 | 12.84 | 53.65 | cpu-small | 0.651 | 74 | 65% | SCORING_COMMIT 3.6d ago |
| 8 | 15 | ORO | 69.1 | 1.0 | 12.82 | 12,761 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 2.6d ago |
| 9 | 85 | Vidaio | 68.8 | 0.85 | 513 | 584 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 4.1d ago |
| 10 | 56 | Gradients | 68.7 | 0.85 | 503 | 956 | rtx4090 | 0.676 | 7 | 68% | SCORING_COMMIT 4.0d ago |
| 11 | 62 | Ridges | 68.5 | 0.85 | 474 | 2,193 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.6d ago |
| 12 | 91 | cascade | 68.3 | 0.85 | 443 | 2,278 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.6d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.61 | 34.12 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.0d ago |
| 14 | 11 | TrajectoryRL | 67.0 | 0.85 | 4,084 | 4,084 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 96.67 | 1,322 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.8d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 223 | 715 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.9d ago |
| 17 | 2 | DSperse | 62.8 | 0.85 | 86.24 | 151 | rtx4090 | 0.822 | 5 | 82% | RELEASE 5.7d ago |
| 18 | 55 | NIOME | 61.4 | 0.85 | 56.81 | 469 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.7d ago |
| 19 | 28 | gm | 60.2 | 0.85 | 41.09 | 2,550 | rtx4090 | 0.077 | 42 | 28% | RELEASE 4.0d ago |
| 20 | 60 | Bitsec.ai | 59.3 | 0.85 | 411 | 411 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 21 | 74 | Gittensor | 58.4 | 0.85 | 26.05 | 207 | rtx4090 | 0.630 | 14 | 63% | RELEASE 4.8d ago |
| 22 | 61 | RedTeam | 57.6 | 0.85 | 17.28 | 438 | rtx4090 | 0.000 | 81 | 10% | RELEASE 5.2d ago |
| 23 | 51 | lium.io | 57.1 | 0.85 | 22.32 | 1,349 | rtx4090 | 0.000 | 53 | 82% | SCORING_COMMIT 2.2d ago |
| 24 | 102 | ConnitoAI | 56.9 | 0.85 | 515 | 1,888 | rtx4090 | 0.251 | 7 | 35% | RELEASE 16d ago |
| 25 | 120 | Affine | 55.7 | 0.6 | 10,726 | 11,736 | rtx4090 | 0.354 | 3 | 35% | SCORING_COMMIT 4.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 242.89347832046195 |
| 54 | Yanez | -3.86 | a4000 | 945.6849979226861 |
| 104 | Masx.ai | -0.04 | rtx4090 | 9.195240904184141 |
| 89 | InfiniteQuant | -4.67 | rtx4090 | 129.0368502385192 |
| 75 | Hippius | -7.21 | rtx4090 | 10891.785257869455 |
| 13 | Data Universe | -3.61 | rtx4090 | 5.820722490627943 |
| 88 | Investing | -5.44 | rtx4090 | 1122.2384588851094 |
| 8 | Vanta | -7.71 | rtx4090 | 2896.3953417240978 |
| 114 | SOMA | -8.13 | rtx4090 | 599.4762092782814 |
| 43 | Graphite | -0.75 | cpu-small | 16.706499970161676 |
| 32 | ItsAI | -0.39 | rtx4090 | 10.7337335080571 |
| 22 | Desearch | -2.65 | rtx4090 | 71.84439469875281 |
| 18 | Zeus | -3.76 | rtx4090 | 1594.0724003416192 |
| 45 | AlphaRidge.ai | -4.10 | rtx4090 | 18.09730936194365 |
| 123 | MANTIS | -6.04 | rtx4090 | 75.24417089473536 |
| 19 | blockmachine | -6.19 | rtx4090 | 1082.2318163546236 |
| 63 | Enigma | -8.14 | rtx4090 | 5011.39802660455 |
| 105 | Beam | -2.92 | rtx4090 | 89.79503785216248 |
| 84 | ansuz | -8.16 | rtx4090 | 438.12042501391034 |
| 34 | BitMind | -20.18 | a100-80 | 21.26776368335359 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.71 | 35.0 | 15.0 | 9.43 | 1.0 |
| 76 | 13.87 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.65 | 35.0 | 15.0 | 9.81 | 1.0 |
| 26 | 14.7 | 35.0 | 11.25 | 9.84 | 1.0 |
| 96 | 14.16 | 35.0 | 11.25 | 9.81 | 1.0 |
| 1 | 26.25 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.38 | 35.0 | 15.0 | 9.49 | 1.0 |
| 15 | 10.37 | 35.0 | 15.0 | 8.72 | 1.0 |
| 85 | 24.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.34 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.08 | 35.0 | 11.25 | 9.99 | 0.85 |
| 21 | 8.5 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 32.84 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.1 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.37 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 17.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.77 | 35.0 | 11.25 | 9.84 | 0.85 |
| 60 | 23.78 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 13.03 | 35.0 | 11.25 | 9.45 | 0.85 |
| 61 | 11.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.44 | 35.0 | 11.25 | 8.54 | 0.85 |
| 102 | 24.67 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 36.66 | 35.0 | 11.25 | 9.99 | 0.6 |
