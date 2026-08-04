# RANKING - generated 2026-08-04T04:26:17Z, block 8768416

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
| 1 | 23 | Trishool | 84.9 | 1.0 | 542 | 542 | cpu-small | 0.000 | 5 | 20% | SCORING_COMMIT 5.6d ago |
| 2 | 107 | Minos | 78.4 | 1.0 | 119 | 26,483 | cpu-small | 0.000 | 20 | 88% | WEIGHTS_VERSION_BUMP 0.0d ago |
| 3 | 76 | Phylax | 77.2 | 1.0 | 77.44 | 157 | cpu-small | 0.000 | 7 | 66% | SCORING_COMMIT 1.5d ago |
| 4 | 60 | Bitsec.ai | 76.4 | 0.85 | 1,951 | 1,951 | cpu-small | 0.103 | 2 | 90% | SCORING_COMMIT 0.6d ago |
| 5 | 98 | NeverPlayAlone | 75.9 | 0.85 | 1,675 | 1,675 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 4.5d ago |
| 6 | 67 | Harnyx | 71.9 | 1.0 | 20.78 | 701 | cpu-small | 0.057 | 144 | 17% | SCORING_COMMIT 0.0d ago |
| 7 | 102 | ConnitoAI | 70.0 | 0.85 | 751 | 751 | rtx4090 | 0.250 | 4 | 25% | RELEASE 3.2d ago |
| 8 | 62 | Ridges | 70.0 | 0.85 | 745 | 3,057 | rtx4090 | 0.015 | 7 | 39% | RELEASE 4.2d ago |
| 9 | 26 | Perturb | 68.6 | 1.0 | 23.71 | 184 | rtx3060 | 0.501 | 11 | 50% | README_TASK_DIFF 4.5d ago |
| 10 | 15 | ORO | 66.9 | 1.0 | 8.32 | 17.29 | cpu-small | 0.000 | 86 | 93% | RELEASE 3.5d ago |
| 11 | 74 | Gittensor | 66.1 | 0.85 | 235 | 355 | rtx4090 | 0.000 | 8 | 18% | RELEASE 3.3d ago |
| 12 | 124 | Swarm | 66.0 | 0.85 | 234 | 684 | rtx4090 | 0.000 | 21 | 12% | SCORING_COMMIT 2.6d ago |
| 13 | 38 | ChronoLLM | 65.4 | 0.85 | 199 | 3,344 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 4.8d ago |
| 14 | 41 | Almanac | 65.3 | 1.0 | 4.50 | 66.82 | cpu-small | 0.892 | 36 | 89% | SCORING_COMMIT 1.0d ago |
| 15 | 21 | AdTAO | 65.3 | 1.0 | 4.46 | 20.80 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.6d ago |
| 16 | 85 | Vidaio | 64.2 | 0.85 | 129 | 457 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 6.9d ago |
| 17 | 53 | engy | 64.1 | 0.85 | 129 | 3,005 | rtx4090 | 0.000 | 28 | 17% | SCORING_COMMIT 5.5d ago |
| 18 | 61 | RedTeam | 58.3 | 0.85 | 21.68 | 76.43 | rtx4090 | 0.000 | 98 | 3% | RELEASE 0.1d ago |
| 19 | 9 | iota | 55.3 | 0.6 | 8,709 | 8,709 | rtx4090 | 0.504 | 3 | 50% | RELEASE 3.5d ago |
| 20 | 28 | gm | 53.0 | 0.85 | 5.62 | 2,288 | rtx4090 | 0.629 | 17 | 63% | RELEASE 0.6d ago |
| 21 | 97 | Albedo | 52.6 | 0.6 | 2,903 | 2,903 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.1d ago |
| 22 | 101 | Tag101 | 50.0 | 1.0 | -0.02 | 0.88 | cpu-small | 0.893 | 243 | 90% | SCORING_COMMIT 3.5d ago |
| 23 | 11 | TrajectoryRL | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 1.7d ago |
| 24 | 51 | lium.io | 49.8 | 0.85 | 6.00 | 4,443 | rtx4090 | 0.000 | 45 | 54% | RELEASE 0.7d ago |
| 25 | 99 | Thirty Spokes | 49.7 | 0.6 | 841 | 841 | rtx4090 | 0.000 | 4 | 25% | subnet is 27 days old |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 101 | Tag101 | -0.02 | cpu-small | 1.8640066844305225 |
| 54 | Yanez MIID | -4.25 | a4000 | 841.6214574432515 |
| 50 | Synth | -0.41 | rtx4090 | 50.438740455693484 |
| 13 | Data Universe | -3.09 | rtx4090 | 5.572049043043069 |
| 56 | Gradients | -7.34 | rtx4090 | 946.9911941212277 |
| 8 | Vanta | -7.49 | rtx4090 | 2914.4678239201767 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 177.75525404603334 |
| 43 | Graphite | -0.48 | cpu-small | 12.077798331441862 |
| 32 | ItsAI | -0.19 | rtx4090 | 10.541016079893406 |
| 104 | Masx.ai | -1.79 | rtx4090 | 8.397613170249523 |
| 19 | blockmachine | -2.03 | rtx4090 | 70.02350865099102 |
| 5 | Hone | -2.12 | rtx4090 | 6.219236065563144 |
| 18 | Zeus | -4.46 | rtx4090 | 1445.4553057294322 |
| 22 | Desearch | -4.71 | rtx4090 | 114.27711159789445 |
| 75 | Hippius | -5.26 | rtx4090 | 4.328628156874664 |
| 45 | AlphaRidge.ai | -5.67 | rtx4090 | 13.427176823799524 |
| 88 | Investing | -5.81 | rtx4090 | 480.37678399494746 |
| 123 | MANTIS | -6.03 | rtx4090 | 84.23059338890066 |
| 114 | SOMA | -8.13 | rtx4090 | 1413.5344591494932 |
| 46 | Zipcode | -8.14 | rtx4090 | 0.12252619943896505 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 35 subnets: sn6, sn10, sn12, sn14, sn20, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn103, sn108, sn109, sn111, sn113, sn120, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 23 | 24.88 | 35.0 | 15.0 | 9.99 | 1.0 |
| 107 | 18.9 | 35.0 | 15.0 | 9.47 | 1.0 |
| 76 | 17.23 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 29.93 | 35.0 | 15.0 | 10.0 | 0.85 |
| 98 | 29.32 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.17 | 35.0 | 15.0 | 9.74 | 1.0 |
| 102 | 26.16 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 26.13 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.67 | 35.0 | 11.25 | 9.73 | 1.0 |
| 15 | 8.82 | 35.0 | 15.0 | 8.08 | 1.0 |
| 74 | 21.58 | 35.0 | 11.25 | 9.96 | 0.85 |
| 124 | 21.56 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 20.92 | 35.0 | 11.25 | 9.76 | 0.85 |
| 41 | 6.74 | 35.0 | 15.0 | 8.58 | 1.0 |
| 21 | 6.71 | 35.0 | 15.0 | 8.57 | 1.0 |
| 85 | 19.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 19.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 12.33 | 35.0 | 11.25 | 10.0 | 0.85 |
| 9 | 35.84 | 35.0 | 11.25 | 10.0 | 0.6 |
| 28 | 7.46 | 35.0 | 11.25 | 8.59 | 0.85 |
| 97 | 31.5 | 35.0 | 11.25 | 9.99 | 0.6 |
| 101 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
| 11 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
| 51 | 7.69 | 35.0 | 11.25 | 4.69 | 0.85 |
| 99 | 26.61 | 35.0 | 11.25 | 10.0 | 0.6 |
