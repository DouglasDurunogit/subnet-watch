# RANKING - generated 2026-08-23T18:44:52Z, block 8909493

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 75.46 | 84.47 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.1d ago |
| 2 | 67 | Harnyx | 72.8 | 1.0 | 25.49 | 817 | cpu-small | 0.026 | 125 | 20% | SCORING_COMMIT 2.3d ago |
| 3 | 23 | Trishool | 72.4 | 0.85 | 592 | 592 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.6d ago |
| 4 | 102 | ConnitoAI | 72.1 | 0.85 | 1,381 | 2,578 | rtx4090 | 0.252 | 5 | 36% | RELEASE 2.1d ago |
| 5 | 62 | Ridges | 71.8 | 0.85 | 1,284 | 3,161 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.8d ago |
| 6 | 15 | ORO | 71.8 | 1.0 | 27.09 | 46.30 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 1.8d ago |
| 7 | 56 | Gradients | 69.9 | 0.85 | 725 | 1,139 | rtx4090 | 0.730 | 5 | 73% | SCORING_COMMIT 5.8d ago |
| 8 | 91 | cascade | 69.0 | 0.85 | 558 | 1,503 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.8d ago |
| 9 | 1 | Apex | 68.9 | 0.85 | 536 | 1,210 | rtx4090 | 0.542 | 5 | 54% | RELEASE 2.2d ago |
| 10 | 96 | Verathos | 68.5 | 1.0 | 23.50 | 307 | rtx4090 | 0.403 | 88 | 40% | RELEASE 5.1d ago |
| 11 | 26 | Perturb | 67.7 | 1.0 | 19.19 | 274 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.7d ago |
| 12 | 124 | Swarm | 66.8 | 0.85 | 293 | 2,549 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.2d ago |
| 13 | 38 | ChronoLLM | 66.7 | 0.85 | 120 | 1,637 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.9d ago |
| 14 | 108 | Prometheon | 65.5 | 0.85 | 192 | 210 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.2d ago |
| 15 | 107 | Minos | 65.4 | 1.0 | 153 | 43,389 | cpu-small | 0.000 | 20 | 89% | README_TASK_DIFF 13d ago |
| 16 | 81 | Reliquary | 64.9 | 0.85 | 162 | 272 | rtx4090 | 0.006 | 36 | 6% | SCORING_COMMIT 1.0d ago |
| 17 | 85 | Vidaio | 64.7 | 0.85 | 152 | 436 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.5d ago |
| 18 | 51 | lium.io | 61.5 | 0.85 | 68.05 | 2,105 | rtx4090 | 0.000 | 53 | 71% | SCORING_COMMIT 3.4d ago |
| 19 | 53 | engy | 60.2 | 0.85 | 38.76 | 12,908 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.6d ago |
| 20 | 60 | Bitsec.ai | 60.1 | 0.85 | 520 | 520 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 21 | 28 | gm | 59.3 | 0.85 | 31.59 | 1,638 | rtx4090 | 0.238 | 55 | 24% | RELEASE 3.2d ago |
| 22 | 61 | RedTeam | 57.1 | 0.85 | 14.78 | 302 | rtx4090 | 0.000 | 85 | 6% | RELEASE 1.4d ago |
| 23 | 41 | Almanac | 56.5 | 1.0 | 15.25 | 29.79 | cpu-small | 0.641 | 79 | 64% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,563 | 7,563 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.9d ago |
| 25 | 33 | ReadyAI | 54.2 | 0.85 | 6.84 | 11.78 | rtx4090 | 0.000 | 244 | 1% | SCORING_COMMIT 3.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.15 | a4000 | 1239.6712512292659 |
| 89 | InfiniteQuant | -1.10 | rtx4090 | 117.71493078737619 |
| 13 | Data Universe | -2.59 | rtx4090 | 7.695693159820134 |
| 18 | Zeus | -3.21 | rtx4090 | 1894.1388013481937 |
| 123 | MANTIS | -5.59 | rtx4090 | 122.64430993422958 |
| 75 | Hippius | -6.29 | rtx4090 | 12461.679704384458 |
| 34 | BitMind | -18.73 | a100-80 | 345.00530115489374 |
| 6 | Numinous | -0.93 | cpu-small | 186.74951972558114 |
| 50 | Synth | -1.24 | rtx4090 | 66.95352350078466 |
| 104 | Masx.ai | -2.23 | rtx4090 | 10.473361196699189 |
| 88 | Investing | -2.70 | rtx4090 | 690.926212771484 |
| 8 | Vanta | -7.33 | rtx4090 | 3360.712947608846 |
| 43 | Graphite | -0.25 | cpu-small | 197.96861346954242 |
| 22 | Desearch | -0.21 | rtx4090 | 68.39680032295622 |
| 19 | blockmachine | -0.61 | rtx4090 | 581.1794305450115 |
| 45 | AlphaRidge.ai | -3.80 | rtx4090 | 14.104040903817989 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08706148992388393 |
| 105 | Beam | -1.71 | rtx4090 | 86.04383106125172 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07255559920698305 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.13 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 12.94 | 35.0 | 15.0 | 9.9 | 1.0 |
| 23 | 25.22 | 35.0 | 15.0 | 9.99 | 0.85 |
| 102 | 28.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 28.28 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 13.17 | 35.0 | 15.0 | 8.64 | 1.0 |
| 56 | 26.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.99 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.63 | 35.0 | 11.25 | 9.66 | 1.0 |
| 26 | 11.87 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.45 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.94 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.78 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.9 | 21.0 | 15.0 | 9.49 | 1.0 |
| 81 | 20.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.73 | 35.0 | 11.25 | 9.42 | 0.85 |
| 53 | 14.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.71 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.76 | 35.0 | 11.25 | 9.75 | 0.85 |
| 61 | 10.9 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 11.01 | 21.0 | 15.0 | 9.48 | 1.0 |
| 120 | 35.28 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 8.13 | 35.0 | 11.25 | 9.44 | 0.85 |
