from typing import Dict, Callable, Union, List
from mikan.base import BaseWord, Form
from mikan.word import Word
from mikan.writing import Writing

__all__ = ['IAdjective', 'YoiAdjective']

class IAdjective(Word):

    _ENDINGS: Dict[Form, Dict[bool, Callable[[BaseWord], BaseWord]]] = {
        Form.PRESENT: {
            False: lambda x: x + 'い',
            True: lambda x: x + 'くない',
        },
        Form.PAST: {
            False: lambda x: x + 'かった',
            True: lambda x: x + 'くなかった',
        },
        Form.TE: {
            False: lambda x: x + 'くて',
        },
        Form.ADVERB: {
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
        forms: Union[Form, List[Form]],
        negative: bool=False
    ) -> BaseWord:

        if isinstance(forms, Form):
            current = forms
        else:
            current = forms[0]

        return self._ENDINGS[current][negative](self._stem)

class YoiAdjective(IAdjective):

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        word = Word(*args)
        base, ending = word.split_okurigana(2)

        if not ending in ('良い', 'よい', 'いい'):
            raise ValueError('This is not a yoi adjective')

        super().__init__(base + Word('良い', 'よい'))

        self._ii = base + Word('良い', 'いい')

    def conjugate(
        self,
        forms: Union[Form, List[Form]],
        negative: bool=False
    ) -> BaseWord:

        if isinstance(forms, Form):
            current = forms
        else:
            current = forms[0]

        if (current == Form.PRESENT) and not negative:
            return self._ii

        return super().conjugate(current, negative)

    @property
    def writings(self) -> List[Writing]:

        return super().writings + self._ii.writings
