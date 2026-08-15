# RANKING - generated 2026-08-15T08:41:40Z, block 8848878

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
| 1 | 107 | Minos | 77.5 | 1.0 | 99.16 | 32,100 | cpu-small | 0.000 | 19 | 91% | README_TASK_DIFF 4.7d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.45 | 194 | cpu-small | 0.000 | 10 | 35% | SCORING_COMMIT 6.4d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.36 | 376 | cpu-small | 0.016 | 120 | 10% | SCORING_COMMIT 0.2d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 41.27 | 75.66 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.7d ago |
| 5 | 1 | Apex | 70.6 | 0.85 | 893 | 1,101 | rtx4090 | 0.548 | 4 | 55% | RELEASE 1.8d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.81 | 443 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 1.7d ago |
| 7 | 41 | Almanac | 69.6 | 1.0 | 12.06 | 53.62 | cpu-small | 0.661 | 72 | 66% | SCORING_COMMIT 2.4d ago |
| 8 | 96 | Verathos | 69.5 | 1.0 | 29.28 | 222 | rtx4090 | 0.436 | 53 | 44% | RELEASE 0.5d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 513 | 963 | rtx4090 | 0.667 | 7 | 67% | SCORING_COMMIT 2.8d ago |
| 10 | 62 | Ridges | 68.6 | 0.85 | 485 | 2,244 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.4d ago |
| 11 | 91 | cascade | 68.6 | 0.85 | 484 | 1,114 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.4d ago |
| 12 | 15 | ORO | 68.0 | 1.0 | 10.87 | 20.16 | cpu-small | 0.000 | 82 | 93% | SCORING_COMMIT 1.4d ago |
| 13 | 21 | AdTAO | 67.5 | 1.0 | 7.41 | 33.33 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 3.9d ago |
| 14 | 85 | Vidaio | 66.9 | 0.85 | 296 | 478 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 2.9d ago |
| 15 | 38 | ChronoLLM | 66.1 | 0.85 | 99.64 | 1,362 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.7d ago |
| 16 | 124 | Swarm | 65.8 | 0.85 | 222 | 718 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 3.7d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.53 | 477 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 0.5d ago |
| 18 | 28 | gm | 60.2 | 0.85 | 41.30 | 2,480 | rtx4090 | 0.127 | 32 | 29% | RELEASE 2.8d ago |
| 19 | 60 | Bitsec.ai | 59.5 | 0.85 | 433 | 433 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 2 | DSperse | 58.1 | 0.85 | 20.16 | 70.67 | rtx4090 | 0.823 | 11 | 82% | RELEASE 4.5d ago |
| 21 | 74 | Gittensor | 57.8 | 0.85 | 20.88 | 211 | rtx4090 | 0.631 | 15 | 63% | RELEASE 3.6d ago |
| 22 | 61 | RedTeam | 57.8 | 0.85 | 18.65 | 768 | rtx4090 | 0.000 | 70 | 18% | RELEASE 4.0d ago |
| 23 | 51 | lium.io | 57.6 | 0.85 | 25.02 | 1,841 | rtx4090 | 0.000 | 45 | 78% | SCORING_COMMIT 1.0d ago |
| 24 | 120 | Affine | 54.6 | 0.6 | 6,571 | 6,571 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.8d ago |
| 25 | 80 | OpenRoboto | 53.2 | 0.85 | 172 | 622 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.15 | a4000 | 949.183937360482 |
| 75 | Hippius | -7.21 | rtx4090 | 10925.584215348 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 228.51088422603408 |
| 101 | Tag101 | -0.08 | cpu-small | 2.109398746171863 |
| 13 | Data Universe | -3.42 | rtx4090 | 5.797241297367347 |
| 88 | Investing | -5.88 | rtx4090 | 869.8466248353124 |
| 8 | Vanta | -7.96 | rtx4090 | 2906.626641700711 |
| 114 | SOMA | -8.13 | rtx4090 | 1536.1636258448668 |
| 43 | Graphite | -0.47 | cpu-small | 11.31337901188105 |
| 45 | AlphaRidge.ai | -4.47 | rtx4090 | 16.46732772718108 |
| 18 | Zeus | -5.12 | rtx4090 | 1093.3215614449196 |
| 22 | Desearch | -5.57 | rtx4090 | 63.67329900316373 |
| 123 | MANTIS | -6.02 | rtx4090 | 79.82860304729516 |
| 63 | Enigma | -8.14 | rtx4090 | 4942.030133960511 |
| 105 | Beam | -2.60 | rtx4090 | 82.05517438476181 |
| 34 | BitMind | -19.51 | a100-80 | 22.317935801906806 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.2 | 35.0 | 15.0 | 9.34 | 1.0 |
| 76 | 14.71 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.61 | 35.0 | 15.0 | 9.86 | 1.0 |
| 26 | 14.79 | 35.0 | 11.25 | 9.81 | 1.0 |
| 1 | 26.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.15 | 35.0 | 15.0 | 9.17 | 1.0 |
| 41 | 10.15 | 35.0 | 15.0 | 9.45 | 1.0 |
| 96 | 13.47 | 35.0 | 11.25 | 9.76 | 1.0 |
| 56 | 24.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.43 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.77 | 35.0 | 15.0 | 8.23 | 1.0 |
| 21 | 8.41 | 35.0 | 15.0 | 9.11 | 1.0 |
| 85 | 22.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.22 | 35.0 | 15.0 | 9.51 | 0.85 |
| 124 | 21.36 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.79 | 35.0 | 11.25 | 9.84 | 0.85 |
| 60 | 23.99 | 21.0 | 15.0 | 10.0 | 0.85 |
| 2 | 12.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.19 | 35.0 | 11.25 | 9.53 | 0.85 |
| 61 | 11.76 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.87 | 35.0 | 11.25 | 8.69 | 0.85 |
| 120 | 34.72 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.35 | 21.0 | 11.25 | 10.0 | 0.85 |
