# RANKING - generated 2026-08-09T19:56:14Z, block 8809060

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
| 1 | 107 | Minos | 78.1 | 1.0 | 114 | 33,745 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 5.6d ago |
| 2 | 76 | Phylax | 76.8 | 1.0 | 68.54 | 206 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.9d ago |
| 3 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,218 | 1,218 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 2.0d ago |
| 4 | 67 | Harnyx | 70.8 | 1.0 | 15.19 | 868 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.4d ago |
| 5 | 91 | cascade | 70.3 | 0.85 | 801 | 2,741 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.6d ago |
| 6 | 1 | Apex | 70.1 | 0.85 | 757 | 1,560 | rtx4090 | 0.494 | 4 | 49% | RELEASE 2.0d ago |
| 7 | 41 | Almanac | 69.5 | 1.0 | 11.77 | 35.07 | cpu-small | 0.718 | 66 | 72% | SCORING_COMMIT 2.8d ago |
| 8 | 96 | Verathos | 68.6 | 1.0 | 23.28 | 230 | rtx4090 | 0.414 | 68 | 41% | RELEASE 0.3d ago |
| 9 | 62 | Ridges | 68.3 | 0.85 | 443 | 2,054 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.9d ago |
| 10 | 26 | Perturb | 68.2 | 1.0 | 21.32 | 40.60 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.2d ago |
| 11 | 100 | BASE | 68.1 | 0.85 | 416 | 1,687 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.9d ago |
| 12 | 15 | ORO | 68.1 | 1.0 | 10.34 | 19.75 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.4d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 220 | 3,693 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.4d ago |
| 14 | 21 | AdTAO | 65.5 | 1.0 | 4.76 | 21.98 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.2d ago |
| 15 | 80 | OpenRoboto | 65.1 | 0.85 | 171 | 620 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 1.6d ago |
| 16 | 28 | gm | 62.8 | 0.85 | 87.11 | 3,988 | rtx4090 | 0.304 | 26 | 40% | RELEASE 1.9d ago |
| 17 | 61 | RedTeam | 62.7 | 0.85 | 83.65 | 350 | rtx4090 | 0.000 | 48 | 7% | RELEASE 0.4d ago |
| 18 | 51 | lium.io | 59.3 | 0.85 | 37.95 | 3,109 | rtx4090 | 0.000 | 50 | 60% | SCORING_COMMIT 2.0d ago |
| 19 | 6 | Numinous | 59.1 | 1.0 | 29.82 | 342 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 20 | 102 | ConnitoAI | 58.9 | 0.85 | 932 | 1,447 | rtx4090 | 0.250 | 6 | 31% | RELEASE 9d ago |
| 21 | 56 | Gradients | 56.7 | 0.85 | 482 | 1,015 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 22 | 85 | Vidaio | 55.1 | 0.85 | 305 | 479 | rtx4090 | 0.000 | 10 | 21% | SCORING_COMMIT 13d ago |
| 23 | 120 | Affine | 54.9 | 0.6 | 7,396 | 7,396 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.3d ago |
| 24 | 124 | Swarm | 54.0 | 0.85 | 226 | 687 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |
| 25 | 2 | DSperse | 53.2 | 0.85 | 3.92 | 113 | rtx4090 | 0.827 | 12 | 83% | RELEASE 3.6d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.81 | a4000 | 1020.3022721476426 |
| 104 | Masx.ai | -1.53 | rtx4090 | 8.347462669242633 |
| 13 | Data Universe | -2.86 | rtx4090 | 7.302413318430752 |
| 88 | Investing | -4.87 | rtx4090 | 520.966969972163 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 123.4474677727342 |
| 8 | Vanta | -7.39 | rtx4090 | 3406.8526886864265 |
| 22 | Desearch | -0.40 | rtx4090 | 109.14639331635404 |
| 19 | blockmachine | -1.21 | rtx4090 | 340.08960339357134 |
| 45 | AlphaRidge.ai | -3.94 | rtx4090 | 32.746340295611276 |
| 18 | Zeus | -4.37 | rtx4090 | 998.4442986193742 |
| 75 | Hippius | -4.50 | rtx4090 | 5.844320612674204 |
| 123 | MANTIS | -6.24 | rtx4090 | 75.27897470134087 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07638520917830531 |
| 105 | Beam | -4.15 | rtx4090 | 195.89206989649176 |
| 84 | ansuz | -8.15 | rtx4090 | 521.156300407839 |
| 34 | BitMind | -18.28 | a100-80 | 301.47218045323746 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.74 | 35.0 | 15.0 | 9.4 | 1.0 |
| 76 | 16.76 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.07 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.0 | 35.0 | 15.0 | 9.83 | 1.0 |
| 91 | 26.41 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.06 | 35.0 | 15.0 | 9.41 | 1.0 |
| 96 | 12.6 | 35.0 | 11.25 | 9.7 | 1.0 |
| 62 | 24.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.27 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 23.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.59 | 35.0 | 15.0 | 8.55 | 1.0 |
| 38 | 21.32 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 6.91 | 35.0 | 15.0 | 8.55 | 1.0 |
| 80 | 20.33 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 17.69 | 35.0 | 11.25 | 9.92 | 0.85 |
| 61 | 17.53 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.47 | 35.0 | 11.25 | 9.09 | 0.85 |
| 6 | 13.54 | 21.0 | 15.0 | 9.54 | 1.0 |
| 102 | 27.01 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.41 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 22.6 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.19 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.43 | 21.0 | 11.25 | 9.85 | 0.85 |
| 2 | 6.29 | 35.0 | 11.25 | 9.99 | 0.85 |
