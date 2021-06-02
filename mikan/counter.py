from typing import List, Optional, Tuple
from mikan.combine import NumberCombine, StandardCombine, TsuCombine
from mikan.compound import Compound
from mikan.number import Number
from mikan.word import Word
from mikan.writing import Writing

__all__ = [
    'Counter',
    'DayHourCounter',
    'MonthDayCounter',
    'MonthCounter',
    'PersonCounter',
    'TsuCounter',
]

class Counter(Word):
    pass

class CounterCompound(Compound):

    def __init__(self, words: List[Word], writings: Optional[List[Writing]]=None) -> None:

        if (
            (len(words) != 2) or
            not (isinstance(words[0], Number) and isinstance(words[1], Counter))
        ):
            raise ValueError

        super().__init__(words, writings=writings, combine=StandardCombine())

class DayHourCounter(Word):

    def __init__(self) -> None:
        super().__init__('時', 'じ')

class DayHourCounterCompound(Compound):

    __EXCEPTIONS = {
        4: ['よじ'],
        9: ['くじ'],
    }

    def __init__(
        self,
        words: Tuple[Number, Counter],
        writings: Optional[List[Writing]]=None
    ) -> None:

        if (
            (len(words) != 2) or
            not (isinstance(words[0], Number) and isinstance(words[1], DayHourCounter))
        ):
            raise ValueError

        super().__init__(words, writings=writings, combine=NumberCombine(self.__EXCEPTIONS))

class MonthDayCounter(Word):

    def __init__(self) -> None:
        super().__init__('日', 'にち')

class MonthDayCounterCompound(Compound):

    __EXCEPTIONS = {
        1: ['ついたち'],
        2: ['ふつか'],
        3: ['みっか'],
        4: ['よっか'],
        5: ['いつか'],
        6: ['むいか'],
        7: ['なのか'],
        8: ['ようか'],
        9: ['ここのか'],
        10: ['とおか'],
        14: ['じゅうよっか'],
        20: ['はつか'],
        24: ['にじゅうよっか'],
    }

    def __init__(
        self,
        words: Tuple[Number, Counter],
        writings: Optional[List[Writing]]=None
    ) -> None:

        if (
            (len(words) != 2) or
            not (isinstance(words[0], Number) and isinstance(words[1], MonthDayCounter))
        ):
            raise ValueError

        super().__init__(words, writings=writings, combine=NumberCombine(self.__EXCEPTIONS))

class MonthCounter(Word):

    def __init__(self) -> None:
        super().__init__('月', 'がつ')

class MonthCounterCompound(Compound):

    __EXCEPTIONS = {
        4: ['しがつ'],
        7: ['しちがつ'],
        9: ['くがつ'],
    }

    def __init__(
        self,
        words: Tuple[Number, Counter],
        writings: Optional[List[Writing]]=None
    ) -> None:

        if (
            (len(words) != 2) or
            not (isinstance(words[0], Number) and isinstance(words[1], MonthCounter))
        ):
            raise ValueError

        super().__init__(words, writings=writings, combine=NumberCombine(self.__EXCEPTIONS))

class PersonCounter(Word):

    def __init__(self) -> None:
        super().__init__('人', 'にん')

class PersonCounterCompound(Compound):

    __EXCEPTIONS = {
        1: ['ひとり'],
        2: ['ふたり'],
        4: ['よにん'],
        7: ['ななにん', 'しちにん'],
    }

    def __init__(
        self,
        words: Tuple[Number, Counter],
        writings: Optional[List[Writing]]=None
    ) -> None:

        if (
            (len(words) != 2) or
            not (isinstance(words[0], Number) and isinstance(words[1], PersonCounter))
        ):
            raise ValueError

        super().__init__(words, writings=writings, combine=NumberCombine(self.__EXCEPTIONS))

class TsuCounter(Word):

    def __init__(self) -> None:
        super().__init__('つ')

class TsuCounterCompound(Compound):

    __EXCEPTIONS = {
        1: ['ひとつ'],
        2: ['ふたつ'],
        3: ['みっつ'],
        4: ['よっつ'],
        5: ['いつつ'],
        6: ['むっつ'],
        7: ['ななつ'],
        8: ['やっつ'],
        9: ['ここのつ'],
        10: ['とお'],
    }

    def __init__(
        self,
        words: Tuple[Number, Counter],
        writings: Optional[List[Writing]]=None
    ) -> None:

        if (
            (len(words) != 2) or
            not (isinstance(words[0], Number) and isinstance(words[1], TsuCounter))
        ):
            raise ValueError

        super().__init__(words, writings=writings, combine=TsuCombine(self.__EXCEPTIONS))
