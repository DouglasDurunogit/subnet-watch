# RANKING - generated 2026-08-07T19:28:10Z, block 8794520

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
| 1 | 107 | Minos | 78.0 | 1.0 | 110 | 31,965 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 3.6d ago |
| 2 | 76 | Phylax | 77.1 | 1.0 | 75.73 | 275 | cpu-small | 0.000 | 10 | 31% | SCORING_COMMIT 5.1d ago |
| 3 | 98 | NeverPlayAlone | 76.0 | 0.85 | 1,706 | 1,706 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 0.5d ago |
| 4 | 60 | Bitsec.ai | 75.1 | 0.85 | 1,306 | 1,306 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 0.0d ago |
| 5 | 114 | SOMA | 72.7 | 0.85 | 1,667 | 4,347 | rtx4090 | 0.000 | 3 | 65% | SCORING_COMMIT 0.4d ago |
| 6 | 67 | Harnyx | 72.2 | 1.0 | 21.09 | 764 | cpu-small | 0.012 | 135 | 20% | SCORING_COMMIT 0.7d ago |
| 7 | 102 | ConnitoAI | 69.6 | 0.85 | 656 | 1,363 | rtx4090 | 0.251 | 7 | 25% | RELEASE 6.8d ago |
| 8 | 62 | Ridges | 69.1 | 0.85 | 565 | 2,044 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.9d ago |
| 9 | 91 | cascade | 68.6 | 0.85 | 489 | 1,388 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.6d ago |
| 10 | 15 | ORO | 68.4 | 1.0 | 11.48 | 10,348 | cpu-small | 0.000 | 74 | 93% | RELEASE 1.4d ago |
| 11 | 26 | Perturb | 68.1 | 1.0 | 20.94 | 39.16 | rtx3060 | 0.506 | 11 | 51% | SCORING_COMMIT 1.2d ago |
| 12 | 100 | BASE | 67.9 | 0.85 | 399 | 1,621 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.2d ago |
| 13 | 41 | Almanac | 67.6 | 1.0 | 7.55 | 44.55 | cpu-small | 0.799 | 62 | 80% | SCORING_COMMIT 0.8d ago |
| 14 | 96 | Verathos | 66.9 | 1.0 | 15.48 | 222 | rtx4090 | 0.428 | 65 | 43% | RELEASE 0.8d ago |
| 15 | 124 | Swarm | 65.6 | 0.85 | 211 | 606 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 6.2d ago |
| 16 | 21 | AdTAO | 65.5 | 1.0 | 4.74 | 21.92 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.1d ago |
| 17 | 61 | RedTeam | 61.9 | 0.85 | 66.29 | 183 | rtx4090 | 0.000 | 37 | 6% | RELEASE 2.3d ago |
| 18 | 28 | gm | 59.9 | 0.85 | 37.58 | 4,360 | rtx4090 | 0.216 | 19 | 49% | RELEASE 0.0d ago |
| 19 | 74 | Gittensor | 58.5 | 0.85 | 25.66 | 243 | rtx4090 | 0.601 | 15 | 60% | RELEASE 0.1d ago |
| 20 | 51 | lium.io | 57.9 | 0.85 | 26.52 | 2,745 | rtx4090 | 0.000 | 42 | 69% | SCORING_COMMIT 3.5d ago |
| 21 | 85 | Vidaio | 57.1 | 0.85 | 557 | 584 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 10d ago |
| 22 | 56 | Gradients | 56.4 | 0.85 | 451 | 952 | rtx4090 | 0.701 | 7 | 70% | SCORING_COMMIT 10d ago |
| 23 | 2 | DSperse | 55.6 | 0.85 | 9.29 | 146 | rtx4090 | 0.826 | 9 | 83% | RELEASE 1.6d ago |
| 24 | 120 | Affine | 54.6 | 0.6 | 6,583 | 6,583 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.3d ago |
| 25 | 38 | ChronoLLM | 53.7 | 0.85 | 213 | 3,574 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.68 | a4000 | 1083.1761249413064 |
| 104 | Masx.ai | -2.45 | rtx4090 | 9.572740540779355 |
| 13 | Data Universe | -3.24 | rtx4090 | 6.360278221000348 |
| 88 | Investing | -6.82 | rtx4090 | 636.4836579360234 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 135.64237406801536 |
| 8 | Vanta | -7.44 | rtx4090 | 3182.6572951534113 |
| 32 | ItsAI | -0.16 | rtx4090 | 10.200023185578383 |
| 19 | blockmachine | -1.31 | rtx4090 | 231.49959693613644 |
| 45 | AlphaRidge.ai | -2.55 | rtx4090 | 27.967565558231488 |
| 22 | Desearch | -4.16 | rtx4090 | 72.2548527501231 |
| 75 | Hippius | -4.71 | rtx4090 | 5.2170942900363935 |
| 18 | Zeus | -4.77 | rtx4090 | 1296.755632653586 |
| 123 | MANTIS | -6.20 | rtx4090 | 77.57014665459577 |
| 63 | Enigma | -8.15 | rtx4090 | 0.07375043846310006 |
| 84 | ansuz | -8.15 | rtx4090 | 480.2541911344505 |
| 34 | BitMind | -17.87 | a100-80 | 281.9709170202269 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.62 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 17.14 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.4 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.34 | 35.0 | 15.0 | 10.0 | 0.85 |
| 114 | 29.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.23 | 35.0 | 15.0 | 9.93 | 1.0 |
| 102 | 25.62 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 25.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.47 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.97 | 35.0 | 15.0 | 8.41 | 1.0 |
| 26 | 12.2 | 35.0 | 11.25 | 9.69 | 1.0 |
| 100 | 23.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 8.47 | 35.0 | 15.0 | 9.14 | 1.0 |
| 96 | 11.07 | 35.0 | 11.25 | 9.58 | 1.0 |
| 124 | 21.15 | 35.0 | 11.25 | 9.82 | 0.85 |
| 21 | 6.9 | 35.0 | 15.0 | 8.64 | 1.0 |
| 61 | 16.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.43 | 35.0 | 11.25 | 9.82 | 0.85 |
| 74 | 12.97 | 35.0 | 11.25 | 9.62 | 0.85 |
| 51 | 13.09 | 35.0 | 11.25 | 8.78 | 0.85 |
| 85 | 24.98 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.15 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.73 | 35.0 | 11.25 | 9.98 | 0.6 |
| 38 | 21.19 | 21.0 | 11.25 | 9.78 | 0.85 |
