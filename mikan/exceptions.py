class MikanException(Exception):
    """Generic Mikan exception"""

class ConversionError(MikanException, ValueError):
    """Cannot convert a string"""

class InvalidConjugation(MikanException):
    """Cannot conjugate with the given parameters"""
