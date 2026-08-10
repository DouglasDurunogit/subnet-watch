# RANKING - generated 2026-08-10T03:01:07Z, block 8811184

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
| 1 | 107 | Minos | 78.2 | 1.0 | 116 | 33,003 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.9d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 67.28 | 203 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.2d ago |
| 3 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,780 | 1,780 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 2.8d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,223 | 1,223 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 2.3d ago |
| 5 | 67 | Harnyx | 71.2 | 1.0 | 17.59 | 764 | cpu-small | 0.051 | 121 | 20% | SCORING_COMMIT 0.7d ago |
| 6 | 91 | cascade | 70.2 | 0.85 | 786 | 2,693 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.9d ago |
| 7 | 96 | Verathos | 70.2 | 1.0 | 35.01 | 265 | rtx4090 | 0.420 | 48 | 42% | RELEASE 0.6d ago |
| 8 | 1 | Apex | 69.9 | 0.85 | 719 | 1,650 | rtx4090 | 0.488 | 4 | 49% | RELEASE 2.3d ago |
| 9 | 41 | Almanac | 69.2 | 1.0 | 11.08 | 34.35 | cpu-small | 0.699 | 69 | 70% | SCORING_COMMIT 3.1d ago |
| 10 | 15 | ORO | 68.3 | 1.0 | 10.26 | 19.79 | cpu-small | 0.000 | 75 | 94% | RELEASE 3.7d ago |
| 11 | 62 | Ridges | 68.2 | 0.85 | 432 | 2,005 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.2d ago |
| 12 | 26 | Perturb | 68.2 | 1.0 | 21.24 | 39.52 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.5d ago |
| 13 | 100 | BASE | 67.1 | 0.85 | 309 | 839 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.2d ago |
| 14 | 28 | gm | 65.8 | 0.85 | 213 | 4,376 | rtx4090 | 0.196 | 24 | 43% | RELEASE 2.2d ago |
| 15 | 38 | ChronoLLM | 65.7 | 0.85 | 218 | 3,657 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.7d ago |
| 16 | 21 | AdTAO | 65.4 | 1.0 | 4.66 | 21.59 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.5d ago |
| 17 | 80 | OpenRoboto | 64.9 | 0.85 | 163 | 591 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 1.9d ago |
| 18 | 61 | RedTeam | 62.7 | 0.85 | 83.93 | 351 | rtx4090 | 0.000 | 47 | 7% | RELEASE 0.7d ago |
| 19 | 51 | lium.io | 58.9 | 0.85 | 33.81 | 3,224 | rtx4090 | 0.000 | 50 | 56% | SCORING_COMMIT 2.3d ago |
| 20 | 6 | Numinous | 58.0 | 1.0 | 22.97 | 451 | cpu-small | 0.000 | 18 | 26% | README_TASK_DIFF 11d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 473 | 997 | rtx4090 | 0.707 | 7 | 71% | SCORING_COMMIT 12d ago |
| 22 | 85 | Vidaio | 56.1 | 0.85 | 402 | 557 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 13d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,289 | 7,289 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.6d ago |
| 24 | 124 | Swarm | 54.0 | 0.85 | 225 | 651 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 9d ago |
| 25 | 2 | DSperse | 53.7 | 0.85 | 4.86 | 105 | rtx4090 | 0.826 | 12 | 83% | RELEASE 3.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.80 | a4000 | 994.7367755853431 |
| 104 | Masx.ai | -2.67 | rtx4090 | 11.254969819441136 |
| 13 | Data Universe | -3.54 | rtx4090 | 7.507295246345395 |
| 88 | Investing | -4.57 | rtx4090 | 564.0785638510245 |
| 89 | InfiniteQuant | -8.20 | rtx4090 | 98.1125218382587 |
| 8 | Vanta | -7.40 | rtx4090 | 3357.547382754915 |
| 19 | blockmachine | -1.71 | rtx4090 | 211.70351783455774 |
| 18 | Zeus | -2.82 | rtx4090 | 1421.1397811421357 |
| 45 | AlphaRidge.ai | -4.45 | rtx4090 | 10.319639966116235 |
| 75 | Hippius | -4.46 | rtx4090 | 5.770899142669057 |
| 123 | MANTIS | -6.22 | rtx4090 | 74.23788562694408 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07504401486818511 |
| 105 | Beam | -4.49 | rtx4090 | 189.46744806906872 |
| 84 | ansuz | -8.15 | rtx4090 | 506.1690156064538 |
| 34 | BitMind | -18.48 | a100-80 | 296.04010848602957 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.8 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 16.68 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.57 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.09 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.54 | 35.0 | 15.0 | 9.69 | 1.0 |
| 91 | 26.34 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 14.16 | 35.0 | 11.25 | 9.77 | 1.0 |
| 1 | 25.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.84 | 35.0 | 15.0 | 9.39 | 1.0 |
| 15 | 9.57 | 35.0 | 15.0 | 8.77 | 1.0 |
| 62 | 23.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.25 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 22.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 21.19 | 35.0 | 11.25 | 9.97 | 0.85 |
| 38 | 21.28 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 6.85 | 35.0 | 15.0 | 8.54 | 1.0 |
| 80 | 20.14 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.02 | 35.0 | 11.25 | 9.0 | 0.85 |
| 6 | 12.55 | 21.0 | 15.0 | 9.41 | 1.0 |
| 56 | 24.34 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.7 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.13 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.41 | 21.0 | 11.25 | 9.85 | 0.85 |
| 2 | 6.99 | 35.0 | 11.25 | 9.99 | 0.85 |
