# RANKING - generated 2026-08-08T19:53:02Z, block 8801844

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
| 1 | 11 | TrajectoryRL | 79.6 | 0.85 | 4,961 | 4,961 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.4d ago |
| 2 | 107 | Minos | 78.4 | 1.0 | 119 | 34,654 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 4.6d ago |
| 3 | 76 | Phylax | 76.3 | 1.0 | 61.67 | 186 | cpu-small | 0.000 | 10 | 31% | SCORING_COMMIT 6.1d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,221 | 1,221 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.0d ago |
| 5 | 96 | Verathos | 72.1 | 1.0 | 56.40 | 240 | rtx4090 | 0.420 | 46 | 42% | RELEASE 0.1d ago |
| 6 | 67 | Harnyx | 71.3 | 1.0 | 17.11 | 744 | cpu-small | 0.017 | 142 | 19% | SCORING_COMMIT 1.7d ago |
| 7 | 91 | cascade | 70.2 | 0.85 | 783 | 2,680 | rtx4090 | 0.000 | 5 | 48% | RELEASE 3.6d ago |
| 8 | 1 | Apex | 69.5 | 0.85 | 643 | 1,593 | rtx4090 | 0.448 | 4 | 45% | RELEASE 1.0d ago |
| 9 | 62 | Ridges | 69.0 | 0.85 | 556 | 2,012 | rtx4090 | 0.133 | 7 | 35% | RELEASE 2.9d ago |
| 10 | 26 | Perturb | 68.3 | 1.0 | 21.62 | 40.58 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 2.2d ago |
| 11 | 41 | Almanac | 68.3 | 1.0 | 8.89 | 26.53 | cpu-small | 0.760 | 68 | 76% | SCORING_COMMIT 1.8d ago |
| 12 | 15 | ORO | 67.5 | 1.0 | 9.12 | 19.23 | cpu-small | 0.000 | 70 | 94% | RELEASE 2.4d ago |
| 13 | 21 | AdTAO | 65.6 | 1.0 | 4.79 | 22.11 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.2d ago |
| 14 | 38 | ChronoLLM | 65.5 | 0.85 | 206 | 3,466 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.4d ago |
| 15 | 80 | OpenRoboto | 63.3 | 0.85 | 99.44 | 369 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 0.6d ago |
| 16 | 61 | RedTeam | 61.7 | 0.85 | 60.80 | 184 | rtx4090 | 0.000 | 43 | 6% | RELEASE 0.9d ago |
| 17 | 102 | ConnitoAI | 59.2 | 0.85 | 1,025 | 1,538 | rtx4090 | 0.251 | 5 | 31% | RELEASE 8d ago |
| 18 | 28 | gm | 58.9 | 0.85 | 27.88 | 3,216 | rtx4090 | 0.286 | 24 | 35% | RELEASE 0.9d ago |
| 19 | 51 | lium.io | 58.7 | 0.85 | 32.41 | 3,048 | rtx4090 | 0.000 | 47 | 65% | SCORING_COMMIT 1.0d ago |
| 20 | 56 | Gradients | 56.5 | 0.85 | 461 | 972 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 21 | 85 | Vidaio | 56.3 | 0.85 | 430 | 481 | rtx4090 | 0.000 | 10 | 20% | SCORING_COMMIT 12d ago |
| 22 | 74 | Gittensor | 55.4 | 0.85 | 10.92 | 235 | rtx4090 | 0.632 | 16 | 63% | RELEASE 1.2d ago |
| 23 | 120 | Affine | 54.7 | 0.6 | 6,851 | 6,851 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.3d ago |
| 24 | 124 | Swarm | 53.8 | 0.85 | 210 | 641 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 7d ago |
| 25 | 100 | BASE | 52.9 | 0.6 | 3,296 | 3,296 | rtx4090 | 0.000 | 1 | 100% | RELEASE 0.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.19 | a4000 | 1042.7496160474357 |
| 104 | Masx.ai | -1.87 | rtx4090 | 9.864490266583537 |
| 13 | Data Universe | -3.09 | rtx4090 | 7.1046821565810285 |
| 88 | Investing | -6.19 | rtx4090 | 380.55252836262065 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 128.94360523135757 |
| 8 | Vanta | -7.42 | rtx4090 | 3246.0522926780523 |
| 19 | blockmachine | -1.03 | rtx4090 | 253.88289484361414 |
| 22 | Desearch | -2.06 | rtx4090 | 72.0305652534702 |
| 45 | AlphaRidge.ai | -3.52 | rtx4090 | 23.635288191573572 |
| 75 | Hippius | -4.69 | rtx4090 | 5.252924718219119 |
| 18 | Zeus | -4.73 | rtx4090 | 907.2672997779556 |
| 123 | MANTIS | -6.22 | rtx4090 | 73.85138786334196 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0751080805689305 |
| 105 | Beam | -3.71 | rtx4090 | 212.81452744656764 |
| 84 | ansuz | -8.15 | rtx4090 | 488.5764430936281 |
| 34 | BitMind | -19.14 | a100-80 | 288.750274714324 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn6, sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn55, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.61 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.91 | 35.0 | 15.0 | 9.45 | 1.0 |
| 76 | 16.34 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.08 | 35.0 | 15.0 | 10.0 | 0.85 |
| 96 | 16.0 | 35.0 | 11.25 | 9.88 | 1.0 |
| 67 | 11.44 | 35.0 | 15.0 | 9.81 | 1.0 |
| 91 | 26.32 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 25.55 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.32 | 35.0 | 11.25 | 9.69 | 1.0 |
| 41 | 9.05 | 35.0 | 15.0 | 9.26 | 1.0 |
| 15 | 9.14 | 35.0 | 15.0 | 8.38 | 1.0 |
| 21 | 6.94 | 35.0 | 15.0 | 8.62 | 1.0 |
| 38 | 21.07 | 35.0 | 11.25 | 9.76 | 0.85 |
| 80 | 18.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 16.29 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.39 | 21.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.28 | 35.0 | 11.25 | 9.76 | 0.85 |
| 51 | 13.86 | 35.0 | 11.25 | 8.98 | 0.85 |
| 56 | 24.23 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.96 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.79 | 35.0 | 11.25 | 9.09 | 0.85 |
| 120 | 34.89 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.15 | 21.0 | 11.25 | 9.84 | 0.85 |
| 100 | 32.0 | 35.0 | 11.25 | 10.0 | 0.6 |
