def calculate_confidence(data):
    score = 0
    max_score = 5 # Total indicators is 5

    inflation = data.get("inflation", 0)
    interest_rate = data.get("interest_rate", 0)
    gdp_growth = data.get("gdp_growth",0)
    unemployment = data.get("gdp_growth",0)
    currency_strength = data.get("currency_strength", 0)

    if 2 <= inflation <= 3:
        score += 1

    if 2 <= interest_rate <= 5:
        score += 1

    if 2<= gdp_growth <=3:
        score += 1

    if unemployment< 5:
        score += 1

    if  currency_strength > 0:
        score +=1

    confidence_percent = int((score/max_score)*100)

    return confidence_percent

def explain_confidence(score):
    if score > 80:
        return "High confidence: Indicators are strongly aligned."
    
    elif score > 60:
        return "Moderate confidence: Most indicators align, but some uncertanity exsists."
    
    elif score > 40:
        return "Low confidence: Signals are mixed."
    
    else:
        return "Very low confidence: Indicators are unclear or conflicting."