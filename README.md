# FinBuildIQ 🏦

AI-driven debt tracker that connects to financial APIs and provides intelligent debt insights.

## Features

- **Smart Debt Analysis** - AI-powered debt scoring and payoff strategies
- **Financial API Integration** - Connect to banks and credit providers
- **Real-time Insights** - Track debt trends and optimization opportunities
- **Credit Utilization Monitoring** - Automated alerts and recommendations

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your API keys

# Run the application
python app.py
```

Visit `http://localhost:8000` to access the API.

## API Usage

### Analyze Debt
```bash
POST /analyze-debt
{
  "user_id": "user123",
  "account_ids": ["acc1", "acc2"]
}
```

**Response:**
```json
{
  "total_debt": 5000.00,
  "monthly_payment": 150.00,
  "payoff_timeline": 36,
  "recommendations": [
    "Prioritize paying off high-interest debt",
    "Consider debt consolidation"
  ]
}
```

## Tech Stack

- **Backend:** FastAPI, Python 3.8+
- **AI Engine:** Custom debt analysis algorithms
- **APIs:** Financial institution integrations
- **Deployment:** Docker ready

## Development

Built with Amazon Q Developer assistance for rapid prototyping and code generation.

## License

MIT