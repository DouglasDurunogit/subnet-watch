# RANKING - generated 2026-08-23T07:10:26Z, block 8906021

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
| 1 | 76 | Phylax | 76.7 | 1.0 | 69.58 | 77.71 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 3.9d ago |
| 2 | 67 | Harnyx | 72.5 | 1.0 | 23.64 | 760 | cpu-small | 0.055 | 120 | 20% | SCORING_COMMIT 1.9d ago |
| 3 | 23 | Trishool | 72.2 | 0.85 | 549 | 549 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 3.1d ago |
| 4 | 62 | Ridges | 71.6 | 0.85 | 1,186 | 2,920 | rtx4090 | 0.000 | 6 | 39% | RELEASE 4.3d ago |
| 5 | 102 | ConnitoAI | 71.2 | 0.85 | 1,052 | 2,883 | rtx4090 | 0.250 | 5 | 42% | RELEASE 1.6d ago |
| 6 | 15 | ORO | 70.6 | 1.0 | 20.89 | 38.79 | cpu-small | 0.000 | 78 | 93% | SCORING_COMMIT 1.3d ago |
| 7 | 56 | Gradients | 69.8 | 0.85 | 706 | 1,050 | rtx4090 | 0.729 | 5 | 73% | SCORING_COMMIT 5.3d ago |
| 8 | 91 | cascade | 69.7 | 0.85 | 682 | 2,751 | rtx4090 | 0.000 | 5 | 52% | SCORING_COMMIT 2.3d ago |
| 9 | 1 | Apex | 68.5 | 0.85 | 479 | 1,176 | rtx4090 | 0.533 | 5 | 53% | RELEASE 1.7d ago |
| 10 | 96 | Verathos | 67.7 | 1.0 | 19.18 | 263 | rtx4090 | 0.402 | 92 | 40% | RELEASE 4.6d ago |
| 11 | 26 | Perturb | 67.3 | 1.0 | 17.47 | 251 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.2d ago |
| 12 | 38 | ChronoLLM | 66.4 | 0.85 | 111 | 1,512 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.4d ago |
| 13 | 107 | Minos | 65.6 | 1.0 | 161 | 42,331 | cpu-small | 0.000 | 19 | 90% | README_TASK_DIFF 13d ago |
| 14 | 98 | NeverPlayAlone | 64.4 | 0.85 | 1,875 | 1,875 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 16d ago |
| 15 | 85 | Vidaio | 64.1 | 0.85 | 126 | 393 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 5.0d ago |
| 16 | 108 | Prometheon | 63.8 | 0.85 | 117 | 126 | rtx4090 | 0.655 | 8 | 66% | SCORING_COMMIT 1.7d ago |
| 17 | 81 | Reliquary | 63.0 | 0.85 | 91.44 | 233 | rtx4090 | 0.091 | 39 | 9% | SCORING_COMMIT 0.5d ago |
| 18 | 28 | gm | 60.7 | 0.85 | 47.92 | 1,285 | rtx4090 | 0.094 | 54 | 12% | RELEASE 2.7d ago |
| 19 | 51 | lium.io | 60.1 | 0.85 | 46.49 | 4,283 | rtx4090 | 0.000 | 54 | 71% | SCORING_COMMIT 3.0d ago |
| 20 | 60 | Bitsec.ai | 59.8 | 0.85 | 469 | 469 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 15d ago |
| 21 | 53 | engy | 59.7 | 0.85 | 33.81 | 227 | rtx4090 | 0.000 | 144 | 63% | RELEASE 1.1d ago |
| 22 | 61 | RedTeam | 57.2 | 0.85 | 15.47 | 293 | rtx4090 | 0.000 | 85 | 6% | RELEASE 1.0d ago |
| 23 | 41 | Almanac | 56.5 | 1.0 | 15.00 | 28.69 | cpu-small | 0.620 | 79 | 62% | SCORING_COMMIT 10d ago |
| 24 | 68 | NOVA | 55.2 | 0.6 | 8,539 | 8,539 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 6.7d ago |
| 25 | 120 | Affine | 54.7 | 0.6 | 6,996 | 6,996 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.4d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 21 | AdTAO | -0.30 | cpu-small | 5.744389975163119 |
| 54 | Yanez | -3.27 | a4000 | 1195.3805258019295 |
| 89 | InfiniteQuant | -3.00 | rtx4090 | 110.21538533432151 |
| 13 | Data Universe | -3.47 | rtx4090 | 7.1725077307141945 |
| 18 | Zeus | -4.52 | rtx4090 | 1409.5050891279561 |
| 123 | MANTIS | -5.74 | rtx4090 | 107.94655510808354 |
| 75 | Hippius | -6.46 | rtx4090 | 11410.136838944401 |
| 34 | BitMind | -18.74 | a100-80 | 317.760005532331 |
| 6 | Numinous | -0.93 | cpu-small | 172.1275497122924 |
| 104 | Masx.ai | -1.80 | rtx4090 | 10.771219243412641 |
| 50 | Synth | -2.21 | rtx4090 | 61.951335945874646 |
| 88 | Investing | -3.20 | rtx4090 | 629.5959626535263 |
| 8 | Vanta | -7.39 | rtx4090 | 1061.5299202224794 |
| 43 | Graphite | -0.26 | cpu-small | 181.35931246941067 |
| 32 | ItsAI | -0.23 | rtx4090 | 11.468711554117599 |
| 22 | Desearch | -0.86 | rtx4090 | 36.842722279827534 |
| 19 | blockmachine | -1.21 | rtx4090 | 535.0115913380278 |
| 45 | AlphaRidge.ai | -5.54 | rtx4090 | 8.896600214129654 |
| 63 | Enigma | -8.14 | rtx4090 | 0.08131313307929525 |
| 105 | Beam | -2.36 | rtx4090 | 78.07242401672003 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.81 | 35.0 | 15.0 | 9.89 | 1.0 |
| 67 | 12.66 | 35.0 | 15.0 | 9.85 | 1.0 |
| 23 | 24.92 | 35.0 | 15.0 | 9.99 | 0.85 |
| 62 | 27.96 | 35.0 | 11.25 | 10.0 | 0.85 |
| 102 | 27.49 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 12.19 | 35.0 | 15.0 | 8.4 | 1.0 |
| 56 | 25.92 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.78 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 24.39 | 35.0 | 11.25 | 10.0 | 0.85 |
| 96 | 11.87 | 35.0 | 11.25 | 9.62 | 1.0 |
| 26 | 11.52 | 35.0 | 11.25 | 9.58 | 1.0 |
| 38 | 18.63 | 35.0 | 15.0 | 9.51 | 0.85 |
| 107 | 20.09 | 21.0 | 15.0 | 9.55 | 1.0 |
| 98 | 29.77 | 21.0 | 15.0 | 10.0 | 0.85 |
| 85 | 19.12 | 35.0 | 11.25 | 10.0 | 0.85 |
| 108 | 18.84 | 35.0 | 11.25 | 9.97 | 0.85 |
| 81 | 17.88 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.37 | 35.0 | 11.25 | 9.85 | 0.85 |
| 51 | 15.25 | 35.0 | 11.25 | 9.21 | 0.85 |
| 60 | 24.31 | 21.0 | 15.0 | 10.0 | 0.85 |
| 53 | 14.02 | 35.0 | 11.25 | 10.0 | 0.85 |
| 61 | 11.07 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 10.95 | 21.0 | 15.0 | 9.51 | 1.0 |
| 68 | 35.76 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.97 | 35.0 | 11.25 | 9.99 | 0.6 |
