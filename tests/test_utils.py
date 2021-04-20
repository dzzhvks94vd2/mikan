import pytest
from mikan.utils import is_hiragana, is_katakana, to_hiragana, to_katakana

@pytest.mark.parametrize(
    "string,expected",
    [
        ('よろしく', True),
        ('はぁ', True),
        ('あひゞき', True),
        (chr(0x3040), False),
        (chr(0x309F), False),
    ]
)
def test_is_hiragana(string, expected):
    assert is_hiragana(string) == expected

@pytest.mark.parametrize(
    "string,expected",
    [
        ('シャツ', True),
        ('ファクス', True),
        ('ジャン゠ポール', True),
        ('サヾエ', True),
        ('よろしく', False),
        (chr(0x3009), False),
        (chr(0x30FF), False),
    ]
)
def test_is_katakana(string, expected):
    assert is_katakana(string) == expected

@pytest.mark.parametrize(
    "hiragana,katakana",
    [
        ("ねこ", "ネコ"),
    ]
)
def test_conversion(hiragana, katakana):
    assert to_hiragana(katakana) == hiragana
    assert to_katakana(hiragana) == katakana
