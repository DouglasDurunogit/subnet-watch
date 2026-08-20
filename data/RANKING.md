# RANKING - generated 2026-08-20T23:08:22Z, block 8889211

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 75.66 | 127 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.6d ago |
| 2 | 67 | Harnyx | 72.1 | 1.0 | 21.74 | 288 | cpu-small | 0.034 | 173 | 8% | SCORING_COMMIT 0.6d ago |
| 3 | 23 | Trishool | 72.0 | 0.85 | 525 | 525 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.8d ago |
| 4 | 15 | ORO | 70.3 | 1.0 | 19.68 | 19,205 | cpu-small | 0.000 | 82 | 92% | SCORING_COMMIT 2.2d ago |
| 5 | 56 | Gradients | 69.7 | 0.85 | 681 | 1,042 | rtx4090 | 0.724 | 5 | 72% | SCORING_COMMIT 3.0d ago |
| 6 | 91 | cascade | 69.4 | 0.85 | 613 | 2,475 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 0.0d ago |
| 7 | 1 | Apex | 68.2 | 0.85 | 429 | 1,215 | rtx4090 | 0.532 | 5 | 53% | RELEASE 1.1d ago |
| 8 | 38 | ChronoLLM | 67.7 | 0.85 | 156 | 3,309 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.1d ago |
| 9 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,520 | 4,520 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 19d ago |
| 10 | 96 | Verathos | 67.4 | 1.0 | 17.68 | 368 | rtx4090 | 0.404 | 92 | 40% | RELEASE 2.3d ago |
| 11 | 26 | Perturb | 67.3 | 1.0 | 17.38 | 250 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.9d ago |
| 12 | 107 | Minos | 64.4 | 1.0 | 121 | 37,298 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 13 | 85 | Vidaio | 64.3 | 0.85 | 134 | 1,487 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.7d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 121 | 178 | rtx4090 | 0.662 | 7 | 66% | SCORING_COMMIT 0.9d ago |
| 15 | 51 | lium.io | 61.9 | 0.85 | 73.18 | 1,261 | rtx4090 | 0.000 | 46 | 82% | SCORING_COMMIT 0.6d ago |
| 16 | 55 | NIOME | 61.9 | 0.85 | 64.44 | 537 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 6.1d ago |
| 17 | 60 | Bitsec.ai | 61.3 | 0.85 | 740 | 1,036 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 18 | 81 | Reliquary | 60.8 | 0.85 | 46.97 | 192 | rtx4090 | 0.002 | 51 | 5% | SCORING_COMMIT 1.1d ago |
| 19 | 28 | gm | 60.7 | 0.85 | 47.14 | 1,415 | rtx4090 | 0.128 | 52 | 13% | RELEASE 0.4d ago |
| 20 | 53 | engy | 60.1 | 0.85 | 37.88 | 250 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.3d ago |
| 21 | 102 | ConnitoAI | 59.6 | 0.85 | 1,171 | 1,912 | rtx4090 | 0.250 | 6 | 32% | RELEASE 20d ago |
| 22 | 41 | Almanac | 55.3 | 1.0 | 11.42 | 23.77 | cpu-small | 0.723 | 77 | 72% | SCORING_COMMIT 8d ago |
| 23 | 68 | NOVA | 55.2 | 0.6 | 8,536 | 8,536 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.4d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,218 | 7,218 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.1d ago |
| 25 | 124 | Swarm | 54.4 | 0.85 | 259 | 756 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.41 | cpu-small | 4.789865534265151 |
| 54 | Yanez | -3.52 | a4000 | 1098.0344137722643 |
| 18 | Zeus | -3.67 | rtx4090 | 1646.0380459812145 |
| 13 | Data Universe | -4.04 | rtx4090 | 7.713959147106454 |
| 123 | MANTIS | -5.67 | rtx4090 | 98.07484269510789 |
| 75 | Hippius | -6.11 | rtx4090 | 11878.40769754608 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 127.3257917812437 |
| 34 | BitMind | -19.67 | a100-80 | 3112.8292863713996 |
| 6 | Numinous | -0.96 | cpu-small | 383.4737006688456 |
| 104 | Masx.ai | -1.69 | rtx4090 | 10.064452494916265 |
| 88 | Investing | -4.36 | rtx4090 | 978.5298280789506 |
| 8 | Vanta | -7.41 | rtx4090 | 3169.140063371287 |
| 43 | Graphite | -0.84 | cpu-small | 24.817944743759362 |
| 32 | ItsAI | -0.16 | rtx4090 | 11.548207047247171 |
| 19 | blockmachine | -1.02 | rtx4090 | 1512.3535844066039 |
| 22 | Desearch | -4.34 | rtx4090 | 143.23917359504182 |
| 45 | AlphaRidge.ai | -5.66 | rtx4090 | 10.114626581610958 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0798067056983442 |
| 105 | Beam | -2.41 | rtx4090 | 76.35650976706614 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06543359730253631 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.14 | 35.0 | 15.0 | 9.91 | 1.0 |
| 67 | 12.34 | 35.0 | 15.0 | 9.79 | 1.0 |
| 23 | 24.75 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 11.97 | 35.0 | 15.0 | 8.32 | 1.0 |
| 56 | 25.77 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.36 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 23.95 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 19.97 | 35.0 | 15.0 | 9.66 | 0.85 |
| 11 | 33.25 | 21.0 | 15.0 | 10.0 | 0.85 |
| 96 | 11.56 | 35.0 | 11.25 | 9.6 | 1.0 |
| 26 | 11.5 | 35.0 | 11.25 | 9.59 | 1.0 |
| 107 | 18.99 | 21.0 | 15.0 | 9.42 | 1.0 |
| 85 | 19.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.97 | 35.0 | 11.25 | 9.97 | 0.85 |
| 51 | 17.01 | 35.0 | 11.25 | 9.51 | 0.85 |
| 55 | 16.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.1 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 15.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.3 | 35.0 | 11.25 | 9.85 | 0.85 |
| 53 | 14.46 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.91 | 21.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.95 | 21.0 | 15.0 | 9.37 | 1.0 |
| 68 | 35.76 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.09 | 35.0 | 11.25 | 9.98 | 0.6 |
| 124 | 21.97 | 21.0 | 11.25 | 9.83 | 0.85 |
