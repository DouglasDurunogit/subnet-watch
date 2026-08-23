# RANKING - generated 2026-08-23T00:00:20Z, block 8903870

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 74.39 | 132 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.6d ago |
| 2 | 67 | Harnyx | 72.4 | 1.0 | 22.76 | 118 | cpu-small | 0.027 | 157 | 12% | SCORING_COMMIT 1.6d ago |
| 3 | 62 | Ridges | 71.6 | 0.85 | 1,205 | 2,966 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.0d ago |
| 4 | 102 | ConnitoAI | 71.5 | 0.85 | 1,150 | 2,662 | rtx4090 | 0.250 | 6 | 38% | RELEASE 1.3d ago |
| 5 | 15 | ORO | 70.5 | 1.0 | 19.14 | 22,799 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 1.0d ago |
| 6 | 56 | Gradients | 69.9 | 0.85 | 722 | 1,067 | rtx4090 | 0.729 | 5 | 73% | SCORING_COMMIT 5.0d ago |
| 7 | 91 | cascade | 69.8 | 0.85 | 690 | 2,783 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.0d ago |
| 8 | 1 | Apex | 68.6 | 0.85 | 493 | 1,234 | rtx4090 | 0.521 | 5 | 52% | RELEASE 1.4d ago |
| 9 | 96 | Verathos | 67.6 | 1.0 | 18.73 | 445 | rtx4090 | 0.403 | 92 | 40% | RELEASE 4.3d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.78 | 255 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.9d ago |
| 11 | 38 | ChronoLLM | 66.5 | 0.85 | 113 | 1,549 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.1d ago |
| 12 | 107 | Minos | 65.2 | 1.0 | 144 | 42,704 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 13 | 98 | NeverPlayAlone | 64.5 | 0.85 | 1,904 | 1,904 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 16d ago |
| 14 | 85 | Vidaio | 64.1 | 0.85 | 128 | 401 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.7d ago |
| 15 | 108 | Prometheon | 63.8 | 0.85 | 118 | 127 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.4d ago |
| 16 | 81 | Reliquary | 63.3 | 0.85 | 99.03 | 193 | rtx4090 | 0.036 | 44 | 5% | SCORING_COMMIT 0.3d ago |
| 17 | 51 | lium.io | 62.3 | 0.85 | 83.10 | 4,723 | rtx4090 | 0.000 | 50 | 70% | SCORING_COMMIT 2.7d ago |
| 18 | 60 | Bitsec.ai | 59.8 | 0.85 | 471 | 471 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 19 | 53 | engy | 59.7 | 0.85 | 33.17 | 224 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.8d ago |
| 20 | 28 | gm | 59.1 | 0.85 | 29.47 | 1,635 | rtx4090 | 0.150 | 53 | 15% | RELEASE 2.4d ago |
| 21 | 61 | RedTeam | 57.5 | 0.85 | 17.10 | 282 | rtx4090 | 0.000 | 87 | 6% | RELEASE 0.7d ago |
| 22 | 68 | NOVA | 55.2 | 0.6 | 8,667 | 8,667 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.4d ago |
| 23 | 41 | Almanac | 55.2 | 1.0 | 11.21 | 23.66 | cpu-small | 0.730 | 78 | 73% | SCORING_COMMIT 10d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,091 | 7,091 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.1d ago |
| 25 | 124 | Swarm | 54.6 | 0.85 | 270 | 2,350 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.31 | cpu-small | 5.64958495664631 |
| 54 | Yanez | -3.24 | a4000 | 1215.2283639129182 |
| 13 | Data Universe | -2.48 | rtx4090 | 6.782621529501127 |
| 89 | InfiniteQuant | -3.38 | rtx4090 | 115.98602817078795 |
| 18 | Zeus | -3.62 | rtx4090 | 1767.0315398284088 |
| 123 | MANTIS | -5.70 | rtx4090 | 106.62484593270442 |
| 75 | Hippius | -6.44 | rtx4090 | 11496.361624537813 |
| 34 | BitMind | -19.01 | a100-80 | 322.5807381201692 |
| 6 | Numinous | -0.94 | cpu-small | 286.64197766972705 |
| 104 | Masx.ai | -0.52 | rtx4090 | 8.880131360182862 |
| 50 | Synth | -1.98 | rtx4090 | 55.740035806671926 |
| 88 | Investing | -3.34 | rtx4090 | 670.3303437786747 |
| 8 | Vanta | -7.38 | rtx4090 | 1077.5493283338308 |
| 43 | Graphite | -0.47 | cpu-small | 187.41481804085447 |
| 19 | blockmachine | -1.10 | rtx4090 | 543.5137361805357 |
| 22 | Desearch | -3.58 | rtx4090 | 78.56909975604712 |
| 45 | AlphaRidge.ai | -5.13 | rtx4090 | 9.107230020937548 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08250951976580559 |
| 105 | Beam | -2.30 | rtx4090 | 78.16812527532933 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06936300953325393 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.07 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.51 | 35.0 | 15.0 | 9.84 | 1.0 |
| 62 | 28.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.84 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.86 | 35.0 | 15.0 | 8.62 | 1.0 |
| 56 | 26.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.82 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 11.78 | 35.0 | 11.25 | 9.6 | 1.0 |
| 26 | 11.58 | 35.0 | 11.25 | 9.58 | 1.0 |
| 38 | 18.72 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.67 | 21.0 | 15.0 | 9.49 | 1.0 |
| 98 | 29.83 | 21.0 | 15.0 | 10.0 | 0.85 |
| 85 | 19.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.87 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 17.51 | 35.0 | 11.25 | 9.55 | 0.85 |
| 60 | 24.32 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.95 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.5 | 35.0 | 11.25 | 9.75 | 0.85 |
| 61 | 11.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.82 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.88 | 21.0 | 15.0 | 9.34 | 1.0 |
| 120 | 35.02 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.12 | 21.0 | 11.25 | 9.86 | 0.85 |
