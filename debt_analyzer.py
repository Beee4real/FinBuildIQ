# src/debt_analyzer.py

import numpy as np
import pandas as pd

def calculate_debt_score(data, verified_identity=False, credit_history=0, spending_behavior=None):
    """
    Calculates the FinBuildIQ DebtIQ Score based on spending habits, 
    debt ratio, and verified financial identity.

    Parameters
    ----------
    data : dict
        User financial data, should include:
        {
            "income": float,
            "expenses": float,
            "total_debt": float,
            "credit_limit": float,
            "debt_ratio": float (optional)
        }

    verified_identity : bool
        True if the user's BVN/SSN or equivalent identity has been verified.

    credit_history : int or float
        Historical credit rating or credit score (0–100 scale).

    spending_behavior : list or None
        Optional list of spending trend values (0–100) representing user discipline.

    Returns
    -------
    dict
        {
            "DebtIQ_Score": float,
            "Risk_Level": str,
            "Message": str
        }
    """

    # Compute missing debt ratio if not provided
    if "debt_ratio" not in data:
        income = data.get("income", 0)
        total_debt = data.get("total_debt", 0)
        data["debt_ratio"] = (total_debt / income) if income > 0 else 0.5

    # Default weights for scoring
    w_spending = 0.4
    w_debt_ratio = 0.3
    w_credit_history = 0.2
    w_verification = 0.1

    # --- Calculate Sub-Scores ---
    spending_score = np.clip(100 - np.mean(spending_behavior or [50]), 0, 100)
    debt_ratio = min(data["debt_ratio"], 1.0)
    debt_score = (1 - debt_ratio) * 100
    credit_score = min(max(credit_history, 0), 100)
    verification_bonus = 10 if verified_identity else 0

    # --- Compute Final Score ---
    total_score = (
        (spending_score * w_spending)
        + (debt_score * w_debt_ratio)
        + (credit_score * w_credit_history)
        + (verification_bonus * w_verification)
    )

    total_score = round(total_score, 2)

    # --- Risk Level Classification ---
    if total_score >= 80:
        risk_level = "Low Risk"
        message = "Excellent financial health! Keep it up."
    elif 60 <= total_score < 80:
        risk_level = "Moderate Risk"
        message = "Your finances are stable, but review spending and debt exposure."
    elif 40 <= total_score < 60:
        risk_level = "High Risk"
        message = "Warning: Your debt pattern may be risky. Consider restructuring."
    else:
        risk_level = "Critical Risk"
        message = "Immediate financial attention required!"

    return {
        "DebtIQ_Score": total_score,
        "Risk_Level": risk_level,
        "Message": message
    }


# --- Test Block ---
if __name__ == "__main__":
    sample_data = {
        "income": 5000,
        "expenses": 3200,
        "total_debt": 1500,
        "credit_limit": 10000
    }

    result = calculate_debt_score(
        data=sample_data,
        verified_identity=True,
        credit_history=78,
        spending_behavior=[45, 60, 55, 65, 50]
    )

    print("FinBuildIQ Debt Analysis Result:")
    print(result)
