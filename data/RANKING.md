# RANKING - generated 2026-08-09T17:04:23Z, block 8808201

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
| 1 | 107 | Minos | 78.5 | 1.0 | 123 | 35,191 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 5.5d ago |
| 2 | 76 | Phylax | 76.8 | 1.0 | 68.63 | 207 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.8d ago |
| 3 | 60 | Bitsec.ai | 75.1 | 0.85 | 1,294 | 1,294 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.9d ago |
| 4 | 67 | Harnyx | 70.8 | 1.0 | 15.22 | 869 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.3d ago |
| 5 | 91 | cascade | 70.2 | 0.85 | 798 | 2,731 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.5d ago |
| 6 | 96 | Verathos | 70.2 | 1.0 | 34.67 | 171 | rtx4090 | 0.419 | 59 | 42% | RELEASE 0.1d ago |
| 7 | 1 | Apex | 70.1 | 0.85 | 768 | 1,582 | rtx4090 | 0.483 | 4 | 48% | RELEASE 1.9d ago |
| 8 | 41 | Almanac | 69.4 | 1.0 | 11.65 | 35.13 | cpu-small | 0.721 | 66 | 72% | SCORING_COMMIT 2.7d ago |
| 9 | 26 | Perturb | 68.4 | 1.0 | 22.23 | 40.97 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.1d ago |
| 10 | 62 | Ridges | 68.3 | 0.85 | 443 | 2,055 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.8d ago |
| 11 | 100 | BASE | 68.1 | 0.85 | 420 | 1,705 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.8d ago |
| 12 | 15 | ORO | 68.0 | 1.0 | 10.18 | 19.45 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.3d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 217 | 3,637 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.3d ago |
| 14 | 21 | AdTAO | 65.5 | 1.0 | 4.81 | 22.21 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.1d ago |
| 15 | 80 | OpenRoboto | 64.8 | 0.85 | 157 | 570 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 1.5d ago |
| 16 | 28 | gm | 64.5 | 0.85 | 146 | 4,216 | rtx4090 | 0.278 | 25 | 42% | RELEASE 1.8d ago |
| 17 | 61 | RedTeam | 63.2 | 0.85 | 97.23 | 275 | rtx4090 | 0.000 | 42 | 6% | RELEASE 0.3d ago |
| 18 | 6 | Numinous | 59.1 | 1.0 | 29.84 | 342 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 19 | 51 | lium.io | 58.7 | 0.85 | 32.36 | 3,106 | rtx4090 | 0.000 | 49 | 60% | SCORING_COMMIT 1.9d ago |
| 20 | 56 | Gradients | 56.7 | 0.85 | 482 | 1,017 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 21 | 85 | Vidaio | 55.8 | 0.85 | 368 | 368 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 12d ago |
| 22 | 2 | DSperse | 55.8 | 0.85 | 9.84 | 137 | rtx4090 | 0.826 | 15 | 83% | RELEASE 3.5d ago |
| 23 | 120 | Affine | 54.9 | 0.6 | 7,373 | 7,373 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.2d ago |
| 24 | 124 | Swarm | 53.9 | 0.85 | 221 | 671 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |
| 25 | 74 | Gittensor | 52.7 | 0.85 | 5.73 | 226 | rtx4090 | 0.630 | 16 | 63% | RELEASE 2.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.74 | a4000 | 1071.773830153564 |
| 104 | Masx.ai | -2.21 | rtx4090 | 9.05749893583865 |
| 13 | Data Universe | -2.80 | rtx4090 | 7.188586963684063 |
| 88 | Investing | -4.71 | rtx4090 | 473.943485187136 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 125.77323638451735 |
| 8 | Vanta | -7.38 | rtx4090 | 3534.884643368024 |
| 45 | AlphaRidge.ai | -1.31 | rtx4090 | 40.37196120442572 |
| 19 | blockmachine | -1.58 | rtx4090 | 177.30583708184105 |
| 75 | Hippius | -4.36 | rtx4090 | 5.9175893202162655 |
| 18 | Zeus | -4.37 | rtx4090 | 999.6426234907292 |
| 123 | MANTIS | -6.20 | rtx4090 | 74.98787051980113 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07659809143942085 |
| 105 | Beam | -4.14 | rtx4090 | 192.998123463357 |
| 84 | ansuz | -8.15 | rtx4090 | 507.2206949210952 |
| 34 | BitMind | -18.20 | a100-80 | 301.9113687666864 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 19.05 | 35.0 | 15.0 | 9.45 | 1.0 |
| 76 | 16.76 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.31 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.01 | 35.0 | 15.0 | 9.78 | 1.0 |
| 91 | 26.4 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 14.12 | 35.0 | 11.25 | 9.8 | 1.0 |
| 1 | 26.25 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.02 | 35.0 | 15.0 | 9.41 | 1.0 |
| 26 | 12.43 | 35.0 | 11.25 | 9.69 | 1.0 |
| 62 | 24.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 100 | 23.87 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.54 | 35.0 | 15.0 | 8.47 | 1.0 |
| 38 | 21.26 | 35.0 | 11.25 | 9.76 | 0.85 |
| 21 | 6.95 | 35.0 | 15.0 | 8.56 | 1.0 |
| 80 | 19.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 19.71 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 18.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 13.54 | 21.0 | 15.0 | 9.54 | 1.0 |
| 51 | 13.85 | 35.0 | 11.25 | 8.93 | 0.85 |
| 56 | 24.41 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.35 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 9.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.18 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.33 | 21.0 | 11.25 | 9.84 | 0.85 |
| 74 | 7.53 | 35.0 | 11.25 | 8.19 | 0.85 |
