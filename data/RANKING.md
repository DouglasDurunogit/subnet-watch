# RANKING - generated 2026-08-09T09:01:54Z, block 8805788

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
| 1 | 11 | TrajectoryRL | 79.5 | 0.85 | 4,840 | 4,840 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.9d ago |
| 2 | 107 | Minos | 78.6 | 1.0 | 125 | 35,269 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.2d ago |
| 3 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,251 | 1,251 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.6d ago |
| 4 | 76 | Phylax | 74.9 | 1.0 | 42.80 | 204 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.5d ago |
| 5 | 67 | Harnyx | 70.8 | 1.0 | 15.16 | 866 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 2.2d ago |
| 6 | 1 | Apex | 70.2 | 0.85 | 792 | 1,631 | rtx4090 | 0.451 | 4 | 45% | RELEASE 1.5d ago |
| 7 | 91 | cascade | 70.2 | 0.85 | 784 | 2,684 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.2d ago |
| 8 | 100 | BASE | 69.4 | 0.85 | 625 | 1,681 | rtx4090 | 0.000 | 4 | 50% | SCORING_COMMIT 0.5d ago |
| 9 | 41 | Almanac | 69.4 | 1.0 | 11.68 | 34.70 | cpu-small | 0.715 | 67 | 72% | SCORING_COMMIT 2.4d ago |
| 10 | 96 | Verathos | 69.1 | 1.0 | 26.32 | 253 | rtx4090 | 0.407 | 75 | 41% | RELEASE 0.0d ago |
| 11 | 62 | Ridges | 68.3 | 0.85 | 442 | 2,049 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.5d ago |
| 12 | 26 | Perturb | 68.3 | 1.0 | 21.75 | 41.86 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 2.8d ago |
| 13 | 15 | ORO | 67.3 | 1.0 | 8.91 | 19.18 | cpu-small | 0.000 | 71 | 94% | RELEASE 2.9d ago |
| 14 | 28 | gm | 66.7 | 0.85 | 279 | 4,086 | rtx4090 | 0.000 | 24 | 42% | RELEASE 1.5d ago |
| 15 | 38 | ChronoLLM | 65.7 | 0.85 | 215 | 3,618 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.0d ago |
| 16 | 21 | AdTAO | 65.6 | 1.0 | 4.91 | 22.59 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.8d ago |
| 17 | 80 | OpenRoboto | 64.6 | 0.85 | 147 | 536 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 1.2d ago |
| 18 | 61 | RedTeam | 62.7 | 0.85 | 82.28 | 234 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.3d ago |
| 19 | 51 | lium.io | 60.0 | 0.85 | 44.33 | 2,995 | rtx4090 | 0.000 | 48 | 70% | SCORING_COMMIT 1.5d ago |
| 20 | 6 | Numinous | 59.1 | 1.0 | 30.01 | 344 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 480 | 1,011 | rtx4090 | 0.705 | 7 | 71% | SCORING_COMMIT 11d ago |
| 22 | 2 | DSperse | 56.2 | 0.85 | 11.31 | 126 | rtx4090 | 0.826 | 15 | 83% | RELEASE 3.2d ago |
| 23 | 85 | Vidaio | 55.5 | 0.85 | 345 | 545 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 12d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,286 | 7,286 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.9d ago |
| 25 | 74 | Gittensor | 54.0 | 0.85 | 7.76 | 227 | rtx4090 | 0.630 | 16 | 63% | RELEASE 1.7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.97 | a4000 | 1037.3370184453238 |
| 104 | Masx.ai | -1.49 | rtx4090 | 9.944979423983273 |
| 13 | Data Universe | -2.76 | rtx4090 | 6.9853598815270015 |
| 88 | Investing | -5.77 | rtx4090 | 484.7306724869005 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 131.30874534589776 |
| 8 | Vanta | -7.38 | rtx4090 | 3408.0927710477467 |
| 19 | blockmachine | -1.24 | rtx4090 | 298.7730371331526 |
| 45 | AlphaRidge.ai | -4.34 | rtx4090 | 17.35532301403391 |
| 75 | Hippius | -4.40 | rtx4090 | 5.677075413454615 |
| 18 | Zeus | -4.88 | rtx4090 | 973.8503078507922 |
| 123 | MANTIS | -6.19 | rtx4090 | 74.57181849501883 |
| 63 | Enigma | -8.14 | rtx4090 | 5027.34636945614 |
| 105 | Beam | -4.39 | rtx4090 | 176.78598055287378 |
| 84 | ansuz | -8.15 | rtx4090 | 505.8111946819376 |
| 34 | BitMind | -18.20 | a100-80 | 300.44461316779365 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.51 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 19.11 | 35.0 | 15.0 | 9.46 | 1.0 |
| 60 | 28.17 | 35.0 | 15.0 | 10.0 | 0.85 |
| 76 | 14.93 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 10.99 | 35.0 | 15.0 | 9.77 | 1.0 |
| 1 | 26.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.33 | 35.0 | 11.25 | 9.97 | 0.85 |
| 100 | 25.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.03 | 35.0 | 15.0 | 9.41 | 1.0 |
| 96 | 13.06 | 35.0 | 11.25 | 9.74 | 1.0 |
| 62 | 24.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.34 | 35.0 | 11.25 | 9.68 | 1.0 |
| 15 | 9.06 | 35.0 | 15.0 | 8.22 | 1.0 |
| 28 | 22.26 | 35.0 | 11.25 | 9.98 | 0.85 |
| 38 | 21.24 | 35.0 | 11.25 | 9.76 | 0.85 |
| 21 | 7.02 | 35.0 | 15.0 | 8.6 | 1.0 |
| 80 | 19.75 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.47 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 15.06 | 35.0 | 11.25 | 9.22 | 0.85 |
| 6 | 13.56 | 21.0 | 15.0 | 9.54 | 1.0 |
| 56 | 24.39 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.09 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.13 | 35.0 | 11.25 | 9.99 | 0.6 |
| 74 | 8.57 | 35.0 | 11.25 | 8.67 | 0.85 |
