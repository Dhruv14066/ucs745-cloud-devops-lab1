# CloudCalc CLI - DevOps Cloud Resource and Metric Utility

## Overview
CloudCalc is a lightweight Python utility designed for cloud engineers and DevOps practitioners to compute cloud workload metrics, estimate compute instance costs, and perform common unit conversions.

## Features
- Core arithmetic operations (Addition, Subtraction, Multiplication, Division)
- **Unified Multi-Tier Cloud Pricing Engine** *(Resolved Merge Conflict)*:
  - **Standard Tier**: Baseline 5% loyalty discount
  - **Enterprise Volume Tier**: Tiered volume discount (10% baseline, 15% for >10 instances)
  - **Spot Instance Dynamic Tier**: 40% spot discount with 5% peak dynamic surge adjustments
- Cloud storage metric conversions (Bytes to GiB)

## Usage
Run the utility using Python 3:
```bash
python calculator.py
```
