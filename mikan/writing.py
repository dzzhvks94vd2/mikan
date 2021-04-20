from typing import List, Type

__all__ = ['Writing']

class Writing(str):

    subclasses: List[Type['Writing']] = []

    def __init_subclass__(cls) -> None:
        cls.subclasses.append(cls)

    @classmethod
    def create(cls, something: object) -> 'Writing':
        string = str(something)
        for subclass in cls.subclasses:
            try:
                writing = subclass(string)
                return writing
            except ValueError:
                pass
        return Writing(string)

    def __add__(self, other: object) -> 'Writing':
        return Writing.create(str(self) + str(other))
