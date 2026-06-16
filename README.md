# DevSecOps

Hands-on walkthroughs covering practical container security from build to deployment. Each section is a standalone guide with commands, evidence, and best-practice rationale.

## Available now

### [Docker Hardening](./docker-hardening)
Build an intentionally insecure Docker image, scan it with **Trivy** to expose real vulnerabilities, then rebuild it with security best practices (non-root user, minimal base image, no hardcoded secrets, pinned dependencies) and watch the vulnerability count drop.

### [Container Supply Chain Security](./container-supply-chain-security)
Take a secure image further. Pin base images by digest, generate an **SBOM** with Trivy, push to a registry, sign with **Cosign**, and verify signatures before deployment — the full "trust but verify" supply-chain workflow.

### [Inventory Management](./inventory-management)
Upload your SBOM to **Dependency Track** for continuous component analysis — get a live inventory of every library you ship and an alert the day a new CVE lands in something you already deployed.

## Tools used

- **Docker** — container runtime
- **Trivy** — vulnerability scanner + SBOM generator
- **Cosign** — container image signing & verification
- **Dependency Track** — SBOM analysis & continuous monitoring
