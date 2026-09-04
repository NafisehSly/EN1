
import streamlit as st
from data.binance_feed import get_historical_data
from engine.backtest import run_backtest
from visualization.dashboard import show_report

st.set_page_config(layout="wide")

st.title("ENGINE 1 v0.5 - PROFESSIONAL BACKTEST")

df = get_historical_data()

report = run_backtest(df)

show_report(df, report)
