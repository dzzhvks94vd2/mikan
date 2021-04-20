from mikan.writing import Writing
import mikan.utils as utils

__all__ = ['Reading']

class Reading(Writing):

    def __new__(cls, string: str) -> 'Reading':
        if not utils.is_kana(string):
            raise ValueError
        return super().__new__(cls, string)
