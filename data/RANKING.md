# RANKING - generated 2026-08-15T22:34:03Z, block 8853040

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
| 1 | 107 | Minos | 78.0 | 1.0 | 109 | 32,742 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.3d ago |
| 2 | 76 | Phylax | 74.0 | 1.0 | 33.96 | 163 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.2d ago |
| 3 | 67 | Harnyx | 72.6 | 1.0 | 23.33 | 376 | cpu-small | 0.007 | 123 | 10% | SCORING_COMMIT 0.6d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.31 | 75.93 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.3d ago |
| 5 | 1 | Apex | 70.5 | 0.85 | 863 | 1,032 | rtx4090 | 0.570 | 4 | 57% | RELEASE 2.4d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.83 | 443 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 2.2d ago |
| 7 | 41 | Almanac | 69.6 | 1.0 | 12.19 | 53.10 | cpu-small | 0.662 | 72 | 66% | SCORING_COMMIT 3.0d ago |
| 8 | 96 | Verathos | 69.0 | 1.0 | 25.72 | 157 | rtx4090 | 0.408 | 68 | 41% | RELEASE 1.1d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 511 | 966 | rtx4090 | 0.671 | 7 | 67% | SCORING_COMMIT 3.4d ago |
| 10 | 62 | Ridges | 68.6 | 0.85 | 481 | 2,227 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.0d ago |
| 11 | 91 | cascade | 68.3 | 0.85 | 447 | 2,294 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.0d ago |
| 12 | 15 | ORO | 68.1 | 1.0 | 11.28 | 12,286 | cpu-small | 0.000 | 86 | 93% | SCORING_COMMIT 2.0d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.62 | 34.15 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.4d ago |
| 14 | 85 | Vidaio | 66.4 | 0.85 | 256 | 611 | rtx4090 | 0.000 | 10 | 20% | SCORING_COMMIT 3.5d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.64 | 1,335 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.2d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 721 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.3d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.83 | 477 | rtx4090 | 0.021 | 11 | 29% | SCORING_COMMIT 1.1d ago |
| 18 | 28 | gm | 60.6 | 0.85 | 46.06 | 2,116 | rtx4090 | 0.123 | 41 | 24% | RELEASE 3.4d ago |
| 19 | 60 | Bitsec.ai | 59.3 | 0.85 | 409 | 409 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 74 | Gittensor | 59.0 | 0.85 | 29.40 | 211 | rtx4090 | 0.631 | 15 | 63% | RELEASE 4.2d ago |
| 21 | 102 | ConnitoAI | 58.8 | 0.85 | 908 | 2,054 | rtx4090 | 0.251 | 6 | 37% | RELEASE 15d ago |
| 22 | 61 | RedTeam | 57.5 | 0.85 | 16.84 | 432 | rtx4090 | 0.000 | 81 | 10% | RELEASE 4.6d ago |
| 23 | 120 | Affine | 54.6 | 0.6 | 6,662 | 6,662 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.4d ago |
| 24 | 80 | OpenRoboto | 53.1 | 0.85 | 165 | 598 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |
| 25 | 51 | lium.io | 52.6 | 0.85 | 9.20 | 1,463 | rtx4090 | 0.000 | 54 | 82% | SCORING_COMMIT 1.6d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.00 | a4000 | 965.856203335329 |
| 104 | Masx.ai | -0.04 | rtx4090 | 11.774123689771544 |
| 89 | InfiniteQuant | -3.33 | rtx4090 | 201.24599364855555 |
| 75 | Hippius | -7.37 | rtx4090 | 10961.068505595891 |
| 13 | Data Universe | -3.39 | rtx4090 | 5.769470405960235 |
| 88 | Investing | -5.41 | rtx4090 | 339.6694258966628 |
| 8 | Vanta | -7.96 | rtx4090 | 2913.3853033546998 |
| 114 | SOMA | -8.12 | rtx4090 | 627.6099142313913 |
| 43 | Graphite | -0.52 | cpu-small | 10.890648016370003 |
| 32 | ItsAI | -0.07 | rtx4090 | 11.917690148102556 |
| 45 | AlphaRidge.ai | -3.31 | rtx4090 | 15.716299342637646 |
| 18 | Zeus | -3.41 | rtx4090 | 1138.8649909975143 |
| 22 | Desearch | -4.82 | rtx4090 | 70.20925684074435 |
| 123 | MANTIS | -6.09 | rtx4090 | 77.50144000639442 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0757437866875474 |
| 105 | Beam | -2.70 | rtx4090 | 84.64822274469333 |
| 34 | BitMind | -20.09 | a100-80 | 27.132731228416667 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.56 | 35.0 | 15.0 | 9.4 | 1.0 |
| 76 | 14.04 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.61 | 35.0 | 15.0 | 9.98 | 1.0 |
| 26 | 14.79 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.15 | 35.0 | 15.0 | 9.17 | 1.0 |
| 41 | 10.19 | 35.0 | 15.0 | 9.46 | 1.0 |
| 96 | 12.98 | 35.0 | 11.25 | 9.74 | 1.0 |
| 56 | 24.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.4 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.11 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.91 | 35.0 | 15.0 | 8.16 | 1.0 |
| 21 | 8.51 | 35.0 | 15.0 | 9.13 | 1.0 |
| 85 | 21.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.14 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.4 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.21 | 35.0 | 11.25 | 9.86 | 0.85 |
| 60 | 23.77 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 13.49 | 35.0 | 11.25 | 9.66 | 0.85 |
| 102 | 26.91 | 21.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.78 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.18 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 9.17 | 35.0 | 11.25 | 6.41 | 0.85 |
