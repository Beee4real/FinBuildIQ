"""
main.py
--------
FinBuildIQ Backend — FastAPI Application
Provides endpoints for:
1. Debt/Financial analysis
2. BVN/SSN-based credit verification (mock)
"""

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, List, Dict
from identity_verifier import verify_identity

app = FastAPI(
    title="FinBuildIQ API",
    description="Agentic AI backend for personal finance, debt management, and credit verification.",
    version="1.0.0",
)

# ------------------------------
# Data Models
# ------------------------------

class DebtItem(BaseModel):
    creditor: str
    amount: float
    interest_rate: float
    due_date: str  # simple string format e.g., "2025-12-01"

class AnalyzeRequest(BaseModel):
    user_id: Optional[str] = None
    debts: List[DebtItem]
    monthly_income: float
    monthly_expenses: float
    credit_score: Optional[int] = None


# ------------------------------
# Endpoints
# ------------------------------

@app.get("/")
def home():
    return {"message": "Welcome to FinBuildIQ API – Financial Intelligence powered by Agentic AI."}


@app.post("/analyze")
def analyze_debt(data: AnalyzeRequest):
    """
    Analyze user's debts and generate insights.
    """
    total_debt = sum(item.amount for item in data.debts)
    avg_interest = sum(item.interest_rate for item in data.debts) / len(data.debts)
    monthly_savings = data.monthly_income - data.monthly_expenses
    debt_to_income_ratio = total_debt / max(data.monthly_income, 1)

    # Basic AI-like logic for debt health
    if debt_to_income_ratio < 0.3:
        health_status = "Excellent"
    elif debt_to_income_ratio < 0.6:
        health_status = "Moderate"
    else:
        health_status = "Critical"

    # Adjust with credit score if available
    credit_adjustment = 0
    if data.credit_score:
        if data.credit_score > 700:
            credit_adjustment = +0.1
        elif data.credit_score < 600:
            credit_adjustment = -0.1

    adjusted_score = max(0, min(1, (1 - debt_to_income_ratio) + credit_adjustment))

    return {
        "total_debt": total_debt,
        "average_interest_rate": avg_interest,
        "monthly_savings": monthly_savings,
        "debt_to_income_ratio": round(debt_to_income_ratio, 2),
        "financial_health": health_status,
        "ai_score": round(adjusted_score, 2)
    }


@app.post("/verify")
async def verify_user_identity(
    bvn: str | None = Query(None, description="User BVN for Nigerian users"),
    ssn: str | None = Query(None, description="User SSN for international users"),
    country: str | None = Query("Nigeria", description="User's country")
):
    """
    Verify a user's identity and fetch mock credit score using BVN or SSN.
    This mimics credit lookup services for demo and testing.
    """
    user_data = {"bvn": bvn, "ssn": ssn, "country": country}
    result = verify_identity(user_data)
    return {"success": True, "verification": result}


# ------------------------------
# Run Command
# ------------------------------
# Run this app with:
# uvicorn src.main:app --reload
