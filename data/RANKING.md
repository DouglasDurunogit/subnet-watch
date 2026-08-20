# RANKING - generated 2026-08-20T10:56:38Z, block 8885553

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
| 1 | 76 | Phylax | 76.8 | 1.0 | 70.27 | 125 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.0d ago |
| 2 | 23 | Trishool | 72.1 | 0.85 | 539 | 539 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.3d ago |
| 3 | 67 | Harnyx | 72.0 | 1.0 | 21.10 | 373 | cpu-small | 0.082 | 166 | 10% | SCORING_COMMIT 0.0d ago |
| 4 | 15 | ORO | 70.3 | 1.0 | 19.02 | 18,895 | cpu-small | 0.000 | 81 | 92% | SCORING_COMMIT 1.7d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 677 | 1,029 | rtx4090 | 0.722 | 5 | 72% | SCORING_COMMIT 2.5d ago |
| 6 | 91 | cascade | 69.3 | 0.85 | 611 | 2,467 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.2d ago |
| 7 | 38 | ChronoLLM | 67.7 | 0.85 | 154 | 3,277 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.6d ago |
| 8 | 26 | Perturb | 67.3 | 1.0 | 17.15 | 247 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.4d ago |
| 9 | 1 | Apex | 66.2 | 0.85 | 236 | 1,827 | rtx4090 | 0.533 | 4 | 53% | RELEASE 0.6d ago |
| 10 | 96 | Verathos | 65.9 | 1.0 | 12.27 | 293 | rtx4090 | 0.404 | 97 | 40% | RELEASE 1.8d ago |
| 11 | 107 | Minos | 64.6 | 1.0 | 130 | 38,624 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 12 | 85 | Vidaio | 64.5 | 0.85 | 143 | 406 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.2d ago |
| 13 | 108 | Prometheon | 63.9 | 0.85 | 119 | 175 | rtx4090 | 0.659 | 7 | 66% | SCORING_COMMIT 0.4d ago |
| 14 | 60 | Bitsec.ai | 62.1 | 0.85 | 952 | 952 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 15 | 28 | gm | 62.0 | 0.85 | 69.56 | 2,454 | rtx4090 | 0.103 | 49 | 22% | RELEASE 0.9d ago |
| 16 | 55 | NIOME | 61.7 | 0.85 | 61.48 | 510 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 5.6d ago |
| 17 | 51 | lium.io | 61.3 | 0.85 | 63.31 | 1,225 | rtx4090 | 0.000 | 47 | 80% | SCORING_COMMIT 0.1d ago |
| 18 | 81 | Reliquary | 61.3 | 0.85 | 54.81 | 227 | rtx4090 | 0.002 | 54 | 5% | SCORING_COMMIT 0.5d ago |
| 19 | 53 | engy | 59.9 | 0.85 | 35.94 | 239 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 1.8d ago |
| 20 | 41 | Almanac | 55.4 | 1.0 | 11.67 | 24.56 | cpu-small | 0.717 | 76 | 72% | SCORING_COMMIT 7d ago |
| 21 | 68 | NOVA | 55.2 | 0.6 | 8,389 | 8,389 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 3.9d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 7,011 | 7,011 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.6d ago |
| 23 | 124 | Swarm | 54.5 | 0.85 | 260 | 758 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |
| 24 | 80 | OpenRoboto | 53.7 | 0.85 | 201 | 724 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 12d ago |
| 25 | 33 | ReadyAI | 53.4 | 0.85 | 5.89 | 11.26 | rtx4090 | 0.000 | 243 | 1% | SCORING_COMMIT 1.8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.96 | cpu-small | 382.0090814975408 |
| 54 | Yanez | -3.49 | a4000 | 1085.1135940388656 |
| 123 | MANTIS | -5.70 | rtx4090 | 93.73346821797259 |
| 75 | Hippius | -6.09 | rtx4090 | 12545.577361101175 |
| 114 | SOMA | -8.12 | rtx4090 | 4288.852529771905 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 116.34717940870695 |
| 104 | Masx.ai | -2.60 | rtx4090 | 8.238996600169179 |
| 13 | Data Universe | -3.51 | rtx4090 | 5.412588907968802 |
| 88 | Investing | -4.25 | rtx4090 | 982.2636074651294 |
| 8 | Vanta | -7.95 | rtx4090 | 2950.0997059744323 |
| 43 | Graphite | -0.79 | cpu-small | 25.54088035165548 |
| 18 | Zeus | -5.26 | rtx4090 | 1130.9073306949037 |
| 45 | AlphaRidge.ai | -5.43 | rtx4090 | 10.454269942298785 |
| 19 | blockmachine | -7.88 | rtx4090 | 70.55153127496955 |
| 63 | Enigma | -8.14 | rtx4090 | 5163.366881106441 |
| 105 | Beam | -2.33 | rtx4090 | 79.42765599826652 |
| 84 | ansuz | -8.15 | rtx4090 | 468.4932933759836 |
| 34 | BitMind | -19.84 | a100-80 | 29.436836443460283 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn78, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.85 | 35.0 | 15.0 | 9.9 | 1.0 |
| 23 | 24.85 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.23 | 35.0 | 15.0 | 9.77 | 1.0 |
| 15 | 11.84 | 35.0 | 15.0 | 8.48 | 1.0 |
| 56 | 25.75 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.34 | 35.0 | 11.25 | 9.99 | 0.85 |
| 38 | 19.93 | 35.0 | 15.0 | 9.66 | 0.85 |
| 26 | 11.45 | 35.0 | 11.25 | 9.59 | 1.0 |
| 1 | 21.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 10.21 | 35.0 | 11.25 | 9.42 | 1.0 |
| 107 | 19.24 | 21.0 | 15.0 | 9.4 | 1.0 |
| 85 | 19.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.91 | 35.0 | 11.25 | 9.97 | 0.85 |
| 60 | 27.1 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 16.81 | 35.0 | 11.25 | 9.9 | 0.85 |
| 55 | 16.33 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.45 | 35.0 | 11.25 | 9.44 | 0.85 |
| 81 | 15.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.26 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.03 | 21.0 | 15.0 | 9.39 | 1.0 |
| 68 | 35.69 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.98 | 35.0 | 11.25 | 9.98 | 0.6 |
| 124 | 21.98 | 21.0 | 11.25 | 9.86 | 0.85 |
| 80 | 20.97 | 21.0 | 11.25 | 10.0 | 0.85 |
| 33 | 7.63 | 35.0 | 11.25 | 8.98 | 0.85 |
