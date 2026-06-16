**Docker** is a platform that packages applications and their dependencies into containers - lightweight, portable units that run consistently across different environments.

**Key Concepts:**

1. Dockerfile - A text file with instructions to build a Docker image (like a recipe)
2. Image - A template/snapshot created from a Dockerfile (like a blueprint)
3. Container - A running instance of an image (like an actual running application)
4. Base Image - The starting point for your image (e.g., Ubuntu, Alpine Linux)

------------------------------------------------------------------------------------------------------

**Step 1:** Create an Intentionally Insecure Dockerfile

<img width="600" height="770" alt="image" src="https://github.com/user-attachments/assets/b60f12b6-1e00-463e-8ce6-a208452b5ae7" />


------------------------------------------------------------------------------------------------------

**Step 2:** Create an Application File

<img width="600" height="260" alt="image" src="https://github.com/user-attachments/assets/27683c74-d235-47e4-9220-da5b8dcc9dc4" />

<img width="624" height="177" alt="image" src="https://github.com/user-attachments/assets/110294f9-9fab-4f0f-861d-951767d842bf" />

<img width="402" height="118" alt="image" src="https://github.com/user-attachments/assets/7711ab91-c2c3-443e-bbca-29ba8c0cadae" />

<img width="653" height="174" alt="image" src="https://github.com/user-attachments/assets/c8dabd4b-c775-4abb-b117-3a701cd3acb6" />

------------------------------------------------------------------------------------------------------

**Step 3:** Install Trivy
https://github.com/aquasecurity/trivy/releases

<img width="633" height="499" alt="image" src="https://github.com/user-attachments/assets/53d56945-44ee-4c44-8f73-5e1735ee6175" />

<img width="466" height="85" alt="image" src="https://github.com/user-attachments/assets/8680013d-a4f2-4344-8bb8-6e934c042392" />

<img width="700" height="159" alt="image" src="https://github.com/user-attachments/assets/edfb9ebe-013c-47d3-8b5e-a498c33f70ff" />


------------------------------------------------------------------------------------------------------

**Step 4:** Build the Insecure Docker Image

Command: docker build -f Dockerfile.insecure -t insecure-app:v1 .

<img width="1177" height="733" alt="image" src="https://github.com/user-attachments/assets/3d18656a-fb5b-448b-a3d1-088db3f6859f" />

------------------------------------------------------------------------------------------------------

**Step 5:** Scan with Trivy

Command: trivy image insecure-app:v1
<img width="1886" height="962" alt="image" src="https://github.com/user-attachments/assets/492a0a63-e29e-4e81-a9dd-5787f4159c22" />

----------------------------------------------------------------------------------------------------------------------

Now let's create a SECURE Dockerfile that fixes all the vulnerabilities and follows best practices.

**Step 6:** Create a Secure Dockerfile

<img width="604" height="706" alt="image" src="https://github.com/user-attachments/assets/07bd5192-5f2e-4e4f-a9ce-b01a4e98fee5" />

<img width="599" height="399" alt="image" src="https://github.com/user-attachments/assets/96799d1a-4aa5-4f57-b1b9-721e29960ac9" />

------------------------------------------------------------------------------------------------------

**Step 7:** Build the Secure Docker Image

Command: docker build -f Dockerfile.secure -t secure-app:v1 .
<img width="1843" height="553" alt="image" src="https://github.com/user-attachments/assets/153417b8-590a-457b-a583-183d9188c7bf" />

<img width="1239" height="414" alt="image" src="https://github.com/user-attachments/assets/640d5c3e-135d-41ef-b9ac-2fb820bbc2b7" />

------------------------------------------------------------------------------------------------------

<img width="613" height="355" alt="image" src="https://github.com/user-attachments/assets/39716a26-3bb6-4935-9408-e0fddf82a41c" />

----------------------------------------------------------------------------------------------------------------------

**Get interactive shell:**

**Insecure Docker File:**

**Commands:**

docker run -d -p 8080:80 --name insecure-container insecure-app:v1

docker exec -it insecure-container /bin/bash

<img width="1218" height="194" alt="image" src="https://github.com/user-attachments/assets/63e99eca-3b32-4e7f-8942-f74c7d83e247" />

**Secure Docker File:**

**Commands:**

docker run -d -p 8081:8080 --name secure-container secure-app:v1

docker exec -it secure-container /bin/bash

<img width="1006" height="194" alt="image" src="https://github.com/user-attachments/assets/5fa65ea3-4f04-4c05-a941-0224db17989e" />
