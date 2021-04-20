from typing import Dict, Tuple, Any, Union, List
from mikan.base import BaseWord
from mikan.word import Word
from mikan.writing import Writing

__all__ = ['Number']

class Number(Word):
    DIGITS: Dict[int, Dict[str, str]] = {
        1: {'kana': 'いち', 'kanji': '一'},
        2: {'kana': 'に', 'kanji': '二'},
        3: {'kana': 'さん', 'kanji': '三'},
        4: {'kana': 'よん', 'kanji': '四'},
        5: {'kana': 'ご', 'kanji': '五'},
        6: {'kana': 'ろく', 'kanji': '六'},
        7: {'kana': 'なな', 'kanji': '七'},
        8: {'kana': 'はち', 'kanji': '八'},
        9: {'kana': 'きゅう', 'kanji': '九'},
    }

    POS: Dict[int, Dict[str, Any]] = {
        1: {'kana': 'じゅう', 'kanji': '十'},
        2: {'kana': 'ひゃく', 'kanji': '百', 'exceptions': {3: 'さんびゃく', 6: 'ろっぴゃく', 8: 'はっぴゃく'}},
        3: {'kana': 'せん', 'kanji': '千', 'exceptions': {3: 'さんぜん', 8: 'はっせん'}},
    }

    def __init__(
        self,
        *args: Union[int, str, Writing, BaseWord]
    ) -> None:

        digits = None
        for wri in args:
            if isinstance(wri, int):
                digits = wri
            else:
                try:
                    digits = self._from_kanji(str(wri))
                except ValueError:
                    pass

        if digits is None:
            raise ValueError('Not a number')

        self._digits = digits
        writings = self._from_digits(digits)
        super().__init__(*writings)

    @staticmethod
    def _from_digits(num: int, pos: int=0) -> Tuple[str, str]:

        if pos != 0 and pos not in Number.POS:
            raise IndexError
        left = num // 10
        right = num % 10
        lkana = ''
        rkana = ''
        lkanji = ''
        rkanji = ''
        if pos == 0:
            if right > 0:
                rkana = Number.DIGITS[right]['kana']
                rkanji = Number.DIGITS[right]['kanji']
        elif right in Number.POS[pos].get('exceptions', {}):
            rkana = Number.POS[pos]['exceptions'][right]
            rkanji = Number.DIGITS[right]['kanji'] + Number.POS[pos]['kanji']
        elif right > 1:
            rkana = Number.DIGITS[right]['kana'] + Number.POS[pos]['kana']
            rkanji = Number.DIGITS[right]['kanji'] + Number.POS[pos]['kanji']
        elif right == 1:
            rkana = Number.POS[pos]['kana']
            rkanji = Number.POS[pos]['kanji']
        if left > 0:
            lkana, lkanji = Number._from_digits(left, pos + 1)
        return lkana + rkana, lkanji + rkanji

    @staticmethod
    def _from_kanji(kanji: str) -> int:

        if not kanji:
            raise ValueError('Cannot decode kanji into number')

        revdigits = {word['kanji']: digit for digit, word in Number.DIGITS.items()}
        revpos = {word['kanji']: digit for digit, word in Number.POS.items()}

        number = 0
        state = 2
        pos = 0
        remaining = kanji
        while remaining:
            remaining, current = remaining[:-1], remaining[-1]
            if state == 1:
                if current in revpos:
                    pos = revpos[current]
                    state = 2
                else:
                    raise ValueError('Cannot decode kanji into number')
            elif state == 2:
                if current in revdigits:
                    number += revdigits[current] * 10 ** pos
                    state = 1
                elif current in revpos:
                    if pos:
                        number += 10 ** pos
                    pos = revpos[current]
                    state = 2
                else:
                    raise ValueError('Cannot decode kanji into number')

        if state == 2:
            number += 10 ** pos

        return number

    def __int__(self) -> int:
        return self._digits

    @property
    def writings(self) -> List[Writing]:
        return [Writing.create(self._digits)] + super().writings
