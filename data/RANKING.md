# RANKING - generated 2026-08-07T22:53:40Z, block 8795547

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
| 1 | 107 | Minos | 78.3 | 1.0 | 118 | 33,236 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 3.8d ago |
| 2 | 60 | Bitsec.ai | 74.8 | 0.85 | 1,213 | 1,213 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 0.1d ago |
| 3 | 114 | SOMA | 72.7 | 0.85 | 1,665 | 4,343 | rtx4090 | 0.000 | 3 | 65% | SCORING_COMMIT 0.6d ago |
| 4 | 67 | Harnyx | 72.2 | 1.0 | 20.98 | 760 | cpu-small | 0.012 | 135 | 20% | SCORING_COMMIT 0.8d ago |
| 5 | 91 | cascade | 69.8 | 0.85 | 702 | 2,832 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.8d ago |
| 6 | 1 | Apex | 69.8 | 0.85 | 699 | 1,604 | rtx4090 | 0.385 | 4 | 38% | RELEASE 0.1d ago |
| 7 | 62 | Ridges | 69.1 | 0.85 | 563 | 2,036 | rtx4090 | 0.133 | 7 | 35% | RELEASE 2.0d ago |
| 8 | 15 | ORO | 68.5 | 1.0 | 11.38 | 10,337 | cpu-small | 0.000 | 74 | 93% | RELEASE 1.5d ago |
| 9 | 26 | Perturb | 68.1 | 1.0 | 20.80 | 40.35 | rtx3060 | 0.506 | 11 | 51% | SCORING_COMMIT 1.3d ago |
| 10 | 100 | BASE | 67.9 | 0.85 | 400 | 1,625 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.3d ago |
| 11 | 41 | Almanac | 67.6 | 1.0 | 7.50 | 33.17 | cpu-small | 0.800 | 63 | 80% | SCORING_COMMIT 0.9d ago |
| 12 | 124 | Swarm | 65.6 | 0.85 | 206 | 593 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 6.4d ago |
| 13 | 21 | AdTAO | 65.5 | 1.0 | 4.69 | 21.70 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.2d ago |
| 14 | 96 | Verathos | 65.0 | 1.0 | 9.81 | 175 | rtx4090 | 0.423 | 84 | 42% | RELEASE 0.9d ago |
| 15 | 61 | RedTeam | 61.8 | 0.85 | 63.01 | 180 | rtx4090 | 0.000 | 37 | 6% | RELEASE 0.0d ago |
| 16 | 102 | ConnitoAI | 59.7 | 0.85 | 33.15 | 1,612 | rtx4090 | 0.251 | 8 | 30% | RELEASE 7.0d ago |
| 17 | 28 | gm | 59.4 | 0.85 | 32.21 | 4,500 | rtx4090 | 0.245 | 19 | 51% | RELEASE 0.1d ago |
| 18 | 74 | Gittensor | 57.7 | 0.85 | 22.80 | 212 | rtx4090 | 0.638 | 15 | 64% | RELEASE 0.3d ago |
| 19 | 51 | lium.io | 56.8 | 0.85 | 22.79 | 2,866 | rtx4090 | 0.000 | 44 | 66% | SCORING_COMMIT 0.1d ago |
| 20 | 56 | Gradients | 56.4 | 0.85 | 450 | 948 | rtx4090 | 0.701 | 7 | 70% | SCORING_COMMIT 10d ago |
| 21 | 2 | DSperse | 54.7 | 0.85 | 6.88 | 145 | rtx4090 | 0.826 | 10 | 83% | RELEASE 1.8d ago |
| 22 | 120 | Affine | 54.6 | 0.6 | 6,596 | 6,596 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.4d ago |
| 23 | 38 | ChronoLLM | 53.7 | 0.85 | 212 | 3,564 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 9d ago |
| 24 | 97 | Albedo | 52.6 | 0.6 | 2,905 | 2,905 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.9d ago |
| 25 | 85 | Vidaio | 52.1 | 0.85 | 124 | 607 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.00 | a4000 | 1051.6402647913326 |
| 104 | Masx.ai | -1.64 | rtx4090 | 7.425886822348048 |
| 13 | Data Universe | -3.31 | rtx4090 | 6.283299594886655 |
| 88 | Investing | -6.84 | rtx4090 | 628.2394883841372 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 133.1919901008286 |
| 8 | Vanta | -7.44 | rtx4090 | 3164.653924814796 |
| 32 | ItsAI | -0.15 | rtx4090 | 9.402529274990362 |
| 22 | Desearch | -0.32 | rtx4090 | 84.914555182307 |
| 19 | blockmachine | -1.60 | rtx4090 | 300.9147819295693 |
| 18 | Zeus | -3.39 | rtx4090 | 1704.1468955251628 |
| 45 | AlphaRidge.ai | -3.75 | rtx4090 | 24.598839516412603 |
| 75 | Hippius | -4.70 | rtx4090 | 5.2345385178441495 |
| 123 | MANTIS | -6.31 | rtx4090 | 78.48572722245801 |
| 63 | Enigma | -8.15 | rtx4090 | 0.0733493764986097 |
| 84 | ansuz | -8.15 | rtx4090 | 479.048470516625 |
| 34 | BitMind | -18.28 | a100-80 | 281.0777872395938 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.88 | 35.0 | 15.0 | 9.46 | 1.0 |
| 60 | 28.05 | 35.0 | 15.0 | 10.0 | 0.85 |
| 114 | 29.3 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.21 | 35.0 | 15.0 | 9.96 | 1.0 |
| 91 | 25.89 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 25.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 25.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.94 | 35.0 | 15.0 | 8.59 | 1.0 |
| 26 | 12.17 | 35.0 | 11.25 | 9.69 | 1.0 |
| 100 | 23.68 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 8.45 | 35.0 | 15.0 | 9.14 | 1.0 |
| 124 | 21.07 | 35.0 | 11.25 | 9.84 | 0.85 |
| 21 | 6.86 | 35.0 | 15.0 | 8.62 | 1.0 |
| 96 | 9.4 | 35.0 | 11.25 | 9.34 | 1.0 |
| 61 | 16.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 13.95 | 35.0 | 11.25 | 9.99 | 0.85 |
| 28 | 13.84 | 35.0 | 11.25 | 9.8 | 0.85 |
| 74 | 12.52 | 35.0 | 11.25 | 9.07 | 0.85 |
| 51 | 12.52 | 35.0 | 11.25 | 8.09 | 0.85 |
| 56 | 24.14 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 8.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.74 | 35.0 | 11.25 | 9.99 | 0.6 |
| 38 | 21.18 | 21.0 | 11.25 | 9.78 | 0.85 |
| 97 | 31.5 | 35.0 | 11.25 | 9.98 | 0.6 |
| 85 | 19.08 | 21.0 | 11.25 | 10.0 | 0.85 |
