# RANKING - generated 2026-08-23T16:00:59Z, block 8908674

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
| 1 | 76 | Phylax | 76.9 | 1.0 | 73.61 | 82.41 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 4.3d ago |
| 2 | 102 | ConnitoAI | 72.9 | 0.85 | 1,747 | 1,748 | rtx4090 | 0.250 | 4 | 25% | RELEASE 2.0d ago |
| 3 | 67 | Harnyx | 72.7 | 1.0 | 24.86 | 797 | cpu-small | 0.026 | 125 | 20% | SCORING_COMMIT 2.2d ago |
| 4 | 23 | Trishool | 72.3 | 0.85 | 572 | 572 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.5d ago |
| 5 | 62 | Ridges | 71.8 | 0.85 | 1,256 | 3,093 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.7d ago |
| 6 | 15 | ORO | 71.5 | 1.0 | 25.05 | 43.19 | cpu-small | 0.000 | 79 | 93% | SCORING_COMMIT 1.7d ago |
| 7 | 56 | Gradients | 69.9 | 0.85 | 708 | 1,112 | rtx4090 | 0.730 | 5 | 73% | SCORING_COMMIT 5.7d ago |
| 8 | 91 | cascade | 69.0 | 0.85 | 546 | 1,471 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.7d ago |
| 9 | 1 | Apex | 68.6 | 0.85 | 488 | 1,196 | rtx4090 | 0.551 | 5 | 55% | RELEASE 2.0d ago |
| 10 | 96 | Verathos | 68.4 | 1.0 | 22.52 | 302 | rtx4090 | 0.403 | 89 | 40% | RELEASE 5.0d ago |
| 11 | 26 | Perturb | 67.6 | 1.0 | 18.74 | 267 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.6d ago |
| 12 | 124 | Swarm | 66.7 | 0.85 | 285 | 2,481 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.1d ago |
| 13 | 38 | ChronoLLM | 66.6 | 0.85 | 117 | 1,597 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.8d ago |
| 14 | 108 | Prometheon | 65.4 | 0.85 | 186 | 204 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.1d ago |
| 15 | 107 | Minos | 65.4 | 1.0 | 155 | 43,621 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 16 | 85 | Vidaio | 64.3 | 0.85 | 136 | 425 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.4d ago |
| 17 | 81 | Reliquary | 64.2 | 0.85 | 132 | 300 | rtx4090 | 0.019 | 35 | 7% | SCORING_COMMIT 0.9d ago |
| 18 | 51 | lium.io | 60.4 | 0.85 | 50.33 | 1,724 | rtx4090 | 0.000 | 53 | 80% | SCORING_COMMIT 3.3d ago |
| 19 | 53 | engy | 60.2 | 0.85 | 38.67 | 12,885 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.5d ago |
| 20 | 60 | Bitsec.ai | 60.0 | 0.85 | 509 | 509 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 21 | 28 | gm | 59.4 | 0.85 | 32.74 | 1,510 | rtx4090 | 0.137 | 55 | 14% | RELEASE 3.1d ago |
| 22 | 61 | RedTeam | 57.2 | 0.85 | 15.48 | 328 | rtx4090 | 0.000 | 84 | 7% | RELEASE 1.3d ago |
| 23 | 41 | Almanac | 56.4 | 1.0 | 14.88 | 29.04 | cpu-small | 0.641 | 79 | 64% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,466 | 7,466 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.8d ago |
| 25 | 33 | ReadyAI | 54.0 | 0.85 | 6.50 | 11.77 | rtx4090 | 0.000 | 246 | 1% | SCORING_COMMIT 2.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.51 | a4000 | 1216.5052162033273 |
| 89 | InfiniteQuant | -1.05 | rtx4090 | 115.72248338128601 |
| 13 | Data Universe | -2.79 | rtx4090 | 7.636016195145387 |
| 18 | Zeus | -3.34 | rtx4090 | 1844.8621788667224 |
| 123 | MANTIS | -5.67 | rtx4090 | 118.09112610780282 |
| 75 | Hippius | -6.35 | rtx4090 | 12113.973569454884 |
| 34 | BitMind | -19.25 | a100-80 | 336.6022736071595 |
| 6 | Numinous | -0.93 | cpu-small | 182.24184124756485 |
| 50 | Synth | -1.42 | rtx4090 | 65.83951780000822 |
| 104 | Masx.ai | -1.56 | rtx4090 | 9.71860287942995 |
| 88 | Investing | -2.90 | rtx4090 | 666.2483323734458 |
| 8 | Vanta | -7.35 | rtx4090 | 3278.740804537058 |
| 43 | Graphite | -0.21 | cpu-small | 193.18812063306981 |
| 19 | blockmachine | -0.80 | rtx4090 | 566.654342323068 |
| 22 | Desearch | -1.09 | rtx4090 | 47.31005425431258 |
| 45 | AlphaRidge.ai | -5.15 | rtx4090 | 13.590811771371712 |
| 63 | Enigma | -8.13 | rtx4090 | 5598.401350408034 |
| 105 | Beam | -1.98 | rtx4090 | 83.18044121493256 |
| 84 | ansuz | -8.15 | rtx4090 | 0.0706889688653622 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.03 | 35.0 | 15.0 | 9.89 | 1.0 |
| 102 | 29.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.85 | 35.0 | 15.0 | 9.85 | 1.0 |
| 23 | 25.09 | 35.0 | 15.0 | 9.99 | 0.85 |
| 62 | 28.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 12.88 | 35.0 | 15.0 | 8.62 | 1.0 |
| 56 | 25.93 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.9 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.46 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.47 | 35.0 | 11.25 | 9.66 | 1.0 |
| 26 | 11.78 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.34 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.84 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.67 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.94 | 21.0 | 15.0 | 9.46 | 1.0 |
| 85 | 19.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 19.3 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 15.56 | 35.0 | 11.25 | 9.23 | 0.85 |
| 53 | 14.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.63 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.9 | 35.0 | 11.25 | 9.72 | 0.85 |
| 61 | 11.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.92 | 21.0 | 15.0 | 9.48 | 1.0 |
| 120 | 35.23 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 7.96 | 35.0 | 11.25 | 9.3 | 0.85 |
