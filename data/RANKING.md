# RANKING - generated 2026-08-21T04:08:40Z, block 8890712

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 76.41 | 128 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.8d ago |
| 2 | 23 | Trishool | 72.2 | 0.85 | 548 | 548 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 1.0d ago |
| 3 | 15 | ORO | 70.6 | 1.0 | 20.33 | 19,598 | cpu-small | 0.000 | 79 | 93% | SCORING_COMMIT 2.4d ago |
| 4 | 67 | Harnyx | 70.1 | 1.0 | 13.30 | 864 | cpu-small | 0.066 | 140 | 23% | SCORING_COMMIT 0.8d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 687 | 1,052 | rtx4090 | 0.724 | 5 | 72% | SCORING_COMMIT 3.2d ago |
| 6 | 91 | cascade | 69.4 | 0.85 | 626 | 2,528 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 0.2d ago |
| 7 | 1 | Apex | 68.2 | 0.85 | 432 | 1,201 | rtx4090 | 0.538 | 5 | 54% | RELEASE 1.3d ago |
| 8 | 38 | ChronoLLM | 67.7 | 0.85 | 155 | 3,281 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.3d ago |
| 9 | 96 | Verathos | 67.6 | 1.0 | 18.62 | 355 | rtx4090 | 0.403 | 91 | 40% | RELEASE 2.5d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.57 | 253 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.1d ago |
| 11 | 107 | Minos | 65.2 | 1.0 | 144 | 42,243 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 11d ago |
| 12 | 85 | Vidaio | 65.0 | 0.85 | 164 | 1,496 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.9d ago |
| 13 | 108 | Prometheon | 64.0 | 0.85 | 124 | 183 | rtx4090 | 0.660 | 7 | 66% | SCORING_COMMIT 1.1d ago |
| 14 | 55 | NIOME | 61.9 | 0.85 | 64.87 | 540 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 6.3d ago |
| 15 | 51 | lium.io | 61.7 | 0.85 | 70.52 | 1,263 | rtx4090 | 0.000 | 45 | 82% | SCORING_COMMIT 0.8d ago |
| 16 | 60 | Bitsec.ai | 61.4 | 0.85 | 777 | 1,088 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 17 | 81 | Reliquary | 60.9 | 0.85 | 48.71 | 209 | rtx4090 | 0.002 | 53 | 5% | SCORING_COMMIT 1.3d ago |
| 18 | 28 | gm | 60.3 | 0.85 | 42.14 | 1,661 | rtx4090 | 0.128 | 52 | 15% | RELEASE 0.6d ago |
| 19 | 53 | engy | 60.1 | 0.85 | 37.60 | 248 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.5d ago |
| 20 | 102 | ConnitoAI | 57.6 | 0.85 | 633 | 1,546 | rtx4090 | 0.250 | 7 | 26% | RELEASE 20d ago |
| 21 | 68 | NOVA | 55.2 | 0.6 | 8,628 | 8,628 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.6d ago |
| 22 | 120 | Affine | 54.8 | 0.6 | 7,308 | 7,308 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.3d ago |
| 23 | 124 | Swarm | 54.6 | 0.85 | 268 | 781 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 10d ago |
| 24 | 41 | Almanac | 54.6 | 1.0 | 9.62 | 24.01 | cpu-small | 0.738 | 75 | 74% | SCORING_COMMIT 8d ago |
| 25 | 80 | OpenRoboto | 53.8 | 0.85 | 204 | 736 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 13d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.40 | cpu-small | 4.909081066700852 |
| 54 | Yanez | -3.17 | a4000 | 1114.6093235108053 |
| 13 | Data Universe | -3.17 | rtx4090 | 6.132909289224629 |
| 18 | Zeus | -5.08 | rtx4090 | 1149.2735553691393 |
| 123 | MANTIS | -5.62 | rtx4090 | 100.8148811902979 |
| 75 | Hippius | -6.14 | rtx4090 | 11712.235628478193 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 128.0162827437436 |
| 34 | BitMind | -19.59 | a100-80 | 3139.081352148598 |
| 6 | Numinous | -0.93 | cpu-small | 366.1922446647126 |
| 104 | Masx.ai | -2.22 | rtx4090 | 8.760205772997507 |
| 88 | Investing | -4.00 | rtx4090 | 930.5444828105292 |
| 8 | Vanta | -7.40 | rtx4090 | 3243.8919258203514 |
| 43 | Graphite | -0.78 | cpu-small | 26.02665500602835 |
| 19 | blockmachine | -0.89 | rtx4090 | 1539.106659278603 |
| 45 | AlphaRidge.ai | -4.31 | rtx4090 | 13.163706452819804 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08060961658121896 |
| 105 | Beam | -2.29 | rtx4090 | 77.692491958095 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06607832323802922 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.18 | 35.0 | 15.0 | 9.91 | 1.0 |
| 23 | 24.92 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 12.09 | 35.0 | 15.0 | 8.54 | 1.0 |
| 67 | 10.51 | 35.0 | 15.0 | 9.62 | 1.0 |
| 56 | 25.81 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.44 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 23.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.94 | 35.0 | 15.0 | 9.65 | 0.85 |
| 96 | 11.76 | 35.0 | 11.25 | 9.61 | 1.0 |
| 26 | 11.54 | 35.0 | 11.25 | 9.59 | 1.0 |
| 107 | 19.66 | 21.0 | 15.0 | 9.5 | 1.0 |
| 85 | 20.16 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 19.08 | 35.0 | 11.25 | 9.97 | 0.85 |
| 55 | 16.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.87 | 35.0 | 11.25 | 9.49 | 0.85 |
| 60 | 26.29 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 15.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.87 | 35.0 | 11.25 | 9.83 | 0.85 |
| 53 | 14.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 25.49 | 21.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.8 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.14 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.1 | 21.0 | 11.25 | 9.87 | 0.85 |
| 41 | 9.33 | 21.0 | 15.0 | 9.25 | 1.0 |
| 80 | 21.03 | 21.0 | 11.25 | 10.0 | 0.85 |
