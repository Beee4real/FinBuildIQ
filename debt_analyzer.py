"""
debt_analyzer.py
----------------
Core logic for analyzing user financial data and estimating debt health.

This module will later expand to include:
- BVN/SSN credit verification
- AI-based pattern analysis
- Spending category insights
"""

from typing import Dict


def analyze_debt(data: Dict) -> Dict:
    """
    Analyzes a user's debt and spending data to estimate a 'Debt Score'.

    Args:
        data (dict): {
            "income": float,
            "expenses": float,
            "debts": float,
            "credit_limit": float
        }

    Returns:
        dict: containing debt score and health interpretation
    """
    try:
        income = float(data.get("income", 0))
        debts = float(data.get("debts", 0))
        credit_limit = float(data.get("credit_limit", 0))

        # Calculate Debt-to-Income (DTI) ratio
        dti = (debts / income) * 100 if income > 0 else 0

        # Calculate credit utilization
        utilization = (debts / credit_limit) * 100 if credit_limit > 0 else 0

        # Combine for overall debt score
        score = max(0, 100 - (dti * 0.6 + utilization * 0.4))

        # Interpret the score
        if score >= 80:
            health = "Excellent"
        elif score >= 60:
            health = "Good"
        elif score >= 40:
            health = "Fair"
        else:
            health = "Poor"

        return {
            "debt_score": round(score, 2),
            "health_status": health,
            "debt_to_income_ratio": round(dti, 2),
            "credit_utilization": round(utilization, 2)
        }

    except Exception as e:
        return {"error": str(e)}
