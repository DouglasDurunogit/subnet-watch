# RANKING - generated 2026-08-10T04:49:52Z, block 8811728

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
| 1 | 107 | Minos | 78.2 | 1.0 | 116 | 32,680 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 6.0d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 66.88 | 202 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.3d ago |
| 3 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,770 | 1,770 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 2.9d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,222 | 1,222 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 2.4d ago |
| 5 | 96 | Verathos | 72.2 | 1.0 | 57.01 | 299 | rtx4090 | 0.421 | 40 | 42% | RELEASE 0.6d ago |
| 6 | 67 | Harnyx | 71.2 | 1.0 | 17.21 | 749 | cpu-small | 0.024 | 125 | 19% | SCORING_COMMIT 0.8d ago |
| 7 | 91 | cascade | 70.2 | 0.85 | 782 | 2,678 | rtx4090 | 0.000 | 5 | 48% | RELEASE 5.0d ago |
| 8 | 1 | Apex | 69.8 | 0.85 | 708 | 1,625 | rtx4090 | 0.496 | 4 | 50% | RELEASE 2.4d ago |
| 9 | 41 | Almanac | 69.2 | 1.0 | 11.03 | 34.14 | cpu-small | 0.699 | 69 | 70% | SCORING_COMMIT 3.2d ago |
| 10 | 26 | Perturb | 68.2 | 1.0 | 21.09 | 39.27 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.6d ago |
| 11 | 15 | ORO | 68.2 | 1.0 | 10.23 | 19.72 | cpu-small | 0.000 | 75 | 94% | RELEASE 3.8d ago |
| 12 | 62 | Ridges | 68.1 | 0.85 | 425 | 1,974 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.3d ago |
| 13 | 100 | BASE | 66.4 | 0.85 | 255 | 840 | rtx4090 | 0.000 | 6 | 51% | SCORING_COMMIT 1.3d ago |
| 14 | 38 | ChronoLLM | 65.7 | 0.85 | 217 | 3,638 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.8d ago |
| 15 | 21 | AdTAO | 65.4 | 1.0 | 4.62 | 21.46 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.6d ago |
| 16 | 80 | OpenRoboto | 65.0 | 0.85 | 164 | 596 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 2.0d ago |
| 17 | 28 | gm | 64.3 | 0.85 | 135 | 3,886 | rtx4090 | 0.288 | 26 | 39% | RELEASE 2.3d ago |
| 18 | 61 | RedTeam | 62.7 | 0.85 | 83.29 | 349 | rtx4090 | 0.000 | 45 | 7% | RELEASE 0.8d ago |
| 19 | 51 | lium.io | 58.9 | 0.85 | 34.23 | 3,170 | rtx4090 | 0.000 | 50 | 56% | SCORING_COMMIT 2.4d ago |
| 20 | 6 | Numinous | 57.9 | 1.0 | 22.83 | 448 | cpu-small | 0.000 | 18 | 26% | README_TASK_DIFF 11d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 470 | 990 | rtx4090 | 0.707 | 7 | 71% | SCORING_COMMIT 12d ago |
| 22 | 120 | Affine | 54.8 | 0.6 | 7,222 | 7,222 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.7d ago |
| 23 | 2 | DSperse | 54.3 | 0.85 | 5.86 | 106 | rtx4090 | 0.826 | 12 | 83% | RELEASE 4.0d ago |
| 24 | 124 | Swarm | 53.9 | 0.85 | 218 | 669 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 9d ago |
| 25 | 74 | Gittensor | 51.8 | 0.85 | 4.66 | 219 | rtx4090 | 0.630 | 16 | 63% | RELEASE 2.5d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.97 | a4000 | 993.5285866850879 |
| 104 | Masx.ai | -1.91 | rtx4090 | 10.389672894981064 |
| 13 | Data Universe | -3.46 | rtx4090 | 6.541037637183691 |
| 88 | Investing | -4.55 | rtx4090 | 564.0279704515922 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 212.88566299083354 |
| 8 | Vanta | -7.40 | rtx4090 | 3338.634163386158 |
| 19 | blockmachine | -1.28 | rtx4090 | 341.923541747948 |
| 18 | Zeus | -3.39 | rtx4090 | 1416.2417477605898 |
| 45 | AlphaRidge.ai | -4.23 | rtx4090 | 11.233373928124943 |
| 75 | Hippius | -4.57 | rtx4090 | 5.738694235699514 |
| 123 | MANTIS | -6.22 | rtx4090 | 73.8936119068895 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07462197957952844 |
| 105 | Beam | -4.56 | rtx4090 | 196.10797477810823 |
| 84 | ansuz | -8.15 | rtx4090 | 502.58996694077643 |
| 34 | BitMind | -18.49 | a100-80 | 294.2502805983741 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn117, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.81 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 16.66 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.54 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.08 | 35.0 | 15.0 | 10.0 | 0.85 |
| 96 | 16.04 | 35.0 | 11.25 | 9.88 | 1.0 |
| 67 | 11.46 | 35.0 | 15.0 | 9.72 | 1.0 |
| 91 | 26.32 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 25.93 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.82 | 35.0 | 15.0 | 9.39 | 1.0 |
| 26 | 12.23 | 35.0 | 11.25 | 9.68 | 1.0 |
| 15 | 9.55 | 35.0 | 15.0 | 8.64 | 1.0 |
| 62 | 23.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 21.9 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 21.26 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 6.82 | 35.0 | 15.0 | 8.54 | 1.0 |
| 80 | 20.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 19.4 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 17.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.07 | 35.0 | 11.25 | 9.01 | 0.85 |
| 6 | 12.53 | 21.0 | 15.0 | 9.41 | 1.0 |
| 56 | 24.31 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.1 | 35.0 | 11.25 | 9.99 | 0.6 |
| 2 | 7.61 | 35.0 | 11.25 | 9.99 | 0.85 |
| 124 | 21.29 | 21.0 | 11.25 | 9.85 | 0.85 |
| 74 | 6.85 | 35.0 | 11.25 | 7.83 | 0.85 |
