import aiohttp
from typing import List, Dict
import os

class FinancialConnector:
    def __init__(self):
        self.api_key = os.getenv("FINANCIAL_API_KEY", "demo_key")
        self.base_url = "https://api.example-bank.com/v1"
    
    async def get_accounts(self, account_ids: List[str]) -> List[Dict]:
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
    
    async def _make_api_call(self, endpoint: str) -> Dict:
        """Make authenticated API call"""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/{endpoint}", headers=headers) as response:
                return await response.json()