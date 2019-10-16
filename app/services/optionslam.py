import json
from datetime import datetime
from typing import List

import requests


def get_earnings_dates(stock_symbol: str, last: int = 4) -> List[str]:
    """Return earnings dates in format YYYY-MM-DD"""
    r = requests.get(f'https://www.optionslam.com/tv/marks?symbol={stock_symbol}')
    try:
        timestamps = r.json()['time'][:last]
    except (json.decoder.JSONDecodeError, KeyError):
        return []
    return [datetime.fromtimestamp(ts).strftime('%Y-%m-%d') for ts in timestamps]
