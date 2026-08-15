# RANKING - generated 2026-08-15T17:02:47Z, block 8851384

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
| 1 | 107 | Minos | 78.1 | 1.0 | 113 | 32,720 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.1d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.64 | 195 | cpu-small | 0.000 | 10 | 35% | SCORING_COMMIT 6.8d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.41 | 377 | cpu-small | 0.007 | 123 | 10% | SCORING_COMMIT 0.3d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.40 | 75.90 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.1d ago |
| 5 | 1 | Apex | 70.5 | 0.85 | 856 | 1,138 | rtx4090 | 0.548 | 4 | 55% | RELEASE 2.1d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.88 | 445 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 2.0d ago |
| 7 | 41 | Almanac | 69.6 | 1.0 | 12.15 | 54.08 | cpu-small | 0.661 | 72 | 66% | SCORING_COMMIT 2.8d ago |
| 8 | 96 | Verathos | 69.4 | 1.0 | 28.70 | 168 | rtx4090 | 0.408 | 59 | 41% | RELEASE 0.9d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 513 | 967 | rtx4090 | 0.670 | 7 | 67% | SCORING_COMMIT 3.1d ago |
| 10 | 85 | Vidaio | 68.7 | 0.85 | 498 | 510 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 3.3d ago |
| 11 | 62 | Ridges | 68.6 | 0.85 | 483 | 2,238 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.8d ago |
| 12 | 91 | cascade | 68.3 | 0.85 | 443 | 2,276 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 1.7d ago |
| 13 | 15 | ORO | 68.0 | 1.0 | 10.95 | 20.12 | cpu-small | 0.000 | 85 | 93% | SCORING_COMMIT 1.8d ago |
| 14 | 21 | AdTAO | 67.6 | 1.0 | 7.61 | 34.13 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.2d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.41 | 1,332 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.0d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 719 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.1d ago |
| 17 | 55 | NIOME | 61.5 | 0.85 | 57.54 | 479 | rtx4090 | 0.021 | 11 | 29% | SCORING_COMMIT 0.9d ago |
| 18 | 28 | gm | 60.9 | 0.85 | 49.68 | 2,786 | rtx4090 | 0.042 | 36 | 31% | RELEASE 3.1d ago |
| 19 | 102 | ConnitoAI | 59.9 | 0.85 | 1,263 | 1,518 | rtx4090 | 0.251 | 6 | 28% | RELEASE 15d ago |
| 20 | 60 | Bitsec.ai | 59.5 | 0.85 | 428 | 428 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 21 | 74 | Gittensor | 58.2 | 0.85 | 23.75 | 211 | rtx4090 | 0.631 | 15 | 63% | RELEASE 3.9d ago |
| 22 | 61 | RedTeam | 57.4 | 0.85 | 16.59 | 407 | rtx4090 | 0.000 | 81 | 10% | RELEASE 4.4d ago |
| 23 | 120 | Affine | 54.6 | 0.6 | 6,653 | 6,653 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.1d ago |
| 24 | 80 | OpenRoboto | 53.1 | 0.85 | 164 | 595 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 7d ago |
| 25 | 51 | lium.io | 52.8 | 0.85 | 9.53 | 1,455 | rtx4090 | 0.000 | 56 | 84% | SCORING_COMMIT 1.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.07 | a4000 | 958.6147397925355 |
| 104 | Masx.ai | -0.04 | rtx4090 | 9.324914542401006 |
| 75 | Hippius | -7.21 | rtx4090 | 10966.955059360986 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 216.86881484980123 |
| 13 | Data Universe | -3.35 | rtx4090 | 5.758044032401257 |
| 88 | Investing | -5.64 | rtx4090 | 312.3607823840256 |
| 8 | Vanta | -7.96 | rtx4090 | 2919.0576803124277 |
| 114 | SOMA | -8.12 | rtx4090 | 1560.246985441374 |
| 43 | Graphite | -0.47 | cpu-small | 11.355203040075272 |
| 32 | ItsAI | -0.07 | rtx4090 | 11.442990288190796 |
| 22 | Desearch | -3.50 | rtx4090 | 49.90559488512533 |
| 45 | AlphaRidge.ai | -4.48 | rtx4090 | 17.320533149277438 |
| 18 | Zeus | -5.17 | rtx4090 | 1069.2362202776908 |
| 123 | MANTIS | -6.07 | rtx4090 | 77.90617944473932 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07568823242582845 |
| 105 | Beam | -2.75 | rtx4090 | 85.43792974294087 |
| 34 | BitMind | -20.34 | a100-80 | 31.446707945137884 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.72 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 14.73 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.62 | 35.0 | 15.0 | 9.91 | 1.0 |
| 26 | 14.8 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.68 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.16 | 35.0 | 15.0 | 9.17 | 1.0 |
| 41 | 10.18 | 35.0 | 15.0 | 9.46 | 1.0 |
| 96 | 13.4 | 35.0 | 11.25 | 9.77 | 1.0 |
| 56 | 24.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.08 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.8 | 35.0 | 15.0 | 8.19 | 1.0 |
| 21 | 8.5 | 35.0 | 15.0 | 9.13 | 1.0 |
| 38 | 18.13 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.39 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.51 | 35.0 | 11.25 | 9.87 | 0.85 |
| 102 | 28.21 | 21.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.95 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.68 | 35.0 | 11.25 | 9.58 | 0.85 |
| 61 | 11.33 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.77 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.17 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 9.3 | 35.0 | 11.25 | 6.54 | 0.85 |
