from typing import List, Union, Optional, Sequence
import datetime
from mikan.base import BaseWord
from mikan.compound import Compound
from mikan.number import Number
from mikan.counter import Counter, MonthCounter, MonthDayCounter
from mikan.writing import Writing

__all__ = ['Date']

class Date(Compound):

    def __init__(
        self,
        words: Union[datetime.date, Sequence[BaseWord]],
        writings: Optional[List[Writing]]=None
    ) -> None:
        if isinstance(words, datetime.date):
            date = words
            words = [
                Number(date.year) + Counter('年', 'ねん'),
                Number(date.month) + MonthCounter(),
                Number(date.day) + MonthDayCounter(),
            ]
        else:
            raise ValueError
        super().__init__(words)
