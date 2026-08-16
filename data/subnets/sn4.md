# sn4 - Targon (δ)

snapshot_utc: 2026-08-16T16:38:05Z  |  block: 8858460  |  row_status: ok

## Chain row

- miner_burn: **0.0697345589287579**
- registration cost: 0.0005 TAO (0.09875 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 14  |  free: 0
- subnet age: 1034.3 days  |  registered at block 1411451
- weights_version: 70001  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 15068.035930459682** (uid 156) <- the only figure quotable as achievable
- median_miner_usd_day: 2288.42259154567
- top_miner_usd_day: 15068.035930459682 (uid 156, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 7  |  gini: 0.5257795111146961  |  top1_share: 0.4591872548870001  |  top10_share: 1.0
- owner_incentive_share: 0.069737986601761 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/manifold-inc/targon`
- resolved URL: `https://github.com/manifold-inc/targon`
- status: **ok** 
- README: 3254 bytes, sha 3d27a420f8f1eb8b
- latest release: v2.0.0 2026-07-10T02:44:52Z
- last commit: 2026-07-16T22:28:35Z
- scoring-related commit: update miner doc 2026-07-10T02:38:17Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 2019.3132 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 43.6 (rank 35), confidence 0.85 - hardware requirement unknown
- components: income 30.06 / freshness 0.0 / resource 11.25 / registration 10.0
- freshness basis: no challenge change on record

## On-chain description

> Incentivized Compute Marketplace powered by the Targon Virtual Machine (TVM).

## README excerpt (evidence for the brief)

```markdown
# Targon: The Confidential Decentralized AI Cloud

Targon is a next-generation AI infrastructure platform that leverages
Trusted Execution Environment and Confidential Compute to secure the
entire stack. By providing a secure execution environment from hardware to
application layers, Targon enables verifiable and trustworthy operations across
the entire infrastructure in a decentralized fashion.

NOTICE: Using this software, you must agree to the Terms and Agreements provided
in the terms and conditions document. By downloading and running this software,
you implicitly agree to these terms and conditions.

## Docs

For validators, see [validator docs](/docs/validator/validator.md)

For miners, see [miner docs](/docs/miner/miner.md)

For the sn4 CLI, see [cli docs](/docs/sn4/sn4.md)

For mongo-wrapper service, see [mongo-wrapper docs](/docs/mongo-wrapper.md)

---

### Core Security Features

- Hardware-enforced memory encryption and protection
- Secure boot with hardware root of trust
- GPU TEE (Trusted Execution Environment) for isolated execution
- Remote attestation for verifiable computation
- Secure key management and cryptographic operations
- Protected execution environment with memory isolation

### AI Infrastructure Capabilities

- End-to-end secure model inference pipeline
- Hardware-level attestation and verification
- Protected model execution with CC or PPCIE isolation
- Verifiable computation through remote attestation
- Secure memory management for AI workloads
- Isolated execution environment for sensitive operations

### Current Implementation

- NVIDIA Confidential Compute integration OR
- NVIDIA PPCIE
- Hardware-level security guarantees
- Protected inference execution
- Remote attestation capabilities
- Secure memory encryption
- Isolated compute resources

### Future Roadmap

- Secure model training with Confidential Compute or PPCIE
- Protected data processing and storage
- Bare metal access for secure AI workloads
- Comprehensive AI development platform
- Developer-friendly tools and interfaces
- Multi-vendor Confidential Compute / PPCIE support:
  - AMD SEV-SNP integration
  - Additional hardware security technologies

## Contribution Guidelines

1. **Proposal Requirements**
  - Must be discussed on Discord and other community channels
  - Must demonstrate clear technical consensus
  - Must be approved by project maintainers
2. **Implementation Process**
  - Changes must be thoroughly tested
  - Must include migration plans if needed
  - Must consider backward compatibility
  - Must document security implications
3. **Making Changes**
  - Follow the existing code style
  - Write clear commit messages
  - Include tests for new features
  - Update documentation as needed

### Community Guidelines

1. **Communication**
  - Be respectful and professional
  - Provide constructive feedback
  - Help others when possible
  - Follow the project's code of conduct
2. **Collaboration**
  - Respond to review comments promptly
  - Be open to feedback and suggestions
  - Help maintain project quality
  - Share knowledge with the community

Remember: The goal is to improve Targon and Bittensor as a whole. We welcome all
contributions that align with this mission and follow our guidelines.
```
