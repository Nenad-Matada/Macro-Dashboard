def detect_regime(data):
    inflation = data.get("inflation", 0)
    rates = data.get("interest_rate", 0)
    growth = data.get("gdp_growth", 0)

    if inflation > 5 and rates > 5:
        return "Tight Monetary Regime(Central Banks fighting inflation)"
    
    elif growth < 2 and rates < 3:
        return "Stimulus Environment (Growth support mode)"
    
    elif growth > 3 and inflation < 3:
        return "Goldilocks Economy (Stable growth, low inflation)"
    
    else:
        return "Mixed/Trasitional Regime"