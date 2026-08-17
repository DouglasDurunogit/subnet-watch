# RANKING - generated 2026-08-17T04:10:59Z, block 8861925

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
| 1 | 107 | Minos | 78.3 | 1.0 | 117 | 32,881 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.5d ago |
| 2 | 67 | Harnyx | 72.1 | 1.0 | 21.31 | 399 | cpu-small | 0.008 | 128 | 11% | SCORING_COMMIT 0.9d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.72 | 74.69 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.5d ago |
| 4 | 1 | Apex | 70.6 | 0.85 | 885 | 992 | rtx4090 | 0.537 | 4 | 54% | RELEASE 3.6d ago |
| 5 | 76 | Phylax | 70.5 | 1.0 | 13.36 | 156 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.7d ago |
| 6 | 96 | Verathos | 70.0 | 1.0 | 33.14 | 391 | rtx4090 | 0.409 | 54 | 41% | RELEASE 2.3d ago |
| 7 | 91 | cascade | 69.1 | 0.85 | 570 | 2,304 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 3.2d ago |
| 8 | 15 | ORO | 69.0 | 1.0 | 12.65 | 21.47 | cpu-small | 0.000 | 67 | 94% | SCORING_COMMIT 3.3d ago |
| 9 | 85 | Vidaio | 68.8 | 0.85 | 520 | 659 | rtx4090 | 0.000 | 10 | 21% | SCORING_COMMIT 0.5d ago |
| 10 | 56 | Gradients | 68.7 | 0.85 | 503 | 961 | rtx4090 | 0.681 | 7 | 68% | SCORING_COMMIT 4.6d ago |
| 11 | 41 | Almanac | 68.7 | 1.0 | 9.76 | 53.68 | cpu-small | 0.694 | 75 | 69% | SCORING_COMMIT 4.2d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 467 | 2,162 | rtx4090 | 0.000 | 6 | 40% | RELEASE 2.2d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.66 | 34.33 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.7d ago |
| 14 | 38 | ChronoLLM | 66.1 | 0.85 | 100 | 1,372 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.5d ago |
| 15 | 124 | Swarm | 65.9 | 0.85 | 225 | 722 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.5d ago |
| 16 | 98 | NeverPlayAlone | 64.1 | 0.85 | 1,696 | 1,696 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 10d ago |
| 17 | 55 | NIOME | 61.5 | 0.85 | 57.32 | 483 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.3d ago |
| 18 | 28 | gm | 60.2 | 0.85 | 41.02 | 2,255 | rtx4090 | 0.108 | 43 | 25% | RELEASE 4.6d ago |
| 19 | 60 | Bitsec.ai | 59.1 | 0.85 | 386 | 386 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 20 | 74 | Gittensor | 58.2 | 0.85 | 23.85 | 214 | rtx4090 | 0.630 | 14 | 63% | RELEASE 5.4d ago |
| 21 | 61 | RedTeam | 57.1 | 0.85 | 14.83 | 411 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.8d ago |
| 22 | 51 | lium.io | 55.4 | 0.85 | 15.29 | 2,608 | rtx4090 | 0.000 | 59 | 74% | SCORING_COMMIT 2.8d ago |
| 23 | 68 | NOVA | 55.1 | 0.6 | 8,113 | 8,113 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.6d ago |
| 24 | 93 | Bitcast | 54.7 | 0.85 | 269 | 486 | rtx4090 | 0.000 | 4 | 83% | SCORING_COMMIT 19d ago |
| 25 | 120 | Affine | 54.6 | 0.6 | 6,676 | 6,676 | rtx4090 | 0.202 | 5 | 20% | SCORING_COMMIT 4.6d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 226.47520692495496 |
| 54 | Yanez | -4.56 | a4000 | 955.1300650992561 |
| 104 | Masx.ai | -0.46 | rtx4090 | 9.520159001347386 |
| 75 | Hippius | -7.21 | rtx4090 | 10877.569320968874 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 154.64465883319795 |
| 13 | Data Universe | -3.69 | rtx4090 | 6.248140821304027 |
| 88 | Investing | -5.20 | rtx4090 | 268.9947483563988 |
| 8 | Vanta | -7.96 | rtx4090 | 2857.3498906064196 |
| 114 | SOMA | -8.12 | rtx4090 | 637.1375264465985 |
| 43 | Graphite | -0.78 | cpu-small | 16.713766255936832 |
| 45 | AlphaRidge.ai | -4.06 | rtx4090 | 23.07988434875217 |
| 22 | Desearch | -4.70 | rtx4090 | 57.3179383303149 |
| 18 | Zeus | -5.28 | rtx4090 | 1176.4290230705271 |
| 123 | MANTIS | -6.18 | rtx4090 | 75.81736551638987 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07675909205078546 |
| 105 | Beam | -2.94 | rtx4090 | 111.1278913520587 |
| 84 | ansuz | -8.16 | rtx4090 | 439.12623036737097 |
| 34 | BitMind | -19.74 | a100-80 | 25.91336525261472 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.84 | 35.0 | 15.0 | 9.44 | 1.0 |
| 67 | 12.27 | 35.0 | 15.0 | 9.87 | 1.0 |
| 26 | 14.74 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.81 | 35.0 | 11.25 | 10.0 | 0.85 |
| 76 | 10.52 | 35.0 | 15.0 | 10.0 | 1.0 |
| 96 | 13.95 | 35.0 | 11.25 | 9.8 | 1.0 |
| 91 | 25.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.33 | 35.0 | 15.0 | 8.71 | 1.0 |
| 85 | 24.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.38 | 35.0 | 15.0 | 9.33 | 1.0 |
| 62 | 24.28 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.53 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.24 | 35.0 | 15.0 | 9.52 | 0.85 |
| 124 | 21.41 | 35.0 | 11.25 | 9.85 | 0.85 |
| 98 | 29.37 | 21.0 | 15.0 | 10.0 | 0.85 |
| 55 | 16.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.77 | 35.0 | 11.25 | 9.84 | 0.85 |
| 60 | 23.54 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.69 | 35.0 | 11.25 | 9.59 | 0.85 |
| 61 | 10.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 11.02 | 35.0 | 11.25 | 7.85 | 0.85 |
| 68 | 35.56 | 35.0 | 11.25 | 10.0 | 0.6 |
| 93 | 22.11 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.78 | 35.0 | 11.25 | 9.99 | 0.6 |
