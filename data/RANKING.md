# RANKING - generated 2026-08-12T18:40:22Z, block 8830273

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
| 1 | 107 | Minos | 78.0 | 1.0 | 111 | 31,080 | cpu-small | 0.000 | 20 | 89% | README_TASK_DIFF 2.1d ago |
| 2 | 76 | Phylax | 76.4 | 1.0 | 62.35 | 189 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 3.9d ago |
| 3 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,750 | 1,750 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 5.5d ago |
| 4 | 114 | SOMA | 71.5 | 0.85 | 1,165 | 4,349 | rtx4090 | 0.000 | 4 | 65% | SCORING_COMMIT 5.4d ago |
| 5 | 67 | Harnyx | 71.4 | 1.0 | 17.99 | 749 | cpu-small | 0.038 | 131 | 20% | SCORING_COMMIT 0.3d ago |
| 6 | 91 | cascade | 70.1 | 0.85 | 766 | 2,624 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.6d ago |
| 7 | 96 | Verathos | 69.3 | 1.0 | 28.14 | 323 | rtx4090 | 0.415 | 60 | 42% | RELEASE 0.2d ago |
| 8 | 41 | Almanac | 69.1 | 1.0 | 10.68 | 23.85 | cpu-small | 0.718 | 69 | 72% | SCORING_COMMIT 5.8d ago |
| 9 | 62 | Ridges | 69.0 | 0.85 | 548 | 1,981 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 0.8d ago |
| 10 | 56 | Gradients | 68.9 | 0.85 | 535 | 981 | rtx4090 | 0.645 | 7 | 65% | SCORING_COMMIT 0.2d ago |
| 11 | 100 | BASE | 68.4 | 0.85 | 465 | 1,886 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.3d ago |
| 12 | 26 | Perturb | 67.9 | 1.0 | 19.64 | 172 | rtx3060 | 0.508 | 11 | 51% | SCORING_COMMIT 6.2d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.50 | 33.68 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 1.3d ago |
| 14 | 11 | TrajectoryRL | 67.1 | 0.85 | 4,220 | 4,220 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 10d ago |
| 15 | 15 | ORO | 66.2 | 1.0 | 8.77 | 20.88 | cpu-small | 0.000 | 68 | 94% | RELEASE 6.3d ago |
| 16 | 124 | Swarm | 65.8 | 0.85 | 220 | 667 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 1.1d ago |
| 17 | 80 | OpenRoboto | 65.0 | 0.85 | 168 | 610 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 4.6d ago |
| 18 | 38 | ChronoLLM | 64.6 | 0.85 | 161 | 3,523 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 4.4d ago |
| 19 | 85 | Vidaio | 64.1 | 0.85 | 125 | 480 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 0.3d ago |
| 20 | 28 | gm | 61.4 | 0.85 | 58.03 | 2,742 | rtx4090 | 0.085 | 32 | 28% | RELEASE 0.2d ago |
| 21 | 51 | lium.io | 60.4 | 0.85 | 49.64 | 1,991 | rtx4090 | 0.000 | 47 | 75% | RELEASE 0.3d ago |
| 22 | 2 | DSperse | 59.4 | 0.85 | 30.84 | 93.65 | rtx4090 | 0.826 | 14 | 83% | RELEASE 1.9d ago |
| 23 | 74 | Gittensor | 58.5 | 0.85 | 25.39 | 216 | rtx4090 | 0.630 | 13 | 63% | RELEASE 1.0d ago |
| 24 | 61 | RedTeam | 58.3 | 0.85 | 21.76 | 1,637 | rtx4090 | 0.000 | 60 | 35% | RELEASE 1.4d ago |
| 25 | 102 | ConnitoAI | 57.8 | 0.85 | 687 | 1,603 | rtx4090 | 0.251 | 7 | 26% | RELEASE 12d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.56 | a4000 | 1010.8441872411739 |
| 104 | Masx.ai | -0.90 | rtx4090 | 19.083280048338032 |
| 13 | Data Universe | -3.12 | rtx4090 | 5.777177169124895 |
| 88 | Investing | -5.00 | rtx4090 | 643.2455997290139 |
| 75 | Hippius | -7.70 | rtx4090 | 11273.46980647558 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 141.5915302944934 |
| 8 | Vanta | -7.95 | rtx4090 | 3280.4143309361943 |
| 18 | Zeus | -3.39 | rtx4090 | 1857.8292465328955 |
| 123 | MANTIS | -6.09 | rtx4090 | 80.85313062273836 |
| 45 | AlphaRidge.ai | -6.20 | rtx4090 | 9.99317487659274 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07482311272978462 |
| 105 | Beam | -2.09 | rtx4090 | 83.5176342122784 |
| 84 | ansuz | -8.15 | rtx4090 | 484.22551213068687 |
| 34 | BitMind | -19.54 | a100-80 | 291.21523589839217 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn55, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn94, sn95, sn108, sn109, sn111, sn113, sn115, sn116, sn118, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.64 | 35.0 | 15.0 | 9.41 | 1.0 |
| 76 | 16.39 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.5 | 35.0 | 15.0 | 10.0 | 0.85 |
| 114 | 27.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 11.63 | 35.0 | 15.0 | 9.77 | 1.0 |
| 91 | 26.24 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 13.32 | 35.0 | 11.25 | 9.76 | 1.0 |
| 41 | 9.71 | 35.0 | 15.0 | 9.37 | 1.0 |
| 62 | 24.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.82 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 24.27 | 35.0 | 11.25 | 9.99 | 0.85 |
| 26 | 11.96 | 35.0 | 11.25 | 9.66 | 1.0 |
| 21 | 8.45 | 35.0 | 15.0 | 9.11 | 1.0 |
| 11 | 32.97 | 21.0 | 15.0 | 10.0 | 0.85 |
| 15 | 9.0 | 35.0 | 15.0 | 7.2 | 1.0 |
| 124 | 21.33 | 35.0 | 11.25 | 9.83 | 0.85 |
| 80 | 20.27 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 20.11 | 35.0 | 11.25 | 9.69 | 0.85 |
| 85 | 19.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.11 | 35.0 | 11.25 | 9.88 | 0.85 |
| 51 | 15.5 | 35.0 | 11.25 | 9.33 | 0.85 |
| 2 | 13.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.93 | 35.0 | 11.25 | 9.61 | 0.85 |
| 61 | 12.34 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 25.81 | 21.0 | 11.25 | 10.0 | 0.85 |
