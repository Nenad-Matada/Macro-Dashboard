🌍 Global Macro Dashboard

A **financial literacy-focused macroeconomic dashboard** that helps users understand how key economic indicators impact financial markets.

---

## 🧠 Overview

Most people see economic data but don’t understand what it means.

This project solves that by transforming:

* 📊 Raw macro data
  ➡️ into
* 🧠 Clear explanations
* 📈 Market insights
* 📉 Investment implications

---

## 🚀 Features

### 📊 1. Real-Time Macro Indicators

* Inflation
* Interest Rates
* GDP Growth
* Unemployment
* Currency Strength

Data is fetched using:

* yfinance (market data)
* Alpha Vantage (inflation)
* World Bank API (GDP, unemployment)

---

### 🧠 2. Macro Regime Detector

Automatically classifies the economic environment:

* Tight Monetary Regime
* Stimulus Environment
* Goldilocks Economy
* Transitional Phase

---

### 📈 3. Market Insights Engine

Translates macro conditions into market impact:

* Equities (Stocks)
* Bonds
* USD / Currency
* Gold

Example:

> High inflation + high rates → Stocks may struggle, USD strengthens

---

### 📊 4. Confidence Score

Shows how reliable the macro signals are:

* Based on multiple indicators
* Encourages probabilistic thinking
* Teaches users not to rely on single data points

---

### 🧾 5. Today's Macro Summary (Key Feature)

A simple, human-readable explanation of the current macro environment:

> “The economy is in a tight monetary regime with high inflation and interest rates. This may pressure equities while supporting the US dollar.”

---

### 📉 6. Interactive Charts

* Interest Rate Trend (7-day)
* Currency Movement (USD/INR)

---

### Screenshots

<img width="1919" height="975" alt="Screenshot 2026-03-28 205133" src="https://github.com/user-attachments/assets/e26a76c9-d4bf-4249-9c43-b57cb440f593" />

---
<img width="1919" height="907" alt="Screenshot 2026-03-28 205209" src="https://github.com/user-attachments/assets/46d10ca0-f7fd-4256-8857-afa06ea95451" />

---

<img width="1919" height="677" alt="Screenshot 2026-03-28 205226" src="https://github.com/user-attachments/assets/b794c1e9-643b-4f50-9203-aa39d570d14e" />

---

## 🎯 Goal

This project is built for:

> 📚 **Financial Literacy & Economic Awareness**

It helps users:

* Understand economic indicators
* Learn how macro affects markets
* Think like an investor

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS (Jinja2 templates)
* **Data Sources:**

  * yfinance
  * Alpha Vantage API
  * World Bank API
* **Visualization:** Plotly

---

## 📂 Project Structure

```
macro_dashboard/
│
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── templates/
│   └── static/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/macro-dashboard.git
cd macro-dashboard
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add API Key

In `app/core/config.py`:

```python
ALPHA_VANTAGE_API_KEY = "your_api_key_here"
```

---

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

---

### 5. Open in browser

```
http://127.0.0.1:8000/dashboard
```

---

## 🧠 How It Works

1. Fetch macro data from multiple sources
2. Process and normalize data
3. Detect macro regime
4. Generate market insights
5. Calculate confidence score
6. Create summary for users

---

## 📌 Future Improvements

* Add country selection (India / US)
* More indicators (CPI, central bank rates)
* Better models for regime detection
* AI-based explanations

---

## 👨‍💻 Author

Built as a solo hackathon project combining:

* Economics
* Systematic Macro Thinking
* Python & Backend Development


---

## 📣 Final Thought

> “Don’t just look at economic data—understand what it means.”

---

