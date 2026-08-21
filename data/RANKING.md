# RANKING - generated 2026-08-21T05:03:33Z, block 8890987

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 76.77 | 129 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.8d ago |
| 2 | 23 | Trishool | 72.2 | 0.85 | 550 | 550 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 1.0d ago |
| 3 | 67 | Harnyx | 70.7 | 1.0 | 15.72 | 887 | cpu-small | 0.057 | 142 | 23% | SCORING_COMMIT 0.8d ago |
| 4 | 15 | ORO | 70.4 | 1.0 | 20.37 | 19,634 | cpu-small | 0.000 | 79 | 93% | SCORING_COMMIT 2.4d ago |
| 5 | 56 | Gradients | 69.8 | 0.85 | 689 | 1,056 | rtx4090 | 0.724 | 5 | 72% | SCORING_COMMIT 3.2d ago |
| 6 | 91 | cascade | 69.4 | 0.85 | 622 | 2,514 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 0.2d ago |
| 7 | 1 | Apex | 68.2 | 0.85 | 432 | 1,201 | rtx4090 | 0.540 | 5 | 54% | RELEASE 1.3d ago |
| 8 | 38 | ChronoLLM | 67.7 | 0.85 | 155 | 3,295 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.3d ago |
| 9 | 96 | Verathos | 67.5 | 1.0 | 18.30 | 321 | rtx4090 | 0.403 | 92 | 40% | RELEASE 2.5d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.65 | 254 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.1d ago |
| 11 | 107 | Minos | 65.3 | 1.0 | 150 | 42,473 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 11d ago |
| 12 | 85 | Vidaio | 65.0 | 0.85 | 166 | 1,503 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.9d ago |
| 13 | 108 | Prometheon | 64.0 | 0.85 | 125 | 184 | rtx4090 | 0.660 | 7 | 66% | SCORING_COMMIT 1.1d ago |
| 14 | 55 | NIOME | 61.9 | 0.85 | 65.03 | 544 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 6.4d ago |
| 15 | 51 | lium.io | 61.7 | 0.85 | 69.56 | 1,293 | rtx4090 | 0.000 | 44 | 83% | SCORING_COMMIT 0.9d ago |
| 16 | 60 | Bitsec.ai | 61.4 | 0.85 | 771 | 1,080 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 17 | 81 | Reliquary | 61.0 | 0.85 | 50.24 | 196 | rtx4090 | 0.002 | 53 | 5% | SCORING_COMMIT 1.3d ago |
| 18 | 28 | gm | 60.3 | 0.85 | 42.39 | 1,670 | rtx4090 | 0.128 | 52 | 15% | RELEASE 0.6d ago |
| 19 | 53 | engy | 60.1 | 0.85 | 37.73 | 249 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.0d ago |
| 20 | 102 | ConnitoAI | 57.6 | 0.85 | 638 | 1,557 | rtx4090 | 0.250 | 7 | 26% | RELEASE 20d ago |
| 21 | 68 | NOVA | 55.2 | 0.6 | 8,676 | 8,676 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.6d ago |
| 22 | 120 | Affine | 54.8 | 0.6 | 7,338 | 7,338 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.4d ago |
| 23 | 124 | Swarm | 54.6 | 0.85 | 269 | 784 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 10d ago |
| 24 | 41 | Almanac | 54.6 | 1.0 | 9.76 | 24.12 | cpu-small | 0.736 | 75 | 74% | SCORING_COMMIT 8d ago |
| 25 | 80 | OpenRoboto | 53.8 | 0.85 | 206 | 741 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 13d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.39 | cpu-small | 4.929227154907445 |
| 54 | Yanez | -3.11 | a4000 | 1118.954774806044 |
| 13 | Data Universe | -3.09 | rtx4090 | 6.1498063193439725 |
| 18 | Zeus | -5.06 | rtx4090 | 1153.5048367609877 |
| 123 | MANTIS | -5.61 | rtx4090 | 101.22860941021595 |
| 75 | Hippius | -6.13 | rtx4090 | 11745.383965251001 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 128.73292290798227 |
| 34 | BitMind | -19.55 | a100-80 | 3152.204494384513 |
| 6 | Numinous | -0.93 | cpu-small | 367.6950394161839 |
| 104 | Masx.ai | -0.53 | rtx4090 | 9.095054787064159 |
| 88 | Investing | -4.01 | rtx4090 | 926.4990337749176 |
| 8 | Vanta | -7.39 | rtx4090 | 3257.533081324182 |
| 43 | Graphite | -0.78 | cpu-small | 26.235349117352666 |
| 19 | blockmachine | -0.88 | rtx4090 | 1542.2454169886287 |
| 45 | AlphaRidge.ai | -4.74 | rtx4090 | 11.971068250239703 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08080813205865883 |
| 105 | Beam | -2.21 | rtx4090 | 77.71299035410547 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06634949817197842 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.2 | 35.0 | 15.0 | 9.91 | 1.0 |
| 23 | 24.93 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 11.12 | 35.0 | 15.0 | 9.62 | 1.0 |
| 15 | 12.1 | 35.0 | 15.0 | 8.27 | 1.0 |
| 56 | 25.82 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.42 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 23.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.96 | 35.0 | 15.0 | 9.65 | 0.85 |
| 96 | 11.69 | 35.0 | 11.25 | 9.6 | 1.0 |
| 26 | 11.56 | 35.0 | 11.25 | 9.59 | 1.0 |
| 107 | 19.83 | 21.0 | 15.0 | 9.52 | 1.0 |
| 85 | 20.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 19.1 | 35.0 | 11.25 | 9.97 | 0.85 |
| 55 | 16.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.81 | 35.0 | 11.25 | 9.48 | 0.85 |
| 60 | 26.26 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 15.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.89 | 35.0 | 11.25 | 9.83 | 0.85 |
| 53 | 14.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 25.51 | 21.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.82 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.16 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.12 | 21.0 | 11.25 | 9.87 | 0.85 |
| 41 | 9.38 | 21.0 | 15.0 | 9.26 | 1.0 |
| 80 | 21.06 | 21.0 | 11.25 | 10.0 | 0.85 |
