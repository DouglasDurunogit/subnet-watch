# RANKING - generated 2026-08-15T19:09:55Z, block 8852019

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
| 1 | 107 | Minos | 78.1 | 1.0 | 112 | 32,452 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.2d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.53 | 194 | cpu-small | 0.000 | 10 | 35% | SCORING_COMMIT 0.0d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.26 | 374 | cpu-small | 0.007 | 123 | 10% | SCORING_COMMIT 0.4d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.28 | 75.69 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.2d ago |
| 5 | 96 | Verathos | 70.5 | 1.0 | 37.70 | 170 | rtx4090 | 0.409 | 56 | 41% | RELEASE 1.0d ago |
| 6 | 1 | Apex | 70.4 | 0.85 | 847 | 1,126 | rtx4090 | 0.552 | 4 | 55% | RELEASE 2.2d ago |
| 7 | 6 | Numinous | 70.3 | 1.0 | 15.83 | 443 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 2.1d ago |
| 8 | 41 | Almanac | 69.6 | 1.0 | 12.07 | 53.98 | cpu-small | 0.662 | 72 | 66% | SCORING_COMMIT 2.8d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 511 | 964 | rtx4090 | 0.670 | 7 | 67% | SCORING_COMMIT 3.2d ago |
| 10 | 62 | Ridges | 68.5 | 0.85 | 479 | 2,216 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.9d ago |
| 11 | 85 | Vidaio | 68.4 | 0.85 | 462 | 510 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 3.4d ago |
| 12 | 91 | cascade | 68.3 | 0.85 | 442 | 2,270 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 1.8d ago |
| 13 | 15 | ORO | 68.1 | 1.0 | 10.86 | 20.14 | cpu-small | 0.000 | 86 | 93% | SCORING_COMMIT 1.9d ago |
| 14 | 21 | AdTAO | 67.6 | 1.0 | 7.59 | 34.03 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.3d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.28 | 1,330 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.1d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 719 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.2d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.90 | 480 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 1.0d ago |
| 18 | 28 | gm | 60.9 | 0.85 | 49.52 | 2,437 | rtx4090 | 0.148 | 35 | 27% | RELEASE 3.2d ago |
| 19 | 102 | ConnitoAI | 59.9 | 0.85 | 1,257 | 1,511 | rtx4090 | 0.251 | 6 | 28% | RELEASE 15d ago |
| 20 | 60 | Bitsec.ai | 59.3 | 0.85 | 409 | 409 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 21 | 74 | Gittensor | 58.6 | 0.85 | 26.36 | 210 | rtx4090 | 0.631 | 15 | 63% | RELEASE 4.0d ago |
| 22 | 2 | DSperse | 57.4 | 0.85 | 16.19 | 95.98 | rtx4090 | 0.824 | 10 | 82% | RELEASE 4.9d ago |
| 23 | 61 | RedTeam | 57.3 | 0.85 | 16.10 | 418 | rtx4090 | 0.000 | 81 | 10% | RELEASE 4.5d ago |
| 24 | 120 | Affine | 54.6 | 0.6 | 6,636 | 6,636 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.2d ago |
| 25 | 80 | OpenRoboto | 53.1 | 0.85 | 168 | 607 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.89 | a4000 | 958.0685870346617 |
| 104 | Masx.ai | -1.40 | rtx4090 | 11.121166353701147 |
| 75 | Hippius | -7.38 | rtx4090 | 10916.511126352249 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 216.4869238395966 |
| 13 | Data Universe | -3.35 | rtx4090 | 5.803950754765269 |
| 88 | Investing | -5.51 | rtx4090 | 327.1516683608655 |
| 8 | Vanta | -7.96 | rtx4090 | 3029.1712345310625 |
| 114 | SOMA | -8.12 | rtx4090 | 1556.9269147179132 |
| 43 | Graphite | -0.47 | cpu-small | 11.324796081622312 |
| 32 | ItsAI | -0.01 | rtx4090 | 10.558382903124043 |
| 22 | Desearch | -4.45 | rtx4090 | 81.27759780631622 |
| 45 | AlphaRidge.ai | -4.51 | rtx4090 | 14.96031732157963 |
| 18 | Zeus | -5.18 | rtx4090 | 1066.372726521767 |
| 123 | MANTIS | -6.10 | rtx4090 | 77.67212458213993 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07549953144749376 |
| 105 | Beam | -2.79 | rtx4090 | 84.38624322101946 |
| 34 | BitMind | -20.39 | a100-80 | 32.1298388587653 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.67 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 14.72 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.6 | 35.0 | 15.0 | 9.93 | 1.0 |
| 26 | 14.79 | 35.0 | 11.25 | 9.84 | 1.0 |
| 96 | 14.44 | 35.0 | 11.25 | 9.83 | 1.0 |
| 1 | 26.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.15 | 35.0 | 15.0 | 9.17 | 1.0 |
| 41 | 10.15 | 35.0 | 15.0 | 9.45 | 1.0 |
| 56 | 24.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.77 | 35.0 | 15.0 | 8.3 | 1.0 |
| 21 | 8.49 | 35.0 | 15.0 | 9.13 | 1.0 |
| 38 | 18.12 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.39 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.49 | 35.0 | 11.25 | 9.87 | 0.85 |
| 102 | 28.19 | 21.0 | 11.25 | 10.0 | 0.85 |
| 60 | 23.76 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 13.07 | 35.0 | 11.25 | 9.63 | 0.85 |
| 2 | 11.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.76 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.26 | 21.0 | 11.25 | 10.0 | 0.85 |
