def get_market_insights(data, regime):
    inflation = data.get("inflation", 0)
    rates = data.get("interest_rate",0)
    growth = data.get("gdp_growth",0)

    insights = {}

    # Tight Regime
    if inflation > 5 and rates > 5:
        insights = {
            "Equities": "📉 Likely to struggle due to high borrowing costs",
            "Bonds": "📈 May perform better as growth slows",
            "USD": "📈 Strong due to high interest rates",
            "Gold": "📈 Can perform well as inflation hedge"
        }

    # Stimulus Regime
    elif growth < 2 and rates < 3:
        insights = {
            "Equities": "📈 Likely to rise due to easy money",
            "Bonds": "📈 Supported by low interest rates",
            "USD": "📉 May weaken",
            "Gold": "📈 Benefits from loose policy"
        }

    # Goldilocks
    elif growth > 3 and inflation < 3:
        insights = {
            "Equities": "📈 Strong performance expected",
            "Bonds": "📉 Less attractive",
            "USD": "➡️ Stable",
            "Gold": "➡️ Neutral"
        }
        
    # Default
    else:
        insights = {
            "Equities": "➡️ Mixed signals",
            "Bonds": "➡️ Uncertain direction",
            "USD": "➡️ Stable",
            "Gold": "➡️ Neutral"
        }

    return insights
