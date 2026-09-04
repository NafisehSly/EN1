import streamlit as st
from data.loader import get_data
from engine.backtest import run_backtest
from visualization.dashboard import render

st.set_page_config(layout="wide")

st.title("ENGINE 1 v1.5 - PROFESSIONAL BACKTEST ENGINE")

capital = st.number_input("Initial Capital USDT", value=10000)
risk = st.number_input("Risk Per Trade %", value=1.0)
fee = st.number_input("Fee %", value=0.05)
slippage = st.number_input("Slippage %", value=0.02)

df = get_data()

result = run_backtest(
    df,
    capital,
    risk,
    fee,
    slippage
)

render(result)