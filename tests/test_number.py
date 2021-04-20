import pytest
from mikan import Number

@pytest.mark.parametrize(
    "digits,expkana,expkanji",
    [
        (1, 'いち', '一'),
        (2, 'に', '二'),
        (3, 'さん', '三'),
        (4, 'よん', '四'),
        (5, 'ご', '五'),
        (6, 'ろく', '六'),
        (7, 'なな', '七'),
        (8, 'はち', '八'),
        (9, 'きゅう', '九'),
        (10, 'じゅう', '十'),
        (600, 'ろっぴゃく', '六百'),
        (800, 'はっぴゃく', '八百'),
        (1110, 'せんひゃくじゅう', '千百十'),
        (1234, 'せんにひゃくさんじゅうよん', '千二百三十四'),
        (1334, 'せんさんびゃくさんじゅうよん', '千三百三十四'),
        (3000, 'さんぜん', '三千'),
        (8000, 'はっせん', '八千'),
    ]
)
def test_number(digits, expkana, expkanji):

    n = Number(digits)
    assert expkana in n.readings
    assert expkanji in n.writings
    assert str(digits) in n.writings

    n = Number(expkanji)
    assert str(digits) in n.writings

@pytest.mark.parametrize(
    "kanji",
    [
        ('',),
        None,
        '',
        '一二',
        '木',
    ]
)
def test_not_number_kanji(kanji):

    with pytest.raises(ValueError):
        Number(kanji)

def test_number_equal():
    num1 = Number(42)
    num2 = Number('四十二')

    assert num1 == num2
