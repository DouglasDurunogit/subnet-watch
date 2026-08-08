# RANKING - generated 2026-08-08T21:55:29Z, block 8802456

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
| 1 | 11 | TrajectoryRL | 79.6 | 0.85 | 4,973 | 4,973 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.4d ago |
| 2 | 107 | Minos | 78.2 | 1.0 | 116 | 34,921 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 4.7d ago |
| 3 | 76 | Phylax | 76.6 | 1.0 | 65.59 | 198 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.0d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,217 | 1,217 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.1d ago |
| 5 | 67 | Harnyx | 71.3 | 1.0 | 17.13 | 744 | cpu-small | 0.017 | 142 | 19% | SCORING_COMMIT 1.8d ago |
| 6 | 91 | cascade | 70.2 | 0.85 | 787 | 2,695 | rtx4090 | 0.000 | 5 | 48% | RELEASE 3.7d ago |
| 7 | 1 | Apex | 69.5 | 0.85 | 639 | 1,585 | rtx4090 | 0.456 | 4 | 46% | RELEASE 1.1d ago |
| 8 | 62 | Ridges | 69.1 | 0.85 | 559 | 2,023 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.0d ago |
| 9 | 96 | Verathos | 68.3 | 1.0 | 21.83 | 170 | rtx4090 | 0.418 | 72 | 42% | RELEASE 0.2d ago |
| 10 | 26 | Perturb | 68.3 | 1.0 | 21.75 | 40.80 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 2.3d ago |
| 11 | 41 | Almanac | 68.3 | 1.0 | 8.81 | 44.89 | cpu-small | 0.760 | 66 | 76% | SCORING_COMMIT 1.9d ago |
| 12 | 15 | ORO | 67.6 | 1.0 | 9.19 | 19.36 | cpu-small | 0.000 | 70 | 94% | RELEASE 2.5d ago |
| 13 | 21 | AdTAO | 65.6 | 1.0 | 4.82 | 22.23 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.3d ago |
| 14 | 38 | ChronoLLM | 65.5 | 0.85 | 208 | 3,499 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.5d ago |
| 15 | 80 | OpenRoboto | 63.6 | 0.85 | 110 | 406 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 0.7d ago |
| 16 | 61 | RedTeam | 61.9 | 0.85 | 64.92 | 188 | rtx4090 | 0.000 | 42 | 6% | RELEASE 1.0d ago |
| 17 | 28 | gm | 61.4 | 0.85 | 57.86 | 3,793 | rtx4090 | 0.184 | 24 | 41% | RELEASE 1.0d ago |
| 18 | 51 | lium.io | 59.3 | 0.85 | 37.59 | 2,963 | rtx4090 | 0.000 | 47 | 67% | SCORING_COMMIT 1.1d ago |
| 19 | 85 | Vidaio | 57.0 | 0.85 | 535 | 574 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 12d ago |
| 20 | 56 | Gradients | 56.5 | 0.85 | 463 | 976 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 21 | 74 | Gittensor | 55.3 | 0.85 | 10.84 | 236 | rtx4090 | 0.631 | 16 | 63% | RELEASE 1.2d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 6,908 | 6,908 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.4d ago |
| 23 | 124 | Swarm | 53.8 | 0.85 | 211 | 644 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 7d ago |
| 24 | 100 | BASE | 53.0 | 0.6 | 3,313 | 3,313 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.0d ago |
| 25 | 97 | Albedo | 52.7 | 0.6 | 2,972 | 2,972 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 6.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.04 | a4000 | 1032.9863060927726 |
| 104 | Masx.ai | -1.50 | rtx4090 | 8.328697979440069 |
| 13 | Data Universe | -3.00 | rtx4090 | 7.3207887124303195 |
| 88 | Investing | -6.18 | rtx4090 | 381.8994978126071 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 128.6794285348577 |
| 8 | Vanta | -7.42 | rtx4090 | 3262.342515342047 |
| 19 | blockmachine | -1.18 | rtx4090 | 192.02391810394641 |
| 22 | Desearch | -2.36 | rtx4090 | 110.6618838891716 |
| 18 | Zeus | -3.40 | rtx4090 | 1396.8227501961685 |
| 45 | AlphaRidge.ai | -4.66 | rtx4090 | 14.325810412946812 |
| 75 | Hippius | -4.66 | rtx4090 | 5.294110103750232 |
| 123 | MANTIS | -6.25 | rtx4090 | 72.66899735547868 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07544962085137165 |
| 105 | Beam | -3.79 | rtx4090 | 207.1601686627534 |
| 84 | ansuz | -8.15 | rtx4090 | 498.6729775640323 |
| 34 | BitMind | -18.86 | a100-80 | 290.17227873781053 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.62 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.8 | 35.0 | 15.0 | 9.43 | 1.0 |
| 76 | 16.58 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.07 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.44 | 35.0 | 15.0 | 9.82 | 1.0 |
| 91 | 26.34 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 25.52 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 25.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.36 | 35.0 | 11.25 | 9.7 | 1.0 |
| 26 | 12.34 | 35.0 | 11.25 | 9.69 | 1.0 |
| 41 | 9.02 | 35.0 | 15.0 | 9.25 | 1.0 |
| 15 | 9.17 | 35.0 | 15.0 | 8.42 | 1.0 |
| 21 | 6.96 | 35.0 | 15.0 | 8.62 | 1.0 |
| 38 | 21.1 | 35.0 | 11.25 | 9.76 | 0.85 |
| 80 | 18.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 16.54 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.1 | 35.0 | 11.25 | 9.89 | 0.85 |
| 51 | 14.43 | 35.0 | 11.25 | 9.12 | 0.85 |
| 85 | 24.82 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.25 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.76 | 35.0 | 11.25 | 9.08 | 0.85 |
| 120 | 34.92 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.17 | 21.0 | 11.25 | 9.84 | 0.85 |
| 100 | 32.02 | 35.0 | 11.25 | 10.0 | 0.6 |
| 97 | 31.59 | 35.0 | 11.25 | 9.99 | 0.6 |
