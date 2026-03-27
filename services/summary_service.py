def generate_summary(data, regime, insights, confidence):

    inflation = data.get("inflation", 0)
    rates = data.get("interest_rate", 0)
    growth = data.get("gdp_growth", 0)

    summary = f"The economy is currently in a {regime.lower()}." # Base summary

    if inflation > 5 and rates > 5:
        summary += " High inflation and high interest rates indicate tight financial conditions."
    elif growth < 2:
        summary += " Weak economic growth suggests a slowing economy."
    elif growth > 3:
        summary += " Strong growth indicates economic expansion."

    # market view
    eq_view = insights.get("Equities", "")
    if "📉" in eq_view:
        summary += " Equity markets may face pressure."
    elif "📈" in eq_view:
        summary += " Equity markets may perform well."

    # confidence view
    if confidence > 70:
        summary += " The signals are strong and relatively consistent."
    else:
        summary += " However, signals are mixed and should be interpreted cautiously."

    return summary
