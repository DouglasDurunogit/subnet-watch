# RANKING - generated 2026-08-05T14:53:30Z, block 8778748

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
| 1 | 76 | Phylax | 81.1 | 1.0 | 206 | 412 | cpu-small | 0.000 | 7 | 25% | SCORING_COMMIT 2.9d ago |
| 2 | 107 | Minos | 77.7 | 1.0 | 104 | 28,331 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 1.4d ago |
| 3 | 60 | Bitsec.ai | 76.8 | 0.85 | 2,163 | 2,163 | cpu-small | 0.102 | 2 | 90% | SCORING_COMMIT 2.0d ago |
| 4 | 98 | NeverPlayAlone | 76.0 | 0.85 | 1,709 | 1,709 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 5.9d ago |
| 5 | 67 | Harnyx | 72.1 | 1.0 | 22.43 | 961 | cpu-small | 0.011 | 155 | 22% | SCORING_COMMIT 0.1d ago |
| 6 | 91 | cascade | 70.1 | 0.85 | 764 | 3,080 | rtx4090 | 0.000 | 5 | 52% | RELEASE 0.4d ago |
| 7 | 102 | ConnitoAI | 69.9 | 0.85 | 724 | 1,622 | rtx4090 | 0.251 | 7 | 26% | RELEASE 4.7d ago |
| 8 | 62 | Ridges | 69.5 | 0.85 | 643 | 2,642 | rtx4090 | 0.133 | 7 | 35% | RELEASE 0.3d ago |
| 9 | 26 | Perturb | 68.8 | 1.0 | 24.92 | 203 | rtx3060 | 0.501 | 11 | 50% | README_TASK_DIFF 5.9d ago |
| 10 | 41 | Almanac | 68.5 | 1.0 | 9.19 | 66.66 | cpu-small | 0.782 | 60 | 78% | SCORING_COMMIT 2.4d ago |
| 11 | 15 | ORO | 66.6 | 1.0 | 8.69 | 10,758 | cpu-small | 0.000 | 75 | 93% | RELEASE 0.3d ago |
| 12 | 74 | Gittensor | 66.2 | 0.85 | 239 | 266 | rtx4090 | 0.000 | 9 | 18% | RELEASE 4.7d ago |
| 13 | 124 | Swarm | 65.8 | 0.85 | 222 | 636 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 4.0d ago |
| 14 | 38 | ChronoLLM | 65.6 | 0.85 | 210 | 3,524 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 6.2d ago |
| 15 | 21 | AdTAO | 65.6 | 1.0 | 4.82 | 22.22 | cpu-small | 0.451 | 142 | 45% | RELEASE 0.0d ago |
| 16 | 53 | engy | 62.3 | 0.85 | 72.77 | 1,598 | rtx4090 | 0.000 | 102 | 10% | SCORING_COMMIT 6.9d ago |
| 17 | 80 | OpenRoboto | 62.2 | 0.85 | 71.41 | 271 | rtx4090 | 0.909 | 4 | 91% | SCORING_COMMIT 5.3d ago |
| 18 | 61 | RedTeam | 58.6 | 0.85 | 23.56 | 104 | rtx4090 | 0.000 | 90 | 3% | RELEASE 0.1d ago |
| 19 | 101 | Tag101 | 58.6 | 1.0 | 0.04 | 0.74 | cpu-small | 0.902 | 247 | 90% | SCORING_COMMIT 4.9d ago |
| 20 | 51 | lium.io | 58.5 | 0.85 | 30.68 | 4,851 | rtx4090 | 0.000 | 47 | 71% | SCORING_COMMIT 1.3d ago |
| 21 | 28 | gm | 57.6 | 0.85 | 19.09 | 4,526 | rtx4090 | 0.399 | 16 | 48% | RELEASE 2.0d ago |
| 22 | 9 | iota | 56.0 | 0.6 | 11,834 | 11,834 | rtx4090 | 0.358 | 3 | 60% | RELEASE 4.9d ago |
| 23 | 56 | Gradients | 55.4 | 0.85 | 335 | 976 | rtx4090 | 0.714 | 7 | 71% | SCORING_COMMIT 8d ago |
| 24 | 120 | Affine | 55.1 | 0.6 | 8,347 | 8,347 | rtx4090 | 0.000 | 4 | 25% | SCORING_COMMIT 0.0d ago |
| 25 | 97 | Albedo | 52.8 | 0.6 | 3,094 | 3,094 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.6d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.12 | a4000 | 951.9073808799235 |
| 50 | Synth | -0.14 | rtx4090 | 36.72339299882877 |
| 104 | Masx.ai | -1.52 | rtx4090 | 8.53833865672036 |
| 13 | Data Universe | -3.51 | rtx4090 | 6.918058203701774 |
| 8 | Vanta | -7.46 | rtx4090 | 3109.2888307356616 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 261.69210777366703 |
| 43 | Graphite | -0.84 | cpu-small | 13.026324697666 |
| 45 | AlphaRidge.ai | -0.05 | rtx4090 | 67.1631857679789 |
| 19 | blockmachine | -1.07 | rtx4090 | 79.03793817504463 |
| 5 | Hone | -2.10 | rtx4090 | 7.494944592755516 |
| 18 | Zeus | -4.81 | rtx4090 | 1298.2601483436113 |
| 75 | Hippius | -4.82 | rtx4090 | 5.215381819703838 |
| 88 | Investing | -5.92 | rtx4090 | 725.6269835044085 |
| 123 | MANTIS | -6.08 | rtx4090 | 83.7686375930543 |
| 63 | Enigma | -8.15 | rtx4090 | 4797.9250217264835 |
| 105 | Beam | -2.78 | rtx4090 | 217.3325543964213 |
| 84 | ansuz | -8.15 | rtx4090 | 499.2204313174688 |
| 34 | BitMind | -16.32 | a100-80 | 24.775754885791958 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn36, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 21.06 | 35.0 | 15.0 | 10.0 | 1.0 |
| 107 | 18.37 | 35.0 | 15.0 | 9.37 | 1.0 |
| 60 | 30.34 | 35.0 | 15.0 | 10.0 | 0.85 |
| 98 | 29.4 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.46 | 35.0 | 15.0 | 9.69 | 1.0 |
| 91 | 26.23 | 35.0 | 11.25 | 9.99 | 0.85 |
| 102 | 26.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 25.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.86 | 35.0 | 11.25 | 9.74 | 1.0 |
| 41 | 9.17 | 35.0 | 15.0 | 9.28 | 1.0 |
| 15 | 8.97 | 35.0 | 15.0 | 7.65 | 1.0 |
| 74 | 21.65 | 35.0 | 11.25 | 9.94 | 0.85 |
| 124 | 21.35 | 35.0 | 11.25 | 9.85 | 0.85 |
| 38 | 21.13 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 6.95 | 35.0 | 15.0 | 8.63 | 1.0 |
| 53 | 16.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 80 | 16.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 12.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 101 | 0.17 | 35.0 | 15.0 | 8.46 | 1.0 |
| 51 | 13.65 | 35.0 | 11.25 | 8.93 | 0.85 |
| 28 | 11.85 | 35.0 | 11.25 | 9.66 | 0.85 |
| 9 | 37.05 | 35.0 | 11.25 | 10.0 | 0.6 |
| 56 | 22.98 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.67 | 35.0 | 11.25 | 9.99 | 0.6 |
| 97 | 31.75 | 35.0 | 11.25 | 9.99 | 0.6 |
