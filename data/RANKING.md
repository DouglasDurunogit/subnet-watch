# RANKING - generated 2026-11-03T17:16:32Z, block 9426877

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
| 1 | 120 | Affine | 74.3 | 0.85 | 2,661 | 5,329 | rtx4090 | 0.000 | 10 | 19% | SCORING_COMMIT 0.6d ago |
| 2 | 97 | Ingot | 72.6 | 0.85 | 1,588 | 1,588 | rtx4090 | 0.000 | 5 | 20% | SCORING_COMMIT 4.0d ago |
| 3 | 34 | Yugos | 70.2 | 0.85 | 804 | 6,895 | rtx4090 | 0.000 | 3 | 85% | SCORING_COMMIT 0.6d ago |
| 4 | 103 | Terza Inference | 69.6 | 0.85 | 653 | 1,449 | rtx4090 | 0.000 | 5 | 38% | subnet is 15 days old |
| 5 | 14 | Cacheon | 69.5 | 0.85 | 632 | 5,149 | rtx4090 | 0.000 | 3 | 80% | SCORING_COMMIT 3.2d ago |
| 6 | 53 | engy | 67.7 | 0.85 | 370 | 2,011 | rtx4090 | 0.000 | 29 | 26% | SCORING_COMMIT 4.0d ago |
| 7 | 67 | Harnyx | 67.3 | 1.0 | 6.31 | 80.43 | cpu-small | 0.079 | 139 | 8% | SCORING_COMMIT 0.0d ago |
| 8 | 1 | Apex | 67.2 | 0.85 | 326 | 803 | rtx4090 | 0.680 | 4 | 68% | RELEASE 0.0d ago |
| 9 | 56 | Gradients | 66.8 | 0.85 | 283 | 4,985 | rtx4090 | 0.000 | 7 | 51% | SCORING_COMMIT 0.9d ago |
| 10 | 107 | Minos | 66.0 | 1.0 | 177 | 15,062 | cpu-small | 0.000 | 20 | 80% | SCORING_COMMIT 25d ago |
| 11 | 102 | ConnitoAI | 65.6 | 0.85 | 202 | 1,884 | rtx4090 | 0.294 | 5 | 53% | RELEASE 4.0d ago |
| 12 | 15 | ORO | 65.6 | 1.0 | 6.54 | 13.33 | cpu-small | 0.000 | 76 | 95% | RELEASE 2.7d ago |
| 13 | 38 | ChronoLLM | 63.6 | 0.85 | 53.91 | 481 | cpu-small | 0.000 | 10 | 52% | SCORING_COMMIT 0.9d ago |
| 14 | 124 | Swarm | 62.1 | 0.85 | 80.41 | 1,828 | rtx4090 | 0.000 | 15 | 31% | SCORING_COMMIT 4.6d ago |
| 15 | 121 | sundae_bar | 62.0 | 0.85 | 911 | 911 | cpu-small | 0.600 | 2 | 60% | SCORING_COMMIT 18d ago |
| 16 | 62 | Ridges | 61.6 | 0.85 | 59.42 | 1,406 | rtx4090 | 0.000 | 36 | 25% | RELEASE 3.4d ago |
| 17 | 117 | everyframe.studio | 61.4 | 0.85 | 57.51 | 102 | rtx4090 | 0.803 | 13 | 80% | RELEASE 0.0d ago |
| 18 | 3 | Teutonic | 61.2 | 0.85 | 1,859 | 3,727 | rtx4090 | 0.000 | 7 | 25% | SCORING_COMMIT 7d ago |
| 19 | 60 | Bitsec.ai | 60.0 | 0.85 | 499 | 769 | cpu-small | 0.500 | 3 | 50% | SCORING_COMMIT 8d ago |
| 20 | 80 | OpenRoboto | 58.7 | 0.85 | 893 | 1,277 | rtx4090 | 0.000 | 12 | 15% | README_TASK_DIFF 29d ago |
| 21 | 111 | Claims | 58.6 | 0.85 | 24.91 | 2,476 | rtx4090 | 0.000 | 6 | 90% | SCORING_COMMIT 0.0d ago |
| 22 | 58 | Attune | 56.3 | 0.85 | 434 | 711 | rtx4090 | 0.711 | 5 | 71% | SCORING_COMMIT 22d ago |
| 23 | 9 | iota | 56.1 | 0.6 | 12,295 | 12,295 | rtx4090 | 0.000 | 2 | 80% | RELEASE 2.1d ago |
| 24 | 46 | Instant | 55.5 | 0.85 | 133 | 160 | cpu-small | 0.473 | 10 | 47% | RELEASE 11d ago |
| 25 | 81 | Reliquary | 55.5 | 0.85 | 8.87 | 51.43 | rtx4090 | 0.840 | 24 | 84% | SCORING_COMMIT 0.0d ago |

