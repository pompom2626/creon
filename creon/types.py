from datetime import datetime
from typing_extensions import TypedDict


class Candle(TypedDict):
    start_time: datetime
    end_time: datetime
    open_price: int
    high_price: int
    low_price: int
    close_price: int
    volume: int
