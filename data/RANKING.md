# RANKING - generated 2026-08-22T14:34:31Z, block 8901041

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
| 1 | 76 | Phylax | 77.2 | 1.0 | 78.64 | 132 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.2d ago |
| 2 | 102 | ConnitoAI | 72.9 | 0.85 | 1,736 | 1,736 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.9d ago |
| 3 | 23 | Trishool | 72.2 | 0.85 | 559 | 559 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 2.4d ago |
| 4 | 67 | Harnyx | 72.2 | 1.0 | 22.74 | 443 | cpu-small | 0.058 | 148 | 12% | SCORING_COMMIT 1.2d ago |
| 5 | 62 | Ridges | 71.6 | 0.85 | 1,202 | 2,960 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.6d ago |
| 6 | 56 | Gradients | 69.9 | 0.85 | 726 | 1,064 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.6d ago |
| 7 | 91 | cascade | 69.7 | 0.85 | 689 | 2,779 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.6d ago |
| 8 | 15 | ORO | 69.6 | 1.0 | 18.31 | 21,858 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.6d ago |
| 9 | 1 | Apex | 68.5 | 0.85 | 471 | 1,108 | rtx4090 | 0.552 | 5 | 55% | RELEASE 1.0d ago |
| 10 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,596 | 4,596 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 11 | 26 | Perturb | 67.4 | 1.0 | 17.72 | 254 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.5d ago |
| 12 | 96 | Verathos | 66.8 | 1.0 | 15.30 | 466 | rtx4090 | 0.405 | 92 | 41% | RELEASE 3.9d ago |
| 13 | 38 | ChronoLLM | 66.5 | 0.85 | 113 | 1,541 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.7d ago |
| 14 | 107 | Minos | 64.8 | 1.0 | 133 | 43,798 | cpu-small | 0.000 | 19 | 91% | README_TASK_DIFF 12d ago |
| 15 | 85 | Vidaio | 64.2 | 0.85 | 129 | 401 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.3d ago |
| 16 | 108 | Prometheon | 63.8 | 0.85 | 118 | 128 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.0d ago |
| 17 | 81 | Reliquary | 63.8 | 0.85 | 117 | 213 | rtx4090 | 0.004 | 39 | 5% | SCORING_COMMIT 1.1d ago |
| 18 | 60 | Bitsec.ai | 59.7 | 0.85 | 463 | 463 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 19 | 53 | engy | 59.6 | 0.85 | 32.67 | 221 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.4d ago |
| 20 | 51 | lium.io | 59.5 | 0.85 | 40.31 | 4,484 | rtx4090 | 0.000 | 55 | 66% | SCORING_COMMIT 2.3d ago |
| 21 | 28 | gm | 58.4 | 0.85 | 24.08 | 1,951 | rtx4090 | 0.090 | 56 | 17% | RELEASE 2.0d ago |
| 22 | 61 | RedTeam | 57.9 | 0.85 | 18.98 | 275 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.3d ago |
| 23 | 68 | NOVA | 55.2 | 0.6 | 8,686 | 8,686 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.0d ago |
| 24 | 41 | Almanac | 55.2 | 1.0 | 11.24 | 23.67 | cpu-small | 0.729 | 78 | 73% | SCORING_COMMIT 10d ago |
| 25 | 120 | Affine | 54.8 | 0.6 | 7,195 | 7,195 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.00 | cpu-small | 863.180510616626 |
| 54 | Yanez | -3.41 | a4000 | 1157.074067803119 |
| 89 | InfiniteQuant | -2.26 | rtx4090 | 118.56916160709555 |
| 13 | Data Universe | -3.05 | rtx4090 | 6.578571425191792 |
| 18 | Zeus | -3.57 | rtx4090 | 2089.1451125257713 |
| 123 | MANTIS | -5.59 | rtx4090 | 107.90223900285528 |
| 75 | Hippius | -6.28 | rtx4090 | 11403.498321645637 |
| 34 | BitMind | -19.16 | a100-80 | 321.78661329738554 |
| 101 | Tag101 | -0.02 | cpu-small | 2.350883063604192 |
| 6 | Numinous | -0.93 | cpu-small | 338.1113276670513 |
| 50 | Synth | -1.10 | rtx4090 | 102.2441425220542 |
| 104 | Masx.ai | -1.28 | rtx4090 | 12.657754445922015 |
| 88 | Investing | -3.32 | rtx4090 | 672.4421816726917 |
| 8 | Vanta | -7.38 | rtx4090 | 1063.0699919736217 |
| 43 | Graphite | -0.46 | cpu-small | 190.4731686583373 |
| 19 | blockmachine | -1.46 | rtx4090 | 536.796308955122 |
| 45 | AlphaRidge.ai | -4.56 | rtx4090 | 13.407826208489888 |
| 22 | Desearch | -5.23 | rtx4090 | 101.32905936904119 |
| 63 | Enigma | -8.14 | rtx4090 | 5393.088643049596 |
| 105 | Beam | -2.60 | rtx4090 | 81.79613240646098 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.29 | 35.0 | 15.0 | 9.91 | 1.0 |
| 102 | 29.47 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.0 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.51 | 35.0 | 15.0 | 9.71 | 1.0 |
| 62 | 28.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 26.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.82 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 11.69 | 35.0 | 15.0 | 7.93 | 1.0 |
| 1 | 24.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.31 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.57 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.03 | 35.0 | 11.25 | 9.52 | 1.0 |
| 38 | 18.7 | 35.0 | 15.0 | 9.51 | 0.85 |
| 107 | 19.35 | 21.0 | 15.0 | 9.45 | 1.0 |
| 85 | 19.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.88 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.26 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.7 | 35.0 | 11.25 | 9.08 | 0.85 |
| 28 | 12.73 | 35.0 | 11.25 | 9.69 | 0.85 |
| 61 | 11.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.82 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.89 | 21.0 | 15.0 | 9.34 | 1.0 |
| 120 | 35.08 | 35.0 | 11.25 | 9.99 | 0.6 |
