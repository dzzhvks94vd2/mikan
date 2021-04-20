class MikanException(Exception):
    """Generic Mikan exception"""

class ConversionError(MikanException, ValueError):
    """Cannot convert a string"""
