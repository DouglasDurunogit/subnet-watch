# RANKING - generated 2026-08-09T19:10:59Z, block 8808834

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
| 1 | 107 | Minos | 78.2 | 1.0 | 115 | 34,320 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.6d ago |
| 2 | 76 | Phylax | 76.8 | 1.0 | 68.53 | 206 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 0.9d ago |
| 3 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,250 | 1,250 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 2.0d ago |
| 4 | 67 | Harnyx | 70.8 | 1.0 | 15.19 | 868 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.3d ago |
| 5 | 91 | cascade | 70.3 | 0.85 | 800 | 2,739 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.6d ago |
| 6 | 1 | Apex | 70.1 | 0.85 | 760 | 1,567 | rtx4090 | 0.490 | 4 | 49% | RELEASE 1.9d ago |
| 7 | 41 | Almanac | 69.5 | 1.0 | 11.72 | 35.02 | cpu-small | 0.719 | 66 | 72% | SCORING_COMMIT 2.8d ago |
| 8 | 96 | Verathos | 68.5 | 1.0 | 23.11 | 216 | rtx4090 | 0.415 | 68 | 42% | RELEASE 0.2d ago |
| 9 | 62 | Ridges | 68.3 | 0.85 | 443 | 2,053 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.9d ago |
| 10 | 26 | Perturb | 68.2 | 1.0 | 21.30 | 40.20 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.2d ago |
| 11 | 100 | BASE | 68.1 | 0.85 | 420 | 1,704 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 0.9d ago |
| 12 | 15 | ORO | 67.7 | 1.0 | 10.12 | 19.34 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.4d ago |
| 13 | 38 | ChronoLLM | 65.7 | 0.85 | 219 | 3,683 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.4d ago |
| 14 | 21 | AdTAO | 65.5 | 1.0 | 4.75 | 21.98 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.2d ago |
| 15 | 80 | OpenRoboto | 65.4 | 0.85 | 186 | 672 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 1.6d ago |
| 16 | 28 | gm | 62.9 | 0.85 | 90.17 | 4,158 | rtx4090 | 0.254 | 26 | 42% | RELEASE 1.9d ago |
| 17 | 61 | RedTeam | 62.7 | 0.85 | 83.01 | 339 | rtx4090 | 0.000 | 48 | 7% | RELEASE 0.3d ago |
| 18 | 102 | ConnitoAI | 59.3 | 0.85 | 1,072 | 1,287 | rtx4090 | 0.251 | 6 | 28% | RELEASE 9d ago |
| 19 | 6 | Numinous | 59.1 | 1.0 | 29.81 | 342 | cpu-small | 0.000 | 18 | 19% | README_TASK_DIFF 11d ago |
| 20 | 51 | lium.io | 58.9 | 0.85 | 33.74 | 2,759 | rtx4090 | 0.000 | 50 | 61% | SCORING_COMMIT 1.9d ago |
| 21 | 56 | Gradients | 56.7 | 0.85 | 482 | 1,015 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 22 | 85 | Vidaio | 55.6 | 0.85 | 355 | 355 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 12d ago |
| 23 | 120 | Affine | 54.9 | 0.6 | 7,399 | 7,399 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.3d ago |
| 24 | 2 | DSperse | 54.8 | 0.85 | 7.01 | 107 | rtx4090 | 0.827 | 12 | 83% | RELEASE 3.6d ago |
| 25 | 124 | Swarm | 54.1 | 0.85 | 230 | 698 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.64 | a4000 | 1045.205406513601 |
| 104 | Masx.ai | -2.27 | rtx4090 | 10.67778154246247 |
| 13 | Data Universe | -2.81 | rtx4090 | 7.35201804635273 |
| 88 | Investing | -4.74 | rtx4090 | 470.01098531862385 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 123.69744194148072 |
| 8 | Vanta | -7.38 | rtx4090 | 3412.5299646100093 |
| 22 | Desearch | -1.02 | rtx4090 | 80.3109730737199 |
| 19 | blockmachine | -1.16 | rtx4090 | 251.5376011189106 |
| 75 | Hippius | -4.37 | rtx4090 | 5.912937808031598 |
| 18 | Zeus | -4.38 | rtx4090 | 997.8940974065748 |
| 45 | AlphaRidge.ai | -4.69 | rtx4090 | 19.99822120572338 |
| 123 | MANTIS | -6.24 | rtx4090 | 75.26443436144974 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07639749279637788 |
| 105 | Beam | -4.20 | rtx4090 | 193.0984328118665 |
| 84 | ansuz | -8.15 | rtx4090 | 527.2942502078571 |
| 34 | BitMind | -18.28 | a100-80 | 301.42403747421645 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.77 | 35.0 | 15.0 | 9.4 | 1.0 |
| 76 | 16.75 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.17 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.0 | 35.0 | 15.0 | 9.84 | 1.0 |
| 91 | 26.41 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.21 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.05 | 35.0 | 15.0 | 9.41 | 1.0 |
| 96 | 12.57 | 35.0 | 11.25 | 9.7 | 1.0 |
| 62 | 24.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.26 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 23.87 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.51 | 35.0 | 15.0 | 8.18 | 1.0 |
| 38 | 21.31 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 6.91 | 35.0 | 15.0 | 8.55 | 1.0 |
| 80 | 20.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 17.83 | 35.0 | 11.25 | 9.92 | 0.85 |
| 61 | 17.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.56 | 21.0 | 11.25 | 10.0 | 0.85 |
| 6 | 13.54 | 21.0 | 15.0 | 9.54 | 1.0 |
| 51 | 14.01 | 35.0 | 11.25 | 8.98 | 0.85 |
| 56 | 24.41 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.21 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.19 | 35.0 | 11.25 | 9.99 | 0.6 |
| 2 | 8.22 | 35.0 | 11.25 | 10.0 | 0.85 |
| 124 | 21.49 | 21.0 | 11.25 | 9.85 | 0.85 |
