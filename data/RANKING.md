# RANKING - generated 2026-08-17T03:09:55Z, block 8861619

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
| 1 | 107 | Minos | 77.9 | 1.0 | 106 | 33,199 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 6.5d ago |
| 2 | 67 | Harnyx | 72.1 | 1.0 | 21.45 | 401 | cpu-small | 0.016 | 126 | 11% | SCORING_COMMIT 0.9d ago |
| 3 | 26 | Perturb | 70.8 | 1.0 | 40.68 | 74.62 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 3.5d ago |
| 4 | 1 | Apex | 70.6 | 0.85 | 890 | 998 | rtx4090 | 0.535 | 4 | 53% | RELEASE 3.5d ago |
| 5 | 76 | Phylax | 70.5 | 1.0 | 13.35 | 156 | cpu-small | 0.000 | 10 | 29% | SCORING_COMMIT 0.6d ago |
| 6 | 96 | Verathos | 70.0 | 1.0 | 33.40 | 373 | rtx4090 | 0.408 | 57 | 41% | RELEASE 2.3d ago |
| 7 | 91 | cascade | 69.1 | 0.85 | 570 | 2,307 | rtx4090 | 0.000 | 5 | 51% | SCORING_COMMIT 3.2d ago |
| 8 | 15 | ORO | 68.9 | 1.0 | 12.72 | 21.57 | cpu-small | 0.000 | 67 | 94% | SCORING_COMMIT 3.2d ago |
| 9 | 85 | Vidaio | 68.8 | 0.85 | 522 | 525 | rtx4090 | 0.000 | 10 | 17% | SCORING_COMMIT 0.4d ago |
| 10 | 56 | Gradients | 68.7 | 0.85 | 504 | 963 | rtx4090 | 0.681 | 7 | 68% | SCORING_COMMIT 4.5d ago |
| 11 | 41 | Almanac | 68.7 | 1.0 | 9.77 | 53.61 | cpu-small | 0.694 | 75 | 69% | SCORING_COMMIT 4.2d ago |
| 12 | 62 | Ridges | 68.5 | 0.85 | 472 | 2,187 | rtx4090 | 0.000 | 6 | 40% | RELEASE 2.2d ago |
| 13 | 21 | AdTAO | 67.7 | 1.0 | 7.67 | 34.38 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 5.6d ago |
| 14 | 38 | ChronoLLM | 66.1 | 0.85 | 101 | 1,379 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 3.4d ago |
| 15 | 124 | Swarm | 65.9 | 0.85 | 225 | 723 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 5.5d ago |
| 16 | 98 | NeverPlayAlone | 64.1 | 0.85 | 1,698 | 1,698 | cpu-small | 0.000 | 1 | 100% | SCORING_COMMIT 10d ago |
| 17 | 55 | NIOME | 61.4 | 0.85 | 56.24 | 487 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 2.3d ago |
| 18 | 28 | gm | 61.2 | 0.85 | 55.38 | 2,192 | rtx4090 | 0.123 | 43 | 24% | RELEASE 4.5d ago |
| 19 | 51 | lium.io | 59.3 | 0.85 | 36.84 | 2,577 | rtx4090 | 0.000 | 56 | 77% | SCORING_COMMIT 2.7d ago |
| 20 | 60 | Bitsec.ai | 59.1 | 0.85 | 384 | 384 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 9d ago |
| 21 | 74 | Gittensor | 58.2 | 0.85 | 23.65 | 212 | rtx4090 | 0.630 | 14 | 63% | RELEASE 5.4d ago |
| 22 | 61 | RedTeam | 57.0 | 0.85 | 14.47 | 404 | rtx4090 | 0.000 | 84 | 10% | RELEASE 5.8d ago |
| 23 | 68 | NOVA | 55.1 | 0.6 | 8,112 | 8,112 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 0.6d ago |
| 24 | 120 | Affine | 54.7 | 0.6 | 6,840 | 6,840 | rtx4090 | 0.207 | 5 | 21% | SCORING_COMMIT 4.5d ago |
| 25 | 93 | Bitcast | 54.7 | 0.85 | 269 | 491 | rtx4090 | 0.000 | 4 | 83% | SCORING_COMMIT 19d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 226.84315510201375 |
| 54 | Yanez | -4.43 | a4000 | 955.8282393662543 |
| 104 | Masx.ai | -0.04 | rtx4090 | 9.686240229131089 |
| 75 | Hippius | -7.38 | rtx4090 | 10907.225150780405 |
| 89 | InfiniteQuant | -8.18 | rtx4090 | 147.77995772814586 |
| 13 | Data Universe | -3.57 | rtx4090 | 6.03700223814719 |
| 88 | Investing | -5.21 | rtx4090 | 249.61724340557595 |
| 8 | Vanta | -7.96 | rtx4090 | 2858.9872590908703 |
| 114 | SOMA | -8.12 | rtx4090 | 636.8605093478923 |
| 43 | Graphite | -0.78 | cpu-small | 17.432473708897394 |
| 45 | AlphaRidge.ai | -3.72 | rtx4090 | 16.666804468944036 |
| 18 | Zeus | -5.28 | rtx4090 | 1177.8008476259226 |
| 22 | Desearch | -5.34 | rtx4090 | 54.568891096359195 |
| 123 | MANTIS | -6.16 | rtx4090 | 75.058817342709 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07684177774708684 |
| 105 | Beam | -2.95 | rtx4090 | 110.80263830670025 |
| 84 | ansuz | -8.16 | rtx4090 | 439.70845566870395 |
| 34 | BitMind | -19.83 | a100-80 | 22.61922514367583 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.48 | 35.0 | 15.0 | 9.39 | 1.0 |
| 67 | 12.29 | 35.0 | 15.0 | 9.85 | 1.0 |
| 26 | 14.73 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.83 | 35.0 | 11.25 | 10.0 | 0.85 |
| 76 | 10.52 | 35.0 | 15.0 | 10.0 | 1.0 |
| 96 | 13.98 | 35.0 | 11.25 | 9.8 | 1.0 |
| 91 | 25.08 | 35.0 | 11.25 | 9.99 | 0.85 |
| 15 | 10.34 | 35.0 | 15.0 | 8.54 | 1.0 |
| 85 | 24.72 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 24.59 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 9.39 | 35.0 | 15.0 | 9.33 | 1.0 |
| 62 | 24.33 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 8.53 | 35.0 | 15.0 | 9.14 | 1.0 |
| 38 | 18.26 | 35.0 | 15.0 | 9.52 | 0.85 |
| 124 | 21.42 | 35.0 | 11.25 | 9.85 | 0.85 |
| 98 | 29.38 | 21.0 | 15.0 | 10.0 | 0.85 |
| 55 | 15.99 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 15.93 | 35.0 | 11.25 | 9.88 | 0.85 |
| 51 | 14.35 | 35.0 | 11.25 | 9.11 | 0.85 |
| 60 | 23.52 | 21.0 | 15.0 | 10.0 | 0.85 |
| 74 | 12.66 | 35.0 | 11.25 | 9.58 | 0.85 |
| 61 | 10.82 | 35.0 | 11.25 | 10.0 | 0.85 |
| 68 | 35.55 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.88 | 35.0 | 11.25 | 9.99 | 0.6 |
| 93 | 22.12 | 21.0 | 11.25 | 10.0 | 0.85 |
