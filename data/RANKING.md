# RANKING - generated 2026-08-17T11:49:46Z, block 8864219

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
| 1 | 76 | Phylax | 78.4 | 1.0 | 105 | 203 | cpu-small | 0.000 | 10 | 20% | SCORING_COMMIT 1.0d ago |
| 2 | 107 | Minos | 78.1 | 1.0 | 113 | 33,049 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.9d ago |
| 3 | 67 | Harnyx | 72.0 | 1.0 | 20.81 | 389 | cpu-small | 0.000 | 129 | 11% | SCORING_COMMIT 0.0d ago |
| 4 | 26 | Perturb | 71.3 | 1.0 | 45.40 | 1,622 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.8d ago |
| 5 | 91 | cascade | 69.1 | 0.85 | 570 | 2,305 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 3.5d ago |
| 6 | 85 | Vidaio | 68.7 | 0.85 | 503 | 505 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 0.0d ago |
| 7 | 41 | Almanac | 68.7 | 1.0 | 9.82 | 53.55 | cpu-small | 0.691 | 75 | 69% | SCORING_COMMIT 4.5d ago |
| 8 | 96 | Verathos | 68.5 | 1.0 | 23.02 | 423 | rtx4090 | 0.408 | 67 | 41% | RELEASE 2.6d ago |
| 9 | 62 | Ridges | 68.4 | 0.85 | 466 | 2,157 | rtx4090 | 0.000 | 6 | 40% | RELEASE 2.6d ago |
| 10 | 15 | ORO | 67.9 | 1.0 | 10.84 | 12,363 | cpu-small | 0.000 | 66 | 94% | SCORING_COMMIT 3.6d ago |
| 11 | 21 | AdTAO | 67.7 | 1.0 | 7.65 | 34.28 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 6.0d ago |
| 12 | 38 | ChronoLLM | 66.1 | 0.85 | 101 | 1,378 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.8d ago |
| 13 | 124 | Swarm | 65.9 | 0.85 | 224 | 719 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.9d ago |
| 14 | 2 | DSperse | 62.8 | 0.85 | 85.82 | 136 | rtx4090 | 0.823 | 5 | 82% | RELEASE 6.6d ago |
| 15 | 55 | NIOME | 61.5 | 0.85 | 58.06 | 489 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.6d ago |
| 16 | 28 | gm | 61.4 | 0.85 | 58.78 | 2,467 | rtx4090 | 0.097 | 43 | 25% | RELEASE 4.9d ago |
| 17 | 60 | Bitsec.ai | 58.9 | 0.85 | 364 | 364 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 10d ago |
| 18 | 74 | Gittensor | 58.2 | 0.85 | 23.36 | 208 | rtx4090 | 0.630 | 14 | 63% | RELEASE 5.7d ago |
| 19 | 51 | lium.io | 57.1 | 0.85 | 22.30 | 2,563 | rtx4090 | 0.000 | 56 | 79% | RELEASE 0.2d ago |
| 20 | 61 | RedTeam | 57.0 | 0.85 | 14.59 | 406 | rtx4090 | 0.000 | 84 | 10% | RELEASE 6.2d ago |
| 21 | 68 | NOVA | 55.1 | 0.6 | 8,051 | 8,051 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.9d ago |
| 22 | 120 | Affine | 54.6 | 0.6 | 6,604 | 6,604 | rtx4090 | 0.200 | 5 | 20% | SCORING_COMMIT 4.9d ago |
| 23 | 93 | Bitcast | 54.2 | 0.85 | 234 | 622 | rtx4090 | 0.000 | 4 | 82% | SCORING_COMMIT 19d ago |
| 24 | 97 | Albedo | 52.6 | 0.6 | 2,826 | 2,826 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.0d ago |
| 25 | 80 | OpenRoboto | 52.4 | 0.85 | 133 | 428 | rtx4090 | 0.933 | 4 | 93% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 226.38413379917804 |
| 54 | Yanez | -4.72 | a4000 | 954.3215552600271 |
| 104 | Masx.ai | -0.57 | rtx4090 | 10.737511144299729 |
| 75 | Hippius | -7.02 | rtx4090 | 11050.954839227848 |
| 56 | Gradients | -7.47 | rtx4090 | 970.1525644951774 |
| 89 | InfiniteQuant | -8.11 | rtx4090 | 148.5982557288716 |
| 114 | SOMA | -8.13 | rtx4090 | 3940.5084204409104 |
| 13 | Data Universe | -3.70 | rtx4090 | 5.893877264853587 |
| 88 | Investing | -4.94 | rtx4090 | 940.7659876722452 |
| 8 | Vanta | -7.96 | rtx4090 | 2852.7061048575897 |
| 43 | Graphite | -0.78 | cpu-small | 17.375361626190124 |
| 19 | blockmachine | -3.63 | rtx4090 | 419.99866797572963 |
| 45 | AlphaRidge.ai | -3.96 | rtx4090 | 21.70496728320346 |
| 18 | Zeus | -4.06 | rtx4090 | 1085.1874774925013 |
| 123 | MANTIS | -6.17 | rtx4090 | 74.43483651111647 |
| 22 | Desearch | -6.24 | rtx4090 | 79.54347932475197 |
| 63 | Enigma | -8.14 | rtx4090 | 5014.248856690725 |
| 105 | Beam | -2.97 | rtx4090 | 72.84790942565455 |
| 84 | ansuz | -8.16 | rtx4090 | 0.06032208786344772 |
| 34 | BitMind | -20.50 | a100-80 | 26.730599641214855 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 18.41 | 35.0 | 15.0 | 10.0 | 1.0 |
| 107 | 18.7 | 35.0 | 15.0 | 9.42 | 1.0 |
| 67 | 12.18 | 35.0 | 15.0 | 9.84 | 1.0 |
| 26 | 15.16 | 35.0 | 11.25 | 9.86 | 1.0 |
| 91 | 25.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 85 | 24.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.41 | 35.0 | 15.0 | 9.33 | 1.0 |
| 96 | 12.56 | 35.0 | 11.25 | 9.72 | 1.0 |
| 62 | 24.27 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.76 | 35.0 | 15.0 | 8.15 | 1.0 |
| 21 | 8.52 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.26 | 35.0 | 15.0 | 9.52 | 0.85 |
| 124 | 21.39 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 17.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.16 | 35.0 | 11.25 | 9.88 | 0.85 |
| 60 | 23.31 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.61 | 35.0 | 11.25 | 9.58 | 0.85 |
| 51 | 12.44 | 35.0 | 11.25 | 8.53 | 0.85 |
| 61 | 10.85 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.52 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.74 | 35.0 | 11.25 | 9.97 | 0.6 |
| 93 | 21.57 | 21.0 | 11.25 | 10.0 | 0.85 |
| 97 | 31.39 | 35.0 | 11.25 | 9.98 | 0.6 |
| 80 | 19.35 | 21.0 | 11.25 | 10.0 | 0.85 |
