# RANKING - generated 2026-08-09T03:59:37Z, block 8804277

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
| 1 | 107 | Minos | 78.6 | 1.0 | 126 | 35,442 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.0d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 68.27 | 206 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.3d ago |
| 3 | 98 | NeverPlayAlone | 76.2 | 0.85 | 1,818 | 1,818 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 1.9d ago |
| 4 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,264 | 1,264 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.4d ago |
| 5 | 67 | Harnyx | 70.8 | 1.0 | 15.30 | 874 | cpu-small | 0.018 | 151 | 22% | SCORING_COMMIT 2.0d ago |
| 6 | 100 | BASE | 70.5 | 0.85 | 854 | 1,716 | rtx4090 | 0.000 | 3 | 50% | SCORING_COMMIT 0.3d ago |
| 7 | 1 | Apex | 70.3 | 0.85 | 814 | 1,678 | rtx4090 | 0.430 | 4 | 43% | RELEASE 1.3d ago |
| 8 | 91 | cascade | 70.3 | 0.85 | 802 | 2,744 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.0d ago |
| 9 | 41 | Almanac | 69.3 | 1.0 | 11.36 | 46.46 | cpu-small | 0.717 | 67 | 72% | SCORING_COMMIT 2.1d ago |
| 10 | 96 | Verathos | 68.9 | 1.0 | 25.23 | 262 | rtx4090 | 0.403 | 73 | 40% | RELEASE 0.4d ago |
| 11 | 26 | Perturb | 68.4 | 1.0 | 22.23 | 42.68 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 2.5d ago |
| 12 | 62 | Ridges | 68.3 | 0.85 | 449 | 2,084 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.3d ago |
| 13 | 15 | ORO | 68.0 | 1.0 | 9.89 | 20.57 | cpu-small | 0.000 | 71 | 94% | RELEASE 2.7d ago |
| 14 | 28 | gm | 67.0 | 0.85 | 301 | 3,903 | rtx4090 | 0.000 | 25 | 40% | RELEASE 1.3d ago |
| 15 | 38 | ChronoLLM | 65.7 | 0.85 | 218 | 3,664 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.8d ago |
| 16 | 21 | AdTAO | 65.7 | 1.0 | 5.05 | 23.16 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.5d ago |
| 17 | 80 | OpenRoboto | 64.2 | 0.85 | 131 | 481 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 1.0d ago |
| 18 | 61 | RedTeam | 62.4 | 0.85 | 75.93 | 217 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.1d ago |
| 19 | 51 | lium.io | 60.7 | 0.85 | 54.12 | 3,048 | rtx4090 | 0.000 | 47 | 67% | SCORING_COMMIT 1.3d ago |
| 20 | 6 | Numinous | 59.1 | 1.0 | 30.26 | 347 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 10d ago |
| 21 | 102 | ConnitoAI | 58.2 | 0.85 | 756 | 1,471 | rtx4090 | 0.251 | 6 | 29% | RELEASE 8d ago |
| 22 | 85 | Vidaio | 56.9 | 0.85 | 519 | 603 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 12d ago |
| 23 | 56 | Gradients | 56.7 | 0.85 | 483 | 1,017 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 24 | 74 | Gittensor | 55.4 | 0.85 | 11.14 | 245 | rtx4090 | 0.627 | 16 | 63% | RELEASE 1.5d ago |
| 25 | 120 | Affine | 54.8 | 0.6 | 7,246 | 7,246 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.6d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.73 | a4000 | 1045.65191440577 |
| 104 | Masx.ai | -0.70 | rtx4090 | 10.35178690850917 |
| 13 | Data Universe | -2.82 | rtx4090 | 7.550164825795127 |
| 88 | Investing | -5.68 | rtx4090 | 502.10784217784726 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 133.23259032282488 |
| 8 | Vanta | -7.38 | rtx4090 | 3423.971598981075 |
| 19 | blockmachine | -1.24 | rtx4090 | 299.25115308788565 |
| 45 | AlphaRidge.ai | -3.94 | rtx4090 | 41.827129470042735 |
| 75 | Hippius | -4.43 | rtx4090 | 5.644424959768874 |
| 18 | Zeus | -4.87 | rtx4090 | 978.7201918454086 |
| 123 | MANTIS | -6.22 | rtx4090 | 74.86422902715705 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07852761638496716 |
| 105 | Beam | -3.80 | rtx4090 | 195.4665461875626 |
| 84 | ansuz | -8.15 | rtx4090 | 508.312539657545 |
| 34 | BitMind | -19.01 | a100-80 | 301.7825178568841 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn9, sn10, sn12, sn14, sn16, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 19.13 | 35.0 | 15.0 | 9.46 | 1.0 |
| 76 | 16.74 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.65 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.21 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.02 | 35.0 | 15.0 | 9.8 | 1.0 |
| 100 | 26.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 1 | 26.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.42 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 9.93 | 35.0 | 15.0 | 9.39 | 1.0 |
| 96 | 12.9 | 35.0 | 11.25 | 9.73 | 1.0 |
| 26 | 12.43 | 35.0 | 11.25 | 9.69 | 1.0 |
| 62 | 24.14 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.43 | 35.0 | 15.0 | 8.53 | 1.0 |
| 28 | 22.56 | 35.0 | 11.25 | 9.98 | 0.85 |
| 38 | 21.29 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 7.11 | 35.0 | 15.0 | 8.63 | 1.0 |
| 80 | 19.3 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 15.84 | 35.0 | 11.25 | 9.36 | 0.85 |
| 6 | 13.6 | 21.0 | 15.0 | 9.54 | 1.0 |
| 102 | 26.19 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.7 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.42 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.86 | 35.0 | 11.25 | 9.07 | 0.85 |
| 120 | 35.11 | 35.0 | 11.25 | 9.99 | 0.6 |
