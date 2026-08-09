# RANKING - generated 2026-08-09T22:14:14Z, block 8809750

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
| 1 | 107 | Minos | 78.2 | 1.0 | 116 | 33,531 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 5.7d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 68.21 | 206 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.0d ago |
| 3 | 60 | Bitsec.ai | 74.8 | 0.85 | 1,201 | 1,201 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 2.1d ago |
| 4 | 67 | Harnyx | 70.8 | 1.0 | 15.11 | 864 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.5d ago |
| 5 | 91 | cascade | 70.2 | 0.85 | 798 | 2,732 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.7d ago |
| 6 | 1 | Apex | 70.0 | 0.85 | 746 | 1,700 | rtx4090 | 0.470 | 4 | 47% | RELEASE 2.1d ago |
| 7 | 96 | Verathos | 69.9 | 1.0 | 32.63 | 273 | rtx4090 | 0.424 | 51 | 42% | RELEASE 0.4d ago |
| 8 | 41 | Almanac | 69.5 | 1.0 | 11.86 | 34.74 | cpu-small | 0.717 | 65 | 72% | SCORING_COMMIT 2.9d ago |
| 9 | 62 | Ridges | 68.3 | 0.85 | 440 | 2,042 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.0d ago |
| 10 | 26 | Perturb | 68.3 | 1.0 | 21.71 | 191 | rtx3060 | 0.502 | 11 | 50% | SCORING_COMMIT 3.3d ago |
| 11 | 15 | ORO | 68.1 | 1.0 | 10.41 | 19.88 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.5d ago |
| 12 | 100 | BASE | 68.0 | 0.85 | 410 | 1,666 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.0d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 220 | 3,686 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.5d ago |
| 14 | 21 | AdTAO | 65.4 | 1.0 | 4.71 | 21.79 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.3d ago |
| 15 | 80 | OpenRoboto | 65.3 | 0.85 | 182 | 656 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 1.7d ago |
| 16 | 28 | gm | 65.2 | 0.85 | 176 | 4,555 | rtx4090 | 0.161 | 25 | 45% | RELEASE 2.0d ago |
| 17 | 61 | RedTeam | 62.6 | 0.85 | 80.49 | 338 | rtx4090 | 0.000 | 47 | 7% | RELEASE 0.5d ago |
| 18 | 6 | Numinous | 59.1 | 1.0 | 29.65 | 340 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 19 | 51 | lium.io | 59.0 | 0.85 | 35.10 | 2,658 | rtx4090 | 0.000 | 47 | 60% | SCORING_COMMIT 2.1d ago |
| 20 | 56 | Gradients | 56.6 | 0.85 | 479 | 1,009 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 21 | 120 | Affine | 54.9 | 0.6 | 7,391 | 7,391 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.4d ago |
| 22 | 124 | Swarm | 54.0 | 0.85 | 224 | 683 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |
| 23 | 2 | DSperse | 52.5 | 0.85 | 3.10 | 117 | rtx4090 | 0.826 | 12 | 83% | RELEASE 3.7d ago |
| 24 | 85 | Vidaio | 52.3 | 0.85 | 129 | 637 | rtx4090 | 0.000 | 10 | 20% | SCORING_COMMIT 13d ago |
| 25 | 74 | Gittensor | 52.0 | 0.85 | 4.96 | 235 | rtx4090 | 0.626 | 16 | 63% | RELEASE 2.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.89 | a4000 | 1022.6120756295127 |
| 104 | Masx.ai | -1.60 | rtx4090 | 9.243286146912583 |
| 13 | Data Universe | -2.93 | rtx4090 | 7.365764930730128 |
| 88 | Investing | -4.92 | rtx4090 | 514.2634923202962 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 125.84315473247129 |
| 8 | Vanta | -7.39 | rtx4090 | 3391.517735976708 |
| 19 | blockmachine | -1.10 | rtx4090 | 318.2144589010033 |
| 18 | Zeus | -2.69 | rtx4090 | 1455.5404074585156 |
| 45 | AlphaRidge.ai | -4.35 | rtx4090 | 26.56514833900669 |
| 75 | Hippius | -4.43 | rtx4090 | 5.82044533156651 |
| 123 | MANTIS | -6.24 | rtx4090 | 74.91177563094675 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0760003333608547 |
| 105 | Beam | -4.13 | rtx4090 | 196.5555334491855 |
| 84 | ansuz | -8.15 | rtx4090 | 511.72594630242116 |
| 34 | BitMind | -18.27 | a100-80 | 300.0519223562219 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.8 | 35.0 | 15.0 | 9.41 | 1.0 |
| 76 | 16.74 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.01 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 10.98 | 35.0 | 15.0 | 9.82 | 1.0 |
| 91 | 26.4 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.13 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 13.89 | 35.0 | 11.25 | 9.79 | 1.0 |
| 41 | 10.09 | 35.0 | 15.0 | 9.42 | 1.0 |
| 62 | 24.05 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.34 | 35.0 | 11.25 | 9.68 | 1.0 |
| 15 | 9.62 | 35.0 | 15.0 | 8.48 | 1.0 |
| 100 | 23.78 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 21.32 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 6.88 | 35.0 | 15.0 | 8.54 | 1.0 |
| 80 | 20.57 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 20.44 | 35.0 | 11.25 | 9.96 | 0.85 |
| 61 | 17.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 13.52 | 21.0 | 15.0 | 9.54 | 1.0 |
| 51 | 14.17 | 35.0 | 11.25 | 9.02 | 0.85 |
| 56 | 24.39 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.19 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.4 | 21.0 | 11.25 | 9.85 | 0.85 |
| 2 | 5.57 | 35.0 | 11.25 | 9.99 | 0.85 |
| 85 | 19.23 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 7.05 | 35.0 | 11.25 | 7.92 | 0.85 |
