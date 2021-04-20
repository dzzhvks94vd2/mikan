from typing import List, Optional, Tuple, Callable, Dict
from mikan.compound import CompoundBase
from mikan.number import Number
from mikan.word import Word
from mikan.reading import Reading
from mikan.writing import Writing

__all__ = [
    'Counter',
    'DayHourCounter',
    'MonthDayCounter',
    'MonthCounter',
    'TsuCounter',
]

class Counter(Word):
    pass

class CounterCompound(CompoundBase):

    __EXCEPTIONS: Dict[str, Dict[str, Callable[[str, str], List[str]]]] = {
        'いち': {
            'ふ': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'ひ': lambda x, y: [x[:-1] + 'っぴ' + y[1:]],
            'ほ': lambda x, y: [x[:-1] + 'っぽ' + y[1:]],
        },
        'さん': {
            'ふ': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'ひ': lambda x, y: [x + 'び' + y[1:]],
            'ほ': lambda x, y: [x + 'ぼ' + y[1:]],
        },
        'ろく': {
            'ふ': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'ひ': lambda x, y: [x[:-1] + 'っぴ' + y[1:]],
            'ほ': lambda x, y: [x[:-1] + 'っぽ' + y[1:]],
        },
        'はち': {
            'ふ': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'ひ': lambda x, y: [x[:-1] + 'っぴ' + y[1:], x + y],
            'ほ': lambda x, y: [x[:-1] + 'っぽ' + y[1:], x + y],
        },
        'じゅう': {
            'ふ': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'ひ': lambda x, y: [x[:-1] + 'っぴ' + y[1:]],
            'ほ': lambda x, y: [x[:-1] + 'っぽ' + y[1:]],
        }
    }

    def _find_func(self, writing1: str, writing2: str) -> Optional[Callable[[str, str], List[str]]]:
        suffix = None
        if writing1[-3:] in self.__EXCEPTIONS:
            suffix = writing1[-3:]
        elif writing1[-2:] in self.__EXCEPTIONS:
            suffix = writing1[-2:]
        if suffix is None:
            return None

        return self.__EXCEPTIONS[suffix].get(writing2[0])

    def __init__(self, words: List[Word], writings: Optional[List[Writing]]=None) -> None:

        if (
            (len(words) != 2) or
            not (isinstance(words[0], Number) and isinstance(words[1], Counter))
        ):
            raise ValueError

        number, counter = words

        if writings is None:
            writings = []

            for wri1 in number.writings:
                for wri2 in counter.writings:
                    if isinstance(wri1, Reading) and isinstance(wri2, Reading):
                        func = self._find_func(wri1, wri2)
                        if func is not None:
                            writings.extend([Reading(reading) for reading in func(wri1, wri2)])
                        else:
                            writings.append(wri1 + wri2)
                    elif (not isinstance(wri1, Reading)) and (not isinstance(wri2, Reading)):
                        writings.append(wri1 + wri2)

        super().__init__(words, writings=writings)

class DayHourCounter(Word):

    def __init__(self) -> None:
        super().__init__('時', 'じ')

class DayHourCounterCompound(CompoundBase):

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

        number, counter = words

        if writings is None:
            writings = []
            value = int(number)
            if value in self.__EXCEPTIONS:
                writings = [Reading(reading) for reading in self.__EXCEPTIONS[value]]
            else:
                writings.extend(self._combine_writings(
                    number.writings,
                    counter.writings,
                    lambda x: isinstance(x, Reading)
                ))
            writings.extend(self._combine_writings(
                number.writings,
                counter.writings,
                lambda x: not isinstance(x, Reading)
            ))

        super().__init__(words, writings=writings)

class MonthDayCounter(Word):

    def __init__(self) -> None:
        super().__init__('日', 'にち')

class MonthDayCounterCompound(CompoundBase):

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

        number, counter = words

        if writings is None:
            writings = []
            value = int(number)
            if value in self.__EXCEPTIONS:
                writings = [Reading(reading) for reading in self.__EXCEPTIONS[value]]
            else:
                writings.extend(self._combine_writings(
                    number.writings,
                    counter.writings,
                    lambda x: isinstance(x, Reading)
                ))
            writings.extend(self._combine_writings(
                number.writings,
                counter.writings,
                lambda x: not isinstance(x, Reading)
            ))

        super().__init__(words, writings=writings)

class MonthCounter(Word):

    def __init__(self) -> None:
        super().__init__('月', 'がつ')

class MonthCounterCompound(CompoundBase):

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

        number, counter = words

        if writings is None:
            writings = []
            value = int(number)
            if value in self.__EXCEPTIONS:
                writings = [Reading(reading) for reading in self.__EXCEPTIONS[value]]
            else:
                writings.extend(self._combine_writings(
                    number.writings,
                    counter.writings,
                    lambda x: isinstance(x, Reading)
                ))
            writings.extend(self._combine_writings(
                number.writings,
                counter.writings,
                lambda x: not isinstance(x, Reading)
            ))

        super().__init__(words, writings=writings)

class TsuCounter(Word):

    def __init__(self) -> None:
        super().__init__('つ')

class TsuCounterCompound(CompoundBase):

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

        number, counter = words

        if writings is None:
            writings = []
            value = int(number)
            if value in self.__EXCEPTIONS:
                writings = [Reading(reading) for reading in self.__EXCEPTIONS[value]]
            for wri1 in number.writings:
                for wri2 in counter.writings:
                    if not isinstance(wri1, Reading):
                        writings.append(wri1 + wri2)

        super().__init__(words, writings=writings)
