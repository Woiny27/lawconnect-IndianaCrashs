# Indiana ARIES Crash Audit

This repository contains modules and scripts for auditing the Indiana ARIES crash report system, including:

- **assessor/indiana/audit_gateway.py**: Audits the ARIES/BuyCrash portal for security headers and exposure risks.
- **assessor/indiana/fetch_crash_cases.py**: Fetches crash case data from the NHTSA Crash API for Indiana (2024–2025).
- **assessment_report.js**: Formats audit findings and vulnerabilities into structured assessment reports.

## Usage

### Python Audit & Fetch Scripts
```bash
cd alawconnect-Indiana-Audit
python3 assessor/indiana/audit_gateway.py
python3 assessor/indiana/fetch_crash_cases.py
```

### Node.js Assessment Report
```bash
cd alawconnect-Indiana-Audit
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
Since Indiana's row-level data is behind a commercial paywall, the proto
