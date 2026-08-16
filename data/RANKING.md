# RANKING - generated 2026-08-16T09:51:06Z, block 8856425

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
| 1 | 107 | Minos | 78.2 | 1.0 | 115 | 32,270 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.8d ago |
| 2 | 76 | Phylax | 73.6 | 1.0 | 30.62 | 191 | cpu-small | 0.000 | 10 | 27% | SCORING_COMMIT 0.1d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.56 | 416 | cpu-small | 0.032 | 133 | 11% | SCORING_COMMIT 0.2d ago |
| 4 | 96 | Verathos | 70.9 | 1.0 | 41.20 | 228 | rtx4090 | 0.411 | 55 | 41% | RELEASE 1.6d ago |
| 5 | 26 | Perturb | 70.8 | 1.0 | 40.49 | 74.29 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.8d ago |
| 6 | 1 | Apex | 70.2 | 0.85 | 782 | 1,076 | rtx4090 | 0.539 | 4 | 54% | RELEASE 2.8d ago |
| 7 | 41 | Almanac | 69.9 | 1.0 | 12.88 | 53.65 | cpu-small | 0.651 | 74 | 65% | SCORING_COMMIT 3.5d ago |
| 8 | 15 | ORO | 69.1 | 1.0 | 12.74 | 12,878 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 2.5d ago |
| 9 | 56 | Gradients | 68.7 | 0.85 | 504 | 956 | rtx4090 | 0.675 | 7 | 68% | SCORING_COMMIT 3.8d ago |
| 10 | 62 | Ridges | 68.5 | 0.85 | 473 | 2,193 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.5d ago |
| 11 | 91 | cascade | 68.2 | 0.85 | 439 | 2,258 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.4d ago |
| 12 | 85 | Vidaio | 67.8 | 0.85 | 383 | 649 | rtx4090 | 0.000 | 10 | 21% | SCORING_COMMIT 4.0d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.60 | 34.11 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.9d ago |
| 14 | 38 | ChronoLLM | 66.0 | 0.85 | 96.97 | 1,326 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.7d ago |
| 15 | 124 | Swarm | 65.9 | 0.85 | 223 | 715 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.8d ago |
| 16 | 2 | DSperse | 62.9 | 0.85 | 87.42 | 149 | rtx4090 | 0.822 | 5 | 82% | RELEASE 5.6d ago |
| 17 | 55 | NIOME | 61.5 | 0.85 | 57.92 | 472 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.6d ago |
| 18 | 28 | gm | 60.2 | 0.85 | 41.20 | 2,405 | rtx4090 | 0.177 | 40 | 28% | RELEASE 3.8d ago |
| 19 | 60 | Bitsec.ai | 59.4 | 0.85 | 418 | 418 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 20 | 102 | ConnitoAI | 58.6 | 0.85 | 869 | 1,738 | rtx4090 | 0.251 | 6 | 33% | RELEASE 15d ago |
| 21 | 74 | Gittensor | 58.1 | 0.85 | 25.99 | 207 | rtx4090 | 0.630 | 14 | 63% | RELEASE 4.6d ago |
| 22 | 61 | RedTeam | 57.6 | 0.85 | 17.35 | 439 | rtx4090 | 0.000 | 81 | 10% | RELEASE 5.1d ago |
| 23 | 120 | Affine | 56.8 | 0.6 | 16,493 | 16,493 | rtx4090 | 0.500 | 2 | 50% | SCORING_COMMIT 3.8d ago |
| 24 | 51 | lium.io | 56.2 | 0.85 | 18.28 | 1,341 | rtx4090 | 0.000 | 54 | 82% | SCORING_COMMIT 2.0d ago |
| 25 | 80 | OpenRoboto | 53.1 | 0.85 | 167 | 607 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 243.14643443758578 |
| 54 | Yanez | -3.65 | a4000 | 946.5611287050633 |
| 104 | Masx.ai | -0.49 | rtx4090 | 9.46360948419695 |
| 75 | Hippius | -7.31 | rtx4090 | 10769.22379012672 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 128.5476276982189 |
| 13 | Data Universe | -3.55 | rtx4090 | 5.7642204262515495 |
| 88 | Investing | -5.37 | rtx4090 | 1148.481022874241 |
| 8 | Vanta | -7.71 | rtx4090 | 3011.260103289141 |
| 114 | SOMA | -8.13 | rtx4090 | 608.4695633813225 |
| 43 | Graphite | -0.75 | cpu-small | 16.010699822676948 |
| 32 | ItsAI | -0.49 | rtx4090 | 10.459006944437668 |
| 22 | Desearch | -2.02 | rtx4090 | 50.5604145902321 |
| 45 | AlphaRidge.ai | -3.11 | rtx4090 | 22.840027104366936 |
| 18 | Zeus | -3.75 | rtx4090 | 1599.727965445663 |
| 123 | MANTIS | -6.04 | rtx4090 | 75.26016441691073 |
| 19 | blockmachine | -6.23 | rtx4090 | 1081.4571286061484 |
| 63 | Enigma | -8.14 | rtx4090 | 5004.429272611631 |
| 105 | Beam | -2.97 | rtx4090 | 110.76545253285384 |
| 84 | ansuz | -8.16 | rtx4090 | 438.298361031796 |
| 34 | BitMind | -20.13 | a100-80 | 19.240919349803356 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.77 | 35.0 | 15.0 | 9.44 | 1.0 |
| 76 | 13.64 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.64 | 35.0 | 15.0 | 9.82 | 1.0 |
| 96 | 14.78 | 35.0 | 11.25 | 9.84 | 1.0 |
| 26 | 14.72 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.39 | 35.0 | 15.0 | 9.49 | 1.0 |
| 15 | 10.35 | 35.0 | 15.0 | 8.78 | 1.0 |
| 56 | 24.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.34 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.05 | 35.0 | 11.25 | 9.99 | 0.85 |
| 85 | 23.51 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.5 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.11 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.37 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 17.7 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.78 | 35.0 | 11.25 | 9.84 | 0.85 |
| 60 | 23.85 | 21.0 | 15.0 | 10.0 | 0.85 |
| 102 | 26.73 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 13.02 | 35.0 | 11.25 | 9.14 | 0.85 |
| 61 | 11.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 38.36 | 35.0 | 11.25 | 10.0 | 0.6 |
| 51 | 11.69 | 35.0 | 11.25 | 8.21 | 0.85 |
| 80 | 20.25 | 21.0 | 11.25 | 10.0 | 0.85 |
