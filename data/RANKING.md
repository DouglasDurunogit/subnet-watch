# RANKING - generated 2026-08-07T23:44:46Z, block 8795803

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
| 1 | 107 | Minos | 78.3 | 1.0 | 118 | 33,281 | cpu-small | 0.000 | 20 | 90% | WEIGHTS_VERSION_BUMP 3.8d ago |
| 2 | 60 | Bitsec.ai | 74.9 | 0.85 | 1,226 | 1,226 | cpu-small | 0.505 | 2 | 50% | SCORING_COMMIT 0.2d ago |
| 3 | 114 | SOMA | 72.7 | 0.85 | 1,672 | 4,359 | rtx4090 | 0.000 | 3 | 65% | SCORING_COMMIT 0.6d ago |
| 4 | 67 | Harnyx | 72.1 | 1.0 | 21.01 | 761 | cpu-small | 0.012 | 135 | 20% | SCORING_COMMIT 0.8d ago |
| 5 | 91 | cascade | 69.9 | 0.85 | 711 | 2,870 | rtx4090 | 0.000 | 5 | 52% | RELEASE 2.8d ago |
| 6 | 1 | Apex | 69.8 | 0.85 | 696 | 1,599 | rtx4090 | 0.389 | 4 | 39% | RELEASE 0.1d ago |
| 7 | 62 | Ridges | 69.1 | 0.85 | 564 | 2,039 | rtx4090 | 0.133 | 7 | 35% | RELEASE 2.1d ago |
| 8 | 15 | ORO | 68.6 | 1.0 | 11.39 | 10,349 | cpu-small | 0.000 | 74 | 93% | RELEASE 1.6d ago |
| 9 | 26 | Perturb | 68.0 | 1.0 | 20.17 | 39.96 | rtx3060 | 0.501 | 11 | 50% | SCORING_COMMIT 1.4d ago |
| 10 | 100 | BASE | 67.9 | 0.85 | 401 | 1,627 | rtx4090 | 0.000 | 5 | 50% | RELEASE 0.4d ago |
| 11 | 41 | Almanac | 67.6 | 1.0 | 7.44 | 33.87 | cpu-small | 0.801 | 63 | 80% | SCORING_COMMIT 1.0d ago |
| 12 | 124 | Swarm | 65.6 | 0.85 | 207 | 595 | rtx4090 | 0.000 | 23 | 10% | SCORING_COMMIT 6.4d ago |
| 13 | 21 | AdTAO | 65.5 | 1.0 | 4.69 | 21.73 | cpu-small | 0.451 | 142 | 45% | SCORING_COMMIT 0.2d ago |
| 14 | 96 | Verathos | 65.0 | 1.0 | 9.83 | 175 | rtx4090 | 0.423 | 84 | 42% | RELEASE 1.0d ago |
| 15 | 28 | gm | 62.8 | 0.85 | 88.24 | 4,058 | rtx4090 | 0.253 | 18 | 46% | RELEASE 0.1d ago |
| 16 | 61 | RedTeam | 62.1 | 0.85 | 69.39 | 181 | rtx4090 | 0.000 | 36 | 6% | RELEASE 0.0d ago |
| 17 | 51 | lium.io | 57.0 | 0.85 | 21.63 | 2,921 | rtx4090 | 0.000 | 44 | 71% | SCORING_COMMIT 0.1d ago |
| 18 | 56 | Gradients | 56.4 | 0.85 | 450 | 949 | rtx4090 | 0.701 | 7 | 70% | SCORING_COMMIT 10d ago |
| 19 | 74 | Gittensor | 55.9 | 0.85 | 14.29 | 212 | rtx4090 | 0.636 | 15 | 64% | RELEASE 0.3d ago |
| 20 | 2 | DSperse | 54.8 | 0.85 | 6.93 | 145 | rtx4090 | 0.826 | 10 | 83% | RELEASE 1.8d ago |
| 21 | 120 | Affine | 54.6 | 0.6 | 6,613 | 6,613 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.5d ago |
| 22 | 38 | ChronoLLM | 53.7 | 0.85 | 213 | 3,571 | rtx4090 | 0.000 | 10 | 52% | SCORING_COMMIT 9d ago |
| 23 | 97 | Albedo | 52.7 | 0.6 | 2,924 | 2,924 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 5.9d ago |
| 24 | 85 | Vidaio | 52.1 | 0.85 | 125 | 608 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 11d ago |
| 25 | 126 | Poker44 | 51.7 | 0.6 | 1,908 | 1,908 | rtx4090 | 0.300 | 3 | 65% | SCORING_COMMIT 0.4d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 54 | Yanez MIID | -4.02 | a4000 | 1056.261018941458 |
| 104 | Masx.ai | -1.63 | rtx4090 | 7.435876632322748 |
| 13 | Data Universe | -3.14 | rtx4090 | 6.5716499105518285 |
| 88 | Investing | -6.84 | rtx4090 | 625.611714732621 |
| 89 | InfiniteQuant | -8.19 | rtx4090 | 133.37116905993358 |
| 8 | Vanta | -7.44 | rtx4090 | 3169.196350821721 |
| 32 | ItsAI | -0.12 | rtx4090 | 9.687074969700971 |
| 19 | blockmachine | -1.90 | rtx4090 | 337.2712775411865 |
| 22 | Desearch | -3.01 | rtx4090 | 114.09296106264443 |
| 18 | Zeus | -3.39 | rtx4090 | 1706.1430608275143 |
| 45 | AlphaRidge.ai | -4.43 | rtx4090 | 13.458968883871929 |
| 75 | Hippius | -4.69 | rtx4090 | 5.254417858427779 |
| 123 | MANTIS | -6.31 | rtx4090 | 78.59131158152998 |
| 63 | Enigma | -8.15 | rtx4090 | 0.07345089305461519 |
| 84 | ansuz | -8.15 | rtx4090 | 479.6929192274147 |
| 34 | BitMind | -18.37 | a100-80 | 281.4715955807341 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 36 subnets: sn6, sn10, sn12, sn14, sn20, sn23, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn58, sn59, sn65, sn69, sn71, sn72, sn73, sn87, sn92, sn94, sn95, sn103, sn108, sn109, sn111, sn113, sn122, sn125

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 107 | 18.89 | 35.0 | 15.0 | 9.46 | 1.0 |
| 60 | 28.09 | 35.0 | 15.0 | 10.0 | 0.85 |
| 114 | 29.32 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 12.21 | 35.0 | 15.0 | 9.94 | 1.0 |
| 91 | 25.95 | 35.0 | 11.25 | 9.99 | 0.85 |
| 1 | 25.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 62 | 25.03 | 35.0 | 11.25 | 10.0 | 0.85 |
| 15 | 9.94 | 35.0 | 15.0 | 8.63 | 1.0 |
| 26 | 12.06 | 35.0 | 11.25 | 9.68 | 1.0 |
| 100 | 23.68 | 35.0 | 11.25 | 10.0 | 0.85 |
| 41 | 8.43 | 35.0 | 15.0 | 9.13 | 1.0 |
| 124 | 21.08 | 35.0 | 11.25 | 9.84 | 0.85 |
| 21 | 6.87 | 35.0 | 15.0 | 8.63 | 1.0 |
| 96 | 9.41 | 35.0 | 11.25 | 9.34 | 1.0 |
| 28 | 17.74 | 35.0 | 11.25 | 9.93 | 0.85 |
| 61 | 16.8 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 12.32 | 35.0 | 11.25 | 8.51 | 0.85 |
| 56 | 24.14 | 21.0 | 11.25 | 10.0 | 0.85 |
| 74 | 10.77 | 35.0 | 11.25 | 8.69 | 0.85 |
| 2 | 8.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 120 | 34.75 | 35.0 | 11.25 | 9.99 | 0.6 |
| 38 | 21.19 | 21.0 | 11.25 | 9.78 | 0.85 |
| 97 | 31.52 | 35.0 | 11.25 | 9.99 | 0.6 |
| 85 | 19.09 | 21.0 | 11.25 | 10.0 | 0.85 |
| 126 | 29.84 | 35.0 | 11.25 | 9.99 | 0.6 |
