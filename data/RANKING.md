# RANKING - generated 2026-08-18T13:04:58Z, block 8871795

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
| 1 | 76 | Phylax | 78.1 | 1.0 | 97.94 | 189 | cpu-small | 0.000 | 10 | 20% | SCORING_COMMIT 2.0d ago |
| 2 | 67 | Harnyx | 71.8 | 1.0 | 19.93 | 425 | cpu-small | 0.074 | 128 | 13% | SCORING_COMMIT 0.1d ago |
| 3 | 26 | Perturb | 70.7 | 1.0 | 39.34 | 72.23 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 4.9d ago |
| 4 | 1 | Apex | 70.4 | 0.85 | 832 | 1,085 | rtx4090 | 0.524 | 4 | 52% | RELEASE 5.0d ago |
| 5 | 41 | Almanac | 69.1 | 1.0 | 10.73 | 49.22 | cpu-small | 0.670 | 74 | 67% | SCORING_COMMIT 5.6d ago |
| 6 | 91 | cascade | 68.8 | 0.85 | 523 | 2,115 | rtx4090 | 0.000 | 5 | 51% | README_TASK_DIFF 0.3d ago |
| 7 | 62 | Ridges | 68.4 | 0.85 | 453 | 2,100 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.6d ago |
| 8 | 56 | Gradients | 68.0 | 0.85 | 406 | 630 | rtx4090 | 0.740 | 8 | 74% | SCORING_COMMIT 0.5d ago |
| 9 | 96 | Verathos | 67.9 | 1.0 | 19.80 | 396 | rtx4090 | 0.405 | 65 | 41% | RELEASE 3.7d ago |
| 10 | 21 | AdTAO | 67.8 | 1.0 | 7.81 | 34.96 | cpu-small | 0.451 | 88 | 45% | RELEASE 0.7d ago |
| 11 | 15 | ORO | 67.6 | 1.0 | 10.08 | 12,238 | cpu-small | 0.000 | 67 | 95% | RELEASE 0.4d ago |
| 12 | 38 | ChronoLLM | 67.5 | 0.85 | 148 | 3,147 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.9d ago |
| 13 | 11 | TrajectoryRL | 67.0 | 0.85 | 4,110 | 4,110 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 16d ago |
| 14 | 124 | Swarm | 66.1 | 0.85 | 240 | 719 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 6.9d ago |
| 15 | 107 | Minos | 64.3 | 1.0 | 118 | 33,618 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 8d ago |
| 16 | 85 | Vidaio | 63.8 | 0.85 | 117 | 1,316 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 0.2d ago |
| 17 | 28 | gm | 62.8 | 0.85 | 88.48 | 2,354 | rtx4090 | 0.130 | 41 | 25% | RELEASE 6.0d ago |
| 18 | 55 | NIOME | 61.5 | 0.85 | 57.78 | 493 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 3.7d ago |
| 19 | 102 | ConnitoAI | 59.6 | 0.85 | 1,173 | 1,307 | rtx4090 | 0.250 | 5 | 26% | RELEASE 18d ago |
| 20 | 60 | Bitsec.ai | 58.9 | 0.85 | 366 | 366 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 11d ago |
| 21 | 74 | Gittensor | 57.6 | 0.85 | 19.63 | 200 | rtx4090 | 0.638 | 14 | 64% | RELEASE 6.8d ago |
| 22 | 51 | lium.io | 57.3 | 0.85 | 22.99 | 1,155 | rtx4090 | 0.000 | 55 | 80% | SCORING_COMMIT 0.2d ago |
| 23 | 68 | NOVA | 55.0 | 0.6 | 7,743 | 7,743 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 2.0d ago |
| 24 | 120 | Affine | 54.5 | 0.6 | 6,367 | 6,367 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 6.0d ago |
| 25 | 80 | OpenRoboto | 53.0 | 0.85 | 163 | 592 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 10d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.94 | cpu-small | 284.14123122899247 |
| 54 | Yanez | -3.66 | a4000 | 950.7381706378031 |
| 123 | MANTIS | -6.08 | rtx4090 | 81.29297858850752 |
| 75 | Hippius | -6.27 | rtx4090 | 10989.495652527847 |
| 114 | SOMA | -8.12 | rtx4090 | 4050.029763533451 |
| 89 | InfiniteQuant | -8.16 | rtx4090 | 120.91728612192665 |
| 101 | Tag101 | -0.08 | cpu-small | 2.0210370872632235 |
| 104 | Masx.ai | -1.21 | rtx4090 | 9.568494093956653 |
| 13 | Data Universe | -4.04 | rtx4090 | 4.7676611884032045 |
| 88 | Investing | -5.19 | rtx4090 | 650.351017187597 |
| 8 | Vanta | -7.97 | rtx4090 | 2903.477568233492 |
| 43 | Graphite | -0.83 | cpu-small | 23.55822682994137 |
| 19 | blockmachine | -1.87 | rtx4090 | 658.2134923936057 |
| 18 | Zeus | -4.09 | rtx4090 | 1648.349106050483 |
| 45 | AlphaRidge.ai | -4.64 | rtx4090 | 10.472427809661982 |
| 22 | Desearch | -5.60 | rtx4090 | 70.42566650928858 |
| 63 | Enigma | -8.15 | rtx4090 | 4653.161757460398 |
| 105 | Beam | -2.81 | rtx4090 | 71.29865036809396 |
| 84 | ansuz | -8.16 | rtx4090 | 0.05930328971131028 |
| 34 | BitMind | -20.08 | a100-80 | 18.90908608303862 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 18.15 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.01 | 35.0 | 15.0 | 9.74 | 1.0 |
| 26 | 14.6 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.73 | 35.0 | 15.0 | 9.4 | 1.0 |
| 91 | 24.73 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 24.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 23.73 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 11.99 | 35.0 | 11.25 | 9.68 | 1.0 |
| 21 | 8.6 | 35.0 | 15.0 | 9.18 | 1.0 |
| 15 | 9.5 | 35.0 | 15.0 | 8.11 | 1.0 |
| 38 | 19.77 | 35.0 | 15.0 | 9.68 | 0.85 |
| 11 | 32.87 | 21.0 | 15.0 | 10.0 | 0.85 |
| 124 | 21.66 | 35.0 | 11.25 | 9.87 | 0.85 |
| 107 | 18.87 | 21.0 | 15.0 | 9.46 | 1.0 |
| 85 | 18.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 17.75 | 35.0 | 11.25 | 9.93 | 0.85 |
| 55 | 16.09 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.92 | 21.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.33 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 11.96 | 35.0 | 11.25 | 9.51 | 0.85 |
| 51 | 12.55 | 35.0 | 11.25 | 8.61 | 0.85 |
| 68 | 35.37 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.6 | 35.0 | 11.25 | 9.97 | 0.6 |
| 80 | 20.15 | 21.0 | 11.25 | 10.0 | 0.85 |
