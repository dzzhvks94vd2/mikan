import pytest
from mikan import Counter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一本', '1本', 'いっぽん'),
        (2, '二本', '2本', 'にほん'),
        (3, '三本', '3本', 'さんぼん'),
        (6, '六本', '6本', 'ろっぽん'),
        (8, '八本', '8本', 'はっぽん'),
        (8, '八本', '8本', 'はちほん'),
        (11, '十一本', '11本', 'じゅういっぽん'),
        (20, '二十本', '20本', 'にじゅっぽん'),
    ]
)
def test_hon_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + Counter('本', 'ほん')
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
