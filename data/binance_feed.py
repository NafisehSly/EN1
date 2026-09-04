
import requests
import pandas as pd

def get_market_data(symbol="BTCUSDT", interval="5m", limit=300):

    url = "https://api.binance.com/api/v3/klines"

    response = requests.get(
        url,
        params={
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
    )

    raw = response.json()

    df = pd.DataFrame(raw, columns=[
        "time","open","high","low","close",
        "volume","close_time","qav",
        "trades","tbv","tqv","ignore"
    ])

    for c in ["open","high","low","close","volume"]:
        df[c] = df[c].astype(float)

    df["time"] = pd.to_datetime(df["time"], unit="ms")

    return df
