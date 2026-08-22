# RANKING - generated 2026-08-22T21:02:12Z, block 8902980

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
| 1 | 76 | Phylax | 77.0 | 1.0 | 75.29 | 133 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.5d ago |
| 2 | 67 | Harnyx | 72.4 | 1.0 | 22.95 | 119 | cpu-small | 0.052 | 151 | 12% | SCORING_COMMIT 1.4d ago |
| 3 | 62 | Ridges | 71.7 | 0.85 | 1,214 | 2,990 | rtx4090 | 0.000 | 6 | 39% | RELEASE 3.9d ago |
| 4 | 15 | ORO | 70.3 | 1.0 | 19.22 | 22,891 | cpu-small | 0.000 | 61 | 95% | SCORING_COMMIT 0.9d ago |
| 5 | 56 | Gradients | 69.9 | 0.85 | 729 | 1,076 | rtx4090 | 0.728 | 5 | 73% | SCORING_COMMIT 4.9d ago |
| 6 | 91 | cascade | 69.8 | 0.85 | 702 | 2,835 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 1.9d ago |
| 7 | 1 | Apex | 68.6 | 0.85 | 493 | 1,259 | rtx4090 | 0.519 | 5 | 52% | RELEASE 1.3d ago |
| 8 | 102 | ConnitoAI | 68.5 | 0.85 | 479 | 2,303 | rtx4090 | 0.250 | 7 | 33% | RELEASE 1.2d ago |
| 9 | 96 | Verathos | 67.8 | 1.0 | 19.55 | 440 | rtx4090 | 0.402 | 91 | 40% | RELEASE 4.2d ago |
| 10 | 26 | Perturb | 67.5 | 1.0 | 17.95 | 257 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 2.8d ago |
| 11 | 38 | ChronoLLM | 66.5 | 0.85 | 115 | 1,569 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.0d ago |
| 12 | 107 | Minos | 65.3 | 1.0 | 148 | 42,731 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 12d ago |
| 13 | 85 | Vidaio | 64.2 | 0.85 | 129 | 403 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 4.6d ago |
| 14 | 108 | Prometheon | 63.9 | 0.85 | 119 | 128 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.3d ago |
| 15 | 81 | Reliquary | 63.3 | 0.85 | 98.68 | 221 | rtx4090 | 0.002 | 43 | 5% | SCORING_COMMIT 0.1d ago |
| 16 | 51 | lium.io | 60.9 | 0.85 | 57.36 | 4,332 | rtx4090 | 0.000 | 52 | 69% | SCORING_COMMIT 2.5d ago |
| 17 | 60 | Bitsec.ai | 59.8 | 0.85 | 479 | 479 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 18 | 53 | engy | 59.4 | 0.85 | 30.23 | 207 | rtx4090 | 0.000 | 144 | 63% | RELEASE 0.7d ago |
| 19 | 28 | gm | 58.9 | 0.85 | 28.06 | 1,603 | rtx4090 | 0.078 | 54 | 15% | RELEASE 2.3d ago |
| 20 | 61 | RedTeam | 57.7 | 0.85 | 18.08 | 284 | rtx4090 | 0.000 | 87 | 6% | RELEASE 0.5d ago |
| 21 | 68 | NOVA | 55.3 | 0.6 | 8,737 | 8,737 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.3d ago |
| 22 | 41 | Almanac | 55.2 | 1.0 | 11.26 | 23.87 | cpu-small | 0.732 | 78 | 73% | SCORING_COMMIT 10d ago |
| 23 | 120 | Affine | 54.8 | 0.6 | 7,146 | 7,146 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.0d ago |
| 24 | 124 | Swarm | 54.6 | 0.85 | 271 | 2,366 | rtx4090 | 0.000 | 21 | 30% | SCORING_COMMIT 11d ago |
| 25 | 80 | OpenRoboto | 53.8 | 0.85 | 204 | 734 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 15d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -3.17 | a4000 | 1225.5500351988098 |
| 13 | Data Universe | -2.56 | rtx4090 | 6.7796254989699305 |
| 89 | InfiniteQuant | -3.27 | rtx4090 | 117.88220854565152 |
| 18 | Zeus | -4.39 | rtx4090 | 1710.8992044842657 |
| 123 | MANTIS | -5.69 | rtx4090 | 106.54409375509972 |
| 75 | Hippius | -6.43 | rtx4090 | 11577.201608704529 |
| 34 | BitMind | -18.74 | a100-80 | 325.19892733873183 |
| 6 | Numinous | -0.94 | cpu-small | 288.9394246873387 |
| 50 | Synth | -1.76 | rtx4090 | 51.922739360340145 |
| 104 | Masx.ai | -1.82 | rtx4090 | 8.248517254164168 |
| 88 | Investing | -3.26 | rtx4090 | 680.4442794998024 |
| 8 | Vanta | -7.38 | rtx4090 | 1086.0208713155946 |
| 43 | Graphite | -0.45 | cpu-small | 192.26880271775227 |
| 19 | blockmachine | -1.05 | rtx4090 | 547.0945603827357 |
| 22 | Desearch | -4.09 | rtx4090 | 76.66762730541585 |
| 45 | AlphaRidge.ai | -4.86 | rtx4090 | 10.254491231632318 |
| 63 | Enigma | -8.14 | rtx4090 | 0.0831812729143519 |
| 105 | Beam | -2.18 | rtx4090 | 79.91702265314086 |
| 84 | ansuz | -8.15 | rtx4090 | 0.06994212871030163 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 38 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 17.12 | 35.0 | 15.0 | 9.9 | 1.0 |
| 67 | 12.55 | 35.0 | 15.0 | 9.83 | 1.0 |
| 62 | 28.06 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 11.88 | 35.0 | 15.0 | 8.47 | 1.0 |
| 56 | 26.04 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.9 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.5 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 24.38 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 11.94 | 35.0 | 11.25 | 9.62 | 1.0 |
| 26 | 11.62 | 35.0 | 11.25 | 9.58 | 1.0 |
| 38 | 18.77 | 35.0 | 15.0 | 9.52 | 0.85 |
| 107 | 19.77 | 21.0 | 15.0 | 9.5 | 1.0 |
| 85 | 19.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.9 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 18.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.06 | 35.0 | 11.25 | 9.35 | 0.85 |
| 60 | 24.39 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 13.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 13.31 | 35.0 | 11.25 | 9.73 | 0.85 |
| 61 | 11.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.85 | 35.0 | 11.25 | 10.0 | 0.6 |
| 41 | 9.9 | 21.0 | 15.0 | 9.34 | 1.0 |
| 120 | 35.05 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 22.15 | 21.0 | 11.25 | 9.86 | 0.85 |
| 80 | 21.02 | 21.0 | 11.25 | 10.0 | 0.85 |
