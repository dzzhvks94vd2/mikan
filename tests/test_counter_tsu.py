import pytest
from mikan import TsuCounter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一つ', '1つ', 'ひとつ'),
        (2, '二つ', '2つ', 'ふたつ'),
        (3, '三つ', '3つ', 'みっつ'),
        (4, '四つ', '4つ', 'よっつ'),
        (5, '五つ', '5つ', 'いつつ'),
        (6, '六つ', '6つ', 'むっつ'),
        (7, '七つ', '7つ', 'ななつ'),
        (8, '八つ', '8つ', 'やっつ'),
        (9, '九つ', '9つ', 'ここのつ'),
    ]
)
def test_tsu_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + TsuCounter()
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
