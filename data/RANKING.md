# RANKING - generated 2026-08-18T17:38:29Z, block 8873162

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
| 1 | 76 | Phylax | 78.2 | 1.0 | 98.31 | 190 | cpu-small | 0.000 | 10 | 20% | SCORING_COMMIT 2.2d ago |
| 2 | 21 | AdTAO | 76.6 | 1.0 | 66.82 | 271 | cpu-small | 0.300 | 16 | 30% | SCORING_COMMIT 0.0d ago |
| 3 | 67 | Harnyx | 71.9 | 1.0 | 19.92 | 425 | cpu-small | 0.062 | 131 | 13% | SCORING_COMMIT 0.3d ago |
| 4 | 26 | Perturb | 70.7 | 1.0 | 39.32 | 72.20 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 5.1d ago |
| 5 | 1 | Apex | 70.3 | 0.85 | 817 | 1,103 | rtx4090 | 0.525 | 4 | 53% | RELEASE 0.1d ago |
| 6 | 56 | Gradients | 69.5 | 0.85 | 633 | 934 | rtx4090 | 0.716 | 5 | 72% | SCORING_COMMIT 0.7d ago |
| 7 | 41 | Almanac | 69.1 | 1.0 | 10.55 | 35.99 | cpu-small | 0.668 | 75 | 67% | SCORING_COMMIT 5.8d ago |
| 8 | 91 | cascade | 68.7 | 0.85 | 509 | 2,059 | rtx4090 | 0.000 | 5 | 51% | README_TASK_DIFF 0.5d ago |
| 9 | 62 | Ridges | 68.4 | 0.85 | 454 | 2,103 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.8d ago |
| 10 | 38 | ChronoLLM | 67.5 | 0.85 | 146 | 3,097 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 5.0d ago |
| 11 | 15 | ORO | 67.4 | 1.0 | 10.23 | 19.64 | cpu-small | 0.000 | 67 | 95% | RELEASE 0.6d ago |
| 12 | 11 | TrajectoryRL | 67.0 | 0.85 | 4,069 | 4,069 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 16d ago |
| 13 | 96 | Verathos | 66.9 | 1.0 | 15.31 | 419 | rtx4090 | 0.405 | 79 | 41% | RELEASE 0.1d ago |
| 14 | 85 | Vidaio | 64.1 | 0.85 | 128 | 1,324 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 0.4d ago |
| 15 | 107 | Minos | 64.1 | 1.0 | 115 | 33,463 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 8d ago |
| 16 | 81 | Reliquary | 63.3 | 0.85 | 99.49 | 392 | rtx4090 | 0.000 | 34 | 9% | SCORING_COMMIT 0.2d ago |
| 17 | 53 | engy | 63.0 | 0.85 | 90.67 | 2,133 | rtx4090 | 0.000 | 144 | 11% | SCORING_COMMIT 0.1d ago |
| 18 | 55 | NIOME | 61.4 | 0.85 | 56.36 | 465 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 3.9d ago |
| 19 | 51 | lium.io | 61.0 | 0.85 | 57.82 | 912 | rtx4090 | 0.000 | 53 | 80% | SCORING_COMMIT 0.4d ago |
| 20 | 28 | gm | 60.9 | 0.85 | 50.20 | 2,236 | rtx4090 | 0.000 | 40 | 23% | RELEASE 0.1d ago |
| 21 | 60 | Bitsec.ai | 58.9 | 0.85 | 366 | 366 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 11d ago |
| 22 | 74 | Gittensor | 58.0 | 0.85 | 22.14 | 197 | rtx4090 | 0.631 | 14 | 63% | RELEASE 7.0d ago |
| 23 | 102 | ConnitoAI | 57.2 | 0.85 | 568 | 1,365 | rtx4090 | 0.250 | 7 | 27% | RELEASE 18d ago |
| 24 | 68 | NOVA | 55.0 | 0.6 | 7,966 | 7,966 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 2.2d ago |
| 25 | 120 | Affine | 54.5 | 0.6 | 6,314 | 6,314 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 6.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.94 | cpu-small | 285.97265882518826 |
| 54 | Yanez | -3.44 | a4000 | 958.9337398309574 |
| 123 | MANTIS | -6.09 | rtx4090 | 79.6859081031212 |
| 75 | Hippius | -6.23 | rtx4090 | 11193.950305240367 |
| 114 | SOMA | -8.12 | rtx4090 | 4135.9113607136105 |
| 89 | InfiniteQuant | -8.16 | rtx4090 | 169.47075805320537 |
| 101 | Tag101 | -0.14 | cpu-small | 2.104891107858514 |
| 104 | Masx.ai | -2.11 | rtx4090 | 7.16532742489779 |
| 13 | Data Universe | -3.98 | rtx4090 | 4.777777627656375 |
| 88 | Investing | -5.25 | rtx4090 | 636.4441510316398 |
| 8 | Vanta | -7.97 | rtx4090 | 2803.7598403127827 |
| 43 | Graphite | -0.83 | cpu-small | 23.585826264701844 |
| 32 | ItsAI | -0.30 | rtx4090 | 10.201095234482857 |
| 19 | blockmachine | -2.77 | rtx4090 | 540.225826709517 |
| 22 | Desearch | -3.30 | rtx4090 | 68.52247614620197 |
| 18 | Zeus | -4.32 | rtx4090 | 1450.9354852974009 |
| 45 | AlphaRidge.ai | -5.55 | rtx4090 | 9.58895706677736 |
| 63 | Enigma | -8.15 | rtx4090 | 0.07113022110432059 |
| 105 | Beam | -2.83 | rtx4090 | 70.43281546140092 |
| 84 | ansuz | -8.16 | rtx4090 | 0.059368055776499506 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 18.16 | 35.0 | 15.0 | 10.0 | 1.0 |
| 21 | 16.66 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.01 | 35.0 | 15.0 | 9.85 | 1.0 |
| 26 | 14.6 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 25.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.67 | 35.0 | 15.0 | 9.39 | 1.0 |
| 91 | 24.62 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 24.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.71 | 35.0 | 15.0 | 9.68 | 0.85 |
| 15 | 9.55 | 35.0 | 15.0 | 7.86 | 1.0 |
| 11 | 32.83 | 21.0 | 15.0 | 10.0 | 0.85 |
| 96 | 11.03 | 35.0 | 11.25 | 9.58 | 1.0 |
| 85 | 19.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 107 | 18.77 | 21.0 | 15.0 | 9.38 | 1.0 |
| 81 | 18.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 17.85 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 15.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.09 | 35.0 | 11.25 | 9.45 | 0.85 |
| 28 | 15.55 | 35.0 | 11.25 | 9.87 | 0.85 |
| 60 | 23.33 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.41 | 35.0 | 11.25 | 9.57 | 0.85 |
| 102 | 25.06 | 21.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.48 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.56 | 35.0 | 11.25 | 9.97 | 0.6 |
