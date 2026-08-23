# RANKING - generated 2026-08-23T21:32:51Z, block 8910333

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 76.93 | 86.12 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.2d ago |
| 2 | 102 | ConnitoAI | 73.0 | 0.85 | 1,817 | 1,817 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.1d ago |
| 3 | 67 | Harnyx | 72.9 | 1.0 | 26.12 | 836 | cpu-small | 0.026 | 125 | 20% | SCORING_COMMIT 2.5d ago |
| 4 | 62 | Ridges | 72.5 | 0.85 | 1,560 | 3,189 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.9d ago |
| 5 | 23 | Trishool | 72.5 | 0.85 | 600 | 600 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.7d ago |
| 6 | 15 | ORO | 71.9 | 1.0 | 27.63 | 47.21 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 1.9d ago |
| 7 | 56 | Gradients | 70.0 | 0.85 | 740 | 1,164 | rtx4090 | 0.731 | 5 | 73% | SCORING_COMMIT 5.9d ago |
| 8 | 91 | cascade | 70.0 | 0.85 | 734 | 2,959 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.9d ago |
| 9 | 1 | Apex | 69.0 | 0.85 | 543 | 1,225 | rtx4090 | 0.548 | 5 | 55% | RELEASE 2.3d ago |
| 10 | 96 | Verathos | 68.6 | 1.0 | 23.92 | 303 | rtx4090 | 0.402 | 90 | 40% | RELEASE 5.2d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.80 | 281 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.8d ago |
| 12 | 124 | Swarm | 66.8 | 0.85 | 297 | 2,581 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.4d ago |
| 13 | 38 | ChronoLLM | 66.8 | 0.85 | 123 | 1,675 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.0d ago |
| 14 | 108 | Prometheon | 65.5 | 0.85 | 194 | 199 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.3d ago |
| 15 | 107 | Minos | 65.3 | 1.0 | 152 | 45,097 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 16 | 81 | Reliquary | 65.2 | 0.85 | 178 | 263 | rtx4090 | 0.003 | 30 | 6% | SCORING_COMMIT 1.1d ago |
| 17 | 85 | Vidaio | 64.5 | 0.85 | 143 | 446 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.6d ago |
| 18 | 60 | Bitsec.ai | 61.6 | 0.85 | 817 | 1,145 | cpu-small | 0.541 | 3 | 54% | SCORING_COMMIT 16d ago |
| 19 | 51 | lium.io | 61.0 | 0.85 | 59.00 | 2,054 | rtx4090 | 0.000 | 54 | 74% | SCORING_COMMIT 3.6d ago |
| 20 | 53 | engy | 60.3 | 0.85 | 40.32 | 339 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.7d ago |
| 21 | 61 | RedTeam | 57.2 | 0.85 | 15.17 | 313 | rtx4090 | 0.000 | 85 | 6% | RELEASE 1.6d ago |
| 22 | 28 | gm | 57.1 | 0.85 | 17.04 | 1,975 | rtx4090 | 0.149 | 53 | 16% | RELEASE 3.3d ago |
| 23 | 41 | Almanac | 56.5 | 1.0 | 15.26 | 29.88 | cpu-small | 0.649 | 79 | 65% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 55.0 | 0.6 | 7,736 | 7,736 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.0d ago |
| 25 | 33 | ReadyAI | 54.4 | 0.85 | 7.05 | 11.65 | rtx4090 | 0.000 | 245 | 1% | SCORING_COMMIT 3.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.31 | a4000 | 1241.0800140398146 |
| 13 | Data Universe | -2.53 | rtx4090 | 7.679053909989181 |
| 18 | Zeus | -3.66 | rtx4090 | 1721.805519758157 |
| 89 | InfiniteQuant | -3.76 | rtx4090 | 120.24284349169648 |
| 123 | MANTIS | -5.57 | rtx4090 | 123.19254613585079 |
| 75 | Hippius | -5.93 | rtx4090 | 12870.181778478554 |
| 34 | BitMind | -18.81 | a100-80 | 353.25056573225953 |
| 6 | Numinous | -0.92 | cpu-small | 193.51267951430864 |
| 50 | Synth | -0.80 | rtx4090 | 68.77935517607446 |
| 104 | Masx.ai | -1.33 | rtx4090 | 11.678161952062322 |
| 88 | Investing | -2.55 | rtx4090 | 710.6605797831738 |
| 8 | Vanta | -7.31 | rtx4090 | 3612.806812252959 |
| 43 | Graphite | -0.47 | cpu-small | 202.59516760487008 |
| 19 | blockmachine | -0.19 | rtx4090 | 700.1843490966968 |
| 22 | Desearch | -1.56 | rtx4090 | 60.8882798646239 |
| 45 | AlphaRidge.ai | -5.36 | rtx4090 | 12.211363898363466 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08903562292613951 |
| 105 | Beam | -1.54 | rtx4090 | 87.38525247063009 |
| 84 | ansuz | -8.14 | rtx4090 | 0.07427174157692958 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.21 | 35.0 | 15.0 | 9.89 | 1.0 |
| 102 | 29.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 13.04 | 35.0 | 15.0 | 9.9 | 1.0 |
| 62 | 29.05 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.27 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 13.25 | 35.0 | 15.0 | 8.63 | 1.0 |
| 56 | 26.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.7 | 35.0 | 11.25 | 9.66 | 1.0 |
| 26 | 11.99 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.5 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 19.03 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.83 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.87 | 21.0 | 15.0 | 9.47 | 1.0 |
| 81 | 20.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.49 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 16.17 | 35.0 | 11.25 | 9.31 | 0.85 |
| 53 | 14.7 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 10.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 11.43 | 35.0 | 11.25 | 9.52 | 0.85 |
| 41 | 11.01 | 21.0 | 15.0 | 9.47 | 1.0 |
| 120 | 35.37 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 8.24 | 35.0 | 11.25 | 9.56 | 0.85 |
