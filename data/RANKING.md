# RANKING - generated 2026-08-18T13:54:58Z, block 8872045

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
| 1 | 76 | Phylax | 78.1 | 1.0 | 97.76 | 189 | cpu-small | 0.000 | 10 | 20% | SCORING_COMMIT 2.1d ago |
| 2 | 67 | Harnyx | 71.8 | 1.0 | 19.88 | 424 | cpu-small | 0.070 | 129 | 13% | SCORING_COMMIT 0.1d ago |
| 3 | 26 | Perturb | 70.7 | 1.0 | 39.22 | 72.03 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 4.9d ago |
| 4 | 1 | Apex | 70.4 | 0.85 | 828 | 1,079 | rtx4090 | 0.526 | 4 | 53% | RELEASE 5.0d ago |
| 5 | 56 | Gradients | 69.1 | 0.85 | 562 | 922 | rtx4090 | 0.698 | 6 | 70% | SCORING_COMMIT 0.6d ago |
| 6 | 41 | Almanac | 69.1 | 1.0 | 10.70 | 49.08 | cpu-small | 0.670 | 74 | 67% | SCORING_COMMIT 5.6d ago |
| 7 | 91 | cascade | 68.8 | 0.85 | 519 | 2,100 | rtx4090 | 0.000 | 5 | 51% | README_TASK_DIFF 0.4d ago |
| 8 | 62 | Ridges | 68.3 | 0.85 | 451 | 2,093 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.6d ago |
| 9 | 15 | ORO | 67.7 | 1.0 | 10.10 | 12,147 | cpu-small | 0.000 | 67 | 95% | RELEASE 0.5d ago |
| 10 | 21 | AdTAO | 67.7 | 1.0 | 7.75 | 34.70 | cpu-small | 0.451 | 88 | 45% | RELEASE 0.7d ago |
| 11 | 38 | ChronoLLM | 67.5 | 0.85 | 147 | 3,110 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.9d ago |
| 12 | 96 | Verathos | 67.4 | 1.0 | 17.54 | 385 | rtx4090 | 0.404 | 75 | 40% | RELEASE 3.7d ago |
| 13 | 11 | TrajectoryRL | 67.0 | 0.85 | 4,086 | 4,086 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 16d ago |
| 14 | 124 | Swarm | 66.1 | 0.85 | 241 | 722 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 6.9d ago |
| 15 | 85 | Vidaio | 64.1 | 0.85 | 125 | 1,310 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 0.3d ago |
| 16 | 107 | Minos | 64.1 | 1.0 | 112 | 33,302 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 8d ago |
| 17 | 81 | Reliquary | 63.2 | 0.85 | 96.35 | 451 | rtx4090 | 0.000 | 36 | 11% | SCORING_COMMIT 0.0d ago |
| 18 | 55 | NIOME | 61.5 | 0.85 | 58.28 | 491 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 3.7d ago |
| 19 | 28 | gm | 60.5 | 0.85 | 44.22 | 2,547 | rtx4090 | 0.051 | 40 | 26% | RELEASE 6.0d ago |
| 20 | 60 | Bitsec.ai | 58.9 | 0.85 | 363 | 363 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 11d ago |
| 21 | 102 | ConnitoAI | 58.3 | 0.85 | 794 | 1,596 | rtx4090 | 0.250 | 6 | 32% | RELEASE 18d ago |
| 22 | 74 | Gittensor | 57.6 | 0.85 | 19.62 | 200 | rtx4090 | 0.638 | 14 | 64% | RELEASE 6.8d ago |
| 23 | 51 | lium.io | 56.1 | 0.85 | 17.67 | 1,031 | rtx4090 | 0.000 | 55 | 82% | SCORING_COMMIT 0.2d ago |
| 24 | 68 | NOVA | 55.0 | 0.6 | 7,722 | 7,722 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 2.0d ago |
| 25 | 120 | Affine | 54.5 | 0.6 | 6,348 | 6,348 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 6.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.94 | cpu-small | 284.3944172151891 |
| 54 | Yanez | -3.64 | a4000 | 947.0954909270475 |
| 123 | MANTIS | -6.08 | rtx4090 | 81.05381003502501 |
| 75 | Hippius | -6.28 | rtx4090 | 10891.52168363698 |
| 114 | SOMA | -8.12 | rtx4090 | 4124.171857601245 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 121.5048525499745 |
| 101 | Tag101 | -0.14 | cpu-small | 1.9760664718428007 |
| 104 | Masx.ai | -1.19 | rtx4090 | 8.34079487756172 |
| 13 | Data Universe | -3.99 | rtx4090 | 4.759305696225502 |
| 88 | Investing | -5.19 | rtx4090 | 649.8401969162678 |
| 8 | Vanta | -7.97 | rtx4090 | 2903.3924027300773 |
| 43 | Graphite | -0.83 | cpu-small | 22.591962034142206 |
| 19 | blockmachine | -2.03 | rtx4090 | 586.371977208515 |
| 18 | Zeus | -4.11 | rtx4090 | 1641.051954854369 |
| 22 | Desearch | -4.73 | rtx4090 | 67.1444861248875 |
| 45 | AlphaRidge.ai | -4.94 | rtx4090 | 11.798051003847215 |
| 63 | Enigma | -8.15 | rtx4090 | 4641.129863239842 |
| 105 | Beam | -2.90 | rtx4090 | 69.85422670561672 |
| 84 | ansuz | -8.16 | rtx4090 | 0.05914571485810613 |
| 34 | BitMind | -20.42 | a100-80 | 19.171899897327958 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 18.14 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.0 | 35.0 | 15.0 | 9.8 | 1.0 |
| 26 | 14.59 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 25.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.72 | 35.0 | 15.0 | 9.4 | 1.0 |
| 91 | 24.7 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 24.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.51 | 35.0 | 15.0 | 8.16 | 1.0 |
| 21 | 8.57 | 35.0 | 15.0 | 9.18 | 1.0 |
| 38 | 19.73 | 35.0 | 15.0 | 9.68 | 0.85 |
| 96 | 11.53 | 35.0 | 11.25 | 9.64 | 1.0 |
| 11 | 32.85 | 21.0 | 15.0 | 10.0 | 0.85 |
| 124 | 21.68 | 35.0 | 11.25 | 9.87 | 0.85 |
| 85 | 19.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 107 | 18.69 | 21.0 | 15.0 | 9.44 | 1.0 |
| 81 | 18.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.06 | 35.0 | 11.25 | 9.86 | 0.85 |
| 60 | 23.3 | 21.0 | 15.0 | 10.0 | 0.85 |
| 102 | 26.38 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 11.95 | 35.0 | 11.25 | 9.51 | 0.85 |
| 51 | 11.56 | 35.0 | 11.25 | 8.19 | 0.85 |
| 68 | 35.36 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.59 | 35.0 | 11.25 | 9.97 | 0.6 |
