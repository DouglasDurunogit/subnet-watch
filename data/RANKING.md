# RANKING - generated 2026-08-04T15:03:11Z, block 8771597

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
| 1 | 23 | Trishool | 84.8 | 1.0 | 534 | 534 | cpu-small | 0.000 | 5 | 20% | SCORING_COMMIT 6.0d ago |
| 2 | 107 | Minos | 77.7 | 1.0 | 101 | 28,725 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 0.4d ago |
| 3 | 76 | Phylax | 77.2 | 1.0 | 76.72 | 154 | cpu-small | 0.000 | 7 | 67% | SCORING_COMMIT 1.9d ago |
| 4 | 60 | Bitsec.ai | 76.4 | 0.85 | 1,924 | 1,924 | cpu-small | 0.103 | 2 | 90% | SCORING_COMMIT 1.0d ago |
| 5 | 67 | Harnyx | 71.9 | 1.0 | 20.83 | 702 | cpu-small | 0.007 | 155 | 17% | SCORING_COMMIT 0.4d ago |
| 6 | 62 | Ridges | 69.7 | 0.85 | 672 | 2,428 | rtx4090 | 0.015 | 7 | 39% | RELEASE 4.6d ago |
| 7 | 26 | Perturb | 68.5 | 1.0 | 22.74 | 190 | rtx3060 | 0.501 | 11 | 50% | README_TASK_DIFF 4.9d ago |
| 8 | 56 | Gradients | 67.2 | 0.85 | 325 | 947 | rtx4090 | 0.708 | 7 | 71% | SCORING_COMMIT 6.7d ago |
| 9 | 102 | ConnitoAI | 67.1 | 0.85 | 313 | 955 | rtx4090 | 0.251 | 6 | 31% | RELEASE 3.7d ago |
| 10 | 15 | ORO | 66.8 | 1.0 | 7.81 | 17.78 | cpu-small | 0.000 | 71 | 94% | RELEASE 3.9d ago |
| 11 | 124 | Swarm | 66.2 | 0.85 | 246 | 486 | rtx4090 | 0.000 | 22 | 8% | SCORING_COMMIT 3.0d ago |
| 12 | 74 | Gittensor | 65.7 | 0.85 | 209 | 323 | rtx4090 | 0.000 | 8 | 18% | RELEASE 3.7d ago |
| 13 | 38 | ChronoLLM | 65.4 | 0.85 | 200 | 3,370 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 5.2d ago |
| 14 | 41 | Almanac | 65.4 | 1.0 | 4.62 | 66.87 | cpu-small | 0.891 | 36 | 89% | SCORING_COMMIT 1.4d ago |
| 15 | 21 | AdTAO | 65.2 | 1.0 | 4.42 | 20.63 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.0d ago |
| 16 | 53 | engy | 64.1 | 0.85 | 127 | 2,977 | rtx4090 | 0.000 | 28 | 17% | SCORING_COMMIT 5.9d ago |
| 17 | 80 | OpenRoboto | 62.3 | 0.85 | 74.51 | 281 | rtx4090 | 0.909 | 4 | 91% | SCORING_COMMIT 4.3d ago |
| 18 | 28 | gm | 58.8 | 0.85 | 27.30 | 1,057 | rtx4090 | 0.652 | 18 | 65% | RELEASE 1.0d ago |
| 19 | 61 | RedTeam | 58.4 | 0.85 | 22.57 | 78.91 | rtx4090 | 0.000 | 95 | 3% | RELEASE 0.6d ago |
| 20 | 9 | iota | 55.2 | 0.6 | 8,686 | 8,686 | rtx4090 | 0.456 | 3 | 46% | RELEASE 3.9d ago |
| 21 | 51 | lium.io | 55.2 | 0.85 | 14.64 | 4,750 | rtx4090 | 0.000 | 45 | 66% | SCORING_COMMIT 0.3d ago |
| 22 | 85 | Vidaio | 52.8 | 0.85 | 153 | 498 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 7d ago |
| 23 | 97 | Albedo | 52.7 | 0.6 | 2,964 | 2,964 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.6d ago |
| 24 | 101 | Tag101 | 50.7 | 1.0 | 0.03 | 0.96 | cpu-small | 0.893 | 241 | 90% | SCORING_COMMIT 3.9d ago |
| 25 | 11 | TrajectoryRL | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 2.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.61 | a4000 | 860.4724508410388 |
| 50 | Synth | -0.74 | rtx4090 | 40.90586292133691 |
| 104 | Masx.ai | -1.09 | rtx4090 | 7.703985329646671 |
| 13 | Data Universe | -3.38 | rtx4090 | 4.999884532291373 |
| 8 | Vanta | -7.48 | rtx4090 | 2947.224206098775 |
| 114 | SOMA | -8.13 | rtx4090 | 1390.6067176039899 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 205.24120156582356 |
| 43 | Graphite | -0.47 | cpu-small | 12.097318757824247 |
| 32 | ItsAI | -0.11 | rtx4090 | 11.084032580976533 |
| 19 | blockmachine | -1.45 | rtx4090 | 79.01152790543487 |
| 5 | Hone | -2.81 | rtx4090 | 9.261242485670335 |
| 18 | Zeus | -3.18 | rtx4090 | 2520.9050205337953 |
| 22 | Desearch | -4.51 | rtx4090 | 67.2255460970271 |
| 88 | Investing | -4.79 | rtx4090 | 548.7608419624175 |
| 75 | Hippius | -4.86 | rtx4090 | 9510.965860152211 |
| 45 | AlphaRidge.ai | -4.98 | rtx4090 | 16.634364106266176 |
| 123 | MANTIS | -6.11 | rtx4090 | 85.54454880099475 |
| 63 | Enigma | -8.15 | rtx4090 | 4684.510584370613 |
| 105 | Beam | -4.57 | rtx4090 | 198.72577669054624 |
| 84 | ansuz | -8.15 | rtx4090 | 500.76352200773147 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn10, sn12, sn14, sn20, sn25, sn27, sn30, sn31, sn36, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn103, sn108, sn109, sn111, sn113, sn120, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 23 | 24.81 | 35.0 | 15.0 | 9.99 | 1.0 |
| 107 | 18.29 | 35.0 | 15.0 | 9.37 | 1.0 |
| 76 | 17.19 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 29.87 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.18 | 35.0 | 15.0 | 9.7 | 1.0 |
| 62 | 25.72 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.51 | 35.0 | 11.25 | 9.72 | 1.0 |
| 56 | 22.85 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 22.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 8.6 | 35.0 | 15.0 | 8.17 | 1.0 |
| 124 | 21.76 | 35.0 | 11.25 | 9.84 | 0.85 |
| 74 | 21.12 | 35.0 | 11.25 | 9.95 | 0.85 |
| 38 | 20.95 | 35.0 | 11.25 | 9.76 | 0.85 |
| 41 | 6.82 | 35.0 | 15.0 | 8.61 | 1.0 |
| 21 | 6.67 | 35.0 | 15.0 | 8.55 | 1.0 |
| 53 | 19.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 80 | 17.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.2 | 35.0 | 11.25 | 9.77 | 0.85 |
| 61 | 12.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 9 | 35.82 | 35.0 | 11.25 | 10.0 | 0.6 |
| 51 | 10.86 | 35.0 | 11.25 | 7.81 | 0.85 |
| 85 | 19.9 | 21.0 | 11.25 | 10.0 | 0.85 |
| 97 | 31.58 | 35.0 | 11.25 | 9.98 | 0.6 |
| 101 | 0.11 | 35.0 | 15.0 | 0.63 | 1.0 |
| 11 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
