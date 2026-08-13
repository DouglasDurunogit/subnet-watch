# RANKING - generated 2026-08-13T12:35:40Z, block 8835649

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
| 1 | 107 | Minos | 78.0 | 1.0 | 110 | 31,368 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 2.9d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.22 | 192 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 4.6d ago |
| 3 | 67 | Harnyx | 71.2 | 1.0 | 16.88 | 695 | cpu-small | 0.022 | 147 | 19% | SCORING_COMMIT 0.1d ago |
| 4 | 91 | cascade | 69.0 | 0.85 | 551 | 1,268 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 2.3d ago |
| 5 | 62 | Ridges | 69.0 | 0.85 | 542 | 1,961 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 1.6d ago |
| 6 | 56 | Gradients | 68.9 | 0.85 | 528 | 975 | rtx4090 | 0.652 | 7 | 65% | SCORING_COMMIT 0.9d ago |
| 7 | 41 | Almanac | 68.9 | 1.0 | 10.29 | 29.01 | cpu-small | 0.724 | 68 | 72% | SCORING_COMMIT 0.6d ago |
| 8 | 85 | Vidaio | 68.8 | 0.85 | 511 | 511 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 1.1d ago |
| 9 | 96 | Verathos | 68.6 | 1.0 | 23.40 | 240 | rtx4090 | 0.434 | 58 | 43% | RELEASE 0.9d ago |
| 10 | 100 | BASE | 68.1 | 0.85 | 422 | 1,751 | rtx4090 | 0.000 | 5 | 51% | RELEASE 1.1d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.46 | 36.69 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 6.9d ago |
| 12 | 21 | AdTAO | 67.6 | 1.0 | 7.57 | 33.97 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 2.0d ago |
| 13 | 124 | Swarm | 65.9 | 0.85 | 223 | 466 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 1.9d ago |
| 14 | 80 | OpenRoboto | 64.9 | 0.85 | 162 | 587 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 5.3d ago |
| 15 | 38 | ChronoLLM | 63.1 | 0.85 | 107 | 1,556 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 5.1d ago |
| 16 | 28 | gm | 60.1 | 0.85 | 39.34 | 2,940 | rtx4090 | 0.052 | 27 | 30% | RELEASE 0.9d ago |
| 17 | 51 | lium.io | 60.0 | 0.85 | 44.75 | 2,146 | rtx4090 | 0.000 | 46 | 77% | RELEASE 0.4d ago |
| 18 | 61 | RedTeam | 58.4 | 0.85 | 22.20 | 1,632 | rtx4090 | 0.000 | 58 | 35% | RELEASE 2.2d ago |
| 19 | 102 | ConnitoAI | 58.3 | 0.85 | 783 | 2,842 | rtx4090 | 0.251 | 6 | 46% | RELEASE 13d ago |
| 20 | 74 | Gittensor | 58.3 | 0.85 | 24.39 | 215 | rtx4090 | 0.630 | 13 | 63% | RELEASE 1.8d ago |
| 21 | 2 | DSperse | 55.3 | 0.85 | 8.39 | 79.63 | rtx4090 | 0.828 | 13 | 83% | RELEASE 2.7d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 6,919 | 6,919 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.9d ago |
| 23 | 15 | ORO | 54.3 | 1.0 | 11.76 | 12,336 | cpu-small | 0.000 | 76 | 93% | RELEASE 7d ago |
| 24 | 6 | Numinous | 54.1 | 1.0 | 9.82 | 519 | cpu-small | 0.000 | 19 | 29% | README_TASK_DIFF 15d ago |
| 25 | 97 | Albedo | 52.7 | 0.6 | 2,935 | 2,935 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.11 | a4000 | 966.5690489657734 |
| 104 | Masx.ai | -0.04 | rtx4090 | 11.880462017305328 |
| 75 | Hippius | -7.35 | rtx4090 | 11272.218126215168 |
| 114 | SOMA | -8.12 | rtx4090 | 682.319929032132 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 151.15609016479678 |
| 13 | Data Universe | -3.15 | rtx4090 | 5.742945612185034 |
| 88 | Investing | -5.20 | rtx4090 | 668.773971980345 |
| 8 | Vanta | -7.95 | rtx4090 | 3263.0750409902835 |
| 43 | Graphite | -0.23 | cpu-small | 39.69891511922813 |
| 19 | blockmachine | -2.15 | rtx4090 | 438.7440116199833 |
| 18 | Zeus | -3.33 | rtx4090 | 1721.141999842036 |
| 45 | AlphaRidge.ai | -5.05 | rtx4090 | 11.549732277319956 |
| 123 | MANTIS | -6.10 | rtx4090 | 80.38679939780054 |
| 63 | Enigma | -8.14 | rtx4090 | 5035.7071490798835 |
| 105 | Beam | -2.13 | rtx4090 | 84.55538094004501 |
| 84 | ansuz | -8.15 | rtx4090 | 468.3229545640874 |
| 34 | BitMind | -20.01 | a100-80 | 290.4542598188921 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn118, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.6 | 35.0 | 15.0 | 9.4 | 1.0 |
| 76 | 14.69 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 11.39 | 35.0 | 15.0 | 9.79 | 1.0 |
| 91 | 24.94 | 35.0 | 11.25 | 9.98 | 0.85 |
| 62 | 24.87 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.77 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.57 | 35.0 | 15.0 | 9.35 | 1.0 |
| 85 | 24.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.62 | 35.0 | 11.25 | 9.72 | 1.0 |
| 100 | 23.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 11.92 | 35.0 | 11.25 | 9.66 | 1.0 |
| 21 | 8.49 | 35.0 | 15.0 | 9.12 | 1.0 |
| 124 | 21.38 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 20.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.5 | 35.0 | 11.25 | 9.54 | 0.85 |
| 28 | 14.6 | 35.0 | 11.25 | 9.83 | 0.85 |
| 51 | 15.1 | 35.0 | 11.25 | 9.26 | 0.85 |
| 61 | 12.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 26.33 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.78 | 35.0 | 11.25 | 9.59 | 0.85 |
| 2 | 8.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.93 | 35.0 | 11.25 | 9.99 | 0.6 |
| 15 | 10.06 | 21.0 | 15.0 | 8.26 | 1.0 |
| 6 | 9.41 | 21.0 | 15.0 | 8.65 | 1.0 |
| 97 | 31.54 | 35.0 | 11.25 | 9.96 | 0.6 |
