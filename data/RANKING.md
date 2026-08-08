# RANKING - generated 2026-08-08T21:14:37Z, block 8802252

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
| 1 | 11 | TrajectoryRL | 79.6 | 0.85 | 4,959 | 4,959 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.4d ago |
| 2 | 107 | Minos | 78.3 | 1.0 | 117 | 34,808 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 4.7d ago |
| 3 | 76 | Phylax | 76.6 | 1.0 | 65.30 | 197 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 6.2d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,223 | 1,223 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.1d ago |
| 5 | 67 | Harnyx | 71.3 | 1.0 | 17.08 | 743 | cpu-small | 0.017 | 142 | 19% | SCORING_COMMIT 1.7d ago |
| 6 | 91 | cascade | 70.2 | 0.85 | 785 | 2,688 | rtx4090 | 0.000 | 5 | 48% | RELEASE 3.7d ago |
| 7 | 96 | Verathos | 69.7 | 1.0 | 30.75 | 239 | rtx4090 | 0.439 | 59 | 44% | RELEASE 0.1d ago |
| 8 | 1 | Apex | 69.5 | 0.85 | 639 | 1,586 | rtx4090 | 0.453 | 4 | 45% | RELEASE 1.0d ago |
| 9 | 62 | Ridges | 69.1 | 0.85 | 558 | 2,017 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.0d ago |
| 10 | 26 | Perturb | 68.3 | 1.0 | 21.69 | 40.69 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 2.3d ago |
| 11 | 41 | Almanac | 68.3 | 1.0 | 8.78 | 44.77 | cpu-small | 0.760 | 66 | 76% | SCORING_COMMIT 1.9d ago |
| 12 | 15 | ORO | 67.3 | 1.0 | 9.16 | 19.30 | cpu-small | 0.000 | 70 | 94% | RELEASE 2.5d ago |
| 13 | 21 | AdTAO | 65.6 | 1.0 | 4.80 | 22.17 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.3d ago |
| 14 | 38 | ChronoLLM | 65.5 | 0.85 | 208 | 3,492 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.5d ago |
| 15 | 80 | OpenRoboto | 63.5 | 0.85 | 105 | 387 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 0.7d ago |
| 16 | 61 | RedTeam | 61.7 | 0.85 | 60.65 | 183 | rtx4090 | 0.000 | 43 | 6% | RELEASE 0.9d ago |
| 17 | 28 | gm | 60.6 | 0.85 | 45.60 | 3,765 | rtx4090 | 0.151 | 22 | 41% | RELEASE 1.0d ago |
| 18 | 51 | lium.io | 59.0 | 0.85 | 34.51 | 3,200 | rtx4090 | 0.000 | 47 | 68% | SCORING_COMMIT 1.0d ago |
| 19 | 85 | Vidaio | 57.0 | 0.85 | 527 | 537 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 12d ago |
| 20 | 56 | Gradients | 56.5 | 0.85 | 462 | 974 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 21 | 74 | Gittensor | 55.4 | 0.85 | 10.93 | 236 | rtx4090 | 0.631 | 16 | 63% | RELEASE 1.2d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 6,883 | 6,883 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.4d ago |
| 23 | 124 | Swarm | 53.8 | 0.85 | 211 | 643 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 7d ago |
| 24 | 100 | BASE | 53.0 | 0.6 | 3,304 | 3,304 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.0d ago |
| 25 | 97 | Albedo | 52.7 | 0.6 | 2,963 | 2,963 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 6.8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.09 | a4000 | 1030.6204621163818 |
| 104 | Masx.ai | -1.49 | rtx4090 | 10.601397159549412 |
| 13 | Data Universe | -3.07 | rtx4090 | 7.240550644653329 |
| 88 | Investing | -6.18 | rtx4090 | 381.5688201321205 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 129.13662898974587 |
| 8 | Vanta | -7.42 | rtx4090 | 3253.5444830942874 |
| 22 | Desearch | -1.13 | rtx4090 | 64.97305386142673 |
| 19 | blockmachine | -1.20 | rtx4090 | 195.76285977562543 |
| 18 | Zeus | -3.41 | rtx4090 | 1393.1769748104236 |
| 75 | Hippius | -4.67 | rtx4090 | 5.280304269339438 |
| 45 | AlphaRidge.ai | -5.12 | rtx4090 | 11.99013621794457 |
| 123 | MANTIS | -6.25 | rtx4090 | 72.47932780158673 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07525340083942067 |
| 105 | Beam | -3.72 | rtx4090 | 209.10477333745433 |
| 84 | ansuz | -8.15 | rtx4090 | 499.96434706612087 |
| 34 | BitMind | -19.27 | a100-80 | 289.395985001807 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.61 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.85 | 35.0 | 15.0 | 9.44 | 1.0 |
| 76 | 16.57 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.08 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.43 | 35.0 | 15.0 | 9.83 | 1.0 |
| 91 | 26.33 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 13.66 | 35.0 | 11.25 | 9.78 | 1.0 |
| 1 | 25.53 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.33 | 35.0 | 11.25 | 9.69 | 1.0 |
| 41 | 9.01 | 35.0 | 15.0 | 9.25 | 1.0 |
| 15 | 9.16 | 35.0 | 15.0 | 8.14 | 1.0 |
| 21 | 6.95 | 35.0 | 15.0 | 8.62 | 1.0 |
| 38 | 21.1 | 35.0 | 11.25 | 9.76 | 0.85 |
| 80 | 18.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 16.28 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.17 | 35.0 | 11.25 | 9.85 | 0.85 |
| 51 | 14.1 | 35.0 | 11.25 | 9.04 | 0.85 |
| 85 | 24.77 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.24 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.79 | 35.0 | 11.25 | 9.09 | 0.85 |
| 120 | 34.91 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.16 | 21.0 | 11.25 | 9.84 | 0.85 |
| 100 | 32.01 | 35.0 | 11.25 | 10.0 | 0.6 |
| 97 | 31.58 | 35.0 | 11.25 | 9.99 | 0.6 |
