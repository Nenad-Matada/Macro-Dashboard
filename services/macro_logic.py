def explain_indicator(name, value):
    explanations = {
        "inflation": f"Inflation is at {value}%. Higher inflation reduces purchasing power and may trigger rate hikes.",
        "interest_rate": f"Interest rate is at {value}%. Higher interest rate make borrowing expensive.",
        "gdp_growth": f"GDP growth is {value}%. Higher growth indicates economic expansion.",
        "unemployment": f"Unemployment is {value}%. Higher unemployment indicate economic stress.",
        "currency_strength": f"Currency index is {value}. Currency strength impacts trade and capital flows."
    }

    return explanations.get(name, "No explanation avaliable.")