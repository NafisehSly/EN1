
import ta

def run_engine(df):
    close=df.close

    ema20=ta.trend.EMAIndicator(close,20).ema_indicator()
    ema50=ta.trend.EMAIndicator(close,50).ema_indicator()
    ema200=ta.trend.EMAIndicator(close,200).ema_indicator()

    rsi=ta.momentum.RSIIndicator(close).rsi()
    adx=ta.trend.ADXIndicator(df.high,df.low,close).adx()
    atr=ta.volatility.AverageTrueRange(df.high,df.low,close).average_true_range()

    trend=30 if ema20.iloc[-1]>ema50.iloc[-1] else 15
    momentum=25 if 45<rsi.iloc[-1]<70 else 10
    strength=min(25, float(adx.iloc[-1]))
    long_term=20 if close.iloc[-1]>ema200.iloc[-1] else 10

    score=round(trend+momentum+strength+long_term,1)

    if score>=75 and ema20.iloc[-1]>ema50.iloc[-1]:
        signal="LONG"
    elif score>=75 and ema20.iloc[-1]<ema50.iloc[-1]:
        signal="SHORT"
    else:
        signal="WAIT"

    price=float(close.iloc[-1])

    if signal=="LONG":
        entry=price
        stop=price-float(atr.iloc[-1])*2
        target=price+float(atr.iloc[-1])*4
    elif signal=="SHORT":
        entry=price
        stop=price+float(atr.iloc[-1])*2
        target=price-float(atr.iloc[-1])*4
    else:
        entry=stop=target=None

    return {
        "price":round(price,2),
        "signal":signal,
        "trend":"BULLISH" if ema20.iloc[-1]>ema50.iloc[-1] else "BEARISH",
        "score":score,
        "entry":entry,
        "stop":stop,
        "target":target,
        "breakdown":{
            "Trend":trend,
            "Momentum":momentum,
            "ADX":round(strength,1),
            "Long Term":long_term
        },
        "reason":f"EMA20/50 trend | RSI {rsi.iloc[-1]:.1f} | ADX {adx.iloc[-1]:.1f}"
    }
