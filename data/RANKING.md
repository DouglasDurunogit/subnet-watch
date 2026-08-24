# RANKING - generated 2026-08-24T03:13:19Z, block 8912035

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 75.36 | 84.37 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.4d ago |
| 2 | 67 | Harnyx | 72.7 | 1.0 | 24.91 | 799 | cpu-small | 0.020 | 127 | 20% | SCORING_COMMIT 2.7d ago |
| 3 | 62 | Ridges | 72.4 | 0.85 | 1,503 | 3,072 | rtx4090 | 0.000 | 6 | 39% | RELEASE 5.2d ago |
| 4 | 23 | Trishool | 72.4 | 0.85 | 579 | 579 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 4.0d ago |
| 5 | 102 | ConnitoAI | 71.8 | 0.85 | 1,280 | 2,569 | rtx4090 | 0.250 | 6 | 37% | RELEASE 0.3d ago |
| 6 | 15 | ORO | 71.5 | 1.0 | 26.78 | 45.71 | cpu-small | 0.000 | 81 | 92% | SCORING_COMMIT 2.2d ago |
| 7 | 56 | Gradients | 69.9 | 0.85 | 711 | 1,122 | rtx4090 | 0.731 | 5 | 73% | SCORING_COMMIT 6.1d ago |
| 8 | 91 | cascade | 69.8 | 0.85 | 706 | 2,849 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 3.2d ago |
| 9 | 1 | Apex | 68.8 | 0.85 | 518 | 1,153 | rtx4090 | 0.544 | 5 | 54% | RELEASE 2.5d ago |
| 10 | 96 | Verathos | 67.7 | 1.0 | 20.21 | 266 | rtx4090 | 0.403 | 94 | 40% | RELEASE 5.5d ago |
| 11 | 11 | TrajectoryRL | 67.6 | 0.85 | 4,790 | 4,790 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 22d ago |
| 12 | 26 | Perturb | 67.6 | 1.0 | 18.86 | 269 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 4.1d ago |
| 13 | 124 | Swarm | 66.9 | 0.85 | 300 | 2,606 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.6d ago |
| 14 | 38 | ChronoLLM | 66.6 | 0.85 | 119 | 1,618 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.3d ago |
| 15 | 108 | Prometheon | 65.4 | 0.85 | 187 | 191 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.6d ago |
| 16 | 107 | Minos | 65.4 | 1.0 | 153 | 44,080 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 14d ago |
| 17 | 85 | Vidaio | 64.3 | 0.85 | 134 | 426 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.8d ago |
| 18 | 60 | Bitsec.ai | 64.1 | 0.85 | 1,713 | 1,713 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 16d ago |
| 19 | 81 | Reliquary | 63.7 | 0.85 | 114 | 235 | rtx4090 | 0.003 | 38 | 5% | SCORING_COMMIT 1.4d ago |
| 20 | 51 | lium.io | 61.4 | 0.85 | 65.06 | 2,121 | rtx4090 | 0.000 | 53 | 72% | SCORING_COMMIT 3.8d ago |
| 21 | 53 | engy | 60.2 | 0.85 | 38.70 | 327 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.0d ago |
| 22 | 28 | gm | 59.0 | 0.85 | 28.67 | 2,098 | rtx4090 | 0.176 | 53 | 18% | RELEASE 3.5d ago |
| 23 | 61 | RedTeam | 56.8 | 0.85 | 13.39 | 305 | rtx4090 | 0.000 | 83 | 6% | RELEASE 1.8d ago |
| 24 | 41 | Almanac | 56.3 | 1.0 | 14.64 | 29.84 | cpu-small | 0.653 | 81 | 65% | SCORING_COMMIT 11d ago |
| 25 | 120 | Affine | 54.9 | 0.6 | 7,455 | 7,455 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.26 | cpu-small | 6.039850731572833 |
| 54 | Yanez | -3.36 | a4000 | 1175.6792958054805 |
| 13 | Data Universe | -2.40 | rtx4090 | 7.801380252510069 |
| 18 | Zeus | -3.99 | rtx4090 | 1342.1058698992013 |
| 89 | InfiniteQuant | -4.12 | rtx4090 | 114.92147060276663 |
| 123 | MANTIS | -5.61 | rtx4090 | 121.21053650210969 |
| 75 | Hippius | -5.98 | rtx4090 | 12577.880455369199 |
| 34 | BitMind | -16.31 | a100-80 | 340.0499311719752 |
| 6 | Numinous | -0.96 | cpu-small | 179.9286442594459 |
| 50 | Synth | -0.93 | rtx4090 | 67.25372713572229 |
| 104 | Masx.ai | -1.88 | rtx4090 | 10.54302087839525 |
| 88 | Investing | -2.75 | rtx4090 | 650.8585038514551 |
| 2 | DSperse | -3.72 | rtx4090 | 358.56212352764203 |
| 8 | Vanta | -7.34 | rtx4090 | 3315.9175239560604 |
| 43 | Graphite | -0.26 | cpu-small | 194.3886631088547 |
| 19 | blockmachine | -0.47 | rtx4090 | 675.9270749119078 |
| 22 | Desearch | -0.65 | rtx4090 | 56.71555664372972 |
| 45 | AlphaRidge.ai | -4.73 | rtx4090 | 11.071106991822164 |
| 63 | Enigma | -8.13 | rtx4090 | 0.0857998023509544 |
| 105 | Beam | -1.41 | rtx4090 | 88.554953070588 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.13 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.86 | 35.0 | 15.0 | 9.85 | 1.0 |
| 62 | 28.9 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.13 | 35.0 | 15.0 | 9.99 | 0.85 |
| 102 | 28.26 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 13.13 | 35.0 | 15.0 | 8.35 | 1.0 |
| 56 | 25.95 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.92 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.69 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.07 | 35.0 | 11.25 | 9.4 | 1.0 |
| 11 | 33.47 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.81 | 35.0 | 11.25 | 9.58 | 1.0 |
| 124 | 22.54 | 35.0 | 11.25 | 9.87 | 0.85 |
| 38 | 18.89 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.68 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.89 | 21.0 | 15.0 | 9.49 | 1.0 |
| 85 | 19.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 29.41 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 18.73 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.55 | 35.0 | 11.25 | 9.4 | 0.85 |
| 53 | 14.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.39 | 35.0 | 11.25 | 9.73 | 0.85 |
| 61 | 10.53 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 10.86 | 21.0 | 15.0 | 9.46 | 1.0 |
| 120 | 35.22 | 35.0 | 11.25 | 9.99 | 0.6 |