## BELOW COST (ranked, but the cheapest satisfying machine costs more than the
competitive miner earns - listed so the information is not destroyed)

| netuid | name | net $/day | machine | competitive $/day |
|---|---|---|---|---|
| 114 | SOMA | -0.80 | cpu-small | 7732.543281448472 |
| 32 | ItsAI | -1.09 | rtx4090 | 7.786520511158457 |
| 33 | ReadyAI | -1.86 | rtx4090 | 8.968651275545659 |
| 50 | Synth | -2.24 | rtx4090 | 32.422157821880226 |
| 89 | InfiniteQuant | -6.56 | rtx4090 | 40.91083663162408 |
| 8 | Vanta | -7.42 | rtx4090 | 1.2055661511374547 |
| 96 | Verathos | -2.77 | rtx4090 | 83.69026439854802 |
| 54 | Yanez | -4.10 | a4000 | 1642.2208921352171 |
| 51 | lium.io | -45.70 | h200-141 | 2616.368293572397 |
| 91 | cascade | -421.22 | 8xh100 | 71.71545886953024 |
| 22 | Desearch | -2.17 | rtx4090 | 7.839009649294277 |
| 18 | Zeus | -3.03 | rtx4090 | 1045.4865166053698 |
| 13 | Data Universe | -4.47 | rtx4090 | 3.8268318431857575 |
| 45 | AlphaRidge.ai | -4.96 | rtx4090 | 5.937591293632617 |
| 123 | MANTIS | -6.00 | rtx4090 | 59.685260416327424 |
| 30 | Endure Network | -7.15 | rtx4090 | 1.245537313497694 |
| 75 | Hippius | -8.03 | rtx4090 | 12183.209252685816 |
| 6 | Numinous | -8.07 | rtx4090 | 167.1676424111148 |
| 63 | Enigma | -8.17 | rtx4090 | 0.04591038229022877 |
| 88 | Investing | -7.76 | rtx4090 | 58.90643537796278 |

## GATED (excluded from the ranking)

- **BLOCKED:burn** - 29 subnets: sn2, sn7, sn10, sn12, sn26, sn27, sn39, sn40, sn42, sn52, sn57, sn69, sn70, sn72, sn74, sn76, sn84, sn87, sn94, sn95, sn100, sn108, sn109, sn113, sn115, sn116, sn119, sn126, sn127

## COMPONENT POINTS (for re-weighting without re-deriving)

| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |
|---|---|---|---|---|---|
| 120 | 31.15 | 35.0 | 11.25 | 9.96 | 0.85 |
| 97 | 29.11 | 35.0 | 11.25 | 10.0 | 0.85 |
| 34 | 26.43 | 35.0 | 11.25 | 9.95 | 0.85 |
| 103 | 25.61 | 35.0 | 11.25 | 10.0 | 0.85 |
| 14 | 25.48 | 35.0 | 11.25 | 10.0 | 0.85 |
| 53 | 23.37 | 35.0 | 11.25 | 10.0 | 0.85 |
| 67 | 7.86 | 35.0 | 15.0 | 9.44 | 1.0 |
| 1 | 22.86 | 35.0 | 11.25 | 10.0 | 0.85 |
| 56 | 22.31 | 35.0 | 11.25 | 10.0 | 0.85 |
| 107 | 20.47 | 21.0 | 15.0 | 9.58 | 1.0 |
| 102 | 21.0 | 35.0 | 11.25 | 9.98 | 0.85 |
| 15 | 7.98 | 35.0 | 15.0 | 7.57 | 1.0 |
| 38 | 15.82 | 35.0 | 15.0 | 8.96 | 0.85 |
| 124 | 17.38 | 35.0 | 11.25 | 9.46 | 0.85 |
| 121 | 26.92 | 21.0 | 15.0 | 10.0 | 0.85 |
| 62 | 16.2 | 35.0 | 11.25 | 10.0 | 0.85 |
| 117 | 16.07 | 35.0 | 11.25 | 9.93 | 0.85 |
| 3 | 29.74 | 21.0 | 11.25 | 9.96 | 0.85 |
| 60 | 24.55 | 21.0 | 15.0 | 10.0 | 0.85 |
| 80 | 26.84 | 21.0 | 11.25 | 10.0 | 0.85 |
| 111 | 12.86 | 35.0 | 11.25 | 9.85 | 0.85 |
| 58 | 24.0 | 21.0 | 11.25 | 9.95 | 0.85 |
| 9 | 37.2 | 35.0 | 11.25 | 10.0 | 0.6 |
| 46 | 19.36 | 21.0 | 15.0 | 9.94 | 0.85 |
| 81 | 9.05 | 35.0 | 11.25 | 10.0 | 0.85 |
