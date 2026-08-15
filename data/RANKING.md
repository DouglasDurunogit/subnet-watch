# RANKING - generated 2026-08-15T17:32:21Z, block 8851532

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
| 1 | 107 | Minos | 78.1 | 1.0 | 113 | 32,525 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.1d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.58 | 194 | cpu-small | 0.000 | 10 | 35% | SCORING_COMMIT 6.8d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.37 | 376 | cpu-small | 0.007 | 123 | 10% | SCORING_COMMIT 0.4d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.33 | 75.77 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.1d ago |
| 5 | 1 | Apex | 70.5 | 0.85 | 852 | 1,133 | rtx4090 | 0.549 | 4 | 55% | RELEASE 2.1d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.85 | 444 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 2.0d ago |
| 7 | 41 | Almanac | 69.6 | 1.0 | 12.09 | 54.04 | cpu-small | 0.662 | 72 | 66% | SCORING_COMMIT 2.8d ago |
| 8 | 96 | Verathos | 69.4 | 1.0 | 28.64 | 168 | rtx4090 | 0.408 | 59 | 41% | RELEASE 0.9d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 512 | 965 | rtx4090 | 0.670 | 7 | 67% | SCORING_COMMIT 3.1d ago |
| 10 | 85 | Vidaio | 68.7 | 0.85 | 497 | 510 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 3.3d ago |
| 11 | 62 | Ridges | 68.6 | 0.85 | 483 | 2,235 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.8d ago |
| 12 | 91 | cascade | 68.3 | 0.85 | 442 | 2,272 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 1.8d ago |
| 13 | 15 | ORO | 68.0 | 1.0 | 10.86 | 20.14 | cpu-small | 0.000 | 86 | 93% | SCORING_COMMIT 1.8d ago |
| 14 | 21 | AdTAO | 67.6 | 1.0 | 7.59 | 34.06 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.2d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.27 | 1,330 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.0d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 718 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.1d ago |
| 17 | 55 | NIOME | 61.5 | 0.85 | 57.44 | 479 | rtx4090 | 0.021 | 11 | 29% | SCORING_COMMIT 0.9d ago |
| 18 | 28 | gm | 60.4 | 0.85 | 43.27 | 2,105 | rtx4090 | 0.274 | 34 | 27% | RELEASE 3.1d ago |
| 19 | 102 | ConnitoAI | 59.9 | 0.85 | 1,259 | 1,512 | rtx4090 | 0.251 | 6 | 28% | RELEASE 15d ago |
| 20 | 60 | Bitsec.ai | 59.4 | 0.85 | 425 | 425 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 21 | 74 | Gittensor | 58.2 | 0.85 | 23.70 | 210 | rtx4090 | 0.631 | 15 | 63% | RELEASE 4.0d ago |
| 22 | 61 | RedTeam | 57.4 | 0.85 | 16.50 | 405 | rtx4090 | 0.000 | 81 | 10% | RELEASE 4.4d ago |
| 23 | 2 | DSperse | 57.4 | 0.85 | 16.22 | 96.09 | rtx4090 | 0.824 | 10 | 82% | RELEASE 4.9d ago |
| 24 | 120 | Affine | 54.6 | 0.6 | 6,642 | 6,642 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.1d ago |
| 25 | 80 | OpenRoboto | 53.1 | 0.85 | 167 | 604 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.08 | a4000 | 957.0312993934779 |
| 104 | Masx.ai | -0.05 | rtx4090 | 9.310283536351465 |
| 75 | Hippius | -7.21 | rtx4090 | 10950.517936860468 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 216.52881967743883 |
| 13 | Data Universe | -3.35 | rtx4090 | 5.814331151423098 |
| 88 | Investing | -5.61 | rtx4090 | 315.4928421725182 |
| 8 | Vanta | -7.96 | rtx4090 | 3031.5860999309066 |
| 114 | SOMA | -8.12 | rtx4090 | 1557.9812462753962 |
| 43 | Graphite | -0.47 | cpu-small | 11.337409913842679 |
| 32 | ItsAI | -0.02 | rtx4090 | 11.350863272958552 |
| 45 | AlphaRidge.ai | -4.46 | rtx4090 | 17.29294046715796 |
| 22 | Desearch | -4.71 | rtx4090 | 102.8080405430138 |
| 18 | Zeus | -5.18 | rtx4090 | 1067.5606637671474 |
| 123 | MANTIS | -6.07 | rtx4090 | 77.78404432693557 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07557287070056462 |
| 105 | Beam | -2.78 | rtx4090 | 84.8969173274201 |
| 34 | BitMind | -20.44 | a100-80 | 31.294846523058418 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.69 | 35.0 | 15.0 | 9.4 | 1.0 |
| 76 | 14.72 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.61 | 35.0 | 15.0 | 9.91 | 1.0 |
| 26 | 14.79 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.66 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.16 | 35.0 | 15.0 | 9.17 | 1.0 |
| 41 | 10.16 | 35.0 | 15.0 | 9.45 | 1.0 |
| 96 | 13.39 | 35.0 | 11.25 | 9.77 | 1.0 |
| 56 | 24.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.53 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.07 | 35.0 | 11.25 | 9.98 | 0.85 |
| 15 | 9.77 | 35.0 | 15.0 | 8.27 | 1.0 |
| 21 | 8.5 | 35.0 | 15.0 | 9.13 | 1.0 |
| 38 | 18.12 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.39 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.97 | 35.0 | 11.25 | 9.85 | 0.85 |
| 102 | 28.2 | 21.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.91 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.67 | 35.0 | 11.25 | 9.58 | 0.85 |
| 61 | 11.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 2 | 11.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.77 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.23 | 21.0 | 11.25 | 10.0 | 0.85 |
