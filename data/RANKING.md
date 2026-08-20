# RANKING - generated 2026-08-20T10:15:45Z, block 8885348

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
| 1 | 76 | Phylax | 76.7 | 1.0 | 69.51 | 123 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.0d ago |
| 2 | 23 | Trishool | 72.1 | 0.85 | 534 | 534 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.3d ago |
| 3 | 67 | Harnyx | 71.9 | 1.0 | 20.70 | 366 | cpu-small | 0.082 | 166 | 10% | SCORING_COMMIT 0.0d ago |
| 4 | 15 | ORO | 70.3 | 1.0 | 18.56 | 18,461 | cpu-small | 0.000 | 81 | 92% | SCORING_COMMIT 1.6d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 669 | 1,018 | rtx4090 | 0.722 | 5 | 72% | SCORING_COMMIT 2.4d ago |
| 6 | 91 | cascade | 69.3 | 0.85 | 599 | 2,420 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.2d ago |
| 7 | 38 | ChronoLLM | 67.6 | 0.85 | 152 | 3,234 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.5d ago |
| 8 | 26 | Perturb | 67.2 | 1.0 | 16.93 | 245 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.3d ago |
| 9 | 1 | Apex | 66.1 | 0.85 | 234 | 1,813 | rtx4090 | 0.531 | 4 | 53% | RELEASE 0.6d ago |
| 10 | 96 | Verathos | 65.7 | 1.0 | 11.71 | 289 | rtx4090 | 0.403 | 96 | 40% | RELEASE 1.8d ago |
| 11 | 107 | Minos | 64.7 | 1.0 | 129 | 38,099 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 12 | 85 | Vidaio | 64.4 | 0.85 | 140 | 219 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.1d ago |
| 13 | 108 | Prometheon | 64.1 | 0.85 | 126 | 186 | rtx4090 | 0.659 | 7 | 66% | SCORING_COMMIT 0.3d ago |
| 14 | 60 | Bitsec.ai | 62.1 | 0.85 | 940 | 940 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 15 | 28 | gm | 62.0 | 0.85 | 68.71 | 2,427 | rtx4090 | 0.103 | 49 | 22% | RELEASE 0.8d ago |
| 16 | 55 | NIOME | 61.7 | 0.85 | 60.74 | 504 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 5.6d ago |
| 17 | 51 | lium.io | 61.3 | 0.85 | 62.59 | 1,213 | rtx4090 | 0.000 | 47 | 80% | SCORING_COMMIT 0.1d ago |
| 18 | 81 | Reliquary | 61.2 | 0.85 | 53.68 | 206 | rtx4090 | 0.002 | 54 | 5% | SCORING_COMMIT 0.5d ago |
| 19 | 53 | engy | 59.9 | 0.85 | 35.26 | 235 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 1.8d ago |
| 20 | 102 | ConnitoAI | 57.5 | 0.85 | 616 | 1,805 | rtx4090 | 0.250 | 7 | 30% | RELEASE 19d ago |
| 21 | 41 | Almanac | 55.4 | 1.0 | 11.53 | 24.29 | cpu-small | 0.717 | 76 | 72% | SCORING_COMMIT 7d ago |
| 22 | 68 | NOVA | 55.1 | 0.6 | 8,299 | 8,299 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 3.9d ago |
| 23 | 120 | Affine | 54.7 | 0.6 | 6,943 | 6,943 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.6d ago |
| 24 | 124 | Swarm | 54.4 | 0.85 | 256 | 747 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |
| 25 | 80 | OpenRoboto | 53.7 | 0.85 | 201 | 722 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 12d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.96 | cpu-small | 377.95451212598374 |
| 54 | Yanez | -3.49 | a4000 | 1085.9852681635025 |
| 123 | MANTIS | -5.78 | rtx4090 | 91.95104971505431 |
| 75 | Hippius | -6.11 | rtx4090 | 12411.848638205698 |
| 114 | SOMA | -8.12 | rtx4090 | 4245.753981900515 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 141.47640871476793 |
| 104 | Masx.ai | -2.13 | rtx4090 | 8.151458578758115 |
| 13 | Data Universe | -3.56 | rtx4090 | 5.357667939598412 |
| 88 | Investing | -4.25 | rtx4090 | 973.4448164316158 |
| 8 | Vanta | -7.95 | rtx4090 | 2918.532596743721 |
| 43 | Graphite | -0.79 | cpu-small | 25.269770486876375 |
| 18 | Zeus | -5.30 | rtx4090 | 1118.9016476049467 |
| 45 | AlphaRidge.ai | -5.51 | rtx4090 | 10.34433301068509 |
| 19 | blockmachine | -7.88 | rtx4090 | 69.83663337300148 |
| 63 | Enigma | -8.14 | rtx4090 | 5108.267848160512 |
| 105 | Beam | -2.41 | rtx4090 | 78.51788123487123 |
| 84 | ansuz | -8.16 | rtx4090 | 463.50306831285536 |
| 34 | BitMind | -19.94 | a100-80 | 29.12361262858181 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn78, sn87, sn92, sn94, sn95, sn109, sn111, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.81 | 35.0 | 15.0 | 9.9 | 1.0 |
| 23 | 24.81 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.15 | 35.0 | 15.0 | 9.78 | 1.0 |
| 15 | 11.75 | 35.0 | 15.0 | 8.56 | 1.0 |
| 56 | 25.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.27 | 35.0 | 11.25 | 9.99 | 0.85 |
| 38 | 19.88 | 35.0 | 15.0 | 9.66 | 0.85 |
| 26 | 11.4 | 35.0 | 11.25 | 9.59 | 1.0 |
| 1 | 21.56 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 10.04 | 35.0 | 11.25 | 9.4 | 1.0 |
| 107 | 19.22 | 21.0 | 15.0 | 9.46 | 1.0 |
| 85 | 19.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 19.15 | 35.0 | 11.25 | 9.97 | 0.85 |
| 60 | 27.04 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 16.76 | 35.0 | 11.25 | 9.9 | 0.85 |
| 55 | 16.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.4 | 35.0 | 11.25 | 9.44 | 0.85 |
| 81 | 15.81 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 25.38 | 21.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.99 | 21.0 | 15.0 | 9.39 | 1.0 |
| 68 | 35.64 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.94 | 35.0 | 11.25 | 9.98 | 0.6 |
| 124 | 21.93 | 21.0 | 11.25 | 9.83 | 0.85 |
| 80 | 20.96 | 21.0 | 11.25 | 10.0 | 0.85 |
