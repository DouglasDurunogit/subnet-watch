# RANKING - generated 2026-08-16T21:00:42Z, block 8859773

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
| 1 | 107 | Minos | 78.3 | 1.0 | 118 | 34,052 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.2d ago |
| 2 | 67 | Harnyx | 72.6 | 1.0 | 23.61 | 418 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.6d ago |
| 3 | 96 | Verathos | 71.2 | 1.0 | 44.22 | 372 | rtx4090 | 0.415 | 46 | 42% | RELEASE 2.0d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.57 | 345 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.2d ago |
| 5 | 1 | Apex | 70.0 | 0.85 | 742 | 1,026 | rtx4090 | 0.562 | 4 | 56% | RELEASE 3.3d ago |
| 6 | 41 | Almanac | 69.9 | 1.0 | 12.81 | 47.85 | cpu-small | 0.653 | 75 | 65% | SCORING_COMMIT 3.9d ago |
| 7 | 76 | Phylax | 69.5 | 1.0 | 9.99 | 103 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 0.4d ago |
| 8 | 85 | Vidaio | 69.2 | 0.85 | 587 | 587 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 0.2d ago |
| 9 | 91 | cascade | 69.1 | 0.85 | 565 | 2,285 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.9d ago |
| 10 | 15 | ORO | 69.0 | 1.0 | 12.52 | 21.25 | cpu-small | 0.000 | 65 | 94% | SCORING_COMMIT 3.0d ago |
| 11 | 56 | Gradients | 68.7 | 0.85 | 504 | 960 | rtx4090 | 0.679 | 7 | 68% | SCORING_COMMIT 4.3d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 476 | 2,204 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.9d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.65 | 34.31 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.4d ago |
| 14 | 38 | ChronoLLM | 66.0 | 0.85 | 98.01 | 1,340 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.2d ago |
| 15 | 124 | Swarm | 65.9 | 0.85 | 225 | 721 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.2d ago |
| 16 | 55 | NIOME | 61.4 | 0.85 | 56.58 | 478 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.0d ago |
| 17 | 28 | gm | 60.1 | 0.85 | 39.62 | 2,588 | rtx4090 | 0.083 | 42 | 30% | RELEASE 4.3d ago |
| 18 | 60 | Bitsec.ai | 59.0 | 0.85 | 378 | 378 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 19 | 74 | Gittensor | 58.2 | 0.85 | 23.62 | 209 | rtx4090 | 0.631 | 14 | 63% | RELEASE 5.1d ago |
| 20 | 51 | lium.io | 57.2 | 0.85 | 22.60 | 2,520 | rtx4090 | 0.000 | 57 | 77% | SCORING_COMMIT 2.5d ago |
| 21 | 61 | RedTeam | 57.0 | 0.85 | 14.65 | 407 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.5d ago |
| 22 | 120 | Affine | 55.1 | 0.6 | 8,259 | 8,259 | rtx4090 | 0.250 | 4 | 25% | SCORING_COMMIT 4.3d ago |
| 23 | 68 | NOVA | 55.1 | 0.6 | 8,073 | 8,073 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.3d ago |
| 24 | 93 | Bitcast | 54.3 | 0.85 | 241 | 435 | rtx4090 | 0.000 | 4 | 85% | SCORING_COMMIT 18d ago |
| 25 | 80 | OpenRoboto | 53.0 | 0.85 | 164 | 593 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 246.0684887966765 |
| 54 | Yanez | -4.02 | a4000 | 948.7868202856628 |
| 104 | Masx.ai | -0.32 | rtx4090 | 11.671659103107146 |
| 75 | Hippius | -7.38 | rtx4090 | 10859.16775810566 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 134.2372870234715 |
| 101 | Tag101 | -0.03 | cpu-small | 1.9082082955588595 |
| 13 | Data Universe | -3.48 | rtx4090 | 5.791436488399528 |
| 88 | Investing | -5.55 | rtx4090 | 1075.0373984613848 |
| 8 | Vanta | -7.70 | rtx4090 | 2909.424440003432 |
| 114 | SOMA | -8.13 | rtx4090 | 614.1949785599573 |
| 43 | Graphite | -0.78 | cpu-small | 16.563787341765007 |
| 45 | AlphaRidge.ai | -2.46 | rtx4090 | 19.05704356567138 |
| 22 | Desearch | -3.36 | rtx4090 | 50.64684003970687 |
| 18 | Zeus | -3.46 | rtx4090 | 1397.0325765929342 |
| 123 | MANTIS | -6.17 | rtx4090 | 75.04042076148397 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07582087264869453 |
| 105 | Beam | -2.97 | rtx4090 | 110.55229515998865 |
| 84 | ansuz | -8.16 | rtx4090 | 439.5836049237425 |
| 34 | BitMind | -20.93 | a100-80 | 23.087611649979316 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.86 | 35.0 | 15.0 | 9.45 | 1.0 |
| 67 | 12.65 | 35.0 | 15.0 | 9.91 | 1.0 |
| 96 | 15.06 | 35.0 | 11.25 | 9.85 | 1.0 |
| 26 | 14.72 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.37 | 35.0 | 15.0 | 9.49 | 1.0 |
| 76 | 9.47 | 35.0 | 15.0 | 10.0 | 1.0 |
| 85 | 25.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.04 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.29 | 35.0 | 15.0 | 8.72 | 1.0 |
| 56 | 24.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.52 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.15 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.4 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.63 | 35.0 | 11.25 | 9.83 | 0.85 |
| 60 | 23.46 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.65 | 35.0 | 11.25 | 9.58 | 0.85 |
| 51 | 12.49 | 35.0 | 11.25 | 8.55 | 0.85 |
| 61 | 10.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.63 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.54 | 35.0 | 11.25 | 10.0 | 0.6 |
| 93 | 21.69 | 21.0 | 11.25 | 10.0 | 0.85 |
| 80 | 20.16 | 21.0 | 11.25 | 10.0 | 0.85 |
