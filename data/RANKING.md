# RANKING - generated 2026-08-09T02:25:03Z, block 8803804

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
| 1 | 107 | Minos | 78.3 | 1.0 | 118 | 34,827 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 4.9d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 67.66 | 204 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.2d ago |
| 3 | 98 | NeverPlayAlone | 76.2 | 0.85 | 1,802 | 1,802 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 1.8d ago |
| 4 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,268 | 1,268 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.3d ago |
| 5 | 67 | Harnyx | 70.8 | 1.0 | 15.21 | 866 | cpu-small | 0.030 | 148 | 22% | SCORING_COMMIT 1.9d ago |
| 6 | 1 | Apex | 70.3 | 0.85 | 811 | 1,672 | rtx4090 | 0.425 | 4 | 42% | RELEASE 1.3d ago |
| 7 | 91 | cascade | 70.3 | 0.85 | 804 | 2,753 | rtx4090 | 0.000 | 5 | 48% | RELEASE 3.9d ago |
| 8 | 62 | Ridges | 69.1 | 0.85 | 573 | 2,071 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.2d ago |
| 9 | 96 | Verathos | 68.7 | 1.0 | 24.31 | 300 | rtx4090 | 0.411 | 75 | 41% | RELEASE 0.4d ago |
| 10 | 41 | Almanac | 68.5 | 1.0 | 9.28 | 46.69 | cpu-small | 0.761 | 65 | 76% | SCORING_COMMIT 2.1d ago |
| 11 | 26 | Perturb | 68.4 | 1.0 | 22.41 | 41.94 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 2.5d ago |
| 12 | 15 | ORO | 67.9 | 1.0 | 9.74 | 20.28 | cpu-small | 0.000 | 71 | 94% | RELEASE 2.7d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 216 | 3,629 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.7d ago |
| 14 | 21 | AdTAO | 65.7 | 1.0 | 5.00 | 22.95 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.5d ago |
| 15 | 80 | OpenRoboto | 64.2 | 0.85 | 132 | 484 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 0.9d ago |
| 16 | 61 | RedTeam | 62.3 | 0.85 | 73.79 | 212 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.0d ago |
| 17 | 51 | lium.io | 59.4 | 0.85 | 38.16 | 3,016 | rtx4090 | 0.000 | 47 | 62% | SCORING_COMMIT 1.3d ago |
| 18 | 28 | gm | 59.3 | 0.85 | 31.12 | 2,699 | rtx4090 | 0.598 | 23 | 60% | RELEASE 1.2d ago |
| 19 | 6 | Numinous | 59.1 | 1.0 | 29.90 | 343 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 10d ago |
| 20 | 85 | Vidaio | 57.0 | 0.85 | 539 | 554 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 12d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 478 | 1,008 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 22 | 74 | Gittensor | 55.5 | 0.85 | 11.31 | 244 | rtx4090 | 0.631 | 16 | 63% | RELEASE 1.4d ago |
| 23 | 2 | DSperse | 55.3 | 0.85 | 8.26 | 117 | rtx4090 | 0.826 | 13 | 83% | RELEASE 2.9d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,174 | 7,174 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.6d ago |
| 25 | 124 | Swarm | 53.9 | 0.85 | 219 | 666 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.79 | a4000 | 1036.6130990550175 |
| 104 | Masx.ai | -1.05 | rtx4090 | 8.386649026834018 |
| 13 | Data Universe | -2.85 | rtx4090 | 7.651931064751985 |
| 88 | Investing | -5.69 | rtx4090 | 481.41509056357097 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 132.28249627088616 |
| 8 | Vanta | -7.39 | rtx4090 | 3389.449909061619 |
| 19 | blockmachine | -0.87 | rtx4090 | 316.75837728225457 |
| 18 | Zeus | -3.27 | rtx4090 | 1434.8707015729522 |
| 45 | AlphaRidge.ai | -3.37 | rtx4090 | 29.962088929472632 |
| 75 | Hippius | -4.45 | rtx4090 | 5.604079510860947 |
| 123 | MANTIS | -6.23 | rtx4090 | 74.58363026583206 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07781341320101846 |
| 105 | Beam | -4.02 | rtx4090 | 200.69478296853427 |
| 84 | ansuz | -8.15 | rtx4090 | 503.6370677722841 |
| 34 | BitMind | -18.88 | a100-80 | 299.04283666779895 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn9, sn10, sn12, sn14, sn16, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.87 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 16.7 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.61 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.23 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.0 | 35.0 | 15.0 | 9.8 | 1.0 |
| 1 | 26.46 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.43 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 25.09 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.76 | 35.0 | 11.25 | 9.72 | 1.0 |
| 41 | 9.2 | 35.0 | 15.0 | 9.26 | 1.0 |
| 26 | 12.45 | 35.0 | 11.25 | 9.69 | 1.0 |
| 15 | 9.38 | 35.0 | 15.0 | 8.54 | 1.0 |
| 38 | 21.25 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 7.08 | 35.0 | 15.0 | 8.63 | 1.0 |
| 80 | 19.33 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.49 | 35.0 | 11.25 | 9.1 | 0.85 |
| 28 | 13.7 | 35.0 | 11.25 | 9.78 | 0.85 |
| 6 | 13.55 | 21.0 | 15.0 | 9.54 | 1.0 |
| 85 | 24.85 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.38 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.92 | 35.0 | 11.25 | 9.09 | 0.85 |
| 2 | 8.79 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.07 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.3 | 21.0 | 11.25 | 9.84 | 0.85 |
