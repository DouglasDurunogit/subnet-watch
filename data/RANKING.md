# RANKING - generated 2026-08-16T19:43:19Z, block 8859386

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
| 1 | 107 | Minos | 78.3 | 1.0 | 119 | 33,666 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.2d ago |
| 2 | 67 | Harnyx | 72.6 | 1.0 | 23.70 | 419 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.6d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.71 | 74.68 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.2d ago |
| 4 | 1 | Apex | 70.0 | 0.85 | 750 | 1,037 | rtx4090 | 0.559 | 4 | 56% | RELEASE 3.2d ago |
| 5 | 76 | Phylax | 70.0 | 1.0 | 11.68 | 158 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.3d ago |
| 6 | 41 | Almanac | 69.9 | 1.0 | 12.92 | 48.01 | cpu-small | 0.652 | 75 | 65% | SCORING_COMMIT 3.9d ago |
| 7 | 96 | Verathos | 69.6 | 1.0 | 29.70 | 279 | rtx4090 | 0.408 | 64 | 41% | RELEASE 2.0d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 567 | 2,292 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.9d ago |
| 9 | 15 | ORO | 69.0 | 1.0 | 12.68 | 21.17 | cpu-small | 0.000 | 64 | 94% | SCORING_COMMIT 2.9d ago |
| 10 | 85 | Vidaio | 68.7 | 0.85 | 508 | 716 | rtx4090 | 0.000 | 10 | 23% | SCORING_COMMIT 0.1d ago |
| 11 | 56 | Gradients | 68.7 | 0.85 | 506 | 963 | rtx4090 | 0.678 | 7 | 68% | SCORING_COMMIT 4.2d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 477 | 2,210 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.9d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.68 | 34.42 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.3d ago |
| 14 | 11 | TrajectoryRL | 67.2 | 0.85 | 4,267 | 4,267 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 98.31 | 1,344 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.1d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 225 | 723 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.2d ago |
| 17 | 2 | DSperse | 61.6 | 0.85 | 59.38 | 143 | rtx4090 | 0.822 | 6 | 82% | RELEASE 6.0d ago |
| 18 | 55 | NIOME | 61.4 | 0.85 | 55.66 | 480 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.0d ago |
| 19 | 28 | gm | 60.3 | 0.85 | 41.70 | 2,267 | rtx4090 | 0.122 | 42 | 26% | RELEASE 4.2d ago |
| 20 | 60 | Bitsec.ai | 59.0 | 0.85 | 376 | 376 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 21 | 74 | Gittensor | 58.4 | 0.85 | 24.99 | 209 | rtx4090 | 0.631 | 14 | 63% | RELEASE 5.1d ago |
| 22 | 51 | lium.io | 57.8 | 0.85 | 25.97 | 2,530 | rtx4090 | 0.000 | 53 | 77% | SCORING_COMMIT 2.4d ago |
| 23 | 61 | RedTeam | 57.0 | 0.85 | 14.64 | 407 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.5d ago |
| 24 | 120 | Affine | 55.1 | 0.6 | 8,284 | 8,284 | rtx4090 | 0.250 | 4 | 25% | SCORING_COMMIT 4.2d ago |
| 25 | 68 | NOVA | 55.1 | 0.6 | 8,097 | 8,097 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 244.56113766108678 |
| 54 | Yanez | -4.06 | a4000 | 951.8712783900847 |
| 104 | Masx.ai | -0.17 | rtx4090 | 9.189365442454081 |
| 75 | Hippius | -7.38 | rtx4090 | 10892.289228886411 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 134.67442320542685 |
| 101 | Tag101 | -0.03 | cpu-small | 1.9560348485149563 |
| 13 | Data Universe | -3.46 | rtx4090 | 5.870948412937701 |
| 88 | Investing | -5.46 | rtx4090 | 1112.4854003061823 |
| 8 | Vanta | -7.70 | rtx4090 | 2919.400765172055 |
| 114 | SOMA | -8.13 | rtx4090 | 616.0102177090897 |
| 43 | Graphite | -0.78 | cpu-small | 16.61293274340533 |
| 45 | AlphaRidge.ai | -2.59 | rtx4090 | 25.080835426442146 |
| 18 | Zeus | -3.44 | rtx4090 | 1401.5738979505754 |
| 22 | Desearch | -4.30 | rtx4090 | 80.80343523787796 |
| 123 | MANTIS | -6.18 | rtx4090 | 75.00962997155018 |
| 19 | blockmachine | -7.03 | rtx4090 | 465.196150598914 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07605883787380703 |
| 105 | Beam | -2.95 | rtx4090 | 110.91759494702357 |
| 84 | ansuz | -8.16 | rtx4090 | 441.102878433428 |
| 34 | BitMind | -20.58 | a100-80 | 22.30752323502482 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.9 | 35.0 | 15.0 | 9.45 | 1.0 |
| 67 | 12.67 | 35.0 | 15.0 | 9.9 | 1.0 |
| 26 | 14.74 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 76 | 10.03 | 35.0 | 15.0 | 10.0 | 1.0 |
| 41 | 10.4 | 35.0 | 15.0 | 9.49 | 1.0 |
| 96 | 13.53 | 35.0 | 11.25 | 9.78 | 1.0 |
| 91 | 25.05 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.33 | 35.0 | 15.0 | 8.66 | 1.0 |
| 85 | 24.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.54 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 33.02 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.16 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.42 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 16.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 15.95 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.83 | 35.0 | 11.25 | 9.84 | 0.85 |
| 60 | 23.43 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.87 | 35.0 | 11.25 | 9.6 | 0.85 |
| 51 | 13.01 | 35.0 | 11.25 | 8.73 | 0.85 |
| 61 | 10.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.64 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.55 | 35.0 | 11.25 | 10.0 | 0.6 |
