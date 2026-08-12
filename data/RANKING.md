# RANKING - generated 2026-08-12T23:54:36Z, block 8831844

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
| 1 | 76 | Phylax | 78.7 | 1.0 | 111 | 374 | cpu-small | 0.000 | 10 | 27% | SCORING_COMMIT 4.1d ago |
| 2 | 107 | Minos | 77.8 | 1.0 | 105 | 31,092 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 2.4d ago |
| 3 | 67 | Harnyx | 71.4 | 1.0 | 17.92 | 746 | cpu-small | 0.038 | 131 | 20% | SCORING_COMMIT 0.5d ago |
| 4 | 96 | Verathos | 71.1 | 1.0 | 43.58 | 375 | rtx4090 | 0.417 | 49 | 42% | RELEASE 0.4d ago |
| 5 | 91 | cascade | 70.1 | 0.85 | 761 | 2,625 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.8d ago |
| 6 | 114 | SOMA | 69.6 | 0.85 | 663 | 4,353 | rtx4090 | 0.000 | 4 | 65% | SCORING_COMMIT 5.6d ago |
| 7 | 62 | Ridges | 69.0 | 0.85 | 544 | 1,968 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 1.0d ago |
| 8 | 41 | Almanac | 69.0 | 1.0 | 10.53 | 29.86 | cpu-small | 0.716 | 68 | 72% | SCORING_COMMIT 0.0d ago |
| 9 | 56 | Gradients | 68.9 | 0.85 | 532 | 977 | rtx4090 | 0.647 | 7 | 65% | SCORING_COMMIT 0.4d ago |
| 10 | 100 | BASE | 68.3 | 0.85 | 448 | 1,815 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.6d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.32 | 36.66 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 6.4d ago |
| 12 | 21 | AdTAO | 67.6 | 1.0 | 7.49 | 33.63 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 1.5d ago |
| 13 | 15 | ORO | 67.0 | 1.0 | 9.03 | 12,259 | cpu-small | 0.000 | 69 | 94% | RELEASE 6.6d ago |
| 14 | 124 | Swarm | 66.5 | 0.85 | 266 | 697 | rtx4090 | 0.000 | 21 | 12% | SCORING_COMMIT 1.4d ago |
| 15 | 80 | OpenRoboto | 64.9 | 0.85 | 162 | 587 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 4.8d ago |
| 16 | 38 | ChronoLLM | 64.6 | 0.85 | 161 | 3,504 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 4.6d ago |
| 17 | 85 | Vidaio | 63.9 | 0.85 | 119 | 496 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 0.6d ago |
| 18 | 28 | gm | 61.5 | 0.85 | 58.82 | 2,522 | rtx4090 | 0.133 | 29 | 26% | RELEASE 0.4d ago |
| 19 | 51 | lium.io | 59.8 | 0.85 | 42.62 | 2,258 | rtx4090 | 0.000 | 48 | 70% | RELEASE 0.5d ago |
| 20 | 102 | ConnitoAI | 59.6 | 0.85 | 1,141 | 1,914 | rtx4090 | 0.250 | 6 | 32% | RELEASE 12d ago |
| 21 | 74 | Gittensor | 58.2 | 0.85 | 23.39 | 215 | rtx4090 | 0.631 | 13 | 63% | RELEASE 1.2d ago |
| 22 | 61 | RedTeam | 58.2 | 0.85 | 21.10 | 1,599 | rtx4090 | 0.000 | 59 | 35% | RELEASE 1.7d ago |
| 23 | 6 | Numinous | 56.3 | 1.0 | 15.79 | 476 | cpu-small | 0.000 | 20 | 26% | README_TASK_DIFF 14d ago |
| 24 | 120 | Affine | 54.7 | 0.6 | 6,928 | 6,928 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.4d ago |
| 25 | 97 | Albedo | 52.6 | 0.6 | 2,915 | 2,915 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.97 | a4000 | 998.9956395144588 |
| 2 | DSperse | -3.91 | rtx4090 | 106.61848070672748 |
| 75 | Hippius | -7.71 | rtx4090 | 11130.367778812602 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 139.88705136636327 |
| 13 | Data Universe | -3.12 | rtx4090 | 5.745277867120627 |
| 88 | Investing | -5.05 | rtx4090 | 633.262502333428 |
| 8 | Vanta | -7.95 | rtx4090 | 3249.4527475164887 |
| 43 | Graphite | -0.23 | cpu-small | 37.92276732817727 |
| 32 | ItsAI | -0.29 | rtx4090 | 10.73652299950504 |
| 19 | blockmachine | -1.86 | rtx4090 | 549.3007859378997 |
| 18 | Zeus | -3.31 | rtx4090 | 1738.090641933226 |
| 123 | MANTIS | -6.08 | rtx4090 | 81.28569272832239 |
| 45 | AlphaRidge.ai | -6.11 | rtx4090 | 8.240963004376114 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07644571611825478 |
| 105 | Beam | -2.21 | rtx4090 | 81.34880680856138 |
| 84 | ansuz | -8.15 | rtx4090 | 475.8952104119022 |
| 34 | BitMind | -19.57 | a100-80 | 290.37972273228627 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn108, sn109, sn111, sn113, sn115, sn116, sn118, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 18.65 | 35.0 | 15.0 | 10.0 | 1.0 |
| 107 | 18.41 | 35.0 | 15.0 | 9.37 | 1.0 |
| 67 | 11.61 | 35.0 | 15.0 | 9.82 | 1.0 |
| 96 | 15.0 | 35.0 | 11.25 | 9.85 | 1.0 |
| 91 | 26.21 | 35.0 | 11.25 | 9.99 | 0.85 |
| 114 | 25.67 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 24.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.66 | 35.0 | 15.0 | 9.37 | 1.0 |
| 56 | 24.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 24.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 11.9 | 35.0 | 11.25 | 9.66 | 1.0 |
| 21 | 8.45 | 35.0 | 15.0 | 9.11 | 1.0 |
| 15 | 9.11 | 35.0 | 15.0 | 7.89 | 1.0 |
| 124 | 22.07 | 35.0 | 11.25 | 9.86 | 0.85 |
| 80 | 20.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 20.08 | 35.0 | 11.25 | 9.69 | 0.85 |
| 85 | 18.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.16 | 35.0 | 11.25 | 9.89 | 0.85 |
| 51 | 14.91 | 35.0 | 11.25 | 9.22 | 0.85 |
| 102 | 27.81 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.62 | 35.0 | 11.25 | 9.57 | 0.85 |
| 61 | 12.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.14 | 21.0 | 15.0 | 9.16 | 1.0 |
| 120 | 34.93 | 35.0 | 11.25 | 9.99 | 0.6 |
| 97 | 31.51 | 35.0 | 11.25 | 9.97 | 0.6 |
