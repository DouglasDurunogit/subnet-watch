# RANKING - generated 2026-08-09T05:15:34Z, block 8804657

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
| 1 | 11 | TrajectoryRL | 79.5 | 0.85 | 4,894 | 4,894 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.8d ago |
| 2 | 107 | Minos | 78.6 | 1.0 | 126 | 35,403 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.0d ago |
| 3 | 76 | Phylax | 76.7 | 1.0 | 67.82 | 204 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.3d ago |
| 4 | 98 | NeverPlayAlone | 76.2 | 0.85 | 1,807 | 1,807 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 1.9d ago |
| 5 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,255 | 1,255 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.4d ago |
| 6 | 67 | Harnyx | 70.8 | 1.0 | 15.19 | 868 | cpu-small | 0.009 | 153 | 22% | SCORING_COMMIT 2.1d ago |
| 7 | 1 | Apex | 70.3 | 0.85 | 804 | 1,657 | rtx4090 | 0.435 | 4 | 44% | RELEASE 1.4d ago |
| 8 | 91 | cascade | 70.2 | 0.85 | 785 | 2,687 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.0d ago |
| 9 | 41 | Almanac | 69.4 | 1.0 | 11.44 | 34.61 | cpu-small | 0.715 | 68 | 72% | SCORING_COMMIT 2.2d ago |
| 10 | 96 | Verathos | 68.8 | 1.0 | 24.98 | 289 | rtx4090 | 0.407 | 74 | 41% | RELEASE 0.5d ago |
| 11 | 62 | Ridges | 68.3 | 0.85 | 445 | 2,064 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.3d ago |
| 12 | 26 | Perturb | 68.3 | 1.0 | 22.02 | 42.37 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 2.6d ago |
| 13 | 15 | ORO | 67.5 | 1.0 | 9.66 | 20.12 | cpu-small | 0.000 | 71 | 94% | RELEASE 2.8d ago |
| 14 | 38 | ChronoLLM | 65.7 | 0.85 | 217 | 3,642 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.8d ago |
| 15 | 21 | AdTAO | 65.7 | 1.0 | 5.01 | 23.01 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.6d ago |
| 16 | 80 | OpenRoboto | 64.0 | 0.85 | 125 | 458 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 1.0d ago |
| 17 | 28 | gm | 62.9 | 0.85 | 88.95 | 3,649 | rtx4090 | 0.329 | 25 | 38% | RELEASE 1.3d ago |
| 18 | 61 | RedTeam | 62.4 | 0.85 | 75.59 | 216 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.1d ago |
| 19 | 51 | lium.io | 60.4 | 0.85 | 50.00 | 2,865 | rtx4090 | 0.000 | 48 | 72% | SCORING_COMMIT 1.4d ago |
| 20 | 6 | Numinous | 59.1 | 1.0 | 30.06 | 345 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 10d ago |
| 21 | 102 | ConnitoAI | 58.2 | 0.85 | 759 | 1,478 | rtx4090 | 0.251 | 6 | 29% | RELEASE 8d ago |
| 22 | 56 | Gradients | 56.6 | 0.85 | 479 | 1,011 | rtx4090 | 0.705 | 7 | 70% | SCORING_COMMIT 11d ago |
| 23 | 74 | Gittensor | 55.4 | 0.85 | 11.14 | 245 | rtx4090 | 0.630 | 16 | 63% | RELEASE 1.5d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,201 | 7,201 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.7d ago |
| 25 | 2 | DSperse | 54.8 | 0.85 | 6.96 | 119 | rtx4090 | 0.826 | 13 | 83% | RELEASE 3.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.79 | a4000 | 1016.368078914813 |
| 104 | Masx.ai | -1.26 | rtx4090 | 7.631280551358303 |
| 13 | Data Universe | -2.83 | rtx4090 | 7.5005451876465035 |
| 88 | Investing | -5.69 | rtx4090 | 498.7502189932619 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 132.25570869314583 |
| 8 | Vanta | -7.39 | rtx4090 | 3400.8577473709342 |
| 19 | blockmachine | -1.96 | rtx4090 | 244.09159808985325 |
| 45 | AlphaRidge.ai | -4.22 | rtx4090 | 21.142469998127734 |
| 75 | Hippius | -4.45 | rtx4090 | 5.608339828970716 |
| 18 | Zeus | -4.89 | rtx4090 | 972.252669757154 |
| 123 | MANTIS | -6.21 | rtx4090 | 74.57547644310658 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07800534285555004 |
| 105 | Beam | -3.90 | rtx4090 | 194.8169101361291 |
| 84 | ansuz | -8.15 | rtx4090 | 504.9774130187987 |
| 34 | BitMind | -19.13 | a100-80 | 299.8392723865438 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn9, sn10, sn12, sn14, sn16, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.56 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 19.12 | 35.0 | 15.0 | 9.46 | 1.0 |
| 76 | 16.71 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.62 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.18 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.0 | 35.0 | 15.0 | 9.8 | 1.0 |
| 1 | 26.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.34 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 9.96 | 35.0 | 15.0 | 9.4 | 1.0 |
| 96 | 12.87 | 35.0 | 11.25 | 9.73 | 1.0 |
| 62 | 24.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.39 | 35.0 | 11.25 | 9.69 | 1.0 |
| 15 | 9.35 | 35.0 | 15.0 | 8.19 | 1.0 |
| 38 | 21.27 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 7.09 | 35.0 | 15.0 | 8.63 | 1.0 |
| 80 | 19.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 17.77 | 35.0 | 11.25 | 9.92 | 0.85 |
| 61 | 17.14 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 15.53 | 35.0 | 11.25 | 9.29 | 0.85 |
| 6 | 13.57 | 21.0 | 15.0 | 9.54 | 1.0 |
| 102 | 26.2 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.39 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.86 | 35.0 | 11.25 | 9.08 | 0.85 |
| 120 | 35.08 | 35.0 | 11.25 | 9.99 | 0.6 |
| 2 | 8.19 | 35.0 | 11.25 | 10.0 | 0.85 |
