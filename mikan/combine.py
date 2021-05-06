import abc
from typing import Callable, Dict, Iterable, List, Optional, SupportsInt

from mikan.base import BaseWord
from mikan.reading import Reading
from mikan.writing import Writing

class BaseCombine(abc.ABC):

    @abc.abstractmethod
    def __call__(self, words: Iterable[BaseWord]) -> List[Writing]:
        pass

def _combine_writings(
    writings1: List[Writing],
    writings2: List[Writing],
    testfunc: Optional[Callable[[Writing, Writing], bool]]=None
) -> List[Writing]:

    writings = []
    for writing1 in writings1:
        for writing2 in writings2:
            if testfunc is None or testfunc(writing1, writing2):
                writings.append(writing1 + writing2)
    return writings

class DefaultCombine(BaseCombine):

    def __call__(self, words: Iterable[BaseWord]) -> List[Writing]:
        readings = [Writing.create('')]
        writings = [Writing.create('')]
        for word in words:
            wreadings: List[Writing] = []
            wwritings: List[Writing] = []
            for wri in word.writings:
                if isinstance(wri, Reading):
                    wreadings.append(wri)
                else:
                    wwritings.append(wri)
            if len(readings) > 0 and len(wreadings) > 0:
                new_readings = _combine_writings(readings, wreadings)
            else:
                new_readings = []

            if len(writings) > 0 and len(wwritings) > 0:
                new_writings = _combine_writings(writings, wwritings)
            elif len(writings) > 0 and len(wreadings) > 0:
                new_writings = _combine_writings(writings, wreadings)
            elif len(readings) > 0 and len(wwritings) > 0:
                new_writings = _combine_writings(readings, wwritings)
            else:
                new_writings = _combine_writings(readings + writings, wreadings + wwritings)

            readings = new_readings
            writings = new_writings

        return writings + readings

class NumberCombine(BaseCombine):

    def __init__(
        self,
        exceptions: Optional[Dict[int, List[str]]]=None,
        hide_one: bool=False
    ) -> None:
        self._exceptions = exceptions or {}
        self._hide_one = hide_one

    def __call__(self, words: Iterable[BaseWord]) -> List[Writing]:
        number, word = words
        if not isinstance(number, SupportsInt):
            raise ValueError
        value = int(number)

        if self._hide_one and value == 1:
            return word.writings

        writings = _combine_writings(
            number.writings,
            word.writings,
            lambda x, y: not isinstance(x, Reading) and not isinstance(y, Reading)
        )
        if value in self._exceptions:
            writings.extend([Reading(reading) for reading in self._exceptions[value]])
        else:
            writings.extend(_combine_writings(
                number.writings,
                word.writings,
                lambda x, y: isinstance(x, Reading) and isinstance(y, Reading)
            ))

        return writings

class TsuCombine(BaseCombine):

    def __init__(self, exceptions: Optional[Dict[int, List[str]]]=None) -> None:
        self._exceptions = exceptions or {}

    def __call__(self, words: Iterable[BaseWord]) -> List[Writing]:
        number, word = words
        if not isinstance(number, SupportsInt):
            raise ValueError

        writings = []
        for wri1 in number.writings:
            for wri2 in word.writings:
                if not isinstance(wri1, Reading):
                    writings.append(wri1 + wri2)
        value = int(number)
        if value in self._exceptions:
            writings.extend([Reading(reading) for reading in self._exceptions[value]])

        return writings

def _build_h_exceptions(
    dakuten: str,
    handakuten: str
) -> Dict[str, Callable[[str, str], List[str]]]:

    return {
        'いち': lambda x, y: [x[:-1] + 'っ' + handakuten + y[1:]],
        'さん': lambda x, y: [x + dakuten + y[1:]],
        'ろく': lambda x, y: [x[:-1] + 'っ' + handakuten + y[1:]],
        'はち': lambda x, y: [x[:-1] + 'っ' + handakuten + y[1:], x + y],
        'じゅう': lambda x, y: [x[:-1] + 'っ' + handakuten + y[1:]],
    }

def _build_k_exceptions(
    kana: str,
) -> Dict[str, Callable[[str, str], List[str]]]:

    return {
        'いち': lambda x, y: [x[:-1] + 'っ' + kana + y[1:]],
        'ろく': lambda x, y: [x[:-1] + 'っ' + kana + y[1:]],
        'はち': lambda x, y: [x[:-1] + 'っ' + kana + y[1:], x + y],
        'じゅう': lambda x, y: [x[:-1] + 'っ' + kana + y[1:]],
    }

class StandardCombine(BaseCombine):

    __EXCEPTIONS: Dict[str, Dict[str, Callable[[str, str], List[str]]]] = {
        'ふ': {
            'いち': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'さん': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'ろく': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'はち': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
            'じゅう': lambda x, y: [x[:-1] + 'っぷ' + y[1:]],
        },
        'ひ': _build_h_exceptions('び', 'ぴ'),
        'ほ': _build_h_exceptions('ぼ', 'ぽ'),
        'か': _build_k_exceptions('か'),
        'け': _build_k_exceptions('け'),
        'こ': _build_k_exceptions('こ'),
        'さ': {
            'いち': lambda x, y: [x[:-1] + 'っさ' + y[1:]],
            'はち': lambda x, y: [x[:-1] + 'っさ' + y[1:], x + y],
            'じゅう': lambda x, y: [x[:-1] + 'っさ' + y[1:]],
        },
    }

    def _find_func(self, writing1: str, writing2: str) -> Optional[Callable[[str, str], List[str]]]:
        if writing2[0] not in self.__EXCEPTIONS:
            return None

        exceptions = self.__EXCEPTIONS[writing2[0]]

        if writing1[-3:] in exceptions:
            return exceptions[writing1[-3:]]
        if writing1[-2:] in exceptions:
            return exceptions[writing1[-2:]]
        return None

    def __call__(self, words: Iterable[BaseWord]) -> List[Writing]:

        number, counter = words

        writings: List[Writing] = []

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

        return writings
