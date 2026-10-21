# RANKING - generated 2026-10-21T11:40:19Z, block 9331602

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
| 1 | 114 | SOMA | 79.2 | 0.85 | 4,399 | 4,399 | cpu-small | 0.000 | 2 | 75% | SCORING_COMMIT 4.9d ago |
| 2 | 121 | sundae_bar | 74.7 | 0.85 | 1,169 | 1,169 | cpu-small | 0.600 | 2 | 60% | SCORING_COMMIT 4.7d ago |
| 3 | 3 | Teutonic | 74.4 | 0.85 | 2,745 | 7,335 | rtx4090 | 0.000 | 5 | 40% | SCORING_COMMIT 0.9d ago |
| 4 | 120 | Affine | 73.8 | 0.85 | 2,325 | 11,472 | rtx4090 | 0.100 | 10 | 33% | MECHANISM_ADDED 4.1d ago |
| 5 | 97 | Ingot | 73.4 | 0.85 | 2,028 | 2,028 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.9d ago |
| 6 | 91 | cascade | 71.2 | 0.85 | 410 | 1,643 | cpu-small | 0.000 | 5 | 52% | SCORING_COMMIT 3.6d ago |
| 7 | 102 | ConnitoAI | 71.1 | 0.85 | 1,024 | 1,024 | rtx4090 | 0.250 | 4 | 25% | RELEASE 4.6d ago |
| 8 | 1 | Apex | 68.5 | 0.85 | 474 | 1,011 | rtx4090 | 0.569 | 5 | 57% | RELEASE 2.7d ago |
| 9 | 82 | Noah | 68.0 | 0.85 | 667 | 672 | rtx4090 | 0.000 | 61 | 2% | subnet is 24 days old |
| 10 | 67 | Harnyx | 68.0 | 1.0 | 8.26 | 236 | cpu-small | 0.095 | 132 | 10% | SCORING_COMMIT 0.0d ago |
| 11 | 125 | Refinery | 67.4 | 0.85 | 337 | 994 | rtx4090 | 0.232 | 4 | 50% | README_TASK_DIFF 3.2d ago |
| 12 | 53 | engy | 67.3 | 0.85 | 332 | 2,810 | rtx4090 | 0.000 | 36 | 12% | SCORING_COMMIT 2.0d ago |
| 13 | 107 | Minos | 67.2 | 1.0 | 235 | 20,988 | cpu-small | 0.000 | 20 | 80% | SCORING_COMMIT 12d ago |
| 14 | 15 | ORO | 66.7 | 1.0 | 8.08 | 16.38 | cpu-small | 0.000 | 63 | 97% | SCORING_COMMIT 1.6d ago |
| 15 | 66 | conjectures | 63.8 | 0.85 | 115 | 239 | rtx4090 | 0.000 | 4 | 80% | RELEASE 0.7d ago |
| 16 | 26 | Perturb | 63.0 | 1.0 | 194 | 262 | rtx3060 | 0.000 | 4 | 61% | SCORING_COMMIT 17d ago |
| 17 | 81 | Reliquary | 63.0 | 0.85 | 90.61 | 221 | rtx4090 | 0.761 | 12 | 76% | SCORING_COMMIT 0.2d ago |
| 18 | 55 | NIOME | 62.2 | 0.85 | 70.82 | 585 | rtx4090 | 0.010 | 11 | 30% | SCORING_COMMIT 3.2d ago |
| 19 | 23 | Trishool | 61.5 | 0.85 | 794 | 794 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 22d ago |
| 20 | 92 | REAX | 60.1 | 0.85 | 75.86 | 3,023 | rtx4090 | 0.000 | 245 | 11% | subnet is 12 days old |
| 21 | 49 | Nepher Robotics | 59.6 | 0.85 | 1,164 | 4,101 | rtx4090 | 0.000 | 3 | 70% | SCORING_COMMIT 16d ago |
| 22 | 80 | OpenRoboto | 59.3 | 0.85 | 1,074 | 4,525 | rtx4090 | 0.000 | 11 | 25% | README_TASK_DIFF 16d ago |
| 23 | 4 | Targon | 57.9 | 0.85 | 9,949 | 29,328 | rtx4090 | 0.000 | 5 | 70% | RELEASE 34d ago |
| 24 | 111 | Claims | 57.9 | 0.85 | 20.22 | 2,921 | rtx4090 | 0.000 | 7 | 90% | RELEASE 1.6d ago |
| 25 | 5 | Hone | 57.8 | 0.85 | 33.37 | 39.82 | rtx4090 | 0.000 | 242 | 0% | SCORING_COMMIT 0.5d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 96 | Verathos | -4.33 | rtx4090 | 53.03222547483359 |
| 18 | Zeus | -1.74 | rtx4090 | 789.7454588811958 |
| 50 | Synth | -2.11 | rtx4090 | 65.10772133821742 |
| 22 | Desearch | -3.93 | rtx4090 | 20.69033715387437 |
| 78 | Umi | -4.10 | rtx4090 | 185.8081636864489 |
| 8 | Vanta | -6.83 | rtx4090 | 1.857835576743411 |
| 89 | InfiniteQuant | -8.10 | rtx4090 | 403.6401507640574 |
| 54 | Yanez | -3.66 | a4000 | 1377.071968939147 |
| 51 | lium.io | -38.34 | h200-141 | 2550.0560683842546 |
| 13 | Data Universe | -3.48 | rtx4090 | 4.845173908622369 |
| 45 | AlphaRidge.ai | -4.88 | rtx4090 | 5.1785864316676475 |
| 88 | Investing | -6.89 | rtx4090 | 210.00905327782112 |
| 63 | Enigma | -8.13 | rtx4090 | 3021.612402537549 |
| 6 | Numinous | -0.96 | cpu-small | 259.57052813783014 |
| 34 | BitMind | -3.82 | a100-80 | 3299.142137072934 |
| 123 | MANTIS | -5.57 | rtx4090 | 57.59251423974983 |
| 75 | Hippius | -7.57 | rtx4090 | 14010.88278505088 |
| 19 | blockmachine | -2.57 | rtx4090 | 1701.5873978507707 |
| 105 | Beam | -6.25 | rtx4090 | 73.17579166000223 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 34 subnets: sn2, sn7, sn10, sn12, sn24, sn27, sn30, sn31, sn37, sn39, sn42, sn52, sn57, sn59, sn69, sn72, sn73, sn74, sn76, sn84, sn87, sn94, sn95, sn100, sn104, sn108, sn109, sn113, sn115, sn116, sn117, sn119, sn126, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 114 | 33.14 | 35.0 | 15.0 | 9.99 | 0.85 |
| 121 | 27.9 | 35.0 | 15.0 | 10.0 | 0.85 |
| 3 | 31.28 | 35.0 | 11.25 | 9.97 | 0.85 |
| 120 | 30.62 | 35.0 | 11.25 | 9.98 | 0.85 |
| 97 | 30.08 | 35.0 | 11.25 | 9.99 | 0.85 |
| 91 | 23.77 | 35.0 | 15.0 | 9.98 | 0.85 |
| 102 | 27.38 | 35.0 | 11.25 | 9.98 | 0.85 |
| 1 | 24.34 | 35.0 | 11.25 | 10.0 | 0.85 |
| 82 | 25.69 | 35.0 | 11.25 | 8.01 | 0.85 |
| 67 | 8.79 | 35.0 | 15.0 | 9.22 | 1.0 |
| 125 | 23.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 22.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 107 | 21.58 | 21.0 | 15.0 | 9.62 | 1.0 |
| 15 | 8.71 | 35.0 | 15.0 | 8.02 | 1.0 |
| 66 | 18.78 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 20.84 | 21.0 | 11.25 | 9.95 | 1.0 |
| 81 | 17.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 26.38 | 21.0 | 15.0 | 9.99 | 0.85 |
| 92 | 17.15 | 35.0 | 11.25 | 7.26 | 0.85 |
| 49 | 27.89 | 21.0 | 11.25 | 10.0 | 0.85 |
| 80 | 27.57 | 21.0 | 11.25 | 10.0 | 0.85 |
| 4 | 36.36 | 10.5 | 11.25 | 10.0 | 0.85 |
| 111 | 12.07 | 35.0 | 11.25 | 9.78 | 0.85 |
| 5 | 13.97 | 35.0 | 11.25 | 7.81 | 0.85 |
