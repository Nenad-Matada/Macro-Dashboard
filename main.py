from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.services.chart_service import interest_rate_chart, currency_chart
from app.services.macro_logic import explain_indicator
from app.services.data_services import load_macro_data
from app.services.regime_detector import detect_regime
from app.services.market_insight import get_market_insights
from app.services.confidence_score import calculate_confidence, explain_confidence
from app.services.summary_service import generate_summary
from fastapi.staticfiles import StaticFiles
from app.api import macro

app = FastAPI()
app.include_router(macro.router)

templates = Jinja2Templates(directory= "app/templates")
app.mount("/static", StaticFiles(directory= "app/static"), name= "static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard")
def dashboard(request: Request):
    data = load_macro_data()

    explained = {
        key: {
            "value": value,
            "explanation": explain_indicator(key, value)
        }
        for key, value in data.items()
    }

    # Regime
    regime = detect_regime(data)

    # Charts
    rate_chart = interest_rate_chart()
    fx_chart = currency_chart()

    # Insights of Market
    insights = get_market_insights(data, regime)

    # Confidence Score of Market
    confidence = calculate_confidence(data)
    confidence_text = explain_confidence(confidence)

    # Macro Summary
    summary = generate_summary(data, regime, insights, confidence)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "data": explained,
            "regime": regime,
            "rate_chart": rate_chart,
            "fx_chart": fx_chart,
            "insights": insights,
            "confidence": confidence,
            "confidence_text": confidence_text,
            "summary": summary
        }
    )