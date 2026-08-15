# RANKING - generated 2026-08-15T19:59:57Z, block 8852270

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
| 1 | 107 | Minos | 78.1 | 1.0 | 111 | 32,064 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 5.2d ago |
| 2 | 76 | Phylax | 74.6 | 1.0 | 39.45 | 189 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 0.1d ago |
| 3 | 67 | Harnyx | 72.6 | 1.0 | 23.26 | 375 | cpu-small | 0.007 | 123 | 10% | SCORING_COMMIT 0.5d ago |
| 4 | 26 | Perturb | 70.8 | 1.0 | 41.18 | 75.71 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.2d ago |
| 5 | 1 | Apex | 70.4 | 0.85 | 844 | 1,123 | rtx4090 | 0.553 | 4 | 55% | RELEASE 2.2d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.84 | 443 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 2.1d ago |
| 7 | 96 | Verathos | 70.2 | 1.0 | 34.78 | 169 | rtx4090 | 0.415 | 55 | 42% | RELEASE 1.0d ago |
| 8 | 41 | Almanac | 69.6 | 1.0 | 12.07 | 53.98 | cpu-small | 0.662 | 72 | 66% | SCORING_COMMIT 2.9d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 510 | 963 | rtx4090 | 0.670 | 7 | 67% | SCORING_COMMIT 3.2d ago |
| 10 | 62 | Ridges | 68.5 | 0.85 | 479 | 2,219 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.9d ago |
| 11 | 85 | Vidaio | 68.3 | 0.85 | 443 | 567 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 3.4d ago |
| 12 | 91 | cascade | 68.3 | 0.85 | 442 | 2,270 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 1.9d ago |
| 13 | 15 | ORO | 68.1 | 1.0 | 10.89 | 20.19 | cpu-small | 0.000 | 86 | 93% | SCORING_COMMIT 1.9d ago |
| 14 | 21 | AdTAO | 67.6 | 1.0 | 7.59 | 34.04 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.3d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.30 | 1,330 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.1d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 224 | 719 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 4.2d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.66 | 480 | rtx4090 | 0.021 | 11 | 29% | SCORING_COMMIT 1.0d ago |
| 18 | 28 | gm | 60.4 | 0.85 | 43.34 | 2,498 | rtx4090 | 0.161 | 36 | 28% | RELEASE 3.2d ago |
| 19 | 60 | Bitsec.ai | 59.3 | 0.85 | 413 | 413 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 74 | Gittensor | 58.7 | 0.85 | 26.76 | 210 | rtx4090 | 0.631 | 15 | 63% | RELEASE 4.1d ago |
| 21 | 102 | ConnitoAI | 58.3 | 0.85 | 791 | 2,229 | rtx4090 | 0.251 | 6 | 41% | RELEASE 15d ago |
| 22 | 61 | RedTeam | 57.4 | 0.85 | 16.15 | 421 | rtx4090 | 0.000 | 81 | 10% | RELEASE 4.5d ago |
| 23 | 51 | lium.io | 56.2 | 0.85 | 18.22 | 1,442 | rtx4090 | 0.000 | 54 | 81% | SCORING_COMMIT 1.4d ago |
| 24 | 120 | Affine | 54.6 | 0.6 | 6,638 | 6,638 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.2d ago |
| 25 | 80 | OpenRoboto | 53.0 | 0.85 | 163 | 593 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.89 | a4000 | 958.123906529578 |
| 104 | Masx.ai | -2.13 | rtx4090 | 11.664843696998558 |
| 75 | Hippius | -7.38 | rtx4090 | 10917.127116035324 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 216.66212456736258 |
| 101 | Tag101 | -0.03 | cpu-small | 1.9881689925474033 |
| 13 | Data Universe | -3.41 | rtx4090 | 5.751110341675438 |
| 88 | Investing | -5.42 | rtx4090 | 337.90696838277694 |
| 8 | Vanta | -7.96 | rtx4090 | 2912.9090728804886 |
| 114 | SOMA | -8.12 | rtx4090 | 625.4429592652012 |
| 43 | Graphite | -0.47 | cpu-small | 11.325943192193122 |
| 45 | AlphaRidge.ai | -3.93 | rtx4090 | 16.679891659942992 |
| 22 | Desearch | -4.70 | rtx4090 | 67.04966501370609 |
| 18 | Zeus | -5.18 | rtx4090 | 1066.3653097873937 |
| 123 | MANTIS | -6.10 | rtx4090 | 77.63332338708234 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0755126849219933 |
| 105 | Beam | -2.72 | rtx4090 | 85.12679611103943 |
| 34 | BitMind | -20.18 | a100-80 | 28.997613970615255 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.64 | 35.0 | 15.0 | 9.41 | 1.0 |
| 76 | 14.62 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.6 | 35.0 | 15.0 | 9.96 | 1.0 |
| 26 | 14.78 | 35.0 | 11.25 | 9.8 | 1.0 |
| 1 | 26.62 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.15 | 35.0 | 15.0 | 9.17 | 1.0 |
| 96 | 14.13 | 35.0 | 11.25 | 9.81 | 1.0 |
| 41 | 10.15 | 35.0 | 15.0 | 9.45 | 1.0 |
| 56 | 24.64 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 24.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.07 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.78 | 35.0 | 15.0 | 8.34 | 1.0 |
| 21 | 8.49 | 35.0 | 15.0 | 9.13 | 1.0 |
| 38 | 18.12 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.39 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 16.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.98 | 35.0 | 11.25 | 9.85 | 0.85 |
| 60 | 23.8 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 13.13 | 35.0 | 11.25 | 9.63 | 0.85 |
| 102 | 26.36 | 21.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 11.68 | 35.0 | 11.25 | 8.19 | 0.85 |
| 120 | 34.76 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.16 | 21.0 | 11.25 | 10.0 | 0.85 |
