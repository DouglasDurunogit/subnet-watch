# RANKING - generated 2026-08-24T08:10:44Z, block 8913523

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
| 1 | 76 | Phylax | 77.1 | 1.0 | 77.11 | 86.33 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.6d ago |
| 2 | 62 | Ridges | 72.4 | 0.85 | 1,502 | 3,069 | rtx4090 | 0.000 | 6 | 39% | RELEASE 5.4d ago |
| 3 | 23 | Trishool | 72.4 | 0.85 | 580 | 580 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 4.2d ago |
| 4 | 102 | ConnitoAI | 72.1 | 0.85 | 1,400 | 2,337 | rtx4090 | 0.250 | 5 | 33% | RELEASE 0.5d ago |
| 5 | 15 | ORO | 71.6 | 1.0 | 26.42 | 25,412 | cpu-small | 0.000 | 80 | 93% | SCORING_COMMIT 2.4d ago |
| 6 | 67 | Harnyx | 71.5 | 1.0 | 18.83 | 162 | cpu-small | 0.085 | 166 | 8% | SCORING_COMMIT 0.1d ago |
| 7 | 56 | Gradients | 69.9 | 0.85 | 708 | 1,119 | rtx4090 | 0.732 | 5 | 73% | SCORING_COMMIT 6.3d ago |
| 8 | 91 | cascade | 69.8 | 0.85 | 705 | 2,845 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 3.4d ago |
| 9 | 1 | Apex | 68.7 | 0.85 | 505 | 1,340 | rtx4090 | 0.514 | 5 | 51% | RELEASE 2.7d ago |
| 10 | 96 | Verathos | 68.3 | 1.0 | 22.33 | 219 | rtx4090 | 0.405 | 95 | 41% | RELEASE 5.7d ago |
| 11 | 11 | TrajectoryRL | 67.7 | 0.85 | 4,935 | 4,935 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 22d ago |
| 12 | 26 | Perturb | 67.6 | 1.0 | 18.83 | 404 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 4.3d ago |
| 13 | 124 | Swarm | 66.9 | 0.85 | 301 | 2,618 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.8d ago |
| 14 | 38 | ChronoLLM | 66.6 | 0.85 | 118 | 1,612 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 4.5d ago |
| 15 | 108 | Prometheon | 65.4 | 0.85 | 188 | 353 | rtx4090 | 0.655 | 6 | 66% | SCORING_COMMIT 2.8d ago |
| 16 | 107 | Minos | 65.4 | 1.0 | 154 | 43,405 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 14d ago |
| 17 | 85 | Vidaio | 64.5 | 0.85 | 142 | 425 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 6.0d ago |
| 18 | 60 | Bitsec.ai | 64.1 | 0.85 | 1,701 | 1,701 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 17d ago |
| 19 | 81 | Reliquary | 63.9 | 0.85 | 119 | 328 | rtx4090 | 0.043 | 38 | 7% | SCORING_COMMIT 1.6d ago |
| 20 | 28 | gm | 62.1 | 0.85 | 71.61 | 1,547 | rtx4090 | 0.125 | 48 | 13% | RELEASE 3.8d ago |
| 21 | 51 | lium.io | 61.3 | 0.85 | 63.36 | 2,176 | rtx4090 | 0.000 | 52 | 72% | SCORING_COMMIT 0.2d ago |
| 22 | 53 | engy | 60.1 | 0.85 | 38.16 | 323 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 0.2d ago |
| 23 | 61 | RedTeam | 56.5 | 0.85 | 12.94 | 305 | rtx4090 | 0.000 | 82 | 6% | RELEASE 2.0d ago |
| 24 | 41 | Almanac | 56.4 | 1.0 | 14.77 | 29.69 | cpu-small | 0.650 | 81 | 65% | SCORING_COMMIT 11d ago |
| 25 | 120 | Affine | 54.9 | 0.6 | 7,446 | 7,446 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.5d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.30 | a4000 | 1213.0185862765559 |
| 13 | Data Universe | -2.48 | rtx4090 | 7.78588638000012 |
| 18 | Zeus | -3.97 | rtx4090 | 1347.8588809977027 |
| 89 | InfiniteQuant | -4.41 | rtx4090 | 114.45169194367263 |
| 123 | MANTIS | -5.59 | rtx4090 | 122.77667542628504 |
| 75 | Hippius | -6.01 | rtx4090 | 12409.423998819 |
| 34 | BitMind | -16.46 | a100-80 | 339.50830759971274 |
| 6 | Numinous | -0.96 | cpu-small | 179.7085574859628 |
| 104 | Masx.ai | -0.42 | rtx4090 | 8.448145497187719 |
| 50 | Synth | -0.64 | rtx4090 | 68.18084321987503 |
| 88 | Investing | -2.84 | rtx4090 | 642.5531558650804 |
| 8 | Vanta | -7.34 | rtx4090 | 3313.7532160733053 |
| 43 | Graphite | -0.26 | cpu-small | 195.33155310621274 |
| 19 | blockmachine | -0.48 | rtx4090 | 674.638222390034 |
| 45 | AlphaRidge.ai | -4.59 | rtx4090 | 11.894080469918649 |
| 63 | Enigma | -8.13 | rtx4090 | 0.08595581927459396 |
| 105 | Beam | -1.51 | rtx4090 | 89.43323265528142 |
| 84 | ansuz | -8.15 | rtx4090 | 524.8390963476883 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn100, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.21 | 35.0 | 15.0 | 9.9 | 1.0 |
| 62 | 28.89 | 35.0 | 11.25 | 10.0 | 0.85 |
| 23 | 25.14 | 35.0 | 15.0 | 9.99 | 0.85 |
| 102 | 28.62 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 13.08 | 35.0 | 15.0 | 8.48 | 1.0 |
| 67 | 11.8 | 35.0 | 15.0 | 9.71 | 1.0 |
| 56 | 25.93 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.91 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.44 | 35.0 | 11.25 | 9.64 | 1.0 |
| 11 | 33.59 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.8 | 35.0 | 11.25 | 9.58 | 1.0 |
| 124 | 22.56 | 35.0 | 11.25 | 9.87 | 0.85 |
| 38 | 18.88 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.7 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.91 | 21.0 | 15.0 | 9.45 | 1.0 |
| 85 | 19.6 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 29.39 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 18.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.93 | 35.0 | 11.25 | 9.89 | 0.85 |
| 51 | 16.45 | 35.0 | 11.25 | 9.38 | 0.85 |
| 53 | 14.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 10.41 | 35.0 | 11.25 | 9.82 | 0.85 |
| 41 | 10.89 | 21.0 | 15.0 | 9.46 | 1.0 |
| 120 | 35.22 | 35.0 | 11.25 | 9.99 | 0.6 |
