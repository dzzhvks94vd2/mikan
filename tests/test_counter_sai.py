import pytest
from mikan import Counter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一才', '1才', 'いっさい'),
        (8, '八才', '8才', 'はっさい'),
        (8, '八才', '8才', 'はちさい'),
        (10, '十才', '10才', 'じゅっさい'),
    ]
)
def test_hon_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + Counter('才', 'さい')
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
