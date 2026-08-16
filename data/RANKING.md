# RANKING - generated 2026-08-16T18:43:31Z, block 8859087

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
| 1 | 107 | Minos | 78.2 | 1.0 | 115 | 33,457 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.1d ago |
| 2 | 67 | Harnyx | 72.5 | 1.0 | 23.53 | 416 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.5d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.52 | 74.35 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.1d ago |
| 4 | 1 | Apex | 70.0 | 0.85 | 750 | 1,036 | rtx4090 | 0.557 | 4 | 56% | RELEASE 3.2d ago |
| 5 | 41 | Almanac | 69.9 | 1.0 | 12.79 | 47.76 | cpu-small | 0.653 | 75 | 65% | SCORING_COMMIT 3.8d ago |
| 6 | 76 | Phylax | 69.9 | 1.0 | 11.36 | 154 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.3d ago |
| 7 | 96 | Verathos | 69.8 | 1.0 | 31.20 | 269 | rtx4090 | 0.409 | 62 | 41% | RELEASE 1.9d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 564 | 2,282 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.8d ago |
| 9 | 85 | Vidaio | 68.8 | 0.85 | 516 | 683 | rtx4090 | 0.000 | 10 | 22% | SCORING_COMMIT 0.1d ago |
| 10 | 15 | ORO | 68.8 | 1.0 | 12.62 | 20.86 | cpu-small | 0.000 | 64 | 94% | SCORING_COMMIT 2.9d ago |
| 11 | 56 | Gradients | 68.7 | 0.85 | 504 | 959 | rtx4090 | 0.678 | 7 | 68% | SCORING_COMMIT 4.2d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 475 | 2,200 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.8d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.64 | 34.27 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.3d ago |
| 14 | 11 | TrajectoryRL | 67.1 | 0.85 | 4,139 | 4,139 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.87 | 1,338 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.1d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 225 | 721 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.1d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.72 | 479 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.9d ago |
| 18 | 28 | gm | 61.1 | 0.85 | 52.74 | 2,648 | rtx4090 | 0.045 | 41 | 30% | RELEASE 4.2d ago |
| 19 | 2 | DSperse | 60.7 | 0.85 | 45.86 | 143 | rtx4090 | 0.822 | 6 | 82% | RELEASE 5.9d ago |
| 20 | 102 | ConnitoAI | 59.8 | 0.85 | 1,229 | 1,423 | rtx4090 | 0.250 | 5 | 27% | RELEASE 16d ago |
| 21 | 60 | Bitsec.ai | 59.0 | 0.85 | 373 | 373 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 22 | 51 | lium.io | 58.5 | 0.85 | 30.49 | 2,503 | rtx4090 | 0.000 | 53 | 77% | SCORING_COMMIT 2.4d ago |
| 23 | 74 | Gittensor | 58.4 | 0.85 | 24.88 | 209 | rtx4090 | 0.631 | 14 | 63% | RELEASE 5.0d ago |
| 24 | 61 | RedTeam | 57.0 | 0.85 | 14.29 | 401 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.4d ago |
| 25 | 120 | Affine | 55.1 | 0.6 | 8,371 | 8,371 | rtx4090 | 0.254 | 4 | 25% | SCORING_COMMIT 4.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 243.48315508352195 |
| 54 | Yanez | -3.90 | a4000 | 947.6118800789666 |
| 104 | Masx.ai | -0.67 | rtx4090 | 10.616900973802812 |
| 75 | Hippius | -7.38 | rtx4090 | 10845.507830776232 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 133.90042759709087 |
| 101 | Tag101 | -0.03 | cpu-small | 1.9882888493745197 |
| 13 | Data Universe | -3.43 | rtx4090 | 5.838892082401865 |
| 88 | Investing | -5.46 | rtx4090 | 1111.6661356603383 |
| 8 | Vanta | -7.70 | rtx4090 | 2908.5547916479068 |
| 114 | SOMA | -8.13 | rtx4090 | 613.2344570179042 |
| 43 | Graphite | -0.78 | cpu-small | 16.680871469817177 |
| 45 | AlphaRidge.ai | -2.45 | rtx4090 | 21.07603418563791 |
| 22 | Desearch | -2.99 | rtx4090 | 53.164669894037104 |
| 18 | Zeus | -3.46 | rtx4090 | 1395.5451655318818 |
| 123 | MANTIS | -6.19 | rtx4090 | 74.68698336877178 |
| 19 | blockmachine | -7.08 | rtx4090 | 436.8930887530127 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07572506638064537 |
| 105 | Beam | -3.01 | rtx4090 | 114.72455620380012 |
| 84 | ansuz | -8.16 | rtx4090 | 439.27388411276763 |
| 34 | BitMind | -20.09 | a100-80 | 21.461611760836046 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.79 | 35.0 | 15.0 | 9.44 | 1.0 |
| 67 | 12.64 | 35.0 | 15.0 | 9.86 | 1.0 |
| 26 | 14.72 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.37 | 35.0 | 15.0 | 9.49 | 1.0 |
| 76 | 9.93 | 35.0 | 15.0 | 10.0 | 1.0 |
| 96 | 13.71 | 35.0 | 11.25 | 9.79 | 1.0 |
| 91 | 25.03 | 35.0 | 11.25 | 9.99 | 0.85 |
| 85 | 24.68 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 10.31 | 35.0 | 15.0 | 8.5 | 1.0 |
| 56 | 24.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.35 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.52 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 32.9 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.15 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.4 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.74 | 35.0 | 11.25 | 9.88 | 0.85 |
| 2 | 15.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 28.1 | 21.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.4 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 13.63 | 35.0 | 11.25 | 8.92 | 0.85 |
| 74 | 12.85 | 35.0 | 11.25 | 9.6 | 0.85 |
| 61 | 10.77 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.68 | 35.0 | 11.25 | 9.99 | 0.6 |
