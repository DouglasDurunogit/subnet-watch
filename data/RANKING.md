# RANKING - generated 2026-08-05T23:43:10Z, block 8781396

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
| 1 | 76 | Phylax | 79.5 | 1.0 | 140 | 234 | cpu-small | 0.000 | 10 | 20% | SCORING_COMMIT 3.3d ago |
| 2 | 107 | Minos | 77.7 | 1.0 | 102 | 28,613 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 1.8d ago |
| 3 | 67 | Harnyx | 72.3 | 1.0 | 22.79 | 976 | cpu-small | 0.011 | 155 | 22% | SCORING_COMMIT 0.5d ago |
| 4 | 96 | Verathos | 72.0 | 1.0 | 54.74 | 241 | rtx4090 | 0.414 | 38 | 41% | RELEASE 0.1d ago |
| 5 | 114 | SOMA | 71.6 | 0.85 | 1,180 | 4,404 | rtx4090 | 0.000 | 4 | 65% | SCORING_COMMIT 1.5d ago |
| 6 | 91 | cascade | 70.1 | 0.85 | 771 | 3,110 | rtx4090 | 0.000 | 5 | 52% | RELEASE 0.8d ago |
| 7 | 62 | Ridges | 69.5 | 0.85 | 635 | 2,612 | rtx4090 | 0.133 | 7 | 35% | RELEASE 0.1d ago |
| 8 | 102 | ConnitoAI | 69.4 | 0.85 | 612 | 2,216 | rtx4090 | 0.250 | 7 | 34% | RELEASE 5.0d ago |
| 9 | 26 | Perturb | 68.9 | 1.0 | 25.01 | 203 | rtx3060 | 0.501 | 11 | 50% | README_TASK_DIFF 6.3d ago |
| 10 | 41 | Almanac | 68.4 | 1.0 | 9.11 | 65.88 | cpu-small | 0.782 | 60 | 78% | SCORING_COMMIT 2.8d ago |
| 11 | 15 | ORO | 67.0 | 1.0 | 8.51 | 19.07 | cpu-small | 0.000 | 76 | 93% | SCORING_COMMIT 0.0d ago |
| 12 | 74 | Gittensor | 66.1 | 0.85 | 236 | 257 | rtx4090 | 0.000 | 9 | 18% | RELEASE 5.1d ago |
| 13 | 124 | Swarm | 65.8 | 0.85 | 221 | 634 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 4.4d ago |
| 14 | 21 | AdTAO | 65.6 | 1.0 | 4.78 | 22.09 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.1d ago |
| 15 | 38 | ChronoLLM | 65.5 | 0.85 | 205 | 3,456 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 6.6d ago |
| 16 | 80 | OpenRoboto | 62.2 | 0.85 | 71.03 | 269 | rtx4090 | 0.909 | 4 | 91% | SCORING_COMMIT 5.6d ago |
| 17 | 61 | RedTeam | 62.0 | 0.85 | 66.49 | 171 | rtx4090 | 0.000 | 40 | 5% | RELEASE 0.5d ago |
| 18 | 2 | DSperse | 58.1 | 0.85 | 20.11 | 101 | rtx4090 | 0.826 | 13 | 83% | RELEASE 0.0d ago |
| 19 | 51 | lium.io | 57.5 | 0.85 | 24.46 | 5,114 | rtx4090 | 0.000 | 45 | 68% | SCORING_COMMIT 1.7d ago |
| 20 | 56 | Gradients | 56.5 | 0.85 | 463 | 976 | rtx4090 | 0.714 | 7 | 71% | SCORING_COMMIT 8d ago |
| 21 | 28 | gm | 56.0 | 0.85 | 12.16 | 6,159 | rtx4090 | 0.152 | 16 | 67% | RELEASE 2.4d ago |
| 22 | 120 | Affine | 55.1 | 0.6 | 8,291 | 8,291 | rtx4090 | 0.000 | 4 | 25% | SCORING_COMMIT 0.4d ago |
| 23 | 85 | Vidaio | 54.5 | 0.85 | 252 | 653 | rtx4090 | 0.000 | 10 | 20% | SCORING_COMMIT 9d ago |
| 24 | 101 | Tag101 | 54.4 | 1.0 | 0.01 | 0.79 | cpu-small | 0.902 | 246 | 90% | SCORING_COMMIT 5.3d ago |
| 25 | 97 | Albedo | 52.8 | 0.6 | 3,098 | 3,098 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.92 | a4000 | 969.1534092721292 |
| 50 | Synth | -0.71 | rtx4090 | 36.26165159682859 |
| 13 | Data Universe | -3.51 | rtx4090 | 8.910881004105539 |
| 88 | Investing | -5.89 | rtx4090 | 734.7863940899069 |
| 8 | Vanta | -7.46 | rtx4090 | 3093.110152594238 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 202.69386336498658 |
| 43 | Graphite | -0.60 | cpu-small | 12.278053590055201 |
| 19 | blockmachine | -2.05 | rtx4090 | 65.9869115370707 |
| 5 | Hone | -2.19 | rtx4090 | 6.277151264271675 |
| 18 | Zeus | -3.45 | rtx4090 | 2016.5898812643686 |
| 22 | Desearch | -3.66 | rtx4090 | 83.09977399497451 |
| 75 | Hippius | -4.83 | rtx4090 | 5.041912513568416 |
| 45 | AlphaRidge.ai | -4.97 | rtx4090 | 23.858675222201352 |
| 123 | MANTIS | -6.10 | rtx4090 | 83.4560314090818 |
| 63 | Enigma | -8.15 | rtx4090 | 0.07350533155106738 |
| 105 | Beam | -1.42 | rtx4090 | 225.27587952398707 |
| 84 | ansuz | -8.15 | rtx4090 | 498.59996256359585 |
| 34 | BitMind | -17.87 | a100-80 | 2915.744284175721 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 19.54 | 35.0 | 15.0 | 10.0 | 1.0 |
| 107 | 18.32 | 35.0 | 15.0 | 9.36 | 1.0 |
| 67 | 12.52 | 35.0 | 15.0 | 9.81 | 1.0 |
| 96 | 15.88 | 35.0 | 11.25 | 9.88 | 1.0 |
| 114 | 27.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.27 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 25.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 25.36 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.87 | 35.0 | 11.25 | 9.74 | 1.0 |
| 41 | 9.14 | 35.0 | 15.0 | 9.28 | 1.0 |
| 15 | 8.9 | 35.0 | 15.0 | 8.12 | 1.0 |
| 74 | 21.6 | 35.0 | 11.25 | 9.96 | 0.85 |
| 124 | 21.34 | 35.0 | 11.25 | 9.85 | 0.85 |
| 21 | 6.93 | 35.0 | 15.0 | 8.62 | 1.0 |
| 38 | 21.05 | 35.0 | 11.25 | 9.76 | 0.85 |
| 80 | 16.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 16.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 2 | 12.05 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.79 | 35.0 | 11.25 | 8.65 | 0.85 |
| 56 | 24.25 | 21.0 | 11.25 | 10.0 | 0.85 |
| 28 | 10.18 | 35.0 | 11.25 | 9.46 | 0.85 |
| 120 | 35.64 | 35.0 | 11.25 | 10.0 | 0.6 |
| 85 | 21.85 | 21.0 | 11.25 | 10.0 | 0.85 |
| 101 | 0.03 | 35.0 | 15.0 | 4.4 | 1.0 |
| 97 | 31.75 | 35.0 | 11.25 | 9.99 | 0.6 |
