
import requests
import pandas as pd

def get_historical_data(symbol="BTCUSDT", interval="1h", limit=1000):

    data = requests.get(
        "https://api.binance.com/api/v3/klines",
        params={
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
    ).json()

    df = pd.DataFrame(data, columns=[
        "time","open","high","low","close",
        "volume","close_time","qav",
        "trades","tbv","tqv","ignore"
    ])

    for c in ["open","high","low","close","volume"]:
        df[c] = df[c].astype(float)

    df["time"] = pd.to_datetime(df["time"], unit="ms")

    return df
