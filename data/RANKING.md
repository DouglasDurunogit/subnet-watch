# RANKING - generated 2026-08-07T16:07:52Z, block 8793518

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
| 1 | 11 | TrajectoryRL | 79.9 | 0.85 | 5,409 | 5,409 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 5.2d ago |
| 2 | 107 | Minos | 78.5 | 1.0 | 121 | 31,336 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 3.5d ago |
| 3 | 76 | Phylax | 77.1 | 1.0 | 75.79 | 274 | cpu-small | 0.000 | 10 | 31% | SCORING_COMMIT 5.0d ago |
| 4 | 98 | NeverPlayAlone | 76.0 | 0.85 | 1,703 | 1,703 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 0.4d ago |
| 5 | 60 | Bitsec.ai | 75.0 | 0.85 | 1,290 | 1,290 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 4.0d ago |
| 6 | 114 | SOMA | 72.7 | 0.85 | 1,662 | 4,336 | rtx4090 | 0.000 | 3 | 65% | SCORING_COMMIT 0.3d ago |
| 7 | 67 | Harnyx | 72.0 | 1.0 | 21.07 | 763 | cpu-small | 0.012 | 135 | 20% | SCORING_COMMIT 0.5d ago |
| 8 | 62 | Ridges | 69.1 | 0.85 | 566 | 2,045 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.8d ago |
| 9 | 102 | ConnitoAI | 69.0 | 0.85 | 553 | 1,741 | rtx4090 | 0.250 | 7 | 32% | RELEASE 6.7d ago |
| 10 | 91 | cascade | 68.8 | 0.85 | 515 | 1,462 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.5d ago |
| 11 | 96 | Verathos | 68.4 | 1.0 | 22.45 | 424 | rtx4090 | 0.428 | 47 | 43% | RELEASE 0.6d ago |
| 12 | 26 | Perturb | 68.2 | 1.0 | 21.45 | 39.28 | rtx3060 | 0.508 | 11 | 51% | SCORING_COMMIT 1.1d ago |
| 13 | 15 | ORO | 68.2 | 1.0 | 11.37 | 10,257 | cpu-small | 0.000 | 74 | 93% | RELEASE 1.2d ago |
| 14 | 100 | BASE | 67.9 | 0.85 | 397 | 1,633 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.0d ago |
| 15 | 41 | Almanac | 67.6 | 1.0 | 7.50 | 44.75 | cpu-small | 0.799 | 62 | 80% | SCORING_COMMIT 0.6d ago |
| 16 | 124 | Swarm | 65.6 | 0.85 | 208 | 597 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 6.1d ago |
| 17 | 21 | AdTAO | 65.5 | 1.0 | 4.73 | 21.88 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.0d ago |
| 18 | 74 | Gittensor | 65.3 | 0.85 | 183 | 386 | rtx4090 | 0.000 | 9 | 18% | RELEASE 0.0d ago |
| 19 | 61 | RedTeam | 62.2 | 0.85 | 71.38 | 189 | rtx4090 | 0.000 | 38 | 6% | RELEASE 2.2d ago |
| 20 | 101 | Tag101 | 58.2 | 1.0 | 0.05 | 0.76 | cpu-small | 0.902 | 242 | 90% | SCORING_COMMIT 7.0d ago |
| 21 | 51 | lium.io | 58.1 | 0.85 | 27.43 | 2,835 | rtx4090 | 0.000 | 41 | 70% | SCORING_COMMIT 3.4d ago |
| 22 | 28 | gm | 57.2 | 0.85 | 16.99 | 4,272 | rtx4090 | 0.249 | 19 | 49% | RELEASE 4.0d ago |
| 23 | 56 | Gradients | 56.4 | 0.85 | 452 | 953 | rtx4090 | 0.701 | 7 | 70% | SCORING_COMMIT 10d ago |
| 24 | 2 | DSperse | 56.4 | 0.85 | 11.88 | 144 | rtx4090 | 0.826 | 8 | 83% | RELEASE 1.5d ago |
| 25 | 9 | iota | 55.0 | 0.6 | 7,711 | 7,711 | rtx4090 | 0.580 | 3 | 58% | RELEASE 7.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.77 | a4000 | 1089.39991151119 |
| 104 | Masx.ai | -1.43 | rtx4090 | 7.78821112804197 |
| 13 | Data Universe | -3.24 | rtx4090 | 6.198713147702518 |
| 88 | Investing | -6.80 | rtx4090 | 643.7284194273498 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 142.8276518641519 |
| 8 | Vanta | -7.44 | rtx4090 | 3177.3810821018656 |
| 32 | ItsAI | -0.33 | rtx4090 | 9.456116034610568 |
| 19 | blockmachine | -1.16 | rtx4090 | 231.95173308160844 |
| 22 | Desearch | -2.96 | rtx4090 | 98.02285824930975 |
| 45 | AlphaRidge.ai | -4.24 | rtx4090 | 20.937219050726874 |
| 75 | Hippius | -4.62 | rtx4090 | 5.240854061300432 |
| 18 | Zeus | -4.76 | rtx4090 | 1302.935128155231 |
| 123 | MANTIS | -6.28 | rtx4090 | 76.9124749942984 |
| 63 | Enigma | -8.15 | rtx4090 | 4830.056682209295 |
| 84 | ansuz | -8.15 | rtx4090 | 479.6102859786925 |
| 34 | BitMind | -18.20 | a100-80 | 281.56018806808834 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn121, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.95 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.98 | 35.0 | 15.0 | 9.47 | 1.0 |
| 76 | 17.15 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.39 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.29 | 35.0 | 15.0 | 10.0 | 0.85 |
| 114 | 29.3 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.22 | 35.0 | 15.0 | 9.8 | 1.0 |
| 62 | 25.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 24.95 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.67 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 12.46 | 35.0 | 11.25 | 9.71 | 1.0 |
| 26 | 12.29 | 35.0 | 11.25 | 9.7 | 1.0 |
| 15 | 9.94 | 35.0 | 15.0 | 8.26 | 1.0 |
| 100 | 23.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 8.45 | 35.0 | 15.0 | 9.14 | 1.0 |
| 124 | 21.1 | 35.0 | 11.25 | 9.84 | 0.85 |
| 21 | 6.9 | 35.0 | 15.0 | 8.64 | 1.0 |
| 74 | 20.59 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 16.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 101 | 0.21 | 35.0 | 15.0 | 8.0 | 1.0 |
| 51 | 13.22 | 35.0 | 11.25 | 8.82 | 0.85 |
| 28 | 11.42 | 35.0 | 11.25 | 9.62 | 0.85 |
| 56 | 24.16 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 10.1 | 35.0 | 11.25 | 10.0 | 0.85 |
| 9 | 35.35 | 35.0 | 11.25 | 10.0 | 0.6 |
