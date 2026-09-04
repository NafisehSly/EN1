
import streamlit as st
from data.binance_feed import get_market_data
from engine.analysis import run_engine
from visualization.dashboard import render_dashboard

st.set_page_config(
    page_title="Engine1 AI Trading System",
    layout="wide"
)

st.title("ENGINE 1 - LIVE BTC INTELLIGENCE")

df = get_market_data()

result = run_engine(df)

render_dashboard(df, result)
