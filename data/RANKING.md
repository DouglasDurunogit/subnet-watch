# RANKING - generated 2026-08-16T08:43:49Z, block 8856089

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
| 1 | 107 | Minos | 77.7 | 1.0 | 103 | 31,929 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.7d ago |
| 2 | 76 | Phylax | 73.9 | 1.0 | 32.68 | 157 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.0d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.62 | 417 | cpu-small | 0.045 | 131 | 11% | SCORING_COMMIT 0.1d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 40.59 | 74.46 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.7d ago |
| 5 | 96 | Verathos | 70.3 | 1.0 | 35.35 | 251 | rtx4090 | 0.410 | 56 | 41% | RELEASE 1.5d ago |
| 6 | 1 | Apex | 70.2 | 0.85 | 789 | 1,086 | rtx4090 | 0.536 | 4 | 54% | RELEASE 2.8d ago |
| 7 | 41 | Almanac | 69.9 | 1.0 | 12.91 | 53.78 | cpu-small | 0.651 | 74 | 65% | SCORING_COMMIT 3.4d ago |
| 8 | 15 | ORO | 68.8 | 1.0 | 12.57 | 12,637 | cpu-small | 0.000 | 60 | 95% | SCORING_COMMIT 2.4d ago |
| 9 | 56 | Gradients | 68.7 | 0.85 | 505 | 958 | rtx4090 | 0.675 | 7 | 67% | SCORING_COMMIT 3.8d ago |
| 10 | 85 | Vidaio | 68.6 | 0.85 | 494 | 494 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 3.9d ago |
| 11 | 62 | Ridges | 68.5 | 0.85 | 474 | 2,196 | rtx4090 | 0.000 | 6 | 40% | RELEASE 1.4d ago |
| 12 | 91 | cascade | 68.2 | 0.85 | 440 | 2,263 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 2.4d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.62 | 34.15 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.9d ago |
| 14 | 38 | ChronoLLM | 66.0 | 0.85 | 97.16 | 1,328 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.7d ago |
| 15 | 124 | Swarm | 65.9 | 0.85 | 223 | 716 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.7d ago |
| 16 | 2 | DSperse | 63.0 | 0.85 | 90.53 | 144 | rtx4090 | 0.822 | 5 | 82% | RELEASE 5.5d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.98 | 481 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.5d ago |
| 18 | 28 | gm | 60.2 | 0.85 | 41.29 | 2,409 | rtx4090 | 0.177 | 40 | 28% | RELEASE 3.8d ago |
| 19 | 60 | Bitsec.ai | 59.4 | 0.85 | 421 | 421 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 20 | 102 | ConnitoAI | 58.6 | 0.85 | 871 | 1,742 | rtx4090 | 0.251 | 6 | 33% | RELEASE 15d ago |
| 21 | 74 | Gittensor | 58.0 | 0.85 | 26.00 | 208 | rtx4090 | 0.630 | 14 | 63% | RELEASE 4.6d ago |
| 22 | 61 | RedTeam | 57.6 | 0.85 | 17.38 | 440 | rtx4090 | 0.000 | 81 | 10% | RELEASE 5.0d ago |
| 23 | 51 | lium.io | 57.1 | 0.85 | 22.29 | 1,355 | rtx4090 | 0.000 | 52 | 82% | SCORING_COMMIT 2.0d ago |
| 24 | 120 | Affine | 56.8 | 0.6 | 16,527 | 16,527 | rtx4090 | 0.500 | 2 | 50% | SCORING_COMMIT 3.8d ago |
| 25 | 80 | OpenRoboto | 53.1 | 0.85 | 167 | 606 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 243.67760339347117 |
| 54 | Yanez | -3.73 | a4000 | 951.8729714097723 |
| 89 | InfiniteQuant | -4.39 | rtx4090 | 185.89233937661575 |
| 75 | Hippius | -7.30 | rtx4090 | 10790.771645796378 |
| 101 | Tag101 | -0.04 | cpu-small | 1.941676782219088 |
| 13 | Data Universe | -3.60 | rtx4090 | 5.667873410127574 |
| 88 | Investing | -5.34 | rtx4090 | 1161.6967134282104 |
| 8 | Vanta | -7.70 | rtx4090 | 2899.587666323 |
| 114 | SOMA | -8.13 | rtx4090 | 602.4296963836822 |
| 43 | Graphite | -0.75 | cpu-small | 16.555131105333036 |
| 32 | ItsAI | -0.49 | rtx4090 | 10.518113675875231 |
| 22 | Desearch | -2.01 | rtx4090 | 50.668827184670015 |
| 45 | AlphaRidge.ai | -3.54 | rtx4090 | 16.18137255357388 |
| 18 | Zeus | -5.10 | rtx4090 | 726.633441169442 |
| 123 | MANTIS | -6.03 | rtx4090 | 75.81551630771462 |
| 19 | blockmachine | -6.23 | rtx4090 | 1083.094728531671 |
| 63 | Enigma | -8.14 | rtx4090 | 5015.600224709527 |
| 105 | Beam | -2.91 | rtx4090 | 101.01788955841491 |
| 84 | ansuz | -8.16 | rtx4090 | 439.31701937834987 |
| 34 | BitMind | -20.11 | a100-80 | 19.281042669355045 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.36 | 35.0 | 15.0 | 9.37 | 1.0 |
| 76 | 13.89 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.65 | 35.0 | 15.0 | 9.83 | 1.0 |
| 26 | 14.72 | 35.0 | 11.25 | 9.84 | 1.0 |
| 96 | 14.19 | 35.0 | 11.25 | 9.81 | 1.0 |
| 1 | 26.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.4 | 35.0 | 15.0 | 9.49 | 1.0 |
| 15 | 10.3 | 35.0 | 15.0 | 8.5 | 1.0 |
| 56 | 24.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.51 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.35 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.05 | 35.0 | 11.25 | 9.99 | 0.85 |
| 21 | 8.51 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.12 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.38 | 35.0 | 11.25 | 9.85 | 0.85 |
| 2 | 17.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.79 | 35.0 | 11.25 | 9.84 | 0.85 |
| 60 | 23.88 | 21.0 | 15.0 | 10.0 | 0.85 |
| 102 | 26.74 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 13.02 | 35.0 | 11.25 | 8.98 | 0.85 |
| 61 | 11.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.43 | 35.0 | 11.25 | 8.53 | 0.85 |
| 120 | 38.37 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.25 | 21.0 | 11.25 | 10.0 | 0.85 |
