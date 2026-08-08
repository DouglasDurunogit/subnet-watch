# RANKING - generated 2026-08-08T23:54:17Z, block 8803050

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
| 1 | 11 | TrajectoryRL | 79.6 | 0.85 | 5,014 | 5,014 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.5d ago |
| 2 | 107 | Minos | 78.3 | 1.0 | 118 | 34,947 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 4.8d ago |
| 3 | 76 | Phylax | 76.7 | 1.0 | 66.84 | 201 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.1d ago |
| 4 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,783 | 1,783 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 1.7d ago |
| 5 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,249 | 1,249 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.2d ago |
| 6 | 67 | Harnyx | 70.9 | 1.0 | 15.52 | 875 | cpu-small | 0.057 | 143 | 22% | SCORING_COMMIT 1.8d ago |
| 7 | 1 | Apex | 70.3 | 0.85 | 809 | 1,671 | rtx4090 | 0.415 | 4 | 41% | RELEASE 1.1d ago |
| 8 | 100 | BASE | 70.3 | 0.85 | 806 | 1,621 | rtx4090 | 0.000 | 3 | 50% | SCORING_COMMIT 0.1d ago |
| 9 | 91 | cascade | 70.3 | 0.85 | 805 | 2,755 | rtx4090 | 0.000 | 5 | 48% | RELEASE 3.8d ago |
| 10 | 62 | Ridges | 69.1 | 0.85 | 565 | 2,045 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.1d ago |
| 11 | 96 | Verathos | 68.9 | 1.0 | 25.09 | 178 | rtx4090 | 0.411 | 71 | 41% | RELEASE 0.3d ago |
| 12 | 26 | Perturb | 68.4 | 1.0 | 22.25 | 41.37 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 2.4d ago |
| 13 | 41 | Almanac | 68.3 | 1.0 | 8.95 | 46.12 | cpu-small | 0.761 | 66 | 76% | SCORING_COMMIT 2.0d ago |
| 14 | 15 | ORO | 67.6 | 1.0 | 9.37 | 19.73 | cpu-small | 0.000 | 70 | 94% | RELEASE 2.6d ago |
| 15 | 21 | AdTAO | 65.7 | 1.0 | 4.93 | 22.66 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.4d ago |
| 16 | 38 | ChronoLLM | 65.6 | 0.85 | 214 | 3,597 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.6d ago |
| 17 | 80 | OpenRoboto | 63.6 | 0.85 | 110 | 404 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 0.8d ago |
| 18 | 61 | RedTeam | 62.3 | 0.85 | 74.18 | 213 | rtx4090 | 0.000 | 42 | 6% | RELEASE 1.0d ago |
| 19 | 28 | gm | 61.4 | 0.85 | 57.97 | 4,390 | rtx4090 | 0.000 | 25 | 47% | RELEASE 1.1d ago |
| 20 | 51 | lium.io | 58.6 | 0.85 | 32.80 | 2,859 | rtx4090 | 0.000 | 47 | 69% | SCORING_COMMIT 1.1d ago |
| 21 | 102 | ConnitoAI | 57.1 | 0.85 | 542 | 1,397 | rtx4090 | 0.250 | 7 | 28% | RELEASE 8d ago |
| 22 | 85 | Vidaio | 57.0 | 0.85 | 537 | 537 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 12d ago |
| 23 | 56 | Gradients | 56.6 | 0.85 | 472 | 995 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 24 | 74 | Gittensor | 55.4 | 0.85 | 11.16 | 241 | rtx4090 | 0.631 | 16 | 63% | RELEASE 1.3d ago |
| 25 | 120 | Affine | 54.8 | 0.6 | 7,100 | 7,100 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.5d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.87 | a4000 | 1045.3968688462762 |
| 104 | Masx.ai | -1.63 | rtx4090 | 8.726839998227625 |
| 13 | Data Universe | -2.91 | rtx4090 | 7.2763836359950735 |
| 88 | Investing | -6.13 | rtx4090 | 392.7227899490775 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 131.0057651009252 |
| 8 | Vanta | -7.40 | rtx4090 | 3459.2942692419692 |
| 19 | blockmachine | -0.91 | rtx4090 | 223.32802107018694 |
| 18 | Zeus | -3.31 | rtx4090 | 1422.8472688583029 |
| 45 | AlphaRidge.ai | -4.08 | rtx4090 | 17.088500395484832 |
| 75 | Hippius | -4.54 | rtx4090 | 5.470916197345055 |
| 123 | MANTIS | -6.25 | rtx4090 | 73.85524102555489 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0768348143727566 |
| 105 | Beam | -3.83 | rtx4090 | 206.78562992911338 |
| 84 | ansuz | -8.15 | rtx4090 | 507.91977796922976 |
| 34 | BitMind | -18.50 | a100-80 | 295.3995215055381 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.65 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.89 | 35.0 | 15.0 | 9.43 | 1.0 |
| 76 | 16.66 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.57 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.17 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.08 | 35.0 | 15.0 | 9.79 | 1.0 |
| 1 | 26.45 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 26.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.43 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 25.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.88 | 35.0 | 11.25 | 9.73 | 1.0 |
| 26 | 12.43 | 35.0 | 11.25 | 9.7 | 1.0 |
| 41 | 9.07 | 35.0 | 15.0 | 9.24 | 1.0 |
| 15 | 9.24 | 35.0 | 15.0 | 8.4 | 1.0 |
| 21 | 7.03 | 35.0 | 15.0 | 8.63 | 1.0 |
| 38 | 21.22 | 35.0 | 11.25 | 9.77 | 0.85 |
| 80 | 18.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.1 | 35.0 | 11.25 | 9.88 | 0.85 |
| 51 | 13.91 | 35.0 | 11.25 | 8.78 | 0.85 |
| 102 | 24.87 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.84 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.33 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.87 | 35.0 | 11.25 | 9.09 | 0.85 |
| 120 | 35.03 | 35.0 | 11.25 | 9.99 | 0.6 |
