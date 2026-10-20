"""Load statements and calculate key ratios."""

import pandas as pd
from pathlib import Path

def load_statements(income_path, balance_path, cashflow_path):
    """Load the three statement CSVs."""
    income = pd.read_csv(income_path)
    balance = pd.read_csv(balance_path)
    cashflow = pd.read_csv(cashflow_path)
    return {"income": income, "balance": balance, "cashflow": cashflow}

def _get(df, line_item, default=0.0):
    """Helper to extract a line item value (case-insensitive)."""
    row = df[df["line_item"].str.lower() == line_item.lower()]
    if row.empty:
        return default
    return float(row["amount"].iloc[0])

def calculate_ratios(statements):
    """Compute a set of common financial ratios."""
    inc = statements["income"]
    bal = statements["balance"]
    cf = statements["cashflow"]

    revenue = _get(inc, "Revenue")
    cogs = _get(inc, "Cost of Goods Sold")
    gross_profit = _get(inc, "Gross Profit", revenue - cogs)
    operating_income = _get(inc, "Operating Income")
    net_income = _get(inc, "Net Income")

    total_assets = _get(bal, "Total Assets")
    total_liabilities = _get(bal, "Total Liabilities")
    equity = _get(bal, "Total Equity", total_assets - total_liabilities)
    current_assets = _get(bal, "Current Assets")
    current_liabilities = _get(bal, "Current Liabilities")

    operating_cf = _get(cf, "Operating Cash Flow")
    capex = _get(cf, "Capital Expenditures")  # usually negative
    free_cash_flow = operating_cf + capex  # if capex is negative

    ratios = {
        "Revenue": revenue,
        "Gross Margin": gross_profit / revenue if revenue else 0,
        "Operating Margin": operating_income / revenue if revenue else 0,
        "Net Margin": net_income / revenue if revenue else 0,
        "Current Ratio": current_assets / current_liabilities if current_liabilities else 0,
        "Debt-to-Equity": total_liabilities / equity if equity else 0,
        "ROE": net_income / equity if equity else 0,
        "Operating Cash Flow": operating_cf,
        "Free Cash Flow": free_cash_flow,
    }
    return ratios
