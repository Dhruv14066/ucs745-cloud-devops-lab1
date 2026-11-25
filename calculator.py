"""
CloudCalc CLI - DevOps Cloud Resource and Metric Utility
Author: Dhruv
UCS 745 Cloud and DevOps Lab Assignment
"""

def add(a, b):
    """Return sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return product of two numbers."""
    return a * b

def divide(a, b):
    """Return division result, avoiding division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate_resource_cost(hours: float, instances: int, rate_per_hour: float, pricing_tier: str = "standard") -> float:
    """
    Calculate cloud compute cost with unified multi-tier pricing models.
    RESOLVED MERGE CONFLICT: Integrated Enterprise Volume Pricing and Spot Instance Dynamic Pricing.
    
    Supported Tiers:
    - 'standard': 5% baseline tier discount
    - 'enterprise': 10% volume discount (15% if instances > 10)
    - 'spot': 40% spot discount with 5% dynamic peak surge factor
    """
    base_cost = hours * instances * rate_per_hour
    
    tier = pricing_tier.lower()
    if tier == "spot":
        spot_savings = 0.40  # 40% spot discount
        surge_factor = 1.05  # 5% peak dynamic surge adjustment
        return round(base_cost * (1 - spot_savings) * surge_factor, 2)
    elif tier == "enterprise":
        discount = 0.15 if instances > 10 else 0.10  # 10-15% enterprise volume discount
        return round(base_cost * (1 - discount), 2)
    elif tier == "standard":
        discount = 0.05  # 5% standard tier discount
        return round(base_cost * (1 - discount), 2)
    else:
        raise ValueError(f"Unknown pricing tier: {pricing_tier}. Valid options: 'standard', 'enterprise', 'spot'")

def convert_bytes_to_gib(byte_count: int) -> float:
    """Convert bytes to GiB (Gibibytes)."""
    return round(byte_count / (1024 ** 3), 4)

if __name__ == "__main__":
    print("=== CloudCalc CLI Utility (Resolved & Unified) ===")
    std = calculate_resource_cost(100, 5, 0.08, pricing_tier="standard")
    ent = calculate_resource_cost(100, 15, 0.08, pricing_tier="enterprise")
    spot = calculate_resource_cost(100, 5, 0.08, pricing_tier="spot")
    print(f"Standard Tier (100 hrs, 5 instances @ $0.08/hr):   ${std:.2f}")
    print(f"Enterprise Tier (100 hrs, 15 instances @ $0.08/hr): ${ent:.2f}")
    print(f"Spot Dynamic Tier (100 hrs, 5 instances @ $0.08/hr): ${spot:.2f}")
    sample_gib = convert_bytes_to_gib(10737418240)
    print(f"Storage: 10,737,418,240 bytes = {sample_gib} GiB")
