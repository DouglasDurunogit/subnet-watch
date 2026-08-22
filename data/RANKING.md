# RANKING - generated 2026-08-22T15:59:45Z, block 8901468

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
| 1 | 76 | Phylax | 77.2 | 1.0 | 78.02 | 131 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.3d ago |
| 2 | 67 | Harnyx | 72.3 | 1.0 | 22.51 | 439 | cpu-small | 0.054 | 150 | 12% | SCORING_COMMIT 1.2d ago |
| 3 | 102 | ConnitoAI | 71.9 | 0.85 | 1,290 | 2,442 | rtx4090 | 0.250 | 5 | 36% | RELEASE 1.0d ago |
| 4 | 62 | Ridges | 71.6 | 0.85 | 1,193 | 2,937 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.7d ago |
| 5 | 56 | Gradients | 69.9 | 0.85 | 719 | 1,056 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.7d ago |
| 6 | 91 | cascade | 69.8 | 0.85 | 689 | 2,782 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.7d ago |
| 7 | 15 | ORO | 69.8 | 1.0 | 17.95 | 21,459 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.7d ago |
| 8 | 1 | Apex | 68.4 | 0.85 | 456 | 1,100 | rtx4090 | 0.556 | 5 | 56% | RELEASE 1.0d ago |
| 9 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,533 | 4,533 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.57 | 252 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.6d ago |
| 11 | 96 | Verathos | 67.1 | 1.0 | 16.43 | 460 | rtx4090 | 0.406 | 93 | 41% | RELEASE 4.0d ago |
| 12 | 38 | ChronoLLM | 66.5 | 0.85 | 113 | 1,539 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.8d ago |
| 13 | 107 | Minos | 65.3 | 1.0 | 148 | 42,997 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 14 | 85 | Vidaio | 64.1 | 0.85 | 128 | 401 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.4d ago |
| 15 | 108 | Prometheon | 63.8 | 0.85 | 117 | 126 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.1d ago |
| 16 | 81 | Reliquary | 63.7 | 0.85 | 112 | 210 | rtx4090 | 0.003 | 39 | 5% | SCORING_COMMIT 0.0d ago |
| 17 | 51 | lium.io | 61.1 | 0.85 | 60.32 | 4,425 | rtx4090 | 0.000 | 53 | 68% | SCORING_COMMIT 2.3d ago |
| 18 | 60 | Bitsec.ai | 59.7 | 0.85 | 460 | 460 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 19 | 28 | gm | 59.7 | 0.85 | 35.34 | 1,614 | rtx4090 | 0.103 | 55 | 14% | RELEASE 2.1d ago |
| 20 | 53 | engy | 59.6 | 0.85 | 32.14 | 218 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.5d ago |
| 21 | 61 | RedTeam | 57.8 | 0.85 | 18.84 | 277 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.3d ago |
| 22 | 68 | NOVA | 55.2 | 0.6 | 8,623 | 8,623 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.1d ago |
| 23 | 41 | Almanac | 55.2 | 1.0 | 11.25 | 23.49 | cpu-small | 0.728 | 78 | 73% | SCORING_COMMIT 10d ago |
| 24 | 120 | Affine | 54.7 | 0.6 | 7,053 | 7,053 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.8d ago |
| 25 | 124 | Swarm | 54.6 | 0.85 | 267 | 2,326 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.01 | cpu-small | 856.2684356040396 |
| 54 | Yanez | -3.48 | a4000 | 1160.4526660316124 |
| 13 | Data Universe | -2.96 | rtx4090 | 6.417676119492818 |
| 89 | InfiniteQuant | -2.99 | rtx4090 | 118.0068770244507 |
| 18 | Zeus | -4.41 | rtx4090 | 1701.5358811214262 |
| 123 | MANTIS | -5.61 | rtx4090 | 107.67319284996468 |
| 75 | Hippius | -6.30 | rtx4090 | 11313.986626373604 |
| 34 | BitMind | -19.90 | a100-80 | 319.3992751046927 |
| 101 | Tag101 | -0.03 | cpu-small | 2.2875036981959567 |
| 6 | Numinous | -0.94 | cpu-small | 285.14876653958464 |
| 104 | Masx.ai | -1.42 | rtx4090 | 7.927721865890464 |
| 50 | Synth | -1.49 | rtx4090 | 81.25531324119818 |
| 88 | Investing | -3.24 | rtx4090 | 683.1448504140368 |
| 8 | Vanta | -7.39 | rtx4090 | 1066.080733821188 |
| 43 | Graphite | -0.46 | cpu-small | 188.93740658421277 |
| 19 | blockmachine | -1.51 | rtx4090 | 532.8358530197041 |
| 22 | Desearch | -4.74 | rtx4090 | 94.44298281084522 |
| 45 | AlphaRidge.ai | -5.14 | rtx4090 | 15.135318261237021 |
| 63 | Enigma | -8.14 | rtx4090 | 5350.966418752625 |
| 105 | Beam | -2.41 | rtx4090 | 81.29910856081973 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.26 | 35.0 | 15.0 | 9.91 | 1.0 |
| 67 | 12.47 | 35.0 | 15.0 | 9.8 | 1.0 |
| 102 | 28.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 27.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 25.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.82 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 11.62 | 35.0 | 15.0 | 8.16 | 1.0 |
| 1 | 24.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.26 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.54 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.29 | 35.0 | 11.25 | 9.55 | 1.0 |
| 38 | 18.7 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.77 | 21.0 | 15.0 | 9.51 | 1.0 |
| 85 | 19.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.85 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.66 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.26 | 35.0 | 11.25 | 9.39 | 0.85 |
| 60 | 24.23 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 14.19 | 35.0 | 11.25 | 9.79 | 0.85 |
| 53 | 13.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.8 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.9 | 21.0 | 15.0 | 9.35 | 1.0 |
| 120 | 35.0 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.08 | 21.0 | 11.25 | 9.86 | 0.85 |
