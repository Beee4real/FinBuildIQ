from typing import List, Dict
import math

class DebtAnalyzer:
    def analyze(self, accounts: List[Dict]) -> Dict:
        """Analyze debt and provide AI-driven insights"""
        total_debt = sum(acc["balance"] for acc in accounts)
        total_minimum = sum(acc["minimum_payment"] for acc in accounts)
        
        # Calculate weighted average interest rate
        weighted_rate = sum(acc["balance"] * acc["interest_rate"] for acc in accounts) / total_debt if total_debt > 0 else 0
        
        # Payoff timeline (months) using minimum payments
        payoff_months = self._calculate_payoff_time(total_debt, total_minimum, weighted_rate)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(accounts, total_debt)
        
        return {
            "total_debt": round(total_debt, 2),
            "monthly_payment": round(total_minimum, 2),
            "payoff_timeline": payoff_months,
            "recommendations": recommendations
        }
    
    def _calculate_payoff_time(self, balance: float, payment: float, rate: float) -> int:
        """Calculate months to pay off debt"""
        if payment <= balance * (rate / 12):
            return 999  # Never pays off with minimum
        
        monthly_rate = rate / 12
        months = -math.log(1 - (balance * monthly_rate) / payment) / math.log(1 + monthly_rate)
        return math.ceil(months)
    
    def _generate_recommendations(self, accounts: List[Dict], total_debt: float) -> List[str]:
        """Generate AI-driven debt recommendations"""
        recommendations = []
        
        if total_debt > 10000:
            recommendations.append("Consider debt consolidation to reduce interest rates")
        
        # Find highest interest rate account
        highest_rate_account = max(accounts, key=lambda x: x["interest_rate"])
        if highest_rate_account["interest_rate"] > 0.15:
            recommendations.append(f"Prioritize paying off high-interest debt (Account {highest_rate_account['id']})")
        
        # Credit utilization check
        for acc in accounts:
            if "credit_limit" in acc:
                utilization = acc["balance"] / acc["credit_limit"]
                if utilization > 0.7:
                    recommendations.append(f"Reduce credit utilization on Account {acc['id']} (currently {utilization:.0%})")
        
        return recommendations