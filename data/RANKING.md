# RANKING - generated 2026-08-20T11:37:35Z, block 8885758

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
| 1 | 76 | Phylax | 76.7 | 1.0 | 70.21 | 124 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.1d ago |
| 2 | 23 | Trishool | 72.1 | 0.85 | 539 | 539 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.3d ago |
| 3 | 67 | Harnyx | 72.1 | 1.0 | 21.51 | 287 | cpu-small | 0.073 | 168 | 8% | SCORING_COMMIT 0.1d ago |
| 4 | 15 | ORO | 70.2 | 1.0 | 18.98 | 18,861 | cpu-small | 0.000 | 81 | 92% | SCORING_COMMIT 1.7d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 676 | 1,028 | rtx4090 | 0.722 | 5 | 72% | SCORING_COMMIT 2.5d ago |
| 6 | 91 | cascade | 69.3 | 0.85 | 597 | 2,412 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.3d ago |
| 7 | 38 | ChronoLLM | 67.6 | 0.85 | 154 | 3,266 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.6d ago |
| 8 | 26 | Perturb | 67.3 | 1.0 | 17.13 | 247 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.4d ago |
| 9 | 1 | Apex | 66.2 | 0.85 | 235 | 1,821 | rtx4090 | 0.534 | 4 | 53% | RELEASE 0.6d ago |
| 10 | 96 | Verathos | 65.9 | 1.0 | 12.24 | 292 | rtx4090 | 0.404 | 97 | 40% | RELEASE 1.8d ago |
| 11 | 107 | Minos | 64.7 | 1.0 | 130 | 38,630 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 12 | 85 | Vidaio | 64.5 | 0.85 | 143 | 406 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.2d ago |
| 13 | 108 | Prometheon | 63.8 | 0.85 | 118 | 174 | rtx4090 | 0.659 | 7 | 66% | SCORING_COMMIT 0.4d ago |
| 14 | 28 | gm | 63.1 | 0.85 | 96.55 | 941 | rtx4090 | 0.000 | 49 | 8% | RELEASE 0.9d ago |
| 15 | 60 | Bitsec.ai | 62.1 | 0.85 | 956 | 956 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 16 | 51 | lium.io | 61.7 | 0.85 | 70.85 | 1,173 | rtx4090 | 0.000 | 44 | 81% | SCORING_COMMIT 0.1d ago |
| 17 | 55 | NIOME | 61.7 | 0.85 | 60.98 | 511 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 5.6d ago |
| 18 | 81 | Reliquary | 61.3 | 0.85 | 54.69 | 226 | rtx4090 | 0.002 | 54 | 5% | SCORING_COMMIT 0.6d ago |
| 19 | 53 | engy | 59.9 | 0.85 | 35.57 | 237 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 1.8d ago |
| 20 | 41 | Almanac | 55.4 | 1.0 | 11.56 | 24.53 | cpu-small | 0.719 | 76 | 72% | SCORING_COMMIT 8d ago |
| 21 | 68 | NOVA | 55.2 | 0.6 | 8,383 | 8,383 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 3.9d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 7,006 | 7,006 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.6d ago |
| 23 | 124 | Swarm | 54.5 | 0.85 | 259 | 753 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |
| 24 | 80 | OpenRoboto | 53.7 | 0.85 | 199 | 717 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 12d ago |
| 25 | 33 | ReadyAI | 53.4 | 0.85 | 5.96 | 11.23 | rtx4090 | 0.000 | 244 | 1% | SCORING_COMMIT 1.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.96 | cpu-small | 381.6809969654991 |
| 54 | Yanez | -3.54 | a4000 | 1084.4784324972375 |
| 123 | MANTIS | -5.70 | rtx4090 | 93.8659802293065 |
| 75 | Hippius | -6.09 | rtx4090 | 12538.014187336226 |
| 114 | SOMA | -8.12 | rtx4090 | 4268.277893779036 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 116.24654484967417 |
| 104 | Masx.ai | -2.61 | rtx4090 | 8.231824072878917 |
| 13 | Data Universe | -3.57 | rtx4090 | 5.645657263752623 |
| 88 | Investing | -4.23 | rtx4090 | 986.7565734391568 |
| 8 | Vanta | -7.95 | rtx4090 | 2949.573470202089 |
| 43 | Graphite | -0.84 | cpu-small | 24.575532855445676 |
| 45 | AlphaRidge.ai | -4.98 | rtx4090 | 10.421192284546388 |
| 18 | Zeus | -5.27 | rtx4090 | 1129.9350110863613 |
| 19 | blockmachine | -7.88 | rtx4090 | 70.48329518694567 |
| 63 | Enigma | -8.14 | rtx4090 | 5153.766488154818 |
| 105 | Beam | -2.34 | rtx4090 | 79.28385536400273 |
| 84 | ansuz | -8.15 | rtx4090 | 468.0727738239756 |
| 34 | BitMind | -19.90 | a100-80 | 29.29612477177175 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn78, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.85 | 35.0 | 15.0 | 9.9 | 1.0 |
| 23 | 24.85 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.3 | 35.0 | 15.0 | 9.75 | 1.0 |
| 15 | 11.83 | 35.0 | 15.0 | 8.37 | 1.0 |
| 56 | 25.74 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.25 | 35.0 | 11.25 | 9.98 | 0.85 |
| 38 | 19.92 | 35.0 | 15.0 | 9.66 | 0.85 |
| 26 | 11.45 | 35.0 | 11.25 | 9.59 | 1.0 |
| 1 | 21.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 10.2 | 35.0 | 11.25 | 9.42 | 1.0 |
| 107 | 19.24 | 21.0 | 15.0 | 9.46 | 1.0 |
| 85 | 19.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.89 | 35.0 | 11.25 | 9.97 | 0.85 |
| 28 | 18.09 | 35.0 | 11.25 | 9.93 | 0.85 |
| 60 | 27.11 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 16.88 | 35.0 | 11.25 | 9.5 | 0.85 |
| 55 | 16.3 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 15.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.0 | 21.0 | 15.0 | 9.39 | 1.0 |
| 68 | 35.68 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.98 | 35.0 | 11.25 | 9.98 | 0.6 |
| 124 | 21.96 | 21.0 | 11.25 | 9.86 | 0.85 |
| 80 | 20.93 | 21.0 | 11.25 | 10.0 | 0.85 |
| 33 | 7.66 | 35.0 | 11.25 | 8.92 | 0.85 |
