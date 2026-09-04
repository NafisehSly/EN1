import ta

def prepare(df):
    x=df.copy()
    x["ema20"]=ta.trend.EMAIndicator(x.close,20).ema_indicator()
    x["ema200"]=ta.trend.EMAIndicator(x.close,200).ema_indicator()
    x["rsi"]=ta.momentum.RSIIndicator(x.close).rsi()
    x["adx"]=ta.trend.ADXIndicator(x.high,x.low,x.close).adx()
    return x

def run_strategy(data):
    h4=prepare(data["4H"])
    h1=prepare(data["1H"])
    m15=prepare(data["15M"])
    return {
        "signal":"WAIT",
        "h4":h4.iloc[-1].to_dict(),
        "h1":h1.iloc[-1].to_dict(),
        "m15":m15.iloc[-1].to_dict(),
        "trades":[]
    }
