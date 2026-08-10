# RANKING - generated 2026-08-10T00:37:04Z, block 8810464

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
| 1 | 107 | Minos | 78.1 | 1.0 | 112 | 32,924 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 5.8d ago |
| 2 | 76 | Phylax | 76.7 | 1.0 | 67.39 | 203 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 1.1d ago |
| 3 | 98 | NeverPlayAlone | 76.1 | 0.85 | 1,784 | 1,784 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 2.7d ago |
| 4 | 60 | Bitsec.ai | 74.8 | 0.85 | 1,207 | 1,207 | cpu-small | 0.500 | 2 | 50% | SCORING_COMMIT 2.2d ago |
| 5 | 96 | Verathos | 71.8 | 1.0 | 52.14 | 316 | rtx4090 | 0.423 | 42 | 42% | RELEASE 0.5d ago |
| 6 | 67 | Harnyx | 70.7 | 1.0 | 14.90 | 852 | cpu-small | 0.004 | 155 | 22% | SCORING_COMMIT 0.6d ago |
| 7 | 91 | cascade | 70.2 | 0.85 | 792 | 2,714 | rtx4090 | 0.000 | 5 | 48% | RELEASE 4.8d ago |
| 8 | 1 | Apex | 69.9 | 0.85 | 728 | 1,669 | rtx4090 | 0.478 | 4 | 48% | RELEASE 2.2d ago |
| 9 | 41 | Almanac | 69.5 | 1.0 | 11.71 | 34.37 | cpu-small | 0.716 | 65 | 72% | SCORING_COMMIT 3.0d ago |
| 10 | 15 | ORO | 68.4 | 1.0 | 10.36 | 19.78 | cpu-small | 0.000 | 74 | 94% | RELEASE 3.6d ago |
| 11 | 62 | Ridges | 68.2 | 0.85 | 436 | 2,020 | rtx4090 | 0.133 | 7 | 35% | RELEASE 4.1d ago |
| 12 | 26 | Perturb | 68.2 | 1.0 | 21.17 | 39.15 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 3.4d ago |
| 13 | 100 | BASE | 67.0 | 0.85 | 306 | 831 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.1d ago |
| 14 | 38 | ChronoLLM | 65.7 | 0.85 | 217 | 3,649 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 1.6d ago |
| 15 | 21 | AdTAO | 65.4 | 1.0 | 4.64 | 21.53 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 1.4d ago |
| 16 | 80 | OpenRoboto | 65.1 | 0.85 | 171 | 618 | rtx4090 | 0.911 | 4 | 91% | SCORING_COMMIT 1.8d ago |
| 17 | 28 | gm | 63.7 | 0.85 | 115 | 4,241 | rtx4090 | 0.227 | 26 | 42% | RELEASE 2.1d ago |
| 18 | 61 | RedTeam | 62.6 | 0.85 | 81.65 | 342 | rtx4090 | 0.000 | 47 | 7% | RELEASE 0.6d ago |
| 19 | 51 | lium.io | 59.0 | 0.85 | 34.65 | 2,636 | rtx4090 | 0.000 | 47 | 60% | SCORING_COMMIT 2.2d ago |
| 20 | 6 | Numinous | 58.2 | 1.0 | 24.43 | 458 | cpu-small | 0.000 | 18 | 26% | README_TASK_DIFF 11d ago |
| 21 | 56 | Gradients | 56.6 | 0.85 | 474 | 998 | rtx4090 | 0.706 | 7 | 71% | SCORING_COMMIT 12d ago |
| 22 | 85 | Vidaio | 55.6 | 0.85 | 353 | 458 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 13d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,301 | 7,301 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 3.5d ago |
| 24 | 124 | Swarm | 53.9 | 0.85 | 221 | 673 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 8d ago |
| 25 | 2 | DSperse | 53.8 | 0.85 | 4.95 | 104 | rtx4090 | 0.826 | 12 | 83% | RELEASE 3.8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.81 | a4000 | 988.4727461511262 |
| 104 | Masx.ai | -2.31 | rtx4090 | 12.751651858224259 |
| 13 | Data Universe | -3.65 | rtx4090 | 7.571212774231329 |
| 88 | Investing | -4.29 | rtx4090 | 611.2727054718921 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 122.51254457008783 |
| 8 | Vanta | -7.40 | rtx4090 | 3363.5668185598224 |
| 19 | blockmachine | -1.09 | rtx4090 | 253.31254670908234 |
| 18 | Zeus | -2.75 | rtx4090 | 1438.375539490294 |
| 75 | Hippius | -4.44 | rtx4090 | 5.795479212642158 |
| 45 | AlphaRidge.ai | -5.51 | rtx4090 | 8.808504360993222 |
| 123 | MANTIS | -6.26 | rtx4090 | 74.0726051767994 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07511038690010222 |
| 105 | Beam | -4.31 | rtx4090 | 190.58021967603688 |
| 84 | ansuz | -8.15 | rtx4090 | 505.8657306718005 |
| 34 | BitMind | -18.64 | a100-80 | 296.18993077374625 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.68 | 35.0 | 15.0 | 9.4 | 1.0 |
| 76 | 16.69 | 35.0 | 15.0 | 10.0 | 1.0 |
| 98 | 29.57 | 35.0 | 15.0 | 10.0 | 0.85 |
| 60 | 28.03 | 35.0 | 15.0 | 10.0 | 0.85 |
| 96 | 15.69 | 35.0 | 11.25 | 9.87 | 1.0 |
| 67 | 10.93 | 35.0 | 15.0 | 9.82 | 1.0 |
| 91 | 26.37 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 26.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.04 | 35.0 | 15.0 | 9.42 | 1.0 |
| 15 | 9.6 | 35.0 | 15.0 | 8.78 | 1.0 |
| 62 | 24.01 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.24 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 22.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 21.28 | 35.0 | 11.25 | 9.77 | 0.85 |
| 21 | 6.83 | 35.0 | 15.0 | 8.54 | 1.0 |
| 80 | 20.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 18.76 | 35.0 | 11.25 | 9.94 | 0.85 |
| 61 | 17.44 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 14.12 | 35.0 | 11.25 | 9.02 | 0.85 |
| 6 | 12.78 | 21.0 | 15.0 | 9.44 | 1.0 |
| 56 | 24.34 | 21.0 | 11.25 | 10.0 | 0.85 |
| 85 | 23.18 | 21.0 | 11.25 | 10.0 | 0.85 |
| 120 | 35.14 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.34 | 21.0 | 11.25 | 9.85 | 0.85 |
| 2 | 7.05 | 35.0 | 11.25 | 9.99 | 0.85 |
