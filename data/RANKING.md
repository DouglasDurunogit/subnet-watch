# RANKING - generated 2026-08-07T08:20:10Z, block 8791180

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
| 1 | 107 | Minos | 78.3 | 1.0 | 116 | 30,622 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 3.2d ago |
| 2 | 76 | Phylax | 76.8 | 1.0 | 69.11 | 250 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 4.7d ago |
| 3 | 98 | NeverPlayAlone | 75.9 | 0.85 | 1,679 | 1,679 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 0.1d ago |
| 4 | 102 | ConnitoAI | 72.1 | 0.85 | 1,372 | 1,373 | rtx4090 | 0.250 | 4 | 25% | RELEASE 6.4d ago |
| 5 | 67 | Harnyx | 72.0 | 1.0 | 21.21 | 767 | cpu-small | 0.040 | 126 | 20% | SCORING_COMMIT 0.2d ago |
| 6 | 96 | Verathos | 69.7 | 1.0 | 30.90 | 746 | rtx4090 | 0.438 | 39 | 44% | RELEASE 0.3d ago |
| 7 | 62 | Ridges | 69.0 | 0.85 | 547 | 1,978 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.4d ago |
| 8 | 91 | cascade | 68.8 | 0.85 | 520 | 1,475 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.2d ago |
| 9 | 15 | ORO | 68.4 | 1.0 | 11.24 | 18.48 | cpu-small | 0.000 | 73 | 93% | RELEASE 0.9d ago |
| 10 | 26 | Perturb | 68.2 | 1.0 | 21.01 | 38.44 | rtx3060 | 0.508 | 11 | 51% | SCORING_COMMIT 0.7d ago |
| 11 | 41 | Almanac | 67.6 | 1.0 | 7.44 | 44.20 | cpu-small | 0.797 | 62 | 80% | SCORING_COMMIT 0.3d ago |
| 12 | 124 | Swarm | 65.6 | 0.85 | 209 | 600 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 5.8d ago |
| 13 | 21 | AdTAO | 65.5 | 1.0 | 4.66 | 21.61 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.3d ago |
| 14 | 74 | Gittensor | 65.2 | 0.85 | 178 | 487 | rtx4090 | 0.000 | 9 | 23% | RELEASE 0.3d ago |
| 15 | 61 | RedTeam | 62.7 | 0.85 | 83.67 | 191 | rtx4090 | 0.000 | 38 | 6% | RELEASE 1.8d ago |
| 16 | 28 | gm | 58.7 | 0.85 | 26.21 | 2,378 | rtx4090 | 0.310 | 19 | 31% | RELEASE 3.7d ago |
| 17 | 85 | Vidaio | 57.6 | 0.85 | 641 | 641 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 10d ago |
| 18 | 51 | lium.io | 57.3 | 0.85 | 23.24 | 2,721 | rtx4090 | 0.000 | 41 | 68% | SCORING_COMMIT 3.0d ago |
| 19 | 2 | DSperse | 56.7 | 0.85 | 13.24 | 141 | rtx4090 | 0.827 | 8 | 83% | RELEASE 1.2d ago |
| 20 | 56 | Gradients | 56.4 | 0.85 | 446 | 941 | rtx4090 | 0.700 | 7 | 70% | SCORING_COMMIT 9d ago |
| 21 | 9 | iota | 55.8 | 0.6 | 11,003 | 11,003 | rtx4090 | 0.380 | 3 | 56% | RELEASE 6.6d ago |
| 22 | 120 | Affine | 54.6 | 0.6 | 6,501 | 6,501 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.8d ago |
| 23 | 38 | ChronoLLM | 53.8 | 0.85 | 215 | 3,616 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 8d ago |
| 24 | 97 | Albedo | 52.7 | 0.6 | 2,937 | 2,937 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.3d ago |
| 25 | 100 | BASE | 52.2 | 0.6 | 2,430 | 2,430 | rtx4090 | 0.269 | 2 | 73% | RELEASE 0.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 101 | Tag101 | -0.04 | cpu-small | 1.8068924124698367 |
| 54 | Yanez MIID | -4.03 | a4000 | 1021.9308561550268 |
| 104 | Masx.ai | -2.70 | rtx4090 | 10.01937998253224 |
| 13 | Data Universe | -3.34 | rtx4090 | 6.521550227323436 |
| 88 | Investing | -7.13 | rtx4090 | 638.8820549787706 |
| 114 | SOMA | -8.12 | rtx4090 | 1681.585734076892 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 154.58920857201397 |
| 8 | Vanta | -7.45 | rtx4090 | 3135.5330460975556 |
| 32 | ItsAI | -0.35 | rtx4090 | 10.234816185314664 |
| 22 | Desearch | -1.24 | rtx4090 | 68.2961447358496 |
| 19 | blockmachine | -1.72 | rtx4090 | 347.18510781361164 |
| 45 | AlphaRidge.ai | -2.47 | rtx4090 | 23.358775292201017 |
| 18 | Zeus | -3.80 | rtx4090 | 1660.4812160030826 |
| 75 | Hippius | -4.60 | rtx4090 | 5.38791560986683 |
| 123 | MANTIS | -6.15 | rtx4090 | 77.3511275719283 |
| 63 | Enigma | -8.15 | rtx4090 | 0.07188329476607538 |
| 84 | ansuz | -8.15 | rtx4090 | 473.98470243108267 |
| 34 | BitMind | -19.73 | a100-80 | 279.2101994820375 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn121, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.8 | 35.0 | 15.0 | 9.45 | 1.0 |
| 76 | 16.79 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.34 | 35.0 | 15.0 | 10.0 | 0.85 |
| 102 | 28.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.25 | 35.0 | 15.0 | 9.72 | 1.0 |
| 96 | 13.68 | 35.0 | 11.25 | 9.79 | 1.0 |
| 62 | 24.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.71 | 35.0 | 11.25 | 9.98 | 0.85 |
| 15 | 9.9 | 35.0 | 15.0 | 8.46 | 1.0 |
| 26 | 12.21 | 35.0 | 11.25 | 9.7 | 1.0 |
| 41 | 8.43 | 35.0 | 15.0 | 9.14 | 1.0 |
| 124 | 21.12 | 35.0 | 11.25 | 9.85 | 0.85 |
| 21 | 6.85 | 35.0 | 15.0 | 8.63 | 1.0 |
| 74 | 20.48 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 17.53 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.05 | 35.0 | 11.25 | 9.76 | 0.85 |
| 85 | 25.53 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.59 | 35.0 | 11.25 | 8.63 | 0.85 |
| 2 | 10.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.11 | 21.0 | 11.25 | 10.0 | 0.85 |
| 9 | 36.76 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.68 | 35.0 | 11.25 | 9.99 | 0.6 |
| 38 | 21.24 | 21.0 | 11.25 | 9.78 | 0.85 |
| 97 | 31.54 | 35.0 | 11.25 | 9.99 | 0.6 |
| 100 | 30.79 | 35.0 | 11.25 | 10.0 | 0.6 |
