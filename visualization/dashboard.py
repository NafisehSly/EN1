
import plotly.graph_objects as go
import streamlit as st

def render_dashboard(df, result):

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("PRICE", result["price"])
    c2.metric("SIGNAL", result["signal"])
    c3.metric("TREND", result["trend"])
    c4.metric("CONFIDENCE", str(result["confidence"])+"%")

    st.subheader("ENGINE FLOW")

    st.code(
f'''
DATA FEED
   |
   OK ✓
   |
MARKET ANALYSIS
   |
   OK ✓
   |
SIGNAL ENGINE
   |
   {result["signal"]}
'''
    )

    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df["time"],
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"],
        name="BTC"
    ))

    fig.update_layout(
        height=650,
        title="BTCUSDT LIVE ENGINE1 CHART"
    )

    st.plotly_chart(fig, use_container_width=True)
