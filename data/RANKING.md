# RANKING - generated 2026-08-22T22:00:25Z, block 8903271

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 73.93 | 131 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.5d ago |
| 2 | 67 | Harnyx | 72.2 | 1.0 | 21.94 | 117 | cpu-small | 0.027 | 157 | 12% | SCORING_COMMIT 1.5d ago |
| 3 | 62 | Ridges | 71.6 | 0.85 | 1,192 | 2,936 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.0d ago |
| 4 | 102 | ConnitoAI | 71.4 | 0.85 | 1,138 | 2,635 | rtx4090 | 0.250 | 6 | 38% | RELEASE 1.2d ago |
| 5 | 15 | ORO | 70.4 | 1.0 | 18.86 | 22,489 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.9d ago |
| 6 | 56 | Gradients | 69.9 | 0.85 | 715 | 1,056 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.9d ago |
| 7 | 91 | cascade | 69.8 | 0.85 | 690 | 2,785 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.0d ago |
| 8 | 1 | Apex | 68.6 | 0.85 | 482 | 1,232 | rtx4090 | 0.521 | 5 | 52% | RELEASE 1.3d ago |
| 9 | 96 | Verathos | 67.4 | 1.0 | 17.77 | 432 | rtx4090 | 0.403 | 92 | 40% | RELEASE 4.2d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.57 | 253 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.8d ago |
| 11 | 38 | ChronoLLM | 66.5 | 0.85 | 113 | 1,540 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.0d ago |
| 12 | 107 | Minos | 64.5 | 1.0 | 125 | 42,753 | cpu-small | 0.000 | 19 | 91% | README_TASK_DIFF 12d ago |
| 13 | 85 | Vidaio | 64.4 | 0.85 | 141 | 397 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.6d ago |
| 14 | 108 | Prometheon | 63.8 | 0.85 | 116 | 126 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.3d ago |
| 15 | 81 | Reliquary | 63.5 | 0.85 | 106 | 230 | rtx4090 | 0.002 | 43 | 6% | SCORING_COMMIT 0.2d ago |
| 16 | 51 | lium.io | 61.6 | 0.85 | 68.94 | 4,672 | rtx4090 | 0.000 | 51 | 69% | SCORING_COMMIT 2.6d ago |
| 17 | 60 | Bitsec.ai | 59.8 | 0.85 | 473 | 473 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 18 | 28 | gm | 59.3 | 0.85 | 31.72 | 1,392 | rtx4090 | 0.106 | 55 | 13% | RELEASE 2.3d ago |
| 19 | 53 | engy | 59.3 | 0.85 | 29.39 | 202 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.7d ago |
| 20 | 61 | RedTeam | 57.6 | 0.85 | 17.21 | 276 | rtx4090 | 0.000 | 87 | 6% | RELEASE 0.6d ago |
| 21 | 68 | NOVA | 55.2 | 0.6 | 8,577 | 8,577 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.3d ago |
| 22 | 41 | Almanac | 55.1 | 1.0 | 10.94 | 23.41 | cpu-small | 0.733 | 78 | 73% | SCORING_COMMIT 10d ago |
| 23 | 120 | Affine | 54.7 | 0.6 | 7,013 | 7,013 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.1d ago |
| 24 | 124 | Swarm | 54.6 | 0.85 | 266 | 2,323 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |
| 25 | 80 | OpenRoboto | 53.7 | 0.85 | 199 | 717 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 15d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.31 | cpu-small | 5.635046604594848 |
| 54 | Yanez | -3.26 | a4000 | 1203.0651045785885 |
| 13 | Data Universe | -2.60 | rtx4090 | 6.719834345109969 |
| 89 | InfiniteQuant | -3.39 | rtx4090 | 115.0925338569374 |
| 18 | Zeus | -3.67 | rtx4090 | 1749.0273134474648 |
| 123 | MANTIS | -5.74 | rtx4090 | 104.77286083080531 |
| 75 | Hippius | -6.46 | rtx4090 | 11374.361513626998 |
| 34 | BitMind | -19.42 | a100-80 | 319.2439688031329 |
| 6 | Numinous | -0.94 | cpu-small | 283.62751773180423 |
| 104 | Masx.ai | -1.72 | rtx4090 | 7.577286197758233 |
| 50 | Synth | -1.94 | rtx4090 | 51.269618858048325 |
| 88 | Investing | -3.35 | rtx4090 | 667.9347404373559 |
| 8 | Vanta | -7.39 | rtx4090 | 1066.0503594709544 |
| 43 | Graphite | -0.49 | cpu-small | 181.8121569357931 |
| 19 | blockmachine | -1.17 | rtx4090 | 537.9033884020772 |
| 22 | Desearch | -2.96 | rtx4090 | 72.52502502028018 |
| 45 | AlphaRidge.ai | -5.37 | rtx4090 | 10.028310436550914 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08165780701226069 |
| 105 | Beam | -2.34 | rtx4090 | 77.54798939256504 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06865627210500093 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.05 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.37 | 35.0 | 15.0 | 9.84 | 1.0 |
| 62 | 27.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.81 | 35.0 | 15.0 | 8.62 | 1.0 |
| 56 | 25.97 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.83 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 11.58 | 35.0 | 11.25 | 9.59 | 1.0 |
| 26 | 11.54 | 35.0 | 11.25 | 9.58 | 1.0 |
| 38 | 18.7 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.1 | 21.0 | 15.0 | 9.42 | 1.0 |
| 85 | 19.57 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.82 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.45 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.78 | 35.0 | 11.25 | 9.47 | 0.85 |
| 60 | 24.34 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 13.78 | 35.0 | 11.25 | 9.77 | 0.85 |
| 53 | 13.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.46 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.77 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.8 | 21.0 | 15.0 | 9.33 | 1.0 |
| 120 | 34.98 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.07 | 21.0 | 11.25 | 9.86 | 0.85 |
| 80 | 20.92 | 21.0 | 11.25 | 10.0 | 0.85 |
