# RANKING - generated 2026-08-16T19:58:53Z, block 8859464

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
| 1 | 107 | Minos | 78.4 | 1.0 | 119 | 33,888 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.2d ago |
| 2 | 67 | Harnyx | 72.6 | 1.0 | 23.68 | 419 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.6d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.69 | 74.64 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.2d ago |
| 4 | 1 | Apex | 70.0 | 0.85 | 748 | 1,034 | rtx4090 | 0.560 | 4 | 56% | RELEASE 3.2d ago |
| 5 | 76 | Phylax | 70.0 | 1.0 | 11.67 | 158 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.3d ago |
| 6 | 41 | Almanac | 69.9 | 1.0 | 12.91 | 47.99 | cpu-small | 0.652 | 75 | 65% | SCORING_COMMIT 3.9d ago |
| 7 | 96 | Verathos | 69.5 | 1.0 | 29.67 | 279 | rtx4090 | 0.408 | 64 | 41% | RELEASE 2.0d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 566 | 2,291 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.9d ago |
| 9 | 15 | ORO | 68.9 | 1.0 | 12.69 | 21.18 | cpu-small | 0.000 | 64 | 94% | SCORING_COMMIT 2.9d ago |
| 10 | 85 | Vidaio | 68.7 | 0.85 | 506 | 714 | rtx4090 | 0.000 | 10 | 23% | SCORING_COMMIT 0.1d ago |
| 11 | 56 | Gradients | 68.7 | 0.85 | 505 | 963 | rtx4090 | 0.678 | 7 | 68% | SCORING_COMMIT 4.2d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 477 | 2,209 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.9d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.68 | 34.41 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.3d ago |
| 14 | 11 | TrajectoryRL | 67.2 | 0.85 | 4,258 | 4,258 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 98.27 | 1,343 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.1d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 225 | 723 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.2d ago |
| 17 | 2 | DSperse | 61.6 | 0.85 | 59.35 | 143 | rtx4090 | 0.822 | 6 | 82% | RELEASE 6.0d ago |
| 18 | 55 | NIOME | 61.4 | 0.85 | 55.62 | 480 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.0d ago |
| 19 | 28 | gm | 60.3 | 0.85 | 41.68 | 2,266 | rtx4090 | 0.122 | 42 | 26% | RELEASE 4.2d ago |
| 20 | 60 | Bitsec.ai | 59.0 | 0.85 | 374 | 374 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 21 | 74 | Gittensor | 58.4 | 0.85 | 24.97 | 209 | rtx4090 | 0.631 | 14 | 63% | RELEASE 5.1d ago |
| 22 | 51 | lium.io | 57.8 | 0.85 | 25.96 | 2,529 | rtx4090 | 0.000 | 53 | 77% | SCORING_COMMIT 2.4d ago |
| 23 | 61 | RedTeam | 57.0 | 0.85 | 14.64 | 407 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.5d ago |
| 24 | 120 | Affine | 55.1 | 0.6 | 8,280 | 8,280 | rtx4090 | 0.250 | 4 | 25% | SCORING_COMMIT 4.2d ago |
| 25 | 68 | NOVA | 55.1 | 0.6 | 8,094 | 8,094 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 244.45526139597519 |
| 54 | Yanez | -4.06 | a4000 | 951.3895865331998 |
| 104 | Masx.ai | -0.18 | rtx4090 | 9.184691995209764 |
| 75 | Hippius | -7.38 | rtx4090 | 10888.171509254376 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 134.60627158192327 |
| 101 | Tag101 | -0.03 | cpu-small | 1.9550450024299832 |
| 13 | Data Universe | -3.46 | rtx4090 | 5.867977435551466 |
| 88 | Investing | -5.47 | rtx4090 | 1110.906442689521 |
| 8 | Vanta | -7.70 | rtx4090 | 2918.0959004257793 |
| 114 | SOMA | -8.13 | rtx4090 | 615.7318253194844 |
| 43 | Graphite | -0.78 | cpu-small | 16.60452581422998 |
| 45 | AlphaRidge.ai | -2.60 | rtx4090 | 24.908783636329776 |
| 18 | Zeus | -3.44 | rtx4090 | 1400.8646353130819 |
| 22 | Desearch | -4.31 | rtx4090 | 80.75912775620678 |
| 123 | MANTIS | -6.18 | rtx4090 | 74.97167155346833 |
| 19 | blockmachine | -7.03 | rtx4090 | 464.96949289110944 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07602209228268246 |
| 105 | Beam | -2.95 | rtx4090 | 110.85525222184377 |
| 84 | ansuz | -8.16 | rtx4090 | 440.86182426123526 |
| 34 | BitMind | -20.59 | a100-80 | 22.291515703240574 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.92 | 35.0 | 15.0 | 9.45 | 1.0 |
| 67 | 12.66 | 35.0 | 15.0 | 9.92 | 1.0 |
| 26 | 14.73 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.14 | 35.0 | 11.25 | 10.0 | 0.85 |
| 76 | 10.03 | 35.0 | 15.0 | 10.0 | 1.0 |
| 41 | 10.4 | 35.0 | 15.0 | 9.49 | 1.0 |
| 96 | 13.52 | 35.0 | 11.25 | 9.78 | 1.0 |
| 91 | 25.05 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.33 | 35.0 | 15.0 | 8.55 | 1.0 |
| 85 | 24.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.53 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 33.01 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.16 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.41 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 16.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 15.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.83 | 35.0 | 11.25 | 9.84 | 0.85 |
| 60 | 23.41 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.87 | 35.0 | 11.25 | 9.6 | 0.85 |
| 51 | 13.01 | 35.0 | 11.25 | 8.73 | 0.85 |
| 61 | 10.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.64 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.55 | 35.0 | 11.25 | 10.0 | 0.6 |
