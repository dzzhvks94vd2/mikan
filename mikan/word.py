from typing import Tuple, List, Union

from mikan.base import BaseWord
from mikan.writing import Writing

import mikan.compound

__all__ = ['Word']

class Word(BaseWord):

    def __init__(
        self,
        *args: Union[str, Writing, BaseWord]
    ) -> None:

        super().__init__()

        self._writings: List[Writing] = []
        for wri in args:
            if isinstance(wri, BaseWord):
                self._writings.extend(wri.writings)
            else:
                self._writings.append(Writing.create(wri))

        if len(self._writings) == 0:
            raise ValueError('No writing provided')

    def __add__(self, other: Union[str, BaseWord]) -> BaseWord:
        if isinstance(other, BaseWord):
            return mikan.compound.Compound((self, other))
        writings = [writing + other for writing in self._writings]
        return Word(*writings)

    @property
    def writings(self) -> List[Writing]:
        return self._writings

    def split_okurigana(self, count: int) -> Tuple['Word', str]:
        okurigana = None
        writings = []

        for writing in self._writings:
            stem, oku = writing[:-count], writing[-count:]
            if okurigana is None:
                okurigana = oku
            elif okurigana != oku:
                raise ValueError('Not okurigana')
            writings.append(Writing.create(stem))

        if okurigana is None:
            # this should not be possible, but...
            raise ValueError('Not okurigana')

        return Word(*writings), okurigana
