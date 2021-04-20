import pytest
from mikan import Counter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一分', '1分', 'いっぷん'),
        (20, '二十分', '20分', 'にじゅっぷん')
    ]
)
def test_minute_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + Counter('分', 'ふん')
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
