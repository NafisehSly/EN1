
import plotly.graph_objects as go

def create_chart(df,result):
    fig=go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.time,
        open=df.open,
        high=df.high,
        low=df.low,
        close=df.close,
        name="BTC"
    ))

    for span,name in [(20,"EMA20"),(50,"EMA50"),(200,"EMA200")]:
        ema=df.close.ewm(span=span).mean()
        fig.add_trace(go.Scatter(x=df.time,y=ema,name=name))

    if result["signal"]!="WAIT":
        fig.add_trace(go.Scatter(
            x=[df.time.iloc[-1]],
            y=[df.close.iloc[-1]],
            mode="markers",
            marker={"size":16},
            name=result["signal"]
        ))

    fig.update_layout(height=700,title="BTCUSDT Engine1 v0.3")
    return fig
