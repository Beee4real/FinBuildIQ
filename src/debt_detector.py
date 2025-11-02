# src/debt_detector.py
def detect_forgotten_debts(transactions):
    """
    Placeholder that flags possible forgotten debts by looking at repeating payments 
    without corresponding credits (e.g., loan or subscription-like patterns).
    """
    flagged = []
    for t in transactions:
        desc = t['description'].lower()
        if "loan" in desc or "repayment" in desc or "owed" in desc:
            flagged.append(t)
    return {"potential_debts": flagged, "count": len(flagged)}
