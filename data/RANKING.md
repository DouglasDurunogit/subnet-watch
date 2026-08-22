# RANKING - generated 2026-08-22T08:03:13Z, block 8899085

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
| 1 | 76 | Phylax | 77.3 | 1.0 | 80.89 | 136 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 2.9d ago |
| 2 | 102 | ConnitoAI | 72.9 | 0.85 | 1,778 | 1,780 | rtx4090 | 0.254 | 4 | 26% | RELEASE 0.7d ago |
| 3 | 23 | Trishool | 72.4 | 0.85 | 579 | 579 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 2.2d ago |
| 4 | 67 | Harnyx | 72.4 | 1.0 | 23.41 | 456 | cpu-small | 0.106 | 137 | 12% | SCORING_COMMIT 0.9d ago |
| 5 | 91 | cascade | 69.9 | 0.85 | 725 | 2,926 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.4d ago |
| 6 | 56 | Gradients | 69.9 | 0.85 | 711 | 1,096 | rtx4090 | 0.726 | 5 | 73% | SCORING_COMMIT 4.3d ago |
| 7 | 15 | ORO | 69.3 | 1.0 | 17.89 | 22,248 | cpu-small | 0.000 | 59 | 95% | SCORING_COMMIT 0.4d ago |
| 8 | 1 | Apex | 68.7 | 0.85 | 499 | 1,177 | rtx4090 | 0.538 | 5 | 54% | RELEASE 0.7d ago |
| 9 | 26 | Perturb | 67.5 | 1.0 | 18.33 | 262 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.3d ago |
| 10 | 96 | Verathos | 66.9 | 1.0 | 15.74 | 475 | rtx4090 | 0.405 | 92 | 41% | RELEASE 3.7d ago |
| 11 | 38 | ChronoLLM | 66.7 | 0.85 | 118 | 1,616 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.5d ago |
| 12 | 107 | Minos | 65.4 | 1.0 | 151 | 45,261 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 13 | 98 | NeverPlayAlone | 64.5 | 0.85 | 1,953 | 1,953 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 15d ago |
| 14 | 85 | Vidaio | 64.0 | 0.85 | 122 | 412 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.0d ago |
| 15 | 81 | Reliquary | 63.2 | 0.85 | 96.57 | 221 | rtx4090 | 0.002 | 43 | 5% | SCORING_COMMIT 0.8d ago |
| 16 | 108 | Prometheon | 61.5 | 0.85 | 59.41 | 409 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 0.8d ago |
| 17 | 51 | lium.io | 60.4 | 0.85 | 50.15 | 5,058 | rtx4090 | 0.000 | 52 | 68% | SCORING_COMMIT 2.0d ago |
| 18 | 53 | engy | 59.9 | 0.85 | 35.83 | 239 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.2d ago |
| 19 | 60 | Bitsec.ai | 59.7 | 0.85 | 467 | 467 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 20 | 61 | RedTeam | 58.2 | 0.85 | 20.82 | 282 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.0d ago |
| 21 | 28 | gm | 58.0 | 0.85 | 21.97 | 1,632 | rtx4090 | 0.138 | 55 | 14% | RELEASE 1.7d ago |
| 22 | 68 | NOVA | 55.3 | 0.6 | 8,940 | 8,940 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 5.8d ago |
| 23 | 41 | Almanac | 55.2 | 1.0 | 11.24 | 24.39 | cpu-small | 0.735 | 78 | 74% | SCORING_COMMIT 9d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,650 | 7,650 | rtx4090 | 0.000 | 5 | 21% | SCORING_COMMIT 3.5d ago |
| 25 | 124 | Swarm | 54.7 | 0.85 | 279 | 2,431 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.01 | a4000 | 1211.8853410968582 |
| 89 | InfiniteQuant | -2.84 | rtx4090 | 115.99110480329206 |
| 13 | Data Universe | -2.90 | rtx4090 | 6.967829530974375 |
| 18 | Zeus | -3.67 | rtx4090 | 2074.4764977688237 |
| 123 | MANTIS | -5.51 | rtx4090 | 106.71926403129181 |
| 75 | Hippius | -6.23 | rtx4090 | 11716.147850959787 |
| 34 | BitMind | -19.17 | a100-80 | 331.12044809279337 |
| 101 | Tag101 | -0.09 | cpu-small | 2.3170949628575506 |
| 6 | Numinous | -0.93 | cpu-small | 349.8307879494545 |
| 50 | Synth | -0.23 | rtx4090 | 111.15736332735976 |
| 104 | Masx.ai | -3.15 | rtx4090 | 10.992629196024865 |
| 88 | Investing | -4.10 | rtx4090 | 714.556207509703 |
| 8 | Vanta | -7.36 | rtx4090 | 1104.5103371819987 |
| 43 | Graphite | -0.73 | cpu-small | 195.94861344839487 |
| 19 | blockmachine | -1.27 | rtx4090 | 551.9617788363715 |
| 45 | AlphaRidge.ai | -5.19 | rtx4090 | 17.41023958654201 |
| 22 | Desearch | -5.76 | rtx4090 | 108.75336666831463 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08399384449558168 |
| 105 | Beam | -2.02 | rtx4090 | 80.81589467407687 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07122644062537722 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.4 | 35.0 | 15.0 | 9.91 | 1.0 |
| 102 | 29.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.13 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.62 | 35.0 | 15.0 | 9.76 | 1.0 |
| 91 | 26.02 | 35.0 | 11.25 | 9.99 | 0.85 |
| 56 | 25.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.61 | 35.0 | 15.0 | 7.66 | 1.0 |
| 1 | 24.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 11.7 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.13 | 35.0 | 11.25 | 9.52 | 1.0 |
| 38 | 18.89 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.85 | 21.0 | 15.0 | 9.5 | 1.0 |
| 98 | 29.93 | 21.0 | 15.0 | 10.0 | 0.85 |
| 85 | 19.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 18.09 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 16.2 | 35.0 | 11.25 | 9.94 | 0.85 |
| 51 | 15.54 | 35.0 | 11.25 | 9.24 | 0.85 |
| 53 | 14.25 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.29 | 21.0 | 15.0 | 10.0 | 0.85 |
| 61 | 12.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 12.38 | 35.0 | 11.25 | 9.65 | 0.85 |
| 68 | 35.94 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.89 | 21.0 | 15.0 | 9.32 | 1.0 |
| 120 | 35.32 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.26 | 21.0 | 11.25 | 9.86 | 0.85 |
