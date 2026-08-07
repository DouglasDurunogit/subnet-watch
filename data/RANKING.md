# RANKING - generated 2026-08-07T00:33:22Z, block 8788846

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
| 1 | 107 | Minos | 78.2 | 1.0 | 115 | 31,241 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 2.8d ago |
| 2 | 76 | Phylax | 77.5 | 1.0 | 83.20 | 418 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 4.3d ago |
| 3 | 60 | Bitsec.ai | 74.8 | 0.85 | 1,207 | 1,207 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 3.4d ago |
| 4 | 67 | Harnyx | 71.7 | 1.0 | 19.84 | 933 | cpu-small | 0.000 | 126 | 25% | SCORING_COMMIT 0.5d ago |
| 5 | 91 | cascade | 70.0 | 0.85 | 743 | 2,999 | rtx4090 | 0.000 | 5 | 52% | RELEASE 1.8d ago |
| 6 | 62 | Ridges | 69.0 | 0.85 | 546 | 1,975 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.1d ago |
| 7 | 96 | Verathos | 68.1 | 1.0 | 20.79 | 283 | rtx4090 | 0.446 | 55 | 45% | RELEASE 0.0d ago |
| 8 | 26 | Perturb | 68.0 | 1.0 | 20.05 | 37.98 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 0.4d ago |
| 9 | 41 | Almanac | 67.5 | 1.0 | 7.28 | 43.33 | cpu-small | 0.820 | 53 | 82% | SCORING_COMMIT 0.0d ago |
| 10 | 15 | ORO | 67.3 | 1.0 | 8.82 | 17.12 | cpu-small | 0.000 | 83 | 93% | RELEASE 0.6d ago |
| 11 | 124 | Swarm | 65.6 | 0.85 | 209 | 600 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 5.4d ago |
| 12 | 21 | AdTAO | 65.6 | 1.0 | 4.75 | 21.97 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.0d ago |
| 13 | 74 | Gittensor | 65.2 | 0.85 | 180 | 433 | rtx4090 | 0.000 | 9 | 20% | RELEASE 0.0d ago |
| 14 | 28 | gm | 65.0 | 0.85 | 169 | 1,682 | rtx4090 | 0.254 | 19 | 25% | RELEASE 3.4d ago |
| 15 | 98 | NeverPlayAlone | 64.1 | 0.85 | 1,693 | 1,693 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 7d ago |
| 16 | 80 | OpenRoboto | 63.4 | 0.85 | 104 | 384 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 6.7d ago |
| 17 | 61 | RedTeam | 62.4 | 0.85 | 75.72 | 174 | rtx4090 | 0.000 | 38 | 6% | RELEASE 1.5d ago |
| 18 | 101 | Tag101 | 59.7 | 1.0 | 0.08 | 0.74 | cpu-small | 0.902 | 245 | 90% | SCORING_COMMIT 6.3d ago |
| 19 | 51 | lium.io | 57.8 | 0.85 | 25.87 | 2,001 | rtx4090 | 0.000 | 44 | 68% | SCORING_COMMIT 2.7d ago |
| 20 | 85 | Vidaio | 57.2 | 0.85 | 569 | 622 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 10d ago |
| 21 | 102 | ConnitoAI | 57.1 | 0.85 | 14.71 | 1,715 | rtx4090 | 0.251 | 9 | 32% | RELEASE 6.1d ago |
| 22 | 56 | Gradients | 56.4 | 0.85 | 444 | 936 | rtx4090 | 0.699 | 7 | 70% | SCORING_COMMIT 9d ago |
| 23 | 9 | iota | 55.8 | 0.6 | 10,984 | 10,984 | rtx4090 | 0.357 | 3 | 56% | RELEASE 6.3d ago |
| 24 | 120 | Affine | 54.5 | 0.6 | 6,423 | 6,423 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.5d ago |
| 25 | 38 | ChronoLLM | 53.7 | 0.85 | 211 | 3,544 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.01 | a4000 | 993.7695858047163 |
| 104 | Masx.ai | -1.71 | rtx4090 | 7.097756786082726 |
| 13 | Data Universe | -3.27 | rtx4090 | 6.378049552018804 |
| 88 | Investing | -5.73 | rtx4090 | 434.9844584821645 |
| 114 | SOMA | -8.12 | rtx4090 | 4198.149458398082 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 152.39480988547228 |
| 8 | Vanta | -7.45 | rtx4090 | 3131.572098893729 |
| 32 | ItsAI | -0.03 | rtx4090 | 11.518235729176517 |
| 19 | blockmachine | -1.94 | rtx4090 | 162.38013623171705 |
| 18 | Zeus | -3.25 | rtx4090 | 1855.2261944229983 |
| 45 | AlphaRidge.ai | -3.69 | rtx4090 | 21.53804216577655 |
| 22 | Desearch | -4.16 | rtx4090 | 65.78483272045452 |
| 75 | Hippius | -4.54 | rtx4090 | 5.478085536301062 |
| 123 | MANTIS | -6.22 | rtx4090 | 79.03872567847851 |
| 63 | Enigma | -8.15 | rtx4090 | 0.07177367216662286 |
| 84 | ansuz | -8.15 | rtx4090 | 466.065221927845 |
| 34 | BitMind | -19.24 | a100-80 | 279.5384228224768 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn73, sn87, sn92, sn94, sn95, sn100, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.78 | 35.0 | 15.0 | 9.45 | 1.0 |
| 76 | 17.51 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.03 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.0 | 35.0 | 15.0 | 9.74 | 1.0 |
| 91 | 26.12 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 24.9 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.17 | 35.0 | 11.25 | 9.69 | 1.0 |
| 26 | 12.03 | 35.0 | 11.25 | 9.68 | 1.0 |
| 41 | 8.35 | 35.0 | 15.0 | 9.12 | 1.0 |
| 15 | 9.02 | 35.0 | 15.0 | 8.27 | 1.0 |
| 124 | 21.12 | 35.0 | 11.25 | 9.85 | 0.85 |
| 21 | 6.91 | 35.0 | 15.0 | 8.66 | 1.0 |
| 74 | 20.52 | 35.0 | 11.25 | 9.95 | 0.85 |
| 28 | 20.29 | 35.0 | 11.25 | 9.96 | 0.85 |
| 98 | 29.37 | 21.0 | 15.0 | 10.0 | 0.85 |
| 80 | 18.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.14 | 35.0 | 11.25 | 10.0 | 0.85 |
| 101 | 0.32 | 35.0 | 15.0 | 9.37 | 1.0 |
| 51 | 13.0 | 35.0 | 11.25 | 8.77 | 0.85 |
| 85 | 25.06 | 21.0 | 11.25 | 10.0 | 0.85 |
| 102 | 10.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.09 | 21.0 | 11.25 | 10.0 | 0.85 |
| 9 | 36.75 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.63 | 35.0 | 11.25 | 9.99 | 0.6 |
| 38 | 21.16 | 21.0 | 11.25 | 9.78 | 0.85 |
