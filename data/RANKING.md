# RANKING - generated 2026-08-16T16:00:09Z, block 8858270

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
| 1 | 107 | Minos | 78.4 | 1.0 | 119 | 33,500 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.0d ago |
| 2 | 76 | Phylax | 73.7 | 1.0 | 31.20 | 154 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.2d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.73 | 420 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.4d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.63 | 74.53 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.0d ago |
| 5 | 1 | Apex | 70.1 | 0.85 | 761 | 1,051 | rtx4090 | 0.552 | 4 | 55% | RELEASE 3.1d ago |
| 6 | 96 | Verathos | 70.1 | 1.0 | 33.89 | 209 | rtx4090 | 0.434 | 54 | 43% | RELEASE 1.8d ago |
| 7 | 41 | Almanac | 69.9 | 1.0 | 12.87 | 47.88 | cpu-small | 0.652 | 75 | 65% | SCORING_COMMIT 3.7d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 565 | 2,285 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.7d ago |
| 9 | 15 | ORO | 68.9 | 1.0 | 12.72 | 21.03 | cpu-small | 0.000 | 62 | 94% | SCORING_COMMIT 2.7d ago |
| 10 | 56 | Gradients | 68.7 | 0.85 | 505 | 961 | rtx4090 | 0.677 | 7 | 68% | SCORING_COMMIT 4.1d ago |
| 11 | 85 | Vidaio | 68.6 | 0.85 | 491 | 560 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 4.2d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 476 | 2,204 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.7d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.66 | 34.34 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.2d ago |
| 14 | 11 | TrajectoryRL | 67.1 | 0.85 | 4,126 | 4,126 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 96.88 | 1,325 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.0d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 720 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.0d ago |
| 17 | 2 | DSperse | 64.3 | 0.85 | 134 | 195 | rtx4090 | 0.822 | 4 | 82% | RELEASE 5.8d ago |
| 18 | 55 | NIOME | 61.5 | 0.85 | 57.09 | 482 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.8d ago |
| 19 | 60 | Bitsec.ai | 59.2 | 0.85 | 399 | 399 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 20 | 28 | gm | 58.8 | 0.85 | 26.93 | 2,388 | rtx4090 | 0.216 | 40 | 27% | RELEASE 4.1d ago |
| 21 | 74 | Gittensor | 58.5 | 0.85 | 25.72 | 209 | rtx4090 | 0.631 | 14 | 63% | RELEASE 4.9d ago |
| 22 | 51 | lium.io | 58.3 | 0.85 | 28.90 | 1,461 | rtx4090 | 0.000 | 52 | 82% | SCORING_COMMIT 2.3d ago |
| 23 | 61 | RedTeam | 57.5 | 0.85 | 16.90 | 440 | rtx4090 | 0.000 | 81 | 10% | RELEASE 5.3d ago |
| 24 | 120 | Affine | 55.8 | 0.6 | 11,091 | 11,091 | rtx4090 | 0.333 | 3 | 33% | SCORING_COMMIT 4.1d ago |
| 25 | 68 | NOVA | 55.1 | 0.6 | 8,057 | 8,057 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 244.59741000484118 |
| 54 | Yanez | -4.14 | a4000 | 950.3949830857591 |
| 104 | Masx.ai | -0.42 | rtx4090 | 9.248216414717005 |
| 75 | Hippius | -7.21 | rtx4090 | 10917.121558664663 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 132.74714908348216 |
| 13 | Data Universe | -3.57 | rtx4090 | 6.085368571143386 |
| 88 | Investing | -5.43 | rtx4090 | 1125.7761786638089 |
| 8 | Vanta | -7.70 | rtx4090 | 2912.8290537264434 |
| 114 | SOMA | -8.13 | rtx4090 | 603.3057857510377 |
| 43 | Graphite | -0.78 | cpu-small | 17.417418376194057 |
| 32 | ItsAI | -0.06 | rtx4090 | 10.695942360865674 |
| 18 | Zeus | -3.45 | rtx4090 | 1398.9341393452328 |
| 22 | Desearch | -3.57 | rtx4090 | 51.391853480351486 |
| 45 | AlphaRidge.ai | -4.03 | rtx4090 | 14.641558546817409 |
| 123 | MANTIS | -6.18 | rtx4090 | 75.37679545475666 |
| 19 | blockmachine | -7.08 | rtx4090 | 479.2255615226081 |
| 63 | Enigma | -8.14 | rtx4090 | 5024.846071456442 |
| 105 | Beam | -3.03 | rtx4090 | 110.67952959237148 |
| 84 | ansuz | -8.16 | rtx4090 | 440.4722862668012 |
| 34 | BitMind | -19.75 | a100-80 | 20.97020089348871 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.9 | 35.0 | 15.0 | 9.45 | 1.0 |
| 76 | 13.71 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.67 | 35.0 | 15.0 | 9.87 | 1.0 |
| 26 | 14.73 | 35.0 | 11.25 | 9.83 | 1.0 |
| 1 | 26.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 14.03 | 35.0 | 11.25 | 9.81 | 1.0 |
| 41 | 10.39 | 35.0 | 15.0 | 9.49 | 1.0 |
| 91 | 25.04 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.34 | 35.0 | 15.0 | 8.57 | 1.0 |
| 56 | 24.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.53 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 32.88 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.11 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.4 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 19.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.66 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.15 | 35.0 | 11.25 | 9.76 | 0.85 |
| 74 | 12.98 | 35.0 | 11.25 | 9.62 | 0.85 |
| 51 | 13.42 | 35.0 | 11.25 | 8.86 | 0.85 |
| 61 | 11.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 36.79 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.53 | 35.0 | 11.25 | 10.0 | 0.6 |
