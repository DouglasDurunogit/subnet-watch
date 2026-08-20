# RANKING - generated 2026-08-20T12:15:25Z, block 8885947

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
| 1 | 76 | Phylax | 76.7 | 1.0 | 69.35 | 123 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.1d ago |
| 2 | 23 | Trishool | 72.1 | 0.85 | 532 | 532 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.3d ago |
| 3 | 67 | Harnyx | 72.0 | 1.0 | 21.38 | 284 | cpu-small | 0.058 | 171 | 8% | SCORING_COMMIT 0.1d ago |
| 4 | 15 | ORO | 70.3 | 1.0 | 18.63 | 18,531 | cpu-small | 0.000 | 81 | 92% | SCORING_COMMIT 1.7d ago |
| 5 | 1 | Apex | 69.8 | 0.85 | 708 | 1,201 | rtx4090 | 0.556 | 4 | 56% | RELEASE 0.6d ago |
| 6 | 56 | Gradients | 69.6 | 0.85 | 667 | 1,015 | rtx4090 | 0.723 | 5 | 72% | SCORING_COMMIT 2.5d ago |
| 7 | 91 | cascade | 69.2 | 0.85 | 593 | 2,395 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.3d ago |
| 8 | 38 | ChronoLLM | 67.6 | 0.85 | 152 | 3,228 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.6d ago |
| 9 | 26 | Perturb | 67.2 | 1.0 | 16.89 | 244 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.4d ago |
| 10 | 96 | Verathos | 65.7 | 1.0 | 11.80 | 325 | rtx4090 | 0.404 | 95 | 40% | RELEASE 1.8d ago |
| 11 | 107 | Minos | 64.5 | 1.0 | 126 | 37,272 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 12 | 85 | Vidaio | 64.1 | 0.85 | 128 | 401 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.2d ago |
| 13 | 108 | Prometheon | 63.8 | 0.85 | 117 | 172 | rtx4090 | 0.659 | 7 | 66% | SCORING_COMMIT 0.4d ago |
| 14 | 28 | gm | 63.1 | 0.85 | 94.72 | 924 | rtx4090 | 0.000 | 49 | 8% | RELEASE 0.0d ago |
| 15 | 60 | Bitsec.ai | 62.1 | 0.85 | 947 | 947 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 16 | 51 | lium.io | 62.0 | 0.85 | 76.09 | 1,157 | rtx4090 | 0.000 | 44 | 82% | SCORING_COMMIT 0.2d ago |
| 17 | 55 | NIOME | 61.6 | 0.85 | 59.83 | 500 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 5.7d ago |
| 18 | 81 | Reliquary | 61.3 | 0.85 | 54.37 | 217 | rtx4090 | 0.002 | 54 | 5% | SCORING_COMMIT 0.6d ago |
| 19 | 53 | engy | 59.9 | 0.85 | 35.44 | 236 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 1.9d ago |
| 20 | 41 | Almanac | 55.3 | 1.0 | 11.32 | 24.28 | cpu-small | 0.722 | 76 | 72% | SCORING_COMMIT 8d ago |
| 21 | 68 | NOVA | 55.1 | 0.6 | 8,283 | 8,283 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 3.9d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 6,919 | 6,919 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.7d ago |
| 23 | 124 | Swarm | 54.4 | 0.85 | 257 | 748 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |
| 24 | 80 | OpenRoboto | 53.7 | 0.85 | 197 | 709 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 12d ago |
| 25 | 33 | ReadyAI | 53.4 | 0.85 | 5.76 | 10.96 | rtx4090 | 0.000 | 243 | 1% | SCORING_COMMIT 1.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.96 | cpu-small | 377.1245770350465 |
| 54 | Yanez | -3.69 | a4000 | 1075.831526082164 |
| 123 | MANTIS | -5.71 | rtx4090 | 93.4729938274138 |
| 75 | Hippius | -6.12 | rtx4090 | 12360.671661127046 |
| 114 | SOMA | -8.12 | rtx4090 | 4232.68321604074 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 125.62118608454576 |
| 104 | Masx.ai | -1.24 | rtx4090 | 8.379939671322855 |
| 13 | Data Universe | -3.63 | rtx4090 | 5.5727985585376265 |
| 88 | Investing | -4.28 | rtx4090 | 974.4875347250893 |
| 8 | Vanta | -7.95 | rtx4090 | 2915.055151423036 |
| 43 | Graphite | -0.79 | cpu-small | 25.11607390628447 |
| 45 | AlphaRidge.ai | -4.63 | rtx4090 | 11.271888584816496 |
| 18 | Zeus | -5.31 | rtx4090 | 1114.3264777352356 |
| 19 | blockmachine | -7.88 | rtx4090 | 69.64079070676542 |
| 63 | Enigma | -8.14 | rtx4090 | 5092.4759760050865 |
| 105 | Beam | -2.50 | rtx4090 | 77.1655268052407 |
| 84 | ansuz | -8.16 | rtx4090 | 462.4811117764921 |
| 34 | BitMind | -20.02 | a100-80 | 28.947893739704657 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn78, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.8 | 35.0 | 15.0 | 9.9 | 1.0 |
| 23 | 24.8 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.28 | 35.0 | 15.0 | 9.73 | 1.0 |
| 15 | 11.76 | 35.0 | 15.0 | 8.56 | 1.0 |
| 1 | 25.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 25.69 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.23 | 35.0 | 11.25 | 9.98 | 0.85 |
| 38 | 19.87 | 35.0 | 15.0 | 9.66 | 0.85 |
| 26 | 11.39 | 35.0 | 11.25 | 9.59 | 1.0 |
| 96 | 10.07 | 35.0 | 11.25 | 9.41 | 1.0 |
| 107 | 19.14 | 21.0 | 15.0 | 9.37 | 1.0 |
| 85 | 19.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.84 | 35.0 | 11.25 | 9.97 | 0.85 |
| 28 | 18.02 | 35.0 | 11.25 | 9.93 | 0.85 |
| 60 | 27.08 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 17.16 | 35.0 | 11.25 | 9.54 | 0.85 |
| 55 | 16.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 15.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.92 | 21.0 | 15.0 | 9.38 | 1.0 |
| 68 | 35.64 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.93 | 35.0 | 11.25 | 9.97 | 0.6 |
| 124 | 21.93 | 21.0 | 11.25 | 9.86 | 0.85 |
| 80 | 20.88 | 21.0 | 11.25 | 10.0 | 0.85 |
| 33 | 7.55 | 35.0 | 11.25 | 9.03 | 0.85 |
