# RANKING - generated 2026-08-20T23:49:36Z, block 8889417

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 75.82 | 127 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.6d ago |
| 2 | 67 | Harnyx | 72.2 | 1.0 | 21.77 | 289 | cpu-small | 0.034 | 172 | 8% | SCORING_COMMIT 0.6d ago |
| 3 | 23 | Trishool | 72.0 | 0.85 | 526 | 526 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.8d ago |
| 4 | 15 | ORO | 70.3 | 1.0 | 20.16 | 19,673 | cpu-small | 0.000 | 81 | 92% | SCORING_COMMIT 2.2d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 683 | 1,044 | rtx4090 | 0.724 | 5 | 72% | SCORING_COMMIT 3.0d ago |
| 6 | 91 | cascade | 69.4 | 0.85 | 621 | 2,508 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 0.0d ago |
| 7 | 1 | Apex | 68.2 | 0.85 | 428 | 1,214 | rtx4090 | 0.534 | 5 | 53% | RELEASE 1.1d ago |
| 8 | 38 | ChronoLLM | 67.6 | 0.85 | 154 | 3,268 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.1d ago |
| 9 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,535 | 4,535 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 19d ago |
| 10 | 96 | Verathos | 67.4 | 1.0 | 17.55 | 367 | rtx4090 | 0.404 | 92 | 40% | RELEASE 2.3d ago |
| 11 | 26 | Perturb | 67.4 | 1.0 | 17.44 | 251 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.9d ago |
| 12 | 107 | Minos | 64.4 | 1.0 | 122 | 37,629 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 13 | 85 | Vidaio | 64.3 | 0.85 | 135 | 1,491 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.7d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 122 | 179 | rtx4090 | 0.662 | 7 | 66% | SCORING_COMMIT 0.9d ago |
| 15 | 51 | lium.io | 61.9 | 0.85 | 73.19 | 1,261 | rtx4090 | 0.000 | 46 | 82% | SCORING_COMMIT 0.7d ago |
| 16 | 55 | NIOME | 61.9 | 0.85 | 64.63 | 538 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 6.1d ago |
| 17 | 60 | Bitsec.ai | 61.3 | 0.85 | 739 | 1,035 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 18 | 81 | Reliquary | 60.8 | 0.85 | 47.01 | 192 | rtx4090 | 0.002 | 51 | 5% | SCORING_COMMIT 1.1d ago |
| 19 | 28 | gm | 60.7 | 0.85 | 47.22 | 1,417 | rtx4090 | 0.128 | 52 | 13% | RELEASE 0.4d ago |
| 20 | 53 | engy | 60.1 | 0.85 | 37.52 | 248 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.3d ago |
| 21 | 102 | ConnitoAI | 59.6 | 0.85 | 1,160 | 1,894 | rtx4090 | 0.250 | 6 | 32% | RELEASE 20d ago |
| 22 | 41 | Almanac | 55.3 | 1.0 | 11.45 | 23.83 | cpu-small | 0.723 | 77 | 72% | SCORING_COMMIT 8d ago |
| 23 | 68 | NOVA | 55.2 | 0.6 | 8,552 | 8,552 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.4d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,236 | 7,236 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.1d ago |
| 25 | 124 | Swarm | 54.5 | 0.85 | 260 | 758 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.41 | cpu-small | 4.802114031665155 |
| 54 | Yanez | -3.52 | a4000 | 1095.8745626296864 |
| 18 | Zeus | -3.66 | rtx4090 | 1651.4567441987892 |
| 13 | Data Universe | -4.22 | rtx4090 | 7.69989161812138 |
| 123 | MANTIS | -5.57 | rtx4090 | 101.67210444351073 |
| 75 | Hippius | -6.12 | rtx4090 | 11780.628660967983 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 127.65124899425852 |
| 34 | BitMind | -19.66 | a100-80 | 3118.236652723148 |
| 6 | Numinous | -0.96 | cpu-small | 384.454639979355 |
| 104 | Masx.ai | -1.68 | rtx4090 | 10.090159205287412 |
| 88 | Investing | -4.32 | rtx4090 | 988.6487612583221 |
| 8 | Vanta | -7.40 | rtx4090 | 3061.6787967456216 |
| 43 | Graphite | -0.84 | cpu-small | 24.881429764022425 |
| 32 | ItsAI | -0.14 | rtx4090 | 11.577934480097577 |
| 19 | blockmachine | -1.00 | rtx4090 | 1516.1707800380293 |
| 22 | Desearch | -4.33 | rtx4090 | 143.6055034234313 |
| 45 | AlphaRidge.ai | -5.65 | rtx4090 | 10.140627098912796 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08001511509489165 |
| 105 | Beam | -2.41 | rtx4090 | 76.4039935608016 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06560039488757698 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.15 | 35.0 | 15.0 | 9.91 | 1.0 |
| 67 | 12.35 | 35.0 | 15.0 | 9.82 | 1.0 |
| 23 | 24.76 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 12.06 | 35.0 | 15.0 | 8.24 | 1.0 |
| 56 | 25.79 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.41 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 23.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.92 | 35.0 | 15.0 | 9.66 | 0.85 |
| 11 | 33.26 | 21.0 | 15.0 | 10.0 | 0.85 |
| 96 | 11.54 | 35.0 | 11.25 | 9.59 | 1.0 |
| 26 | 11.51 | 35.0 | 11.25 | 9.59 | 1.0 |
| 107 | 19.02 | 21.0 | 15.0 | 9.42 | 1.0 |
| 85 | 19.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 19.0 | 35.0 | 11.25 | 9.97 | 0.85 |
| 51 | 17.01 | 35.0 | 11.25 | 9.51 | 0.85 |
| 55 | 16.53 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.1 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 15.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.31 | 35.0 | 11.25 | 9.85 | 0.85 |
| 53 | 14.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.88 | 21.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.96 | 21.0 | 15.0 | 9.37 | 1.0 |
| 68 | 35.76 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.1 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.98 | 21.0 | 11.25 | 9.85 | 0.85 |
