# RANKING - generated 2026-08-23T14:35:21Z, block 8908246

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
| 1 | 76 | Phylax | 76.9 | 1.0 | 73.57 | 82.36 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 4.2d ago |
| 2 | 67 | Harnyx | 72.7 | 1.0 | 24.89 | 798 | cpu-small | 0.033 | 124 | 20% | SCORING_COMMIT 2.2d ago |
| 3 | 23 | Trishool | 72.3 | 0.85 | 570 | 570 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.4d ago |
| 4 | 15 | ORO | 71.0 | 1.0 | 23.62 | 41.69 | cpu-small | 0.000 | 78 | 93% | SCORING_COMMIT 1.6d ago |
| 5 | 56 | Gradients | 70.0 | 0.85 | 743 | 1,111 | rtx4090 | 0.730 | 5 | 73% | SCORING_COMMIT 5.6d ago |
| 6 | 91 | cascade | 68.9 | 0.85 | 540 | 1,453 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.6d ago |
| 7 | 1 | Apex | 68.6 | 0.85 | 491 | 1,203 | rtx4090 | 0.548 | 5 | 55% | RELEASE 2.0d ago |
| 8 | 96 | Verathos | 68.2 | 1.0 | 21.45 | 296 | rtx4090 | 0.402 | 90 | 40% | RELEASE 4.9d ago |
| 9 | 26 | Perturb | 67.6 | 1.0 | 18.68 | 266 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.5d ago |
| 10 | 124 | Swarm | 66.7 | 0.85 | 284 | 2,470 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.1d ago |
| 11 | 38 | ChronoLLM | 66.6 | 0.85 | 117 | 1,597 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.7d ago |
| 12 | 108 | Prometheon | 65.4 | 0.85 | 186 | 204 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.0d ago |
| 13 | 107 | Minos | 65.4 | 1.0 | 154 | 43,991 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 14 | 85 | Vidaio | 64.3 | 0.85 | 136 | 425 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.3d ago |
| 15 | 81 | Reliquary | 64.3 | 0.85 | 135 | 324 | rtx4090 | 0.046 | 37 | 7% | SCORING_COMMIT 0.9d ago |
| 16 | 51 | lium.io | 61.3 | 0.85 | 63.77 | 4,453 | rtx4090 | 0.000 | 53 | 71% | SCORING_COMMIT 3.3d ago |
| 17 | 102 | ConnitoAI | 61.1 | 0.85 | 51.99 | 2,915 | rtx4090 | 0.250 | 6 | 42% | RELEASE 1.9d ago |
| 18 | 53 | engy | 60.2 | 0.85 | 38.47 | 12,829 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.4d ago |
| 19 | 60 | Bitsec.ai | 60.0 | 0.85 | 508 | 508 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 20 | 28 | gm | 59.2 | 0.85 | 31.05 | 1,610 | rtx4090 | 0.215 | 55 | 22% | RELEASE 3.0d ago |
| 21 | 61 | RedTeam | 57.0 | 0.85 | 14.44 | 323 | rtx4090 | 0.000 | 84 | 7% | RELEASE 1.3d ago |
| 22 | 41 | Almanac | 56.5 | 1.0 | 15.31 | 29.54 | cpu-small | 0.633 | 79 | 63% | SCORING_COMMIT 11d ago |
| 23 | 120 | Affine | 54.9 | 0.6 | 7,491 | 7,491 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.7d ago |
| 24 | 80 | OpenRoboto | 54.0 | 0.85 | 215 | 772 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 15d ago |
| 25 | 33 | ReadyAI | 53.9 | 0.85 | 6.57 | 11.88 | rtx4090 | 0.000 | 245 | 1% | SCORING_COMMIT 2.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.21 | a4000 | 1203.3226823750176 |
| 89 | InfiniteQuant | -0.74 | rtx4090 | 116.1363683282476 |
| 13 | Data Universe | -2.85 | rtx4090 | 7.512177848930137 |
| 18 | Zeus | -3.33 | rtx4090 | 1428.2040589710882 |
| 123 | MANTIS | -5.62 | rtx4090 | 115.87296889169086 |
| 75 | Hippius | -6.35 | rtx4090 | 12105.467343226757 |
| 34 | BitMind | -18.43 | a100-80 | 336.29048345819103 |
| 6 | Numinous | -0.93 | cpu-small | 182.75592176181596 |
| 50 | Synth | -1.43 | rtx4090 | 66.81898534527235 |
| 88 | Investing | -2.90 | rtx4090 | 666.1492495691222 |
| 104 | Masx.ai | -3.43 | rtx4090 | 13.449048676392882 |
| 8 | Vanta | -7.35 | rtx4090 | 1122.5893791053816 |
| 43 | Graphite | -0.27 | cpu-small | 185.8314779040503 |
| 19 | blockmachine | -0.80 | rtx4090 | 566.1372122307711 |
| 22 | Desearch | -0.89 | rtx4090 | 41.60085736994122 |
| 45 | AlphaRidge.ai | -4.35 | rtx4090 | 13.15908863609153 |
| 63 | Enigma | -8.13 | rtx4090 | 5593.387538846146 |
| 105 | Beam | -2.03 | rtx4090 | 82.59995666950131 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07063125836267929 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.03 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 12.85 | 35.0 | 15.0 | 9.86 | 1.0 |
| 23 | 25.07 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 12.65 | 35.0 | 15.0 | 8.33 | 1.0 |
| 56 | 26.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.86 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.29 | 35.0 | 11.25 | 9.64 | 1.0 |
| 26 | 11.77 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.32 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.84 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.67 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.91 | 21.0 | 15.0 | 9.5 | 1.0 |
| 85 | 19.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 19.4 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.47 | 35.0 | 11.25 | 9.39 | 0.85 |
| 102 | 15.68 | 35.0 | 11.25 | 9.94 | 0.85 |
| 53 | 14.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.62 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.7 | 35.0 | 11.25 | 9.69 | 0.85 |
| 61 | 10.81 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 11.03 | 21.0 | 15.0 | 9.49 | 1.0 |
| 120 | 35.24 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 21.22 | 21.0 | 11.25 | 10.0 | 0.85 |
| 33 | 8.0 | 35.0 | 11.25 | 9.22 | 0.85 |
