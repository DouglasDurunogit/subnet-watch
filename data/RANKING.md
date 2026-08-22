# RANKING - generated 2026-08-22T15:01:08Z, block 8901174

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
| 1 | 76 | Phylax | 77.2 | 1.0 | 78.15 | 131 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.2d ago |
| 2 | 102 | ConnitoAI | 72.8 | 0.85 | 1,719 | 1,719 | rtx4090 | 0.250 | 4 | 25% | RELEASE 0.9d ago |
| 3 | 67 | Harnyx | 72.2 | 1.0 | 22.59 | 440 | cpu-small | 0.058 | 148 | 12% | SCORING_COMMIT 1.2d ago |
| 4 | 62 | Ridges | 71.6 | 0.85 | 1,194 | 2,941 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.7d ago |
| 5 | 56 | Gradients | 69.9 | 0.85 | 720 | 1,058 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.6d ago |
| 6 | 91 | cascade | 69.7 | 0.85 | 684 | 2,761 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.7d ago |
| 7 | 15 | ORO | 69.5 | 1.0 | 17.71 | 36.76 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.6d ago |
| 8 | 1 | Apex | 68.5 | 0.85 | 467 | 1,099 | rtx4090 | 0.553 | 5 | 55% | RELEASE 1.0d ago |
| 9 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,524 | 4,524 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.59 | 253 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.5d ago |
| 11 | 96 | Verathos | 66.8 | 1.0 | 15.15 | 463 | rtx4090 | 0.405 | 92 | 41% | RELEASE 4.0d ago |
| 12 | 38 | ChronoLLM | 66.5 | 0.85 | 112 | 1,531 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.7d ago |
| 13 | 107 | Minos | 64.8 | 1.0 | 132 | 43,461 | cpu-small | 0.000 | 19 | 91% | README_TASK_DIFF 12d ago |
| 14 | 85 | Vidaio | 64.2 | 0.85 | 129 | 401 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.3d ago |
| 15 | 108 | Prometheon | 63.8 | 0.85 | 117 | 127 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.0d ago |
| 16 | 81 | Reliquary | 63.8 | 0.85 | 116 | 212 | rtx4090 | 0.004 | 39 | 5% | SCORING_COMMIT 1.1d ago |
| 17 | 51 | lium.io | 61.1 | 0.85 | 60.57 | 4,440 | rtx4090 | 0.000 | 55 | 67% | SCORING_COMMIT 2.3d ago |
| 18 | 28 | gm | 59.9 | 0.85 | 37.28 | 1,660 | rtx4090 | 0.000 | 55 | 15% | RELEASE 2.0d ago |
| 19 | 60 | Bitsec.ai | 59.7 | 0.85 | 463 | 463 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 20 | 53 | engy | 59.6 | 0.85 | 32.13 | 218 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.4d ago |
| 21 | 61 | RedTeam | 57.8 | 0.85 | 18.71 | 273 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.3d ago |
| 22 | 68 | NOVA | 55.2 | 0.6 | 8,633 | 8,633 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.1d ago |
| 23 | 41 | Almanac | 55.2 | 1.0 | 11.22 | 23.52 | cpu-small | 0.729 | 78 | 73% | SCORING_COMMIT 10d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,150 | 7,150 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.8d ago |
| 25 | 124 | Swarm | 54.6 | 0.85 | 266 | 2,323 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.01 | cpu-small | 857.7839342576276 |
| 54 | Yanez | -3.64 | a4000 | 1150.3909361414378 |
| 89 | InfiniteQuant | -2.30 | rtx4090 | 117.82707289443307 |
| 13 | Data Universe | -2.99 | rtx4090 | 6.487117801254909 |
| 18 | Zeus | -3.60 | rtx4090 | 2076.0838445618847 |
| 123 | MANTIS | -5.60 | rtx4090 | 107.22763767953423 |
| 75 | Hippius | -6.29 | rtx4090 | 11332.449933369795 |
| 34 | BitMind | -19.40 | a100-80 | 319.78594114942524 |
| 101 | Tag101 | -0.02 | cpu-small | 2.3359521477396337 |
| 6 | Numinous | -0.93 | cpu-small | 335.99746901413477 |
| 50 | Synth | -1.25 | rtx4090 | 91.83534633845196 |
| 104 | Masx.ai | -1.32 | rtx4090 | 12.578618572761256 |
| 88 | Investing | -3.36 | rtx4090 | 667.3470053238484 |
| 8 | Vanta | -7.39 | rtx4090 | 1067.5994715547429 |
| 43 | Graphite | -0.46 | cpu-small | 189.28233649514846 |
| 32 | ItsAI | -0.06 | rtx4090 | 10.719579350907338 |
| 19 | blockmachine | -1.50 | rtx4090 | 533.4560030374911 |
| 22 | Desearch | -4.83 | rtx4090 | 101.44530976908285 |
| 45 | AlphaRidge.ai | -4.95 | rtx4090 | 12.960979215540474 |
| 63 | Enigma | -8.14 | rtx4090 | 5359.521205877501 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.27 | 35.0 | 15.0 | 9.91 | 1.0 |
| 102 | 29.43 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.49 | 35.0 | 15.0 | 9.72 | 1.0 |
| 62 | 27.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 26.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.79 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 11.57 | 35.0 | 15.0 | 7.92 | 1.0 |
| 1 | 24.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.25 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.54 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 10.99 | 35.0 | 11.25 | 9.51 | 1.0 |
| 38 | 18.68 | 35.0 | 15.0 | 9.51 | 0.85 |
| 107 | 19.32 | 21.0 | 15.0 | 9.45 | 1.0 |
| 85 | 19.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.85 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.82 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.27 | 35.0 | 11.25 | 9.39 | 0.85 |
| 28 | 14.4 | 35.0 | 11.25 | 9.8 | 0.85 |
| 60 | 24.25 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.78 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.8 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.89 | 21.0 | 15.0 | 9.34 | 1.0 |
| 120 | 35.06 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.08 | 21.0 | 11.25 | 9.86 | 0.85 |
