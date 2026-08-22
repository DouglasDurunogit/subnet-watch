# RANKING - generated 2026-08-22T11:01:55Z, block 8899978

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
| 1 | 76 | Phylax | 77.2 | 1.0 | 79.12 | 133 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.1d ago |
| 2 | 23 | Trishool | 72.3 | 0.85 | 563 | 563 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 2.3d ago |
| 3 | 67 | Harnyx | 72.3 | 1.0 | 22.85 | 446 | cpu-small | 0.089 | 141 | 12% | SCORING_COMMIT 1.0d ago |
| 4 | 102 | ConnitoAI | 71.8 | 0.85 | 1,284 | 2,433 | rtx4090 | 0.250 | 6 | 36% | RELEASE 0.8d ago |
| 5 | 62 | Ridges | 71.6 | 0.85 | 1,208 | 2,974 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.5d ago |
| 6 | 91 | cascade | 70.0 | 0.85 | 742 | 2,992 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.5d ago |
| 7 | 56 | Gradients | 70.0 | 0.85 | 732 | 1,069 | rtx4090 | 0.727 | 5 | 73% | SCORING_COMMIT 4.5d ago |
| 8 | 15 | ORO | 69.4 | 1.0 | 17.56 | 21,435 | cpu-small | 0.000 | 60 | 95% | SCORING_COMMIT 0.5d ago |
| 9 | 1 | Apex | 68.6 | 0.85 | 482 | 1,135 | rtx4090 | 0.544 | 5 | 54% | RELEASE 0.8d ago |
| 10 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,635 | 4,635 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 11 | 26 | Perturb | 67.4 | 1.0 | 17.85 | 256 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.4d ago |
| 12 | 96 | Verathos | 67.1 | 1.0 | 16.49 | 419 | rtx4090 | 0.406 | 95 | 41% | RELEASE 3.8d ago |
| 13 | 38 | ChronoLLM | 66.6 | 0.85 | 115 | 1,575 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.6d ago |
| 14 | 107 | Minos | 65.6 | 1.0 | 159 | 43,984 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 15 | 85 | Vidaio | 64.2 | 0.85 | 132 | 405 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.2d ago |
| 16 | 108 | Prometheon | 63.9 | 0.85 | 119 | 128 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 0.9d ago |
| 17 | 81 | Reliquary | 63.6 | 0.85 | 108 | 235 | rtx4090 | 0.011 | 42 | 6% | SCORING_COMMIT 0.9d ago |
| 18 | 51 | lium.io | 62.0 | 0.85 | 76.05 | 5,370 | rtx4090 | 0.000 | 50 | 65% | SCORING_COMMIT 2.1d ago |
| 19 | 60 | Bitsec.ai | 59.7 | 0.85 | 456 | 456 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 20 | 53 | engy | 59.7 | 0.85 | 33.75 | 227 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.3d ago |
| 21 | 28 | gm | 58.4 | 0.85 | 24.55 | 1,661 | rtx4090 | 0.045 | 56 | 14% | RELEASE 1.9d ago |
| 22 | 61 | RedTeam | 58.0 | 0.85 | 19.79 | 279 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.1d ago |
| 23 | 68 | NOVA | 55.3 | 0.6 | 8,741 | 8,741 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 5.9d ago |
| 24 | 41 | Almanac | 55.1 | 1.0 | 10.97 | 23.82 | cpu-small | 0.735 | 78 | 74% | SCORING_COMMIT 10d ago |
| 25 | 120 | Affine | 54.8 | 0.6 | 7,272 | 7,272 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.6d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.18 | a4000 | 1190.5378573655278 |
| 89 | InfiniteQuant | -2.39 | rtx4090 | 111.84281297441723 |
| 13 | Data Universe | -3.08 | rtx4090 | 6.809459579629888 |
| 18 | Zeus | -3.54 | rtx4090 | 2104.0997282455455 |
| 123 | MANTIS | -5.57 | rtx4090 | 105.50112947159259 |
| 75 | Hippius | -6.26 | rtx4090 | 11519.540002271458 |
| 34 | BitMind | -18.66 | a100-80 | 323.79233814548115 |
| 101 | Tag101 | -0.06 | cpu-small | 2.4052749801631212 |
| 6 | Numinous | -0.93 | cpu-small | 337.1267206582048 |
| 50 | Synth | -0.94 | rtx4090 | 110.41357899846261 |
| 104 | Masx.ai | -1.59 | rtx4090 | 9.439732865642714 |
| 88 | Investing | -3.27 | rtx4090 | 679.1154481208074 |
| 8 | Vanta | -7.38 | rtx4090 | 1080.1240395137236 |
| 43 | Graphite | -0.46 | cpu-small | 184.5277289499323 |
| 32 | ItsAI | -0.09 | rtx4090 | 11.233154814891545 |
| 19 | blockmachine | -1.42 | rtx4090 | 539.7275875376587 |
| 45 | AlphaRidge.ai | -4.47 | rtx4090 | 11.546205043546633 |
| 22 | Desearch | -5.93 | rtx4090 | 67.47105038577541 |
| 63 | Enigma | -8.14 | rtx4090 | 5382.054132465889 |
| 105 | Beam | -2.10 | rtx4090 | 79.23292555865126 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.31 | 35.0 | 15.0 | 9.91 | 1.0 |
| 23 | 25.02 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.53 | 35.0 | 15.0 | 9.78 | 1.0 |
| 102 | 28.28 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 28.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.11 | 35.0 | 11.25 | 9.99 | 0.85 |
| 56 | 26.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.54 | 35.0 | 15.0 | 7.9 | 1.0 |
| 1 | 24.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.34 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.6 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.3 | 35.0 | 11.25 | 9.55 | 1.0 |
| 38 | 18.79 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 20.05 | 21.0 | 15.0 | 9.54 | 1.0 |
| 85 | 19.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.9 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 17.16 | 35.0 | 11.25 | 9.51 | 0.85 |
| 60 | 24.19 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 14.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 12.8 | 35.0 | 11.25 | 9.7 | 0.85 |
| 61 | 11.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.85 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.8 | 21.0 | 15.0 | 9.32 | 1.0 |
| 120 | 35.12 | 35.0 | 11.25 | 9.99 | 0.6 |
