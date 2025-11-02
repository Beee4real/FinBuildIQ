# src/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from src.debt_iq_engine import compute_debt_iq
from src.debt_detector import detect_forgotten_debts
from src.credit_integration import get_credit_data

app = FastAPI(
    title="FinBuildIQ",
    description="AI-driven financial insight and debt intelligence system",
    version="1.0.0"
)

class Transaction(BaseModel):
    description: str
    amount: float
    date: str

@app.get("/")
def home():
    return {"message": "Welcome to FinBuildIQ API"}

@app.post("/analyze")
def analyze_transactions(data: list[Transaction], country_code: str = "NG", user_id: str = "demo_user"):
    tx_data = [t.dict() for t in data]

    score = compute_debt_iq(tx_data)
    forgotten = detect_forgotten_debts(tx_data)
    credit_info = get_credit_data(country_code, user_id)

    return {
        "DebtIQ": score,
        "ForgottenDebts": forgotten,
        "CreditProfile": credit_info
    }
