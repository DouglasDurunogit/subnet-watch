# RANKING - generated 2026-08-23T09:51:47Z, block 8906828

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
| 1 | 76 | Phylax | 76.8 | 1.0 | 70.51 | 79.56 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 4.0d ago |
| 2 | 102 | ConnitoAI | 72.8 | 0.85 | 1,729 | 1,729 | rtx4090 | 0.250 | 4 | 25% | RELEASE 1.7d ago |
| 3 | 67 | Harnyx | 72.6 | 1.0 | 24.05 | 772 | cpu-small | 0.033 | 124 | 20% | SCORING_COMMIT 2.0d ago |
| 4 | 23 | Trishool | 72.2 | 0.85 | 559 | 559 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.2d ago |
| 5 | 15 | ORO | 71.1 | 1.0 | 22.18 | 39.19 | cpu-small | 0.000 | 78 | 93% | SCORING_COMMIT 1.4d ago |
| 6 | 56 | Gradients | 69.9 | 0.85 | 718 | 1,070 | rtx4090 | 0.730 | 5 | 73% | SCORING_COMMIT 5.4d ago |
| 7 | 91 | cascade | 69.8 | 0.85 | 693 | 2,798 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.4d ago |
| 8 | 1 | Apex | 68.6 | 0.85 | 483 | 1,185 | rtx4090 | 0.538 | 5 | 54% | RELEASE 1.8d ago |
| 9 | 96 | Verathos | 68.0 | 1.0 | 20.45 | 271 | rtx4090 | 0.402 | 91 | 40% | RELEASE 4.7d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.85 | 256 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.3d ago |
| 11 | 38 | ChronoLLM | 66.5 | 0.85 | 113 | 1,547 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.5d ago |
| 12 | 107 | Minos | 65.1 | 1.0 | 146 | 42,167 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 13 | 85 | Vidaio | 64.4 | 0.85 | 140 | 410 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.1d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 119 | 129 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.8d ago |
| 15 | 81 | Reliquary | 63.4 | 0.85 | 104 | 235 | rtx4090 | 0.084 | 38 | 8% | SCORING_COMMIT 0.7d ago |
| 16 | 51 | lium.io | 61.5 | 0.85 | 66.31 | 4,362 | rtx4090 | 0.000 | 52 | 71% | SCORING_COMMIT 3.1d ago |
| 17 | 60 | Bitsec.ai | 59.9 | 0.85 | 490 | 490 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 18 | 53 | engy | 59.9 | 0.85 | 35.12 | 11,908 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.2d ago |
| 19 | 28 | gm | 58.2 | 0.85 | 22.66 | 1,397 | rtx4090 | 0.194 | 53 | 19% | RELEASE 2.8d ago |
| 20 | 61 | RedTeam | 57.0 | 0.85 | 14.30 | 309 | rtx4090 | 0.000 | 85 | 7% | RELEASE 1.1d ago |
| 21 | 41 | Almanac | 56.5 | 1.0 | 15.03 | 28.85 | cpu-small | 0.626 | 79 | 63% | SCORING_COMMIT 10d ago |
| 22 | 68 | NOVA | 55.3 | 0.6 | 8,709 | 8,709 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.8d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,108 | 7,108 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.6d ago |
| 24 | 124 | Swarm | 54.6 | 0.85 | 271 | 2,364 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 12d ago |
| 25 | 33 | ReadyAI | 53.9 | 0.85 | 6.07 | 10.27 | rtx4090 | 0.000 | 244 | 1% | SCORING_COMMIT 2.7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.28 | cpu-small | 5.917506648287162 |
| 54 | Yanez | -3.19 | a4000 | 1180.0825616681325 |
| 89 | InfiniteQuant | -0.25 | rtx4090 | 112.98602372702686 |
| 13 | Data Universe | -3.29 | rtx4090 | 7.300271473960122 |
| 18 | Zeus | -3.56 | rtx4090 | 1361.2293218455359 |
| 123 | MANTIS | -5.72 | rtx4090 | 110.9482569562486 |
| 75 | Hippius | -6.41 | rtx4090 | 11710.518796150829 |
| 34 | BitMind | -18.78 | a100-80 | 323.7911390969718 |
| 6 | Numinous | -0.93 | cpu-small | 175.11613980658566 |
| 104 | Masx.ai | -1.42 | rtx4090 | 7.813378644155403 |
| 50 | Synth | -1.89 | rtx4090 | 64.27970857313002 |
| 88 | Investing | -3.12 | rtx4090 | 639.1673028985766 |
| 8 | Vanta | -7.38 | rtx4090 | 1081.9095596580078 |
| 43 | Graphite | -0.29 | cpu-small | 178.92381334254412 |
| 32 | ItsAI | -0.00 | rtx4090 | 11.282264080927503 |
| 22 | Desearch | -0.89 | rtx4090 | 37.74493695340876 |
| 19 | blockmachine | -1.08 | rtx4090 | 545.3389092057754 |
| 45 | AlphaRidge.ai | -5.46 | rtx4090 | 12.734612909438534 |
| 63 | Enigma | -8.14 | rtx4090 | 5385.737068673675 |
| 105 | Beam | -2.23 | rtx4090 | 79.93770526440643 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.87 | 35.0 | 15.0 | 9.89 | 1.0 |
| 102 | 29.45 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.72 | 35.0 | 15.0 | 9.84 | 1.0 |
| 23 | 24.99 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 12.42 | 35.0 | 15.0 | 8.7 | 1.0 |
| 56 | 25.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.84 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.11 | 35.0 | 11.25 | 9.64 | 1.0 |
| 26 | 11.6 | 35.0 | 11.25 | 9.58 | 1.0 |
| 38 | 18.72 | 35.0 | 15.0 | 9.51 | 0.85 |
| 107 | 19.71 | 21.0 | 15.0 | 9.39 | 1.0 |
| 85 | 19.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.91 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.63 | 35.0 | 11.25 | 9.44 | 0.85 |
| 60 | 24.48 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 14.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 12.5 | 35.0 | 11.25 | 9.67 | 0.85 |
| 61 | 10.78 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.96 | 21.0 | 15.0 | 9.5 | 1.0 |
| 68 | 35.83 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.03 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.15 | 21.0 | 11.25 | 9.86 | 0.85 |
| 33 | 7.73 | 35.0 | 11.25 | 9.38 | 0.85 |
