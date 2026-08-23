# RANKING - generated 2026-08-23T23:01:19Z, block 8910775

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 76.33 | 85.45 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.3d ago |
| 2 | 67 | Harnyx | 72.9 | 1.0 | 25.92 | 830 | cpu-small | 0.020 | 127 | 20% | SCORING_COMMIT 2.5d ago |
| 3 | 102 | ConnitoAI | 72.7 | 0.85 | 1,672 | 2,514 | rtx4090 | 0.254 | 4 | 35% | RELEASE 0.1d ago |
| 4 | 62 | Ridges | 72.5 | 0.85 | 1,547 | 3,162 | rtx4090 | 0.000 | 6 | 39% | RELEASE 5.0d ago |
| 5 | 23 | Trishool | 72.5 | 0.85 | 598 | 598 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.8d ago |
| 6 | 15 | ORO | 72.0 | 1.0 | 27.32 | 46.68 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 2.0d ago |
| 7 | 56 | Gradients | 70.0 | 0.85 | 734 | 1,155 | rtx4090 | 0.731 | 5 | 73% | SCORING_COMMIT 6.0d ago |
| 8 | 91 | cascade | 69.9 | 0.85 | 727 | 2,933 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 3.0d ago |
| 9 | 1 | Apex | 68.9 | 0.85 | 536 | 1,208 | rtx4090 | 0.551 | 5 | 55% | RELEASE 2.3d ago |
| 10 | 96 | Verathos | 68.7 | 1.0 | 24.31 | 303 | rtx4090 | 0.403 | 88 | 40% | RELEASE 5.3d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.53 | 278 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.9d ago |
| 12 | 124 | Swarm | 66.8 | 0.85 | 294 | 2,561 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.4d ago |
| 13 | 38 | ChronoLLM | 66.7 | 0.85 | 122 | 1,659 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.1d ago |
| 14 | 108 | Prometheon | 65.5 | 0.85 | 192 | 197 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.4d ago |
| 15 | 107 | Minos | 65.3 | 1.0 | 153 | 44,255 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 16 | 85 | Vidaio | 64.4 | 0.85 | 141 | 439 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.7d ago |
| 17 | 60 | Bitsec.ai | 64.1 | 0.85 | 1,711 | 1,711 | cpu-small | 0.515 | 2 | 52% | SCORING_COMMIT 16d ago |
| 18 | 81 | Reliquary | 63.5 | 0.85 | 106 | 270 | rtx4090 | 0.007 | 38 | 6% | SCORING_COMMIT 1.2d ago |
| 19 | 51 | lium.io | 60.7 | 0.85 | 55.32 | 2,063 | rtx4090 | 0.000 | 53 | 75% | SCORING_COMMIT 3.6d ago |
| 20 | 53 | engy | 60.2 | 0.85 | 39.60 | 334 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.8d ago |
| 21 | 28 | gm | 59.1 | 0.85 | 29.93 | 1,790 | rtx4090 | 0.135 | 54 | 15% | RELEASE 3.4d ago |
| 22 | 61 | RedTeam | 57.1 | 0.85 | 14.75 | 313 | rtx4090 | 0.000 | 83 | 6% | RELEASE 1.6d ago |
| 23 | 41 | Almanac | 56.4 | 1.0 | 14.93 | 29.34 | cpu-small | 0.653 | 79 | 65% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,677 | 7,677 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.1d ago |
| 25 | 33 | ReadyAI | 54.4 | 0.85 | 7.00 | 11.17 | rtx4090 | 0.000 | 243 | 1% | SCORING_COMMIT 3.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.24 | a4000 | 1219.8120597749603 |
| 13 | Data Universe | -2.51 | rtx4090 | 7.416173151055783 |
| 18 | Zeus | -3.69 | rtx4090 | 1713.3593715773468 |
| 89 | InfiniteQuant | -3.89 | rtx4090 | 119.02530935296403 |
| 123 | MANTIS | -5.54 | rtx4090 | 123.94032588828603 |
| 75 | Hippius | -5.95 | rtx4090 | 12758.401086206559 |
| 34 | BitMind | -17.42 | a100-80 | 350.5722368948573 |
| 6 | Numinous | -0.92 | cpu-small | 190.16129340898232 |
| 50 | Synth | -0.85 | rtx4090 | 67.88843864468657 |
| 104 | Masx.ai | -2.23 | rtx4090 | 12.540799030074744 |
| 88 | Investing | -2.61 | rtx4090 | 702.5627136933598 |
| 8 | Vanta | -7.31 | rtx4090 | 3403.660016981166 |
| 43 | Graphite | -0.48 | cpu-small | 200.98723180327286 |
| 19 | blockmachine | -0.20 | rtx4090 | 698.9666367909027 |
| 22 | Desearch | -1.47 | rtx4090 | 103.83232015318968 |
| 45 | AlphaRidge.ai | -4.31 | rtx4090 | 11.280695879025098 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08835089891843265 |
| 105 | Beam | -1.54 | rtx4090 | 87.33733815471875 |
| 84 | ansuz | -8.15 | rtx4090 | 535.2967023218913 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.17 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 13.01 | 35.0 | 15.0 | 9.93 | 1.0 |
| 102 | 29.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 29.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.26 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 13.21 | 35.0 | 15.0 | 8.83 | 1.0 |
| 56 | 26.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.03 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.76 | 35.0 | 11.25 | 9.67 | 1.0 |
| 26 | 11.94 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.47 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.99 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.79 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.9 | 21.0 | 15.0 | 9.35 | 1.0 |
| 85 | 19.57 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 29.41 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 18.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 15.92 | 35.0 | 11.25 | 9.27 | 0.85 |
| 53 | 14.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.55 | 35.0 | 11.25 | 9.73 | 0.85 |
| 61 | 10.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.93 | 21.0 | 15.0 | 9.46 | 1.0 |
| 120 | 35.34 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 8.22 | 35.0 | 11.25 | 9.52 | 0.85 |
