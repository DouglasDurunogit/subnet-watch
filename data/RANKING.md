# RANKING - generated 2026-08-17T01:52:10Z, block 8861231

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
| 1 | 107 | Minos | 78.1 | 1.0 | 113 | 32,912 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.4d ago |
| 2 | 67 | Harnyx | 72.5 | 1.0 | 23.63 | 418 | cpu-small | 0.011 | 137 | 11% | SCORING_COMMIT 0.8d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.47 | 74.25 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.4d ago |
| 4 | 1 | Apex | 70.6 | 0.85 | 891 | 1,000 | rtx4090 | 0.532 | 4 | 53% | RELEASE 3.5d ago |
| 5 | 76 | Phylax | 70.5 | 1.0 | 13.26 | 156 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.6d ago |
| 6 | 41 | Almanac | 69.9 | 1.0 | 12.91 | 52.78 | cpu-small | 0.650 | 74 | 65% | SCORING_COMMIT 4.1d ago |
| 7 | 96 | Verathos | 69.8 | 1.0 | 31.85 | 384 | rtx4090 | 0.408 | 56 | 41% | RELEASE 2.2d ago |
| 8 | 85 | Vidaio | 69.3 | 0.85 | 592 | 592 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 0.4d ago |
| 9 | 91 | cascade | 69.1 | 0.85 | 564 | 2,282 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 3.1d ago |
| 10 | 15 | ORO | 69.1 | 1.0 | 12.55 | 21.29 | cpu-small | 0.000 | 67 | 94% | SCORING_COMMIT 3.2d ago |
| 11 | 56 | Gradients | 68.7 | 0.85 | 502 | 958 | rtx4090 | 0.681 | 7 | 68% | SCORING_COMMIT 4.5d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 469 | 2,174 | rtx4090 | 0.000 | 6 | 40% | RELEASE 2.1d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.64 | 34.25 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.6d ago |
| 14 | 38 | ChronoLLM | 66.0 | 0.85 | 98.97 | 1,353 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.4d ago |
| 15 | 124 | Swarm | 65.9 | 0.85 | 225 | 721 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.4d ago |
| 16 | 98 | NeverPlayAlone | 64.1 | 0.85 | 1,690 | 1,690 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 10d ago |
| 17 | 2 | DSperse | 63.0 | 0.85 | 90.83 | 137 | rtx4090 | 0.824 | 5 | 82% | RELEASE 6.2d ago |
| 18 | 55 | NIOME | 61.4 | 0.85 | 56.91 | 480 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.2d ago |
| 19 | 28 | gm | 60.3 | 0.85 | 42.59 | 2,655 | rtx4090 | 0.048 | 43 | 29% | RELEASE 4.5d ago |
| 20 | 60 | Bitsec.ai | 59.1 | 0.85 | 382 | 382 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 21 | 51 | lium.io | 58.9 | 0.85 | 33.95 | 2,531 | rtx4090 | 0.000 | 56 | 78% | SCORING_COMMIT 2.7d ago |
| 22 | 74 | Gittensor | 58.0 | 0.85 | 22.41 | 214 | rtx4090 | 0.638 | 14 | 64% | RELEASE 5.3d ago |
| 23 | 61 | RedTeam | 56.9 | 0.85 | 14.15 | 398 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.7d ago |
| 24 | 120 | Affine | 55.1 | 0.6 | 8,215 | 8,215 | rtx4090 | 0.250 | 4 | 25% | SCORING_COMMIT 4.5d ago |
| 25 | 68 | NOVA | 55.1 | 0.6 | 8,077 | 8,077 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.5d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 239.63113101132743 |
| 54 | Yanez | -4.23 | a4000 | 948.4537494960272 |
| 104 | Masx.ai | -0.20 | rtx4090 | 10.257621958260392 |
| 75 | Hippius | -7.38 | rtx4090 | 10849.390346471468 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 153.43575388555467 |
| 13 | Data Universe | -3.54 | rtx4090 | 5.948504534383386 |
| 88 | Investing | -5.14 | rtx4090 | 961.9245388079373 |
| 8 | Vanta | -7.96 | rtx4090 | 2985.2411751024024 |
| 114 | SOMA | -8.12 | rtx4090 | 626.34959341325 |
| 43 | Graphite | -0.78 | cpu-small | 17.363181351538767 |
| 45 | AlphaRidge.ai | -3.18 | rtx4090 | 17.382099229393237 |
| 18 | Zeus | -3.51 | rtx4090 | 1853.384334533055 |
| 22 | Desearch | -4.25 | rtx4090 | 51.30276208050473 |
| 123 | MANTIS | -6.17 | rtx4090 | 74.70532210886735 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07569281649997464 |
| 105 | Beam | -2.98 | rtx4090 | 110.25659091061824 |
| 84 | ansuz | -8.16 | rtx4090 | 437.72616068464134 |
| 34 | BitMind | -20.31 | a100-80 | 23.89708507155147 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.72 | 35.0 | 15.0 | 9.43 | 1.0 |
| 67 | 12.66 | 35.0 | 15.0 | 9.86 | 1.0 |
| 26 | 14.71 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 76 | 10.5 | 35.0 | 15.0 | 10.0 | 1.0 |
| 41 | 10.4 | 35.0 | 15.0 | 9.49 | 1.0 |
| 96 | 13.79 | 35.0 | 11.25 | 9.79 | 1.0 |
| 85 | 25.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.03 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.29 | 35.0 | 15.0 | 8.76 | 1.0 |
| 56 | 24.57 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.52 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.19 | 35.0 | 15.0 | 9.51 | 0.85 |
| 124 | 21.41 | 35.0 | 11.25 | 9.84 | 0.85 |
| 98 | 29.36 | 21.0 | 15.0 | 10.0 | 0.85 |
| 2 | 17.85 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.91 | 35.0 | 11.25 | 9.83 | 0.85 |
| 60 | 23.49 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 14.04 | 35.0 | 11.25 | 9.04 | 0.85 |
| 74 | 12.45 | 35.0 | 11.25 | 9.56 | 0.85 |
| 61 | 10.74 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.6 | 35.0 | 11.25 | 9.99 | 0.6 |
| 68 | 35.54 | 35.0 | 11.25 | 10.0 | 0.6 |
