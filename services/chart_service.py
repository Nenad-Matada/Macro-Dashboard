import yfinance as yf
import plotly.graph_objs as go

# Interest Rate Chart
def interest_rate_chart():
    data = yf.Ticker("^TNX")
    hist = data.history(period="7d")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x= hist.index,
        y= hist["Close"],
        mode='lines+markers',
        name= 'Interest Rate'
    ))

    fig.update_layout(
        title= "Interest Rate (7 Day Trend)",
        xaxis_title= "Date",
        yaxis_title= "Rate (%)",
        template="plotly_dark"
    )

    return fig.to_html(full_html= False)

# Currency Chart
def currency_chart():
    data = yf.Ticker("USDINR=X")
    hist = data.history(period="7d")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist["Close"],
        mode="lines+markers",
        name="USD/INR"
    ))

    fig.update_layout(
        title="USD/INR (7 Day Trend)",
        xaxis_title = "Date",
        yaxis_title = "Exchange Rate",
        template="plotly_dark"
    )

    return fig.to_html(full_html=False)