# RANKING - generated 2026-08-09T20:48:53Z, block 8809323

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
| 1 | 107 | Minos | 78.1 | 1.0 | 113 | 33,490 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.7d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 68.16 | 205 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.0d ago |
| 3 | 60 | Bitsec.ai | 74.8 | 0.85 | 1,195 | 1,195 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 2.1d ago |
| 4 | 67 | Harnyx | 70.8 | 1.0 | 15.10 | 863 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.4d ago |
| 5 | 91 | cascade | 70.2 | 0.85 | 796 | 2,727 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.7d ago |
| 6 | 1 | Apex | 70.0 | 0.85 | 750 | 1,546 | rtx4090 | 0.497 | 4 | 50% | RELEASE 2.0d ago |
| 7 | 96 | Verathos | 69.5 | 1.0 | 29.12 | 194 | rtx4090 | 0.420 | 62 | 42% | RELEASE 0.3d ago |
| 8 | 41 | Almanac | 69.5 | 1.0 | 11.83 | 34.73 | cpu-small | 0.717 | 65 | 72% | SCORING_COMMIT 2.8d ago |
| 9 | 62 | Ridges | 68.3 | 0.85 | 440 | 2,042 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.0d ago |
| 10 | 26 | Perturb | 68.2 | 1.0 | 21.18 | 41.35 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.2d ago |
| 11 | 15 | ORO | 68.2 | 1.0 | 10.31 | 19.69 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.4d ago |
| 12 | 100 | BASE | 68.0 | 0.85 | 410 | 1,665 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.0d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 219 | 3,680 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.5d ago |
| 14 | 28 | gm | 65.7 | 0.85 | 209 | 4,179 | rtx4090 | 0.139 | 24 | 43% | RELEASE 2.0d ago |
| 15 | 21 | AdTAO | 65.4 | 1.0 | 4.70 | 21.77 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.3d ago |
| 16 | 80 | OpenRoboto | 65.2 | 0.85 | 178 | 642 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 1.7d ago |
| 17 | 61 | RedTeam | 62.6 | 0.85 | 81.49 | 342 | rtx4090 | 0.000 | 47 | 7% | RELEASE 0.4d ago |
| 18 | 51 | lium.io | 59.3 | 0.85 | 37.91 | 3,108 | rtx4090 | 0.000 | 50 | 60% | SCORING_COMMIT 2.0d ago |
| 19 | 6 | Numinous | 59.1 | 1.0 | 29.65 | 340 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 20 | 102 | ConnitoAI | 58.9 | 0.85 | 927 | 1,440 | rtx4090 | 0.250 | 6 | 31% | RELEASE 9d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 479 | 1,009 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 22 | 85 | Vidaio | 55.5 | 0.85 | 337 | 454 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 13d ago |
| 23 | 120 | Affine | 54.9 | 0.6 | 7,387 | 7,387 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.3d ago |
| 24 | 124 | Swarm | 54.0 | 0.85 | 224 | 683 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |
| 25 | 2 | DSperse | 53.1 | 0.85 | 3.81 | 112 | rtx4090 | 0.826 | 12 | 83% | RELEASE 3.7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.98 | a4000 | 1026.0927929156398 |
| 104 | Masx.ai | -0.57 | rtx4090 | 8.464696837219794 |
| 13 | Data Universe | -2.96 | rtx4090 | 7.306316617164905 |
| 88 | Investing | -4.92 | rtx4090 | 513.4512021255516 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 126.00834339682577 |
| 8 | Vanta | -7.39 | rtx4090 | 3389.187273694299 |
| 19 | blockmachine | -1.34 | rtx4090 | 350.0906378957802 |
| 22 | Desearch | -1.81 | rtx4090 | 96.94212110708229 |
| 45 | AlphaRidge.ai | -3.20 | rtx4090 | 20.74969571629043 |
| 18 | Zeus | -4.40 | rtx4090 | 993.0100123224428 |
| 75 | Hippius | -4.43 | rtx4090 | 5.811456510432847 |
| 123 | MANTIS | -6.24 | rtx4090 | 74.86821018260295 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07597474474299408 |
| 105 | Beam | -4.14 | rtx4090 | 196.0360911416681 |
| 84 | ansuz | -8.15 | rtx4090 | 514.7904217968887 |
| 34 | BitMind | -18.11 | a100-80 | 299.85287570462555 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.71 | 35.0 | 15.0 | 9.4 | 1.0 |
| 76 | 16.73 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 27.99 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 10.98 | 35.0 | 15.0 | 9.8 | 1.0 |
| 91 | 26.39 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 13.45 | 35.0 | 11.25 | 9.76 | 1.0 |
| 41 | 10.08 | 35.0 | 15.0 | 9.42 | 1.0 |
| 62 | 24.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.24 | 35.0 | 11.25 | 9.68 | 1.0 |
| 15 | 9.58 | 35.0 | 15.0 | 8.61 | 1.0 |
| 100 | 23.77 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 21.31 | 35.0 | 11.25 | 9.77 | 0.85 |
| 28 | 21.13 | 35.0 | 11.25 | 9.97 | 0.85 |
| 21 | 6.88 | 35.0 | 15.0 | 8.54 | 1.0 |
| 80 | 20.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.46 | 35.0 | 11.25 | 9.09 | 0.85 |
| 6 | 13.52 | 21.0 | 15.0 | 9.54 | 1.0 |
| 102 | 26.99 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.39 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.0 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.18 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.4 | 21.0 | 11.25 | 9.85 | 0.85 |
| 2 | 6.21 | 35.0 | 11.25 | 9.99 | 0.85 |
