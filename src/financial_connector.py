from typing import List, Dict, Any
import os

class FinancialConnector:
    def __init__(self):
        self.api_key = os.getenv("FINANCIAL_API_KEY", "demo_key")
        self.base_url = "https://api.example-bank.com/v1"
    
    def get_accounts(self, account_ids: List[str]) -> List[Dict[str, Any]]:
        """Fetch account data from financial API"""
        accounts = []
        
        for account_id in account_ids:
            # Mock data for demo - replace with actual API calls
            account_data = {
                "id": account_id,
                "type": "credit_card",
                "balance": 2500.00,
                "credit_limit": 5000.00,
                "minimum_payment": 75.00,
                "interest_rate": 0.1899,
                "last_payment_date": "2024-01-15"
            }
            accounts.append(account_data)
        
        return accounts
    
    def _make_api_call(self) -> Dict[str, Any]:
        """Make authenticated API call"""
        return {"status": "success", "data": "mock_api_response"}