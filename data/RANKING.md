# RANKING - generated 2026-08-20T00:01:52Z, block 8882279

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
| 1 | 76 | Phylax | 76.7 | 1.0 | 68.30 | 121 | cpu-small | 0.000 | 13 | 20% | SCORING_COMMIT 0.6d ago |
| 2 | 121 | sundae_bar | 74.6 | 0.85 | 1,116 | 1,116 | cpu-small | 0.601 | 2 | 60% | README_TASK_DIFF 5.2d ago |
| 3 | 67 | Harnyx | 72.4 | 1.0 | 22.96 | 307 | cpu-small | 0.009 | 147 | 9% | SCORING_COMMIT 1.5d ago |
| 4 | 23 | Trishool | 72.0 | 0.85 | 522 | 522 | cpu-small | 0.800 | 2 | 80% | SCORING_COMMIT 1.4d ago |
| 5 | 26 | Perturb | 71.0 | 1.0 | 42.35 | 77.63 | rtx3060 | 0.000 | 10 | 70% | SCORING_COMMIT 6.4d ago |
| 6 | 15 | ORO | 70.0 | 1.0 | 16.97 | 16,256 | cpu-small | 0.000 | 84 | 92% | SCORING_COMMIT 1.2d ago |
| 7 | 56 | Gradients | 69.6 | 0.85 | 656 | 994 | rtx4090 | 0.721 | 5 | 72% | SCORING_COMMIT 2.0d ago |
| 8 | 91 | cascade | 69.2 | 0.85 | 578 | 2,338 | rtx4090 | 0.000 | 5 | 52% | README_TASK_DIFF 1.8d ago |
| 9 | 38 | ChronoLLM | 67.6 | 0.85 | 150 | 3,183 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.1d ago |
| 10 | 96 | Verathos | 66.6 | 1.0 | 14.34 | 317 | rtx4090 | 0.409 | 90 | 41% | RELEASE 1.3d ago |
| 11 | 107 | Minos | 64.3 | 1.0 | 120 | 36,253 | cpu-small | 0.000 | 20 | 90% | README_TASK_DIFF 9d ago |
| 12 | 85 | Vidaio | 64.1 | 0.85 | 127 | 193 | rtx4090 | 0.000 | 13 | 42% | SCORING_COMMIT 1.7d ago |
| 13 | 81 | Reliquary | 61.8 | 0.85 | 63.40 | 205 | rtx4090 | 0.003 | 52 | 5% | SCORING_COMMIT 0.1d ago |
| 14 | 55 | NIOME | 61.6 | 0.85 | 59.29 | 495 | rtx4090 | 0.020 | 11 | 29% | SCORING_COMMIT 5.2d ago |
| 15 | 51 | lium.io | 61.3 | 0.85 | 62.13 | 1,058 | rtx4090 | 0.000 | 51 | 81% | RELEASE 0.2d ago |
| 16 | 28 | gm | 60.0 | 0.85 | 37.92 | 997 | rtx4090 | 0.227 | 49 | 23% | RELEASE 0.4d ago |
| 17 | 53 | engy | 59.9 | 0.85 | 35.19 | 12,214 | rtx4090 | 0.000 | 144 | 63% | SCORING_COMMIT 1.3d ago |
| 18 | 21 | AdTAO | 58.5 | 1.0 | 1.40 | 382 | cpu-small | 0.301 | 16 | 37% | SCORING_COMMIT 1.3d ago |
| 19 | 102 | ConnitoAI | 57.4 | 0.85 | 598 | 1,742 | rtx4090 | 0.250 | 7 | 29% | RELEASE 19d ago |
| 20 | 68 | NOVA | 55.0 | 0.6 | 7,983 | 7,983 | rtx4090 | 0.000 | 1 | 100% | SCORING_COMMIT 3.4d ago |
| 21 | 120 | Affine | 54.6 | 0.6 | 6,768 | 6,768 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 1.1d ago |
| 22 | 124 | Swarm | 54.3 | 0.85 | 247 | 721 | rtx4090 | 0.000 | 25 | 10% | SCORING_COMMIT 8d ago |
| 23 | 93 | Bitcast | 53.4 | 0.85 | 184 | 299 | rtx4090 | 0.000 | 4 | 90% | SCORING_COMMIT 21d ago |
| 24 | 80 | OpenRoboto | 53.3 | 0.85 | 174 | 629 | rtx4090 | 0.910 | 4 | 91% | SCORING_COMMIT 12d ago |
| 25 | 33 | ReadyAI | 53.0 | 0.85 | 5.36 | 10.56 | rtx4090 | 0.000 | 244 | 1% | SCORING_COMMIT 1.4d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 6 | Numinous | -0.93 | cpu-small | 396.212476054703 |
| 54 | Yanez | -3.17 | a4000 | 1072.585166344474 |
| 123 | MANTIS | -5.89 | rtx4090 | 88.34694611726324 |
| 75 | Hippius | -6.09 | rtx4090 | 11978.343642108835 |
| 114 | SOMA | -8.12 | rtx4090 | 634.2918264727392 |
| 89 | InfiniteQuant | -8.15 | rtx4090 | 168.98781104248263 |
| 104 | Masx.ai | -1.53 | rtx4090 | 7.660214390335502 |
| 13 | Data Universe | -3.70 | rtx4090 | 5.0384535889584745 |
| 88 | Investing | -4.18 | rtx4090 | 863.9978894818929 |
| 8 | Vanta | -7.96 | rtx4090 | 2873.2279432444075 |
| 43 | Graphite | -0.84 | cpu-small | 23.821835334603595 |
| 22 | Desearch | -0.59 | rtx4090 | 62.50890382950283 |
| 18 | Zeus | -4.06 | rtx4090 | 1492.5509390661182 |
| 45 | AlphaRidge.ai | -4.56 | rtx4090 | 10.688633007460913 |
| 19 | blockmachine | -7.89 | rtx4090 | 68.37059187360144 |
| 63 | Enigma | -8.14 | rtx4090 | 0.07622544756284114 |
| 105 | Beam | -2.58 | rtx4090 | 76.08880455691727 |
| 84 | ansuz | -8.16 | rtx4090 | 453.79890783178996 |
| 34 | BitMind | -20.10 | a100-80 | 24.027025859825997 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 39 subnets: sn7, sn10, sn12, sn14, sn20, sn24, sn25, sn27, sn30, sn31, sn37, sn39, sn42, sn46, sn47, sn52, sn57, sn59, sn65, sn69, sn70, sn71, sn72, sn73, sn78, sn87, sn92, sn94, sn95, sn103, sn109, sn111, sn113, sn115, sn116, sn119, sn122, sn125, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 76 | 16.74 | 35.0 | 15.0 | 10.0 | 1.0 |
| 121 | 27.72 | 35.0 | 15.0 | 10.0 | 0.85 |
| 67 | 12.55 | 35.0 | 15.0 | 9.86 | 1.0 |
| 23 | 24.73 | 35.0 | 15.0 | 9.99 | 0.85 |
| 26 | 14.89 | 35.0 | 11.25 | 9.84 | 1.0 |
| 15 | 11.41 | 35.0 | 15.0 | 8.6 | 1.0 |
| 56 | 25.63 | 35.0 | 11.25 | 10.0 | 0.85 |
| 91 | 25.13 | 35.0 | 11.25 | 9.98 | 0.85 |
| 38 | 19.82 | 35.0 | 15.0 | 9.66 | 0.85 |
| 96 | 10.79 | 35.0 | 11.25 | 9.52 | 1.0 |
| 107 | 18.95 | 21.0 | 15.0 | 9.32 | 1.0 |
| 85 | 19.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 81 | 16.45 | 35.0 | 11.25 | 10.0 | 0.85 |
| 55 | 16.19 | 35.0 | 11.25 | 10.0 | 0.85 |
| 51 | 16.37 | 35.0 | 11.25 | 9.45 | 0.85 |
| 28 | 14.46 | 35.0 | 11.25 | 9.82 | 0.85 |
| 53 | 14.18 | 35.0 | 11.25 | 10.0 | 0.85 |
| 21 | 3.45 | 35.0 | 15.0 | 5.09 | 1.0 |
| 102 | 25.26 | 21.0 | 11.25 | 9.99 | 0.85 |
| 68 | 35.49 | 35.0 | 11.25 | 10.0 | 0.6 |
| 120 | 34.84 | 35.0 | 11.25 | 9.98 | 0.6 |
| 124 | 21.78 | 21.0 | 11.25 | 9.86 | 0.85 |
| 93 | 20.62 | 21.0 | 11.25 | 10.0 | 0.85 |
| 80 | 20.4 | 21.0 | 11.25 | 10.0 | 0.85 |
| 33 | 7.31 | 35.0 | 11.25 | 8.84 | 0.85 |
