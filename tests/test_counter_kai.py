import pytest
from mikan import Counter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一回', '1回', 'いっかい'),
        (6, '六回', '6回', 'ろっかい'),
        (8, '八回', '8回', 'はっかい'),
        (8, '八回', '8回', 'はちかい'),
        (10, '十回', '10回', 'じゅっかい'),
    ]
)
def test_hon_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + Counter('回', 'かい')
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
