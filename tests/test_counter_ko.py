import pytest
from mikan import Counter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一個', '1個', 'いっこ'),
        (6, '六個', '6個', 'ろっこ'),
        (8, '八個', '8個', 'はっこ'),
        (8, '八個', '8個', 'はちこ'),
        (10, '十個', '10個', 'じゅっこ'),
    ]
)
def test_hon_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + Counter('個', 'こ')
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
