# RANKING - generated 2026-08-20T03:07:08Z, block 8883205

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
| 1 | 76 | Phylax | 76.7 | 1.0 | 67.78 | 120 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.7d ago |
| 2 | 121 | sundae_bar | 74.5 | 0.85 | 1,109 | 1,109 | cpu-small | 0.601 | 2 | 60% | README_TASK_DIFF 5.3d ago |
| 3 | 67 | Harnyx | 72.3 | 1.0 | 22.79 | 305 | cpu-small | 0.009 | 147 | 9% | SCORING_COMMIT 1.7d ago |
| 4 | 23 | Trishool | 72.0 | 0.85 | 522 | 522 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 1.5d ago |
| 5 | 15 | ORO | 70.3 | 1.0 | 18.18 | 17,350 | cpu-small | 0.000 | 84 | 92% | SCORING_COMMIT 1.3d ago |
| 6 | 56 | Gradients | 69.6 | 0.85 | 653 | 990 | rtx4090 | 0.722 | 5 | 72% | SCORING_COMMIT 2.1d ago |
| 7 | 91 | cascade | 69.1 | 0.85 | 571 | 2,308 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 1.9d ago |
| 8 | 38 | ChronoLLM | 67.5 | 0.85 | 147 | 3,126 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.2d ago |
| 9 | 26 | Perturb | 67.3 | 1.0 | 17.25 | 249 | rtx3060 | 0.000 | 10 | 69% | SCORING_COMMIT 0.1d ago |
| 10 | 96 | Verathos | 66.3 | 1.0 | 13.39 | 288 | rtx4090 | 0.407 | 92 | 41% | RELEASE 1.5d ago |
| 11 | 107 | Minos | 64.5 | 1.0 | 122 | 36,786 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 9d ago |
| 12 | 85 | Vidaio | 64.1 | 0.85 | 127 | 192 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 1.8d ago |
| 13 | 60 | Bitsec.ai | 62.0 | 0.85 | 909 | 909 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 12d ago |
| 14 | 81 | Reliquary | 61.7 | 0.85 | 62.41 | 231 | rtx4090 | 0.003 | 54 | 6% | SCORING_COMMIT 0.2d ago |
| 15 | 55 | NIOME | 61.6 | 0.85 | 58.95 | 494 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 5.3d ago |
| 16 | 28 | gm | 61.5 | 0.85 | 59.06 | 1,132 | rtx4090 | 0.381 | 49 | 38% | RELEASE 0.5d ago |
| 17 | 51 | lium.io | 61.2 | 0.85 | 60.62 | 1,103 | rtx4090 | 0.000 | 49 | 81% | RELEASE 0.3d ago |
| 18 | 53 | engy | 59.7 | 0.85 | 33.57 | 226 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 1.5d ago |
| 19 | 21 | AdTAO | 58.5 | 1.0 | 1.39 | 380 | cpu-small | 0.301 | 16 | 37% | SCORING_COMMIT 1.4d ago |
| 20 | 41 | Almanac | 55.3 | 1.0 | 11.21 | 28.76 | cpu-small | 0.717 | 75 | 72% | SCORING_COMMIT 7d ago |
| 21 | 68 | NOVA | 55.0 | 0.6 | 7,984 | 7,984 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 3.6d ago |
| 22 | 120 | Affine | 54.6 | 0.6 | 6,742 | 6,742 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.3d ago |
| 23 | 124 | Swarm | 54.3 | 0.85 | 245 | 714 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 8d ago |
| 24 | 93 | Bitcast | 53.3 | 0.85 | 174 | 222 | rtx4090 | 0.000 | 4 | 92% | SCORING_COMMIT 22d ago |
| 25 | 33 | ReadyAI | 53.1 | 0.85 | 5.21 | 8.83 | rtx4090 | 0.000 | 245 | 1% | SCORING_COMMIT 1.5d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.96 | cpu-small | 367.28282516981017 |
| 54 | Yanez | -3.17 | a4000 | 1082.0270832311012 |
| 123 | MANTIS | -5.90 | rtx4090 | 87.94123018199853 |
| 75 | Hippius | -6.12 | rtx4090 | 11793.753633076623 |
| 114 | SOMA | -8.12 | rtx4090 | 643.7005269322717 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 151.35486370406366 |
| 104 | Masx.ai | -1.57 | rtx4090 | 7.165617139590243 |
| 13 | Data Universe | -3.73 | rtx4090 | 5.223537014737764 |
| 88 | Investing | -4.40 | rtx4090 | 941.6674981297037 |
| 8 | Vanta | -7.96 | rtx4090 | 2843.4098210572106 |
| 43 | Graphite | -0.82 | cpu-small | 24.519074153616224 |
| 22 | Desearch | -1.25 | rtx4090 | 98.11721933034704 |
| 18 | Zeus | -4.07 | rtx4090 | 1489.3757926878097 |
| 45 | AlphaRidge.ai | -6.05 | rtx4090 | 9.451811603015154 |
| 19 | blockmachine | -7.89 | rtx4090 | 67.59271140240426 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07569025266132685 |
| 105 | Beam | -2.73 | rtx4090 | 75.72139927713167 |
| 84 | ansuz | -8.16 | rtx4090 | 450.58786381702623 |
| 34 | BitMind | -20.89 | a100-80 | 26.95296302815241 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 40 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn78, sn80, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.71 | 35.0 | 15.0 | 10.0 | 1.0 |
| 121 | 27.7 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.52 | 35.0 | 15.0 | 9.81 | 1.0 |
| 23 | 24.72 | 35.0 | 15.0 | 9.99 | 0.85 |
| 15 | 11.67 | 35.0 | 15.0 | 8.62 | 1.0 |
| 56 | 25.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.08 | 35.0 | 11.25 | 9.99 | 0.85 |
| 38 | 19.75 | 35.0 | 15.0 | 9.66 | 0.85 |
| 26 | 11.47 | 35.0 | 11.25 | 9.61 | 1.0 |
| 96 | 10.53 | 35.0 | 11.25 | 9.49 | 1.0 |
| 107 | 19.01 | 21.0 | 15.0 | 9.44 | 1.0 |
| 85 | 19.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 60 | 26.91 | 21.0 | 15.0 | 10.0 | 0.85 |
| 81 | 16.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.17 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 16.18 | 35.0 | 11.25 | 9.88 | 0.85 |
| 51 | 16.28 | 35.0 | 11.25 | 9.44 | 0.85 |
| 53 | 14.0 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 3.43 | 35.0 | 15.0 | 5.09 | 1.0 |
| 41 | 9.88 | 21.0 | 15.0 | 9.39 | 1.0 |
| 68 | 35.49 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.82 | 35.0 | 11.25 | 9.97 | 0.6 |
| 124 | 21.74 | 21.0 | 11.25 | 9.86 | 0.85 |
| 93 | 20.4 | 21.0 | 11.25 | 10.0 | 0.85 |
| 33 | 7.22 | 35.0 | 11.25 | 9.0 | 0.85 |
