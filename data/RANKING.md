# RANKING - generated 2026-08-23T20:00:29Z, block 8909871

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 76.31 | 85.43 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.1d ago |
| 2 | 67 | Harnyx | 72.9 | 1.0 | 25.89 | 829 | cpu-small | 0.026 | 125 | 20% | SCORING_COMMIT 2.4d ago |
| 3 | 102 | ConnitoAI | 72.8 | 0.85 | 1,705 | 2,734 | rtx4090 | 0.254 | 4 | 38% | RELEASE 0.0d ago |
| 4 | 23 | Trishool | 72.5 | 0.85 | 601 | 601 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.7d ago |
| 5 | 62 | Ridges | 71.9 | 0.85 | 1,300 | 3,200 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.9d ago |
| 6 | 15 | ORO | 71.5 | 1.0 | 27.05 | 46.24 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 1.9d ago |
| 7 | 56 | Gradients | 70.0 | 0.85 | 734 | 1,154 | rtx4090 | 0.731 | 5 | 73% | SCORING_COMMIT 5.8d ago |
| 8 | 91 | cascade | 69.0 | 0.85 | 552 | 1,486 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.9d ago |
| 9 | 1 | Apex | 69.0 | 0.85 | 542 | 1,223 | rtx4090 | 0.545 | 5 | 54% | RELEASE 2.2d ago |
| 10 | 96 | Verathos | 68.4 | 1.0 | 22.74 | 305 | rtx4090 | 0.402 | 90 | 40% | RELEASE 5.2d ago |
| 11 | 26 | Perturb | 67.8 | 1.0 | 19.49 | 278 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.8d ago |
| 12 | 124 | Swarm | 66.8 | 0.85 | 294 | 2,558 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.3d ago |
| 13 | 38 | ChronoLLM | 66.7 | 0.85 | 122 | 1,662 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.0d ago |
| 14 | 108 | Prometheon | 65.5 | 0.85 | 192 | 197 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.3d ago |
| 15 | 107 | Minos | 65.4 | 1.0 | 153 | 44,435 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 16 | 85 | Vidaio | 64.8 | 0.85 | 156 | 445 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.5d ago |
| 17 | 81 | Reliquary | 64.3 | 0.85 | 135 | 290 | rtx4090 | 0.004 | 37 | 6% | SCORING_COMMIT 1.1d ago |
| 18 | 60 | Bitsec.ai | 61.8 | 0.85 | 874 | 1,224 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 19 | 51 | lium.io | 60.7 | 0.85 | 55.52 | 2,053 | rtx4090 | 0.000 | 54 | 73% | SCORING_COMMIT 3.5d ago |
| 20 | 53 | engy | 60.3 | 0.85 | 39.98 | 13,244 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.7d ago |
| 21 | 28 | gm | 59.8 | 0.85 | 36.50 | 1,669 | rtx4090 | 0.141 | 52 | 14% | RELEASE 3.2d ago |
| 22 | 61 | RedTeam | 57.2 | 0.85 | 15.26 | 311 | rtx4090 | 0.000 | 85 | 6% | RELEASE 1.5d ago |
| 23 | 41 | Almanac | 56.5 | 1.0 | 15.38 | 30.08 | cpu-small | 0.643 | 79 | 64% | SCORING_COMMIT 11d ago |
| 24 | 120 | Affine | 54.9 | 0.6 | 7,677 | 7,677 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.0d ago |
| 25 | 33 | ReadyAI | 54.4 | 0.85 | 7.06 | 12.42 | rtx4090 | 0.000 | 245 | 1% | SCORING_COMMIT 3.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.27 | a4000 | 1248.6917791748576 |
| 13 | Data Universe | -2.51 | rtx4090 | 7.744156197360804 |
| 18 | Zeus | -3.14 | rtx4090 | 1922.2786977412657 |
| 89 | InfiniteQuant | -3.77 | rtx4090 | 119.23930806211295 |
| 123 | MANTIS | -5.60 | rtx4090 | 122.15529871693337 |
| 75 | Hippius | -6.07 | rtx4090 | 12647.11882648681 |
| 34 | BitMind | -18.90 | a100-80 | 350.16482150051525 |
| 6 | Numinous | -0.92 | cpu-small | 191.84568929141722 |
| 50 | Synth | -1.08 | rtx4090 | 67.45510461436228 |
| 104 | Masx.ai | -1.72 | rtx4090 | 11.530169598039302 |
| 88 | Investing | -2.63 | rtx4090 | 700.7135605604556 |
| 8 | Vanta | -7.31 | rtx4090 | 3589.2432620350933 |
| 43 | Graphite | -0.24 | cpu-small | 192.82245904019942 |
| 19 | blockmachine | -0.30 | rtx4090 | 690.389254874533 |
| 45 | AlphaRidge.ai | -4.82 | rtx4090 | 11.003526073732946 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08824802154508303 |
| 105 | Beam | -1.63 | rtx4090 | 86.48958237508124 |
| 84 | ansuz | -8.15 | rtx4090 | 0.0736321359725534 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.17 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 13.0 | 35.0 | 15.0 | 9.92 | 1.0 |
| 102 | 29.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.28 | 35.0 | 15.0 | 9.99 | 0.85 |
| 62 | 28.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 13.17 | 35.0 | 15.0 | 8.31 | 1.0 |
| 56 | 26.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.95 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.87 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.51 | 35.0 | 11.25 | 9.65 | 1.0 |
| 26 | 11.93 | 35.0 | 11.25 | 9.59 | 1.0 |
| 124 | 22.46 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 19.0 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.79 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.89 | 21.0 | 15.0 | 9.48 | 1.0 |
| 85 | 19.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 19.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.76 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 15.94 | 35.0 | 11.25 | 9.27 | 0.85 |
| 53 | 14.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.32 | 35.0 | 11.25 | 9.78 | 0.85 |
| 61 | 11.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 11.04 | 21.0 | 15.0 | 9.48 | 1.0 |
| 120 | 35.34 | 35.0 | 11.25 | 9.99 | 0.6 |
| 33 | 8.24 | 35.0 | 11.25 | 9.47 | 0.85 |
