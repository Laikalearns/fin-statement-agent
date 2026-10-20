"""Generate TLDR and pros/cons from ratios (rule-based)."""

def generate_tldr(ratios):
    """Simple rule-based TLDR."""
    points = []

    if ratios.get("Net Margin", 0) > 0.10:
        points.append("strong profitability")
    elif ratios.get("Net Margin", 0) < 0:
        points.append("unprofitable at the net level")

    if ratios.get("Free Cash Flow", 0) > 0:
        points.append("positive free cash flow")
    else:
        points.append("negative free cash flow")

    if ratios.get("Debt-to-Equity", 0) > 1.5:
        points.append("elevated leverage")
    elif ratios.get("Debt-to-Equity", 0) < 0.5:
        points.append("conservative balance sheet")

    if ratios.get("Current Ratio", 0) > 1.5:
        points.append("healthy liquidity")
    elif ratios.get("Current Ratio", 0) < 1:
        points.append("liquidity concerns")

    if not points:
        return "Mixed financial picture with no extreme signals."

    return "Company shows " + ", ".join(points) + "."

def generate_pros_cons(ratios):
    """Return lists of pros and cons."""
    pros = []
    cons = []

    if ratios.get("Gross Margin", 0) > 0.40:
        pros.append(f"Strong gross margin ({ratios['Gross Margin']:.1%})")
    elif ratios.get("Gross Margin", 0) < 0.20:
        cons.append(f"Thin gross margin ({ratios['Gross Margin']:.1%})")

    if ratios.get("Operating Margin", 0) > 0.15:
        pros.append(f"Healthy operating margin ({ratios['Operating Margin']:.1%})")
    elif ratios.get("Operating Margin", 0) < 0.05:
        cons.append(f"Low operating margin ({ratios['Operating Margin']:.1%})")

    if ratios.get("Net Margin", 0) > 0.10:
        pros.append(f"Solid net margin ({ratios['Net Margin']:.1%})")
    elif ratios.get("Net Margin", 0) < 0:
        cons.append("Net loss")

    if ratios.get("Current Ratio", 0) >= 1.5:
        pros.append(f"Comfortable current ratio ({ratios['Current Ratio']:.2f})")
    elif ratios.get("Current Ratio", 0) < 1.0:
        cons.append(f"Current ratio below 1 ({ratios['Current Ratio']:.2f})")

    if ratios.get("Debt-to-Equity", 0) < 0.8:
        pros.append(f"Conservative leverage (D/E {ratios['Debt-to-Equity']:.2f})")
    elif ratios.get("Debt-to-Equity", 0) > 1.5:
        cons.append(f"High leverage (D/E {ratios['Debt-to-Equity']:.2f})")

    if ratios.get("Free Cash Flow", 0) > 0:
        pros.append("Positive free cash flow")
    else:
        cons.append("Negative free cash flow")

    if ratios.get("ROE", 0) > 0.15:
        pros.append(f"Attractive ROE ({ratios['ROE']:.1%})")
    elif ratios.get("ROE", 0) < 0:
        cons.append("Negative ROE")

    if not pros:
        pros.append("No major standout strengths in the core ratios")
    if not cons:
        cons.append("No major red flags in the core ratios")

    return pros, cons
