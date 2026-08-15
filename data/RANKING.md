# RANKING - generated 2026-08-15T02:40:56Z, block 8847074

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
| 1 | 107 | Minos | 77.9 | 1.0 | 108 | 31,872 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 4.5d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.33 | 193 | cpu-small | 0.000 | 10 | 34% | SCORING_COMMIT 6.2d ago |
| 3 | 67 | Harnyx | 72.6 | 1.0 | 24.18 | 388 | cpu-small | 0.084 | 107 | 10% | SCORING_COMMIT 0.6d ago |
| 4 | 6 | Numinous | 71.7 | 1.0 | 21.59 | 473 | cpu-small | 0.000 | 15 | 27% | WEIGHTS_VERSION_BUMP 1.4d ago |
| 5 | 26 | Perturb | 70.9 | 1.0 | 42.00 | 76.97 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.5d ago |
| 6 | 1 | Apex | 70.8 | 0.85 | 931 | 1,149 | rtx4090 | 0.536 | 4 | 54% | RELEASE 1.5d ago |
| 7 | 91 | cascade | 69.6 | 0.85 | 655 | 2,259 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.1d ago |
| 8 | 41 | Almanac | 69.6 | 1.0 | 12.21 | 54.14 | cpu-small | 0.664 | 72 | 66% | SCORING_COMMIT 2.2d ago |
| 9 | 56 | Gradients | 68.8 | 0.85 | 523 | 980 | rtx4090 | 0.665 | 7 | 66% | SCORING_COMMIT 2.5d ago |
| 10 | 62 | Ridges | 68.2 | 0.85 | 426 | 1,978 | rtx4090 | 0.133 | 7 | 35% | RELEASE 0.2d ago |
| 11 | 15 | ORO | 68.1 | 1.0 | 11.05 | 22.06 | cpu-small | 0.000 | 84 | 93% | SCORING_COMMIT 1.2d ago |
| 12 | 21 | AdTAO | 67.5 | 1.0 | 7.46 | 33.52 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 3.6d ago |
| 13 | 96 | Verathos | 67.4 | 1.0 | 17.74 | 185 | rtx4090 | 0.420 | 64 | 42% | RELEASE 0.3d ago |
| 14 | 85 | Vidaio | 66.2 | 0.85 | 239 | 572 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 2.7d ago |
| 15 | 38 | ChronoLLM | 66.1 | 0.85 | 101 | 1,379 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.4d ago |
| 16 | 124 | Swarm | 65.9 | 0.85 | 227 | 732 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 3.5d ago |
| 17 | 80 | OpenRoboto | 65.2 | 0.85 | 176 | 637 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 6.9d ago |
| 18 | 28 | gm | 65.0 | 0.85 | 169 | 2,574 | rtx4090 | 0.071 | 31 | 28% | RELEASE 2.5d ago |
| 19 | 98 | NeverPlayAlone | 64.1 | 0.85 | 1,728 | 1,728 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 8d ago |
| 20 | 55 | NIOME | 61.4 | 0.85 | 56.27 | 486 | rtx4090 | 0.020 | 11 | 30% | SCORING_COMMIT 0.3d ago |
| 21 | 60 | Bitsec.ai | 61.2 | 0.85 | 729 | 1,021 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 7d ago |
| 22 | 102 | ConnitoAI | 60.2 | 0.85 | 1,401 | 1,401 | rtx4090 | 0.251 | 4 | 25% | RELEASE 14d ago |
| 23 | 51 | lium.io | 59.5 | 0.85 | 39.00 | 1,744 | rtx4090 | 0.000 | 47 | 79% | SCORING_COMMIT 0.7d ago |
| 24 | 2 | DSperse | 58.1 | 0.85 | 20.35 | 88.59 | rtx4090 | 0.824 | 11 | 82% | RELEASE 4.3d ago |
| 25 | 74 | Gittensor | 58.0 | 0.85 | 22.56 | 215 | rtx4090 | 0.630 | 14 | 63% | RELEASE 3.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.00 | a4000 | 982.9063905519655 |
| 75 | Hippius | -7.19 | rtx4090 | 11163.94867286214 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 232.38175310255454 |
| 101 | Tag101 | -0.06 | cpu-small | 2.27443971089536 |
| 13 | Data Universe | -3.33 | rtx4090 | 6.067609740019565 |
| 88 | Investing | -5.61 | rtx4090 | 889.0042185309867 |
| 8 | Vanta | -7.95 | rtx4090 | 3098.3253831506945 |
| 114 | SOMA | -8.12 | rtx4090 | 1636.9132038666494 |
| 43 | Graphite | -0.47 | cpu-small | 11.550378980779723 |
| 45 | AlphaRidge.ai | -4.20 | rtx4090 | 17.221340161839912 |
| 18 | Zeus | -5.22 | rtx4090 | 1065.9614037733372 |
| 123 | MANTIS | -6.02 | rtx4090 | 81.05346285127656 |
| 22 | Desearch | -6.48 | rtx4090 | 87.95757578941263 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07600464909851865 |
| 105 | Beam | -2.52 | rtx4090 | 79.0104425360043 |
| 34 | BitMind | -20.06 | a100-80 | 23.343265869570732 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.53 | 35.0 | 15.0 | 9.39 | 1.0 |
| 76 | 14.7 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.74 | 35.0 | 15.0 | 9.86 | 1.0 |
| 6 | 12.31 | 35.0 | 15.0 | 9.38 | 1.0 |
| 26 | 14.86 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 27.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.62 | 35.0 | 11.25 | 9.99 | 0.85 |
| 41 | 10.19 | 35.0 | 15.0 | 9.45 | 1.0 |
| 56 | 24.73 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 23.93 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.83 | 35.0 | 15.0 | 8.22 | 1.0 |
| 21 | 8.43 | 35.0 | 15.0 | 9.1 | 1.0 |
| 96 | 11.58 | 35.0 | 11.25 | 9.62 | 1.0 |
| 85 | 21.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.26 | 35.0 | 15.0 | 9.51 | 0.85 |
| 124 | 21.44 | 35.0 | 11.25 | 9.85 | 0.85 |
| 80 | 20.45 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 20.3 | 35.0 | 11.25 | 9.96 | 0.85 |
| 98 | 29.45 | 21.0 | 15.0 | 10.0 | 0.85 |
| 55 | 15.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.04 | 21.0 | 15.0 | 10.0 | 0.85 |
| 102 | 28.62 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.57 | 35.0 | 11.25 | 9.14 | 0.85 |
| 2 | 12.09 | 35.0 | 11.25 | 10.0 | 0.85 |
| 74 | 12.48 | 35.0 | 11.25 | 9.56 | 0.85 |
