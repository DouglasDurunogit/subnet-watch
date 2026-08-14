# RANKING - generated 2026-08-14T04:30:30Z, block 8840423

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
| 1 | 107 | Minos | 78.5 | 1.0 | 122 | 31,270 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 3.6d ago |
| 2 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,748 | 1,748 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.9d ago |
| 3 | 76 | Phylax | 74.6 | 1.0 | 39.64 | 190 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 5.3d ago |
| 4 | 67 | Harnyx | 73.3 | 1.0 | 28.74 | 489 | cpu-small | 0.034 | 120 | 13% | SCORING_COMMIT 0.7d ago |
| 5 | 1 | Apex | 70.4 | 0.85 | 829 | 1,183 | rtx4090 | 0.554 | 4 | 55% | RELEASE 0.6d ago |
| 6 | 85 | Vidaio | 69.6 | 0.85 | 656 | 656 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 1.7d ago |
| 7 | 91 | cascade | 69.5 | 0.85 | 643 | 2,214 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.2d ago |
| 8 | 41 | Almanac | 69.1 | 1.0 | 10.68 | 26.86 | cpu-small | 0.723 | 68 | 72% | SCORING_COMMIT 1.2d ago |
| 9 | 56 | Gradients | 68.9 | 0.85 | 531 | 987 | rtx4090 | 0.657 | 7 | 66% | SCORING_COMMIT 1.6d ago |
| 10 | 15 | ORO | 68.9 | 1.0 | 12.47 | 12,890 | cpu-small | 0.000 | 79 | 93% | SCORING_COMMIT 0.3d ago |
| 11 | 26 | Perturb | 68.8 | 1.0 | 24.69 | 842 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 0.5d ago |
| 12 | 62 | Ridges | 68.2 | 0.85 | 428 | 1,985 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 2.2d ago |
| 13 | 96 | Verathos | 68.0 | 1.0 | 20.25 | 241 | rtx4090 | 0.408 | 72 | 41% | RELEASE 1.6d ago |
| 14 | 21 | AdTAO | 67.6 | 1.0 | 7.62 | 34.17 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 2.7d ago |
| 15 | 6 | Numinous | 66.7 | 1.0 | 7.54 | 551 | cpu-small | 0.000 | 19 | 32% | WEIGHTS_VERSION_BUMP 0.5d ago |
| 16 | 38 | ChronoLLM | 66.5 | 0.85 | 113 | 1,550 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.5d ago |
| 17 | 124 | Swarm | 65.9 | 0.85 | 228 | 736 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 2.6d ago |
| 18 | 80 | OpenRoboto | 65.3 | 0.85 | 181 | 653 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 6.0d ago |
| 19 | 28 | gm | 61.3 | 0.85 | 56.91 | 2,679 | rtx4090 | 0.121 | 32 | 28% | RELEASE 1.6d ago |
| 20 | 51 | lium.io | 60.0 | 0.85 | 44.68 | 2,169 | rtx4090 | 0.000 | 50 | 72% | RELEASE 0.5d ago |
| 21 | 61 | RedTeam | 57.8 | 0.85 | 18.57 | 1,626 | rtx4090 | 0.000 | 66 | 35% | RELEASE 2.9d ago |
| 22 | 74 | Gittensor | 57.7 | 0.85 | 20.51 | 216 | rtx4090 | 0.631 | 14 | 63% | RELEASE 2.4d ago |
| 23 | 102 | ConnitoAI | 56.2 | 0.85 | 425 | 2,070 | rtx4090 | 0.250 | 7 | 35% | RELEASE 13d ago |
| 24 | 2 | DSperse | 55.4 | 0.85 | 8.53 | 93.79 | rtx4090 | 0.829 | 13 | 83% | RELEASE 3.3d ago |
| 25 | 120 | Affine | 54.7 | 0.6 | 6,871 | 6,871 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.6d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.97 | a4000 | 978.4443024646789 |
| 75 | Hippius | -7.15 | rtx4090 | 11541.529086536204 |
| 114 | SOMA | -8.11 | rtx4090 | 719.160078389476 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 200.18682169874367 |
| 101 | Tag101 | -0.01 | cpu-small | 1.9916327308383606 |
| 13 | Data Universe | -3.22 | rtx4090 | 5.682366402193112 |
| 88 | Investing | -5.14 | rtx4090 | 762.2336972460168 |
| 8 | Vanta | -7.95 | rtx4090 | 3114.363773361187 |
| 43 | Graphite | -0.15 | cpu-small | 57.656276550898276 |
| 18 | Zeus | -4.37 | rtx4090 | 986.9231817338698 |
| 45 | AlphaRidge.ai | -4.62 | rtx4090 | 20.561923497603914 |
| 123 | MANTIS | -6.09 | rtx4090 | 83.47634724680049 |
| 19 | blockmachine | -7.06 | rtx4090 | 8.698645601315844 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07629440372441516 |
| 105 | Beam | -2.36 | rtx4090 | 83.47405557514624 |
| 84 | ansuz | -8.15 | rtx4090 | 467.55658397762573 |
| 34 | BitMind | -19.22 | a100-80 | 294.0982097433563 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 19.0 | 35.0 | 15.0 | 9.45 | 1.0 |
| 98 | 29.49 | 35.0 | 15.0 | 10.0 | 0.85 |
| 76 | 14.63 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 13.4 | 35.0 | 15.0 | 9.87 | 1.0 |
| 1 | 26.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 25.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.55 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 9.71 | 35.0 | 15.0 | 9.37 | 1.0 |
| 56 | 24.79 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 10.27 | 35.0 | 15.0 | 8.61 | 1.0 |
| 26 | 12.82 | 35.0 | 11.25 | 9.73 | 1.0 |
| 62 | 23.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.07 | 35.0 | 11.25 | 9.67 | 1.0 |
| 21 | 8.51 | 35.0 | 15.0 | 9.12 | 1.0 |
| 6 | 8.47 | 35.0 | 15.0 | 8.22 | 1.0 |
| 38 | 18.72 | 35.0 | 15.0 | 9.56 | 0.85 |
| 124 | 21.47 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 20.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.03 | 35.0 | 11.25 | 9.88 | 0.85 |
| 51 | 15.1 | 35.0 | 11.25 | 9.25 | 0.85 |
| 61 | 11.75 | 35.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.12 | 35.0 | 11.25 | 9.51 | 0.85 |
| 102 | 23.91 | 21.0 | 11.25 | 9.99 | 0.85 |
| 2 | 8.9 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.9 | 35.0 | 11.25 | 9.99 | 0.6 |
