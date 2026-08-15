# RANKING - generated 2026-08-15T12:56:02Z, block 8850150

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
| 1 | 107 | Minos | 77.7 | 1.0 | 103 | 31,770 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 4.9d ago |
| 2 | 76 | Phylax | 74.7 | 1.0 | 40.29 | 193 | cpu-small | 0.000 | 10 | 35% | SCORING_COMMIT 6.6d ago |
| 3 | 67 | Harnyx | 72.5 | 1.0 | 23.20 | 374 | cpu-small | 0.007 | 123 | 10% | SCORING_COMMIT 0.2d ago |
| 4 | 26 | Perturb | 70.9 | 1.0 | 41.10 | 75.36 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 1.9d ago |
| 5 | 1 | Apex | 70.6 | 0.85 | 873 | 1,140 | rtx4090 | 0.543 | 4 | 54% | RELEASE 1.9d ago |
| 6 | 6 | Numinous | 70.3 | 1.0 | 15.71 | 440 | cpu-small | 0.000 | 15 | 26% | WEIGHTS_VERSION_BUMP 1.8d ago |
| 7 | 41 | Almanac | 69.6 | 1.0 | 12.06 | 53.45 | cpu-small | 0.661 | 72 | 66% | SCORING_COMMIT 2.6d ago |
| 8 | 56 | Gradients | 68.7 | 0.85 | 510 | 960 | rtx4090 | 0.668 | 7 | 67% | SCORING_COMMIT 2.9d ago |
| 9 | 62 | Ridges | 68.6 | 0.85 | 484 | 2,239 | rtx4090 | 0.000 | 6 | 40% | RELEASE 0.6d ago |
| 10 | 91 | cascade | 68.5 | 0.85 | 479 | 1,112 | rtx4090 | 0.000 | 5 | 50% | SCORING_COMMIT 1.6d ago |
| 11 | 96 | Verathos | 68.4 | 1.0 | 22.59 | 166 | rtx4090 | 0.409 | 67 | 41% | RELEASE 0.7d ago |
| 12 | 15 | ORO | 68.1 | 1.0 | 11.31 | 20.23 | cpu-small | 0.000 | 84 | 93% | SCORING_COMMIT 1.6d ago |
| 13 | 21 | AdTAO | 67.6 | 1.0 | 7.55 | 33.87 | cpu-small | 0.451 | 88 | 45% | SCORING_COMMIT 4.0d ago |
| 14 | 85 | Vidaio | 66.4 | 0.85 | 249 | 540 | rtx4090 | 0.000 | 10 | 18% | SCORING_COMMIT 3.1d ago |
| 15 | 38 | ChronoLLM | 66.0 | 0.85 | 97.59 | 1,334 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 1.8d ago |
| 16 | 124 | Swarm | 65.8 | 0.85 | 221 | 715 | rtx4090 | 0.000 | 24 | 11% | SCORING_COMMIT 3.9d ago |
| 17 | 55 | NIOME | 61.3 | 0.85 | 55.16 | 469 | rtx4090 | 0.021 | 11 | 29% | SCORING_COMMIT 0.7d ago |
| 18 | 28 | gm | 60.4 | 0.85 | 43.25 | 1,953 | rtx4090 | 0.269 | 34 | 27% | RELEASE 2.9d ago |
| 19 | 60 | Bitsec.ai | 59.5 | 0.85 | 429 | 429 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 51 | lium.io | 59.3 | 0.85 | 36.93 | 1,814 | rtx4090 | 0.000 | 47 | 78% | SCORING_COMMIT 1.2d ago |
| 21 | 61 | RedTeam | 57.7 | 0.85 | 18.09 | 752 | rtx4090 | 0.000 | 70 | 18% | RELEASE 4.2d ago |
| 22 | 74 | Gittensor | 57.6 | 0.85 | 19.76 | 212 | rtx4090 | 0.640 | 15 | 64% | RELEASE 3.8d ago |
| 23 | 120 | Affine | 54.6 | 0.6 | 6,603 | 6,603 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 2.9d ago |
| 24 | 80 | OpenRoboto | 53.2 | 0.85 | 169 | 613 | rtx4090 | 0.906 | 4 | 91% | SCORING_COMMIT 7d ago |
| 25 | 97 | Albedo | 52.5 | 0.6 | 2,727 | 2,727 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.1d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez | -4.23 | a4000 | 947.8479264840053 |
| 104 | Masx.ai | -0.08 | rtx4090 | 8.523616237251595 |
| 75 | Hippius | -7.21 | rtx4090 | 10872.614834319285 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 227.69533276775473 |
| 101 | Tag101 | -0.06 | cpu-small | 2.1012607113011943 |
| 13 | Data Universe | -3.49 | rtx4090 | 6.161857983070838 |
| 88 | Investing | -5.60 | rtx4090 | 876.5645614438832 |
| 8 | Vanta | -7.96 | rtx4090 | 2895.3151398705745 |
| 114 | SOMA | -8.12 | rtx4090 | 1561.8778302518795 |
| 43 | Graphite | -0.52 | cpu-small | 11.132499494898036 |
| 22 | Desearch | -3.78 | rtx4090 | 51.71134142605818 |
| 18 | Zeus | -3.83 | rtx4090 | 1541.9787066076906 |
| 45 | AlphaRidge.ai | -4.78 | rtx4090 | 13.568763998621595 |
| 123 | MANTIS | -6.08 | rtx4090 | 78.80578649303791 |
| 63 | Enigma | -8.14 | rtx4090 | 4924.153776046556 |
| 105 | Beam | -2.71 | rtx4090 | 85.56883684193099 |
| 34 | BitMind | -19.76 | a100-80 | 23.107122593983767 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn2, sn10, sn12, sn14, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn87, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn115, sn116, sn119, sn121, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.36 | 35.0 | 15.0 | 9.37 | 1.0 |
| 76 | 14.7 | 35.0 | 15.0 | 10.0 | 1.0 |
| 67 | 12.59 | 35.0 | 15.0 | 9.88 | 1.0 |
| 26 | 14.77 | 35.0 | 11.25 | 9.84 | 1.0 |
| 1 | 26.75 | 35.0 | 11.25 | 10.0 | 0.85 |
| 6 | 11.12 | 35.0 | 15.0 | 9.17 | 1.0 |
| 41 | 10.15 | 35.0 | 15.0 | 9.46 | 1.0 |
| 56 | 24.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 24.42 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 24.39 | 35.0 | 11.25 | 9.98 | 0.85 |
| 96 | 12.48 | 35.0 | 11.25 | 9.71 | 1.0 |
| 15 | 9.91 | 35.0 | 15.0 | 8.14 | 1.0 |
| 21 | 8.47 | 35.0 | 15.0 | 9.13 | 1.0 |
| 85 | 21.82 | 35.0 | 11.25 | 10.0 | 0.85 |
| 38 | 18.13 | 35.0 | 15.0 | 9.5 | 0.85 |
| 124 | 21.35 | 35.0 | 11.25 | 9.85 | 0.85 |
| 55 | 15.91 | 35.0 | 11.25 | 10.0 | 0.85 |
| 28 | 14.97 | 35.0 | 11.25 | 9.85 | 0.85 |
| 60 | 23.95 | 21.0 | 15.0 | 10.0 | 0.85 |
| 51 | 14.36 | 35.0 | 11.25 | 9.11 | 0.85 |
| 61 | 11.65 | 35.0 | 11.25 | 10.0 | 0.85 |
| 74 | 11.98 | 35.0 | 11.25 | 9.5 | 0.85 |
| 120 | 34.74 | 35.0 | 11.25 | 9.99 | 0.6 |
| 80 | 20.29 | 21.0 | 11.25 | 10.0 | 0.85 |
| 97 | 31.25 | 35.0 | 11.25 | 9.98 | 0.6 |
