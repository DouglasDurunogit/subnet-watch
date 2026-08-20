# RANKING - generated 2026-08-20T21:52:47Z, block 8888833

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 75.36 | 127 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.5d ago |
| 2 | 67 | Harnyx | 72.2 | 1.0 | 21.59 | 287 | cpu-small | 0.030 | 176 | 8% | SCORING_COMMIT 0.5d ago |
| 3 | 23 | Trishool | 72.0 | 0.85 | 523 | 523 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.7d ago |
| 4 | 15 | ORO | 70.1 | 1.0 | 19.32 | 18,858 | cpu-small | 0.000 | 82 | 92% | SCORING_COMMIT 2.1d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 679 | 1,037 | rtx4090 | 0.724 | 5 | 72% | SCORING_COMMIT 2.9d ago |
| 6 | 91 | cascade | 69.3 | 0.85 | 611 | 2,469 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.7d ago |
| 7 | 1 | Apex | 68.2 | 0.85 | 430 | 1,217 | rtx4090 | 0.529 | 5 | 53% | RELEASE 1.0d ago |
| 8 | 38 | ChronoLLM | 67.7 | 0.85 | 156 | 3,307 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.0d ago |
| 9 | 96 | Verathos | 67.4 | 1.0 | 17.74 | 381 | rtx4090 | 0.403 | 91 | 40% | RELEASE 2.2d ago |
| 10 | 11 | TrajectoryRL | 67.3 | 0.85 | 4,509 | 4,509 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 18d ago |
| 11 | 26 | Perturb | 67.3 | 1.0 | 17.30 | 249 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.8d ago |
| 12 | 85 | Vidaio | 65.1 | 0.85 | 173 | 1,480 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.6d ago |
| 13 | 107 | Minos | 64.7 | 1.0 | 129 | 36,659 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 120 | 177 | rtx4090 | 0.662 | 7 | 66% | SCORING_COMMIT 0.8d ago |
| 15 | 55 | NIOME | 61.8 | 0.85 | 62.85 | 521 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 6.1d ago |
| 16 | 51 | lium.io | 61.7 | 0.85 | 69.62 | 1,233 | rtx4090 | 0.000 | 47 | 82% | SCORING_COMMIT 0.6d ago |
| 17 | 28 | gm | 61.7 | 0.85 | 63.17 | 1,542 | rtx4090 | 0.123 | 53 | 14% | RELEASE 0.3d ago |
| 18 | 60 | Bitsec.ai | 61.2 | 0.85 | 731 | 1,023 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 19 | 81 | Reliquary | 60.8 | 0.85 | 47.39 | 195 | rtx4090 | 0.002 | 51 | 5% | SCORING_COMMIT 1.0d ago |
| 20 | 53 | engy | 60.1 | 0.85 | 37.90 | 250 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.3d ago |
| 21 | 102 | ConnitoAI | 59.5 | 0.85 | 1,130 | 1,898 | rtx4090 | 0.250 | 6 | 32% | RELEASE 20d ago |
| 22 | 41 | Almanac | 55.4 | 1.0 | 11.51 | 23.67 | cpu-small | 0.720 | 77 | 72% | SCORING_COMMIT 8d ago |
| 23 | 68 | NOVA | 55.2 | 0.6 | 8,474 | 8,474 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.3d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,187 | 7,187 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.1d ago |
| 25 | 124 | Swarm | 54.4 | 0.85 | 257 | 749 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.41 | cpu-small | 4.771129858590449 |
| 54 | Yanez | -3.58 | a4000 | 1093.844167407955 |
| 18 | Zeus | -3.71 | rtx4090 | 1631.6168524151703 |
| 13 | Data Universe | -4.31 | rtx4090 | 7.2843198364611315 |
| 123 | MANTIS | -5.72 | rtx4090 | 95.84761979500269 |
| 75 | Hippius | -5.96 | rtx4090 | 12729.947942888633 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 126.90052240026681 |
| 34 | BitMind | -19.36 | a100-80 | 3100.356550805446 |
| 6 | Numinous | -0.96 | cpu-small | 382.0018274771263 |
| 104 | Masx.ai | -0.88 | rtx4090 | 7.843895058397805 |
| 88 | Investing | -4.40 | rtx4090 | 967.1630211425461 |
| 8 | Vanta | -7.41 | rtx4090 | 3621.80101008955 |
| 43 | Graphite | -0.81 | cpu-small | 25.592980651573757 |
| 32 | ItsAI | -0.13 | rtx4090 | 11.410023009642257 |
| 22 | Desearch | -0.72 | rtx4090 | 111.53739524364562 |
| 19 | blockmachine | -1.04 | rtx4090 | 1507.687079023282 |
| 45 | AlphaRidge.ai | -5.34 | rtx4090 | 11.248284980322726 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07948665790954251 |
| 105 | Beam | -2.29 | rtx4090 | 78.15197683720976 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06509191501547336 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn2, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.12 | 35.0 | 15.0 | 9.91 | 1.0 |
| 67 | 12.31 | 35.0 | 15.0 | 9.86 | 1.0 |
| 23 | 24.73 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 11.89 | 35.0 | 15.0 | 8.23 | 1.0 |
| 56 | 25.76 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.35 | 35.0 | 11.25 | 9.98 | 0.85 |
| 1 | 23.96 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.97 | 35.0 | 15.0 | 9.66 | 0.85 |
| 96 | 11.58 | 35.0 | 11.25 | 9.6 | 1.0 |
| 11 | 33.24 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.48 | 35.0 | 11.25 | 9.59 | 1.0 |
| 85 | 20.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 107 | 19.21 | 21.0 | 15.0 | 9.45 | 1.0 |
| 108 | 18.95 | 35.0 | 11.25 | 9.97 | 0.85 |
| 55 | 16.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.82 | 35.0 | 11.25 | 9.49 | 0.85 |
| 28 | 16.44 | 35.0 | 11.25 | 9.89 | 0.85 |
| 60 | 26.05 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 15.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.46 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.77 | 21.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.98 | 21.0 | 15.0 | 9.38 | 1.0 |
| 68 | 35.73 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.08 | 35.0 | 11.25 | 9.98 | 0.6 |
| 124 | 21.93 | 21.0 | 11.25 | 9.86 | 0.85 |
