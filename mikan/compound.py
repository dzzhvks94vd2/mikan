from typing import List, Type, Union, Callable, Sequence, Optional
from mikan.base import BaseWord
from mikan.writing import Writing
import mikan.word

__all__ = ['Compound']

class CompoundBase:

    subclasses: List[Type['CompoundBase']] = []

    def __init_subclass__(cls) -> None:
        cls.subclasses.append(cls)

    def __init__(
        self,
        words: Sequence[BaseWord],
        writings: Optional[Sequence[Union[str, Writing]]]=None
    ) -> None:

        super().__init__()

        self._words = list(words)
        self._writings = None
        if writings is not None:
            self._writings = [Writing.create(writing) for writing in writings]

    @property
    def writings(self) -> List[Writing]:
        if self._writings is not None:
            return self._writings

        writings = [Writing.create('')]
        for word in self._words:
            newwritings = []
            for wwriting in word.writings:
                for writing in writings:
                    newwritings.append(writing + wwriting)
            writings = newwritings
        return writings

    @staticmethod
    def _combine_writings(
        writings1: List[Writing],
        writings2: List[Writing],
        testfunc: Callable[[Writing, Writing], bool]
    ) -> List[Writing]:

        writings = []
        for writing1 in writings1:
            for writing2 in writings2:
                if testfunc(writing1, writing2):
                    writings.append(writing1 + writing2)
        return writings

class Compound(BaseWord):

    def __init__(
        self,
        words: Sequence[BaseWord],
        writings: Optional[Sequence[Union[str, Writing]]]=None
    ) -> None:

        super().__init__()

        compound = None
        for cls in CompoundBase.subclasses:
            try:
                compound = cls(words, writings=writings)
            except ValueError:
                pass

        if compound is None:
            compound = CompoundBase(words, writings=writings)

        self._compound = compound

    @property
    def writings(self) -> List[Writing]:
        return self._compound.writings

    def __add__(self, other: Union[str, BaseWord]) -> BaseWord:
        word = other if isinstance(other, BaseWord) else mikan.word.Word(other)
        return Compound((self, word))
