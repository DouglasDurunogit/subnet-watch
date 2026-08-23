# RANKING - generated 2026-08-23T12:58:33Z, block 8907762

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
| 1 | 76 | Phylax | 76.8 | 1.0 | 71.61 | 80.20 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 4.1d ago |
| 2 | 67 | Harnyx | 72.6 | 1.0 | 24.22 | 777 | cpu-small | 0.033 | 124 | 20% | SCORING_COMMIT 2.1d ago |
| 3 | 23 | Trishool | 72.2 | 0.85 | 555 | 555 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.4d ago |
| 4 | 102 | ConnitoAI | 71.4 | 0.85 | 1,133 | 2,770 | rtx4090 | 0.250 | 5 | 41% | RELEASE 1.9d ago |
| 5 | 15 | ORO | 71.2 | 1.0 | 22.95 | 40.53 | cpu-small | 0.000 | 78 | 93% | SCORING_COMMIT 1.6d ago |
| 6 | 56 | Gradients | 69.9 | 0.85 | 725 | 1,082 | rtx4090 | 0.730 | 5 | 73% | SCORING_COMMIT 5.5d ago |
| 7 | 91 | cascade | 68.8 | 0.85 | 525 | 1,415 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.6d ago |
| 8 | 1 | Apex | 68.6 | 0.85 | 481 | 1,180 | rtx4090 | 0.545 | 5 | 55% | RELEASE 1.9d ago |
| 9 | 96 | Verathos | 68.1 | 1.0 | 20.93 | 275 | rtx4090 | 0.402 | 92 | 40% | RELEASE 4.9d ago |
| 10 | 26 | Perturb | 67.5 | 1.0 | 18.08 | 259 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.5d ago |
| 11 | 124 | Swarm | 66.6 | 0.85 | 276 | 2,402 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 0.0d ago |
| 12 | 38 | ChronoLLM | 66.5 | 0.85 | 114 | 1,558 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.7d ago |
| 13 | 108 | Prometheon | 65.3 | 0.85 | 181 | 199 | rtx4090 | 0.655 | 5 | 66% | SCORING_COMMIT 2.0d ago |
| 14 | 107 | Minos | 65.2 | 1.0 | 144 | 42,756 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 13d ago |
| 15 | 85 | Vidaio | 64.4 | 0.85 | 139 | 414 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.2d ago |
| 16 | 81 | Reliquary | 63.6 | 0.85 | 110 | 251 | rtx4090 | 0.072 | 38 | 7% | SCORING_COMMIT 0.8d ago |
| 17 | 51 | lium.io | 62.0 | 0.85 | 76.05 | 4,345 | rtx4090 | 0.000 | 53 | 71% | SCORING_COMMIT 3.2d ago |
| 18 | 53 | engy | 60.1 | 0.85 | 37.37 | 12,525 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.4d ago |
| 19 | 60 | Bitsec.ai | 60.0 | 0.85 | 501 | 501 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 16d ago |
| 20 | 28 | gm | 59.6 | 0.85 | 34.34 | 1,366 | rtx4090 | 0.164 | 54 | 16% | RELEASE 3.0d ago |
| 21 | 61 | RedTeam | 57.0 | 0.85 | 14.22 | 309 | rtx4090 | 0.000 | 84 | 7% | RELEASE 1.2d ago |
| 22 | 41 | Almanac | 56.5 | 1.0 | 15.01 | 28.85 | cpu-small | 0.630 | 79 | 63% | SCORING_COMMIT 11d ago |
| 23 | 68 | NOVA | 55.3 | 0.6 | 8,828 | 8,828 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 7.0d ago |
| 24 | 120 | Affine | 54.8 | 0.6 | 7,171 | 7,171 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.7d ago |
| 25 | 80 | OpenRoboto | 53.8 | 0.85 | 206 | 742 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 15d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.30 | a4000 | 1214.2332937038611 |
| 89 | InfiniteQuant | -0.57 | rtx4090 | 114.06723528569263 |
| 13 | Data Universe | -3.11 | rtx4090 | 7.25663784475623 |
| 18 | Zeus | -3.46 | rtx4090 | 1390.3325781813405 |
| 123 | MANTIS | -5.69 | rtx4090 | 112.86334623364299 |
| 75 | Hippius | -6.39 | rtx4090 | 11820.144667135603 |
| 34 | BitMind | -18.65 | a100-80 | 327.66138856675695 |
| 6 | Numinous | -0.93 | cpu-small | 177.57215221399377 |
| 50 | Synth | -1.71 | rtx4090 | 65.88933623983151 |
| 88 | Investing | -3.02 | rtx4090 | 651.8321591170596 |
| 104 | Masx.ai | -4.09 | rtx4090 | 12.433630875181274 |
| 8 | Vanta | -7.37 | rtx4090 | 1094.590338918024 |
| 43 | Graphite | -0.23 | cpu-small | 188.11668941898876 |
| 19 | blockmachine | -0.99 | rtx4090 | 551.7681702415427 |
| 22 | Desearch | -1.01 | rtx4090 | 47.796643601988315 |
| 45 | AlphaRidge.ai | -5.26 | rtx4090 | 10.80574395143643 |
| 63 | Enigma | -8.14 | rtx4090 | 5449.577615800539 |
| 105 | Beam | -2.20 | rtx4090 | 80.38877049398192 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06879671973329662 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.93 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 12.75 | 35.0 | 15.0 | 9.83 | 1.0 |
| 23 | 24.97 | 35.0 | 15.0 | 9.99 | 0.85 |
| 102 | 27.78 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 12.54 | 35.0 | 15.0 | 8.66 | 1.0 |
| 56 | 26.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.75 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.4 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 12.2 | 35.0 | 11.25 | 9.64 | 1.0 |
| 26 | 11.65 | 35.0 | 11.25 | 9.58 | 1.0 |
| 124 | 22.21 | 35.0 | 11.25 | 9.86 | 0.85 |
| 38 | 18.75 | 35.0 | 15.0 | 9.51 | 0.85 |
| 108 | 20.56 | 35.0 | 11.25 | 9.98 | 0.85 |
| 107 | 19.67 | 21.0 | 15.0 | 9.48 | 1.0 |
| 85 | 19.51 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 18.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 17.16 | 35.0 | 11.25 | 9.5 | 0.85 |
| 53 | 14.41 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 24.56 | 21.0 | 15.0 | 10.0 | 0.85 |
| 28 | 14.08 | 35.0 | 11.25 | 9.78 | 0.85 |
| 61 | 10.76 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.95 | 21.0 | 15.0 | 9.5 | 1.0 |
| 68 | 35.89 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 35.07 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 21.07 | 21.0 | 11.25 | 10.0 | 0.85 |
