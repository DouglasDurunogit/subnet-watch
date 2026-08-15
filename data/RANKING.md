# RANKING - generated 2026-08-15T19:43:58Z, block 8852190

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
| 1 | 107 | Minos | 78.0 | 1.0 | 111 | 32,054 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.2d ago |
| 2 | 76 | Phylax | 74.6 | 1.0 | 39.43 | 189 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 0.1d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.25 | 374 | cpu-small | 0.007 | 123 | 10% | SCORING_COMMIT 0.4d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 41.16 | 75.66 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.2d ago |
| 5 | 1 | Apex | 70.4 | 0.85 | 846 | 1,125 | rtx4090 | 0.552 | 4 | 55% | RELEASE 2.2d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.83 | 443 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 2.1d ago |
| 7 | 96 | Verathos | 70.2 | 1.0 | 34.75 | 169 | rtx4090 | 0.415 | 55 | 42% | RELEASE 1.0d ago |
| 8 | 41 | Almanac | 69.6 | 1.0 | 12.07 | 53.95 | cpu-small | 0.662 | 72 | 66% | SCORING_COMMIT 2.9d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 510 | 963 | rtx4090 | 0.670 | 7 | 67% | SCORING_COMMIT 3.2d ago |
| 10 | 62 | Ridges | 68.5 | 0.85 | 479 | 2,217 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.9d ago |
| 11 | 85 | Vidaio | 68.3 | 0.85 | 443 | 566 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 3.4d ago |
| 12 | 91 | cascade | 68.3 | 0.85 | 442 | 2,269 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 1.9d ago |
| 13 | 15 | ORO | 68.2 | 1.0 | 10.87 | 20.16 | cpu-small | 0.000 | 86 | 93% | SCORING_COMMIT 1.9d ago |
| 14 | 21 | AdTAO | 67.6 | 1.0 | 7.58 | 34.02 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.3d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.24 | 1,330 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.1d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 718 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.2d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.62 | 480 | rtx4090 | 0.021 | 11 | 29% | SCORING_COMMIT 1.0d ago |
| 18 | 28 | gm | 60.5 | 0.85 | 43.80 | 2,521 | rtx4090 | 0.161 | 36 | 28% | RELEASE 3.2d ago |
| 19 | 60 | Bitsec.ai | 59.3 | 0.85 | 411 | 411 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 74 | Gittensor | 58.7 | 0.85 | 26.74 | 210 | rtx4090 | 0.631 | 15 | 63% | RELEASE 4.1d ago |
| 21 | 102 | ConnitoAI | 58.3 | 0.85 | 790 | 2,228 | rtx4090 | 0.251 | 6 | 41% | RELEASE 15d ago |
| 22 | 61 | RedTeam | 57.3 | 0.85 | 16.13 | 420 | rtx4090 | 0.000 | 81 | 10% | RELEASE 4.5d ago |
| 23 | 51 | lium.io | 56.2 | 0.85 | 18.21 | 1,441 | rtx4090 | 0.000 | 54 | 81% | SCORING_COMMIT 1.4d ago |
| 24 | 120 | Affine | 54.6 | 0.6 | 6,633 | 6,633 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.2d ago |
| 25 | 80 | OpenRoboto | 53.1 | 0.85 | 165 | 599 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.89 | a4000 | 957.5416668537612 |
| 104 | Masx.ai | -2.14 | rtx4090 | 11.65775512028493 |
| 75 | Hippius | -7.38 | rtx4090 | 10912.692229331971 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 216.5304617580848 |
| 101 | Tag101 | -0.03 | cpu-small | 1.9869608076124476 |
| 13 | Data Universe | -3.41 | rtx4090 | 5.747615465284082 |
| 88 | Investing | -5.54 | rtx4090 | 324.0837869120957 |
| 8 | Vanta | -7.96 | rtx4090 | 2911.0193095206664 |
| 114 | SOMA | -8.12 | rtx4090 | 622.563637068786 |
| 43 | Graphite | -0.47 | cpu-small | 11.319060560993126 |
| 45 | AlphaRidge.ai | -3.93 | rtx4090 | 16.669755502556082 |
| 22 | Desearch | -4.70 | rtx4090 | 67.00891978758747 |
| 18 | Zeus | -5.18 | rtx4090 | 1065.717293191584 |
| 123 | MANTIS | -6.10 | rtx4090 | 77.58614660677927 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07546503668427958 |
| 105 | Beam | -2.73 | rtx4090 | 84.93311029792055 |
| 34 | BitMind | -20.18 | a100-80 | 28.979320649511344 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.64 | 35.0 | 15.0 | 9.41 | 1.0 |
| 76 | 14.61 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.59 | 35.0 | 15.0 | 9.95 | 1.0 |
| 26 | 14.78 | 35.0 | 11.25 | 9.77 | 1.0 |
| 1 | 26.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.15 | 35.0 | 15.0 | 9.17 | 1.0 |
| 96 | 14.13 | 35.0 | 11.25 | 9.81 | 1.0 |
| 41 | 10.15 | 35.0 | 15.0 | 9.45 | 1.0 |
| 56 | 24.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.77 | 35.0 | 15.0 | 8.46 | 1.0 |
| 21 | 8.49 | 35.0 | 15.0 | 9.13 | 1.0 |
| 38 | 18.12 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.39 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.02 | 35.0 | 11.25 | 9.85 | 0.85 |
| 60 | 23.78 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 13.13 | 35.0 | 11.25 | 9.63 | 0.85 |
| 102 | 26.36 | 21.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 11.67 | 35.0 | 11.25 | 8.19 | 0.85 |
| 120 | 34.76 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.2 | 21.0 | 11.25 | 10.0 | 0.85 |
