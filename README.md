# Hardened Microservice CI/CD

Lightweight DevSecOps pipeline automating Shift-Left security practices on GitHub Actions.

### Pipeline Controls
- **Secrets Detection:** TruffleHog git entropy & token scanning
- **SAST:** Bandit code vulnerability analysis for Python
- **Container Hardening:** Hadolint Dockerfile analysis & least-privilege non-root runtime
- **Image CVE Scan:** Aquasec Trivy scanning container layers for High/Critical CVEs

### Run Locally
```bash
docker build -t microservice .
docker run --rm -p 8080:8080 microservice
```
