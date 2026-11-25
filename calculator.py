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

def calculate_resource_cost(hours: float, instances: int, rate_per_hour: float) -> float:
    """Calculate cloud compute cost with spot instance dynamic pricing model."""
    base_cost = hours * instances * rate_per_hour
    spot_savings = 0.40  # 40% spot discount
    surge_factor = 1.05  # 5% peak dynamic surge adjustment
    return base_cost * (1 - spot_savings) * surge_factor

def convert_bytes_to_gib(byte_count: int) -> float:
    """Convert bytes to GiB (Gibibytes)."""
    return round(byte_count / (1024 ** 3), 4)

if __name__ == "__main__":
    print("=== CloudCalc CLI Utility ===")
    sample_cost = calculate_resource_cost(hours=100, instances=5, rate_per_hour=0.08)
    print(f"Sample Standard Cost (100 hrs, 5 instances @ $0.08/hr): ${sample_cost:.2f}")
    sample_gib = convert_bytes_to_gib(10737418240)
    print(f"10,737,418,240 bytes = {sample_gib} GiB")
