# RANKING - generated 2026-08-20T13:26:28Z, block 8886302

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
| 1 | 76 | Phylax | 76.7 | 1.0 | 69.13 | 123 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 1.2d ago |
| 2 | 23 | Trishool | 72.0 | 0.85 | 525 | 525 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 0.4d ago |
| 3 | 67 | Harnyx | 72.0 | 1.0 | 21.19 | 282 | cpu-small | 0.052 | 174 | 8% | SCORING_COMMIT 0.2d ago |
| 4 | 15 | ORO | 70.3 | 1.0 | 18.60 | 18,190 | cpu-small | 0.000 | 82 | 92% | SCORING_COMMIT 1.8d ago |
| 5 | 56 | Gradients | 69.6 | 0.85 | 665 | 1,012 | rtx4090 | 0.723 | 5 | 72% | SCORING_COMMIT 2.6d ago |
| 6 | 1 | Apex | 69.6 | 0.85 | 653 | 1,446 | rtx4090 | 0.519 | 4 | 52% | RELEASE 0.7d ago |
| 7 | 91 | cascade | 69.2 | 0.85 | 591 | 2,388 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 2.4d ago |
| 8 | 38 | ChronoLLM | 67.6 | 0.85 | 151 | 3,204 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.7d ago |
| 9 | 26 | Perturb | 67.2 | 1.0 | 16.83 | 243 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 0.5d ago |
| 10 | 96 | Verathos | 66.2 | 1.0 | 13.11 | 367 | rtx4090 | 0.406 | 96 | 41% | RELEASE 1.9d ago |
| 11 | 107 | Minos | 64.5 | 1.0 | 128 | 37,833 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 10d ago |
| 12 | 85 | Vidaio | 64.1 | 0.85 | 128 | 400 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 2.3d ago |
| 13 | 108 | Prometheon | 63.8 | 0.85 | 116 | 171 | rtx4090 | 0.659 | 7 | 66% | SCORING_COMMIT 0.5d ago |
| 14 | 28 | gm | 63.7 | 0.85 | 114 | 832 | rtx4090 | 0.000 | 49 | 8% | RELEASE 0.0d ago |
| 15 | 60 | Bitsec.ai | 62.1 | 0.85 | 943 | 943 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 13d ago |
| 16 | 81 | Reliquary | 61.8 | 0.85 | 64.13 | 234 | rtx4090 | 0.002 | 53 | 6% | SCORING_COMMIT 0.7d ago |
| 17 | 51 | lium.io | 61.7 | 0.85 | 69.42 | 1,156 | rtx4090 | 0.000 | 44 | 82% | SCORING_COMMIT 0.2d ago |
| 18 | 55 | NIOME | 61.6 | 0.85 | 59.46 | 499 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 5.7d ago |
| 19 | 53 | engy | 59.9 | 0.85 | 35.75 | 238 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 1.9d ago |
| 20 | 41 | Almanac | 55.3 | 1.0 | 11.28 | 24.20 | cpu-small | 0.722 | 76 | 72% | SCORING_COMMIT 8d ago |
| 21 | 68 | NOVA | 55.1 | 0.6 | 8,259 | 8,259 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 4.0d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 6,898 | 6,898 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.7d ago |
| 23 | 124 | Swarm | 54.4 | 0.85 | 251 | 732 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 9d ago |
| 24 | 80 | OpenRoboto | 53.7 | 0.85 | 198 | 714 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 12d ago |
| 25 | 33 | ReadyAI | 53.4 | 0.85 | 5.72 | 11.44 | rtx4090 | 0.000 | 243 | 1% | SCORING_COMMIT 1.9d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.96 | cpu-small | 374.20864793647735 |
| 54 | Yanez | -3.85 | a4000 | 1058.9182321288993 |
| 123 | MANTIS | -5.73 | rtx4090 | 92.74848796550317 |
| 75 | Hippius | -6.08 | rtx4090 | 12552.266225468366 |
| 114 | SOMA | -8.12 | rtx4090 | 4212.395060032062 |
| 89 | InfiniteQuant | -8.17 | rtx4090 | 126.43466209927776 |
| 104 | Masx.ai | -0.72 | rtx4090 | 9.091476471931061 |
| 13 | Data Universe | -3.64 | rtx4090 | 5.504305343429203 |
| 88 | Investing | -4.34 | rtx4090 | 972.8894482995374 |
| 8 | Vanta | -7.95 | rtx4090 | 3019.214960350244 |
| 43 | Graphite | -0.79 | cpu-small | 25.03933003952157 |
| 18 | Zeus | -5.33 | rtx4090 | 1106.4706187075785 |
| 45 | AlphaRidge.ai | -5.62 | rtx4090 | 7.399831084462304 |
| 19 | blockmachine | -7.88 | rtx4090 | 69.39466138476354 |
| 63 | Enigma | -8.14 | rtx4090 | 5077.3748612429545 |
| 105 | Beam | -2.47 | rtx4090 | 77.45786077424832 |
| 84 | ansuz | -8.16 | rtx4090 | 0.06344821514056029 |
| 34 | BitMind | -20.10 | a100-80 | 29.20695731258273 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn78, sn87, sn92, sn94, sn95, sn109, sn111, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.79 | 35.0 | 15.0 | 9.9 | 1.0 |
| 23 | 24.75 | 35.0 | 15.0 | 9.99 | 0.85 |
| 67 | 12.24 | 35.0 | 15.0 | 9.73 | 1.0 |
| 15 | 11.75 | 35.0 | 15.0 | 8.55 | 1.0 |
| 56 | 25.68 | 35.0 | 11.25 | 10.0 | 0.85 |
| 1 | 25.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.21 | 35.0 | 11.25 | 9.99 | 0.85 |
| 38 | 19.84 | 35.0 | 15.0 | 9.66 | 0.85 |
| 26 | 11.38 | 35.0 | 11.25 | 9.59 | 1.0 |
| 96 | 10.45 | 35.0 | 11.25 | 9.47 | 1.0 |
| 107 | 19.18 | 21.0 | 15.0 | 9.34 | 1.0 |
| 85 | 19.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.83 | 35.0 | 11.25 | 9.97 | 0.85 |
| 28 | 18.74 | 35.0 | 11.25 | 9.94 | 0.85 |
| 60 | 27.06 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 16.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.81 | 35.0 | 11.25 | 9.5 | 0.85 |
| 55 | 16.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 14.24 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.91 | 21.0 | 15.0 | 9.38 | 1.0 |
| 68 | 35.63 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.91 | 35.0 | 11.25 | 9.97 | 0.6 |
| 124 | 21.84 | 21.0 | 11.25 | 9.86 | 0.85 |
| 80 | 20.91 | 21.0 | 11.25 | 10.0 | 0.85 |
| 33 | 7.52 | 35.0 | 11.25 | 9.02 | 0.85 |
