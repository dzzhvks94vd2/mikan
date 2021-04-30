from typing import Dict, Iterator, List, Optional, Sequence, Tuple, Union
from mikan.base import BaseWord
from mikan.word import Word
from mikan.writing import Writing
from mikan.reading import Reading
from mikan.compound import Compound

__all__ = ['Number']

class Digit(Word):

    DIGITS: Dict[int, List[str]] = {
        1: ['一', 'いち'],
        2: ['二', 'に'],
        3: ['三', 'さん'],
        4: ['四', 'よん'],
        5: ['五', 'ご'],
        6: ['六', 'ろく'],
        7: ['七', 'なな'],
        8: ['八', 'はち'],
        9: ['九', 'きゅう'],
    }

    def __init__(self, digit: int) -> None:
        if not 0 <= digit < 10:
            raise ValueError

        self._digit = digit
        writings = self.DIGITS[digit]

        super().__init__(*writings)

    def __int__(self) -> int:
        return self._digit

class Juu(Word):
    def __init__(self) -> None:
        super().__init__('十', 'じゅう')

class JuuCompound(Compound):
    def __init__(self, words: Tuple[Digit, Juu], writings: Optional[List[Writing]]=None) -> None:
        if (
            (len(words) != 2) or
            not (isinstance(words[0], Digit) and isinstance(words[1], Juu))
        ):
            raise ValueError

        digit, juu = words

        if int(digit) == 1:
            writings = juu.writings
        else:
            writings = self._combine_writings(
                digit.writings,
                juu.writings,
                lambda x, y: isinstance(x, Reading) == isinstance(y, Reading)
            )

        super().__init__(words, writings)

class Hyaku(Word):
    def __init__(self) -> None:
        super().__init__('百', 'ひゃく')

class HyakuCompound(Compound):
    def __init__(self, words: Tuple[Digit, Hyaku], writings: Optional[List[Writing]]=None) -> None:
        if (
            (len(words) != 2) or
            not (isinstance(words[0], Digit) and isinstance(words[1], Hyaku))
        ):
            raise ValueError

        digit, hyaku = words

        if int(digit) == 1:
            writings = hyaku.writings
        elif int(digit) == 3:
            writings = [Writing('三百'), Reading('さんびゃく')]
        elif int(digit) == 6:
            writings = [Writing('六百'), Reading('ろっぴゃく')]
        elif int(digit) == 8:
            writings = [Writing('八百'), Reading('はっぴゃく')]
        else:
            writings = self._combine_writings(
                digit.writings,
                hyaku.writings,
                lambda x, y: isinstance(x, Reading) == isinstance(y, Reading)
            )

        super().__init__(words, writings)

class Sen(Word):
    def __init__(self) -> None:
        super().__init__('千', 'せん')

class SenCompound(Compound):
    def __init__(self, words: Tuple[Digit, Sen], writings: Optional[List[Writing]]=None) -> None:
        if (
            (len(words) != 2) or
            not (isinstance(words[0], Digit) and isinstance(words[1], Sen))
        ):
            raise ValueError

        digit, sen = words

        if int(digit) == 1:
            writings = sen.writings
        elif int(digit) == 3:
            writings = [Writing('三千'), Reading('さんぜん')]
        elif int(digit) == 8:
            writings = [Writing('八千'), Reading('はっせん')]
        else:
            writings = self._combine_writings(
                digit.writings,
                sen.writings,
                lambda x, y: isinstance(x, Reading) == isinstance(y, Reading)
            )

        super().__init__(words, writings)

class MyriadCompound(Compound):
    def __init__(self, words: Sequence[BaseWord], writings: Optional[List[Writing]]=None) -> None:
        if (len(words) == 0) or (len(words) > 4):
            raise ValueError

        digit = None
        juu = None
        hyaku = None
        sen = None

        for word in words:
            if isinstance(word, Digit):
                if digit is not None:
                    raise ValueError
                digit = word
            elif isinstance(word, JuuCompound):
                if juu is not None:
                    raise ValueError
                juu = word
            elif isinstance(word, HyakuCompound):
                if hyaku is not None:
                    raise ValueError
                hyaku = word
            elif isinstance(word, SenCompound):
                if sen is not None:
                    raise ValueError
                sen = word
            else:
                raise ValueError

        super().__init__([x for x in [sen, hyaku, juu, digit] if x is not None])

class Man(Word):
    def __init__(self) -> None:
        super().__init__('万', 'まん')

class ManCompound(Compound):
    def __init__(self, words: List[Word], writings: Optional[List[Writing]]=None) -> None:
        if (
            (len(words) != 2) or
            not (isinstance(words[0], MyriadCompound) and isinstance(words[1], Man))
        ):
            raise ValueError

        myriad, man = words

        writings = self._combine_writings(
            myriad.writings,
            man.writings,
            lambda x, y: isinstance(x, Reading) == isinstance(y, Reading)
        )

        super().__init__(words, writings)

