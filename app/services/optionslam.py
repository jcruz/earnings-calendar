import datetime
import json
from typing import List

import pytz
import requests

NEW_YORK = pytz.timezone('America/New_York')


def get_earnings_dates(stock_symbol: str, last: int = 4) -> List[str]:
    """Return earnings dates in format YYYY-MM-DD"""
    dates: List[str] = []
    r = requests.get(f'https://www.optionslam.com/tv/marks?symbol={stock_symbol}')
    try:
        timestamps = r.json()['time'][:last]
    except (json.decoder.JSONDecodeError, KeyError):
        return dates
    for ts in timestamps:
        dt = datetime.datetime.fromtimestamp(ts, tz=NEW_YORK)
        dt -= datetime.timedelta(days=1)
        dates.append(dt.strftime('%Y-%m-%d'))
    return dates
