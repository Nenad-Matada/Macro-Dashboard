from fastapi import APIRouter
from app.services.data_services import load_macro_data
from app.services.macro_logic import explain_indicator
from app.services.regime_detector import detect_regime

router = APIRouter()

@router.get("/macro-data")
def get_macro_data():
    data = get_macro_data()

    explained = {
        key : {
            "value" : value,
            "explanation": explain_indicator(key, value)
        }
        for key, value in data.items()
    }

    regime = detect_regime(data)

    return{
        "indicators": explained,
        "regime": regime
    }