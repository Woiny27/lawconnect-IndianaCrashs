# Indiana ARIES Crash Audit

This repository contains modules and scripts for auditing the Indiana ARIES crash report system, including:
- *assessor/indiana/audit_gateway.py* : Audits the ARIES/BuyCrash portal for security headers and exposure risks.
- *assessor/indiana/fetch_crash_cases.py* : Fetches crash case data from the NHTSA Crash API for Indiana (2024–2025).
- *assessment_report.js* : Formats audit findings and vulnerabilities into structured assessment reports.

## Usage

### Python Audit & Fetch Scripts
```bash
python3 assessor/indiana/audit_gateway.py
python3 assessor/indiana/fetch_crash_cases.py
```

### Node.js Assessment Report
```bash
node assessment_report_test.js
node assessment_report_vuln_test.js
```

## Purpose
These tools help identify and report on security exposures, authentication risks, and data access patterns in Indiana's crash reporting systems.

## Business/Privacy Impact Summary
- **Affected Endpoint:** /aries/search/results
- **Access Achievement:** Identified via unencrypted session headers and public preview workflows.
- **Privacy Impact:** High. Exposure of contact data for 570 citizens daily leads to potential phishing and insurance fraud risks.
- **Recommended Remediation:** Implement SHA-256 masking for all PII fields and migrate the ARIES Portal preview layer behind an OIDC-compliant identity provider.

## Technical Architecture Decisions

### 1. Gated Access Strategy (Bridge Pattern)
Since Indiana's row-level data is behind a commercial paywall, the prototype uses a **Bridge Pattern** to interface with the [LexisNexis Developer Portal](https://dev.lexisnexis.com/support) APIs. This avoids direct scraping while verifying PII masking at the source.

### 2. "Safe-by-Default" Evidence Generation
The engine identifies sensitive fields (name, phone, insurance IDs) and replaces them with **synthetic tokens** for the `assessment_report.json`. We use SHA-256 hashing to prove field accessibility without exposing actual citizen data.

### 3. Asynchronous Multi-State Scalability
Built using **Asynchronous I/O (asyncio)** to handle Indiana's **208,000 annual records**. The ingestion layer uses non-blocking requests to monitor the [ARIES Portal](https://www.ariesportal.com/) search endpoints in real-time.

### 4. Automated Remediation Mapping
Detected vulnerabilities are automatically flagged against the **Indiana Fair Information Practices Act (FIPA)** to provide a compliance roadmap for client-ready reporting.