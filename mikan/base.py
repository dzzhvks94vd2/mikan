import abc
from typing import List, Union, cast

from mikan.reading import Reading
from mikan.writing import Writing

class BaseWord(abc.ABC):

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseWord):
            return False
        word: BaseWord = other
        return set(self.writings) == set(word.writings)

    @property
    @abc.abstractmethod
    def writings(self) -> List[Writing]:
        pass

    @property
    def readings(self) -> List[Reading]:
        return cast(List[Reading], list(filter(lambda x: isinstance(x, Reading), self.writings)))

    @abc.abstractmethod
    def __add__(self, other: Union[str, 'BaseWord']) -> 'BaseWord':
        pass

    def __str__(self) -> str:
        return str(self.writings[0])
