# RANKING - generated 2026-08-04T12:25:10Z, block 8770807

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
| 1 | 23 | Trishool | 84.9 | 1.0 | 542 | 542 | cpu-small | 0.000 | 5 | 20% | SCORING_COMMIT 5.9d ago |
| 2 | 107 | Minos | 77.4 | 1.0 | 95.44 | 28,363 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 0.3d ago |
| 3 | 76 | Phylax | 77.3 | 1.0 | 78.03 | 157 | cpu-small | 0.000 | 7 | 67% | SCORING_COMMIT 1.8d ago |
| 4 | 67 | Harnyx | 71.8 | 1.0 | 20.69 | 698 | cpu-small | 0.032 | 151 | 17% | SCORING_COMMIT 0.3d ago |
| 5 | 62 | Ridges | 69.7 | 0.85 | 679 | 2,453 | rtx4090 | 0.015 | 7 | 39% | RELEASE 4.5d ago |
| 6 | 102 | ConnitoAI | 69.0 | 0.85 | 549 | 1,065 | rtx4090 | 0.251 | 5 | 36% | RELEASE 3.5d ago |
| 7 | 26 | Perturb | 68.5 | 1.0 | 22.88 | 189 | rtx3060 | 0.501 | 11 | 50% | README_TASK_DIFF 4.8d ago |
| 8 | 56 | Gradients | 67.2 | 0.85 | 322 | 938 | rtx4090 | 0.707 | 7 | 71% | SCORING_COMMIT 6.6d ago |
| 9 | 15 | ORO | 67.1 | 1.0 | 8.06 | 10,530 | cpu-small | 0.000 | 71 | 94% | RELEASE 3.8d ago |
| 10 | 124 | Swarm | 66.1 | 0.85 | 236 | 692 | rtx4090 | 0.000 | 21 | 12% | SCORING_COMMIT 2.9d ago |
| 11 | 74 | Gittensor | 65.9 | 0.85 | 221 | 361 | rtx4090 | 0.000 | 8 | 18% | RELEASE 3.6d ago |
| 12 | 38 | ChronoLLM | 65.4 | 0.85 | 198 | 3,342 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 5.1d ago |
| 13 | 41 | Almanac | 65.4 | 1.0 | 4.55 | 66.56 | cpu-small | 0.891 | 36 | 89% | SCORING_COMMIT 1.3d ago |
| 14 | 21 | AdTAO | 65.2 | 1.0 | 4.39 | 20.52 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.9d ago |
| 15 | 53 | engy | 64.2 | 0.85 | 132 | 3,081 | rtx4090 | 0.000 | 28 | 17% | SCORING_COMMIT 5.8d ago |
| 16 | 80 | OpenRoboto | 62.3 | 0.85 | 73.33 | 277 | rtx4090 | 0.910 | 4 | 91% | SCORING_COMMIT 4.2d ago |
| 17 | 61 | RedTeam | 58.3 | 0.85 | 21.91 | 77.23 | rtx4090 | 0.000 | 96 | 3% | RELEASE 0.5d ago |
| 18 | 28 | gm | 56.6 | 0.85 | 14.27 | 2,691 | rtx4090 | 0.559 | 18 | 56% | RELEASE 0.9d ago |
| 19 | 9 | iota | 55.2 | 0.6 | 8,687 | 8,687 | rtx4090 | 0.510 | 3 | 51% | RELEASE 3.8d ago |
| 20 | 97 | Albedo | 52.6 | 0.6 | 2,911 | 2,911 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.5d ago |
| 21 | 85 | Vidaio | 52.0 | 0.85 | 118 | 467 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 7d ago |
| 22 | 101 | Tag101 | 50.1 | 1.0 | 0.02 | 1.03 | cpu-small | 0.893 | 242 | 89% | SCORING_COMMIT 3.8d ago |
| 23 | 60 | Bitsec.ai | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.103 | 2 | 90% | SCORING_COMMIT 0.9d ago |
| 24 | 11 | TrajectoryRL | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 2.1d ago |
| 25 | 98 | NeverPlayAlone | 50.0 | 1.0 | n/a | n/a | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 4.8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.39 | a4000 | 856.1382063770109 |
| 50 | Synth | -0.62 | rtx4090 | 42.87519841179014 |
| 104 | Masx.ai | -1.70 | rtx4090 | 8.87607394811545 |
| 13 | Data Universe | -3.27 | rtx4090 | 5.063889295465644 |
| 8 | Vanta | -7.48 | rtx4090 | 2945.874763080462 |
| 114 | SOMA | -8.13 | rtx4090 | 1410.1201394962948 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 204.11446956611863 |
| 43 | Graphite | -0.71 | cpu-small | 12.163049636542008 |
| 32 | ItsAI | -0.21 | rtx4090 | 9.641359114964231 |
| 19 | blockmachine | -1.14 | rtx4090 | 51.66640727356116 |
| 5 | Hone | -2.72 | rtx4090 | 8.544352782841514 |
| 18 | Zeus | -3.23 | rtx4090 | 2497.169898761379 |
| 45 | AlphaRidge.ai | -3.34 | rtx4090 | 59.73362077343552 |
| 22 | Desearch | -4.66 | rtx4090 | 96.25947791704364 |
| 88 | Investing | -4.70 | rtx4090 | 552.3586252378111 |
| 75 | Hippius | -4.96 | rtx4090 | 9234.508889030916 |
| 123 | MANTIS | -6.08 | rtx4090 | 83.71523477574652 |
| 63 | Enigma | -8.15 | rtx4090 | 4666.155225074637 |
| 46 | Zipcode | -8.18 | rtx4090 | 0.07967535772123797 |
| 105 | Beam | -4.65 | rtx4090 | 198.96701567416778 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 35 subnets: sn6, sn10, sn12, sn14, sn20, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn103, sn108, sn109, sn111, sn113, sn120, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 23 | 24.87 | 35.0 | 15.0 | 9.99 | 1.0 |
| 107 | 18.05 | 35.0 | 15.0 | 9.34 | 1.0 |
| 76 | 17.26 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.15 | 35.0 | 15.0 | 9.66 | 1.0 |
| 62 | 25.76 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 24.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.53 | 35.0 | 11.25 | 9.72 | 1.0 |
| 56 | 22.82 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 8.71 | 35.0 | 15.0 | 8.4 | 1.0 |
| 124 | 21.6 | 35.0 | 11.25 | 9.87 | 0.85 |
| 74 | 21.34 | 35.0 | 11.25 | 9.96 | 0.85 |
| 38 | 20.92 | 35.0 | 11.25 | 9.76 | 0.85 |
| 41 | 6.77 | 35.0 | 15.0 | 8.6 | 1.0 |
| 21 | 6.65 | 35.0 | 15.0 | 8.55 | 1.0 |
| 53 | 19.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 80 | 17.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 12.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 10.77 | 35.0 | 11.25 | 9.55 | 0.85 |
| 9 | 35.83 | 35.0 | 11.25 | 10.0 | 0.6 |
| 97 | 31.51 | 35.0 | 11.25 | 9.99 | 0.6 |
| 85 | 18.87 | 21.0 | 11.25 | 10.0 | 0.85 |
| 101 | 0.09 | 35.0 | 15.0 | 0.0 | 1.0 |
| 60 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
| 11 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
| 98 | 0.0 | 35.0 | 15.0 | 0.0 | 1.0 |
