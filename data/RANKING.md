# RANKING - generated 2026-08-07T11:34:06Z, block 8792149

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
| 1 | 11 | TrajectoryRL | 79.9 | 0.85 | 5,484 | 5,484 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 5.0d ago |
| 2 | 107 | Minos | 77.8 | 1.0 | 110 | 31,676 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 3.3d ago |
| 3 | 76 | Phylax | 76.8 | 1.0 | 69.32 | 251 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 4.8d ago |
| 4 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,272 | 1,272 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 3.8d ago |
| 5 | 67 | Harnyx | 72.0 | 1.0 | 21.23 | 767 | cpu-small | 0.019 | 133 | 20% | SCORING_COMMIT 0.3d ago |
| 6 | 102 | ConnitoAI | 70.5 | 0.85 | 858 | 2,074 | rtx4090 | 0.250 | 6 | 37% | RELEASE 6.5d ago |
| 7 | 62 | Ridges | 69.1 | 0.85 | 560 | 2,024 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.6d ago |
| 8 | 91 | cascade | 68.9 | 0.85 | 528 | 1,498 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.3d ago |
| 9 | 96 | Verathos | 68.6 | 1.0 | 23.56 | 581 | rtx4090 | 0.438 | 44 | 44% | RELEASE 0.5d ago |
| 10 | 15 | ORO | 68.5 | 1.0 | 11.49 | 18.77 | cpu-small | 0.000 | 72 | 93% | RELEASE 1.1d ago |
| 11 | 26 | Perturb | 68.2 | 1.0 | 21.28 | 39.08 | rtx3060 | 0.508 | 11 | 51% | SCORING_COMMIT 0.9d ago |
| 12 | 41 | Almanac | 67.6 | 1.0 | 7.48 | 44.90 | cpu-small | 0.799 | 62 | 80% | SCORING_COMMIT 0.5d ago |
| 13 | 124 | Swarm | 65.7 | 0.85 | 212 | 610 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 5.9d ago |
| 14 | 21 | AdTAO | 65.5 | 1.0 | 4.69 | 21.70 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.5d ago |
| 15 | 74 | Gittensor | 65.4 | 0.85 | 188 | 391 | rtx4090 | 0.000 | 9 | 18% | RELEASE 0.5d ago |
| 16 | 61 | RedTeam | 62.7 | 0.85 | 83.23 | 195 | rtx4090 | 0.000 | 38 | 6% | RELEASE 2.0d ago |
| 17 | 101 | Tag101 | 58.0 | 1.0 | 0.03 | 0.72 | cpu-small | 0.902 | 241 | 90% | SCORING_COMMIT 6.8d ago |
| 18 | 51 | lium.io | 57.3 | 0.85 | 23.74 | 2,927 | rtx4090 | 0.000 | 42 | 69% | SCORING_COMMIT 3.2d ago |
| 19 | 2 | DSperse | 56.7 | 0.85 | 12.95 | 146 | rtx4090 | 0.826 | 8 | 83% | RELEASE 1.3d ago |
| 20 | 56 | Gradients | 56.5 | 0.85 | 453 | 956 | rtx4090 | 0.700 | 7 | 70% | SCORING_COMMIT 10d ago |
| 21 | 85 | Vidaio | 56.3 | 0.85 | 428 | 679 | rtx4090 | 0.000 | 10 | 21% | SCORING_COMMIT 10d ago |
| 22 | 9 | iota | 55.9 | 0.6 | 11,247 | 11,247 | rtx4090 | 0.401 | 3 | 56% | RELEASE 6.8d ago |
| 23 | 120 | Affine | 54.6 | 0.6 | 6,617 | 6,617 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.0d ago |
| 24 | 38 | ChronoLLM | 53.8 | 0.85 | 217 | 3,651 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 8d ago |
| 25 | 97 | Albedo | 52.7 | 0.6 | 2,949 | 2,949 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.4d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.87 | a4000 | 1046.9633327327156 |
| 104 | Masx.ai | -1.43 | rtx4090 | 9.439260706244642 |
| 13 | Data Universe | -3.32 | rtx4090 | 6.401626253410993 |
| 88 | Investing | -6.80 | rtx4090 | 647.0825692628409 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 157.87358656106795 |
| 8 | Vanta | -7.43 | rtx4090 | 3185.7571419472033 |
| 32 | ItsAI | -0.18 | rtx4090 | 10.353195978899596 |
| 19 | blockmachine | -1.29 | rtx4090 | 122.853062955786 |
| 22 | Desearch | -1.81 | rtx4090 | 71.66760313094538 |
| 45 | AlphaRidge.ai | -2.59 | rtx4090 | 22.74297780244211 |
| 75 | Hippius | -4.53 | rtx4090 | 5.495855236588819 |
| 18 | Zeus | -5.09 | rtx4090 | 1176.24808692853 |
| 123 | MANTIS | -6.15 | rtx4090 | 78.0437402607339 |
| 63 | Enigma | -8.15 | rtx4090 | 4784.9621141985635 |
| 84 | ansuz | -8.15 | rtx4090 | 481.20154984241856 |
| 34 | BitMind | -18.41 | a100-80 | 283.2111227158599 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn28, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn121, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 34.01 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.61 | 35.0 | 15.0 | 9.14 | 1.0 |
| 76 | 16.8 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.24 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.25 | 35.0 | 15.0 | 9.72 | 1.0 |
| 102 | 26.68 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 25.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.77 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 12.64 | 35.0 | 11.25 | 9.73 | 1.0 |
| 15 | 9.97 | 35.0 | 15.0 | 8.49 | 1.0 |
| 26 | 12.26 | 35.0 | 11.25 | 9.7 | 1.0 |
| 41 | 8.44 | 35.0 | 15.0 | 9.13 | 1.0 |
| 124 | 21.18 | 35.0 | 11.25 | 9.85 | 0.85 |
| 21 | 6.87 | 35.0 | 15.0 | 8.62 | 1.0 |
| 74 | 20.71 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 17.51 | 35.0 | 11.25 | 10.0 | 0.85 |
| 101 | 0.13 | 35.0 | 15.0 | 7.84 | 1.0 |
| 51 | 12.67 | 35.0 | 11.25 | 8.49 | 0.85 |
| 2 | 10.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.17 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.94 | 21.0 | 11.25 | 10.0 | 0.85 |
| 9 | 36.85 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.75 | 35.0 | 11.25 | 9.99 | 0.6 |
| 38 | 21.28 | 21.0 | 11.25 | 9.78 | 0.85 |
| 97 | 31.56 | 35.0 | 11.25 | 9.99 | 0.6 |
