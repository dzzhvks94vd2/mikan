from mikan.writing import Writing
from mikan.utils import is_kana

__all__ = ['Reading']

class Reading(Writing):

    def __new__(cls, string: str) -> 'Reading':
        if not is_kana(string):
            raise ValueError
        return super().__new__(cls, string)
