# RANKING - generated 2026-08-07T22:05:25Z, block 8795306

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
| 1 | 107 | Minos | 78.1 | 1.0 | 111 | 33,478 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 3.7d ago |
| 2 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,235 | 1,235 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 0.1d ago |
| 3 | 114 | SOMA | 72.7 | 0.85 | 1,670 | 4,356 | rtx4090 | 0.000 | 3 | 65% | SCORING_COMMIT 0.5d ago |
| 4 | 67 | Harnyx | 72.2 | 1.0 | 21.05 | 763 | cpu-small | 0.012 | 135 | 20% | SCORING_COMMIT 0.8d ago |
| 5 | 1 | Apex | 69.9 | 0.85 | 712 | 1,575 | rtx4090 | 0.387 | 4 | 39% | RELEASE 0.1d ago |
| 6 | 91 | cascade | 69.8 | 0.85 | 699 | 2,819 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.7d ago |
| 7 | 62 | Ridges | 69.1 | 0.85 | 566 | 2,047 | rtx4090 | 0.133 | 7 | 35% | RELEASE 2.0d ago |
| 8 | 15 | ORO | 68.5 | 1.0 | 11.40 | 10,360 | cpu-small | 0.000 | 74 | 93% | RELEASE 1.5d ago |
| 9 | 26 | Perturb | 68.1 | 1.0 | 20.86 | 40.46 | rtx3060 | 0.506 | 11 | 51% | SCORING_COMMIT 1.3d ago |
| 10 | 100 | BASE | 67.9 | 0.85 | 401 | 1,630 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.3d ago |
| 11 | 41 | Almanac | 67.6 | 1.0 | 7.52 | 33.25 | cpu-small | 0.800 | 63 | 80% | SCORING_COMMIT 0.9d ago |
| 12 | 124 | Swarm | 65.6 | 0.85 | 207 | 595 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 6.3d ago |
| 13 | 21 | AdTAO | 65.5 | 1.0 | 4.70 | 21.76 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.2d ago |
| 14 | 96 | Verathos | 64.8 | 1.0 | 9.56 | 219 | rtx4090 | 0.419 | 86 | 42% | RELEASE 0.9d ago |
| 15 | 61 | RedTeam | 61.9 | 0.85 | 64.49 | 184 | rtx4090 | 0.000 | 37 | 6% | RELEASE 2.4d ago |
| 16 | 102 | ConnitoAI | 59.5 | 0.85 | 31.32 | 1,712 | rtx4090 | 0.251 | 8 | 32% | RELEASE 7.0d ago |
| 17 | 28 | gm | 59.4 | 0.85 | 32.32 | 4,512 | rtx4090 | 0.245 | 19 | 51% | RELEASE 0.0d ago |
| 18 | 74 | Gittensor | 57.6 | 0.85 | 22.87 | 213 | rtx4090 | 0.638 | 15 | 64% | RELEASE 0.2d ago |
| 19 | 51 | lium.io | 57.3 | 0.85 | 22.82 | 2,870 | rtx4090 | 0.000 | 44 | 66% | SCORING_COMMIT 0.1d ago |
| 20 | 56 | Gradients | 56.4 | 0.85 | 451 | 950 | rtx4090 | 0.701 | 7 | 70% | SCORING_COMMIT 10d ago |
| 21 | 2 | DSperse | 54.8 | 0.85 | 6.91 | 145 | rtx4090 | 0.826 | 10 | 83% | RELEASE 1.7d ago |
| 22 | 120 | Affine | 54.6 | 0.6 | 6,617 | 6,617 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.4d ago |
| 23 | 38 | ChronoLLM | 53.7 | 0.85 | 213 | 3,571 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 9d ago |
| 24 | 97 | Albedo | 52.6 | 0.6 | 2,902 | 2,902 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.9d ago |
| 25 | 85 | Vidaio | 52.1 | 0.85 | 124 | 656 | rtx4090 | 0.000 | 10 | 20% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.01 | a4000 | 1039.837421606162 |
| 104 | Masx.ai | -1.99 | rtx4090 | 7.752171413958485 |
| 13 | Data Universe | -3.29 | rtx4090 | 6.307314376216294 |
| 88 | Investing | -6.84 | rtx4090 | 629.8959913980393 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 133.65540045357415 |
| 8 | Vanta | -7.44 | rtx4090 | 3180.2094917515083 |
| 32 | ItsAI | -0.10 | rtx4090 | 9.461096449090874 |
| 22 | Desearch | -0.30 | rtx4090 | 85.1298401827692 |
| 19 | blockmachine | -1.59 | rtx4090 | 301.6778702401925 |
| 18 | Zeus | -3.38 | rtx4090 | 1708.2396019433213 |
| 45 | AlphaRidge.ai | -3.74 | rtx4090 | 24.660637208605998 |
| 75 | Hippius | -4.69 | rtx4090 | 5.248042643033303 |
| 123 | MANTIS | -6.20 | rtx4090 | 76.78016185949636 |
| 63 | Enigma | -8.15 | rtx4090 | 0.0735299463076619 |
| 84 | ansuz | -8.15 | rtx4090 | 480.26300850085886 |
| 34 | BitMind | -18.25 | a100-80 | 281.7677400598641 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.63 | 35.0 | 15.0 | 9.42 | 1.0 |
| 60 | 28.12 | 35.0 | 15.0 | 10.0 | 0.85 |
| 114 | 29.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.22 | 35.0 | 15.0 | 9.96 | 1.0 |
| 1 | 25.95 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.87 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 25.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.95 | 35.0 | 15.0 | 8.59 | 1.0 |
| 26 | 12.18 | 35.0 | 11.25 | 9.69 | 1.0 |
| 100 | 23.69 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 8.46 | 35.0 | 15.0 | 9.14 | 1.0 |
| 124 | 21.08 | 35.0 | 11.25 | 9.84 | 0.85 |
| 21 | 6.87 | 35.0 | 15.0 | 8.63 | 1.0 |
| 96 | 9.31 | 35.0 | 11.25 | 9.27 | 1.0 |
| 61 | 16.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 13.73 | 35.0 | 11.25 | 9.99 | 0.85 |
| 28 | 13.85 | 35.0 | 11.25 | 9.8 | 0.85 |
| 74 | 12.53 | 35.0 | 11.25 | 8.96 | 0.85 |
| 51 | 12.52 | 35.0 | 11.25 | 8.59 | 0.85 |
| 56 | 24.15 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 8.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.75 | 35.0 | 11.25 | 9.99 | 0.6 |
| 38 | 21.19 | 21.0 | 11.25 | 9.78 | 0.85 |
| 97 | 31.5 | 35.0 | 11.25 | 9.98 | 0.6 |
| 85 | 19.06 | 21.0 | 11.25 | 10.0 | 0.85 |
