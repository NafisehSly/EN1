import pandas as pd
import ta

def run_backtest(df, capital, risk, fee):

    x=df.copy()
    x["ema20"]=ta.trend.EMAIndicator(x.close,20).ema_indicator()
    x["ema200"]=ta.trend.EMAIndicator(x.close,200).ema_indicator()
    x["rsi"]=ta.momentum.RSIIndicator(x.close).rsi()
    x["adx"]=ta.trend.ADXIndicator(x.high,x.low,x.close).adx()
    x["atr"]=ta.volatility.AverageTrueRange(x.high,x.low,x.close).average_true_range()
    x["vol_ma"]=x.volume.rolling(20).mean()

    balance=capital
    trades=[]
    equity=[]

    position=None

    for i in range(200,len(x)):
        r=x.iloc[i]

        if position is None:
            if r.close>r.ema20 and r.rsi>50 and r.adx>30 and r.volume>r.vol_ma:
                risk_money=balance*risk/100
                size=risk_money/(r.atr*1.5)

                position={
                    "entry":r.close,
                    "stop":r.close-r.atr*1.5,
                    "target":r.close+r.atr*3,
                    "size":size
                }

        else:
            exit_price=None

            if r.low<=position["stop"]:
                exit_price=position["stop"]

            elif r.high>=position["target"]:
                exit_price=position["target"]

            if exit_price:
                pnl=(exit_price-position["entry"])*position["size"]
                pnl-=abs(pnl)*fee/100
                balance+=pnl

                trades.append({
                    "entry":position["entry"],
                    "exit":exit_price,
                    "pnl":round(pnl,2),
                    "balance":round(balance,2)
                })

                position=None

        equity.append({"index":i,"balance":balance})

    t=pd.DataFrame(trades)

    return {
        "initial":capital,
        "final":round(balance,2),
        "return":round((balance-capital)/capital*100,2),
        "trades":t,
        "equity":pd.DataFrame(equity)
    }