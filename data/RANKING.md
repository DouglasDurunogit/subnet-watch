# RANKING - generated 2026-08-10T06:19:58Z, block 8812178

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
| 1 | 107 | Minos | 78.0 | 1.0 | 111 | 32,212 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 6.1d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 67.23 | 203 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.4d ago |
| 3 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,778 | 1,778 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 3.0d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,225 | 1,225 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 2.5d ago |
| 5 | 96 | Verathos | 72.9 | 1.0 | 68.58 | 312 | rtx4090 | 0.417 | 30 | 42% | RELEASE 0.0d ago |
| 6 | 67 | Harnyx | 71.2 | 1.0 | 17.30 | 752 | cpu-small | 0.008 | 129 | 19% | SCORING_COMMIT 0.8d ago |
| 7 | 91 | cascade | 70.3 | 0.85 | 809 | 2,772 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.0d ago |
| 8 | 1 | Apex | 69.8 | 0.85 | 708 | 1,625 | rtx4090 | 0.500 | 4 | 50% | RELEASE 2.4d ago |
| 9 | 41 | Almanac | 69.3 | 1.0 | 11.18 | 34.26 | cpu-small | 0.696 | 69 | 70% | SCORING_COMMIT 3.2d ago |
| 10 | 26 | Perturb | 68.3 | 1.0 | 21.69 | 40.16 | rtx3060 | 0.500 | 11 | 50% | SCORING_COMMIT 3.6d ago |
| 11 | 62 | Ridges | 68.2 | 0.85 | 428 | 1,984 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.4d ago |
| 12 | 38 | ChronoLLM | 65.7 | 0.85 | 216 | 3,632 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.9d ago |
| 13 | 15 | ORO | 65.7 | 1.0 | 7.14 | 17.78 | cpu-small | 0.000 | 72 | 95% | RELEASE 3.8d ago |
| 14 | 21 | AdTAO | 65.4 | 1.0 | 4.67 | 21.63 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.6d ago |
| 15 | 80 | OpenRoboto | 64.9 | 0.85 | 162 | 589 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 2.1d ago |
| 16 | 28 | gm | 64.1 | 0.85 | 127 | 4,380 | rtx4090 | 0.184 | 26 | 43% | RELEASE 2.4d ago |
| 17 | 100 | BASE | 63.2 | 0.85 | 97.94 | 841 | rtx4090 | 0.000 | 8 | 51% | SCORING_COMMIT 1.4d ago |
| 18 | 61 | RedTeam | 62.7 | 0.85 | 84.50 | 353 | rtx4090 | 0.000 | 45 | 8% | RELEASE 0.8d ago |
| 19 | 102 | ConnitoAI | 59.9 | 0.85 | 1,265 | 1,265 | rtx4090 | 0.250 | 4 | 25% | RELEASE 9d ago |
| 20 | 51 | lium.io | 58.6 | 0.85 | 31.42 | 3,304 | rtx4090 | 0.000 | 50 | 52% | SCORING_COMMIT 2.4d ago |
| 21 | 6 | Numinous | 58.0 | 1.0 | 22.95 | 450 | cpu-small | 0.000 | 18 | 26% | README_TASK_DIFF 11d ago |
| 22 | 56 | Gradients | 56.6 | 0.85 | 472 | 995 | rtx4090 | 0.707 | 7 | 71% | SCORING_COMMIT 12d ago |
| 23 | 2 | DSperse | 56.5 | 0.85 | 12.11 | 112 | rtx4090 | 0.826 | 15 | 83% | RELEASE 4.1d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,216 | 7,216 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.7d ago |
| 25 | 124 | Swarm | 53.9 | 0.85 | 219 | 672 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.75 | a4000 | 1000.2916275653581 |
| 104 | Masx.ai | -2.16 | rtx4090 | 11.242414056461413 |
| 13 | Data Universe | -3.37 | rtx4090 | 6.348641145905085 |
| 88 | Investing | -4.49 | rtx4090 | 572.5903568691616 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 214.66765603216 |
| 8 | Vanta | -7.40 | rtx4090 | 3356.0860836057477 |
| 19 | blockmachine | -1.48 | rtx4090 | 367.60397395933927 |
| 18 | Zeus | -3.36 | rtx4090 | 1423.0358557169468 |
| 75 | Hippius | -4.62 | rtx4090 | 5.788025694710711 |
| 45 | AlphaRidge.ai | -4.72 | rtx4090 | 11.035121073905598 |
| 123 | MANTIS | -6.21 | rtx4090 | 74.24235495670167 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07498410081053793 |
| 105 | Beam | -4.54 | rtx4090 | 197.3273916611307 |
| 84 | ansuz | -8.15 | rtx4090 | 504.9988624310294 |
| 34 | BitMind | -18.60 | a100-80 | 295.674046904039 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.62 | 35.0 | 15.0 | 9.34 | 1.0 |
| 76 | 16.68 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.56 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.09 | 35.0 | 15.0 | 10.0 | 0.85 |
| 96 | 16.76 | 35.0 | 11.25 | 9.9 | 1.0 |
| 67 | 11.48 | 35.0 | 15.0 | 9.77 | 1.0 |
| 91 | 26.46 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 25.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.87 | 35.0 | 15.0 | 9.39 | 1.0 |
| 26 | 12.33 | 35.0 | 11.25 | 9.69 | 1.0 |
| 62 | 23.94 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 21.26 | 35.0 | 11.25 | 9.77 | 0.85 |
| 15 | 8.28 | 35.0 | 15.0 | 7.38 | 1.0 |
| 21 | 6.85 | 35.0 | 15.0 | 8.55 | 1.0 |
| 80 | 20.13 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 19.17 | 35.0 | 11.25 | 9.95 | 0.85 |
| 100 | 18.15 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 17.57 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 28.22 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 13.74 | 35.0 | 11.25 | 8.92 | 0.85 |
| 6 | 12.54 | 21.0 | 15.0 | 9.41 | 1.0 |
| 56 | 24.33 | 21.0 | 11.25 | 10.0 | 0.85 |
| 2 | 10.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.09 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.31 | 21.0 | 11.25 | 9.85 | 0.85 |
