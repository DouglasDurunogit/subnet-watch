# RANKING - generated 2026-08-09T23:42:26Z, block 8810191

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
| 1 | 107 | Minos | 78.2 | 1.0 | 115 | 33,090 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.8d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 67.03 | 202 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.1d ago |
| 3 | 60 | Bitsec.ai | 74.8 | 0.85 | 1,199 | 1,199 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 2.2d ago |
| 4 | 96 | Verathos | 71.2 | 1.0 | 44.86 | 301 | rtx4090 | 0.421 | 35 | 42% | RELEASE 0.4d ago |
| 5 | 67 | Harnyx | 70.8 | 1.0 | 14.84 | 849 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.5d ago |
| 6 | 91 | cascade | 70.2 | 0.85 | 788 | 2,700 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.8d ago |
| 7 | 1 | Apex | 69.9 | 0.85 | 727 | 1,665 | rtx4090 | 0.475 | 4 | 48% | RELEASE 2.1d ago |
| 8 | 41 | Almanac | 69.4 | 1.0 | 11.66 | 34.18 | cpu-small | 0.716 | 65 | 72% | SCORING_COMMIT 3.0d ago |
| 9 | 15 | ORO | 68.3 | 1.0 | 10.27 | 19.62 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.6d ago |
| 10 | 62 | Ridges | 68.2 | 0.85 | 433 | 2,010 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.1d ago |
| 11 | 26 | Perturb | 68.2 | 1.0 | 21.09 | 186 | rtx3060 | 0.502 | 11 | 50% | SCORING_COMMIT 3.4d ago |
| 12 | 100 | BASE | 68.0 | 0.85 | 403 | 1,638 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.1d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 216 | 3,629 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.6d ago |
| 14 | 80 | OpenRoboto | 64.9 | 0.85 | 163 | 593 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 1.8d ago |
| 15 | 21 | AdTAO | 64.9 | 1.0 | 4.61 | 21.41 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.4d ago |
| 16 | 61 | RedTeam | 62.6 | 0.85 | 81.05 | 340 | rtx4090 | 0.000 | 47 | 7% | RELEASE 0.5d ago |
| 17 | 28 | gm | 61.8 | 0.85 | 66.12 | 3,898 | rtx4090 | 0.324 | 26 | 39% | RELEASE 2.1d ago |
| 18 | 6 | Numinous | 59.0 | 1.0 | 29.13 | 334 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 19 | 51 | lium.io | 58.9 | 0.85 | 33.72 | 2,716 | rtx4090 | 0.000 | 47 | 60% | SCORING_COMMIT 2.1d ago |
| 20 | 56 | Gradients | 56.6 | 0.85 | 471 | 992 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 21 | 85 | Vidaio | 55.2 | 0.85 | 309 | 535 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 13d ago |
| 22 | 120 | Affine | 54.8 | 0.6 | 7,261 | 7,261 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.5d ago |
| 23 | 124 | Swarm | 53.9 | 0.85 | 220 | 671 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |
| 24 | 2 | DSperse | 52.1 | 0.85 | 2.58 | 112 | rtx4090 | 0.826 | 12 | 83% | RELEASE 3.8d ago |
| 25 | 74 | Gittensor | 52.0 | 0.85 | 4.85 | 220 | rtx4090 | 0.630 | 16 | 63% | RELEASE 2.3d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.90 | a4000 | 983.3476768539933 |
| 104 | Masx.ai | -1.50 | rtx4090 | 8.361932781347818 |
| 13 | Data Universe | -3.34 | rtx4090 | 7.296784308407438 |
| 88 | Investing | -4.37 | rtx4090 | 598.853656730468 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 122.72545081998562 |
| 8 | Vanta | -7.40 | rtx4090 | 3337.291475860538 |
| 19 | blockmachine | -1.41 | rtx4090 | 180.07944025748026 |
| 18 | Zeus | -2.78 | rtx4090 | 1431.1303661256347 |
| 45 | AlphaRidge.ai | -4.25 | rtx4090 | 24.446692241862426 |
| 75 | Hippius | -4.49 | rtx4090 | 5.72311123273847 |
| 123 | MANTIS | -6.27 | rtx4090 | 73.65403708938203 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07472412683184677 |
| 105 | Beam | -4.31 | rtx4090 | 191.59494624670506 |
| 84 | ansuz | -8.15 | rtx4090 | 503.13427427336586 |
| 34 | BitMind | -18.13 | a100-80 | 294.9589389365954 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.79 | 35.0 | 15.0 | 9.42 | 1.0 |
| 76 | 16.67 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.01 | 35.0 | 15.0 | 10.0 | 0.85 |
| 96 | 15.11 | 35.0 | 11.25 | 9.85 | 1.0 |
| 67 | 10.91 | 35.0 | 15.0 | 9.85 | 1.0 |
| 91 | 26.35 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.03 | 35.0 | 15.0 | 9.42 | 1.0 |
| 15 | 9.57 | 35.0 | 15.0 | 8.7 | 1.0 |
| 62 | 23.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.22 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 23.71 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 21.25 | 35.0 | 11.25 | 9.75 | 0.85 |
| 80 | 20.16 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 6.81 | 35.0 | 15.0 | 8.07 | 1.0 |
| 61 | 17.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.62 | 35.0 | 11.25 | 9.9 | 0.85 |
| 6 | 13.45 | 21.0 | 15.0 | 9.54 | 1.0 |
| 51 | 14.01 | 35.0 | 11.25 | 9.0 | 0.85 |
| 56 | 24.32 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 22.66 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.12 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.33 | 21.0 | 11.25 | 9.85 | 0.85 |
| 2 | 5.04 | 35.0 | 11.25 | 9.99 | 0.85 |
| 74 | 6.98 | 35.0 | 11.25 | 7.91 | 0.85 |
