# RANKING - generated 2026-08-07T12:30:44Z, block 8792432

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
| 1 | 11 | TrajectoryRL | 79.9 | 0.85 | 5,451 | 5,451 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 5.1d ago |
| 2 | 107 | Minos | 78.2 | 1.0 | 115 | 31,498 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 3.3d ago |
| 3 | 76 | Phylax | 77.0 | 1.0 | 73.29 | 265 | cpu-small | 0.000 | 10 | 31% | SCORING_COMMIT 4.8d ago |
| 4 | 98 | NeverPlayAlone | 76.0 | 0.85 | 1,703 | 1,703 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 0.2d ago |
| 5 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,271 | 1,271 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 3.9d ago |
| 6 | 67 | Harnyx | 72.0 | 1.0 | 21.18 | 765 | cpu-small | 0.019 | 133 | 20% | SCORING_COMMIT 0.4d ago |
| 7 | 102 | ConnitoAI | 71.8 | 0.85 | 1,259 | 1,517 | rtx4090 | 0.250 | 5 | 28% | RELEASE 6.6d ago |
| 8 | 62 | Ridges | 69.1 | 0.85 | 560 | 2,024 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.6d ago |
| 9 | 91 | cascade | 68.9 | 0.85 | 530 | 1,501 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.3d ago |
| 10 | 96 | Verathos | 68.6 | 1.0 | 23.50 | 580 | rtx4090 | 0.439 | 44 | 44% | RELEASE 0.5d ago |
| 11 | 15 | ORO | 68.5 | 1.0 | 11.39 | 18.43 | cpu-small | 0.000 | 74 | 93% | RELEASE 1.1d ago |
| 12 | 26 | Perturb | 68.2 | 1.0 | 21.30 | 38.93 | rtx3060 | 0.508 | 11 | 51% | SCORING_COMMIT 0.9d ago |
| 13 | 41 | Almanac | 67.6 | 1.0 | 7.45 | 44.75 | cpu-small | 0.799 | 62 | 80% | SCORING_COMMIT 0.5d ago |
| 14 | 124 | Swarm | 65.7 | 0.85 | 211 | 607 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 5.9d ago |
| 15 | 21 | AdTAO | 65.5 | 1.0 | 4.67 | 21.63 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.5d ago |
| 16 | 74 | Gittensor | 65.4 | 0.85 | 192 | 385 | rtx4090 | 0.000 | 9 | 18% | RELEASE 0.5d ago |
| 17 | 61 | RedTeam | 62.6 | 0.85 | 80.68 | 195 | rtx4090 | 0.000 | 38 | 6% | RELEASE 2.0d ago |
| 18 | 51 | lium.io | 58.4 | 0.85 | 29.57 | 2,899 | rtx4090 | 0.000 | 41 | 70% | SCORING_COMMIT 3.2d ago |
| 19 | 101 | Tag101 | 57.4 | 1.0 | 0.03 | 0.76 | cpu-small | 0.903 | 241 | 90% | SCORING_COMMIT 6.8d ago |
| 20 | 2 | DSperse | 56.6 | 0.85 | 12.84 | 145 | rtx4090 | 0.826 | 8 | 83% | RELEASE 1.3d ago |
| 21 | 85 | Vidaio | 56.5 | 0.85 | 454 | 788 | rtx4090 | 0.000 | 10 | 24% | SCORING_COMMIT 10d ago |
| 22 | 28 | gm | 56.5 | 0.85 | 13.91 | 2,896 | rtx4090 | 0.471 | 17 | 47% | RELEASE 3.9d ago |
| 23 | 56 | Gradients | 56.4 | 0.85 | 451 | 950 | rtx4090 | 0.700 | 7 | 70% | SCORING_COMMIT 10d ago |
| 24 | 9 | iota | 55.8 | 0.6 | 11,202 | 11,202 | rtx4090 | 0.403 | 3 | 56% | RELEASE 6.8d ago |
| 25 | 120 | Affine | 54.6 | 0.6 | 6,627 | 6,627 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.98 | a4000 | 1086.4375586202555 |
| 104 | Masx.ai | -1.47 | rtx4090 | 7.980670411718586 |
| 13 | Data Universe | -3.39 | rtx4090 | 6.268921867383593 |
| 88 | Investing | -6.79 | rtx4090 | 648.6284503629768 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 158.1348458722274 |
| 8 | Vanta | -7.44 | rtx4090 | 3304.9635656905803 |
| 32 | ItsAI | -0.29 | rtx4090 | 9.781010780989083 |
| 19 | blockmachine | -1.07 | rtx4090 | 164.70530418762786 |
| 22 | Desearch | -2.97 | rtx4090 | 59.437167401489425 |
| 45 | AlphaRidge.ai | -4.21 | rtx4090 | 19.004657178656917 |
| 75 | Hippius | -4.60 | rtx4090 | 5.386303182033248 |
| 18 | Zeus | -5.10 | rtx4090 | 1172.250527104608 |
| 123 | MANTIS | -6.15 | rtx4090 | 77.57848035132699 |
| 63 | Enigma | -8.15 | rtx4090 | 4848.291290688975 |
| 84 | ansuz | -8.15 | rtx4090 | 479.5670841782137 |
| 34 | BitMind | -18.66 | a100-80 | 282.272180496958 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn121, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.98 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.77 | 35.0 | 15.0 | 9.44 | 1.0 |
| 76 | 17.02 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.39 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.24 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.24 | 35.0 | 15.0 | 9.74 | 1.0 |
| 102 | 28.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 25.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.78 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 12.64 | 35.0 | 11.25 | 9.73 | 1.0 |
| 15 | 9.94 | 35.0 | 15.0 | 8.61 | 1.0 |
| 26 | 12.26 | 35.0 | 11.25 | 9.7 | 1.0 |
| 41 | 8.43 | 35.0 | 15.0 | 9.13 | 1.0 |
| 124 | 21.17 | 35.0 | 11.25 | 9.83 | 0.85 |
| 21 | 6.85 | 35.0 | 15.0 | 8.62 | 1.0 |
| 74 | 20.79 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 17.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 13.51 | 35.0 | 11.25 | 8.91 | 0.85 |
| 101 | 0.12 | 35.0 | 15.0 | 7.26 | 1.0 |
| 2 | 10.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.17 | 21.0 | 11.25 | 10.0 | 0.85 |
| 28 | 10.67 | 35.0 | 11.25 | 9.54 | 0.85 |
| 56 | 24.15 | 21.0 | 11.25 | 10.0 | 0.85 |
| 9 | 36.83 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.76 | 35.0 | 11.25 | 9.99 | 0.6 |
