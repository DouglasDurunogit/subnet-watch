# RANKING - generated 2026-08-22T16:36:45Z, block 8901653

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
| 1 | 76 | Phylax | 77.2 | 1.0 | 79.11 | 133 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.3d ago |
| 2 | 67 | Harnyx | 72.3 | 1.0 | 22.83 | 445 | cpu-small | 0.054 | 150 | 12% | SCORING_COMMIT 1.2d ago |
| 3 | 102 | ConnitoAI | 71.9 | 0.85 | 1,308 | 2,476 | rtx4090 | 0.250 | 5 | 36% | RELEASE 1.0d ago |
| 4 | 62 | Ridges | 71.6 | 0.85 | 1,209 | 2,978 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.7d ago |
| 5 | 56 | Gradients | 69.9 | 0.85 | 729 | 1,071 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.7d ago |
| 6 | 91 | cascade | 69.8 | 0.85 | 693 | 2,797 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.7d ago |
| 7 | 15 | ORO | 69.6 | 1.0 | 18.22 | 21,766 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.7d ago |
| 8 | 1 | Apex | 68.7 | 0.85 | 501 | 1,246 | rtx4090 | 0.516 | 5 | 52% | RELEASE 1.1d ago |
| 9 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,596 | 4,596 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.85 | 256 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.6d ago |
| 11 | 96 | Verathos | 67.2 | 1.0 | 16.77 | 466 | rtx4090 | 0.406 | 93 | 41% | RELEASE 4.0d ago |
| 12 | 38 | ChronoLLM | 66.5 | 0.85 | 114 | 1,560 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.8d ago |
| 13 | 107 | Minos | 65.3 | 1.0 | 150 | 43,609 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 14 | 85 | Vidaio | 64.2 | 0.85 | 130 | 406 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.4d ago |
| 15 | 108 | Prometheon | 63.9 | 0.85 | 119 | 128 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.1d ago |
| 16 | 81 | Reliquary | 63.7 | 0.85 | 113 | 213 | rtx4090 | 0.003 | 39 | 5% | SCORING_COMMIT 0.0d ago |
| 17 | 51 | lium.io | 61.2 | 0.85 | 61.28 | 4,486 | rtx4090 | 0.000 | 53 | 68% | SCORING_COMMIT 2.4d ago |
| 18 | 28 | gm | 59.8 | 0.85 | 36.00 | 1,639 | rtx4090 | 0.103 | 55 | 14% | RELEASE 2.1d ago |
| 19 | 60 | Bitsec.ai | 59.7 | 0.85 | 460 | 460 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 20 | 53 | engy | 59.6 | 0.85 | 32.40 | 219 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.5d ago |
| 21 | 61 | RedTeam | 57.9 | 0.85 | 19.13 | 280 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.4d ago |
| 22 | 68 | NOVA | 55.3 | 0.6 | 8,743 | 8,743 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.1d ago |
| 23 | 41 | Almanac | 55.3 | 1.0 | 11.42 | 23.83 | cpu-small | 0.728 | 78 | 73% | SCORING_COMMIT 10d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,145 | 7,145 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.8d ago |
| 25 | 124 | Swarm | 54.6 | 0.85 | 271 | 2,359 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.45 | a4000 | 1180.2663284266143 |
| 13 | Data Universe | -2.83 | rtx4090 | 6.500837687055448 |
| 89 | InfiniteQuant | -2.92 | rtx4090 | 119.62677932715124 |
| 18 | Zeus | -4.36 | rtx4090 | 1725.692088876865 |
| 123 | MANTIS | -5.57 | rtx4090 | 109.16153745994606 |
| 75 | Hippius | -6.28 | rtx4090 | 11431.89539694868 |
| 34 | BitMind | -19.76 | a100-80 | 323.92196187378255 |
| 101 | Tag101 | -0.01 | cpu-small | 2.318680790326412 |
| 6 | Numinous | -0.94 | cpu-small | 289.09031985001167 |
| 104 | Masx.ai | -1.32 | rtx4090 | 8.037229545952908 |
| 50 | Synth | -1.38 | rtx4090 | 82.6722299099217 |
| 88 | Investing | -3.26 | rtx4090 | 681.3532595682407 |
| 8 | Vanta | -7.38 | rtx4090 | 1080.7425440008083 |
| 43 | Graphite | -0.46 | cpu-small | 191.54904986579828 |
| 19 | blockmachine | -1.42 | rtx4090 | 540.2234575326842 |
| 22 | Desearch | -4.69 | rtx4090 | 95.74570111054014 |
| 45 | AlphaRidge.ai | -5.07 | rtx4090 | 15.34451794926569 |
| 63 | Enigma | -8.14 | rtx4090 | 5425.145660178527 |
| 105 | Beam | -2.32 | rtx4090 | 82.587292121213 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06966896916835782 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.31 | 35.0 | 15.0 | 9.91 | 1.0 |
| 67 | 12.53 | 35.0 | 15.0 | 9.78 | 1.0 |
| 102 | 28.35 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 28.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 26.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.84 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 11.68 | 35.0 | 15.0 | 7.95 | 1.0 |
| 1 | 24.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.31 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.6 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.37 | 35.0 | 11.25 | 9.56 | 1.0 |
| 38 | 18.75 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.83 | 21.0 | 15.0 | 9.51 | 1.0 |
| 85 | 19.25 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.9 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.72 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.32 | 35.0 | 11.25 | 9.39 | 0.85 |
| 28 | 14.26 | 35.0 | 11.25 | 9.79 | 0.85 |
| 60 | 24.23 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.85 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.95 | 21.0 | 15.0 | 9.35 | 1.0 |
| 120 | 35.05 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.14 | 21.0 | 11.25 | 9.86 | 0.85 |
