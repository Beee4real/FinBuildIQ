# src/credit_integration.py
def get_credit_data(country_code, user_identifier):
    """
    Placeholder for global credit data APIs.
    Nigeria → BVN API
    US → Experian / Equifax
    UK → TransUnion
    """
    mock_data = {
        "NG": {"score": 680, "source": "BVN"},
        "US": {"score": 720, "source": "Experian"},
        "UK": {"score": 705, "source": "TransUnion"},
    }
    return mock_data.get(country_code.upper(), {"score": "N/A", "source": "Unknown"})
