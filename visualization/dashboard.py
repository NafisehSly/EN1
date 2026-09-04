
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show_report(df,r):

    a,b,c=st.columns(3)

    a.metric("Trades",r["count"])
    b.metric("Win Rate",str(r["win_rate"])+"%")
    c.metric("Profit",str(r["profit"]))

    st.subheader("Trade Report")

    st.dataframe(pd.DataFrame(r["trades"]))

    fig=go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.time,
        open=df.open,
        high=df.high,
        low=df.low,
        close=df.close
    ))

    fig.update_layout(height=650)

    st.plotly_chart(fig,use_container_width=True)
