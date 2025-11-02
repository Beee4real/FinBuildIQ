"""
identity_verifier.py
--------------------
Handles user identity and credit verification through
mock APIs for BVN (Nigeria) and SSN (global).

This will later connect to real endpoints or fintech APIs.
"""

from typing import Dict

def verify_identity(user_data: Dict) -> Dict:
    """
    Mock verification function that simulates credit data lookup
    based on BVN or SSN (or other supported IDs).
    """

    bvn = user_data.get("bvn")
    ssn = user_data.get("ssn")
    country = user_data.get("country", "").lower()

    # Mock verification results
    if bvn:
        return {
            "id_type": "BVN",
            "id_value": bvn,
            "country": country or "Nigeria",
            "credit_score": 720,
            "verified": True,
            "message": "BVN verified successfully via mock gateway."
        }

    elif ssn:
        return {
            "id_type": "SSN",
            "id_value": ssn,
            "country": country or "USA",
            "credit_score": 690,
            "verified": True,
            "message": "SSN verified successfully via mock credit API."
        }

    else:
        return {
            "verified": False,
            "message": "No valid identifier (BVN/SSN) provided."
        }
