import json

def assess_indiana_portal():
    # Simulated audit of the Indiana ARIES/BuyCrash workflow
    findings = [
        {
            "field_detected": "phone_number",
            "endpoint": "/report/preview",
            "access_state": "pre-authentication",
            "sample_value": "317-555-0199",
            "severity": "high"
        },
        {
            "field_detected": "insurance_policy_number",
            "endpoint": "/aries/search/results",
            "access_state": "weakly_protected",
            "sample_value": "IN-PROV-99283X",
            "severity": "critical"
        }
    ]
    
    with open("assessment_report.json", "w") as f:
        json.dump(findings, f, indent=4)
    print("✅ assessment_report.json generated successfully.")

if __name__ == "__main__":
    assess_indiana_portal()
