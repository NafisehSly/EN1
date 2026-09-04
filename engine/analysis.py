
import ta

def run_engine(df):

    close = df["close"]

    ema20 = ta.trend.EMAIndicator(
        close,
        window=20
    ).ema_indicator()

    ema50 = ta.trend.EMAIndicator(
        close,
        window=50
    ).ema_indicator()

    rsi = ta.momentum.RSIIndicator(
        close
    ).rsi()

    adx = ta.trend.ADXIndicator(
        df["high"],
        df["low"],
        close
    ).adx()

    last_price = close.iloc[-1]

    if ema20.iloc[-1] > ema50.iloc[-1] and adx.iloc[-1] > 20:
        signal = "LONG"
    elif ema20.iloc[-1] < ema50.iloc[-1] and adx.iloc[-1] > 20:
        signal = "SHORT"
    else:
        signal = "WAIT"

    confidence = round(min(100, abs(rsi.iloc[-1]-50)*2 + adx.iloc[-1]),1)

    return {
        "price": round(last_price,2),
        "signal": signal,
        "trend": "BULLISH" if ema20.iloc[-1] > ema50.iloc[-1] else "BEARISH",
        "rsi": round(rsi.iloc[-1],2),
        "adx": round(adx.iloc[-1],2),
        "confidence": confidence,
        "data_status":"OK",
        "engine_status":"RUNNING"
    }
