# RANKING - generated 2026-08-13T07:51:50Z, block 8834230

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
| 1 | 107 | Minos | 77.8 | 1.0 | 106 | 30,446 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 2.7d ago |
| 2 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,745 | 1,745 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.0d ago |
| 3 | 76 | Phylax | 74.7 | 1.0 | 40.21 | 133 | cpu-small | 0.000 | 10 | 36% | SCORING_COMMIT 4.4d ago |
| 4 | 67 | Harnyx | 71.2 | 1.0 | 17.02 | 700 | cpu-small | 0.024 | 146 | 19% | SCORING_COMMIT 0.8d ago |
| 5 | 54 | Yanez | 69.9 | 0.85 | 725 | 978 | a4000 | 0.464 | 3 | 46% | SCORING_COMMIT 0.5d ago |
| 6 | 91 | cascade | 69.0 | 0.85 | 554 | 1,274 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 2.1d ago |
| 7 | 62 | Ridges | 69.0 | 0.85 | 542 | 1,962 | rtx4090 | 0.133 | 7 | 35% | SCORING_COMMIT 1.4d ago |
| 8 | 56 | Gradients | 68.9 | 0.85 | 530 | 977 | rtx4090 | 0.650 | 7 | 65% | SCORING_COMMIT 0.7d ago |
| 9 | 41 | Almanac | 68.9 | 1.0 | 10.25 | 30.06 | cpu-small | 0.723 | 68 | 72% | SCORING_COMMIT 0.4d ago |
| 10 | 96 | Verathos | 68.7 | 1.0 | 24.04 | 334 | rtx4090 | 0.409 | 63 | 41% | RELEASE 0.7d ago |
| 11 | 100 | BASE | 68.3 | 0.85 | 440 | 440 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.9d ago |
| 12 | 15 | ORO | 68.1 | 1.0 | 11.16 | 12,211 | cpu-small | 0.000 | 72 | 94% | RELEASE 6.9d ago |
| 13 | 26 | Perturb | 67.8 | 1.0 | 19.32 | 36.67 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 6.7d ago |
| 14 | 21 | AdTAO | 67.5 | 1.0 | 7.44 | 33.42 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 1.8d ago |
| 15 | 124 | Swarm | 65.8 | 0.85 | 222 | 463 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 1.7d ago |
| 16 | 80 | OpenRoboto | 64.8 | 0.85 | 156 | 567 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 5.1d ago |
| 17 | 85 | Vidaio | 64.3 | 0.85 | 136 | 351 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 0.9d ago |
| 18 | 38 | ChronoLLM | 63.1 | 0.85 | 107 | 1,556 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 4.9d ago |
| 19 | 51 | lium.io | 62.4 | 0.85 | 84.66 | 2,098 | rtx4090 | 0.000 | 47 | 69% | RELEASE 0.2d ago |
| 20 | 28 | gm | 61.3 | 0.85 | 55.65 | 2,748 | rtx4090 | 0.091 | 29 | 28% | RELEASE 0.7d ago |
| 21 | 102 | ConnitoAI | 60.1 | 0.85 | 1,326 | 1,772 | rtx4090 | 0.250 | 5 | 29% | RELEASE 12d ago |
| 22 | 61 | RedTeam | 58.3 | 0.85 | 21.86 | 1,625 | rtx4090 | 0.000 | 59 | 35% | RELEASE 2.0d ago |
| 23 | 74 | Gittensor | 57.8 | 0.85 | 20.88 | 218 | rtx4090 | 0.639 | 13 | 64% | RELEASE 1.6d ago |
| 24 | 120 | Affine | 54.7 | 0.6 | 7,024 | 7,024 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.7d ago |
| 25 | 6 | Numinous | 54.0 | 1.0 | 9.82 | 519 | cpu-small | 0.000 | 19 | 29% | README_TASK_DIFF 15d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 104 | Masx.ai | -0.18 | rtx4090 | 9.141195269798473 |
| 2 | DSperse | -3.58 | rtx4090 | 102.70555105792042 |
| 75 | Hippius | -7.35 | rtx4090 | 11229.33136686722 |
| 114 | SOMA | -8.12 | rtx4090 | 671.8023668191759 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 142.6655042138979 |
| 13 | Data Universe | -3.15 | rtx4090 | 5.80425823366506 |
| 88 | Investing | -5.13 | rtx4090 | 708.4083453231245 |
| 8 | Vanta | -7.95 | rtx4090 | 3265.1254293108 |
| 43 | Graphite | -0.25 | cpu-small | 37.644915729303904 |
| 19 | blockmachine | -2.59 | rtx4090 | 880.8080949593781 |
| 18 | Zeus | -5.10 | rtx4090 | 1313.362496657349 |
| 45 | AlphaRidge.ai | -5.60 | rtx4090 | 12.471559265827963 |
| 123 | MANTIS | -6.10 | rtx4090 | 80.64104489265878 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07656148040729116 |
| 105 | Beam | -2.10 | rtx4090 | 83.75437516750985 |
| 84 | ansuz | -8.15 | rtx4090 | 471.8421507146354 |
| 34 | BitMind | -19.78 | a100-80 | 290.63161362627443 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn118, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.44 | 35.0 | 15.0 | 9.38 | 1.0 |
| 98 | 29.49 | 35.0 | 15.0 | 10.0 | 0.85 |
| 76 | 14.69 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 11.42 | 35.0 | 15.0 | 9.75 | 1.0 |
| 54 | 26.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.96 | 35.0 | 11.25 | 9.98 | 0.85 |
| 62 | 24.87 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.79 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.56 | 35.0 | 15.0 | 9.35 | 1.0 |
| 96 | 12.72 | 35.0 | 11.25 | 9.72 | 1.0 |
| 100 | 24.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.87 | 35.0 | 15.0 | 8.24 | 1.0 |
| 26 | 11.9 | 35.0 | 11.25 | 9.66 | 1.0 |
| 21 | 8.42 | 35.0 | 15.0 | 9.1 | 1.0 |
| 124 | 21.36 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 19.97 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 19.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.5 | 35.0 | 11.25 | 9.54 | 0.85 |
| 51 | 17.58 | 35.0 | 11.25 | 9.61 | 0.85 |
| 28 | 15.95 | 35.0 | 11.25 | 9.88 | 0.85 |
| 102 | 28.4 | 21.0 | 11.25 | 10.0 | 0.85 |
| 61 | 12.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.19 | 35.0 | 11.25 | 9.52 | 0.85 |
| 120 | 34.99 | 35.0 | 11.25 | 9.99 | 0.6 |
| 6 | 9.4 | 21.0 | 15.0 | 8.64 | 1.0 |
