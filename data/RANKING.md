# RANKING - generated 2026-08-11T10:24:00Z, block 8820599

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
| 1 | 107 | Minos | 78.2 | 1.0 | 115 | 32,473 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 0.8d ago |
| 2 | 76 | Phylax | 76.8 | 1.0 | 69.95 | 211 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 2.5d ago |
| 3 | 96 | Verathos | 71.7 | 1.0 | 50.47 | 616 | rtx4090 | 0.412 | 33 | 41% | RELEASE 0.1d ago |
| 4 | 67 | Harnyx | 70.3 | 1.0 | 13.86 | 802 | cpu-small | 0.080 | 142 | 21% | SCORING_COMMIT 0.9d ago |
| 5 | 91 | cascade | 70.1 | 0.85 | 758 | 2,575 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.2d ago |
| 6 | 41 | Almanac | 69.0 | 1.0 | 10.51 | 27.68 | cpu-small | 0.724 | 67 | 72% | SCORING_COMMIT 4.4d ago |
| 7 | 62 | Ridges | 68.9 | 0.85 | 533 | 1,930 | rtx4090 | 0.133 | 7 | 35% | RELEASE 5.5d ago |
| 8 | 15 | ORO | 68.0 | 1.0 | 10.56 | 21.90 | cpu-small | 0.000 | 86 | 92% | RELEASE 5.0d ago |
| 9 | 26 | Perturb | 67.8 | 1.0 | 19.27 | 173 | rtx3060 | 0.502 | 11 | 50% | SCORING_COMMIT 4.8d ago |
| 10 | 56 | Gradients | 66.6 | 0.85 | 272 | 983 | rtx4090 | 0.724 | 8 | 72% | SCORING_COMMIT 0.5d ago |
| 11 | 100 | BASE | 66.6 | 0.85 | 266 | 1,874 | rtx4090 | 0.000 | 6 | 47% | RELEASE 0.6d ago |
| 12 | 21 | AdTAO | 66.1 | 1.0 | 5.39 | 25.39 | cpu-small | 0.451 | 118 | 45% | SCORING_COMMIT 2.8d ago |
| 13 | 124 | Swarm | 65.7 | 0.85 | 215 | 654 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 0.9d ago |
| 14 | 85 | Vidaio | 64.9 | 0.85 | 159 | 620 | rtx4090 | 0.000 | 10 | 20% | SCORING_COMMIT 0.1d ago |
| 15 | 38 | ChronoLLM | 64.7 | 0.85 | 163 | 3,546 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 3.0d ago |
| 16 | 80 | OpenRoboto | 64.7 | 0.85 | 154 | 559 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 3.2d ago |
| 17 | 61 | RedTeam | 62.3 | 0.85 | 72.82 | 302 | rtx4090 | 0.000 | 46 | 7% | RELEASE 0.1d ago |
| 18 | 28 | gm | 60.8 | 0.85 | 49.15 | 2,483 | rtx4090 | 0.212 | 27 | 25% | RELEASE 3.6d ago |
| 19 | 51 | lium.io | 60.6 | 0.85 | 52.45 | 2,711 | rtx4090 | 0.000 | 48 | 64% | RELEASE 0.9d ago |
| 20 | 6 | Numinous | 57.6 | 1.0 | 21.03 | 463 | cpu-small | 0.000 | 19 | 26% | README_TASK_DIFF 13d ago |
| 21 | 2 | DSperse | 57.1 | 0.85 | 15.10 | 115 | rtx4090 | 0.821 | 13 | 82% | RELEASE 0.6d ago |
| 22 | 120 | Affine | 54.8 | 0.6 | 7,181 | 7,181 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.8d ago |
| 23 | 97 | Albedo | 52.7 | 0.6 | 2,923 | 2,923 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.6d ago |
| 24 | 74 | Gittensor | 52.7 | 0.85 | 5.72 | 215 | rtx4090 | 0.630 | 14 | 63% | RELEASE 3.8d ago |
| 25 | 114 | SOMA | 50.4 | 0.6 | 1,140 | 1,633 | rtx4090 | 0.000 | 3 | 65% | SCORING_COMMIT 4.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 104 | Masx.ai | -1.56 | rtx4090 | 7.108023342445618 |
| 13 | Data Universe | -3.19 | rtx4090 | 5.881065572187453 |
| 88 | Investing | -5.16 | rtx4090 | 776.325472712718 |
| 75 | Hippius | -7.56 | rtx4090 | 10783.048392122893 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 149.55145211358717 |
| 54 | Yanez MIID | -3.91 | a4000 | 959.0751490456637 |
| 50 | Synth | -0.29 | rtx4090 | 31.667961662020616 |
| 8 | Vanta | -7.41 | rtx4090 | 3294.0645562264835 |
| 32 | ItsAI | -0.13 | rtx4090 | 12.728327181911355 |
| 19 | blockmachine | -0.77 | rtx4090 | 1350.1769963329514 |
| 18 | Zeus | -4.76 | rtx4090 | 877.993252145527 |
| 45 | AlphaRidge.ai | -6.22 | rtx4090 | 8.851302018136815 |
| 123 | MANTIS | -6.24 | rtx4090 | 78.0520644328103 |
| 63 | Enigma | -8.15 | rtx4090 | 4840.2437675398105 |
| 84 | ansuz | -8.15 | rtx4090 | 502.8909119992633 |
| 34 | BitMind | -19.34 | a100-80 | 290.6289294397831 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn94, sn95, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.79 | 35.0 | 15.0 | 9.43 | 1.0 |
| 76 | 16.83 | 35.0 | 15.0 | 10.0 | 1.0 |
| 96 | 15.57 | 35.0 | 11.25 | 9.86 | 1.0 |
| 67 | 10.66 | 35.0 | 15.0 | 9.65 | 1.0 |
| 91 | 26.2 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 9.65 | 35.0 | 15.0 | 9.37 | 1.0 |
| 62 | 24.81 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.67 | 35.0 | 15.0 | 8.32 | 1.0 |
| 26 | 11.89 | 35.0 | 11.25 | 9.65 | 1.0 |
| 56 | 22.16 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 22.08 | 35.0 | 11.25 | 9.99 | 0.85 |
| 21 | 7.33 | 35.0 | 15.0 | 8.76 | 1.0 |
| 124 | 21.24 | 35.0 | 11.25 | 9.85 | 0.85 |
| 85 | 20.05 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 20.13 | 35.0 | 11.25 | 9.7 | 0.85 |
| 80 | 19.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 16.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.46 | 35.0 | 11.25 | 9.86 | 0.85 |
| 51 | 15.72 | 35.0 | 11.25 | 9.36 | 0.85 |
| 6 | 12.21 | 21.0 | 15.0 | 9.37 | 1.0 |
| 2 | 10.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.07 | 35.0 | 11.25 | 9.99 | 0.6 |
| 97 | 31.52 | 35.0 | 11.25 | 9.98 | 0.6 |
| 74 | 7.53 | 35.0 | 11.25 | 8.25 | 0.85 |
| 114 | 27.81 | 35.0 | 11.25 | 9.99 | 0.6 |
