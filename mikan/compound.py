from typing import Iterable, List, Type, Union, Sequence, Optional
from mikan.base import BaseWord
from mikan.combine import BaseCombine, DefaultCombine
from mikan.writing import Writing
import mikan.word

__all__ = ['Compound']

class Compound(BaseWord):

    subclasses: List[Type['Compound']] = []

    def __init_subclass__(cls) -> None:
        cls.subclasses.append(cls)

    @classmethod
    def create(
        cls,
        words: Sequence[BaseWord],
        writings: Optional[Sequence[Union[str, Writing]]]=None
    ) -> 'Compound':

        compound = None
        for sub in cls.subclasses:
            try:
                compound = sub(words, writings=writings)
            except ValueError:
                pass

        if compound is None:
            compound = Compound(words, writings=writings)

        return compound

    def __init__(
        self,
        words: Iterable[BaseWord],
        writings: Optional[Sequence[Union[str, Writing]]]=None,
        combine: Optional[BaseCombine]=None
    ) -> None:

        super().__init__()

        self._words = list(words)
        self._writings = None
        if writings is not None:
            self._writings = [Writing.create(writing) for writing in writings]
        self._combine = combine or DefaultCombine()

    def __add__(self, other: Union[str, BaseWord]) -> BaseWord:
        word = other if isinstance(other, BaseWord) else mikan.word.Word(other)
        return Compound.create((self, word))

    @property
    def writings(self) -> List[Writing]:
        if self._writings is not None:
            return self._writings

        return self._combine(self._words)
