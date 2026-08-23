# RANKING - generated 2026-08-23T23:32:23Z, block 8910931

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 76.19 | 85.30 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.3d ago |
| 2 | 67 | Harnyx | 72.8 | 1.0 | 25.87 | 828 | cpu-small | 0.020 | 127 | 20% | SCORING_COMMIT 2.5d ago |
| 3 | 102 | ConnitoAI | 72.7 | 0.85 | 1,643 | 2,471 | rtx4090 | 0.254 | 4 | 35% | RELEASE 0.2d ago |
| 4 | 62 | Ridges | 72.5 | 0.85 | 1,545 | 3,157 | rtx4090 | 0.000 | 6 | 39% | RELEASE 5.0d ago |
| 5 | 23 | Trishool | 72.5 | 0.85 | 597 | 597 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.8d ago |
| 6 | 15 | ORO | 71.9 | 1.0 | 27.50 | 46.99 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 2.0d ago |
| 7 | 56 | Gradients | 70.0 | 0.85 | 732 | 1,153 | rtx4090 | 0.731 | 5 | 73% | SCORING_COMMIT 6.0d ago |
| 8 | 91 | cascade | 69.9 | 0.85 | 726 | 2,928 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 3.0d ago |
| 9 | 1 | Apex | 68.9 | 0.85 | 533 | 1,201 | rtx4090 | 0.552 | 5 | 55% | RELEASE 2.4d ago |
| 10 | 96 | Verathos | 68.5 | 1.0 | 23.44 | 294 | rtx4090 | 0.403 | 88 | 40% | RELEASE 5.3d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.49 | 278 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.9d ago |
| 12 | 124 | Swarm | 66.8 | 0.85 | 294 | 2,558 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.4d ago |
| 13 | 38 | ChronoLLM | 66.7 | 0.85 | 121 | 1,657 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.1d ago |
| 14 | 108 | Prometheon | 65.5 | 0.85 | 192 | 197 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.4d ago |
| 15 | 107 | Minos | 65.4 | 1.0 | 153 | 44,311 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 16 | 85 | Vidaio | 64.4 | 0.85 | 141 | 438 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.7d ago |
| 17 | 60 | Bitsec.ai | 64.1 | 0.85 | 1,708 | 1,708 | cpu-small | 0.515 | 2 | 52% | SCORING_COMMIT 16d ago |
| 18 | 81 | Reliquary | 63.5 | 0.85 | 105 | 270 | rtx4090 | 0.007 | 38 | 6% | SCORING_COMMIT 1.2d ago |
| 19 | 51 | lium.io | 61.6 | 0.85 | 68.49 | 2,088 | rtx4090 | 0.000 | 53 | 74% | SCORING_COMMIT 3.6d ago |
| 20 | 53 | engy | 60.3 | 0.85 | 39.94 | 336 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.8d ago |
| 21 | 28 | gm | 59.5 | 0.85 | 33.21 | 1,870 | rtx4090 | 0.166 | 57 | 17% | RELEASE 3.4d ago |
| 22 | 61 | RedTeam | 57.1 | 0.85 | 14.71 | 313 | rtx4090 | 0.000 | 83 | 6% | RELEASE 1.6d ago |
| 23 | 41 | Almanac | 56.4 | 1.0 | 14.79 | 29.12 | cpu-small | 0.655 | 79 | 66% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,662 | 7,662 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.1d ago |
| 25 | 33 | ReadyAI | 54.2 | 0.85 | 7.04 | 11.81 | rtx4090 | 0.000 | 243 | 1% | SCORING_COMMIT 3.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.24 | cpu-small | 6.218386295369297 |
| 54 | Yanez | -3.24 | a4000 | 1217.017638104461 |
| 13 | Data Universe | -2.58 | rtx4090 | 7.603971351592279 |
| 18 | Zeus | -3.69 | rtx4090 | 1710.203022918608 |
| 89 | InfiniteQuant | -3.90 | rtx4090 | 118.8038440264855 |
| 123 | MANTIS | -5.55 | rtx4090 | 123.70971539976121 |
| 75 | Hippius | -5.95 | rtx4090 | 12777.369090770882 |
| 34 | BitMind | -17.91 | a100-80 | 349.9345370385124 |
| 6 | Numinous | -0.92 | cpu-small | 189.80852766733372 |
| 50 | Synth | -0.72 | rtx4090 | 68.24268846183476 |
| 104 | Masx.ai | -2.24 | rtx4090 | 12.517464899152547 |
| 88 | Investing | -2.61 | rtx4090 | 702.162321578962 |
| 8 | Vanta | -7.31 | rtx4090 | 3396.1025626035216 |
| 43 | Graphite | -0.48 | cpu-small | 200.61326346555194 |
| 19 | blockmachine | -0.19 | rtx4090 | 699.8156619728586 |
| 22 | Desearch | -1.06 | rtx4090 | 69.58677294200047 |
| 45 | AlphaRidge.ai | -4.58 | rtx4090 | 17.754265676183188 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08818968332152692 |
| 105 | Beam | -1.42 | rtx4090 | 88.926004266389 |
| 84 | ansuz | -8.15 | rtx4090 | 534.3006985342342 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.17 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 13.0 | 35.0 | 15.0 | 9.84 | 1.0 |
| 102 | 29.25 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 29.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.25 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 13.23 | 35.0 | 15.0 | 8.63 | 1.0 |
| 56 | 26.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.03 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.81 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.63 | 35.0 | 11.25 | 9.66 | 1.0 |
| 26 | 11.93 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.47 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.99 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.79 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.91 | 21.0 | 15.0 | 9.48 | 1.0 |
| 85 | 19.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 29.4 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 18.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.75 | 35.0 | 11.25 | 9.41 | 0.85 |
| 53 | 14.66 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.95 | 35.0 | 11.25 | 9.76 | 0.85 |
| 61 | 10.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.9 | 21.0 | 15.0 | 9.46 | 1.0 |
| 120 | 35.33 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 8.23 | 35.0 | 11.25 | 9.3 | 0.85 |
