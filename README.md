🌍 Global Macro Dashboard

A financial literacy-focused macroeconomic dashboard that helps users understand how key economic indicators impact financial markets.

🧠 Overview

Most people see economic data but don’t understand what it means.

This project solves that by transforming:

* 📊 Raw macro data
  ➡️ into
* 🧠 Clear explanations
* 📈 Market insights
* 📉 Investment implications

🚀 Features

📊 1. Real-Time Macro Indicators

* Inflation
* Interest Rates
* GDP Growth
* Unemployment
* Currency Strength

Data is fetched using:

* yfinance (market data)
* Alpha Vantage (inflation)
* World Bank API (GDP, unemployment)

🧠 2. Macro Regime Detector

Automatically classifies the economic environment:

* Tight Monetary Regime
* Stimulus Environment
* Goldilocks Economy
* Transitional Phase

📈 3. Market Insights Engine

Translates macro conditions into market impact:

* Equities (Stocks)
* Bonds
* USD / Currency
* Gold

Example:

> High inflation + high rates → Stocks may struggle, USD strengthens

📊 4. Confidence Score

Shows how reliable the macro signals are:

* Based on multiple indicators
* Encourages probabilistic thinking
* Teaches users not to rely on single data points

🧾 5. Today's Macro Summary (Key Feature)

A simple, human-readable explanation of the current macro environment:

> “The economy is in a tight monetary regime with high inflation and interest rates. This may pressure equities while supporting the US dollar.”

📉 6. Interactive Charts

* Interest Rate Trend (7-day)
* Currency Movement (USD/INR)

🎯 Goal

This project is built for:

> 📚 **Financial Literacy & Economic Awareness**

It helps users:

* Understand economic indicators
* Learn how macro affects markets
* Think like an investor

🛠️ Tech Stack

* Backend: FastAPI
* Frontend: HTML, CSS (Jinja2 templates)
* Data Sources:

  * yfinance
  * Alpha Vantage API
  * World Bank API
  * Visualization:Plotly

Built as a solo hackathon project combining:

* Economics
* Systematic Macro Thinking
* Python & Backend Development
  
📣 Final Thought

“Don’t just look at economic data—understand what it means.”
