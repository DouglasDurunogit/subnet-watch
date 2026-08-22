# RANKING - generated 2026-08-22T09:50:54Z, block 8899623

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
| 1 | 76 | Phylax | 77.3 | 1.0 | 80.09 | 134 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.0d ago |
| 2 | 23 | Trishool | 72.3 | 0.85 | 570 | 570 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 2.2d ago |
| 3 | 67 | Harnyx | 72.3 | 1.0 | 23.18 | 452 | cpu-small | 0.091 | 140 | 12% | SCORING_COMMIT 1.0d ago |
| 4 | 102 | ConnitoAI | 71.9 | 0.85 | 1,287 | 2,439 | rtx4090 | 0.250 | 6 | 36% | RELEASE 0.7d ago |
| 5 | 56 | Gradients | 70.0 | 0.85 | 751 | 1,086 | rtx4090 | 0.726 | 5 | 73% | SCORING_COMMIT 4.4d ago |
| 6 | 91 | cascade | 70.0 | 0.85 | 746 | 3,008 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.4d ago |
| 7 | 15 | ORO | 69.5 | 1.0 | 17.64 | 21,954 | cpu-small | 0.000 | 59 | 95% | SCORING_COMMIT 0.4d ago |
| 8 | 1 | Apex | 68.6 | 0.85 | 492 | 1,159 | rtx4090 | 0.541 | 5 | 54% | RELEASE 0.8d ago |
| 9 | 26 | Perturb | 67.5 | 1.0 | 18.14 | 260 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.3d ago |
| 10 | 96 | Verathos | 67.1 | 1.0 | 16.40 | 447 | rtx4090 | 0.404 | 96 | 40% | RELEASE 3.7d ago |
| 11 | 38 | ChronoLLM | 66.6 | 0.85 | 117 | 1,597 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.5d ago |
| 12 | 107 | Minos | 65.2 | 1.0 | 146 | 45,004 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 13 | 85 | Vidaio | 64.4 | 0.85 | 137 | 412 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.1d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 121 | 130 | rtx4090 | 0.658 | 8 | 66% | SCORING_COMMIT 0.8d ago |
| 15 | 81 | Reliquary | 63.3 | 0.85 | 101 | 223 | rtx4090 | 0.002 | 42 | 5% | SCORING_COMMIT 0.9d ago |
| 16 | 53 | engy | 59.9 | 0.85 | 35.25 | 235 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.2d ago |
| 17 | 60 | Bitsec.ai | 59.7 | 0.85 | 462 | 462 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 18 | 28 | gm | 59.3 | 0.85 | 31.58 | 1,415 | rtx4090 | 0.199 | 55 | 20% | RELEASE 1.8d ago |
| 19 | 51 | lium.io | 58.9 | 0.85 | 34.72 | 5,354 | rtx4090 | 0.000 | 53 | 66% | SCORING_COMMIT 2.1d ago |
| 20 | 61 | RedTeam | 58.1 | 0.85 | 20.45 | 283 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.1d ago |
| 21 | 68 | NOVA | 55.3 | 0.6 | 8,863 | 8,863 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 5.8d ago |
| 22 | 41 | Almanac | 55.2 | 1.0 | 11.08 | 24.16 | cpu-small | 0.736 | 78 | 74% | SCORING_COMMIT 9d ago |
| 23 | 120 | Affine | 54.9 | 0.6 | 7,366 | 7,366 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.6d ago |
| 24 | 124 | Swarm | 54.7 | 0.85 | 275 | 2,398 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |
| 25 | 80 | OpenRoboto | 54.0 | 0.85 | 219 | 788 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 14d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.19 | a4000 | 1202.018333728211 |
| 89 | InfiniteQuant | -2.29 | rtx4090 | 113.55624769569027 |
| 13 | Data Universe | -2.95 | rtx4090 | 6.962234901234585 |
| 18 | Zeus | -3.45 | rtx4090 | 2145.868309757881 |
| 123 | MANTIS | -5.53 | rtx4090 | 107.02559891120306 |
| 75 | Hippius | -6.24 | rtx4090 | 11638.422178608354 |
| 34 | BitMind | -18.63 | a100-80 | 328.3040001166237 |
| 101 | Tag101 | -0.05 | cpu-small | 2.43917895417352 |
| 6 | Numinous | -0.93 | cpu-small | 339.7837796691032 |
| 50 | Synth | -0.79 | rtx4090 | 117.67199323541274 |
| 104 | Masx.ai | -1.36 | rtx4090 | 8.948620879561886 |
| 88 | Investing | -3.07 | rtx4090 | 707.4212257754833 |
| 8 | Vanta | -7.37 | rtx4090 | 1095.0618838244834 |
| 43 | Graphite | -0.42 | cpu-small | 193.61399847660886 |
| 19 | blockmachine | -1.33 | rtx4090 | 547.2365500948638 |
| 45 | AlphaRidge.ai | -4.63 | rtx4090 | 11.23522589300456 |
| 22 | Desearch | -5.91 | rtx4090 | 83.44210143041404 |
| 63 | Enigma | -8.14 | rtx4090 | 5456.756083015584 |
| 105 | Beam | -2.02 | rtx4090 | 80.12386314568502 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07060054155241012 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.36 | 35.0 | 15.0 | 9.91 | 1.0 |
| 23 | 25.07 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.58 | 35.0 | 15.0 | 9.73 | 1.0 |
| 102 | 28.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 26.16 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.13 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 11.55 | 35.0 | 15.0 | 7.9 | 1.0 |
| 1 | 24.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 11.66 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.28 | 35.0 | 11.25 | 9.54 | 1.0 |
| 38 | 18.84 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.71 | 21.0 | 15.0 | 9.49 | 1.0 |
| 85 | 19.46 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.96 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.27 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.25 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.76 | 35.0 | 11.25 | 9.76 | 0.85 |
| 51 | 14.12 | 35.0 | 11.25 | 8.91 | 0.85 |
| 61 | 12.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.9 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.84 | 21.0 | 15.0 | 9.32 | 1.0 |
| 120 | 35.17 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.2 | 21.0 | 11.25 | 9.86 | 0.85 |
| 80 | 21.31 | 21.0 | 11.25 | 10.0 | 0.85 |
