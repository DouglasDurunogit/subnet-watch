# RANKING - generated 2026-08-16T17:02:56Z, block 8858584

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
| 1 | 107 | Minos | 78.2 | 1.0 | 114 | 34,147 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.1d ago |
| 2 | 67 | Harnyx | 72.5 | 1.0 | 23.56 | 417 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.5d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.58 | 74.43 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.1d ago |
| 4 | 1 | Apex | 70.1 | 0.85 | 757 | 1,045 | rtx4090 | 0.554 | 4 | 55% | RELEASE 3.1d ago |
| 5 | 96 | Verathos | 70.0 | 1.0 | 32.93 | 261 | rtx4090 | 0.409 | 60 | 41% | RELEASE 1.9d ago |
| 6 | 76 | Phylax | 70.0 | 1.0 | 11.48 | 155 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.2d ago |
| 7 | 41 | Almanac | 69.9 | 1.0 | 12.85 | 47.81 | cpu-small | 0.652 | 75 | 65% | SCORING_COMMIT 3.8d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 564 | 2,282 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.7d ago |
| 9 | 85 | Vidaio | 68.7 | 0.85 | 508 | 676 | rtx4090 | 0.000 | 10 | 22% | SCORING_COMMIT 0.0d ago |
| 10 | 56 | Gradients | 68.7 | 0.85 | 504 | 960 | rtx4090 | 0.678 | 7 | 68% | SCORING_COMMIT 4.1d ago |
| 11 | 62 | Ridges | 68.5 | 0.85 | 475 | 2,201 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.8d ago |
| 12 | 15 | ORO | 68.4 | 1.0 | 12.72 | 21.03 | cpu-small | 0.000 | 62 | 94% | SCORING_COMMIT 2.8d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.65 | 34.31 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.2d ago |
| 14 | 11 | TrajectoryRL | 67.1 | 0.85 | 4,133 | 4,133 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 96.79 | 1,323 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.0d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 720 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.1d ago |
| 17 | 2 | DSperse | 64.3 | 0.85 | 133 | 195 | rtx4090 | 0.822 | 4 | 82% | RELEASE 5.9d ago |
| 18 | 55 | NIOME | 61.4 | 0.85 | 55.92 | 485 | rtx4090 | 0.020 | 11 | 30% | SCORING_COMMIT 1.9d ago |
| 19 | 60 | Bitsec.ai | 59.2 | 0.85 | 393 | 393 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 20 | 28 | gm | 58.8 | 0.85 | 26.81 | 2,380 | rtx4090 | 0.216 | 40 | 27% | RELEASE 4.1d ago |
| 21 | 74 | Gittensor | 58.5 | 0.85 | 25.68 | 209 | rtx4090 | 0.631 | 14 | 63% | RELEASE 4.9d ago |
| 22 | 51 | lium.io | 57.9 | 0.85 | 27.20 | 2,493 | rtx4090 | 0.000 | 53 | 77% | SCORING_COMMIT 2.3d ago |
| 23 | 61 | RedTeam | 57.2 | 0.85 | 15.22 | 418 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.4d ago |
| 24 | 120 | Affine | 55.2 | 0.6 | 8,663 | 8,663 | rtx4090 | 0.261 | 4 | 26% | SCORING_COMMIT 4.1d ago |
| 25 | 68 | NOVA | 55.1 | 0.6 | 8,049 | 8,049 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 243.74513531854467 |
| 54 | Yanez | -3.96 | a4000 | 948.5914665168809 |
| 104 | Masx.ai | -0.28 | rtx4090 | 8.657675451408922 |
| 75 | Hippius | -7.38 | rtx4090 | 10906.317270231828 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 135.3829336900403 |
| 101 | Tag101 | -0.07 | cpu-small | 1.9914116626322607 |
| 13 | Data Universe | -3.59 | rtx4090 | 6.067062174014623 |
| 88 | Investing | -5.42 | rtx4090 | 1130.3960592404667 |
| 8 | Vanta | -7.70 | rtx4090 | 2909.898290559397 |
| 114 | SOMA | -8.13 | rtx4090 | 602.7569600021093 |
| 43 | Graphite | -0.78 | cpu-small | 16.559776416084095 |
| 32 | ItsAI | -0.08 | rtx4090 | 10.655826407663273 |
| 18 | Zeus | -3.46 | rtx4090 | 1397.2991070440958 |
| 22 | Desearch | -3.58 | rtx4090 | 51.33180890721726 |
| 45 | AlphaRidge.ai | -4.18 | rtx4090 | 17.414994619974024 |
| 123 | MANTIS | -6.19 | rtx4090 | 74.77075346789702 |
| 19 | blockmachine | -7.08 | rtx4090 | 478.701116825092 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07658376664200268 |
| 105 | Beam | -3.02 | rtx4090 | 114.46117228836356 |
| 84 | ansuz | -8.16 | rtx4090 | 439.8835604434605 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.73 | 35.0 | 15.0 | 9.43 | 1.0 |
| 67 | 12.64 | 35.0 | 15.0 | 9.86 | 1.0 |
| 26 | 14.72 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 13.92 | 35.0 | 11.25 | 9.8 | 1.0 |
| 76 | 9.97 | 35.0 | 15.0 | 10.0 | 1.0 |
| 41 | 10.38 | 35.0 | 15.0 | 9.49 | 1.0 |
| 91 | 25.03 | 35.0 | 11.25 | 9.99 | 0.85 |
| 85 | 24.62 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.35 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 10.35 | 35.0 | 15.0 | 8.04 | 1.0 |
| 21 | 8.52 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 32.89 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.1 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.4 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 19.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 15.96 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.61 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.14 | 35.0 | 11.25 | 9.76 | 0.85 |
| 74 | 12.97 | 35.0 | 11.25 | 9.62 | 0.85 |
| 51 | 13.19 | 35.0 | 11.25 | 8.68 | 0.85 |
| 61 | 11.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.81 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.52 | 35.0 | 11.25 | 10.0 | 0.6 |
