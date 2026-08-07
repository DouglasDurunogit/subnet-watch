# RANKING - generated 2026-08-07T17:22:06Z, block 8793889

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
| 1 | 107 | Minos | 78.8 | 1.0 | 130 | 31,112 | cpu-small | 0.000 | 20 | 88% | WEIGHTS_VERSION_BUMP 3.5d ago |
| 2 | 76 | Phylax | 77.1 | 1.0 | 75.55 | 273 | cpu-small | 0.000 | 10 | 31% | SCORING_COMMIT 5.0d ago |
| 3 | 98 | NeverPlayAlone | 76.0 | 0.85 | 1,692 | 1,692 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 0.4d ago |
| 4 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,280 | 1,280 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 4.1d ago |
| 5 | 114 | SOMA | 72.7 | 0.85 | 1,650 | 4,304 | rtx4090 | 0.000 | 3 | 65% | SCORING_COMMIT 0.3d ago |
| 6 | 67 | Harnyx | 72.1 | 1.0 | 20.92 | 758 | cpu-small | 0.012 | 135 | 20% | SCORING_COMMIT 0.6d ago |
| 7 | 62 | Ridges | 69.1 | 0.85 | 561 | 2,029 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.8d ago |
| 8 | 91 | cascade | 68.8 | 0.85 | 513 | 1,455 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.5d ago |
| 9 | 15 | ORO | 68.2 | 1.0 | 11.34 | 10,225 | cpu-small | 0.000 | 74 | 93% | RELEASE 1.3d ago |
| 10 | 96 | Verathos | 68.1 | 1.0 | 20.97 | 389 | rtx4090 | 0.422 | 52 | 42% | RELEASE 0.7d ago |
| 11 | 26 | Perturb | 68.1 | 1.0 | 20.84 | 38.88 | rtx3060 | 0.506 | 11 | 51% | SCORING_COMMIT 1.1d ago |
| 12 | 100 | BASE | 67.9 | 0.85 | 396 | 1,609 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.1d ago |
| 13 | 41 | Almanac | 67.5 | 1.0 | 7.39 | 44.41 | cpu-small | 0.800 | 62 | 80% | SCORING_COMMIT 0.7d ago |
| 14 | 124 | Swarm | 65.6 | 0.85 | 207 | 594 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 6.1d ago |
| 15 | 21 | AdTAO | 65.5 | 1.0 | 4.69 | 21.73 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.0d ago |
| 16 | 74 | Gittensor | 65.2 | 0.85 | 179 | 383 | rtx4090 | 0.000 | 9 | 18% | RELEASE 0.1d ago |
| 17 | 61 | RedTeam | 62.0 | 0.85 | 68.38 | 180 | rtx4090 | 0.000 | 37 | 6% | RELEASE 2.2d ago |
| 18 | 102 | ConnitoAI | 59.6 | 0.85 | 32.48 | 1,397 | rtx4090 | 0.251 | 8 | 26% | RELEASE 6.8d ago |
| 19 | 28 | gm | 59.2 | 0.85 | 30.63 | 4,214 | rtx4090 | 0.247 | 19 | 48% | RELEASE 4.1d ago |
| 20 | 51 | lium.io | 57.3 | 0.85 | 22.95 | 2,325 | rtx4090 | 0.000 | 43 | 70% | SCORING_COMMIT 3.4d ago |
| 21 | 56 | Gradients | 56.4 | 0.85 | 448 | 944 | rtx4090 | 0.701 | 7 | 70% | SCORING_COMMIT 10d ago |
| 22 | 2 | DSperse | 56.2 | 0.85 | 11.21 | 140 | rtx4090 | 0.826 | 8 | 83% | RELEASE 1.5d ago |
| 23 | 120 | Affine | 54.6 | 0.6 | 6,531 | 6,531 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.2d ago |
| 24 | 38 | ChronoLLM | 53.7 | 0.85 | 209 | 3,515 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 8d ago |
| 25 | 85 | Vidaio | 53.3 | 0.85 | 175 | 1,039 | rtx4090 | 0.000 | 10 | 32% | SCORING_COMMIT 10d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.78 | a4000 | 1077.4503765450486 |
| 104 | Masx.ai | -2.05 | rtx4090 | 8.655937084730716 |
| 13 | Data Universe | -3.27 | rtx4090 | 6.1008355758276345 |
| 88 | Investing | -6.77 | rtx4090 | 658.5205855654892 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 138.03359683929307 |
| 8 | Vanta | -7.44 | rtx4090 | 3156.21115505409 |
| 32 | ItsAI | -0.21 | rtx4090 | 9.253142519647149 |
| 19 | blockmachine | -1.23 | rtx4090 | 317.57758509983444 |
| 45 | AlphaRidge.ai | -1.94 | rtx4090 | 34.15250486840837 |
| 22 | Desearch | -4.11 | rtx4090 | 68.02269408203507 |
| 75 | Hippius | -4.66 | rtx4090 | 5.170878553327449 |
| 18 | Zeus | -4.80 | rtx4090 | 1287.1224155510488 |
| 123 | MANTIS | -6.29 | rtx4090 | 76.38709013322836 |
| 63 | Enigma | -8.15 | rtx4090 | 0.07315244134396051 |
| 84 | ansuz | -8.15 | rtx4090 | 476.44029133542796 |
| 34 | BitMind | -18.02 | a100-80 | 279.67898642011585 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 19.27 | 35.0 | 15.0 | 9.5 | 1.0 |
| 76 | 17.13 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.37 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.26 | 35.0 | 15.0 | 10.0 | 0.85 |
| 114 | 29.27 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.2 | 35.0 | 15.0 | 9.87 | 1.0 |
| 62 | 25.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.66 | 35.0 | 11.25 | 9.98 | 0.85 |
| 15 | 9.92 | 35.0 | 15.0 | 8.3 | 1.0 |
| 96 | 12.2 | 35.0 | 11.25 | 9.69 | 1.0 |
| 26 | 12.18 | 35.0 | 11.25 | 9.69 | 1.0 |
| 100 | 23.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 8.4 | 35.0 | 15.0 | 9.13 | 1.0 |
| 124 | 21.07 | 35.0 | 11.25 | 9.84 | 0.85 |
| 21 | 6.87 | 35.0 | 15.0 | 8.63 | 1.0 |
| 74 | 20.52 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 16.75 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 13.87 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.64 | 35.0 | 11.25 | 9.79 | 0.85 |
| 51 | 12.55 | 35.0 | 11.25 | 8.6 | 0.85 |
| 56 | 24.12 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.7 | 35.0 | 11.25 | 9.99 | 0.6 |
| 38 | 21.12 | 21.0 | 11.25 | 9.77 | 0.85 |
| 85 | 20.43 | 21.0 | 11.25 | 10.0 | 0.85 |
