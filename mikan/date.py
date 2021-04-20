import datetime
from mikan.compound import Compound
from mikan.number import Number
from mikan.counter import Counter, MonthCounter, MonthDayCounter

__all__ = ['Date']

class Date(Compound):

    def __init__(self, date: datetime.date) -> None:
        words = [
            Number(date.year) + Counter('年', 'ねん'),
            Number(date.month) + MonthCounter(),
            Number(date.day) + MonthDayCounter(),
        ]
        super().__init__(words)
