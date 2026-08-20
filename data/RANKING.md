# RANKING - generated 2026-08-20T21:12:31Z, block 8888631

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 74.52 | 125 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.5d ago |
| 2 | 67 | Harnyx | 72.1 | 1.0 | 21.37 | 284 | cpu-small | 0.032 | 175 | 8% | SCORING_COMMIT 0.5d ago |
| 3 | 23 | Trishool | 72.0 | 0.85 | 518 | 518 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.7d ago |
| 4 | 15 | ORO | 70.2 | 1.0 | 19.09 | 18,645 | cpu-small | 0.000 | 82 | 92% | SCORING_COMMIT 2.1d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 672 | 1,026 | rtx4090 | 0.723 | 5 | 72% | SCORING_COMMIT 2.9d ago |
| 6 | 91 | cascade | 69.3 | 0.85 | 604 | 2,442 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.7d ago |
| 7 | 1 | Apex | 68.1 | 0.85 | 426 | 1,207 | rtx4090 | 0.528 | 5 | 53% | RELEASE 1.0d ago |
| 8 | 38 | ChronoLLM | 67.7 | 0.85 | 154 | 3,277 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.0d ago |
| 9 | 11 | TrajectoryRL | 67.3 | 0.85 | 4,481 | 4,481 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 18d ago |
| 10 | 26 | Perturb | 67.3 | 1.0 | 17.08 | 246 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.8d ago |
| 11 | 96 | Verathos | 67.0 | 1.0 | 16.18 | 368 | rtx4090 | 0.404 | 94 | 40% | RELEASE 2.2d ago |
| 12 | 85 | Vidaio | 64.5 | 0.85 | 145 | 413 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.6d ago |
| 13 | 107 | Minos | 64.4 | 1.0 | 125 | 36,235 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 119 | 175 | rtx4090 | 0.662 | 7 | 66% | SCORING_COMMIT 0.8d ago |
| 15 | 28 | gm | 61.7 | 0.85 | 63.71 | 1,553 | rtx4090 | 0.123 | 53 | 14% | RELEASE 0.3d ago |
| 16 | 55 | NIOME | 61.7 | 0.85 | 62.11 | 519 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 6.0d ago |
| 17 | 51 | lium.io | 61.5 | 0.85 | 66.79 | 1,192 | rtx4090 | 0.000 | 47 | 82% | SCORING_COMMIT 0.5d ago |
| 18 | 81 | Reliquary | 61.4 | 0.85 | 56.70 | 204 | rtx4090 | 0.002 | 50 | 5% | SCORING_COMMIT 1.0d ago |
| 19 | 60 | Bitsec.ai | 61.2 | 0.85 | 726 | 1,016 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 20 | 102 | ConnitoAI | 60.1 | 0.85 | 1,355 | 1,628 | rtx4090 | 0.250 | 5 | 28% | RELEASE 20d ago |
| 21 | 53 | engy | 60.0 | 0.85 | 36.92 | 245 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.2d ago |
| 22 | 41 | Almanac | 55.3 | 1.0 | 11.33 | 23.41 | cpu-small | 0.721 | 77 | 72% | SCORING_COMMIT 8d ago |
| 23 | 68 | NOVA | 55.2 | 0.6 | 8,376 | 8,376 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.3d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,161 | 7,161 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.0d ago |
| 25 | 124 | Swarm | 54.4 | 0.85 | 254 | 740 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.42 | cpu-small | 4.71849152253195 |
| 54 | Yanez | -3.69 | a4000 | 1081.8960110810337 |
| 18 | Zeus | -3.76 | rtx4090 | 1613.6157502147132 |
| 13 | Data Universe | -4.38 | rtx4090 | 7.2137726398918485 |
| 123 | MANTIS | -5.75 | rtx4090 | 94.80260168992191 |
| 75 | Hippius | -5.96 | rtx4090 | 12724.356913190697 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 126.22217891817762 |
| 6 | Numinous | -0.96 | cpu-small | 377.7873245887807 |
| 104 | Masx.ai | -2.66 | rtx4090 | 8.918885132567167 |
| 88 | Investing | -4.44 | rtx4090 | 958.1439456389755 |
| 8 | Vanta | -7.42 | rtx4090 | 3581.576943035348 |
| 43 | Graphite | -0.79 | cpu-small | 25.40968464639743 |
| 32 | ItsAI | -0.21 | rtx4090 | 11.285602227674937 |
| 22 | Desearch | -0.80 | rtx4090 | 110.30683915568807 |
| 19 | blockmachine | -1.12 | rtx4090 | 1490.9798671731915 |
| 45 | AlphaRidge.ai | -4.55 | rtx4090 | 10.770964266649996 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07860554296244388 |
| 105 | Beam | -2.34 | rtx4090 | 77.23925929019246 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06437377692133844 |
| 34 | BitMind | -19.71 | a100-80 | 3066.12782894809 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn2, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.08 | 35.0 | 15.0 | 9.91 | 1.0 |
| 67 | 12.28 | 35.0 | 15.0 | 9.84 | 1.0 |
| 23 | 24.69 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 11.85 | 35.0 | 15.0 | 8.36 | 1.0 |
| 56 | 25.72 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.3 | 35.0 | 11.25 | 9.98 | 0.85 |
| 1 | 23.93 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.93 | 35.0 | 15.0 | 9.66 | 0.85 |
| 11 | 33.21 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.43 | 35.0 | 11.25 | 9.59 | 1.0 |
| 96 | 11.23 | 35.0 | 11.25 | 9.56 | 1.0 |
| 85 | 19.68 | 35.0 | 11.25 | 10.0 | 0.85 |
| 107 | 19.1 | 21.0 | 15.0 | 9.3 | 1.0 |
| 108 | 18.9 | 35.0 | 11.25 | 9.97 | 0.85 |
| 28 | 16.47 | 35.0 | 11.25 | 9.89 | 0.85 |
| 55 | 16.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.65 | 35.0 | 11.25 | 9.47 | 0.85 |
| 81 | 16.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.02 | 21.0 | 15.0 | 10.0 | 0.85 |
| 102 | 28.49 | 21.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.92 | 21.0 | 15.0 | 9.38 | 1.0 |
| 68 | 35.68 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.06 | 35.0 | 11.25 | 9.98 | 0.6 |
| 124 | 21.89 | 21.0 | 11.25 | 9.86 | 0.85 |
