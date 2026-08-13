# RANKING - generated 2026-08-13T21:22:50Z, block 8838285

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
| 1 | 107 | Minos | 78.1 | 1.0 | 112 | 31,881 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 3.3d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.07 | 192 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 5.0d ago |
| 3 | 67 | Harnyx | 71.3 | 1.0 | 17.37 | 714 | cpu-small | 0.019 | 148 | 19% | SCORING_COMMIT 0.4d ago |
| 4 | 1 | Apex | 70.5 | 0.85 | 850 | 1,174 | rtx4090 | 0.546 | 4 | 55% | RELEASE 0.3d ago |
| 5 | 91 | cascade | 69.8 | 0.85 | 708 | 2,441 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 2.7d ago |
| 6 | 62 | Ridges | 69.0 | 0.85 | 552 | 1,995 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 1.9d ago |
| 7 | 41 | Almanac | 69.0 | 1.0 | 10.42 | 29.53 | cpu-small | 0.724 | 68 | 72% | SCORING_COMMIT 0.9d ago |
| 8 | 56 | Gradients | 68.9 | 0.85 | 534 | 989 | rtx4090 | 0.654 | 7 | 65% | SCORING_COMMIT 1.3d ago |
| 9 | 26 | Perturb | 68.8 | 1.0 | 24.88 | 848 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 0.2d ago |
| 10 | 38 | ChronoLLM | 67.9 | 0.85 | 166 | 3,482 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.2d ago |
| 11 | 6 | Numinous | 67.9 | 1.0 | 9.65 | 511 | cpu-small | 0.000 | 19 | 29% | WEIGHTS_VERSION_BUMP 0.2d ago |
| 12 | 21 | AdTAO | 67.7 | 1.0 | 7.69 | 34.48 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 2.4d ago |
| 13 | 96 | Verathos | 67.1 | 1.0 | 16.23 | 277 | rtx4090 | 0.408 | 76 | 41% | RELEASE 1.3d ago |
| 14 | 124 | Swarm | 66.0 | 0.85 | 230 | 741 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 2.3d ago |
| 15 | 80 | OpenRoboto | 65.2 | 0.85 | 176 | 637 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 5.7d ago |
| 16 | 85 | Vidaio | 64.3 | 0.85 | 136 | 798 | rtx4090 | 0.000 | 10 | 24% | SCORING_COMMIT 1.5d ago |
| 17 | 102 | ConnitoAI | 60.5 | 0.85 | 1,529 | 1,536 | rtx4090 | 0.251 | 4 | 25% | RELEASE 13d ago |
| 18 | 28 | gm | 60.1 | 0.85 | 39.61 | 2,205 | rtx4090 | 0.198 | 31 | 23% | RELEASE 1.3d ago |
| 19 | 51 | lium.io | 58.9 | 0.85 | 33.81 | 2,200 | rtx4090 | 0.000 | 48 | 73% | RELEASE 0.2d ago |
| 20 | 74 | Gittensor | 58.1 | 0.85 | 23.27 | 218 | rtx4090 | 0.631 | 14 | 63% | RELEASE 2.1d ago |
| 21 | 61 | RedTeam | 57.8 | 0.85 | 18.50 | 1,630 | rtx4090 | 0.000 | 66 | 35% | RELEASE 2.6d ago |
| 22 | 2 | DSperse | 56.1 | 0.85 | 10.85 | 83.10 | rtx4090 | 0.828 | 13 | 83% | RELEASE 3.0d ago |
| 23 | 15 | ORO | 54.8 | 1.0 | 13.00 | 23.44 | cpu-small | 0.000 | 79 | 93% | RELEASE 7d ago |
| 24 | 120 | Affine | 54.7 | 0.6 | 6,985 | 6,985 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.3d ago |
| 25 | 97 | Albedo | 52.7 | 0.6 | 2,997 | 2,997 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.74 | a4000 | 973.4031052209963 |
| 75 | Hippius | -7.32 | rtx4090 | 11706.168956939338 |
| 114 | SOMA | -8.11 | rtx4090 | 704.0820662190604 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 169.36626404867673 |
| 13 | Data Universe | -3.10 | rtx4090 | 5.832928332334454 |
| 88 | Investing | -5.25 | rtx4090 | 659.3177288109952 |
| 8 | Vanta | -7.95 | rtx4090 | 3317.4904148024625 |
| 43 | Graphite | -0.65 | cpu-small | 39.77572690011506 |
| 32 | ItsAI | -0.04 | rtx4090 | 11.865729690065054 |
| 22 | Desearch | -2.08 | rtx4090 | 119.49170690539147 |
| 19 | blockmachine | -2.29 | rtx4090 | 306.35875083708567 |
| 18 | Zeus | -5.09 | rtx4090 | 1314.2041777004306 |
| 45 | AlphaRidge.ai | -5.10 | rtx4090 | 14.433229724418284 |
| 123 | MANTIS | -6.01 | rtx4090 | 83.43004989601961 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0772085392791458 |
| 105 | Beam | -2.23 | rtx4090 | 84.23097217819742 |
| 84 | ansuz | -8.15 | rtx4090 | 470.16143480723036 |
| 34 | BitMind | -19.62 | a100-80 | 295.4273731283145 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.69 | 35.0 | 15.0 | 9.4 | 1.0 |
| 76 | 14.67 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 11.5 | 35.0 | 15.0 | 9.79 | 1.0 |
| 1 | 26.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.93 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 24.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.62 | 35.0 | 15.0 | 9.35 | 1.0 |
| 56 | 24.81 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.85 | 35.0 | 11.25 | 9.73 | 1.0 |
| 38 | 20.22 | 35.0 | 15.0 | 9.7 | 0.85 |
| 6 | 9.35 | 35.0 | 15.0 | 8.6 | 1.0 |
| 21 | 8.54 | 35.0 | 15.0 | 9.12 | 1.0 |
| 96 | 11.24 | 35.0 | 11.25 | 9.58 | 1.0 |
| 124 | 21.49 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 20.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 28.97 | 21.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.63 | 35.0 | 11.25 | 9.83 | 0.85 |
| 51 | 14.02 | 35.0 | 11.25 | 9.0 | 0.85 |
| 74 | 12.6 | 35.0 | 11.25 | 9.56 | 0.85 |
| 61 | 11.73 | 35.0 | 11.25 | 9.99 | 0.85 |
| 2 | 9.76 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 10.42 | 21.0 | 15.0 | 8.39 | 1.0 |
| 120 | 34.96 | 35.0 | 11.25 | 9.99 | 0.6 |
| 97 | 31.62 | 35.0 | 11.25 | 9.97 | 0.6 |
