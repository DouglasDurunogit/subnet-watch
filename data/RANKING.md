# RANKING - generated 2026-08-08T20:44:40Z, block 8802102

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
| 1 | 11 | TrajectoryRL | 79.6 | 0.85 | 4,951 | 4,951 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 6.4d ago |
| 2 | 107 | Minos | 78.3 | 1.0 | 117 | 34,767 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 4.7d ago |
| 3 | 76 | Phylax | 76.6 | 1.0 | 65.17 | 196 | cpu-small | 0.000 | 10 | 33% | SCORING_COMMIT 6.2d ago |
| 4 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,222 | 1,222 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 1.1d ago |
| 5 | 67 | Harnyx | 71.2 | 1.0 | 17.04 | 741 | cpu-small | 0.017 | 142 | 19% | SCORING_COMMIT 1.7d ago |
| 6 | 91 | cascade | 70.2 | 0.85 | 783 | 2,682 | rtx4090 | 0.000 | 5 | 48% | RELEASE 3.7d ago |
| 7 | 96 | Verathos | 69.7 | 1.0 | 30.67 | 239 | rtx4090 | 0.439 | 59 | 44% | RELEASE 0.1d ago |
| 8 | 1 | Apex | 69.5 | 0.85 | 640 | 1,587 | rtx4090 | 0.451 | 4 | 45% | RELEASE 1.0d ago |
| 9 | 62 | Ridges | 69.0 | 0.85 | 557 | 2,014 | rtx4090 | 0.133 | 7 | 35% | RELEASE 3.0d ago |
| 10 | 26 | Perturb | 68.3 | 1.0 | 21.64 | 40.60 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 2.2d ago |
| 11 | 41 | Almanac | 68.2 | 1.0 | 8.76 | 44.68 | cpu-small | 0.760 | 66 | 76% | SCORING_COMMIT 1.8d ago |
| 12 | 15 | ORO | 67.2 | 1.0 | 9.14 | 19.26 | cpu-small | 0.000 | 70 | 94% | RELEASE 2.4d ago |
| 13 | 21 | AdTAO | 65.6 | 1.0 | 4.79 | 22.12 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.2d ago |
| 14 | 38 | ChronoLLM | 65.5 | 0.85 | 207 | 3,485 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 0.5d ago |
| 15 | 80 | OpenRoboto | 63.3 | 0.85 | 100.00 | 371 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 0.7d ago |
| 16 | 61 | RedTeam | 61.6 | 0.85 | 60.16 | 182 | rtx4090 | 0.000 | 43 | 6% | RELEASE 0.9d ago |
| 17 | 28 | gm | 60.6 | 0.85 | 45.44 | 3,754 | rtx4090 | 0.151 | 22 | 41% | RELEASE 1.0d ago |
| 18 | 51 | lium.io | 59.0 | 0.85 | 34.43 | 3,194 | rtx4090 | 0.000 | 47 | 68% | SCORING_COMMIT 1.0d ago |
| 19 | 85 | Vidaio | 57.0 | 0.85 | 526 | 535 | rtx4090 | 0.000 | 10 | 16% | SCORING_COMMIT 12d ago |
| 20 | 56 | Gradients | 56.5 | 0.85 | 461 | 972 | rtx4090 | 0.704 | 7 | 70% | SCORING_COMMIT 11d ago |
| 21 | 74 | Gittensor | 55.4 | 0.85 | 10.89 | 235 | rtx4090 | 0.631 | 16 | 63% | RELEASE 1.2d ago |
| 22 | 120 | Affine | 54.7 | 0.6 | 6,867 | 6,867 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.3d ago |
| 23 | 124 | Swarm | 53.8 | 0.85 | 211 | 642 | rtx4090 | 0.000 | 23 | 11% | SCORING_COMMIT 7d ago |
| 24 | 100 | BASE | 53.0 | 0.6 | 3,321 | 3,321 | rtx4090 | 0.000 | 1 | 100% | RELEASE 0.0d ago |
| 25 | 97 | Albedo | 52.7 | 0.6 | 2,954 | 2,954 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 6.8d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.08 | a4000 | 1034.5228840804205 |
| 104 | Masx.ai | -1.51 | rtx4090 | 10.581135712626663 |
| 13 | Data Universe | -3.08 | rtx4090 | 7.231133560868652 |
| 88 | Investing | -6.19 | rtx4090 | 380.8393372954056 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 128.88974637764247 |
| 8 | Vanta | -7.42 | rtx4090 | 3247.113158013701 |
| 22 | Desearch | -1.14 | rtx4090 | 64.84884245341317 |
| 19 | blockmachine | -1.21 | rtx4090 | 195.38855248558377 |
| 75 | Hippius | -4.68 | rtx4090 | 5.270213708010375 |
| 18 | Zeus | -4.73 | rtx4090 | 907.7240953675764 |
| 45 | AlphaRidge.ai | -5.12 | rtx4090 | 11.967085013184873 |
| 123 | MANTIS | -6.22 | rtx4090 | 73.89843732096361 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07515984178573082 |
| 105 | Beam | -3.64 | rtx4090 | 212.60004911519832 |
| 84 | ansuz | -8.15 | rtx4090 | 499.0082479675092 |
| 34 | BitMind | -19.29 | a100-80 | 288.82896991768973 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn9, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.6 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.84 | 35.0 | 15.0 | 9.44 | 1.0 |
| 76 | 16.56 | 35.0 | 15.0 | 10.0 | 1.0 |
| 60 | 28.08 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 11.43 | 35.0 | 15.0 | 9.82 | 1.0 |
| 91 | 26.33 | 35.0 | 11.25 | 9.99 | 0.85 |
| 96 | 13.65 | 35.0 | 11.25 | 9.78 | 1.0 |
| 1 | 25.53 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.98 | 35.0 | 11.25 | 10.0 | 0.85 |
| 26 | 12.32 | 35.0 | 11.25 | 9.69 | 1.0 |
| 41 | 9.0 | 35.0 | 15.0 | 9.25 | 1.0 |
| 15 | 9.15 | 35.0 | 15.0 | 8.03 | 1.0 |
| 21 | 6.94 | 35.0 | 15.0 | 8.62 | 1.0 |
| 38 | 21.09 | 35.0 | 11.25 | 9.76 | 0.85 |
| 80 | 18.23 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 16.25 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.16 | 35.0 | 11.25 | 9.85 | 0.85 |
| 51 | 14.09 | 35.0 | 11.25 | 9.04 | 0.85 |
| 85 | 24.75 | 21.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.23 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 9.78 | 35.0 | 11.25 | 9.09 | 0.85 |
| 120 | 34.9 | 35.0 | 11.25 | 9.99 | 0.6 |
| 124 | 21.15 | 21.0 | 11.25 | 9.84 | 0.85 |
| 100 | 32.03 | 35.0 | 11.25 | 10.0 | 0.6 |
| 97 | 31.57 | 35.0 | 11.25 | 9.99 | 0.6 |
