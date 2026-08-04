# RANKING - generated 2026-08-04T10:08:34Z, block 8770128

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
| 1 | 23 | Trishool | 84.8 | 1.0 | 539 | 539 | cpu-small | 0.000 | 5 | 20% | SCORING_COMMIT 5.8d ago |
| 2 | 107 | Minos | 78.0 | 1.0 | 109 | 27,868 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 0.2d ago |
| 3 | 76 | Phylax | 77.2 | 1.0 | 77.51 | 156 | cpu-small | 0.000 | 7 | 67% | SCORING_COMMIT 1.7d ago |
| 4 | 98 | NeverPlayAlone | 75.9 | 0.85 | 1,665 | 1,665 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 4.7d ago |
| 5 | 67 | Harnyx | 71.8 | 1.0 | 20.56 | 693 | cpu-small | 0.039 | 149 | 17% | SCORING_COMMIT 0.2d ago |
| 6 | 62 | Ridges | 70.0 | 0.85 | 741 | 3,041 | rtx4090 | 0.015 | 7 | 39% | RELEASE 4.4d ago |
| 7 | 102 | ConnitoAI | 69.9 | 0.85 | 725 | 725 | rtx4090 | 0.251 | 4 | 25% | RELEASE 3.5d ago |
| 8 | 26 | Perturb | 68.4 | 1.0 | 22.50 | 183 | rtx3060 | 0.502 | 11 | 50% | README_TASK_DIFF 4.7d ago |
| 9 | 56 | Gradients | 66.8 | 0.85 | 286 | 934 | rtx4090 | 0.705 | 8 | 71% | SCORING_COMMIT 6.5d ago |
| 10 | 15 | ORO | 66.2 | 1.0 | 7.88 | 10,433 | cpu-small | 0.000 | 70 | 94% | RELEASE 3.7d ago |
| 11 | 124 | Swarm | 66.0 | 0.85 | 235 | 687 | rtx4090 | 0.000 | 21 | 12% | SCORING_COMMIT 2.8d ago |
| 12 | 74 | Gittensor | 66.0 | 0.85 | 224 | 357 | rtx4090 | 0.000 | 8 | 18% | RELEASE 3.5d ago |
| 13 | 38 | ChronoLLM | 65.4 | 0.85 | 197 | 3,319 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 5.0d ago |
| 14 | 41 | Almanac | 65.3 | 1.0 | 4.52 | 66.18 | cpu-small | 0.891 | 36 | 89% | SCORING_COMMIT 1.2d ago |
| 15 | 21 | AdTAO | 65.2 | 1.0 | 4.40 | 20.54 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.8d ago |
| 16 | 53 | engy | 64.2 | 0.85 | 130 | 3,040 | rtx4090 | 0.000 | 28 | 17% | SCORING_COMMIT 5.7d ago |
| 17 | 80 | OpenRoboto | 62.1 | 0.85 | 68.89 | 154 | rtx4090 | 0.937 | 4 | 94% | SCORING_COMMIT 4.1d ago |
| 18 | 61 | RedTeam | 58.3 | 0.85 | 21.61 | 76.33 | rtx4090 | 0.000 | 98 | 3% | RELEASE 0.4d ago |
| 19 | 9 | iota | 55.2 | 0.6 | 8,639 | 8,639 | rtx4090 | 0.508 | 3 | 51% | RELEASE 3.7d ago |
| 20 | 28 | gm | 53.5 | 0.85 | 6.14 | 2,045 | rtx4090 | 0.634 | 17 | 63% | RELEASE 0.8d ago |
| 21 | 97 | Albedo | 52.6 | 0.6 | 2,880 | 2,880 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.4d ago |
| 22 | 85 | Vidaio | 51.9 | 0.85 | 117 | 478 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 7d ago |
| 23 | 101 | Tag101 | 50.1 | 1.0 | 0.02 | 1.02 | cpu-small | 0.893 | 241 | 90% | SCORING_COMMIT 3.7d ago |
| 24 | 60 | Bitsec.ai | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.103 | 2 | 90% | SCORING_COMMIT 0.8d ago |
| 25 | 11 | TrajectoryRL | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 2.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.58 | a4000 | 856.3634324536242 |
| 50 | Synth | -0.45 | rtx4090 | 45.38532568570823 |
| 13 | Data Universe | -3.29 | rtx4090 | 5.0378438145505635 |
| 8 | Vanta | -7.49 | rtx4090 | 2907.3642444915517 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 172.99739242280077 |
| 43 | Graphite | -0.71 | cpu-small | 12.049334100043241 |
| 32 | ItsAI | -0.23 | rtx4090 | 11.045759250745743 |
| 19 | blockmachine | -2.00 | rtx4090 | 52.99618254648197 |
| 5 | Hone | -2.27 | rtx4090 | 6.881370727208465 |
| 18 | Zeus | -3.25 | rtx4090 | 2484.0480185943215 |
| 22 | Desearch | -4.09 | rtx4090 | 88.3810094425285 |
| 45 | AlphaRidge.ai | -4.33 | rtx4090 | 26.95082649693166 |
| 75 | Hippius | -5.31 | rtx4090 | 4.503813523622185 |
| 88 | Investing | -5.36 | rtx4090 | 494.7755675092139 |
| 123 | MANTIS | -6.06 | rtx4090 | 84.17481118586707 |
| 114 | SOMA | -8.13 | rtx4090 | 1395.8273167487114 |
| 46 | Zipcode | -8.14 | rtx4090 | 0.11968501335731538 |
| 63 | Enigma | -8.15 | rtx4090 | 4640.721358059462 |
| 105 | Beam | -4.62 | rtx4090 | 200.65646362514795 |
| 84 | ansuz | -8.15 | rtx4090 | 492.41166395792544 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn103, sn104, sn108, sn109, sn111, sn113, sn120, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 23 | 24.85 | 35.0 | 15.0 | 9.99 | 1.0 |
| 107 | 18.55 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 17.23 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.3 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.13 | 35.0 | 15.0 | 9.69 | 1.0 |
| 62 | 26.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 26.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.47 | 35.0 | 11.25 | 9.72 | 1.0 |
| 56 | 22.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 8.63 | 35.0 | 15.0 | 7.61 | 1.0 |
| 124 | 21.58 | 35.0 | 11.25 | 9.87 | 0.85 |
| 74 | 21.39 | 35.0 | 11.25 | 9.96 | 0.85 |
| 38 | 20.89 | 35.0 | 11.25 | 9.76 | 0.85 |
| 41 | 6.75 | 35.0 | 15.0 | 8.6 | 1.0 |
| 21 | 6.66 | 35.0 | 15.0 | 8.56 | 1.0 |
| 53 | 19.26 | 35.0 | 11.25 | 10.0 | 0.85 |
| 80 | 16.78 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 12.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 9 | 35.8 | 35.0 | 11.25 | 10.0 | 0.6 |
| 28 | 7.76 | 35.0 | 11.25 | 8.97 | 0.85 |
| 97 | 31.46 | 35.0 | 11.25 | 9.99 | 0.6 |
| 85 | 18.85 | 21.0 | 11.25 | 10.0 | 0.85 |
| 101 | 0.07 | 35.0 | 15.0 | 0.0 | 1.0 |
| 60 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
| 11 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
