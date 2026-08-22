# RANKING - generated 2026-08-22T10:36:02Z, block 8899849

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
| 1 | 76 | Phylax | 77.2 | 1.0 | 78.52 | 132 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.0d ago |
| 2 | 23 | Trishool | 72.2 | 0.85 | 559 | 559 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 2.3d ago |
| 3 | 67 | Harnyx | 72.2 | 1.0 | 22.72 | 443 | cpu-small | 0.091 | 140 | 12% | SCORING_COMMIT 1.0d ago |
| 4 | 102 | ConnitoAI | 71.8 | 0.85 | 1,256 | 2,381 | rtx4090 | 0.250 | 6 | 36% | RELEASE 0.8d ago |
| 5 | 91 | cascade | 70.0 | 0.85 | 738 | 2,979 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.5d ago |
| 6 | 56 | Gradients | 70.0 | 0.85 | 737 | 1,065 | rtx4090 | 0.726 | 5 | 73% | SCORING_COMMIT 4.4d ago |
| 7 | 15 | ORO | 69.4 | 1.0 | 17.42 | 21,268 | cpu-small | 0.000 | 60 | 95% | SCORING_COMMIT 0.5d ago |
| 8 | 1 | Apex | 68.5 | 0.85 | 480 | 1,131 | rtx4090 | 0.543 | 5 | 54% | RELEASE 0.8d ago |
| 9 | 11 | TrajectoryRL | 67.4 | 0.85 | 4,621 | 4,621 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 20d ago |
| 10 | 26 | Perturb | 67.4 | 1.0 | 17.73 | 255 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.4d ago |
| 11 | 96 | Verathos | 67.0 | 1.0 | 16.03 | 440 | rtx4090 | 0.404 | 96 | 40% | RELEASE 3.8d ago |
| 12 | 38 | ChronoLLM | 66.5 | 0.85 | 115 | 1,566 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 2.6d ago |
| 13 | 107 | Minos | 65.1 | 1.0 | 143 | 44,173 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 14 | 85 | Vidaio | 64.3 | 0.85 | 134 | 404 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.1d ago |
| 15 | 108 | Prometheon | 63.8 | 0.85 | 118 | 127 | rtx4090 | 0.658 | 8 | 66% | SCORING_COMMIT 0.9d ago |
| 16 | 81 | Reliquary | 63.3 | 0.85 | 98.45 | 218 | rtx4090 | 0.002 | 42 | 5% | SCORING_COMMIT 0.9d ago |
| 17 | 53 | engy | 59.7 | 0.85 | 33.57 | 226 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.3d ago |
| 18 | 60 | Bitsec.ai | 59.6 | 0.85 | 453 | 453 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 19 | 51 | lium.io | 58.8 | 0.85 | 33.88 | 5,248 | rtx4090 | 0.000 | 53 | 66% | SCORING_COMMIT 2.1d ago |
| 20 | 28 | gm | 58.5 | 0.85 | 24.79 | 1,673 | rtx4090 | 0.045 | 56 | 14% | RELEASE 1.9d ago |
| 21 | 61 | RedTeam | 58.0 | 0.85 | 19.73 | 276 | rtx4090 | 0.000 | 84 | 6% | RELEASE 0.1d ago |
| 22 | 68 | NOVA | 55.2 | 0.6 | 8,690 | 8,690 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 5.9d ago |
| 23 | 41 | Almanac | 55.1 | 1.0 | 10.90 | 23.68 | cpu-small | 0.735 | 78 | 74% | SCORING_COMMIT 9d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,230 | 7,230 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.6d ago |
| 25 | 124 | Swarm | 54.6 | 0.85 | 270 | 2,352 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.00 | cpu-small | 862.7748710480723 |
| 54 | Yanez | -3.22 | a4000 | 1178.6929067466606 |
| 89 | InfiniteQuant | -2.40 | rtx4090 | 111.35289356309836 |
| 13 | Data Universe | -3.11 | rtx4090 | 6.773899896382491 |
| 18 | Zeus | -3.54 | rtx4090 | 2104.2317093416473 |
| 123 | MANTIS | -5.59 | rtx4090 | 104.90244307523331 |
| 75 | Hippius | -6.27 | rtx4090 | 11449.853288702345 |
| 34 | BitMind | -18.72 | a100-80 | 321.9428720819183 |
| 101 | Tag101 | -0.07 | cpu-small | 2.3913472405302865 |
| 6 | Numinous | -0.93 | cpu-small | 334.64608724287433 |
| 50 | Synth | -0.93 | rtx4090 | 115.38879037415728 |
| 104 | Masx.ai | -1.50 | rtx4090 | 8.774989497827889 |
| 88 | Investing | -3.31 | rtx4090 | 675.36541846221 |
| 8 | Vanta | -7.38 | rtx4090 | 1073.9436109358285 |
| 43 | Graphite | -0.46 | cpu-small | 183.48020452761796 |
| 32 | ItsAI | -0.13 | rtx4090 | 11.16938565391472 |
| 19 | blockmachine | -1.46 | rtx4090 | 536.6471643853248 |
| 45 | AlphaRidge.ai | -4.66 | rtx4090 | 11.01729915762099 |
| 22 | Desearch | -5.94 | rtx4090 | 67.0880412340938 |
| 63 | Enigma | -8.14 | rtx4090 | 5351.175080997788 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.28 | 35.0 | 15.0 | 9.91 | 1.0 |
| 23 | 25.0 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.51 | 35.0 | 15.0 | 9.72 | 1.0 |
| 102 | 28.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 26.09 | 35.0 | 11.25 | 9.99 | 0.85 |
| 56 | 26.08 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.51 | 35.0 | 15.0 | 7.86 | 1.0 |
| 1 | 24.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 11 | 33.33 | 21.0 | 15.0 | 10.0 | 0.85 |
| 26 | 11.57 | 35.0 | 11.25 | 9.58 | 1.0 |
| 96 | 11.2 | 35.0 | 11.25 | 9.54 | 1.0 |
| 38 | 18.77 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.64 | 21.0 | 15.0 | 9.49 | 1.0 |
| 85 | 19.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.87 | 35.0 | 11.25 | 9.96 | 0.85 |
| 81 | 18.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 13.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.17 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 14.03 | 35.0 | 11.25 | 8.91 | 0.85 |
| 28 | 12.84 | 35.0 | 11.25 | 9.7 | 0.85 |
| 61 | 11.97 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.83 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.78 | 21.0 | 15.0 | 9.32 | 1.0 |
| 120 | 35.1 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.13 | 21.0 | 11.25 | 9.86 | 0.85 |
