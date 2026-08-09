# RANKING - generated 2026-08-09T10:48:57Z, block 8806323

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
| 1 | 11 | TrajectoryRL | 79.5 | 0.85 | 4,793 | 4,793 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 7.0d ago |
| 2 | 107 | Minos | 78.6 | 1.0 | 127 | 35,077 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.3d ago |
| 3 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,245 | 1,245 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.6d ago |
| 4 | 76 | Phylax | 74.9 | 1.0 | 42.61 | 203 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.5d ago |
| 5 | 67 | Harnyx | 70.7 | 1.0 | 15.09 | 862 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.0d ago |
| 6 | 91 | cascade | 70.2 | 0.85 | 793 | 2,713 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.3d ago |
| 7 | 1 | Apex | 70.2 | 0.85 | 782 | 1,612 | rtx4090 | 0.458 | 4 | 46% | RELEASE 1.6d ago |
| 8 | 100 | BASE | 69.4 | 0.85 | 623 | 1,674 | rtx4090 | 0.000 | 4 | 50% | SCORING_COMMIT 0.6d ago |
| 9 | 41 | Almanac | 69.4 | 1.0 | 11.55 | 34.50 | cpu-small | 0.717 | 67 | 72% | SCORING_COMMIT 2.4d ago |
| 10 | 96 | Verathos | 69.1 | 1.0 | 26.71 | 290 | rtx4090 | 0.409 | 71 | 41% | RELEASE 0.0d ago |
| 11 | 62 | Ridges | 68.3 | 0.85 | 440 | 2,040 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.5d ago |
| 12 | 26 | Perturb | 68.3 | 1.0 | 21.96 | 41.65 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 2.8d ago |
| 13 | 15 | ORO | 67.5 | 1.0 | 8.90 | 19.16 | cpu-small | 0.000 | 71 | 94% | RELEASE 3.0d ago |
| 14 | 38 | ChronoLLM | 65.7 | 0.85 | 215 | 3,604 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.0d ago |
| 15 | 21 | AdTAO | 65.6 | 1.0 | 4.86 | 22.41 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.8d ago |
| 16 | 80 | OpenRoboto | 64.8 | 0.85 | 157 | 572 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 1.2d ago |
| 17 | 28 | gm | 64.5 | 0.85 | 144 | 4,183 | rtx4090 | 0.192 | 25 | 43% | RELEASE 1.6d ago |
| 18 | 61 | RedTeam | 63.2 | 0.85 | 95.46 | 270 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.0d ago |
| 19 | 51 | lium.io | 60.0 | 0.85 | 44.73 | 2,986 | rtx4090 | 0.000 | 48 | 66% | SCORING_COMMIT 1.6d ago |
| 20 | 102 | ConnitoAI | 59.5 | 0.85 | 1,118 | 1,170 | rtx4090 | 0.250 | 6 | 25% | RELEASE 8d ago |
| 21 | 6 | Numinous | 59.1 | 1.0 | 29.72 | 341 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 22 | 85 | Vidaio | 56.7 | 0.85 | 481 | 540 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 12d ago |
| 23 | 56 | Gradients | 56.6 | 0.85 | 478 | 1,007 | rtx4090 | 0.705 | 7 | 71% | SCORING_COMMIT 12d ago |
| 24 | 2 | DSperse | 55.6 | 0.85 | 9.13 | 116 | rtx4090 | 0.829 | 15 | 83% | RELEASE 3.3d ago |
| 25 | 120 | Affine | 54.8 | 0.6 | 7,330 | 7,330 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.89 | a4000 | 1027.4401069854162 |
| 104 | Masx.ai | -1.48 | rtx4090 | 7.831549532085384 |
| 13 | Data Universe | -2.79 | rtx4090 | 6.94802578741571 |
| 88 | Investing | -5.68 | rtx4090 | 501.82765272998466 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 129.13376932807768 |
| 8 | Vanta | -7.39 | rtx4090 | 3393.862562529464 |
| 19 | blockmachine | -1.41 | rtx4090 | 259.7309463495109 |
| 45 | AlphaRidge.ai | -1.48 | rtx4090 | 37.51994184936394 |
| 18 | Zeus | -4.32 | rtx4090 | 1334.1715651124243 |
| 75 | Hippius | -4.42 | rtx4090 | 5.653228664175758 |
| 123 | MANTIS | -6.20 | rtx4090 | 74.13257310390671 |
| 63 | Enigma | -8.14 | rtx4090 | 5009.327380688212 |
| 105 | Beam | -4.48 | rtx4090 | 175.6441002414159 |
| 84 | ansuz | -8.15 | rtx4090 | 503.3312143337789 |
| 34 | BitMind | -18.25 | a100-80 | 299.1694438400317 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.48 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 19.17 | 35.0 | 15.0 | 9.47 | 1.0 |
| 60 | 28.15 | 35.0 | 15.0 | 10.0 | 0.85 |
| 76 | 14.91 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 10.97 | 35.0 | 15.0 | 9.74 | 1.0 |
| 91 | 26.37 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 25.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.99 | 35.0 | 15.0 | 9.41 | 1.0 |
| 96 | 13.12 | 35.0 | 11.25 | 9.74 | 1.0 |
| 62 | 24.05 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.38 | 35.0 | 11.25 | 9.69 | 1.0 |
| 15 | 9.06 | 35.0 | 15.0 | 8.4 | 1.0 |
| 38 | 21.22 | 35.0 | 11.25 | 9.76 | 0.85 |
| 21 | 6.99 | 35.0 | 15.0 | 8.59 | 1.0 |
| 80 | 20.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 19.66 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 18.05 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 15.1 | 35.0 | 11.25 | 9.23 | 0.85 |
| 102 | 27.73 | 21.0 | 11.25 | 10.0 | 0.85 |
| 6 | 13.53 | 21.0 | 15.0 | 9.54 | 1.0 |
| 85 | 24.4 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.38 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.14 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.15 | 35.0 | 11.25 | 9.99 | 0.6 |
