# RANKING - generated 2026-08-09T09:52:42Z, block 8806042

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
| 1 | 11 | TrajectoryRL | 79.5 | 0.85 | 4,825 | 4,825 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.9d ago |
| 2 | 107 | Minos | 78.5 | 1.0 | 123 | 35,083 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.2d ago |
| 3 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,247 | 1,247 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.6d ago |
| 4 | 76 | Phylax | 74.9 | 1.0 | 42.67 | 203 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.5d ago |
| 5 | 67 | Harnyx | 70.7 | 1.0 | 15.11 | 864 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 2.3d ago |
| 6 | 1 | Apex | 70.2 | 0.85 | 787 | 1,622 | rtx4090 | 0.454 | 4 | 45% | RELEASE 1.6d ago |
| 7 | 91 | cascade | 70.2 | 0.85 | 783 | 2,680 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.2d ago |
| 8 | 100 | BASE | 69.4 | 0.85 | 623 | 1,676 | rtx4090 | 0.000 | 4 | 50% | SCORING_COMMIT 0.5d ago |
| 9 | 41 | Almanac | 69.4 | 1.0 | 11.57 | 34.55 | cpu-small | 0.717 | 67 | 72% | SCORING_COMMIT 2.4d ago |
| 10 | 96 | Verathos | 69.1 | 1.0 | 26.80 | 290 | rtx4090 | 0.409 | 71 | 41% | RELEASE 0.0d ago |
| 11 | 62 | Ridges | 68.3 | 0.85 | 441 | 2,043 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.5d ago |
| 12 | 26 | Perturb | 68.3 | 1.0 | 22.00 | 41.71 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 2.8d ago |
| 13 | 15 | ORO | 67.3 | 1.0 | 8.91 | 19.17 | cpu-small | 0.000 | 71 | 94% | RELEASE 3.0d ago |
| 14 | 38 | ChronoLLM | 65.7 | 0.85 | 215 | 3,608 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.0d ago |
| 15 | 21 | AdTAO | 65.6 | 1.0 | 4.89 | 22.52 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.8d ago |
| 16 | 80 | OpenRoboto | 64.8 | 0.85 | 155 | 564 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 1.2d ago |
| 17 | 28 | gm | 64.5 | 0.85 | 143 | 4,162 | rtx4090 | 0.192 | 25 | 43% | RELEASE 1.5d ago |
| 18 | 61 | RedTeam | 62.9 | 0.85 | 87.69 | 249 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.3d ago |
| 19 | 51 | lium.io | 60.0 | 0.85 | 44.81 | 2,991 | rtx4090 | 0.000 | 48 | 66% | SCORING_COMMIT 1.6d ago |
| 20 | 102 | ConnitoAI | 59.5 | 0.85 | 1,141 | 1,194 | rtx4090 | 0.250 | 6 | 25% | RELEASE 8d ago |
| 21 | 6 | Numinous | 59.1 | 1.0 | 29.77 | 342 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 22 | 85 | Vidaio | 56.7 | 0.85 | 481 | 540 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 12d ago |
| 23 | 56 | Gradients | 56.6 | 0.85 | 478 | 1,008 | rtx4090 | 0.705 | 7 | 71% | SCORING_COMMIT 11d ago |
| 24 | 2 | DSperse | 56.2 | 0.85 | 11.25 | 126 | rtx4090 | 0.826 | 15 | 83% | RELEASE 3.2d ago |
| 25 | 120 | Affine | 54.8 | 0.6 | 7,336 | 7,336 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.88 | a4000 | 1031.3965171292823 |
| 104 | Masx.ai | -1.70 | rtx4090 | 9.631030157068514 |
| 13 | Data Universe | -2.72 | rtx4090 | 6.955835007419848 |
| 88 | Investing | -5.70 | rtx4090 | 497.3704064541714 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 130.03125156716965 |
| 8 | Vanta | -7.39 | rtx4090 | 3398.3078212600326 |
| 19 | blockmachine | -1.26 | rtx4090 | 297.88882388714666 |
| 45 | AlphaRidge.ai | -1.47 | rtx4090 | 37.57435787143505 |
| 18 | Zeus | -4.31 | rtx4090 | 1335.7552346466723 |
| 75 | Hippius | -4.41 | rtx4090 | 5.662302174545278 |
| 123 | MANTIS | -6.20 | rtx4090 | 74.2540656080138 |
| 63 | Enigma | -8.14 | rtx4090 | 5017.307784217353 |
| 105 | Beam | -4.47 | rtx4090 | 175.88995378981417 |
| 84 | ansuz | -8.15 | rtx4090 | 504.0665411626084 |
| 34 | BitMind | -18.23 | a100-80 | 299.57969912154056 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.5 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 19.03 | 35.0 | 15.0 | 9.45 | 1.0 |
| 60 | 28.16 | 35.0 | 15.0 | 10.0 | 0.85 |
| 76 | 14.92 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 10.98 | 35.0 | 15.0 | 9.72 | 1.0 |
| 1 | 26.34 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.32 | 35.0 | 11.25 | 9.98 | 0.85 |
| 100 | 25.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.0 | 35.0 | 15.0 | 9.41 | 1.0 |
| 96 | 13.13 | 35.0 | 11.25 | 9.74 | 1.0 |
| 62 | 24.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.39 | 35.0 | 11.25 | 9.69 | 1.0 |
| 15 | 9.06 | 35.0 | 15.0 | 8.27 | 1.0 |
| 38 | 21.23 | 35.0 | 11.25 | 9.76 | 0.85 |
| 21 | 7.0 | 35.0 | 15.0 | 8.6 | 1.0 |
| 80 | 19.95 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 19.64 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 17.72 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 15.11 | 35.0 | 11.25 | 9.24 | 0.85 |
| 102 | 27.81 | 21.0 | 11.25 | 10.0 | 0.85 |
| 6 | 13.53 | 21.0 | 15.0 | 9.54 | 1.0 |
| 85 | 24.4 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.38 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.9 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.16 | 35.0 | 11.25 | 9.99 | 0.6 |
