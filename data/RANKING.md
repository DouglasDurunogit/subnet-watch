# RANKING - generated 2026-08-08T22:42:57Z, block 8802693

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
| 1 | 11 | TrajectoryRL | 79.6 | 0.85 | 4,942 | 4,942 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.5d ago |
| 2 | 107 | Minos | 78.2 | 1.0 | 115 | 34,865 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 4.8d ago |
| 3 | 76 | Phylax | 76.6 | 1.0 | 65.57 | 198 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.0d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,217 | 1,217 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.1d ago |
| 5 | 67 | Harnyx | 71.3 | 1.0 | 17.12 | 744 | cpu-small | 0.017 | 142 | 19% | SCORING_COMMIT 1.8d ago |
| 6 | 91 | cascade | 70.2 | 0.85 | 787 | 2,696 | rtx4090 | 0.000 | 5 | 48% | RELEASE 3.8d ago |
| 7 | 1 | Apex | 69.5 | 0.85 | 637 | 1,643 | rtx4090 | 0.445 | 4 | 45% | RELEASE 1.1d ago |
| 8 | 62 | Ridges | 69.0 | 0.85 | 555 | 2,006 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.0d ago |
| 9 | 26 | Perturb | 68.3 | 1.0 | 21.74 | 40.79 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 2.3d ago |
| 10 | 96 | Verathos | 68.3 | 1.0 | 21.56 | 169 | rtx4090 | 0.418 | 72 | 42% | RELEASE 0.2d ago |
| 11 | 41 | Almanac | 68.3 | 1.0 | 8.81 | 44.88 | cpu-small | 0.760 | 66 | 76% | SCORING_COMMIT 1.9d ago |
| 12 | 15 | ORO | 67.6 | 1.0 | 9.18 | 19.34 | cpu-small | 0.000 | 70 | 94% | RELEASE 2.5d ago |
| 13 | 38 | ChronoLLM | 65.6 | 0.85 | 208 | 3,501 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.5d ago |
| 14 | 21 | AdTAO | 65.6 | 1.0 | 4.82 | 22.22 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.3d ago |
| 15 | 80 | OpenRoboto | 63.7 | 0.85 | 112 | 412 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 0.7d ago |
| 16 | 61 | RedTeam | 62.0 | 0.85 | 67.05 | 194 | rtx4090 | 0.000 | 42 | 6% | RELEASE 1.0d ago |
| 17 | 28 | gm | 61.4 | 0.85 | 57.86 | 3,794 | rtx4090 | 0.184 | 24 | 41% | RELEASE 1.1d ago |
| 18 | 51 | lium.io | 59.3 | 0.85 | 37.56 | 2,961 | rtx4090 | 0.000 | 47 | 67% | SCORING_COMMIT 1.1d ago |
| 19 | 85 | Vidaio | 57.0 | 0.85 | 533 | 572 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 12d ago |
| 20 | 56 | Gradients | 56.5 | 0.85 | 463 | 976 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 21 | 74 | Gittensor | 55.3 | 0.85 | 10.84 | 236 | rtx4090 | 0.631 | 16 | 63% | RELEASE 1.3d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 6,937 | 6,937 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.4d ago |
| 23 | 124 | Swarm | 53.8 | 0.85 | 211 | 644 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 7d ago |
| 24 | 100 | BASE | 52.8 | 0.6 | 3,155 | 3,155 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.1d ago |
| 25 | 97 | Albedo | 52.7 | 0.6 | 2,973 | 2,973 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 6.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.04 | a4000 | 1032.0163780288772 |
| 104 | Masx.ai | -1.50 | rtx4090 | 8.326441954292168 |
| 13 | Data Universe | -3.01 | rtx4090 | 7.31056066276223 |
| 88 | Investing | -6.18 | rtx4090 | 381.9821451367378 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 128.66103845899443 |
| 8 | Vanta | -7.42 | rtx4090 | 3281.3643457015046 |
| 19 | blockmachine | -1.18 | rtx4090 | 191.94072319596594 |
| 22 | Desearch | -2.36 | rtx4090 | 110.63285343503789 |
| 18 | Zeus | -3.40 | rtx4090 | 1396.301100966385 |
| 75 | Hippius | -4.65 | rtx4090 | 5.305927437338098 |
| 45 | AlphaRidge.ai | -4.66 | rtx4090 | 14.322372012521855 |
| 123 | MANTIS | -6.25 | rtx4090 | 72.64972695890481 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0754354766145788 |
| 105 | Beam | -3.80 | rtx4090 | 206.8700294763364 |
| 84 | ansuz | -8.15 | rtx4090 | 498.5331656084125 |
| 34 | BitMind | -18.86 | a100-80 | 290.1189032172374 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.6 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.79 | 35.0 | 15.0 | 9.43 | 1.0 |
| 76 | 16.58 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.06 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.44 | 35.0 | 15.0 | 9.82 | 1.0 |
| 91 | 26.35 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 25.51 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.96 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.34 | 35.0 | 11.25 | 9.69 | 1.0 |
| 96 | 12.31 | 35.0 | 11.25 | 9.69 | 1.0 |
| 41 | 9.02 | 35.0 | 15.0 | 9.25 | 1.0 |
| 15 | 9.16 | 35.0 | 15.0 | 8.41 | 1.0 |
| 38 | 21.11 | 35.0 | 11.25 | 9.76 | 0.85 |
| 21 | 6.95 | 35.0 | 15.0 | 8.62 | 1.0 |
| 80 | 18.66 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 16.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.1 | 35.0 | 11.25 | 9.89 | 0.85 |
| 51 | 14.43 | 35.0 | 11.25 | 9.12 | 0.85 |
| 85 | 24.81 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.25 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.76 | 35.0 | 11.25 | 9.08 | 0.85 |
| 120 | 34.94 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.17 | 21.0 | 11.25 | 9.84 | 0.85 |
| 100 | 31.83 | 35.0 | 11.25 | 10.0 | 0.6 |
| 97 | 31.59 | 35.0 | 11.25 | 9.99 | 0.6 |
