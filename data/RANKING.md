# RANKING - generated 2026-08-15T04:44:35Z, block 8847693

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
| 1 | 107 | Minos | 78.0 | 1.0 | 111 | 31,583 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 4.6d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 39.93 | 191 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 6.3d ago |
| 3 | 67 | Harnyx | 72.6 | 1.0 | 23.92 | 384 | cpu-small | 0.056 | 111 | 10% | SCORING_COMMIT 0.0d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.64 | 76.33 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.6d ago |
| 5 | 1 | Apex | 70.7 | 0.85 | 916 | 1,129 | rtx4090 | 0.540 | 4 | 54% | RELEASE 1.6d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.91 | 445 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 1.5d ago |
| 7 | 91 | cascade | 69.6 | 0.85 | 649 | 2,238 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.2d ago |
| 8 | 41 | Almanac | 69.6 | 1.0 | 11.99 | 54.18 | cpu-small | 0.666 | 72 | 67% | SCORING_COMMIT 2.2d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 517 | 971 | rtx4090 | 0.665 | 7 | 67% | SCORING_COMMIT 2.6d ago |
| 10 | 62 | Ridges | 68.6 | 0.85 | 489 | 2,262 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.3d ago |
| 11 | 96 | Verathos | 68.3 | 1.0 | 21.66 | 196 | rtx4090 | 0.413 | 65 | 41% | RELEASE 0.4d ago |
| 12 | 15 | ORO | 68.1 | 1.0 | 10.92 | 22.01 | cpu-small | 0.000 | 83 | 93% | SCORING_COMMIT 1.3d ago |
| 13 | 21 | AdTAO | 67.5 | 1.0 | 7.38 | 33.20 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 3.7d ago |
| 14 | 85 | Vidaio | 66.9 | 0.85 | 296 | 477 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 2.8d ago |
| 15 | 38 | ChronoLLM | 66.1 | 0.85 | 99.96 | 1,366 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.5d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 225 | 725 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 3.6d ago |
| 17 | 80 | OpenRoboto | 65.2 | 0.85 | 174 | 630 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 7.0d ago |
| 18 | 98 | NeverPlayAlone | 64.1 | 0.85 | 1,711 | 1,711 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 8d ago |
| 19 | 28 | gm | 63.5 | 0.85 | 109 | 1,975 | rtx4090 | 0.330 | 27 | 33% | RELEASE 2.6d ago |
| 20 | 55 | NIOME | 61.5 | 0.85 | 57.56 | 485 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 0.4d ago |
| 21 | 60 | Bitsec.ai | 61.2 | 0.85 | 717 | 1,004 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 7d ago |
| 22 | 51 | lium.io | 59.1 | 0.85 | 35.57 | 1,768 | rtx4090 | 0.000 | 46 | 79% | SCORING_COMMIT 0.8d ago |
| 23 | 102 | ConnitoAI | 59.0 | 0.85 | 962 | 1,673 | rtx4090 | 0.251 | 6 | 30% | RELEASE 14d ago |
| 24 | 2 | DSperse | 58.1 | 0.85 | 20.25 | 88.47 | rtx4090 | 0.823 | 11 | 82% | RELEASE 4.3d ago |
| 25 | 74 | Gittensor | 58.0 | 0.85 | 22.20 | 213 | rtx4090 | 0.630 | 14 | 63% | RELEASE 3.4d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.91 | a4000 | 973.7783150615523 |
| 75 | Hippius | -7.20 | rtx4090 | 10989.925644818779 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 230.37973423573823 |
| 101 | Tag101 | -0.07 | cpu-small | 2.2948460617526485 |
| 13 | Data Universe | -3.32 | rtx4090 | 5.9573771755169025 |
| 88 | Investing | -5.65 | rtx4090 | 898.2529356781658 |
| 8 | Vanta | -7.96 | rtx4090 | 2929.504145517592 |
| 114 | SOMA | -8.12 | rtx4090 | 1620.706289992698 |
| 43 | Graphite | -0.52 | cpu-small | 11.301440621817504 |
| 32 | ItsAI | -0.00 | rtx4090 | 9.796632108506584 |
| 45 | AlphaRidge.ai | -3.87 | rtx4090 | 17.545933566921672 |
| 18 | Zeus | -5.09 | rtx4090 | 1101.4773455142647 |
| 123 | MANTIS | -6.04 | rtx4090 | 80.29366615297816 |
| 22 | Desearch | -6.15 | rtx4090 | 86.26365168663315 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0753053220661415 |
| 105 | Beam | -2.57 | rtx4090 | 78.2543814358663 |
| 34 | BitMind | -19.55 | a100-80 | 23.783186778682868 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.62 | 35.0 | 15.0 | 9.41 | 1.0 |
| 76 | 14.66 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.7 | 35.0 | 15.0 | 9.87 | 1.0 |
| 26 | 14.82 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.17 | 35.0 | 15.0 | 9.17 | 1.0 |
| 91 | 25.58 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 10.13 | 35.0 | 15.0 | 9.45 | 1.0 |
| 56 | 24.69 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.46 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.33 | 35.0 | 11.25 | 9.69 | 1.0 |
| 15 | 9.79 | 35.0 | 15.0 | 8.28 | 1.0 |
| 21 | 8.4 | 35.0 | 15.0 | 9.1 | 1.0 |
| 85 | 22.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.23 | 35.0 | 15.0 | 9.51 | 0.85 |
| 124 | 21.41 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 20.4 | 35.0 | 11.25 | 10.0 | 0.85 |
| 98 | 29.41 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 18.56 | 35.0 | 11.25 | 9.94 | 0.85 |
| 55 | 16.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 25.97 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 14.22 | 35.0 | 11.25 | 9.07 | 0.85 |
| 102 | 27.13 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 12.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.42 | 35.0 | 11.25 | 9.55 | 0.85 |
