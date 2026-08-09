# RANKING - generated 2026-08-09T17:45:21Z, block 8808406

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
| 1 | 107 | Minos | 78.5 | 1.0 | 124 | 35,305 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 5.6d ago |
| 2 | 76 | Phylax | 76.8 | 1.0 | 68.56 | 207 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.8d ago |
| 3 | 60 | Bitsec.ai | 75.1 | 0.85 | 1,292 | 1,292 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.9d ago |
| 4 | 67 | Harnyx | 70.8 | 1.0 | 15.20 | 868 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.3d ago |
| 5 | 91 | cascade | 70.2 | 0.85 | 797 | 2,728 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.6d ago |
| 6 | 1 | Apex | 70.1 | 0.85 | 764 | 1,575 | rtx4090 | 0.486 | 4 | 49% | RELEASE 1.9d ago |
| 7 | 96 | Verathos | 70.1 | 1.0 | 34.36 | 170 | rtx4090 | 0.419 | 59 | 42% | RELEASE 0.2d ago |
| 8 | 41 | Almanac | 69.4 | 1.0 | 11.63 | 35.08 | cpu-small | 0.721 | 66 | 72% | SCORING_COMMIT 2.7d ago |
| 9 | 62 | Ridges | 68.3 | 0.85 | 443 | 2,053 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.8d ago |
| 10 | 26 | Perturb | 68.3 | 1.0 | 21.81 | 40.22 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.1d ago |
| 11 | 100 | BASE | 68.1 | 0.85 | 420 | 1,704 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.9d ago |
| 12 | 15 | ORO | 67.9 | 1.0 | 10.17 | 19.43 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.3d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 216 | 3,632 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.3d ago |
| 14 | 21 | AdTAO | 65.5 | 1.0 | 4.79 | 22.13 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.1d ago |
| 15 | 80 | OpenRoboto | 65.0 | 0.85 | 164 | 596 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 1.5d ago |
| 16 | 28 | gm | 64.5 | 0.85 | 146 | 4,212 | rtx4090 | 0.278 | 25 | 42% | RELEASE 1.9d ago |
| 17 | 61 | RedTeam | 63.2 | 0.85 | 97.65 | 276 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.3d ago |
| 18 | 6 | Numinous | 59.1 | 1.0 | 29.79 | 342 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 19 | 51 | lium.io | 58.7 | 0.85 | 32.30 | 3,102 | rtx4090 | 0.000 | 49 | 60% | SCORING_COMMIT 1.9d ago |
| 20 | 56 | Gradients | 56.7 | 0.85 | 482 | 1,015 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 21 | 85 | Vidaio | 55.8 | 0.85 | 369 | 369 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 12d ago |
| 22 | 120 | Affine | 54.8 | 0.6 | 7,363 | 7,363 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.2d ago |
| 23 | 2 | DSperse | 54.8 | 0.85 | 7.02 | 107 | rtx4090 | 0.827 | 12 | 83% | RELEASE 3.5d ago |
| 24 | 124 | Swarm | 53.9 | 0.85 | 220 | 671 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |
| 25 | 74 | Gittensor | 52.7 | 0.85 | 5.71 | 226 | rtx4090 | 0.630 | 16 | 63% | RELEASE 2.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.75 | a4000 | 1063.874858728139 |
| 104 | Masx.ai | -2.22 | rtx4090 | 9.044833318330003 |
| 13 | Data Universe | -2.80 | rtx4090 | 7.477017963021613 |
| 88 | Investing | -4.72 | rtx4090 | 472.48466977459236 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 125.59735494875706 |
| 8 | Vanta | -7.38 | rtx4090 | 3413.2089758210695 |
| 22 | Desearch | -0.86 | rtx4090 | 72.61139408291865 |
| 19 | blockmachine | -1.16 | rtx4090 | 185.07133888649628 |
| 45 | AlphaRidge.ai | -1.32 | rtx4090 | 40.31462957730089 |
| 75 | Hippius | -4.37 | rtx4090 | 5.910381388659426 |
| 18 | Zeus | -4.37 | rtx4090 | 998.2709963093682 |
| 123 | MANTIS | -6.20 | rtx4090 | 74.83401850979439 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0764964088810013 |
| 105 | Beam | -4.19 | rtx4090 | 190.57010757115782 |
| 84 | ansuz | -8.15 | rtx4090 | 506.285460821035 |
| 34 | BitMind | -18.22 | a100-80 | 301.5093909804202 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 19.07 | 35.0 | 15.0 | 9.45 | 1.0 |
| 76 | 16.76 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.3 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.0 | 35.0 | 15.0 | 9.76 | 1.0 |
| 91 | 26.39 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 14.08 | 35.0 | 11.25 | 9.8 | 1.0 |
| 41 | 10.02 | 35.0 | 15.0 | 9.41 | 1.0 |
| 62 | 24.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.35 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 23.87 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.53 | 35.0 | 15.0 | 8.36 | 1.0 |
| 38 | 21.26 | 35.0 | 11.25 | 9.76 | 0.85 |
| 21 | 6.94 | 35.0 | 15.0 | 8.56 | 1.0 |
| 80 | 20.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 19.7 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 18.14 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 13.54 | 21.0 | 15.0 | 9.54 | 1.0 |
| 51 | 13.85 | 35.0 | 11.25 | 8.93 | 0.85 |
| 56 | 24.41 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.36 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.17 | 35.0 | 11.25 | 9.99 | 0.6 |
| 2 | 8.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 124 | 21.33 | 21.0 | 11.25 | 9.84 | 0.85 |
| 74 | 7.52 | 35.0 | 11.25 | 8.19 | 0.85 |
