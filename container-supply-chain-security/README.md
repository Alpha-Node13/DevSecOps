**Container Supply Chain Security:**

Focuses on securing container images throughout their lifecycle by ensuring they come from trusted sources, contain no known vulnerabilities, and remain 
unchanged before reaching production.

----------------------------------------------------------------------------------------------------------------------------------------------
**Pin Image Digests**

Pinning an image digest means deploying a container image using its exact, immutable version, rather than a moving tag like latest.

**Example:**

<img width="168" height="44" alt="image" src="https://github.com/user-attachments/assets/5a882c96-2803-4450-afe0-79c9af3aa877" />

This tag can change over time and may point to different image versions.

<img width="199" height="40" alt="image" src="https://github.com/user-attachments/assets/00c104e0-a4ba-4887-9b8a-30c03df9e68a" />

This digest is immutable and always refers to the same image.

**Why pin image digests?**

• Prevents unexpected image updates

• Blocks malicious image replacement

• Makes builds reproducible

• Improves security and stability

----------------------------------------------------------------------------------------------------------------------------------------------

**SBOM Generation**

- SBOM (Software Bill of Materials) is a complete list of everything inside an application or container, including libraries, packages, and their versions.

- It provides visibility into what software components an application is made of.

- The generation process creates a detailed list of all packages, libraries, and dependencies in a container image, helping teams track and manage security and compliance risks.

- This inventory is typically generated automatically using specialized tools.

**Common tools that generate SBOM:**

• Syft – SBOM generation

• Trivy – Vulnerability scan + SBOM

**SBOM Formats:**

- CycloneDX
- SPDX (Software Package Data Exchange)

----------------------------------------------------------------------------------------------------------------------------------------------

**Vulnerability Scanning**

We use Trivy for vulnerability scanning to analyze container images against known vulnerability databases and identify outdated, insecure, or vulnerable components before deployment.

**What it checks:**

- Operating system packages (Ubuntu, Alpine)
- Application dependencies (Python, Node.js)
- Known CVEs (Common Vulnerabilities and Exposures)

----------------------------------------------------------------------------------------------------------------------------------------------

**Verify Image Signatures:**

Image signature verification confirms that a container image was created by a trusted publisher and has not been altered or tampered with during storage or 
transfer.

**Tools commonly used:**

- Cosign (modern, recommended)
- Docker Content Trust (DCT)
- Notary

**How it works:**

- Publisher signs image with private key
- You verify with public key
- Like a digital seal on a package
---------------------------------------------------------------------------------------------------------------------

**Workflow**

1. Pin digests (SHA256)            ← Build with known base
2. Build image                     ← Create the container
3. Generate SBOM (Trivy)           ← Document what's inside
4. Scan vulnerabilities (Trivy)    ← Find security issues
5. Push image to registry          ← Make it available to sign
6. Sign image (Cosign)             ← Certify it's safe
7. Verify signature before deploy  ← Final check
8. Deploy                          ← Go to production
---------------------------------------------------------------------------------------------------------------------

**Step 1: Pin Image Digests**

<img width="671" height="606" alt="image" src="https://github.com/user-attachments/assets/552abd3c-f4bb-4bae-9b8d-80cdf4b28ae6" />

We just need to add digest pinning to this existing secure Dockerfile!

**Commands:**
- docker pull python:3.11-slim
- docker inspect python:3.11-slim --format="{{index .RepoDigests 0}}"

<img width="1487" height="178" alt="image" src="https://github.com/user-attachments/assets/09a8d25d-23ee-4238-887f-9d32c2fa00ea" />

Dockerfile.secure with Digest Pinning 

<img width="680" height="602" alt="image" src="https://github.com/user-attachments/assets/688f6bb2-a1d3-4bf1-8b92-bbd3cfe11584" />

---------------------------------------------------------------------------------------------------------------------

**Step 2: Build Secure Image**

**Command:**
docker build -f Dockerfile.secure -t secure-app:v2 .

<img width="1903" height="483" alt="image" src="https://github.com/user-attachments/assets/f940890c-6e43-412e-9aec-7d817470f403" />

---------------------------------------------------------------------------------------------------------------------

**Step 3: Generate SBOM for Secure Image**

**Command:**
trivy image --format cyclonedx secure-app:v2 > sbom.json
 
<img width="1898" height="133" alt="image" src="https://github.com/user-attachments/assets/3d51cb37-ffca-45d9-8f8f-16d80d8c78fb" />
<img width="746" height="240" alt="image" src="https://github.com/user-attachments/assets/5e4fa007-cd2f-4d94-adac-623a690bab3e" />
<img width="1599" height="979" alt="image" src="https://github.com/user-attachments/assets/d48ab514-a0c0-4821-bed3-6747eaf1b42d" />

---------------------------------------------------------------------------------------------------------------------

**Step 4: Scan Secure Image**

**Command:**
trivy image secure-app:v2

<img width="1582" height="969" alt="image" src="https://github.com/user-attachments/assets/be22a01d-16c7-4252-a509-24d22420dd8f" />

---------------------------------------------------------------------------------------------------------------------

**Step 5: Generate a key pair**

• cosign.key → private key (keep this secret)

• cosign.pub → public key (safe to share)

Installation cosign:

https://github.com/sigstore/cosign/releases/tag/v3.0.4

**Command:**
cosign generate-key-pair

<img width="961" height="101" alt="image" src="https://github.com/user-attachments/assets/f32affa6-7965-477b-b39c-f29428a4a079" />
<img width="734" height="179" alt="image" src="https://github.com/user-attachments/assets/15377e4e-9551-4734-84cf-07a7ed282762" />

**Step 6: Push Image to Registry**

**Commands:**

docker login

docker tag secure-app:v2 muhammadsaud13/secure-app:v2

docker push muhammadsaud13/secure-app:v2

<img width="1320" height="664" alt="poc" src="https://github.com/user-attachments/assets/1f2d6bdb-ec69-44a6-9997-29c97adb42f9" />

**Step 7: Sign Your Image**

**Command:**
cosign sign --key cosign.key muhammadsaud13/secure-app:v2

<img width="1434" height="163" alt="image" src="https://github.com/user-attachments/assets/b48b087b-635a-4f3e-a709-f943ad843120" />


**Step 8: Verify your image**

**Command:**
cosign verify --key cosign.pub muhammadsaud13/secure-app:v2

<img width="1890" height="204" alt="image" src="https://github.com/user-attachments/assets/60edda14-ca84-44b2-83b3-95268fa390a2" />

Image Verified Successfully
