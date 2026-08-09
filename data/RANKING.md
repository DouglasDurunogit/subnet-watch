# RANKING - generated 2026-08-09T08:07:23Z, block 8805516

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
| 1 | 11 | TrajectoryRL | 79.5 | 0.85 | 4,850 | 4,850 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.9d ago |
| 2 | 107 | Minos | 78.4 | 1.0 | 120 | 35,598 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.2d ago |
| 3 | 76 | Phylax | 76.7 | 1.0 | 67.65 | 204 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.4d ago |
| 4 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,254 | 1,254 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.5d ago |
| 5 | 67 | Harnyx | 70.8 | 1.0 | 15.20 | 868 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 2.2d ago |
| 6 | 1 | Apex | 70.2 | 0.85 | 797 | 1,641 | rtx4090 | 0.447 | 4 | 45% | RELEASE 1.5d ago |
| 7 | 91 | cascade | 70.2 | 0.85 | 785 | 2,686 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.2d ago |
| 8 | 100 | BASE | 69.9 | 0.85 | 725 | 1,525 | rtx4090 | 0.000 | 4 | 45% | SCORING_COMMIT 0.5d ago |
| 9 | 41 | Almanac | 69.4 | 1.0 | 11.65 | 34.66 | cpu-small | 0.717 | 67 | 72% | SCORING_COMMIT 2.3d ago |
| 10 | 96 | Verathos | 68.4 | 1.0 | 22.50 | 284 | rtx4090 | 0.405 | 75 | 41% | RELEASE 0.6d ago |
| 11 | 26 | Perturb | 68.4 | 1.0 | 22.24 | 42.13 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 2.7d ago |
| 12 | 62 | Ridges | 68.3 | 0.85 | 442 | 2,051 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.4d ago |
| 13 | 15 | ORO | 67.1 | 1.0 | 8.87 | 19.09 | cpu-small | 0.000 | 71 | 94% | RELEASE 2.9d ago |
| 14 | 28 | gm | 65.9 | 0.85 | 222 | 4,387 | rtx4090 | 0.110 | 24 | 45% | RELEASE 1.5d ago |
| 15 | 38 | ChronoLLM | 65.7 | 0.85 | 216 | 3,621 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.9d ago |
| 16 | 21 | AdTAO | 65.7 | 1.0 | 4.96 | 22.81 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.7d ago |
| 17 | 80 | OpenRoboto | 64.7 | 0.85 | 153 | 555 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 1.1d ago |
| 18 | 61 | RedTeam | 62.5 | 0.85 | 77.59 | 222 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.2d ago |
| 19 | 51 | lium.io | 59.6 | 0.85 | 40.97 | 2,967 | rtx4090 | 0.000 | 49 | 69% | SCORING_COMMIT 1.5d ago |
| 20 | 6 | Numinous | 59.1 | 1.0 | 30.11 | 345 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 21 | 56 | Gradients | 56.7 | 0.85 | 480 | 1,013 | rtx4090 | 0.705 | 7 | 70% | SCORING_COMMIT 11d ago |
| 22 | 2 | DSperse | 56.4 | 0.85 | 11.86 | 102 | rtx4090 | 0.826 | 12 | 83% | RELEASE 3.1d ago |
| 23 | 85 | Vidaio | 55.4 | 0.85 | 335 | 594 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 12d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,269 | 7,269 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.8d ago |
| 25 | 74 | Gittensor | 54.0 | 0.85 | 7.78 | 227 | rtx4090 | 0.630 | 16 | 63% | RELEASE 1.7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.01 | a4000 | 1035.77860081512 |
| 104 | Masx.ai | -1.20 | rtx4090 | 8.512918788831918 |
| 13 | Data Universe | -2.70 | rtx4090 | 6.9861593004682225 |
| 88 | Investing | -5.75 | rtx4090 | 487.7591483819762 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 132.36314996722186 |
| 8 | Vanta | -7.38 | rtx4090 | 3411.9199296751526 |
| 19 | blockmachine | -1.18 | rtx4090 | 216.20414291794316 |
| 45 | AlphaRidge.ai | -3.80 | rtx4090 | 58.80959435051061 |
| 75 | Hippius | -4.40 | rtx4090 | 5.682399655622488 |
| 18 | Zeus | -4.88 | rtx4090 | 975.0848241602505 |
| 123 | MANTIS | -6.19 | rtx4090 | 74.66581958402334 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07724408303836185 |
| 105 | Beam | -4.36 | rtx4090 | 177.80482524488664 |
| 84 | ansuz | -8.15 | rtx4090 | 506.44879240849 |
| 34 | BitMind | -19.21 | a100-80 | 300.7968337943046 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.52 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.95 | 35.0 | 15.0 | 9.43 | 1.0 |
| 76 | 16.7 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.18 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.0 | 35.0 | 15.0 | 9.76 | 1.0 |
| 1 | 26.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.33 | 35.0 | 11.25 | 9.98 | 0.85 |
| 100 | 26.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.02 | 35.0 | 15.0 | 9.41 | 1.0 |
| 96 | 12.47 | 35.0 | 11.25 | 9.69 | 1.0 |
| 26 | 12.43 | 35.0 | 11.25 | 9.69 | 1.0 |
| 62 | 24.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.04 | 35.0 | 15.0 | 8.09 | 1.0 |
| 28 | 21.36 | 35.0 | 11.25 | 9.97 | 0.85 |
| 38 | 21.24 | 35.0 | 11.25 | 9.76 | 0.85 |
| 21 | 7.05 | 35.0 | 15.0 | 8.61 | 1.0 |
| 80 | 19.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.76 | 35.0 | 11.25 | 9.16 | 0.85 |
| 6 | 13.58 | 21.0 | 15.0 | 9.54 | 1.0 |
| 56 | 24.4 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 10.09 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 22.98 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.12 | 35.0 | 11.25 | 9.99 | 0.6 |
| 74 | 8.58 | 35.0 | 11.25 | 8.67 | 0.85 |
