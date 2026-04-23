# exposure_engine.py
import requests
import json

def assess_portal_exposure(url):
	# Simulated audit of the Indiana BuyCrash gateway
	# Goal: Detect if PII patterns exist in the public preview layer
	print(f"🔍 Inspecting endpoint: {url}")
    
	# Authorized demo inspection logic
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
	return findings

if __name__ == "__main__":
	results = assess_portal_exposure("https://www.buycrash.com/demo")
	with open("assessment_report.json", "w") as f:
		json.dump(results, f, indent=4)
