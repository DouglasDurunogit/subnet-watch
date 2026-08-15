# RANKING - generated 2026-08-15T11:00:58Z, block 8849575

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
| 1 | 107 | Minos | 77.8 | 1.0 | 107 | 31,797 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 4.8d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.46 | 194 | cpu-small | 0.000 | 10 | 35% | SCORING_COMMIT 6.5d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.28 | 375 | cpu-small | 0.007 | 123 | 10% | SCORING_COMMIT 0.1d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.24 | 75.61 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.8d ago |
| 5 | 1 | Apex | 70.6 | 0.85 | 883 | 1,088 | rtx4090 | 0.553 | 4 | 55% | RELEASE 1.9d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.79 | 442 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 1.8d ago |
| 7 | 41 | Almanac | 69.6 | 1.0 | 12.06 | 53.63 | cpu-small | 0.661 | 72 | 66% | SCORING_COMMIT 2.5d ago |
| 8 | 96 | Verathos | 69.0 | 1.0 | 25.95 | 188 | rtx4090 | 0.409 | 64 | 41% | RELEASE 0.6d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 512 | 963 | rtx4090 | 0.667 | 7 | 67% | SCORING_COMMIT 2.9d ago |
| 10 | 91 | cascade | 68.6 | 0.85 | 486 | 1,117 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.5d ago |
| 11 | 62 | Ridges | 68.6 | 0.85 | 485 | 2,247 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.5d ago |
| 12 | 15 | ORO | 68.0 | 1.0 | 10.96 | 20.31 | cpu-small | 0.000 | 82 | 93% | SCORING_COMMIT 1.5d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.49 | 33.64 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.0d ago |
| 14 | 85 | Vidaio | 67.0 | 0.85 | 301 | 484 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 3.0d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.72 | 1,336 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.8d ago |
| 16 | 124 | Swarm | 65.8 | 0.85 | 222 | 718 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 3.8d ago |
| 17 | 28 | gm | 61.6 | 0.85 | 61.29 | 2,558 | rtx4090 | 0.123 | 31 | 29% | RELEASE 2.9d ago |
| 18 | 55 | NIOME | 61.4 | 0.85 | 56.31 | 476 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 0.6d ago |
| 19 | 60 | Bitsec.ai | 59.5 | 0.85 | 429 | 429 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 74 | Gittensor | 58.3 | 0.85 | 23.92 | 210 | rtx4090 | 0.631 | 15 | 63% | RELEASE 3.7d ago |
| 21 | 61 | RedTeam | 57.7 | 0.85 | 18.16 | 754 | rtx4090 | 0.000 | 70 | 18% | RELEASE 4.1d ago |
| 22 | 51 | lium.io | 57.4 | 0.85 | 23.72 | 1,840 | rtx4090 | 0.000 | 45 | 78% | SCORING_COMMIT 1.1d ago |
| 23 | 120 | Affine | 54.6 | 0.6 | 6,590 | 6,590 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.9d ago |
| 24 | 80 | OpenRoboto | 53.2 | 0.85 | 172 | 624 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 7d ago |
| 25 | 97 | Albedo | 52.5 | 0.6 | 2,783 | 2,783 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.39 | a4000 | 951.2191179914147 |
| 104 | Masx.ai | -0.21 | rtx4090 | 9.324786171784725 |
| 75 | Hippius | -7.21 | rtx4090 | 10911.130010130802 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 228.25048297022627 |
| 101 | Tag101 | -0.06 | cpu-small | 2.1082645723065205 |
| 13 | Data Universe | -3.67 | rtx4090 | 5.96067013761395 |
| 88 | Investing | -5.61 | rtx4090 | 872.5515956209058 |
| 8 | Vanta | -7.96 | rtx4090 | 2904.0274410887655 |
| 114 | SOMA | -8.12 | rtx4090 | 1569.2428456380094 |
| 43 | Graphite | -0.47 | cpu-small | 11.307790206626654 |
| 18 | Zeus | -3.82 | rtx4090 | 1545.477380509832 |
| 45 | AlphaRidge.ai | -3.96 | rtx4090 | 21.41280095046313 |
| 22 | Desearch | -4.95 | rtx4090 | 52.764379602125125 |
| 123 | MANTIS | -6.07 | rtx4090 | 79.10644363123238 |
| 63 | Enigma | -8.14 | rtx4090 | 4940.44051458927 |
| 105 | Beam | -2.63 | rtx4090 | 85.45487908897152 |
| 34 | BitMind | -19.30 | a100-80 | 20.469719507843283 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.5 | 35.0 | 15.0 | 9.3 | 1.0 |
| 76 | 14.71 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.6 | 35.0 | 15.0 | 9.91 | 1.0 |
| 26 | 14.79 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.14 | 35.0 | 15.0 | 9.17 | 1.0 |
| 41 | 10.15 | 35.0 | 15.0 | 9.45 | 1.0 |
| 96 | 13.01 | 35.0 | 11.25 | 9.75 | 1.0 |
| 56 | 24.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.44 | 35.0 | 11.25 | 9.99 | 0.85 |
| 62 | 24.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.8 | 35.0 | 15.0 | 8.17 | 1.0 |
| 21 | 8.45 | 35.0 | 15.0 | 9.12 | 1.0 |
| 85 | 22.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.14 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.36 | 35.0 | 11.25 | 9.85 | 0.85 |
| 28 | 16.32 | 35.0 | 11.25 | 9.89 | 0.85 |
| 55 | 15.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.95 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.7 | 35.0 | 11.25 | 9.59 | 0.85 |
| 61 | 11.66 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.67 | 35.0 | 11.25 | 8.61 | 0.85 |
| 120 | 34.73 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.36 | 21.0 | 11.25 | 10.0 | 0.85 |
| 97 | 31.33 | 35.0 | 11.25 | 9.98 | 0.6 |
