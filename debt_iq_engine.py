# src/debt_iq_engine.py
import numpy as np
import pandas as pd

def compute_debt_iq(transactions):
    """
    Simple placeholder AI model:
    Computes a DebtIQ score based on total expenses, income ratio, and spending pattern.
    """
    if not transactions:
        return {"DebtIQ_Score": 0, "advice": "No data available"}

    df = pd.DataFrame(transactions)
    total_spent = df['amount'].sum()
    avg_spend = df['amount'].mean()
    
    # Simple logic (replace with ML model later)
    score = max(0, 100 - (total_spent / (avg_spend + 1)))
    advice = "Healthy spending pattern." if score > 60 else "You may be overspending."

    return {"DebtIQ_Score": round(score, 2), "advice": advice}
