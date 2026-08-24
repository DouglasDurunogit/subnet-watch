# RANKING - generated 2026-08-24T04:13:31Z, block 8912336

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 74.36 | 83.24 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.5d ago |
| 2 | 102 | ConnitoAI | 72.8 | 0.85 | 1,717 | 1,719 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.4d ago |
| 3 | 67 | Harnyx | 72.7 | 1.0 | 24.74 | 793 | cpu-small | 0.020 | 127 | 20% | SCORING_COMMIT 2.7d ago |
| 4 | 62 | Ridges | 72.4 | 0.85 | 1,495 | 3,055 | rtx4090 | 0.000 | 6 | 39% | RELEASE 5.2d ago |
| 5 | 23 | Trishool | 72.3 | 0.85 | 575 | 575 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 4.0d ago |
| 6 | 15 | ORO | 72.1 | 1.0 | 27.21 | 45.73 | cpu-small | 0.000 | 82 | 92% | SCORING_COMMIT 2.2d ago |
| 7 | 56 | Gradients | 69.8 | 0.85 | 707 | 1,115 | rtx4090 | 0.731 | 5 | 73% | SCORING_COMMIT 6.2d ago |
| 8 | 91 | cascade | 69.8 | 0.85 | 702 | 2,831 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 3.2d ago |
| 9 | 1 | Apex | 68.8 | 0.85 | 512 | 1,140 | rtx4090 | 0.546 | 5 | 55% | RELEASE 2.6d ago |
| 10 | 96 | Verathos | 67.7 | 1.0 | 19.17 | 269 | rtx4090 | 0.403 | 96 | 40% | RELEASE 5.5d ago |
| 11 | 26 | Perturb | 67.6 | 1.0 | 18.73 | 267 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 4.1d ago |
| 12 | 11 | TrajectoryRL | 67.5 | 0.85 | 4,760 | 4,760 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 22d ago |
| 13 | 124 | Swarm | 66.8 | 0.85 | 297 | 2,582 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.6d ago |
| 14 | 38 | ChronoLLM | 66.6 | 0.85 | 118 | 1,608 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.3d ago |
| 15 | 108 | Prometheon | 65.4 | 0.85 | 186 | 190 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.6d ago |
| 16 | 107 | Minos | 65.4 | 1.0 | 154 | 43,492 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 14d ago |
| 17 | 85 | Vidaio | 64.2 | 0.85 | 132 | 422 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.9d ago |
| 18 | 60 | Bitsec.ai | 64.1 | 0.85 | 1,702 | 1,702 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 16d ago |
| 19 | 81 | Reliquary | 63.7 | 0.85 | 114 | 234 | rtx4090 | 0.003 | 38 | 5% | SCORING_COMMIT 1.4d ago |
| 20 | 51 | lium.io | 61.3 | 0.85 | 63.81 | 2,134 | rtx4090 | 0.000 | 53 | 72% | SCORING_COMMIT 0.0d ago |
| 21 | 53 | engy | 60.1 | 0.85 | 38.32 | 324 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.0d ago |
| 22 | 28 | gm | 58.1 | 0.85 | 22.12 | 1,625 | rtx4090 | 0.220 | 45 | 22% | RELEASE 3.6d ago |
| 23 | 61 | RedTeam | 56.7 | 0.85 | 13.10 | 304 | rtx4090 | 0.000 | 83 | 6% | RELEASE 1.8d ago |
| 24 | 41 | Almanac | 56.4 | 1.0 | 14.72 | 29.70 | cpu-small | 0.649 | 81 | 65% | SCORING_COMMIT 11d ago |
| 25 | 120 | Affine | 54.9 | 0.6 | 7,407 | 7,407 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.27 | cpu-small | 6.002136966380915 |
| 54 | Yanez | -3.48 | a4000 | 1175.2090448688348 |
| 13 | Data Universe | -2.44 | rtx4090 | 7.750673031989713 |
| 18 | Zeus | -4.01 | rtx4090 | 1334.7352965519924 |
| 89 | InfiniteQuant | -4.32 | rtx4090 | 112.85734177092493 |
| 123 | MANTIS | -5.62 | rtx4090 | 120.45366253117965 |
| 75 | Hippius | -6.00 | rtx4090 | 12506.093810035198 |
| 34 | BitMind | -16.39 | a100-80 | 337.95256768179365 |
| 6 | Numinous | -0.96 | cpu-small | 179.08527855792045 |
| 50 | Synth | -0.92 | rtx4090 | 67.01041652417504 |
| 104 | Masx.ai | -1.28 | rtx4090 | 9.006675316797743 |
| 88 | Investing | -2.83 | rtx4090 | 642.6216880139094 |
| 2 | DSperse | -3.75 | rtx4090 | 356.4211025947042 |
| 8 | Vanta | -7.34 | rtx4090 | 3293.823899116219 |
| 43 | Graphite | -0.26 | cpu-small | 187.16403706685324 |
| 19 | blockmachine | -0.52 | rtx4090 | 671.7887338065614 |
| 45 | AlphaRidge.ai | -4.91 | rtx4090 | 8.720666903845327 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08526958920724703 |
| 105 | Beam | -1.45 | rtx4090 | 88.56298729270064 |
| 84 | ansuz | -8.15 | rtx4090 | 517.8315987947558 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.07 | 35.0 | 15.0 | 9.9 | 1.0 |
| 102 | 29.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.83 | 35.0 | 15.0 | 9.83 | 1.0 |
| 62 | 28.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.1 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 13.19 | 35.0 | 15.0 | 8.86 | 1.0 |
| 56 | 25.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.89 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 11.87 | 35.0 | 11.25 | 9.59 | 1.0 |
| 26 | 11.78 | 35.0 | 11.25 | 9.58 | 1.0 |
| 11 | 33.45 | 21.0 | 15.0 | 10.0 | 0.85 |
| 124 | 22.5 | 35.0 | 11.25 | 9.87 | 0.85 |
| 38 | 18.87 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.66 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.92 | 21.0 | 15.0 | 9.5 | 1.0 |
| 85 | 19.33 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 29.39 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 18.73 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.48 | 35.0 | 11.25 | 9.39 | 0.85 |
| 53 | 14.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 12.41 | 35.0 | 11.25 | 9.65 | 0.85 |
| 61 | 10.45 | 35.0 | 11.25 | 9.97 | 0.85 |
| 41 | 10.88 | 21.0 | 15.0 | 9.47 | 1.0 |
| 120 | 35.2 | 35.0 | 11.25 | 9.99 | 0.6 |
