from enum import Enum
from typing import Dict, Callable, Union, List
from mikan.base import BaseWord
from mikan.word import Word
from mikan.writing import Writing

__all__ = ['AdjectiveForm', 'IAdjective', 'YoiAdjective']

AdjectiveForm = Enum('AdjectiveForm', (
    'PRESENT',
    'PAST',
    'TE_FORM',
    'ADVERB',
))

class IAdjective(Word):

    _ENDINGS: Dict[AdjectiveForm, Dict[bool, Callable[[BaseWord], BaseWord]]] = {
        AdjectiveForm.PRESENT: {
            False: lambda x: x + 'い',
            True: lambda x: x + 'くない',
        },
        AdjectiveForm.PAST: {
            False: lambda x: x + 'かった',
            True: lambda x: x + 'くなかった',
        },
        AdjectiveForm.TE_FORM: {
            False: lambda x: x + 'くて',
        },
        AdjectiveForm.ADVERB: {
            False: lambda x: x + 'く',
        },
    }

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        super().__init__(*args)

        base, ending = self.split_okurigana(1)

        if ending != 'い':
            raise ValueError('This is not an i adjective')

        self._stem = base

    def conjugate(
        self,
        forms: Union[AdjectiveForm, List[AdjectiveForm]],
        negative: bool=False
    ) -> BaseWord:

        if isinstance(forms, AdjectiveForm):
            current = forms
        else:
            current = forms[0]

        return self._ENDINGS[current][negative](self._stem)

class YoiAdjective(IAdjective):

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        super().__init__(*args)

        base, ending = self.split_okurigana(2)

        if not ending in ('良い', 'よい'):
            raise ValueError('This is not a yoi adjective')

        self._ii = base + Word('良い', 'いい')

    def conjugate(
        self,
        forms: Union[AdjectiveForm, List[AdjectiveForm]],
        negative: bool=False
    ) -> BaseWord:

        if isinstance(forms, AdjectiveForm):
            current = forms
        else:
            current = forms[0]

        if (current == AdjectiveForm.PRESENT) and not negative:
            return self._ii

        return super().conjugate(current, negative)

    @property
    def writings(self) -> List[Writing]:

        return super().writings + self._ii.writings
