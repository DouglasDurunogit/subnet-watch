# RANKING - generated 2026-08-07T10:37:39Z, block 8791867

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
| 1 | 11 | TrajectoryRL | 79.9 | 0.85 | 5,462 | 5,462 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 5.0d ago |
| 2 | 107 | Minos | 77.8 | 1.0 | 105 | 31,004 | cpu-small | 0.000 | 20 | 89% | WEIGHTS_VERSION_BUMP 3.3d ago |
| 3 | 76 | Phylax | 76.8 | 1.0 | 69.05 | 250 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 4.7d ago |
| 4 | 67 | Harnyx | 72.0 | 1.0 | 21.19 | 767 | cpu-small | 0.031 | 131 | 20% | SCORING_COMMIT 0.3d ago |
| 5 | 102 | ConnitoAI | 70.5 | 0.85 | 854 | 2,064 | rtx4090 | 0.250 | 6 | 37% | RELEASE 6.5d ago |
| 6 | 62 | Ridges | 69.0 | 0.85 | 553 | 2,001 | rtx4090 | 0.133 | 7 | 35% | RELEASE 1.5d ago |
| 7 | 91 | cascade | 68.8 | 0.85 | 527 | 1,493 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.3d ago |
| 8 | 15 | ORO | 68.3 | 1.0 | 11.43 | 18.68 | cpu-small | 0.000 | 72 | 93% | RELEASE 1.0d ago |
| 9 | 26 | Perturb | 68.2 | 1.0 | 21.28 | 38.91 | rtx3060 | 0.508 | 11 | 51% | SCORING_COMMIT 0.8d ago |
| 10 | 96 | Verathos | 68.0 | 1.0 | 20.30 | 871 | rtx4090 | 0.411 | 43 | 41% | RELEASE 0.4d ago |
| 11 | 41 | Almanac | 67.6 | 1.0 | 7.54 | 44.72 | cpu-small | 0.798 | 62 | 80% | SCORING_COMMIT 0.4d ago |
| 12 | 124 | Swarm | 65.7 | 0.85 | 211 | 607 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 5.9d ago |
| 13 | 21 | AdTAO | 65.5 | 1.0 | 4.71 | 21.80 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.4d ago |
| 14 | 74 | Gittensor | 65.3 | 0.85 | 187 | 403 | rtx4090 | 0.000 | 9 | 19% | RELEASE 0.4d ago |
| 15 | 61 | RedTeam | 62.8 | 0.85 | 84.65 | 195 | rtx4090 | 0.000 | 38 | 6% | RELEASE 1.9d ago |
| 16 | 85 | Vidaio | 58.0 | 0.85 | 725 | 725 | rtx4090 | 0.000 | 10 | 21% | SCORING_COMMIT 10d ago |
| 17 | 51 | lium.io | 57.4 | 0.85 | 23.77 | 2,751 | rtx4090 | 0.000 | 42 | 68% | SCORING_COMMIT 3.1d ago |
| 18 | 2 | DSperse | 56.8 | 0.85 | 13.70 | 146 | rtx4090 | 0.826 | 8 | 83% | RELEASE 1.2d ago |
| 19 | 56 | Gradients | 56.4 | 0.85 | 451 | 952 | rtx4090 | 0.700 | 7 | 70% | SCORING_COMMIT 9d ago |
| 20 | 101 | Tag101 | 56.0 | 1.0 | 0.01 | 0.76 | cpu-small | 0.902 | 243 | 90% | SCORING_COMMIT 6.7d ago |
| 21 | 9 | iota | 55.8 | 0.6 | 11,133 | 11,133 | rtx4090 | 0.399 | 3 | 56% | RELEASE 6.7d ago |
| 22 | 120 | Affine | 54.6 | 0.6 | 6,646 | 6,646 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 0.9d ago |
| 23 | 38 | ChronoLLM | 53.8 | 0.85 | 218 | 3,655 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 8d ago |
| 24 | 97 | Albedo | 52.7 | 0.6 | 2,955 | 2,955 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.4d ago |
| 25 | 80 | OpenRoboto | 51.5 | 0.85 | 103 | 382 | rtx4090 | 0.907 | 4 | 91% | SCORING_COMMIT 7d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -3.87 | a4000 | 1039.436380258595 |
| 104 | Masx.ai | -1.51 | rtx4090 | 7.436733654987842 |
| 13 | Data Universe | -3.28 | rtx4090 | 6.608299372705893 |
| 88 | Investing | -6.91 | rtx4090 | 625.5706849622773 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 157.02309694634766 |
| 8 | Vanta | -7.44 | rtx4090 | 3172.5931301954224 |
| 32 | ItsAI | -0.25 | rtx4090 | 10.472549157232223 |
| 22 | Desearch | -0.40 | rtx4090 | 57.534399039430824 |
| 19 | blockmachine | -1.10 | rtx4090 | 169.46456641879982 |
| 45 | AlphaRidge.ai | -2.67 | rtx4090 | 44.05962841633756 |
| 75 | Hippius | -4.55 | rtx4090 | 5.463299480401854 |
| 18 | Zeus | -5.10 | rtx4090 | 1171.7929460126754 |
| 123 | MANTIS | -6.15 | rtx4090 | 77.76468640999039 |
| 63 | Enigma | -8.15 | rtx4090 | 4765.613264042351 |
| 84 | ansuz | -8.15 | rtx4090 | 479.2946732279567 |
| 34 | BitMind | -18.50 | a100-80 | 282.3150871404488 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 37 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn28, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn121, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 11 | 33.99 | 35.0 | 15.0 | 10.0 | 0.85 |
| 107 | 18.43 | 35.0 | 15.0 | 9.39 | 1.0 |
| 76 | 16.78 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.24 | 35.0 | 15.0 | 9.76 | 1.0 |
| 102 | 26.67 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.95 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.76 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 9.96 | 35.0 | 15.0 | 8.37 | 1.0 |
| 26 | 12.26 | 35.0 | 11.25 | 9.7 | 1.0 |
| 96 | 12.08 | 35.0 | 11.25 | 9.68 | 1.0 |
| 41 | 8.47 | 35.0 | 15.0 | 9.14 | 1.0 |
| 124 | 21.16 | 35.0 | 11.25 | 9.85 | 0.85 |
| 21 | 6.88 | 35.0 | 15.0 | 8.63 | 1.0 |
| 74 | 20.68 | 35.0 | 11.25 | 9.95 | 0.85 |
| 61 | 17.58 | 35.0 | 11.25 | 10.0 | 0.85 |
| 85 | 26.02 | 21.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.68 | 35.0 | 11.25 | 8.64 | 0.85 |
| 2 | 10.62 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.15 | 21.0 | 11.25 | 10.0 | 0.85 |
| 101 | 0.04 | 35.0 | 15.0 | 6.01 | 1.0 |
| 9 | 36.8 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.77 | 35.0 | 11.25 | 9.99 | 0.6 |
| 38 | 21.28 | 21.0 | 11.25 | 9.76 | 0.85 |
| 97 | 31.57 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 18.35 | 21.0 | 11.25 | 10.0 | 0.85 |
