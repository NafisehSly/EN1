import requests
import pandas as pd

def get_data(symbol="BTCUSDT", interval="15m", limit=1000):

    raw=requests.get(
        "https://api.binance.com/api/v3/klines",
        params={
            "symbol":symbol,
            "interval":interval,
            "limit":limit
        }
    ).json()

    df=pd.DataFrame(raw,columns=[
        "time","open","high","low","close","volume",
        "a","b","c","d","e","f"
    ])

    for c in ["open","high","low","close","volume"]:
        df[c]=df[c].astype(float)

    df["time"]=pd.to_datetime(df["time"],unit="ms")

    return df