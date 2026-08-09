# RANKING - generated 2026-08-09T21:44:55Z, block 8809603

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
| 1 | 107 | Minos | 78.2 | 1.0 | 116 | 33,640 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 5.7d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 68.37 | 206 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.0d ago |
| 3 | 60 | Bitsec.ai | 74.8 | 0.85 | 1,205 | 1,205 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 2.1d ago |
| 4 | 67 | Harnyx | 70.8 | 1.0 | 15.15 | 866 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.5d ago |
| 5 | 91 | cascade | 70.2 | 0.85 | 800 | 2,738 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.7d ago |
| 6 | 1 | Apex | 70.0 | 0.85 | 749 | 1,543 | rtx4090 | 0.501 | 4 | 50% | RELEASE 2.1d ago |
| 7 | 96 | Verathos | 69.9 | 1.0 | 32.73 | 273 | rtx4090 | 0.424 | 51 | 42% | RELEASE 0.3d ago |
| 8 | 41 | Almanac | 69.5 | 1.0 | 11.86 | 34.82 | cpu-small | 0.717 | 65 | 72% | SCORING_COMMIT 2.9d ago |
| 9 | 62 | Ridges | 68.3 | 0.85 | 441 | 2,046 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.0d ago |
| 10 | 26 | Perturb | 68.2 | 1.0 | 21.25 | 41.47 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.3d ago |
| 11 | 100 | BASE | 68.0 | 0.85 | 411 | 1,670 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.0d ago |
| 12 | 15 | ORO | 68.0 | 1.0 | 10.43 | 19.92 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.5d ago |
| 13 | 28 | gm | 65.8 | 0.85 | 210 | 4,198 | rtx4090 | 0.139 | 24 | 43% | RELEASE 2.0d ago |
| 14 | 38 | ChronoLLM | 65.7 | 0.85 | 220 | 3,694 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.5d ago |
| 15 | 21 | AdTAO | 65.4 | 1.0 | 4.72 | 21.84 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.3d ago |
| 16 | 80 | OpenRoboto | 65.3 | 0.85 | 183 | 663 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 1.7d ago |
| 17 | 61 | RedTeam | 62.6 | 0.85 | 79.70 | 335 | rtx4090 | 0.000 | 47 | 7% | RELEASE 0.5d ago |
| 18 | 51 | lium.io | 59.3 | 0.85 | 37.94 | 3,109 | rtx4090 | 0.000 | 50 | 60% | SCORING_COMMIT 2.1d ago |
| 19 | 6 | Numinous | 59.1 | 1.0 | 29.72 | 341 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 20 | 56 | Gradients | 56.7 | 0.85 | 480 | 1,012 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 21 | 120 | Affine | 54.9 | 0.6 | 7,407 | 7,407 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.4d ago |
| 22 | 124 | Swarm | 54.0 | 0.85 | 225 | 685 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |
| 23 | 2 | DSperse | 53.1 | 0.85 | 3.85 | 113 | rtx4090 | 0.826 | 12 | 83% | RELEASE 3.7d ago |
| 24 | 85 | Vidaio | 52.3 | 0.85 | 129 | 638 | rtx4090 | 0.000 | 10 | 20% | SCORING_COMMIT 13d ago |
| 25 | 74 | Gittensor | 52.1 | 0.85 | 4.99 | 235 | rtx4090 | 0.626 | 16 | 63% | RELEASE 2.2d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.98 | a4000 | 1029.585771600184 |
| 104 | Masx.ai | -1.59 | rtx4090 | 9.263918482061941 |
| 13 | Data Universe | -2.95 | rtx4090 | 7.317548875034115 |
| 88 | Investing | -4.91 | rtx4090 | 515.5722095732422 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 126.12405463142768 |
| 8 | Vanta | -7.39 | rtx4090 | 3398.872879048527 |
| 19 | blockmachine | -1.32 | rtx4090 | 351.07641839831894 |
| 22 | Desearch | -1.79 | rtx4090 | 97.21505999106223 |
| 18 | Zeus | -2.67 | rtx4090 | 1459.6792853874676 |
| 45 | AlphaRidge.ai | -3.19 | rtx4090 | 20.808562454361354 |
| 75 | Hippius | -4.42 | rtx4090 | 5.833958406275481 |
| 123 | MANTIS | -6.23 | rtx4090 | 75.07898941583726 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07619583160081023 |
| 105 | Beam | -4.09 | rtx4090 | 198.3346498000609 |
| 84 | ansuz | -8.15 | rtx4090 | 512.8681917182747 |
| 34 | BitMind | -18.08 | a100-80 | 300.70742181243526 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.81 | 35.0 | 15.0 | 9.41 | 1.0 |
| 76 | 16.75 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.03 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 10.99 | 35.0 | 15.0 | 9.81 | 1.0 |
| 91 | 26.41 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 13.9 | 35.0 | 11.25 | 9.79 | 1.0 |
| 41 | 10.09 | 35.0 | 15.0 | 9.42 | 1.0 |
| 62 | 24.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.25 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 23.79 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.62 | 35.0 | 15.0 | 8.4 | 1.0 |
| 28 | 21.15 | 35.0 | 11.25 | 9.97 | 0.85 |
| 38 | 21.32 | 35.0 | 11.25 | 9.73 | 0.85 |
| 21 | 6.89 | 35.0 | 15.0 | 8.54 | 1.0 |
| 80 | 20.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.34 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.46 | 35.0 | 11.25 | 9.09 | 0.85 |
| 6 | 13.53 | 21.0 | 15.0 | 9.54 | 1.0 |
| 56 | 24.4 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.2 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.42 | 21.0 | 11.25 | 9.85 | 0.85 |
| 2 | 6.23 | 35.0 | 11.25 | 9.99 | 0.85 |
| 85 | 19.23 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 7.07 | 35.0 | 11.25 | 7.93 | 0.85 |
