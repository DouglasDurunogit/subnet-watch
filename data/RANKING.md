# RANKING - generated 2026-08-10T11:18:39Z, block 8813672

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
| 1 | 107 | Minos | 78.3 | 1.0 | 118 | 32,662 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 6.3d ago |
| 2 | 76 | Phylax | 76.8 | 1.0 | 68.67 | 207 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.6d ago |
| 3 | 67 | Harnyx | 71.2 | 1.0 | 17.31 | 751 | cpu-small | 0.000 | 129 | 19% | SCORING_COMMIT 1.0d ago |
| 4 | 91 | cascade | 70.3 | 0.85 | 802 | 2,747 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.2d ago |
| 5 | 96 | Verathos | 70.3 | 1.0 | 36.03 | 270 | rtx4090 | 0.437 | 51 | 44% | RELEASE 0.1d ago |
| 6 | 1 | Apex | 69.8 | 0.85 | 691 | 1,591 | rtx4090 | 0.520 | 4 | 52% | RELEASE 2.6d ago |
| 7 | 41 | Almanac | 69.2 | 1.0 | 11.08 | 34.78 | cpu-small | 0.697 | 69 | 70% | SCORING_COMMIT 3.4d ago |
| 8 | 62 | Ridges | 69.0 | 0.85 | 548 | 1,983 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.6d ago |
| 9 | 26 | Perturb | 68.1 | 1.0 | 21.03 | 38.66 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 3.9d ago |
| 10 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,538 | 4,538 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 8d ago |
| 11 | 15 | ORO | 67.4 | 1.0 | 10.12 | 20.45 | cpu-small | 0.000 | 79 | 93% | RELEASE 4.0d ago |
| 12 | 38 | ChronoLLM | 65.7 | 0.85 | 216 | 3,632 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 2.1d ago |
| 13 | 21 | AdTAO | 65.4 | 1.0 | 4.69 | 21.82 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.9d ago |
| 14 | 80 | OpenRoboto | 64.7 | 0.85 | 152 | 553 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 2.3d ago |
| 15 | 28 | gm | 63.4 | 0.85 | 105 | 3,955 | rtx4090 | 0.263 | 26 | 40% | RELEASE 2.6d ago |
| 16 | 100 | BASE | 63.4 | 0.85 | 102 | 324 | rtx4090 | 0.000 | 8 | 50% | SCORING_COMMIT 1.6d ago |
| 17 | 61 | RedTeam | 63.1 | 0.85 | 94.24 | 391 | rtx4090 | 0.000 | 45 | 8% | RELEASE 0.1d ago |
| 18 | 51 | lium.io | 58.7 | 0.85 | 32.20 | 3,206 | rtx4090 | 0.000 | 52 | 55% | SCORING_COMMIT 2.6d ago |
| 19 | 6 | Numinous | 58.0 | 1.0 | 23.28 | 457 | cpu-small | 0.000 | 18 | 26% | README_TASK_DIFF 12d ago |
| 20 | 2 | DSperse | 57.0 | 0.85 | 14.39 | 115 | rtx4090 | 0.826 | 11 | 83% | RELEASE 4.3d ago |
| 21 | 120 | Affine | 54.7 | 0.6 | 7,053 | 7,053 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.0d ago |
| 22 | 85 | Vidaio | 54.6 | 0.85 | 262 | 676 | rtx4090 | 0.000 | 10 | 21% | SCORING_COMMIT 13d ago |
| 23 | 124 | Swarm | 53.9 | 0.85 | 220 | 675 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 9d ago |
| 24 | 53 | engy | 50.5 | 0.85 | 76.24 | 1,953 | rtx4090 | 0.000 | 103 | 10% | SCORING_COMMIT 12d ago |
| 25 | 60 | Bitsec.ai | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 2.7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.95 | a4000 | 1010.370507287278 |
| 104 | Masx.ai | -1.63 | rtx4090 | 8.15267061551564 |
| 13 | Data Universe | -3.44 | rtx4090 | 6.159660938497343 |
| 88 | Investing | -4.42 | rtx4090 | 601.8849896082409 |
| 56 | Gradients | -7.44 | rtx4090 | 1006.2906148301884 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 247.92975411612346 |
| 8 | Vanta | -7.40 | rtx4090 | 3348.61207592852 |
| 19 | blockmachine | -1.76 | rtx4090 | 261.9126226564207 |
| 18 | Zeus | -3.54 | rtx4090 | 1174.9783395272964 |
| 75 | Hippius | -4.30 | rtx4090 | 6.008460203831773 |
| 45 | AlphaRidge.ai | -5.83 | rtx4090 | 8.077355257264003 |
| 123 | MANTIS | -6.16 | rtx4090 | 73.69211049956914 |
| 63 | Enigma | -8.14 | rtx4090 | 4915.382508137741 |
| 105 | Beam | -4.74 | rtx4090 | 190.8205511074467 |
| 84 | ansuz | -8.15 | rtx4090 | 508.51117022405856 |
| 34 | BitMind | -19.05 | a100-80 | 295.87035102530723 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.87 | 35.0 | 15.0 | 9.43 | 1.0 |
| 76 | 16.76 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 11.48 | 35.0 | 15.0 | 9.73 | 1.0 |
| 91 | 26.42 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 14.27 | 35.0 | 11.25 | 9.81 | 1.0 |
| 1 | 25.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.84 | 35.0 | 15.0 | 9.39 | 1.0 |
| 62 | 24.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.21 | 35.0 | 11.25 | 9.68 | 1.0 |
| 11 | 33.26 | 21.0 | 15.0 | 10.0 | 0.85 |
| 15 | 9.52 | 35.0 | 15.0 | 7.9 | 1.0 |
| 38 | 21.26 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 6.86 | 35.0 | 15.0 | 8.55 | 1.0 |
| 80 | 19.87 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 18.41 | 35.0 | 11.25 | 9.94 | 0.85 |
| 100 | 18.32 | 35.0 | 11.25 | 9.99 | 0.85 |
| 61 | 18.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 13.83 | 35.0 | 11.25 | 8.95 | 0.85 |
| 6 | 12.6 | 21.0 | 15.0 | 9.42 | 1.0 |
| 2 | 10.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.0 | 35.0 | 11.25 | 9.99 | 0.6 |
| 85 | 22.0 | 21.0 | 11.25 | 10.0 | 0.85 |
| 124 | 21.33 | 21.0 | 11.25 | 9.85 | 0.85 |
| 53 | 17.17 | 21.0 | 11.25 | 10.0 | 0.85 |
| 60 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
