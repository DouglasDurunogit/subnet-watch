# RANKING - generated 2026-08-13T18:41:45Z, block 8837480

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
| 1 | 107 | Minos | 77.9 | 1.0 | 107 | 31,668 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 3.1d ago |
| 2 | 76 | Phylax | 74.6 | 1.0 | 39.04 | 187 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 4.9d ago |
| 3 | 67 | Harnyx | 71.3 | 1.0 | 17.38 | 714 | cpu-small | 0.019 | 148 | 19% | SCORING_COMMIT 0.3d ago |
| 4 | 1 | Apex | 70.4 | 0.85 | 842 | 1,150 | rtx4090 | 0.543 | 4 | 54% | RELEASE 0.2d ago |
| 5 | 91 | cascade | 69.8 | 0.85 | 695 | 2,394 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 2.6d ago |
| 6 | 26 | Perturb | 69.5 | 1.0 | 29.60 | 839 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 0.1d ago |
| 7 | 62 | Ridges | 69.0 | 0.85 | 547 | 1,978 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 1.8d ago |
| 8 | 41 | Almanac | 69.0 | 1.0 | 10.36 | 28.57 | cpu-small | 0.725 | 68 | 73% | SCORING_COMMIT 0.8d ago |
| 9 | 56 | Gradients | 68.9 | 0.85 | 529 | 980 | rtx4090 | 0.654 | 7 | 65% | SCORING_COMMIT 1.2d ago |
| 10 | 96 | Verathos | 68.6 | 1.0 | 23.57 | 281 | rtx4090 | 0.411 | 58 | 41% | RELEASE 1.2d ago |
| 11 | 38 | ChronoLLM | 68.0 | 0.85 | 169 | 3,540 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.1d ago |
| 12 | 6 | Numinous | 67.9 | 1.0 | 9.51 | 504 | cpu-small | 0.000 | 19 | 29% | WEIGHTS_VERSION_BUMP 0.1d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.60 | 34.11 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 2.3d ago |
| 14 | 124 | Swarm | 66.1 | 0.85 | 238 | 728 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 2.1d ago |
| 15 | 80 | OpenRoboto | 65.3 | 0.85 | 180 | 651 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 5.6d ago |
| 16 | 85 | Vidaio | 64.4 | 0.85 | 141 | 602 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 1.3d ago |
| 17 | 51 | lium.io | 60.9 | 0.85 | 56.65 | 1,636 | rtx4090 | 0.000 | 48 | 72% | RELEASE 0.1d ago |
| 18 | 28 | gm | 59.6 | 0.85 | 34.62 | 894 | rtx4090 | 0.591 | 31 | 59% | RELEASE 1.2d ago |
| 19 | 74 | Gittensor | 58.2 | 0.85 | 23.84 | 215 | rtx4090 | 0.631 | 14 | 63% | RELEASE 2.0d ago |
| 20 | 61 | RedTeam | 57.6 | 0.85 | 17.50 | 1,571 | rtx4090 | 0.000 | 66 | 35% | RELEASE 2.4d ago |
| 21 | 2 | DSperse | 55.8 | 0.85 | 9.70 | 80.94 | rtx4090 | 0.828 | 13 | 83% | RELEASE 2.9d ago |
| 22 | 15 | ORO | 54.8 | 1.0 | 12.60 | 22.73 | cpu-small | 0.000 | 79 | 93% | RELEASE 7d ago |
| 23 | 120 | Affine | 54.7 | 0.6 | 6,950 | 6,950 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.2d ago |
| 24 | 97 | Albedo | 52.7 | 0.6 | 2,944 | 2,944 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.0d ago |
| 25 | 53 | engy | 50.7 | 0.85 | 81.06 | 553 | rtx4090 | 0.000 | 144 | 11% | SCORING_COMMIT 15d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.98 | a4000 | 947.8386931960359 |
| 104 | Masx.ai | -2.15 | rtx4090 | 12.61260129730896 |
| 75 | Hippius | -7.32 | rtx4090 | 11673.607020633857 |
| 114 | SOMA | -8.11 | rtx4090 | 694.8307653805647 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 162.7882053659955 |
| 13 | Data Universe | -3.18 | rtx4090 | 5.77651265949871 |
| 88 | Investing | -5.18 | rtx4090 | 674.8433064948853 |
| 8 | Vanta | -7.95 | rtx4090 | 3399.7362310525637 |
| 43 | Graphite | -0.65 | cpu-small | 40.764396644521725 |
| 32 | ItsAI | -0.16 | rtx4090 | 11.453439596819013 |
| 19 | blockmachine | -2.00 | rtx4090 | 428.858711060088 |
| 18 | Zeus | -3.95 | rtx4090 | 1805.0775943882707 |
| 45 | AlphaRidge.ai | -5.07 | rtx4090 | 12.125081276958602 |
| 123 | MANTIS | -6.09 | rtx4090 | 80.41088281629368 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07637365134123825 |
| 105 | Beam | -2.37 | rtx4090 | 81.75332961979112 |
| 84 | ansuz | -8.16 | rtx4090 | 465.24710267679376 |
| 34 | BitMind | -20.06 | a100-80 | 292.3421696380384 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn100, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.49 | 35.0 | 15.0 | 9.38 | 1.0 |
| 76 | 14.57 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 11.5 | 35.0 | 15.0 | 9.76 | 1.0 |
| 1 | 26.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.85 | 35.0 | 11.25 | 9.99 | 0.85 |
| 26 | 13.51 | 35.0 | 11.25 | 9.77 | 1.0 |
| 62 | 24.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.6 | 35.0 | 15.0 | 9.35 | 1.0 |
| 56 | 24.78 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.65 | 35.0 | 11.25 | 9.72 | 1.0 |
| 38 | 20.29 | 35.0 | 15.0 | 9.71 | 0.85 |
| 6 | 9.29 | 35.0 | 15.0 | 8.59 | 1.0 |
| 21 | 8.5 | 35.0 | 15.0 | 9.12 | 1.0 |
| 124 | 21.63 | 35.0 | 11.25 | 9.86 | 0.85 |
| 80 | 20.53 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.01 | 35.0 | 11.25 | 9.41 | 0.85 |
| 28 | 14.11 | 35.0 | 11.25 | 9.81 | 0.85 |
| 74 | 12.69 | 35.0 | 11.25 | 9.58 | 0.85 |
| 61 | 11.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 10.31 | 21.0 | 15.0 | 8.46 | 1.0 |
| 120 | 34.94 | 35.0 | 11.25 | 9.98 | 0.6 |
| 97 | 31.55 | 35.0 | 11.25 | 9.97 | 0.6 |
| 53 | 17.41 | 21.0 | 11.25 | 10.0 | 0.85 |
