# RANKING - generated 2026-08-16T15:01:36Z, block 8857978

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
| 1 | 107 | Minos | 77.9 | 1.0 | 107 | 32,905 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.0d ago |
| 2 | 76 | Phylax | 73.8 | 1.0 | 31.76 | 157 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.1d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.71 | 419 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.4d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.59 | 74.46 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.0d ago |
| 5 | 96 | Verathos | 70.3 | 1.0 | 35.59 | 203 | rtx4090 | 0.434 | 54 | 43% | RELEASE 1.8d ago |
| 6 | 1 | Apex | 70.1 | 0.85 | 765 | 1,055 | rtx4090 | 0.550 | 4 | 55% | RELEASE 3.0d ago |
| 7 | 41 | Almanac | 69.9 | 1.0 | 12.84 | 47.83 | cpu-small | 0.652 | 75 | 65% | SCORING_COMMIT 3.7d ago |
| 8 | 91 | cascade | 69.1 | 0.85 | 565 | 2,283 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.7d ago |
| 9 | 15 | ORO | 68.8 | 1.0 | 12.91 | 12,841 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 2.7d ago |
| 10 | 85 | Vidaio | 68.7 | 0.85 | 508 | 518 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 4.2d ago |
| 11 | 56 | Gradients | 68.7 | 0.85 | 505 | 961 | rtx4090 | 0.677 | 7 | 68% | SCORING_COMMIT 4.0d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 476 | 2,203 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.7d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.65 | 34.29 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.1d ago |
| 14 | 11 | TrajectoryRL | 67.0 | 0.85 | 4,121 | 4,121 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 14d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 96.72 | 1,323 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.9d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 719 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.0d ago |
| 17 | 2 | DSperse | 64.3 | 0.85 | 134 | 195 | rtx4090 | 0.822 | 4 | 82% | RELEASE 5.8d ago |
| 18 | 55 | NIOME | 61.3 | 0.85 | 55.14 | 484 | rtx4090 | 0.020 | 11 | 30% | SCORING_COMMIT 1.8d ago |
| 19 | 28 | gm | 59.5 | 0.85 | 32.85 | 2,418 | rtx4090 | 0.213 | 40 | 27% | RELEASE 4.0d ago |
| 20 | 60 | Bitsec.ai | 59.3 | 0.85 | 410 | 410 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 21 | 74 | Gittensor | 58.6 | 0.85 | 26.32 | 208 | rtx4090 | 0.630 | 14 | 63% | RELEASE 4.9d ago |
| 22 | 61 | RedTeam | 57.6 | 0.85 | 17.30 | 439 | rtx4090 | 0.000 | 81 | 10% | RELEASE 5.3d ago |
| 23 | 51 | lium.io | 57.2 | 0.85 | 22.51 | 1,356 | rtx4090 | 0.000 | 51 | 82% | SCORING_COMMIT 2.2d ago |
| 24 | 120 | Affine | 55.8 | 0.6 | 11,100 | 11,100 | rtx4090 | 0.333 | 3 | 33% | SCORING_COMMIT 4.0d ago |
| 25 | 68 | NOVA | 55.1 | 0.6 | 8,049 | 8,049 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 244.65296262638066 |
| 54 | Yanez | -3.98 | a4000 | 949.9452628017066 |
| 104 | Masx.ai | -0.06 | rtx4090 | 9.007444048885302 |
| 75 | Hippius | -7.21 | rtx4090 | 10946.8085209084 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 129.89808063693798 |
| 13 | Data Universe | -3.63 | rtx4090 | 6.07606798322615 |
| 88 | Investing | -5.43 | rtx4090 | 1123.7204820779832 |
| 8 | Vanta | -7.70 | rtx4090 | 2906.9068662549016 |
| 114 | SOMA | -8.13 | rtx4090 | 602.6606440874823 |
| 43 | Graphite | -0.78 | cpu-small | 16.702904128202743 |
| 32 | ItsAI | -0.15 | rtx4090 | 11.179975557043626 |
| 22 | Desearch | -2.51 | rtx4090 | 52.26440570177294 |
| 45 | AlphaRidge.ai | -2.54 | rtx4090 | 18.987025956330584 |
| 18 | Zeus | -3.73 | rtx4090 | 1607.8388896093504 |
| 19 | blockmachine | -5.94 | rtx4090 | 473.7076615970219 |
| 123 | MANTIS | -6.18 | rtx4090 | 75.36367367551794 |
| 63 | Enigma | -8.14 | rtx4090 | 5036.80718110751 |
| 105 | Beam | -3.00 | rtx4090 | 99.62816722280608 |
| 84 | ansuz | -8.16 | rtx4090 | 440.12256259540686 |
| 34 | BitMind | -19.81 | a100-80 | 20.520885577442296 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.51 | 35.0 | 15.0 | 9.39 | 1.0 |
| 76 | 13.78 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.67 | 35.0 | 15.0 | 9.86 | 1.0 |
| 26 | 14.72 | 35.0 | 11.25 | 9.84 | 1.0 |
| 96 | 14.22 | 35.0 | 11.25 | 9.82 | 1.0 |
| 1 | 26.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.38 | 35.0 | 15.0 | 9.49 | 1.0 |
| 91 | 25.03 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.4 | 35.0 | 15.0 | 8.45 | 1.0 |
| 85 | 24.62 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.52 | 35.0 | 15.0 | 9.14 | 1.0 |
| 11 | 32.88 | 21.0 | 15.0 | 10.0 | 0.85 |
| 38 | 18.1 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.39 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 19.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 15.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.91 | 35.0 | 11.25 | 9.8 | 0.85 |
| 60 | 23.78 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 13.06 | 35.0 | 11.25 | 9.59 | 0.85 |
| 61 | 11.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.47 | 35.0 | 11.25 | 8.54 | 0.85 |
| 120 | 36.79 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.52 | 35.0 | 11.25 | 10.0 | 0.6 |
