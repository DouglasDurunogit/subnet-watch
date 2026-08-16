# RANKING - generated 2026-08-16T04:07:33Z, block 8854708

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
| 1 | 107 | Minos | 78.1 | 1.0 | 112 | 31,647 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.5d ago |
| 2 | 76 | Phylax | 73.9 | 1.0 | 32.63 | 184 | cpu-small | 0.000 | 10 | 28% | SCORING_COMMIT 0.2d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.49 | 426 | cpu-small | 0.144 | 118 | 14% | SCORING_COMMIT 0.8d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.94 | 75.28 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.5d ago |
| 5 | 1 | Apex | 70.3 | 0.85 | 809 | 1,110 | rtx4090 | 0.528 | 4 | 53% | RELEASE 2.6d ago |
| 6 | 41 | Almanac | 69.9 | 1.0 | 12.81 | 53.83 | cpu-small | 0.652 | 74 | 65% | SCORING_COMMIT 3.2d ago |
| 7 | 96 | Verathos | 69.6 | 1.0 | 30.37 | 223 | rtx4090 | 0.412 | 59 | 41% | RELEASE 1.3d ago |
| 8 | 56 | Gradients | 68.7 | 0.85 | 507 | 959 | rtx4090 | 0.673 | 7 | 67% | SCORING_COMMIT 3.6d ago |
| 9 | 85 | Vidaio | 68.6 | 0.85 | 492 | 492 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 3.7d ago |
| 10 | 62 | Ridges | 68.5 | 0.85 | 474 | 2,198 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.2d ago |
| 11 | 15 | ORO | 68.4 | 1.0 | 11.32 | 12,323 | cpu-small | 0.000 | 86 | 93% | SCORING_COMMIT 2.2d ago |
| 12 | 91 | cascade | 68.3 | 0.85 | 441 | 2,268 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.2d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.66 | 34.33 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.7d ago |
| 14 | 38 | ChronoLLM | 66.0 | 0.85 | 97.14 | 1,328 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.5d ago |
| 15 | 124 | Swarm | 65.8 | 0.85 | 221 | 711 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.5d ago |
| 16 | 2 | DSperse | 63.0 | 0.85 | 90.17 | 145 | rtx4090 | 0.822 | 5 | 82% | RELEASE 5.3d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.45 | 477 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.3d ago |
| 18 | 28 | gm | 60.5 | 0.85 | 44.38 | 2,475 | rtx4090 | 0.097 | 39 | 29% | RELEASE 3.6d ago |
| 19 | 60 | Bitsec.ai | 59.3 | 0.85 | 413 | 413 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 102 | ConnitoAI | 58.7 | 0.85 | 878 | 1,977 | rtx4090 | 0.251 | 6 | 36% | RELEASE 15d ago |
| 21 | 74 | Gittensor | 58.6 | 0.85 | 26.11 | 209 | rtx4090 | 0.630 | 15 | 63% | RELEASE 4.4d ago |
| 22 | 61 | RedTeam | 57.5 | 0.85 | 16.98 | 434 | rtx4090 | 0.000 | 81 | 10% | RELEASE 4.8d ago |
| 23 | 51 | lium.io | 57.3 | 0.85 | 23.00 | 1,391 | rtx4090 | 0.000 | 51 | 82% | SCORING_COMMIT 1.8d ago |
| 24 | 120 | Affine | 56.8 | 0.6 | 16,542 | 16,542 | rtx4090 | 0.500 | 2 | 50% | SCORING_COMMIT 3.6d ago |
| 25 | 80 | OpenRoboto | 53.1 | 0.85 | 164 | 595 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 243.11030488676383 |
| 54 | Yanez | -3.61 | a4000 | 960.335899574037 |
| 104 | Masx.ai | -0.19 | rtx4090 | 11.270471606702548 |
| 89 | InfiniteQuant | -4.20 | rtx4090 | 186.95539931769588 |
| 75 | Hippius | -7.39 | rtx4090 | 10814.53895141496 |
| 13 | Data Universe | -3.53 | rtx4090 | 5.739900368284406 |
| 88 | Investing | -5.47 | rtx4090 | 1107.957826030406 |
| 8 | Vanta | -7.70 | rtx4090 | 2899.9147472956697 |
| 114 | SOMA | -8.13 | rtx4090 | 602.0243766728884 |
| 43 | Graphite | -0.48 | cpu-small | 14.531663915783431 |
| 32 | ItsAI | -0.40 | rtx4090 | 10.898937655030249 |
| 22 | Desearch | -3.07 | rtx4090 | 54.76822971899355 |
| 45 | AlphaRidge.ai | -3.43 | rtx4090 | 16.342349041442016 |
| 18 | Zeus | -5.11 | rtx4090 | 723.8352494286091 |
| 19 | blockmachine | -6.04 | rtx4090 | 1059.1978458549638 |
| 123 | MANTIS | -6.10 | rtx4090 | 75.87680149480767 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07685000752745488 |
| 105 | Beam | -2.84 | rtx4090 | 85.64071312725846 |
| 34 | BitMind | -20.90 | a100-80 | 30.810625181868065 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.69 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 13.89 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.63 | 35.0 | 15.0 | 9.88 | 1.0 |
| 26 | 14.76 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.45 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.37 | 35.0 | 15.0 | 9.49 | 1.0 |
| 96 | 13.61 | 35.0 | 11.25 | 9.78 | 1.0 |
| 56 | 24.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.35 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.92 | 35.0 | 15.0 | 8.52 | 1.0 |
| 91 | 24.06 | 35.0 | 11.25 | 9.99 | 0.85 |
| 21 | 8.53 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.12 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.34 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 17.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.07 | 35.0 | 11.25 | 9.85 | 0.85 |
| 60 | 23.8 | 21.0 | 15.0 | 10.0 | 0.85 |
| 102 | 26.77 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 13.04 | 35.0 | 11.25 | 9.62 | 0.85 |
| 61 | 11.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.55 | 35.0 | 11.25 | 8.57 | 0.85 |
| 120 | 38.37 | 35.0 | 11.25 | 10.0 | 0.6 |
| 80 | 20.17 | 21.0 | 11.25 | 10.0 | 0.85 |
