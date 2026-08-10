# RANKING - generated 2026-08-10T08:13:20Z, block 8812745

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
| 1 | 107 | Minos | 78.2 | 1.0 | 115 | 32,263 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 6.2d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 67.51 | 203 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.4d ago |
| 3 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,779 | 1,779 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 3.1d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,224 | 1,224 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 2.5d ago |
| 5 | 96 | Verathos | 71.5 | 1.0 | 48.64 | 366 | rtx4090 | 0.422 | 36 | 42% | RELEASE 0.0d ago |
| 6 | 67 | Harnyx | 71.2 | 1.0 | 17.30 | 751 | cpu-small | 0.008 | 129 | 19% | SCORING_COMMIT 0.9d ago |
| 7 | 91 | cascade | 70.3 | 0.85 | 810 | 2,774 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.1d ago |
| 8 | 1 | Apex | 69.8 | 0.85 | 702 | 1,614 | rtx4090 | 0.508 | 4 | 51% | RELEASE 2.5d ago |
| 9 | 41 | Almanac | 69.3 | 1.0 | 11.19 | 34.27 | cpu-small | 0.696 | 69 | 70% | SCORING_COMMIT 3.3d ago |
| 10 | 26 | Perturb | 68.3 | 1.0 | 21.71 | 40.19 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 3.7d ago |
| 11 | 62 | Ridges | 68.2 | 0.85 | 428 | 1,984 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.4d ago |
| 12 | 15 | ORO | 67.8 | 1.0 | 9.88 | 20.75 | cpu-small | 0.000 | 72 | 94% | RELEASE 3.9d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 216 | 3,630 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.9d ago |
| 14 | 28 | gm | 65.5 | 0.85 | 196 | 4,412 | rtx4090 | 0.154 | 24 | 43% | RELEASE 2.5d ago |
| 15 | 21 | AdTAO | 65.4 | 1.0 | 4.69 | 21.83 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.7d ago |
| 16 | 100 | BASE | 63.2 | 0.85 | 97.47 | 837 | rtx4090 | 0.000 | 8 | 51% | SCORING_COMMIT 1.5d ago |
| 17 | 61 | RedTeam | 62.8 | 0.85 | 86.55 | 361 | rtx4090 | 0.000 | 45 | 8% | RELEASE 0.0d ago |
| 18 | 102 | ConnitoAI | 59.9 | 0.85 | 1,280 | 1,280 | rtx4090 | 0.250 | 4 | 25% | RELEASE 9d ago |
| 19 | 51 | lium.io | 59.0 | 0.85 | 34.45 | 3,252 | rtx4090 | 0.000 | 50 | 54% | SCORING_COMMIT 2.5d ago |
| 20 | 6 | Numinous | 58.0 | 1.0 | 22.95 | 450 | cpu-small | 0.000 | 18 | 26% | README_TASK_DIFF 12d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 473 | 996 | rtx4090 | 0.707 | 7 | 71% | SCORING_COMMIT 12d ago |
| 22 | 2 | DSperse | 56.5 | 0.85 | 12.13 | 112 | rtx4090 | 0.827 | 15 | 83% | RELEASE 4.1d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,207 | 7,207 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.8d ago |
| 24 | 124 | Swarm | 53.9 | 0.85 | 219 | 672 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 9d ago |
| 25 | 85 | Vidaio | 52.0 | 0.85 | 121 | 554 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 13d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.73 | a4000 | 1015.5587267670905 |
| 104 | Masx.ai | -1.41 | rtx4090 | 8.477794697668907 |
| 13 | Data Universe | -3.37 | rtx4090 | 6.403804483357391 |
| 88 | Investing | -4.30 | rtx4090 | 601.507995856019 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 215.13906851652374 |
| 8 | Vanta | -7.40 | rtx4090 | 3497.9428329221964 |
| 19 | blockmachine | -1.10 | rtx4090 | 387.304899610471 |
| 18 | Zeus | -3.35 | rtx4090 | 1426.680841342767 |
| 75 | Hippius | -4.42 | rtx4090 | 5.829785680368769 |
| 45 | AlphaRidge.ai | -4.55 | rtx4090 | 8.479615911856692 |
| 123 | MANTIS | -6.18 | rtx4090 | 73.99549979418681 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07505058340542857 |
| 105 | Beam | -4.51 | rtx4090 | 198.26543179650196 |
| 84 | ansuz | -8.15 | rtx4090 | 508.7361751769757 |
| 34 | BitMind | -18.60 | a100-80 | 295.9165151144559 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.78 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 16.7 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.56 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.09 | 35.0 | 15.0 | 10.0 | 0.85 |
| 96 | 15.42 | 35.0 | 11.25 | 9.86 | 1.0 |
| 67 | 11.48 | 35.0 | 15.0 | 9.75 | 1.0 |
| 91 | 26.46 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 25.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.88 | 35.0 | 15.0 | 9.39 | 1.0 |
| 26 | 12.33 | 35.0 | 11.25 | 9.69 | 1.0 |
| 62 | 23.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.43 | 35.0 | 15.0 | 8.4 | 1.0 |
| 38 | 21.25 | 35.0 | 11.25 | 9.77 | 0.85 |
| 28 | 20.88 | 35.0 | 11.25 | 9.97 | 0.85 |
| 21 | 6.87 | 35.0 | 15.0 | 8.55 | 1.0 |
| 100 | 18.13 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.66 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 28.26 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.09 | 35.0 | 11.25 | 9.02 | 0.85 |
| 6 | 12.55 | 21.0 | 15.0 | 9.41 | 1.0 |
| 56 | 24.33 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 10.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.09 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.31 | 21.0 | 11.25 | 9.85 | 0.85 |
| 85 | 18.98 | 21.0 | 11.25 | 10.0 | 0.85 |
