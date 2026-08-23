# RANKING - generated 2026-08-23T14:02:41Z, block 8908082

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
| 1 | 76 | Phylax | 76.9 | 1.0 | 73.54 | 82.33 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 4.2d ago |
| 2 | 67 | Harnyx | 72.7 | 1.0 | 24.88 | 798 | cpu-small | 0.033 | 124 | 20% | SCORING_COMMIT 2.1d ago |
| 3 | 23 | Trishool | 72.3 | 0.85 | 570 | 570 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.4d ago |
| 4 | 15 | ORO | 71.2 | 1.0 | 23.69 | 41.81 | cpu-small | 0.000 | 78 | 93% | SCORING_COMMIT 1.6d ago |
| 5 | 56 | Gradients | 70.0 | 0.85 | 743 | 1,110 | rtx4090 | 0.730 | 5 | 73% | SCORING_COMMIT 5.6d ago |
| 6 | 91 | cascade | 68.9 | 0.85 | 539 | 1,452 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.6d ago |
| 7 | 1 | Apex | 68.6 | 0.85 | 492 | 1,205 | rtx4090 | 0.548 | 5 | 55% | RELEASE 2.0d ago |
| 8 | 96 | Verathos | 68.2 | 1.0 | 21.66 | 273 | rtx4090 | 0.402 | 91 | 40% | RELEASE 4.9d ago |
| 9 | 26 | Perturb | 67.6 | 1.0 | 18.67 | 266 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.5d ago |
| 10 | 124 | Swarm | 66.7 | 0.85 | 283 | 2,465 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.0d ago |
| 11 | 38 | ChronoLLM | 66.6 | 0.85 | 117 | 1,596 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.7d ago |
| 12 | 108 | Prometheon | 65.4 | 0.85 | 186 | 204 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.0d ago |
| 13 | 107 | Minos | 65.2 | 1.0 | 146 | 43,930 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 14 | 85 | Vidaio | 64.5 | 0.85 | 143 | 425 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.3d ago |
| 15 | 81 | Reliquary | 63.5 | 0.85 | 106 | 252 | rtx4090 | 0.072 | 38 | 7% | SCORING_COMMIT 0.8d ago |
| 16 | 51 | lium.io | 61.3 | 0.85 | 63.74 | 4,451 | rtx4090 | 0.000 | 53 | 71% | SCORING_COMMIT 3.2d ago |
| 17 | 102 | ConnitoAI | 61.1 | 0.85 | 51.96 | 2,913 | rtx4090 | 0.250 | 6 | 42% | RELEASE 1.9d ago |
| 18 | 53 | engy | 60.2 | 0.85 | 38.52 | 12,841 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.4d ago |
| 19 | 60 | Bitsec.ai | 60.0 | 0.85 | 505 | 505 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 20 | 28 | gm | 59.2 | 0.85 | 31.09 | 1,612 | rtx4090 | 0.215 | 55 | 22% | RELEASE 3.0d ago |
| 21 | 61 | RedTeam | 57.0 | 0.85 | 14.55 | 319 | rtx4090 | 0.000 | 84 | 7% | RELEASE 1.2d ago |
| 22 | 41 | Almanac | 56.5 | 1.0 | 15.30 | 29.53 | cpu-small | 0.633 | 79 | 63% | SCORING_COMMIT 11d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,366 | 7,366 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.7d ago |
| 24 | 80 | OpenRoboto | 53.9 | 0.85 | 213 | 766 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 15d ago |
| 25 | 33 | ReadyAI | 53.9 | 0.85 | 6.60 | 11.91 | rtx4090 | 0.000 | 246 | 1% | SCORING_COMMIT 2.8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.17 | a4000 | 1228.2255409076038 |
| 89 | InfiniteQuant | -0.43 | rtx4090 | 117.18611388148445 |
| 13 | Data Universe | -2.85 | rtx4090 | 7.513210472087128 |
| 18 | Zeus | -3.33 | rtx4090 | 1427.6160631091482 |
| 123 | MANTIS | -5.62 | rtx4090 | 115.82305804301862 |
| 75 | Hippius | -6.35 | rtx4090 | 12107.22053687642 |
| 34 | BitMind | -18.44 | a100-80 | 336.13124170205936 |
| 6 | Numinous | -0.93 | cpu-small | 182.22877904974683 |
| 50 | Synth | -1.43 | rtx4090 | 66.79020390775285 |
| 88 | Investing | -2.91 | rtx4090 | 665.9372257572077 |
| 104 | Masx.ai | -3.16 | rtx4090 | 12.395137420672816 |
| 8 | Vanta | -7.35 | rtx4090 | 1122.2812098667741 |
| 43 | Graphite | -0.27 | cpu-small | 185.75143333224466 |
| 19 | blockmachine | -0.80 | rtx4090 | 566.3042568983044 |
| 22 | Desearch | -0.89 | rtx4090 | 41.58293832386526 |
| 45 | AlphaRidge.ai | -4.39 | rtx4090 | 13.154305236782264 |
| 63 | Enigma | -8.13 | rtx4090 | 5592.8749130338265 |
| 105 | Beam | -2.05 | rtx4090 | 82.40378297378548 |
| 84 | ansuz | -8.15 | rtx4090 | 0.07060083483626738 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.03 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 12.85 | 35.0 | 15.0 | 9.85 | 1.0 |
| 23 | 25.07 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 12.66 | 35.0 | 15.0 | 8.56 | 1.0 |
| 56 | 26.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.85 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.33 | 35.0 | 11.25 | 9.64 | 1.0 |
| 26 | 11.77 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.32 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.84 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.67 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.71 | 21.0 | 15.0 | 9.48 | 1.0 |
| 85 | 19.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 18.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.47 | 35.0 | 11.25 | 9.37 | 0.85 |
| 102 | 15.68 | 35.0 | 11.25 | 9.93 | 0.85 |
| 53 | 14.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.6 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.7 | 35.0 | 11.25 | 9.69 | 0.85 |
| 61 | 10.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 11.03 | 21.0 | 15.0 | 9.49 | 1.0 |
| 120 | 35.17 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 21.19 | 21.0 | 11.25 | 10.0 | 0.85 |
| 33 | 8.01 | 35.0 | 11.25 | 9.15 | 0.85 |
