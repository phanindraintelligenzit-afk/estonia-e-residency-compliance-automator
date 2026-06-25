"""Pipeline for Estonia E Residency Compliance Automator."""
from fastapi import FastAPI
from src.agents.contract_parser import contract_parser
from src.agents.redline_detector import redline_detector
from src.agents.risk_assessor import risk_assessor
from src.agents.compliance_checker import compliance_checker

app = FastAPI(title="Estonia E Residency Compliance Automator")

@app.post("/run")
def run_pipeline(input_data: dict):
    """Run the full agent pipeline."""
    result = input_data
    result = contract_parser(result)  # Parse contracts, extract key clauses, dates, parties
    result = redline_detector(result)  # Identify non-standard terms, risky clauses, deviations from template
    result = risk_assessor(result)  # Score contract risk, generate negotiation recommendations
    result = compliance_checker(result)  # Check GDPR, SOC2, and regulatory compliance requirements
    return {"status": "complete", "result": result}

@app.get("/health")
def health():
    return {"status": "ok"}
