
import ta

def run_backtest(df):

    close=df.close

    ema20=ta.trend.EMAIndicator(close,20).ema_indicator()
    ema50=ta.trend.EMAIndicator(close,50).ema_indicator()

    atr=ta.volatility.AverageTrueRange(
        df.high, df.low, close
    ).average_true_range()

    trades=[]
    position=None

    for i in range(60,len(df)):

        price=close.iloc[i]
        atr_value=atr.iloc[i]

        if position is None:

            if ema20.iloc[i] > ema50.iloc[i]:
                position={
                    "type":"LONG",
                    "entry":price,
                    "stop":price-atr_value*2,
                    "target":price+atr_value*4
                }

            elif ema20.iloc[i] < ema50.iloc[i]:
                position={
                    "type":"SHORT",
                    "entry":price,
                    "stop":price+atr_value*2,
                    "target":price-atr_value*4
                }

        else:

            high=df.high.iloc[i]
            low=df.low.iloc[i]

            exit_price=None
            reason=None

            if position["type"]=="LONG":

                if low <= position["stop"]:
                    exit_price=position["stop"]
                    reason="STOP LOSS"

                elif high >= position["target"]:
                    exit_price=position["target"]
                    reason="TAKE PROFIT"

            else:

                if high >= position["stop"]:
                    exit_price=position["stop"]
                    reason="STOP LOSS"

                elif low <= position["target"]:
                    exit_price=position["target"]
                    reason="TAKE PROFIT"

            if exit_price:

                if position["type"]=="LONG":
                    pnl=exit_price-position["entry"]
                else:
                    pnl=position["entry"]-exit_price

                trades.append({
                    "type":position["type"],
                    "entry":position["entry"],
                    "exit":exit_price,
                    "pnl":pnl,
                    "reason":reason
                })

                position=None


    wins=[t for t in trades if t["pnl"]>0]

    profit=sum(t["pnl"] for t in trades)

    return {
        "trades":trades,
        "count":len(trades),
        "win_rate":round(len(wins)/len(trades)*100,2) if trades else 0,
        "profit":round(profit,2)
    }
