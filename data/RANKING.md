# RANKING - generated 2026-08-12T22:56:42Z, block 8831554

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
| 1 | 76 | Phylax | 78.7 | 1.0 | 111 | 374 | cpu-small | 0.000 | 10 | 27% | SCORING_COMMIT 4.0d ago |
| 2 | 107 | Minos | 77.8 | 1.0 | 105 | 31,053 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 2.3d ago |
| 3 | 67 | Harnyx | 71.5 | 1.0 | 17.93 | 746 | cpu-small | 0.038 | 131 | 20% | SCORING_COMMIT 0.4d ago |
| 4 | 96 | Verathos | 71.1 | 1.0 | 43.55 | 375 | rtx4090 | 0.417 | 49 | 42% | RELEASE 0.4d ago |
| 5 | 91 | cascade | 70.1 | 0.85 | 762 | 2,627 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.8d ago |
| 6 | 114 | SOMA | 69.6 | 0.85 | 667 | 4,384 | rtx4090 | 0.000 | 4 | 65% | SCORING_COMMIT 5.6d ago |
| 7 | 41 | Almanac | 69.1 | 1.0 | 10.61 | 29.75 | cpu-small | 0.715 | 68 | 72% | SCORING_COMMIT 0.0d ago |
| 8 | 62 | Ridges | 69.0 | 0.85 | 545 | 1,974 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 1.0d ago |
| 9 | 56 | Gradients | 68.9 | 0.85 | 532 | 977 | rtx4090 | 0.647 | 7 | 65% | SCORING_COMMIT 0.4d ago |
| 10 | 100 | BASE | 68.3 | 0.85 | 443 | 1,796 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.5d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.31 | 36.65 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 6.3d ago |
| 12 | 21 | AdTAO | 67.6 | 1.0 | 7.49 | 33.63 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 1.5d ago |
| 13 | 15 | ORO | 67.3 | 1.0 | 9.07 | 12,316 | cpu-small | 0.000 | 69 | 94% | RELEASE 6.5d ago |
| 14 | 11 | TrajectoryRL | 67.1 | 0.85 | 4,185 | 4,185 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 10d ago |
| 15 | 124 | Swarm | 66.4 | 0.85 | 264 | 690 | rtx4090 | 0.000 | 21 | 12% | SCORING_COMMIT 1.3d ago |
| 16 | 80 | OpenRoboto | 64.9 | 0.85 | 162 | 587 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 4.7d ago |
| 17 | 38 | ChronoLLM | 64.6 | 0.85 | 160 | 3,502 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 4.5d ago |
| 18 | 85 | Vidaio | 63.9 | 0.85 | 119 | 495 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 0.5d ago |
| 19 | 28 | gm | 62.8 | 0.85 | 88.73 | 2,671 | rtx4090 | 0.079 | 30 | 27% | RELEASE 0.4d ago |
| 20 | 51 | lium.io | 60.4 | 0.85 | 49.94 | 2,261 | rtx4090 | 0.000 | 46 | 71% | RELEASE 0.5d ago |
| 21 | 102 | ConnitoAI | 59.5 | 0.85 | 1,138 | 1,909 | rtx4090 | 0.250 | 6 | 32% | RELEASE 12d ago |
| 22 | 74 | Gittensor | 58.2 | 0.85 | 23.38 | 215 | rtx4090 | 0.631 | 13 | 63% | RELEASE 1.2d ago |
| 23 | 61 | RedTeam | 58.2 | 0.85 | 21.31 | 1,607 | rtx4090 | 0.000 | 59 | 35% | RELEASE 1.6d ago |
| 24 | 6 | Numinous | 56.3 | 1.0 | 15.79 | 476 | cpu-small | 0.000 | 20 | 26% | README_TASK_DIFF 14d ago |
| 25 | 120 | Affine | 54.7 | 0.6 | 6,924 | 6,924 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.4d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.74 | a4000 | 1002.8331662867283 |
| 2 | DSperse | -1.25 | rtx4090 | 107.7116434528015 |
| 75 | Hippius | -7.71 | rtx4090 | 11088.685431284559 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 139.83133392918074 |
| 13 | Data Universe | -3.16 | rtx4090 | 5.680258622852019 |
| 88 | Investing | -5.05 | rtx4090 | 633.0083910972246 |
| 8 | Vanta | -7.95 | rtx4090 | 3263.0944445712544 |
| 32 | ItsAI | -0.18 | rtx4090 | 11.072152950511505 |
| 19 | blockmachine | -2.23 | rtx4090 | 550.7051158007233 |
| 18 | Zeus | -3.30 | rtx4090 | 1742.0728734653496 |
| 123 | MANTIS | -6.08 | rtx4090 | 81.25326097684938 |
| 45 | AlphaRidge.ai | -6.24 | rtx4090 | 7.306508314277312 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07507061480193743 |
| 105 | Beam | -2.20 | rtx4090 | 81.49367062830204 |
| 84 | ansuz | -8.15 | rtx4090 | 475.70461408232546 |
| 34 | BitMind | -19.79 | a100-80 | 290.24959797435423 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn108, sn109, sn111, sn113, sn115, sn116, sn118, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 18.65 | 35.0 | 15.0 | 10.0 | 1.0 |
| 107 | 18.4 | 35.0 | 15.0 | 9.37 | 1.0 |
| 67 | 11.62 | 35.0 | 15.0 | 9.84 | 1.0 |
| 96 | 15.0 | 35.0 | 11.25 | 9.85 | 1.0 |
| 91 | 26.22 | 35.0 | 11.25 | 9.99 | 0.85 |
| 114 | 25.69 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.69 | 35.0 | 15.0 | 9.37 | 1.0 |
| 62 | 24.9 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 24.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 11.89 | 35.0 | 11.25 | 9.66 | 1.0 |
| 21 | 8.45 | 35.0 | 15.0 | 9.11 | 1.0 |
| 15 | 9.12 | 35.0 | 15.0 | 8.17 | 1.0 |
| 11 | 32.94 | 21.0 | 15.0 | 10.0 | 0.85 |
| 124 | 22.04 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 20.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 20.08 | 35.0 | 11.25 | 9.69 | 0.85 |
| 85 | 18.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 17.76 | 35.0 | 11.25 | 9.92 | 0.85 |
| 51 | 15.53 | 35.0 | 11.25 | 9.33 | 0.85 |
| 102 | 27.8 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.61 | 35.0 | 11.25 | 9.57 | 0.85 |
| 61 | 12.26 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.14 | 21.0 | 15.0 | 9.16 | 1.0 |
| 120 | 34.93 | 35.0 | 11.25 | 9.99 | 0.6 |
