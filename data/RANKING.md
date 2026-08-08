# RANKING - generated 2026-08-08T23:11:51Z, block 8802838

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
| 1 | 11 | TrajectoryRL | 79.5 | 0.85 | 4,912 | 4,912 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.5d ago |
| 2 | 107 | Minos | 78.3 | 1.0 | 117 | 34,538 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 4.8d ago |
| 3 | 76 | Phylax | 76.6 | 1.0 | 65.42 | 197 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.1d ago |
| 4 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,745 | 1,745 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 1.7d ago |
| 5 | 60 | Bitsec.ai | 74.8 | 0.85 | 1,215 | 1,215 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.2d ago |
| 6 | 67 | Harnyx | 70.8 | 1.0 | 15.18 | 857 | cpu-small | 0.057 | 143 | 22% | SCORING_COMMIT 1.8d ago |
| 7 | 91 | cascade | 70.2 | 0.85 | 788 | 2,697 | rtx4090 | 0.000 | 5 | 48% | RELEASE 3.8d ago |
| 8 | 100 | BASE | 70.2 | 0.85 | 781 | 1,570 | rtx4090 | 0.000 | 3 | 50% | SCORING_COMMIT 0.1d ago |
| 9 | 1 | Apex | 69.7 | 0.85 | 667 | 1,691 | rtx4090 | 0.427 | 4 | 43% | RELEASE 1.1d ago |
| 10 | 62 | Ridges | 69.0 | 0.85 | 553 | 2,002 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.1d ago |
| 11 | 96 | Verathos | 68.8 | 1.0 | 24.43 | 174 | rtx4090 | 0.411 | 71 | 41% | RELEASE 0.2d ago |
| 12 | 26 | Perturb | 68.3 | 1.0 | 21.73 | 40.45 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 2.3d ago |
| 13 | 41 | Almanac | 68.2 | 1.0 | 8.74 | 45.14 | cpu-small | 0.761 | 66 | 76% | SCORING_COMMIT 1.9d ago |
| 14 | 15 | ORO | 67.6 | 1.0 | 9.16 | 19.30 | cpu-small | 0.000 | 70 | 94% | RELEASE 2.5d ago |
| 15 | 21 | AdTAO | 65.6 | 1.0 | 4.80 | 22.17 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.3d ago |
| 16 | 38 | ChronoLLM | 65.5 | 0.85 | 208 | 3,494 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.6d ago |
| 17 | 80 | OpenRoboto | 63.6 | 0.85 | 108 | 398 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 0.8d ago |
| 18 | 61 | RedTeam | 62.2 | 0.85 | 70.76 | 204 | rtx4090 | 0.000 | 42 | 6% | RELEASE 1.0d ago |
| 19 | 28 | gm | 61.4 | 0.85 | 57.23 | 4,341 | rtx4090 | 0.000 | 25 | 47% | RELEASE 1.1d ago |
| 20 | 51 | lium.io | 58.7 | 0.85 | 31.92 | 2,797 | rtx4090 | 0.000 | 47 | 69% | SCORING_COMMIT 1.1d ago |
| 21 | 102 | ConnitoAI | 57.0 | 0.85 | 531 | 1,368 | rtx4090 | 0.250 | 7 | 28% | RELEASE 8d ago |
| 22 | 85 | Vidaio | 57.0 | 0.85 | 527 | 527 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 12d ago |
| 23 | 56 | Gradients | 56.5 | 0.85 | 462 | 974 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 24 | 74 | Gittensor | 55.3 | 0.85 | 10.76 | 235 | rtx4090 | 0.631 | 16 | 63% | RELEASE 1.3d ago |
| 25 | 120 | Affine | 54.7 | 0.6 | 6,923 | 6,923 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.4d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.90 | a4000 | 1021.2723583850885 |
| 104 | Masx.ai | -1.77 | rtx4090 | 8.545399906340021 |
| 13 | Data Universe | -3.01 | rtx4090 | 7.132983981068668 |
| 88 | Investing | -6.19 | rtx4090 | 381.137505978615 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 128.28050910004774 |
| 8 | Vanta | -7.42 | rtx4090 | 3386.33057383716 |
| 19 | blockmachine | -1.06 | rtx4090 | 218.6742492217736 |
| 18 | Zeus | -3.41 | rtx4090 | 1393.2141876077615 |
| 45 | AlphaRidge.ai | -4.17 | rtx4090 | 16.731915750240418 |
| 75 | Hippius | -4.66 | rtx4090 | 5.297346362174557 |
| 123 | MANTIS | -6.29 | rtx4090 | 72.31716328370514 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0752722819951233 |
| 105 | Beam | -3.95 | rtx4090 | 201.1254017526389 |
| 84 | ansuz | -8.15 | rtx4090 | 497.42934156636545 |
| 34 | BitMind | -18.72 | a100-80 | 289.60084938794444 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.57 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.84 | 35.0 | 15.0 | 9.44 | 1.0 |
| 76 | 16.57 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.49 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.06 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 10.99 | 35.0 | 15.0 | 9.8 | 1.0 |
| 91 | 26.35 | 35.0 | 11.25 | 9.99 | 0.85 |
| 100 | 26.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 1 | 25.69 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.96 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.78 | 35.0 | 11.25 | 9.73 | 1.0 |
| 26 | 12.34 | 35.0 | 11.25 | 9.7 | 1.0 |
| 41 | 8.99 | 35.0 | 15.0 | 9.24 | 1.0 |
| 15 | 9.16 | 35.0 | 15.0 | 8.48 | 1.0 |
| 21 | 6.95 | 35.0 | 15.0 | 8.62 | 1.0 |
| 38 | 21.1 | 35.0 | 11.25 | 9.76 | 0.85 |
| 80 | 18.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 16.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.05 | 35.0 | 11.25 | 9.88 | 0.85 |
| 51 | 13.8 | 35.0 | 11.25 | 8.96 | 0.85 |
| 102 | 24.79 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.77 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.24 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.74 | 35.0 | 11.25 | 9.08 | 0.85 |
| 120 | 34.93 | 35.0 | 11.25 | 9.99 | 0.6 |
