import streamlit as st
import plotly.graph_objects as go

def render(r):

    a,b,c=st.columns(3)

    a.metric("Initial",r["initial"])
    b.metric("Final",r["final"])
    c.metric("ROI %",r["return"])

    st.subheader("Equity Curve")

    fig=go.Figure()

    fig.add_trace(go.Scatter(
        x=r["equity"].time,
        y=r["equity"].balance
    ))

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("Trade Log")
    st.dataframe(r["trades"])