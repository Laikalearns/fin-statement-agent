#!/usr/bin/env python3
"""Financial Statement Analyzer Agent – entry point."""

import sys
from pathlib import Path

from agent.ratios import load_statements, calculate_ratios
from agent.narrative import generate_tldr, generate_pros_cons

def main():
    data_dir = Path("data")
    income_path = data_dir / "income.csv"
    balance_path = data_dir / "balance.csv"
    cashflow_path = data_dir / "cashflow.csv"

    print("Loading financial statements...")
    statements = load_statements(income_path, balance_path, cashflow_path)

    print("Calculating ratios...")
    ratios = calculate_ratios(statements)

    print("\n=== KEY RATIOS ===")
    for name, value in ratios.items():
        if isinstance(value, float):
            print(f"  {name}: {value:.2%}" if "margin" in name.lower() or "roe" in name.lower() else f"  {name}: {value:.2f}")
        else:
            print(f"  {name}: {value}")

    tldr = generate_tldr(ratios)
    pros, cons = generate_pros_cons(ratios)

    print("\n=== TLDR ===")
    print(tldr)

    print("\n=== PROS ===")
    for p in pros:
        print(f"  + {p}")

    print("\n=== CONS ===")
    for c in cons:
        print(f"  - {c}")

if __name__ == "__main__":
    main()
