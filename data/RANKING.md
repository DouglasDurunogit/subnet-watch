# RANKING - generated 2026-08-07T18:10:13Z, block 8794130

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
| 1 | 107 | Minos | 77.9 | 1.0 | 106 | 31,253 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 3.6d ago |
| 2 | 76 | Phylax | 77.1 | 1.0 | 75.07 | 271 | cpu-small | 0.000 | 10 | 31% | SCORING_COMMIT 5.1d ago |
| 3 | 98 | NeverPlayAlone | 75.9 | 0.85 | 1,683 | 1,683 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 0.5d ago |
| 4 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,280 | 1,280 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 4.1d ago |
| 5 | 114 | SOMA | 72.7 | 0.85 | 1,647 | 4,296 | rtx4090 | 0.000 | 3 | 65% | SCORING_COMMIT 0.4d ago |
| 6 | 67 | Harnyx | 72.1 | 1.0 | 20.79 | 754 | cpu-small | 0.012 | 135 | 20% | SCORING_COMMIT 0.6d ago |
| 7 | 62 | Ridges | 69.1 | 0.85 | 558 | 2,018 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.9d ago |
| 8 | 91 | cascade | 68.6 | 0.85 | 483 | 1,372 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.6d ago |
| 9 | 15 | ORO | 68.2 | 1.0 | 11.29 | 10,185 | cpu-small | 0.000 | 74 | 93% | RELEASE 1.3d ago |
| 10 | 26 | Perturb | 68.1 | 1.0 | 20.70 | 38.64 | rtx3060 | 0.506 | 11 | 51% | SCORING_COMMIT 1.1d ago |
| 11 | 96 | Verathos | 68.0 | 1.0 | 20.24 | 274 | rtx4090 | 0.426 | 54 | 43% | RELEASE 0.7d ago |
| 12 | 100 | BASE | 67.9 | 0.85 | 394 | 1,599 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.1d ago |
| 13 | 41 | Almanac | 67.5 | 1.0 | 7.35 | 44.16 | cpu-small | 0.800 | 62 | 80% | SCORING_COMMIT 0.7d ago |
| 14 | 124 | Swarm | 65.6 | 0.85 | 207 | 595 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 6.2d ago |
| 15 | 21 | AdTAO | 65.5 | 1.0 | 4.66 | 21.61 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.0d ago |
| 16 | 61 | RedTeam | 62.0 | 0.85 | 67.07 | 180 | rtx4090 | 0.000 | 37 | 6% | RELEASE 2.2d ago |
| 17 | 102 | ConnitoAI | 59.6 | 0.85 | 32.17 | 1,387 | rtx4090 | 0.251 | 8 | 26% | RELEASE 6.8d ago |
| 18 | 28 | gm | 59.2 | 0.85 | 30.41 | 4,190 | rtx4090 | 0.247 | 19 | 48% | RELEASE 4.1d ago |
| 19 | 74 | Gittensor | 58.4 | 0.85 | 25.04 | 241 | rtx4090 | 0.595 | 15 | 60% | RELEASE 0.1d ago |
| 20 | 51 | lium.io | 57.2 | 0.85 | 22.69 | 2,305 | rtx4090 | 0.000 | 43 | 70% | SCORING_COMMIT 3.5d ago |
| 21 | 85 | Vidaio | 56.9 | 0.85 | 523 | 625 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 10d ago |
| 22 | 56 | Gradients | 56.4 | 0.85 | 445 | 939 | rtx4090 | 0.701 | 7 | 70% | SCORING_COMMIT 10d ago |
| 23 | 2 | DSperse | 56.2 | 0.85 | 11.10 | 139 | rtx4090 | 0.826 | 8 | 83% | RELEASE 1.6d ago |
| 24 | 120 | Affine | 54.5 | 0.6 | 6,496 | 6,496 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.2d ago |
| 25 | 38 | ChronoLLM | 53.7 | 0.85 | 208 | 3,496 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.79 | a4000 | 1070.2630364174415 |
| 104 | Masx.ai | -1.55 | rtx4090 | 7.80801088690904 |
| 13 | Data Universe | -3.30 | rtx4090 | 6.067156317466384 |
| 88 | Investing | -6.85 | rtx4090 | 624.3637033967976 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 133.88761956787894 |
| 101 | Tag101 | -0.00 | cpu-small | 1.6844166064352024 |
| 8 | Vanta | -7.45 | rtx4090 | 3139.1289931670776 |
| 32 | ItsAI | -0.29 | rtx4090 | 9.16739218145844 |
| 19 | blockmachine | -1.27 | rtx4090 | 315.8242430398801 |
| 45 | AlphaRidge.ai | -1.98 | rtx4090 | 33.964519369918 |
| 22 | Desearch | -4.13 | rtx4090 | 67.64670360934801 |
| 75 | Hippius | -4.75 | rtx4090 | 5.1574712045981075 |
| 18 | Zeus | -4.81 | rtx4090 | 1282.2466235877648 |
| 123 | MANTIS | -6.25 | rtx4090 | 75.81718061397169 |
| 63 | Enigma | -8.15 | rtx4090 | 0.0727531426655024 |
| 84 | ansuz | -8.15 | rtx4090 | 473.81513947938873 |
| 34 | BitMind | -18.08 | a100-80 | 278.15631668789183 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.46 | 35.0 | 15.0 | 9.41 | 1.0 |
| 76 | 17.11 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.34 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.26 | 35.0 | 15.0 | 10.0 | 0.85 |
| 114 | 29.26 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.17 | 35.0 | 15.0 | 9.92 | 1.0 |
| 62 | 24.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.42 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.91 | 35.0 | 15.0 | 8.31 | 1.0 |
| 26 | 12.15 | 35.0 | 11.25 | 9.69 | 1.0 |
| 96 | 12.07 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 23.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 8.38 | 35.0 | 15.0 | 9.13 | 1.0 |
| 124 | 21.08 | 35.0 | 11.25 | 9.85 | 0.85 |
| 21 | 6.85 | 35.0 | 15.0 | 8.63 | 1.0 |
| 61 | 16.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 13.83 | 35.0 | 11.25 | 9.99 | 0.85 |
| 28 | 13.62 | 35.0 | 11.25 | 9.79 | 0.85 |
| 74 | 12.88 | 35.0 | 11.25 | 9.62 | 0.85 |
| 51 | 12.5 | 35.0 | 11.25 | 8.59 | 0.85 |
| 85 | 24.73 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.1 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.85 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.68 | 35.0 | 11.25 | 9.98 | 0.6 |
| 38 | 21.1 | 21.0 | 11.25 | 9.77 | 0.85 |
