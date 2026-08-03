# RANKING - generated 2026-08-03T01:17:26Z, block 8760278

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
| 1 | 23 | Trishool | 85.0 | 1.0 | 565 | 565 | cpu-small | 0.000 | 5 | 20% | SCORING_COMMIT 4.4d ago |
| 2 | 107 | Minos | 77.8 | 1.0 | 105 | 27,015 | cpu-small | 0.000 | 20 | 90% | SCORING_COMMIT 3.8d ago |
| 3 | 98 | NeverPlayAlone | 75.9 | 0.85 | 1,687 | 1,687 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 3.4d ago |
| 4 | 67 | Harnyx | 73.5 | 1.0 | 30.64 | 806 | cpu-small | 0.098 | 116 | 18% | SCORING_COMMIT 0.7d ago |
| 5 | 102 | ConnitoAI | 70.2 | 0.85 | 780 | 1,237 | rtx4090 | 0.251 | 5 | 32% | RELEASE 2.1d ago |
| 6 | 62 | Ridges | 69.8 | 0.85 | 700 | 2,526 | rtx4090 | 0.015 | 7 | 39% | RELEASE 3.1d ago |
| 7 | 56 | Gradients | 69.1 | 0.85 | 573 | 1,208 | rtx4090 | 0.645 | 6 | 64% | SCORING_COMMIT 5.1d ago |
| 8 | 26 | Perturb | 68.6 | 1.0 | 23.58 | 194 | rtx3060 | 0.501 | 11 | 50% | README_TASK_DIFF 3.4d ago |
| 9 | 15 | ORO | 68.6 | 1.0 | 10.69 | 18.50 | cpu-small | 0.000 | 94 | 91% | RELEASE 2.3d ago |
| 10 | 74 | Gittensor | 66.0 | 0.85 | 228 | 366 | rtx4090 | 0.000 | 8 | 19% | RELEASE 2.1d ago |
| 11 | 124 | Swarm | 65.9 | 0.85 | 225 | 670 | rtx4090 | 0.000 | 20 | 12% | SCORING_COMMIT 1.5d ago |
| 12 | 53 | engy | 63.9 | 0.85 | 119 | 2,821 | rtx4090 | 0.000 | 28 | 17% | SCORING_COMMIT 4.4d ago |
| 13 | 85 | Vidaio | 63.2 | 0.85 | 98.07 | 515 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 5.7d ago |
| 14 | 38 | ChronoLLM | 63.0 | 0.85 | 103 | 1,494 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 3.6d ago |
| 15 | 71 | Leadpoet | 62.9 | 0.85 | 89.49 | 135 | rtx4090 | 0.700 | 9 | 70% | SCORING_COMMIT 0.0d ago |
| 16 | 28 | gm | 60.7 | 0.85 | 47.75 | 2,986 | rtx4090 | 0.526 | 14 | 53% | RELEASE 3.2d ago |
| 17 | 61 | RedTeam | 58.4 | 0.85 | 22.61 | 84.56 | rtx4090 | 0.000 | 98 | 3% | RELEASE 0.9d ago |
| 18 | 9 | iota | 55.6 | 0.6 | 9,905 | 9,905 | rtx4090 | 0.464 | 3 | 50% | RELEASE 2.3d ago |
| 19 | 51 | lium.io | 53.8 | 0.85 | 11.18 | 8,774 | rtx4090 | 0.000 | 43 | 39% | SCORING_COMMIT 3.5d ago |
| 20 | 90 | KubeTEE AI Factory | 53.2 | 0.6 | 3,623 | 3,623 | rtx4090 | 0.702 | 2 | 70% | subnet is 20 days old |
| 21 | 97 | Albedo | 52.7 | 0.6 | 3,024 | 3,024 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.0d ago |
| 22 | 101 | Tag101 | 50.0 | 1.0 | -0.04 | 0.98 | cpu-small | 0.892 | 243 | 89% | SCORING_COMMIT 2.3d ago |
| 23 | 76 | Phylax | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 0.4d ago |
| 24 | 11 | TrajectoryRL | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 0.6d ago |
| 25 | 99 | Thirty Spokes | 49.8 | 0.6 | 856 | 856 | rtx4090 | 0.000 | 4 | 25% | subnet is 26 days old |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 101 | Tag101 | -0.04 | cpu-small | 1.9710428290845396 |
| 13 | Data Universe | -3.38 | rtx4090 | 8.454185736939875 |
| 103 | Djinn | -7.39 | rtx4090 | 0.9737823447309019 |
| 8 | Vanta | -7.49 | rtx4090 | 2963.619811952532 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 73.51235051681473 |
| 43 | Graphite | -0.50 | cpu-small | 11.999367429879808 |
| 54 | Yanez MIID | -3.87 | a4000 | 880.4864164096589 |
| 22 | Desearch | -0.02 | rtx4090 | 65.44584179261764 |
| 32 | ItsAI | -0.10 | rtx4090 | 10.95775202501297 |
| 50 | Synth | -1.41 | rtx4090 | 46.313782175619345 |
| 19 | blockmachine | -1.47 | rtx4090 | 72.52723244238601 |
| 5 | Hone | -2.03 | rtx4090 | 6.18807974691657 |
| 18 | Zeus | -3.14 | rtx4090 | 1708.6746133549273 |
| 45 | AlphaRidge.ai | -3.18 | rtx4090 | 31.21466515621325 |
| 104 | Masx.ai | -3.74 | rtx4090 | 9.611764570251294 |
| 75 | Hippius | -5.26 | rtx4090 | 4.323570916117978 |
| 123 | MANTIS | -5.91 | rtx4090 | 85.87591929545601 |
| 88 | Investing | -6.33 | rtx4090 | 306.75024009828246 |
| 59 | Babelbit | -7.80 | rtx4090 | 961.1970098710804 |
| 114 | SOMA | -8.13 | rtx4090 | 587.7619539946053 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 32 subnets: sn6, sn10, sn12, sn14, sn20, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn47, sn52, sn57, sn58, sn65, sn69, sn72, sn73, sn80, sn87, sn92, sn94, sn95, sn108, sn109, sn111, sn113, sn121, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 23 | 25.04 | 35.0 | 15.0 | 9.99 | 1.0 |
| 107 | 18.41 | 35.0 | 15.0 | 9.4 | 1.0 |
| 98 | 29.35 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 13.65 | 35.0 | 15.0 | 9.89 | 1.0 |
| 102 | 26.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 25.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 25.09 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.65 | 35.0 | 11.25 | 9.73 | 1.0 |
| 15 | 9.71 | 35.0 | 15.0 | 8.87 | 1.0 |
| 74 | 21.46 | 35.0 | 11.25 | 9.96 | 0.85 |
| 124 | 21.41 | 35.0 | 11.25 | 9.86 | 0.85 |
| 53 | 18.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 18.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.33 | 35.0 | 11.25 | 9.54 | 0.85 |
| 71 | 17.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.35 | 35.0 | 11.25 | 9.87 | 0.85 |
| 61 | 12.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 9 | 36.34 | 35.0 | 11.25 | 10.0 | 0.6 |
| 51 | 9.87 | 35.0 | 11.25 | 7.15 | 0.85 |
| 90 | 32.37 | 35.0 | 11.25 | 10.0 | 0.6 |
| 97 | 31.66 | 35.0 | 11.25 | 9.98 | 0.6 |
| 101 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
| 76 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
| 11 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
| 99 | 26.68 | 35.0 | 11.25 | 10.0 | 0.6 |
