# RANKING - generated 2026-08-16T08:02:20Z, block 8855881

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
| 1 | 107 | Minos | 77.9 | 1.0 | 107 | 31,754 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.7d ago |
| 2 | 76 | Phylax | 73.9 | 1.0 | 32.61 | 157 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.0d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.65 | 417 | cpu-small | 0.077 | 127 | 11% | SCORING_COMMIT 0.1d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.52 | 74.34 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.7d ago |
| 5 | 1 | Apex | 70.2 | 0.85 | 792 | 1,089 | rtx4090 | 0.535 | 4 | 54% | RELEASE 2.7d ago |
| 6 | 41 | Almanac | 69.9 | 1.0 | 12.85 | 53.65 | cpu-small | 0.651 | 74 | 65% | SCORING_COMMIT 3.4d ago |
| 7 | 96 | Verathos | 69.8 | 1.0 | 31.49 | 269 | rtx4090 | 0.409 | 57 | 41% | RELEASE 1.5d ago |
| 8 | 15 | ORO | 68.9 | 1.0 | 12.55 | 12,626 | cpu-small | 0.000 | 60 | 95% | SCORING_COMMIT 2.4d ago |
| 9 | 56 | Gradients | 68.7 | 0.85 | 505 | 957 | rtx4090 | 0.674 | 7 | 67% | SCORING_COMMIT 3.7d ago |
| 10 | 62 | Ridges | 68.5 | 0.85 | 473 | 2,193 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.4d ago |
| 11 | 91 | cascade | 68.3 | 0.85 | 442 | 2,273 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.4d ago |
| 12 | 21 | AdTAO | 67.6 | 1.0 | 7.59 | 34.07 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.8d ago |
| 13 | 85 | Vidaio | 67.4 | 0.85 | 345 | 591 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 3.9d ago |
| 14 | 38 | ChronoLLM | 65.9 | 0.85 | 96.39 | 1,318 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.6d ago |
| 15 | 124 | Swarm | 65.8 | 0.85 | 222 | 714 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.7d ago |
| 16 | 2 | DSperse | 63.0 | 0.85 | 90.38 | 144 | rtx4090 | 0.822 | 5 | 82% | RELEASE 5.5d ago |
| 17 | 55 | NIOME | 61.5 | 0.85 | 57.36 | 473 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.5d ago |
| 18 | 102 | ConnitoAI | 60.1 | 0.85 | 1,332 | 1,332 | rtx4090 | 0.250 | 4 | 25% | RELEASE 15d ago |
| 19 | 60 | Bitsec.ai | 59.4 | 0.85 | 419 | 419 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 20 | 28 | gm | 58.8 | 0.85 | 26.83 | 2,186 | rtx4090 | 0.231 | 40 | 25% | RELEASE 3.7d ago |
| 21 | 74 | Gittensor | 57.7 | 0.85 | 24.73 | 210 | rtx4090 | 0.638 | 14 | 64% | RELEASE 4.6d ago |
| 22 | 61 | RedTeam | 57.6 | 0.85 | 17.23 | 438 | rtx4090 | 0.000 | 81 | 10% | RELEASE 5.0d ago |
| 23 | 51 | lium.io | 57.1 | 0.85 | 22.24 | 1,364 | rtx4090 | 0.000 | 52 | 82% | SCORING_COMMIT 1.9d ago |
| 24 | 120 | Affine | 56.8 | 0.6 | 16,499 | 16,499 | rtx4090 | 0.500 | 2 | 50% | SCORING_COMMIT 3.7d ago |
| 25 | 80 | OpenRoboto | 53.0 | 0.85 | 164 | 594 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 243.29309735126424 |
| 54 | Yanez | -3.55 | a4000 | 945.7606629691667 |
| 89 | InfiniteQuant | -4.29 | rtx4090 | 185.7124557260052 |
| 75 | Hippius | -7.39 | rtx4090 | 10775.80514533739 |
| 101 | Tag101 | -0.04 | cpu-small | 1.8973650946269185 |
| 13 | Data Universe | -3.65 | rtx4090 | 5.667405931618924 |
| 88 | Investing | -5.35 | rtx4090 | 1158.998001889847 |
| 8 | Vanta | -7.71 | rtx4090 | 2894.762616620986 |
| 114 | SOMA | -8.13 | rtx4090 | 600.937332045377 |
| 43 | Graphite | -0.75 | cpu-small | 16.66794248762923 |
| 32 | ItsAI | -0.44 | rtx4090 | 10.924045855846321 |
| 22 | Desearch | -3.08 | rtx4090 | 55.81618068571846 |
| 45 | AlphaRidge.ai | -3.98 | rtx4090 | 23.61051463901498 |
| 18 | Zeus | -5.12 | rtx4090 | 721.8991049626566 |
| 123 | MANTIS | -6.04 | rtx4090 | 75.74180281557949 |
| 19 | blockmachine | -6.14 | rtx4090 | 1078.2337722452103 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0765016988237125 |
| 105 | Beam | -3.29 | rtx4090 | 99.42793949167346 |
| 84 | ansuz | -8.16 | rtx4090 | 438.7067871598769 |
| 34 | BitMind | -20.07 | a100-80 | 18.611340000295588 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.48 | 35.0 | 15.0 | 9.39 | 1.0 |
| 76 | 13.88 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.66 | 35.0 | 15.0 | 9.84 | 1.0 |
| 26 | 14.72 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.38 | 35.0 | 15.0 | 9.49 | 1.0 |
| 96 | 13.75 | 35.0 | 11.25 | 9.79 | 1.0 |
| 15 | 10.3 | 35.0 | 15.0 | 8.59 | 1.0 |
| 56 | 24.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.34 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 21 | 8.5 | 35.0 | 15.0 | 9.14 | 1.0 |
| 85 | 23.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.09 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.37 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 17.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 28.42 | 21.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.86 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.14 | 35.0 | 11.25 | 9.76 | 0.85 |
| 74 | 12.83 | 35.0 | 11.25 | 8.82 | 0.85 |
| 61 | 11.47 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.43 | 35.0 | 11.25 | 8.53 | 0.85 |
| 120 | 38.36 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.16 | 21.0 | 11.25 | 10.0 | 0.85 |
