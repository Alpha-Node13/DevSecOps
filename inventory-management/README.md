**Dependency Track**

It is an open-source Component Analysis Platform that:
- Manages software bill of materials (SBOMs)
- Continuously monitors for vulnerabilities
- Provides visibility into your software supply chain
- Alerts you when new vulnerabilities are discovered
- Generates compliance reports

A centralized inventory system for all your software components across all projects.

---------------------------------------------------------------------------------------------------------------------

**Step 1: Setup Dependency Track**

We'll use Docker to run Dependency Track

https://dependencytrack.org/

<img width="1200" height="232" alt="image" src="https://github.com/user-attachments/assets/ff5d2282-017b-45bf-b4bb-9ed6e7d39a02" />

**Command:**

- curl -LO https://dependencytrack.org/docker-compose.yml
- docker-compose up -d

**Default credentials**

<img width="1235" height="785" alt="image" src="https://github.com/user-attachments/assets/6947d460-3b4f-4b2b-80f0-ee389b98e3ba" />

- username: admin
- password: admin
  
---------------------------------------------------------------------------------------------------------------------

**Step 2: Create a New Project**

<img width="1864" height="965" alt="image" src="https://github.com/user-attachments/assets/60e6f78b-c713-4353-9e32-e3319b42b4d1" />
<img width="1866" height="664" alt="image" src="https://github.com/user-attachments/assets/7097402e-077a-437b-bf85-ec2daa7de2ff" />

---------------------------------------------------------------------------------------------------------------------

**Step 3: Upload Your SBOM File**

<img width="1854" height="635" alt="image" src="https://github.com/user-attachments/assets/46d2f18b-5870-498f-84de-243c9346b590" />

---------------------------------------------------------------------------------------------------------------------

**Scanning Result**

<img width="1847" height="777" alt="image" src="https://github.com/user-attachments/assets/0a6ab2b8-1caf-46f8-ba9e-a54717d76c9f" />
<img width="1860" height="935" alt="image" src="https://github.com/user-attachments/assets/40b8776b-bfab-4445-bb61-5bc5ab1612ad" />


