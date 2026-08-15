# RANKING - generated 2026-08-15T00:02:03Z, block 8846280

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
| 1 | 107 | Minos | 78.1 | 1.0 | 113 | 31,797 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 4.4d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.07 | 192 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 6.1d ago |
| 3 | 67 | Harnyx | 72.4 | 1.0 | 23.19 | 477 | cpu-small | 0.015 | 125 | 13% | SCORING_COMMIT 0.5d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.72 | 76.47 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.4d ago |
| 5 | 1 | Apex | 70.0 | 0.85 | 733 | 1,156 | rtx4090 | 0.574 | 4 | 57% | RELEASE 1.4d ago |
| 6 | 91 | cascade | 69.6 | 0.85 | 654 | 2,256 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.0d ago |
| 7 | 41 | Almanac | 69.1 | 1.0 | 10.59 | 26.18 | cpu-small | 0.723 | 68 | 72% | SCORING_COMMIT 2.0d ago |
| 8 | 56 | Gradients | 68.8 | 0.85 | 521 | 975 | rtx4090 | 0.663 | 7 | 66% | SCORING_COMMIT 2.4d ago |
| 9 | 85 | Vidaio | 68.4 | 0.85 | 460 | 515 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 2.6d ago |
| 10 | 62 | Ridges | 68.1 | 0.85 | 424 | 1,966 | rtx4090 | 0.133 | 7 | 35% | RELEASE 0.1d ago |
| 11 | 15 | ORO | 68.0 | 1.0 | 10.53 | 21.06 | cpu-small | 0.000 | 84 | 93% | SCORING_COMMIT 1.1d ago |
| 12 | 96 | Verathos | 67.8 | 1.0 | 19.11 | 185 | rtx4090 | 0.421 | 62 | 42% | RELEASE 0.2d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.51 | 33.73 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 3.5d ago |
| 14 | 6 | Numinous | 66.7 | 1.0 | 7.55 | 552 | cpu-small | 0.000 | 19 | 32% | WEIGHTS_VERSION_BUMP 1.3d ago |
| 15 | 38 | ChronoLLM | 66.1 | 0.85 | 100 | 1,369 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.3d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 724 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 3.4d ago |
| 17 | 80 | OpenRoboto | 65.3 | 0.85 | 181 | 653 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 6.8d ago |
| 18 | 28 | gm | 63.5 | 0.85 | 109 | 2,128 | rtx4090 | 0.066 | 31 | 23% | RELEASE 2.4d ago |
| 19 | 55 | NIOME | 61.4 | 0.85 | 56.43 | 477 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 0.2d ago |
| 20 | 60 | Bitsec.ai | 61.2 | 0.85 | 726 | 1,017 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 7d ago |
| 21 | 102 | ConnitoAI | 59.9 | 0.85 | 1,274 | 1,471 | rtx4090 | 0.251 | 6 | 27% | RELEASE 14d ago |
| 22 | 51 | lium.io | 59.4 | 0.85 | 38.01 | 1,452 | rtx4090 | 0.000 | 46 | 79% | SCORING_COMMIT 0.6d ago |
| 23 | 74 | Gittensor | 58.0 | 0.85 | 22.39 | 213 | rtx4090 | 0.630 | 14 | 63% | RELEASE 3.2d ago |
| 24 | 61 | RedTeam | 57.5 | 0.85 | 16.87 | 752 | rtx4090 | 0.000 | 72 | 18% | RELEASE 3.7d ago |
| 25 | 2 | DSperse | 57.2 | 0.85 | 15.26 | 63.95 | rtx4090 | 0.824 | 12 | 82% | RELEASE 4.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.99 | a4000 | 975.7913145962984 |
| 75 | Hippius | -7.19 | rtx4090 | 11098.883300847367 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 230.7348801172791 |
| 101 | Tag101 | -0.11 | cpu-small | 2.3017033136613216 |
| 13 | Data Universe | -3.36 | rtx4090 | 6.200024232439482 |
| 88 | Investing | -5.52 | rtx4090 | 766.4986086468431 |
| 8 | Vanta | -7.96 | rtx4090 | 3028.3086267681647 |
| 114 | SOMA | -8.12 | rtx4090 | 1677.33128640736 |
| 43 | Graphite | -0.49 | cpu-small | 10.633262353819937 |
| 45 | AlphaRidge.ai | -3.72 | rtx4090 | 16.24705757375451 |
| 18 | Zeus | -5.23 | rtx4090 | 1059.8539034533046 |
| 123 | MANTIS | -6.03 | rtx4090 | 80.61725614303187 |
| 22 | Desearch | -6.45 | rtx4090 | 85.5247307023568 |
| 19 | blockmachine | -6.95 | rtx4090 | 4.867301757540097 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07541371191290816 |
| 105 | Beam | -2.64 | rtx4090 | 78.48982453594171 |
| 34 | BitMind | -20.07 | a100-80 | 21.1140695224452 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.71 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 14.68 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.58 | 35.0 | 15.0 | 9.83 | 1.0 |
| 26 | 14.83 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.62 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 9.68 | 35.0 | 15.0 | 9.37 | 1.0 |
| 56 | 24.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 23.9 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.66 | 35.0 | 15.0 | 8.3 | 1.0 |
| 96 | 11.86 | 35.0 | 11.25 | 9.65 | 1.0 |
| 21 | 8.46 | 35.0 | 15.0 | 9.12 | 1.0 |
| 6 | 8.48 | 35.0 | 15.0 | 8.24 | 1.0 |
| 38 | 18.24 | 35.0 | 15.0 | 9.51 | 0.85 |
| 124 | 21.4 | 35.0 | 11.25 | 9.83 | 0.85 |
| 80 | 20.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 18.56 | 35.0 | 11.25 | 9.94 | 0.85 |
| 55 | 16.0 | 35.0 | 11.25 | 9.98 | 0.85 |
| 60 | 26.03 | 21.0 | 15.0 | 10.0 | 0.85 |
| 102 | 28.24 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.47 | 35.0 | 11.25 | 9.13 | 0.85 |
| 74 | 12.45 | 35.0 | 11.25 | 9.55 | 0.85 |
| 61 | 11.39 | 35.0 | 11.25 | 9.99 | 0.85 |
| 2 | 11.02 | 35.0 | 11.25 | 10.0 | 0.85 |
