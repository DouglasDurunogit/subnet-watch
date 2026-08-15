# RANKING - generated 2026-08-15T09:06:01Z, block 8849000

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
| 1 | 107 | Minos | 77.5 | 1.0 | 98.95 | 32,033 | cpu-small | 0.000 | 19 | 91% | README_TASK_DIFF 4.7d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.38 | 193 | cpu-small | 0.000 | 10 | 35% | SCORING_COMMIT 6.5d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.30 | 375 | cpu-small | 0.016 | 120 | 10% | SCORING_COMMIT 0.0d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.18 | 75.55 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.7d ago |
| 5 | 1 | Apex | 70.6 | 0.85 | 890 | 1,097 | rtx4090 | 0.549 | 4 | 55% | RELEASE 1.8d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.77 | 442 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 1.7d ago |
| 7 | 41 | Almanac | 69.6 | 1.0 | 12.04 | 53.52 | cpu-small | 0.661 | 72 | 66% | SCORING_COMMIT 2.4d ago |
| 8 | 96 | Verathos | 69.5 | 1.0 | 29.22 | 221 | rtx4090 | 0.436 | 53 | 44% | RELEASE 0.5d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 512 | 961 | rtx4090 | 0.667 | 7 | 67% | SCORING_COMMIT 2.8d ago |
| 10 | 62 | Ridges | 68.6 | 0.85 | 484 | 2,240 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.4d ago |
| 11 | 91 | cascade | 68.6 | 0.85 | 483 | 1,112 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.4d ago |
| 12 | 15 | ORO | 67.6 | 1.0 | 10.94 | 20.29 | cpu-small | 0.000 | 82 | 93% | SCORING_COMMIT 1.5d ago |
| 13 | 21 | AdTAO | 67.5 | 1.0 | 7.40 | 33.27 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 3.9d ago |
| 14 | 85 | Vidaio | 66.9 | 0.85 | 296 | 479 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 2.9d ago |
| 15 | 38 | ChronoLLM | 66.1 | 0.85 | 99.67 | 1,362 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.7d ago |
| 16 | 124 | Swarm | 65.8 | 0.85 | 222 | 716 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 3.7d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.41 | 477 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 0.5d ago |
| 18 | 28 | gm | 60.6 | 0.85 | 45.13 | 2,005 | rtx4090 | 0.127 | 33 | 23% | RELEASE 2.8d ago |
| 19 | 60 | Bitsec.ai | 59.5 | 0.85 | 430 | 430 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 74 | Gittensor | 57.8 | 0.85 | 20.83 | 211 | rtx4090 | 0.631 | 15 | 63% | RELEASE 3.6d ago |
| 21 | 61 | RedTeam | 57.8 | 0.85 | 18.54 | 765 | rtx4090 | 0.000 | 70 | 18% | RELEASE 4.0d ago |
| 22 | 51 | lium.io | 57.6 | 0.85 | 24.97 | 1,838 | rtx4090 | 0.000 | 45 | 78% | SCORING_COMMIT 1.0d ago |
| 23 | 120 | Affine | 54.6 | 0.6 | 6,563 | 6,563 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.8d ago |
| 24 | 80 | OpenRoboto | 53.2 | 0.85 | 170 | 616 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 7d ago |
| 25 | 97 | Albedo | 52.5 | 0.6 | 2,781 | 2,781 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.15 | a4000 | 947.451586448189 |
| 75 | Hippius | -7.21 | rtx4090 | 10905.773543413334 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 228.0938301407546 |
| 101 | Tag101 | -0.08 | cpu-small | 2.1053465676275125 |
| 13 | Data Universe | -3.58 | rtx4090 | 5.904400241291086 |
| 88 | Investing | -5.89 | rtx4090 | 866.9424544077541 |
| 8 | Vanta | -7.96 | rtx4090 | 2902.4957792318664 |
| 114 | SOMA | -8.12 | rtx4090 | 1550.457586480157 |
| 43 | Graphite | -0.48 | cpu-small | 11.29273101976811 |
| 32 | ItsAI | -0.02 | rtx4090 | 10.428114194063559 |
| 45 | AlphaRidge.ai | -4.47 | rtx4090 | 16.43727328874364 |
| 18 | Zeus | -5.12 | rtx4090 | 1092.0925803535822 |
| 22 | Desearch | -5.72 | rtx4090 | 106.25533016428457 |
| 123 | MANTIS | -6.02 | rtx4090 | 79.66721232389106 |
| 63 | Enigma | -8.14 | rtx4090 | 4933.178394053669 |
| 105 | Beam | -2.47 | rtx4090 | 83.8860549446256 |
| 34 | BitMind | -19.53 | a100-80 | 22.277976264679285 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.19 | 35.0 | 15.0 | 9.34 | 1.0 |
| 76 | 14.7 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.6 | 35.0 | 15.0 | 9.86 | 1.0 |
| 26 | 14.78 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.14 | 35.0 | 15.0 | 9.17 | 1.0 |
| 41 | 10.14 | 35.0 | 15.0 | 9.45 | 1.0 |
| 96 | 13.46 | 35.0 | 11.25 | 9.78 | 1.0 |
| 56 | 24.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.42 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.8 | 35.0 | 15.0 | 7.8 | 1.0 |
| 21 | 8.41 | 35.0 | 15.0 | 9.11 | 1.0 |
| 85 | 22.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.22 | 35.0 | 15.0 | 9.51 | 0.85 |
| 124 | 21.35 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.13 | 35.0 | 11.25 | 9.85 | 0.85 |
| 60 | 23.96 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.18 | 35.0 | 11.25 | 9.53 | 0.85 |
| 61 | 11.74 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.86 | 35.0 | 11.25 | 8.69 | 0.85 |
| 120 | 34.72 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.31 | 21.0 | 11.25 | 10.0 | 0.85 |
| 97 | 31.33 | 35.0 | 11.25 | 9.98 | 0.6 |