class Oku(Word):
    def __init__(self) -> None:
        super().__init__('億', 'おく')

class OkuCompound(Compound):
    def __init__(self, words: List[Word], writings: Optional[List[Writing]]=None) -> None:
        if (
            (len(words) != 2) or
            not (isinstance(words[0], MyriadCompound) and isinstance(words[1], Oku))
        ):
            raise ValueError

        myriad, oku = words

        writings = self._combine_writings(
            myriad.writings,
            oku.writings,
            lambda x, y: isinstance(x, Reading) == isinstance(y, Reading)
        )

        super().__init__(words, writings)

class Chou(Word):
    def __init__(self) -> None:
        super().__init__('兆', 'ちょう')

class ChouCompound(Compound):
    def __init__(self, words: List[Word], writings: Optional[List[Writing]]=None) -> None:
        if (
            (len(words) != 2) or
            not (isinstance(words[0], MyriadCompound) and isinstance(words[1], Chou))
        ):
            raise ValueError

        myriad, chou = words

        writings = self._combine_writings(
            myriad.writings,
            chou.writings,
            lambda x, y: isinstance(x, Reading) == isinstance(y, Reading)
        )

        super().__init__(words, writings)

class Kei(Word):
    def __init__(self) -> None:
        super().__init__('京', 'けい')

class KeiCompound(Compound):
    def __init__(self, words: List[Word], writings: Optional[List[Writing]]=None) -> None:
        if (
            (len(words) != 2) or
            not (isinstance(words[0], MyriadCompound) and isinstance(words[1], Kei))
        ):
            raise ValueError

        myriad, kei = words

        writings = self._combine_writings(
            myriad.writings,
            kei.writings,
            lambda x, y: isinstance(x, Reading) == isinstance(y, Reading)
        )

        super().__init__(words, writings)

class Number(Word):
    DIGITS = [Juu(), Hyaku(), Sen()]
    MYRIADS = [Man(), Oku(), Chou(), Kei()]

    @staticmethod
    def _myriad_generator(num: int) -> Iterator[int]:
        while num:
            yield num % 10000
            num //= 10000

    @staticmethod
    def _digit_generator(num: int) -> Iterator[int]:
        while num:
            yield num % 10
            num //= 10

    @staticmethod
    def _from_myriad(num: int) -> List[BaseWord]:
        digits = []
        for digit_index, value in enumerate(Number._digit_generator(num)):
            if value == 0:
                continue
            digit = Digit(value)
            digits.append(
                digit if digit_index == 0 else digit + Number.DIGITS[digit_index - 1]
            )
        return digits

    @staticmethod
    def _from_digits(num: int) -> Compound:
        myriad_digits = []
        for myriad_index, myriad in enumerate(Number._myriad_generator(num)):
            digits = Number._from_myriad(myriad)
            if len(digits) == 0:
                continue
            myriad_digit = MyriadCompound(digits)
            myriad_digits.append(
                myriad_digit if myriad_index == 0 else myriad_digit + Number.MYRIADS[myriad_index - 1]
            )
        return Compound(reversed(myriad_digits))

    @staticmethod
    def _from_kanji(kanji: str) -> int:

        if not kanji:
            raise ValueError('Cannot decode kanji into number')

        revdigits = {writings[0]: digit for digit, writings in Digit.DIGITS.items()}
        revpos = {str(counter): index + 1 for index, counter in enumerate(Number.DIGITS)}
        revmyriad = {str(counter): index + 1 for index, counter in enumerate(Number.MYRIADS)}

        number = 0
        total = 0
        state = 2
        pos = 0
        myriad = 0
        remaining = kanji
        while remaining:
            remaining, current = remaining[:-1], remaining[-1]
            if state == 1:
                if current in revpos:
                    pos = revpos[current]
                    state = 2
                elif current in revmyriad:
                    total += number * 10000 ** myriad
                    number = 0
                    pos = 0
                    myriad = revmyriad[current]
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
                elif current in revmyriad:
                    total += number * 10000 ** myriad
                    number = 0
                    pos = 0
                    myriad = revmyriad[current]
                else:
                    raise ValueError('Cannot decode kanji into number')

        if state == 2:
            number += 10 ** pos

        total += number * 10000 ** myriad

        return total

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
        word = self._from_digits(digits)
        super().__init__(word)

    def __int__(self) -> int:
        return self._digits

    @property
    def writings(self) -> List[Writing]:
        return [Writing.create(self._digits)] + super().writings
